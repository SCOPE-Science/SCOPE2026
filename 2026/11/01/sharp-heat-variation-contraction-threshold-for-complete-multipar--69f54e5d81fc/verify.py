"""Finite exact checks supporting the multipartite heat-variation theorem.

All tests use Python integers. They do not replace the proof for arbitrary graph order.
Run: python verify.py
"""
from itertools import product


def integer_partitions(n, minimum=1):
    if n == 0:
        yield ()
    for first in range(minimum, n + 1):
        for rest in integer_partitions(n - first, first):
            yield (first,) + rest


def pair_contribution(a, b, c, d, r):
    return (a*c*abs(b-d)+b*d*abs(a-c)
            -a*d*(a+d+r)-b*c*(b+c+r))


def pair_lower_bound(a, b, c, d, r):
    return (a*d*(a+d+r)+b*c*(b+c+r)
            -a*b*(c+d)-c*d*(a+b))


def class_cut_derivative(sizes, selected):
    n = sum(sizes)
    outside = [m-a for a,m in zip(selected, sizes)]
    return sum(pair_contribution(selected[i], outside[i],
                                 selected[j], outside[j],
                                 n-sizes[i]-sizes[j])
               for i in range(len(sizes)) for j in range(i+1, len(sizes)))


def direct_cut_derivative(sizes, selected):
    cls = sum(([i]*m for i,m in enumerate(sizes)), [])
    n = len(cls)
    bits = []
    for i, m in enumerate(sizes):
        bits.extend([1]*selected[i]+[0]*(m-selected[i]))
    edges = [(i,j) for i in range(n) for j in range(i+1,n) if cls[i]!=cls[j]]
    boundary = [0]*n
    for i,j in edges:
        if bits[i]!=bits[j]:
            boundary[i]+=1; boundary[j]+=1
    return sum(abs(boundary[i]-boundary[j]) if bits[i]==bits[j]
               else -(boundary[i]+boundary[j]) for i,j in edges)


def run():
    counts = dict(pair_cases=0, cut_checks=0, graph_cut_comparisons=0,
                  contraction_partitions=0, amplifying_partitions=0)
    for a,b,c,d in product(range(8), repeat=4):
        s,t=a+b,c+d
        if s==0 or t==0:continue
        for r in range(6):
            n=s+t+r
            if 2*max(s,t)>n+2:continue
            f=pair_lower_bound(a,b,c,d,r)
            x,y=a-c,b-d
            assert f==(y-x)*(c*y-d*x)+r*(a*d+b*c)
            assert f>=0
            assert pair_contribution(a,b,c,d,r)<=-f<=0
            counts['pair_cases']+=1
    for n in range(2,12):
        for sizes in integer_partitions(n):
            if len(sizes)<2:continue
            contract = 2*max(sizes)<=n+2
            counts['contraction_partitions' if contract else 'amplifying_partitions']+=1
            worst=-10**9
            for selected in product(*(range(m+1) for m in sizes)):
                if not 0<sum(selected)<n:continue
                d=class_cut_derivative(sizes, selected)
                worst=max(worst,d)
                counts['cut_checks']+=1
                if n<=8:
                    assert d==direct_cut_derivative(sizes, selected)
                    counts['graph_cut_comparisons']+=1
            assert (worst<=0)==contract, (sizes,worst,contract)
            if not contract:
                imax=sizes.index(max(sizes))
                chosen=[0]*len(sizes)
                chosen[imax]=1
                d=class_cut_derivative(sizes,chosen)
                s=max(sizes)
                assert d==(n-s)*(2*s-n-2)>0
    assert class_cut_derivative((2,5),(0,1))==2
    assert class_cut_derivative((1,4),(0,1))==1
    assert class_cut_derivative((1,3),(0,1))==0
    print('PASS', counts)

if __name__=='__main__':
    run()
