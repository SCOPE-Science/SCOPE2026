"""Independent exact finite checks for majority dynamics on a chorded ring.
No external dependencies. Run: python verify_chord_majority.py
"""
from math import comb

def fib(n):
    a, b = 0, 1
    for _ in range(n): a, b = b, a+b
    return a

def path_counts(length):
    """Counts of stable arc interiors, by prescribed equal/unequal end bits."""
    assert length >= 2
    if length == 2: return 1,0
    interior = length-1
    same = diff = 0
    for runs in range(1,interior//2 + 1):
        c = comb(interior-runs-1,runs-1)
        if runs % 2: same += c
        else: diff += c
    return same,diff

def prediction(n,d):
    assert n>=4 and 2<=d<=n-2
    m=n-d
    u,v=path_counts(d)
    U,V=path_counts(m)
    stable_u=2*(u*U+v*V)
    active = (2*(U+V) if d%2 else 0)+(2*(u+v) if m%2 else 0)
    global_alternating=int(n%2==0)
    return stable_u+active+global_alternating,(stable_u,active,global_alternating)

def classify(n,d):
    neighbors=[]
    for i in range(n):
        nbrs={(i-1)%n,(i+1)%n}
        if i==0:nbrs.add(d)
        elif i==d:nbrs.add(0)
        neighbors.append(tuple(nbrs))
    def update(x):
        out=0
        for i,adj in enumerate(neighbors):
            votes=sum((x>>j)&1 for j in adj)
            bit=int(2*votes>len(adj)) if 2*votes != len(adj) else (x>>i)&1
            out |= bit<<i
        return out
    fixed=0
    observed=[0,0,0]
    witnesses={}
    for x in range(1<<n):
        y=update(x)
        if y==x:
            fixed+=1
            continue
        if update(y)!=x or x>y:
            continue
        flips=x^y
        assert flips&1 and flips&(1<<d), ('endpoints-must-flip',n,d,x,y)
        arc1=all((flips>>i)&1 for i in range(1,d))
        arc2=all((flips>>i)&1 for i in range(d+1,n))
        assert all(((flips>>i)&1)==arc1 for i in range(1,d)),('partial-flip',n,d,x,y)
        assert all(((flips>>i)&1)==arc2 for i in range(d+1,n)),('partial-flip',n,d,x,y)
        typ=2 if arc1 and arc2 else 1 if arc1 or arc2 else 0
        observed[typ]+=1
        witnesses.setdefault(typ,(x,y))
    return fixed,tuple(observed),witnesses

if __name__=='__main__':
    num_instances=0
    num_states=0
    print('n,d | fixed, endpoint-only, one-arc, global | predicted')
    for n in range(4,15):
        for d in range(2,n-1):
            fixed,actual,wit=classify(n,d)
            total,expected=prediction(n,d)
            if actual != expected or sum(actual)!=total:
                raise AssertionError((n,d,actual,expected,total))
            # independent run compositions vs direct strings for each arc
            for ell in (d,n-d):
                u,v=path_counts(ell)
                same=diff=0
                for word in range(1<<(ell-1)):
                    bits=[(word>>i)&1 for i in range(ell-1)]
                    if ell!=2:
                        runs=[]; run=1
                        for j in range(1,len(bits)):
                            if bits[j]==bits[j-1]:run+=1
                            else:runs.append(run);run=1
                        runs.append(run)
                        if min(runs)<2:continue
                    if bits[0]==bits[-1]:same+=1
                    else:diff+=1
                if (same,diff)!=(2*u,2*v):raise AssertionError(('path-count',ell,same,diff,u,v))
            num_instances+=1
            num_states+=1<<n
            if n<=7: print(n,d,'|',(fixed,)+actual,'|',expected)
    print('VERIFIED parameter pairs:',num_instances)
    print('VERIFIED direct configurations:',num_states)
    print('VERIFIED path endpoint formulas and complete three-type classification on every pair')
    for n,d in [(5,2),(6,3),(9,3),(13,5),(14,7)]:
        print('EXAMPLE n,d',n,d,'formula',prediction(n,d))
