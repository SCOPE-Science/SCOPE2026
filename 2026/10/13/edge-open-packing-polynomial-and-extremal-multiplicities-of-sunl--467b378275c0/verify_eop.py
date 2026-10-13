"""Direct edge-conflict enumeration and symbolic checks for sunlet edge-open packings.
Python 3 is required; SymPy enables exact characteristic-polynomial checks.
"""
from collections import Counter
from math import comb

def sunlet(n):
    # Cycle vertices 0..n-1, private leaves n..2n-1.
    return [(i,(i+1)%n) for i in range(n)]+[(i,n+i) for i in range(n)]

def brute(n):
    E=sunlet(n)
    m=len(E)
    # e_i,e_j conflict iff a third edge connects an endpoint of each.
    bad=[0]*m
    for i,(a,b) in enumerate(E):
        for j,(c,d) in enumerate(E):
            if j<=i: continue
            if any(k not in (i,j) and ((u in (a,b) and v in (c,d)) or (u in (c,d) and v in (a,b))) for k,(u,v) in enumerate(E)):
                bad[i]|=1<<j;bad[j]|=1<<i
    coeff=[0]*(m+1)
    # Incremental independence-mask recurrence brute without using cyclic-site local rule.
    valid=bytearray(1<<m);valid[0]=1
    for mask in range(1,1<<m):
        bit=mask&-mask; i=bit.bit_length()-1; tail=mask^bit
        if valid[tail] and not (tail&bad[i]):valid[mask]=1;coeff[mask.bit_count()]+=1
    coeff[0]=1
    while coeff and not coeff[-1]: coeff.pop()
    return coeff,sum(valid)

def recurrence(N):
    pol={0:[4],1:[1],2:[1,2],3:[1,6,6]}
    def axpy(out,src,shift,c):
        for i,v in enumerate(src):
            j=i+shift
            while len(out)<=j:out.append(0)
            out[j]+=c*v
    for n in range(4,N+1):
        p=[]
        for j,s,c in [(1,0,1),(2,1,1),(3,1,1),(3,2,2),(4,2,1),(4,3,1)]:
            axpy(p,pol[n-j],s,c)
        pol[n]=p
    return pol

if __name__=='__main__':
    P=recurrence(32)
    checked=0
    for n in range(3,10):
        direct,nvalid=brute(n)
        assert direct==P[n],(n,direct,P[n])
        assert nvalid==sum(P[n]),(n,nvalid,sum(P[n]))
        checked+=(1<<(2*n))
        print('direct',n,'candidate_subsets',1<<(2*n),'coefficients',direct,'max',len(direct)-1)
    for n in range(3,33):
        assert len(P[n])-1==3*n//4,(n,P[n])
    print('total_direct_candidates',checked)
    # Sharp top coefficients in each residue class modulo four.
    for n in range(3,33):
        q,r=divmod(n,4)
        formulas={0:4,1:(4*q+1)*(4*q*q+2*q+3)//3,
                  2:2*(2*q+1)**2,3:8*q+6}
        assert P[n][-1]==formulas[r],(n,P[n][-1],formulas[r])
    print('degree_and_extremal_multiplicity_formulas_through_32 PASS')
    try:
        import sympy as S
        x,l=S.symbols('x lambda')
        states4=[(0,0),(1,0),(0,1),(1,1)]
        indices4={v:i for i,v in enumerate(states4)}
        W=S.zeros(4)
        for (f0,f1),i in indices4.items():
            for mask in range(4):
                if f0 and mask:continue
                next_state=(int(bool(f1 or (mask&1))),int(bool(mask&2)))
                W[i,indices4[next_state]]+=x**mask.bit_count()
        expected_q=l**4-l**3-x*l**2-(x+2*x**2)*l-(x**2+x**3)
        assert S.expand(W.charpoly(l).as_expr()-expected_q)==0
        for n in range(3,10):
            computed=S.Poly(S.trace(W**n),x)
            assert all(computed.nth(k)==P[n][k] for k in range(len(P[n])))
        print('exact_4x4_transfer_characteristic_and_traces PASS')
        states=[(a,b) for a in range(4) for b in range(4)]
        idx={v:i for i,v in enumerate(states)}
        T=S.zeros(16)
        for (a,b),j in idx.items():
            for c in range(4):
                # Site b having pendant edge excludes all at the next site c.
                # Site a having cycle edge excludes all at site c two steps later.
                if ((b&1)!=0 or (a&2)!=0) and c!=0:continue
                T[j,idx[(b,c)]]=x**c.bit_count()
        characteristic=S.factor(T.charpoly(l).as_expr())
        expected=l**12*(l**4-l**3-x*l**2-(x+2*x**2)*l-(x**2+x**3))
        assert S.expand(characteristic-expected)==0
        assert S.expand(S.det(S.eye(16)-S.symbols('t')*T)-(1-S.symbols('t')-x*S.symbols('t')**2-(x+2*x**2)*S.symbols('t')**3-(x**2+x**3)*S.symbols('t')**4))==0
        print('exact_16x16_characteristic_certificate PASS')
    except ImportError:
        print('sympy unavailable: symbolic certificate not checked')
