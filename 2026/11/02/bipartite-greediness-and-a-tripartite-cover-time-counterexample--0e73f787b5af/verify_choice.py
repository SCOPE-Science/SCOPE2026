"""Exact, standalone Bellman certificate for the two-choice cover-time counterexample.
Uses only Python's standard library.  A floating-point policy search is
followed by exact rational evaluation and exhaustive Bellman comparisons.
"""
from fractions import Fraction as Q
from itertools import product

A=(1,2,6)
K=len(A)
TERM=A
STATES=sorted(product(*(range(s+1) for s in A)),key=lambda v:-sum(v))
TARGET=((0,2,2),2)

def categories(v,i):
    return tuple((j,new,count) for j in range(K) if j!=i
                 for new,count in ((0,v[j]),(1,A[j]-v[j])) if count)

def step(v,j,new):
    return tuple(v[k]+int(new and k==j) for k in range(K))

def selected(c,d,vals,greedy,alternate=False):
    # c,d are (part, novelty, multiplicity)
    if alternate and c[1]!=d[1]:
        if {c[:2],d[:2]}=={(0,1),(1,0)}:
            return c if c[:2]==(1,0) else d
    if greedy and c[1]!=d[1]:
        return c if c[1] else d
    return c if vals[c[:2]]<=vals[d[:2]] else d

def solve3(mat,rhs):
    n=len(rhs)
    m=[[Q(mat[i][j]) for j in range(n)]+[Q(rhs[i])] for i in range(n)]
    for j in range(n):
        pivot=next((i for i in range(j,n) if m[i][j]!=0),None)
        assert pivot is not None, ('singular',mat,rhs)
        m[j],m[pivot]=m[pivot],m[j]
        z=m[j][j];m[j]=[x/z for x in m[j]]
        for i in range(n):
            if i!=j:
                z=m[i][j]
                m[i]=[m[i][l]-z*m[j][l] for l in range(n+1)]
    return [m[i][-1] for i in range(n)]

def approx_policy(greedy=True):
    V={}
    for v in STATES:
        if v==TERM:
            for i in range(K):V[v,i]=0.
            continue
        parts=[i for i in range(K) if v[i]]
        if not parts:continue
        x={i:0. for i in parts}
        for iteration in range(12000):
            nxt={}
            for i in parts:
                cat=categories(v,i);d=sum(t[2] for t in cat)
                vals={(j,new):(V[step(v,j,new),j] if new else x[j]) for j,new,_ in cat}
                nxt[i]=1+sum(c[2]*e[2]*vals[selected(c,e,vals,greedy)[:2]] for c in cat for e in cat)/(d*d)
            if max(abs(nxt[i]-x[i]) for i in parts)<1e-12:
                x=nxt;break
            x=nxt
        else:raise Exception('float search did not converge')
        for i in parts:V[v,i]=x[i]
    return V

def exact_evaluate(policy_float,greedy=True,alternate=False):
    V={};decisions={};checked=0
    for v in STATES:
        if v==TERM:
            for i in range(K):V[v,i]=Q(0)
            continue
        parts=[i for i in range(K) if v[i]]
        if not parts:continue
        # For a fixed policy, each equation is linear in same-v visited successors.
        M=[[Q(int(i==j)) for j in parts] for i in parts]
        rhs=[Q(1) for _ in parts]
        for pos,i in enumerate(parts):
            cat=categories(v,i);d=A[0]+A[1]+A[2]-A[i]
            vals={(j,new):(float(policy_float[step(v,j,new),j]) if new else float(policy_float[v,j])) for j,new,_ in cat}
            for c in cat:
                for e in cat:
                    chosen=selected(c,e,vals,greedy,alternate and (v,i)==TARGET)
                    j,new,count=chosen
                    p=Q(c[2]*e[2],d*d)
                    if new:rhs[pos]+=p*V[step(v,j,new),j]
                    else:M[pos][parts.index(j)]-=p
                    decisions[v,i,c[:2],e[:2]]=chosen[:2]
                    checked+=1
        sol=solve3(M,rhs)
        for i,z in zip(parts,sol):V[v,i]=z
    return V,decisions,checked

def assert_optimal_greedy(V,decisions):
    checks=0
    for v in STATES:
        if v==TERM:continue
        for i in range(K):
            if not v[i]:continue
            for c in categories(v,i):
                for e in categories(v,i):
                    if c[1]!=e[1]:
                        assert decisions[v,i,c[:2],e[:2]] == (c[:2] if c[1] else e[:2])
                    else:
                        chosen=decisions[v,i,c[:2],e[:2]]
                        alt=e if chosen==c[:2] else c
                        zc=V[step(v,chosen[0],chosen[1]),chosen[0]]
                        za=V[step(v,alt[0],alt[1]),alt[0]]
                        assert zc<=za,(v,i,c,e,zc,za)
                    checks+=1
    return checks

def main():
    pol=approx_policy()
    G,P,eq=exact_evaluate(pol,True)
    n=assert_optimal_greedy(G,P)
    D,R,eq2=exact_evaluate(pol,True,True)
    v,i=TARGET
    optB=G[v,1];newA=G[(1,2,2),0]
    assert newA-optB == Q(3210462360632365129,1379009216128693567275)
    start=(0,1,0)
    difference=G[start,1]-D[start,1]
    assert difference==Q(2285849200770243971848,4016620735540189127344279)
    assert Q(56,100000)<difference<Q(58,100000), float(difference)
    assert R[v,i,(0,1),(1,0)]==(1,0)
    print('GRAPH K_(1,2,6)')
    print('greedy-state comparisons',n,'policy transitions',eq)
    print('local advantage when choosing visited B rather than new A:',float(newA-optB))
    print('start B: greedy expected steps:',format(float(G[start,1]),'.15f'))
    print('start B: modified expected steps:',format(float(D[start,1]),'.15f'))
    print('start B: exact rational improvement bracket: 0.00056 < delta < 0.00058, actual',format(float(difference),'.15f'))
    print('numerator digits:',len(str(difference.numerator)),'denominator digits:',len(str(difference.denominator)))
    print('all exact Bellman checks passed')

if __name__=='__main__':main()
