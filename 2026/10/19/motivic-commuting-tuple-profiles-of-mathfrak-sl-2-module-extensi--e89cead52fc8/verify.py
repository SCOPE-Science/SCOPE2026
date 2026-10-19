"""Independent finite-field checks for commuting tuples in sl2 semidirect symmetric-power modules.

Run: python3 verify.py. Only prime fields are used for checks; theorem covers any finite field.
"""
from itertools import product


def representation(ms, p):
    d = sum(m + 1 for m in ms)
    E = [[0] * d for _ in range(d)]
    F = [[0] * d for _ in range(d)]
    H = [[0] * d for _ in range(d)]
    off = 0
    for m in ms:
        for j in range(m + 1):
            H[off+j][off+j] = (m - 2*j) % p
            if j:
                E[off+j-1][off+j] = j % p
            if j < m:
                F[off+j+1][off+j] = (m-j) % p
        off += m+1
    return E,F,H


def action(rep, x, p):
    return [[sum(x[i] * rep[i][r][c] for i in range(3)) % p for c in range(len(rep[0]))]
            for r in range(len(rep[0]))]


def bracket(x,y,p):
    a,b,c=x; A,B,C=y
    return ((2*(c*A-a*C))%p, (2*(b*C-c*B))%p, (a*B-b*A)%p)


def modrank(A,p):
    if not A: return 0
    B=[list(map(lambda z:z%p,row)) for row in A]
    r=0
    n=len(B[0])
    for col in range(n):
        piv=next((i for i in range(r,len(B)) if B[i][col]),None)
        if piv is None: continue
        B[piv],B[r]=B[r],B[piv]
        inv=pow(B[r][col],-1,p)
        for j in range(col,n): B[r][j]=(B[r][j]*inv)%p
        for i in range(r+1,len(B)):
            if B[i][col]:
                v=B[i][col]
                for j in range(col,n): B[i][j]=(B[i][j]-v*B[r][j])%p
        r+=1
        if r==len(B):break
    return r


def independent_census(ms,q,s):
    rep=representation(ms,q)
    d=sum(m+1 for m in ms)
    base=list(product(range(q),repeat=3))
    acts={x:action(rep,x,q) for x in base}
    ct=0
    valid=0
    for xs in product(base, repeat=s):
        if any(bracket(xs[i],xs[j],q)!=(0,0,0) for i in range(s) for j in range(i+1,s)):
            continue
        valid += 1
        eq=[]
        for i in range(s):
            for j in range(i+1,s):
                for r in range(d):
                    row=[0]*(s*d)
                    for col in range(d):
                        row[j*d+col]=acts[xs[i]][r][col]
                        row[i*d+col]=(-acts[xs[j]][r][col])%q
                    eq.append(row)
        rank=modrank(eq,q)
        ct+=q**(s*d-rank)
    return ct, valid


def predicted(ms,q,s):
    d=sum(m+1 for m in ms)
    e=sum(m%2==0 for m in ms)
    t=len(ms)
    return q**(d*s)+(q**s-1)*(q**(d+2+(s-1)*e)+(q+1)*q**(d+(s-1)*t))


def test_action_ranks(ms,q):
    rep=representation(ms,q)
    d=sum(m+1 for m in ms)
    t=len(ms);e=sum(m%2==0 for m in ms)
    frequencies={}
    for x in product(range(q),repeat=3):
        actual=d-modrank(action(rep,x,q),q)
        if x==(0,0,0):expected=d
        else:
            a,b,c=x
            expected=t if (c*c+a*b)%q==0 else e
        assert actual==expected, (ms,q,x,actual,expected)
        frequencies[actual]=frequencies.get(actual,0)+1
    return frequencies


def run():
    cases=[(3,[1],2),(3,[1],3),(3,[2],2),(3,[2],3),
           (5,[3],2),(5,[1,4],2),(5,[2,3],2),
           (5,[1,2],2)]
    for q,ms,s in cases:
        assert max(ms)<q and q%2
        observed,nproj=independent_census(ms,q,s)
        formula=predicted(ms,q,s)
        assert observed==formula,(q,ms,s,observed,formula)
        spectrum=test_action_ranks(ms,q)
        print('PASS',q,ms,'tuple_length',s,'commuting',observed,'projected',nproj,'action_nullities',spectrum)
    # Check that algebraically distinct module decompositions have equal full counting profiles.
    a,b=[1,4],[2,3]
    for q in (5,7,11):
        for s in (1,2,3,4,5):
            assert predicted(a,q,s)==predicted(b,q,s)
    print('VERIFY_OK')

if __name__=='__main__': run()
