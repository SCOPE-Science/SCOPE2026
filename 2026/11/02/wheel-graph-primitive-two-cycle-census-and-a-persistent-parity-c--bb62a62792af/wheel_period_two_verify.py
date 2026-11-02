#!/usr/bin/env python3
"""Independent exact checks of primitive two-cycles on hub-and-rim wheel graphs."""
from itertools import product
from math import prod


def wheel_edges(n):
    assert n >= 3
    e = {tuple(sorted((0,i))) for i in range(1,n+1)}
    e.update(tuple(sorted((i,1+(i%n)))) for i in range(1,n+1))
    return sorted(e)


def adjacency(n):
    adj=[set() for _ in range(n+1)]
    for i,j in wheel_edges(n):adj[i].add(j);adj[j].add(i)
    return [tuple(sorted(v)) for v in adj]


def update(x,adj):
    fired=[int(x[v]>=len(adj[v])) for v in range(len(adj))]
    return tuple(x[v] - len(adj[v])*fired[v] + sum(fired[w] for w in adj[v]) for v in range(len(adj)))


def orbit_count_by_direct_states(n):
    adj=adjacency(n)
    deg=[len(v) for v in adj]
    cycles_states=0
    for x in product(*(range(2*d) for d in deg)):
        y=update(x,adj)
        if y!=x and update(y,adj)==x:cycles_states+=1
    assert cycles_states%2==0
    return cycles_states//2


def count_by_binary_cuts(n):
    adj=adjacency(n); acc=0
    for mask in range(1<<n):
        spin=[0]+[(mask>>(v-1))&1 for v in range(1,n+1)]
        k=[sum(spin[u]!=spin[v] for u in adj[v]) for v in range(n+1)]
        acc+=prod(k)
    return acc


def count_by_explicit_rim_words(n):
    ans=0
    for a in product((0,1),repeat=n):
        k=sum(a)
        w=1
        for i,b in enumerate(a):
            w *= b + int(a[(i-1)%n]!=b) + int(a[(i+1)%n]!=b)
        ans += k*w
    return ans


def count_by_recurrence(n):
    assert n >= 3
    a={3:20,4:69,5:225}
    for i in range(6,n+1): a[i]=2*a[i-1]+4*a[i-2]+a[i-3]
    return n*a[n]


def main():
    for n in range(3,16):
        a=count_by_binary_cuts(n)
        b=count_by_explicit_rim_words(n)
        c=count_by_recurrence(n)
        assert a==b==c,(n,a,b,c)
        if n<=6:
            d=orbit_count_by_direct_states(n)
            assert d==a,(n,d,a)
            print(f'n={n} direct={d} cut={a} recurrence={c}')
        else:
            print(f'n={n} cut={a} recurrence={c}')
    print('WHEEL_TWO_CYCLE_EXACT_VERIFY_OK')

if __name__ == '__main__': main()
