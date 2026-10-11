from fractions import Fraction
from math import sqrt, cos, acos, pi

def det3(M):
    a,b,c=M[0]; d,e,f=M[1]; g,h,i=M[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)

def char_coeffs(M):
    tr=sum(M[i][i] for i in range(3))
    tr2=sum(M[i][j]*M[j][i] for i in range(3) for j in range(3))
    return -tr,(tr*tr-tr2)/2,-det3(M)

def eigvals_sym3(M):
    A=[[float(v) for v in row] for row in M]
    q=sum(A[i][i] for i in range(3))/3.0
    p2=sum((A[i][i]-q)**2 for i in range(3))+2*sum(A[i][j]**2 for i in range(3) for j in range(i+1,3))
    p=sqrt(p2/6.0)
    if p<1e-15: return [q,q,q]
    C=[[(A[i][j]-(q if i==j else 0.0))/p for j in range(3)] for i in range(3)]
    r=max(-1.0,min(1.0,det3(C)/2.0)); phi=acos(r)/3.0
    return sorted([q+2*p*cos(phi),q+2*p*cos(phi+2*pi/3),q+2*p*cos(phi+4*pi/3)])

count=0
for N in range(1,41):
    for A in range(N+1):
        rem=N-A
        if rem%2: continue
        half=rem//2
        for B in range(half+1):
            C=half-B
            x1=Fraction(A,N); x2=Fraction(B,N); x3=Fraction(C,N)
            s=x2+x3; d=x2-x3
            M=[[x1,s,d],[s,-x1,d],[d,d,-x1]]
            got=char_coeffs(M)
            expected=(x1,-x1*x1-3*x2*x2+2*x2*x3-3*x3*x3,-x1**3-x1*x2*x2-2*x1*x2*x3-x1*x3*x3-2*x2**3+2*x2*x2*x3+2*x2*x3*x3-2*x3**3)
            assert got==expected
            Q=x1*x1+2*x2*x2+2*x3*x3
            dev=(x1-Fraction(1,5))**2+2*(x2-Fraction(1,5))**2+2*(x3-Fraction(1,5))**2
            assert Q==Fraction(1,5)+dev
            vals=eigvals_sym3(M); lam1=vals[-1]; lam3=vals[0]
            assert lam1*lam1+1e-11>=float(Q)
            assert lam3<=-1/sqrt(5)+1e-11
            if x2==x3: assert abs(lam1*lam1-float(Q))<1e-9
            count+=1
print(f"VERIFY_OK tetrahedral spectral stability rational_grid={count} max_denominator=40")
