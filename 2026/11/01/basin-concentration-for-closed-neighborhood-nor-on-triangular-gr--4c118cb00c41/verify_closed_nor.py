"""Independent closed-neighborhood NOR enumeration on triangular graphs."""
from itertools import combinations
from math import comb


def all_covered(m):
    result=0
    for j in range(m+1):
        result+=(-1)**j*comb(m,j)*2**comb(m-j,2)
    return result


def check(n):
    edge_list=list(combinations(range(n),2))
    e=len(edge_list)
    full=(1<<e)-1
    closed_neighbors=[]
    for i,(u,v) in enumerate(edge_list):
        closed_neighbors.append(sum(1<<j for j,(a,b) in enumerate(edge_list) if {u,v}&{a,b}))
    def F(state):
        output=0
        for i,neigh in enumerate(closed_neighbors):
            if not state & neigh:
                output |=1<<i
        return output
    cycles={}; first_entry_counts=[0,0,0]
    b_special=0
    for x in range(1<<e):
        y=F(x); z=F(y)
        if F(z)!=y or x==y and x !=0:
            raise AssertionError(('bad relation',n,x,y,z))
        if y==z:
            raise AssertionError(('fixed state',n,x,y))
        key=(y,z) if y<z else (z,y)
        cycles[key]=cycles.get(key,0)+1
        first_entry_counts[0 if x==y or x==z else 1]+=1
        if key==(0,full):b_special+=1
    expected=2**(n-1)-n
    assert len(cycles)==expected,(n,len(cycles),expected)
    c=[all_covered(m) for m in range(n+1)]
    assert b_special==1+c[n]+n*c[n-1],(n,b_special,c)
    for (a,b), basin in cycles.items():
        if (a,b)==(0,full):continue
        W=0
        for idx,(u,v) in enumerate(edge_list):
            if (a>>idx)&1:W|=(1<<u)|(1<<v)
        k=W.bit_count()
        if not 2<=k<=n-2:
            raise AssertionError((n,k,a,b))
        assert basin==c[k]+c[n-k],(n,basin,k,c)
    assert sum(cycles.values())==(1<<e)
    return {'n':n,'initial_states':1<<e,'attractor_orbits':len(cycles), 'special_basin':b_special,'entry0':first_entry_counts[0], 'entry1':first_entry_counts[1], 'c_n':c[n]}

if __name__=='__main__':
    for n in (4,5,6):
        print(check(n))
    print('VERIFY_PYTHON_OK')
