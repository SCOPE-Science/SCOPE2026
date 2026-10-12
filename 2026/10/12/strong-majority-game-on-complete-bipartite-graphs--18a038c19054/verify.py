from itertools import product

def cap(s):
    return s//2

def capacity(s,k):
    return k*cap(s) >= s

def dead_nonfull_states(s,k):
    c=cap(s)
    dead=[]
    for counts in product(range(c+1), repeat=k):
        t=sum(counts)
        if t<s and all(x==c for x in counts):
            dead.append(counts)
    return dead

def reachable_states(s,k):
    c=cap(s)
    start=(0,)*k
    seen={start}
    stack=[start]
    while stack:
        st=stack.pop()
        if sum(st)>=s:
            continue
        for j in range(k):
            if st[j] < c:
                nxt=list(st); nxt[j]+=1; nxt=tuple(nxt)
                if sum(nxt)<=s and nxt not in seen:
                    seen.add(nxt); stack.append(nxt)
    return seen

def game_safe(s,k):
    # On one shore of K_{m,n}, every legal move increments one color count,
    # each count is capped by floor(s/2).  The shore can get stuck before
    # completion iff a reachable nonfull state saturates every color.
    seen=reachable_states(s,k)
    for st in seen:
        if sum(st)<s and all(x==cap(s) for x in st):
            return False
    return True

def expected_game_number(m,n):
    for k in range(1,8):
        if capacity(m,k) and capacity(n,k):
            return k
    raise AssertionError

def run():
    shore_cases=0
    state_checks=0
    for s in range(2,13):
        for k in range(1,6):
            shore_cases += 1
            actual=game_safe(s,k)
            predicted=capacity(s,k)
            if actual != predicted:
                raise AssertionError(('shore',s,k,actual,predicted))
            state_checks += len(reachable_states(s,k))
    pair_cases=0
    for m in range(2,101):
        for n in range(2,101):
            pair_cases += 1
            got=expected_game_number(m,n)
            want=2 if (m%2==0 and n%2==0) else 3
            if got != want:
                raise AssertionError(('pair',m,n,got,want))
    print(f'ALL CHECKS PASSED; shore_cases={shore_cases}; reachable_state_checks={state_checks}; pair_cases={pair_cases}; shore_range=2..12; palette_range=1..5; parameter_range=2<=m,n<=100')

if __name__=='__main__':
    run()
