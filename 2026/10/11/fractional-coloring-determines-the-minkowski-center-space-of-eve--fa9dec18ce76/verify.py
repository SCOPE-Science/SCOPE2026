from fractions import Fraction as Q
from itertools import combinations

def solve_linear(rows,rhs):
    n=len(rhs)
    a=[[Q(x) for x in row]+[Q(b)] for row,b in zip(rows,rhs)]
    for k in range(n):
        piv=next((i for i in range(k,n) if a[i][k]),None)
        if piv is None: return None
        a[k],a[piv]=a[piv],a[k]
        t=a[k][k];a[k]=[z/t for z in a[k]]
        for i in range(n):
            if i!=k:
                t=a[i][k]
                a[i]=[x-t*y for x,y in zip(a[i],a[k])]
    return tuple(row[-1] for row in a)

def graph(name,n,edges):
    pairs={tuple(sorted(x)) for x in edges}
    inds=[]
    for mask in range(1<<n):
        V=[i for i in range(n) if mask>>i&1]
        if all((u,v) not in pairs for u,v in combinations(V,2)):
            inds.append(tuple(int(j in V) for j in range(n)))
    max_inds=[ind for ind in inds if not any(all(a<=b for a,b in zip(ind,jnd)) and ind!=jnd for jnd in inds)]
    A=list(max_inds)+[tuple(-int(i==j) for i in range(n)) for j in range(n)]
    b=[1]*len(max_inds)+[0]*n
    vertices={}
    for subset in combinations(range(len(A)),n):
        x=solve_linear([A[i] for i in subset],[b[i] for i in subset])
        if x is not None and all(sum(a*z for a,z in zip(row,x))<=bb for row,bb in zip(A,b)):
            vertices[x]=sum(x)
    m=max(vertices.values()); opts=[x for x,val in vertices.items() if val==m]
    T=[i for i in range(n) if any(y[i]>0 for y in opts)]
    # Verify dual optimal face exact and center candidate 1+eps*e_i for unpinned i
    for i in range(n):
        if i in T:continue
        denom=[(m-total)/y[i] for y,total in vertices.items() if y[i]>0 and total<m]
        if denom:
            eps=min(denom)/2
            assert eps>0
            assert all(sum(y)+eps*y[i]<=m for y in vertices)
    print(name,'n',n,'chi_f',m,'minkowski_center',str(Q(1,1)/(m+1)), 'unfixed',[i for i in range(n) if i not in T], 'dual_vertices',len(vertices), 'independent_sets',len(inds))
    return m,T

graph('edgeless3',3,[])
graph('K3',3,[(0,1),(0,2),(1,2)])
graph('P3',3,[(0,1),(1,2)])
graph('K2+isolated',3,[(0,1)])
graph('C5',5,[(i,(i+1)%5) for i in range(5)])
graph('K4+isolated',5,[(i,j) for i in range(4) for j in range(i+1,4)])
print('VERIFY_OK')
