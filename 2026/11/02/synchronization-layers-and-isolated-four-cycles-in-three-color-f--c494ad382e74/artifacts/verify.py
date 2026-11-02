"""Exact standalone checks for three-color inhibitory oscillator dynamics on K(a,b).
Usage: python3 artifacts/verify.py
"""
from collections import defaultdict
from itertools import product
import csv
from pathlib import Path

C = (0, 1, 2)

def support_step(left, right):
    l_has_blink = 1 in left
    r_has_blink = 1 in right
    def local(s, other_blinks):
        return frozenset((2 if state == 2 and other_blinks else (state + 1) % 3) for state in s)
    return local(left, r_has_blink), local(right, l_has_blink)


def support_itinerary(l, r):
    seen = {}
    seq = []
    state = (frozenset(l), frozenset(r))
    while state not in seen:
        seen[state] = len(seq)
        seq.append(state)
        state = support_step(*state)
    tau = seen[state]
    cycle = seq[tau:]
    if len(cycle) == 2:
        assert set(len(a) for pair in cycle for a in pair) == {2}
        actual_period = 4
    else:
        assert len(cycle) in (1, 3)
        actual_period = 3
    return tau, actual_period, tuple(cycle)


def word_support(word):
    return frozenset(word)


def full_step(state, a):
    left, right = state[:a], state[a:]
    lb = 1 in left
    rb = 1 in right
    return tuple(2 if x == 2 and rb else (x+1) % 3 for x in left) + tuple(2 if x == 2 and lb else (x+1) % 3 for x in right)


def direct_itinerary(initial, a):
    seen = {}
    state = initial
    seq = []
    while state not in seen:
        seen[state] = len(seq)
        seq.append(state)
        state = full_step(state, a)
        assert len(seq) <= 25, (a, initial)
    return seen[state], len(seq)-seen[state]


def U(j, n):
    if j == 1: return 1
    if j == 2: return 2**n-2
    if j == 3: return 3**n-3*2**n+3
    raise ValueError

# Analytic closed time-polynomial coefficients in x=U2(a), y=U2(b),
# u=U3(a), v=U3(b). These expressions are not obtained by trajectory code.
def closed_layers(a, b):
    x, y, u, v = U(2,a), U(2,b), U(3,a), U(3,b)
    return {
        0:3 + u + v + 2*x*y,
        1:2 + x+y + x*y,
        2:2 + x+y + 3*x*y+x*v+u*y+u*v,
        3:2 + x+y + x*y,
        4:x+y,
        5:3*(x+y)+u+v+2*x*y+x*v+u*y,
        6:2*(x+y)+u+v+x*v+u*y,
    }


def verify_support():
    masks = [frozenset(i for i in C if mask & (1 << i)) for mask in range(1, 8)]
    coeff = defaultdict(int)
    rows = []
    for ls,rs in product(masks, repeat=2):
        t,p,cyc=support_itinerary(ls,rs)
        coeff[(t,p,len(ls),len(rs))] +=1
        rows.append((sum(1<<i for i in ls), sum(1<<i for i in rs),t,p))
    assert len(rows) == len(set((r[0], r[1]) for r in rows)) == 49
    certificate = Path(__file__).with_name('support_pairs.csv')
    if certificate.exists():
        with certificate.open(newline='',encoding='utf-8') as h:
            recorded=list(csv.DictReader(h))
        assert len(recorded)==49
        for a,b,t,p in rows:
            found=next(x for x in recorded if int(x['left_support_mask'])==a and int(x['right_support_mask'])==b)
            assert int(found['first_periodic_entry'])==t and int(found['least_period'])==p
            l=frozenset(i for i in C if a & (1<<i))
            r=frozenset(i for i in C if b & (1<<i))
            nl,nr=support_step(l,r)
            assert (int(found['next_left_mask']),int(found['next_right_mask'])) == (sum(1<<i for i in nl),sum(1<<i for i in nr))
    assert max(r[2] for r in rows) == 6
    assert sorted(set(r[3] for r in rows)) == [3,4]
    assert sum(1 for r in rows if r[3] == 4) == 2
    for a in range(1,9):
        for b in range(1,9):
            c=defaultdict(int)
            for ls,rs in product(masks, repeat=2):
                t,p,_=support_itinerary(ls,rs)
                c[t] += U(len(ls),a)*U(len(rs),b)
            assert c == closed_layers(a,b), (a,b,c,closed_layers(a,b))
            assert sum(c.values()) == 3**(a+b)
    return rows


def verify_labelled():
    total = 0
    sizes = [(a,b) for a in range(1,5) for b in range(1,5)] + [
        (1,6),(1,7),(1,8),(2,6),(2,7),(3,5),(3,6),(4,5),(5,5)]
    for a,b in sizes:
        count=defaultdict(int)
        for word in product(C,repeat=a+b):
            t,p=direct_itinerary(word,a)
            ts,ps,_=support_itinerary(word_support(word[:a]),word_support(word[a:]))
            assert (t,p)==(ts,ps), (a,b,word,t,p,ts,ps)
            count[t]+=1
        assert dict(count) == {k:v for k,v in closed_layers(a,b).items() if v > 0}, (a,b,count,closed_layers(a,b))
        x,y,u,v=U(2,a),U(2,b),U(3,a),U(3,b)
        assert sum(c for t,c in count.items() if t==0)==3+u+v+2*x*y
        total+=3**(a+b)
    return sizes,total


def main():
    rows=verify_support()
    sizes,total=verify_labelled()
    print('SUPPORT_STATES',len(rows),'ALL_49_CHECKED')
    print('LABELLED_GRAPH_CASES',len(sizes),'LABELLED_STATES',total)
    for a,b in [(1,1),(1,3),(2,2),(2,3),(3,3),(3,4),(4,4)]:
        print('LAYER_COUNTS',a,b,','.join(map(str,(closed_layers(a,b)[t] for t in range(7)))))
    print('FIREFLY_BICLIQUE_EXACT_VERIFY_OK')

if __name__=='__main__':main()
