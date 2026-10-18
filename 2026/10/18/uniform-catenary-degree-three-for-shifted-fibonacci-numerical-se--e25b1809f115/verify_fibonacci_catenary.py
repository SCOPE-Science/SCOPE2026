"""Standalone exact integer checks for shifted-Fibonacci numerical semigroups.
Run: python3 verify_fibonacci_catenary.py
This is finite corroboration, not an infinite proof.
"""
from functools import lru_cache


def fibonacci(a):
    f = [0, 1]
    for _ in range(2, a + 1):
        f.append(f[-1] + f[-2])
    return f


def generators(a):
    f = fibonacci(a)
    return [f[a]] + [f[a] + f[i] for i in range(2, a)]


def normalize(a, initial):
    f = fibonacci(a)
    g = generators(a)
    v = list(initial)
    before = sum(x*y for x, y in zip(v, g))
    steps = 0
    while True:
        move = None
        if a == 3 and v[1] >= 2:
            move = ({1:2}, {0:3})
        else:
            for i in range(2, a-1):
                if v[i-1] and v[i]:
                    move = ({i-1:1, i:1}, {i+1:1,0:1} if i+1<a-1 else {0:3})
                    break
            if move is None:
                for i in range(2,a):
                    if v[i-1]<2: continue
                    if i==2:
                        move=({1:2},{2:1,0:1})
                    elif i==a-1:
                        move=({i-1:2},{0:2,max(2,a-3)-1:1})
                    elif i==3:
                        move=({i-1:2},{i:1,1:1})
                    else:
                        move=({i-1:2},{i:1,i-3:1})
                    break
        if move is None: break
        lhs, rhs = move
        old = v[:]
        for j, c in lhs.items():
            assert v[j]>=c
            v[j]-=c
        for j,c in rhs.items(): v[j]+=c
        assert sum(x*y for x,y in zip(v,g))==before, (a,old, v)
        common=sum(min(x,y) for x,y in zip(old,v))
        assert max(sum(old)-common,sum(v)-common)<=3
        steps+=1
        assert steps < 10000
    assert sum(x*y for x,y in zip(v,g))==before
    assert all(v[i]<=1 for i in range(1,len(v)))
    assert all(not(v[i] and v[i+1]) for i in range(1,len(v)-1))
    assert sum(v[i]*f[i+1] for i in range(1,len(v)))<f[a]
    return tuple(v),steps


def all_factorizations(a, n):
    g=generators(a)
    @lru_cache(None)
    def rec(r,j):
        if j==len(g)-1:
            return ((r//g[j],),) if r%g[j]==0 else ()
        return tuple((k,)+v for k in range(r//g[j]+1) for v in rec(r-k*g[j],j+1))
    return rec(n,0)


def main():
    checked=0; paths=0
    for a in range(3,12):
        f=fibonacci(a); m=f[a]; g=generators(a)
        assert len(all_factorizations(a,3*m))==2
        nmax=min(14*m,250)
        for n in range(nmax+1):
            fs=all_factorizations(a,n)
            if not fs:continue
            finals=set()
            for v in fs:
                end,steps=normalize(a,v)
                finals.add(end)
                paths+=steps
                checked+=1
            assert len(finals)==1,(a,n,finals)
        print(f'a={a}, multiplicity={m}, checked_through={nmax}')
    print(f'PASS: {checked} factorizations reduced; {paths} exact local moves checked')
if __name__=='__main__':main()
