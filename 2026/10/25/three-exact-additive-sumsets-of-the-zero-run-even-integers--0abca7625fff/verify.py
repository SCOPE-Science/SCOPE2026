"""Independent, finite witness and digit-language checks supplement the symbolic proof."""

def baum_sweet_direct(n):
    assert n >= 0
    if n == 0:
        return True
    bits = bin(n)[2:]
    return all(len(run) % 2 == 0 for run in bits.split('1'))


def baum_sweet_recursive(n):
    if n == 0:
        return True
    if n % 4 == 0:
        return baum_sweet_recursive(n // 4)
    if n % 8 == 1:
        return baum_sweet_recursive((n-1) // 8)
    if n % 4 == 3:
        return baum_sweet_recursive((n-3) // 4)
    return False


def witnesses(N):
    """X[n]=(a,b), a+b=n; Y[n]=(a,b), a+2b=n, both a,b in A."""
    X = [(0,0)]
    Y = [(0,0)]
    for n in range(1,N+1):
        q,r=divmod(n,4)
        if r==0:
            a,b=X[q]; x=(4*a,4*b)
        elif r==1:
            a,b=Y[q]; x=(4*a,8*b+1)
        elif r==2:
            if q==0: x=(1,1)
            else:
                a,b=X[q-1]; x=(4*a+3,4*b+3)
        else:
            a,b=X[q]; x=(4*a,4*b+3)
        if r==0:
            a,b=Y[q]; y=(4*a,4*b)
        elif r==3:
            a,b=Y[q]; y=(4*a+3,4*b)
        elif r==2:
            if q==0: y=(0,1)
            else:
                a,b=Y[q-1]; y=(4*a,4*b+3)
        elif n%8==1:
            t=(n-1)//8
            a,b=X[t]; y=(8*a+1,4*b)
        else:
            t=(n-5)//8
            if t==0: y=(3,1)
            else:
                a,b=Y[2*t-1]; y=(4*a+3,4*b+3)
        assert sum(x)==n and x[0]>=0 and x[1]>=0, (n,x,'X')
        assert y[0]+2*y[1]==n and y[0]>=0 and y[1]>=0, (n,y,'Y')
        for z in x+y:
            assert baum_sweet_direct(z), (n,z,x,y)
        X.append(x);Y.append(y)
    return X,Y


def run():
    N=50000
    for n in range(N+1):
        assert baum_sweet_recursive(n)==baum_sweet_direct(n),n
    print('PASS binary language recurrence n=0..%d'%N)
    X,Y=witnesses(N)
    print('PASS explicit mutually inductive witness identities X=A+A and Y=A+2A n=0..%d'%N)
    for n in range(N+1):
        m,r=divmod(n,4)
        if r==2: continue
        if r==0:
            a,b=X[m]; u,v=(4*a,b)
        elif r==3:
            a,b=X[m];u,v=(4*a+3,b)
        else:
            a,b=Y[m];u,v=(8*b+1,a)
        assert u+4*v==n and baum_sweet_direct(u) and baum_sweet_direct(v),n
    print('PASS complete allowed residues A+4A n=0..%d'%N)
    # Independent modular exclusion of residue 2; direct enumeration for small bound.
    aa=[j for j in range(4097) if baum_sweet_direct(j)]
    achievable={a+4*b for a in aa for b in aa if a+4*b<=4096}
    assert achievable=={n for n in range(4097) if n%4!=2}
    print('PASS direct mixed sumset brute force n<=4096')
    f0,f1=0,1
    for k in range(15):
        target=0
        x,y=0,1
        for _ in range(k+2):x,y=y,x+y
        target=x
        actual=sum(baum_sweet_direct(n) for n in range(2**k))
        assert actual==target,(k,actual,target)
    print('PASS dyadic Fibonacci enumeration k=0..14')
    print('ALL CHECKS PASS; finite tests supplement exact induction, not prove it')

if __name__=='__main__':run()
