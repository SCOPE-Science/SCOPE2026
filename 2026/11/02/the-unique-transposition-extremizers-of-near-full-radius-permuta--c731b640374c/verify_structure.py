"""Check exact restriction formulas, Bonferroni gaps, and published benchmarks."""
from itertools import permutations
from math import factorial
D=[1,0]
for n in range(2,101):D.append((n-1)*(D[n-1]+D[n-2]))
for n in range(5,101):
    U=D[n-1]+D[n-2]
    Vmax=D[n-2]+2*D[n-3]+D[n-4]
    delta=U-3*Vmax+D[n-2]
    assert delta>0,(n,delta)
    if n>=8:assert delta==(n-3)*D[n-2]+(n-8)*D[n-3]-3*D[n-4]
for n in range(5,9):
    S=list(permutations(range(n)))
    Dp=[p for p in S if all(p[i]!=i for i in range(n))]
    single=sum(p[0]==1 for p in Dp)
    assert single==D[n-1]+D[n-2]
    two_cycle=sum(p[0]==1 and p[1]==0 for p in Dp)
    chain=sum(p[0]==1 and p[1]==2 for p in Dp)
    disjoint=sum(p[0]==1 and p[2]==3 for p in Dp)
    assert (two_cycle,chain,disjoint)==(D[n-2],D[n-2]+D[n-3],D[n-2]+2*D[n-3]+D[n-4]), (n, two_cycle,chain,disjoint)
    print('restriction_counts',n,single,two_cycle,chain,disjoint)
for n in range(5,101):
    val=factorial(n)-D[n]-2*D[n-1]-D[n-2]
    if n in {5,6,7,8,9,10,11}:
        print('N(n,n-1)',n,val,'gap_lower_bound',D[n-1]-D[n-2]-6*D[n-3]-3*D[n-4])
assert factorial(9)-D[9]-2*D[8]-D[7]==197864
assert factorial(10)-D[10]-2*D[9]-D[8]==2012014
print('STRUCTURE_OK')
