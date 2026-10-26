#!/usr/bin/env python3
"""Independent finite coefficient checks for periodic binary digit weights.
These checks corroborate, but do not replace, the infinite symbolic proof.
"""

def mul(a,b):
    v=0
    while b:
        if b&1:v^=a
        a <<= 1;b >>= 1
    return v

def divide(a,b):
    q=0
    while a and a.bit_length()>=b.bit_length():
        shift=a.bit_length()-b.bit_length()
        q^=1<<shift;a^=b<<shift
    return q,a

def gcd(a,b):
    while b:a,b=b,divide(a,b)[1]
    return a

def coeff_check(d,mask,N=2048):
    B=(1<<d)|1
    D=gcd(mask,B)
    E,rem=divide(B,D);assert rem==0
    C,rem=divide(mask,D);assert rem==0
    assert gcd(E,C)==1
    weights=[(mask>>j)&1 for j in range(d)]
    seq=[sum(weights[j%d]*((n>>j)&1) for j in range(n.bit_length()))&1 for n in range(N)]
    y=[seq[n]^(seq[n-1] if n else 0) for n in range(N)]
    # Compute the two sides of E(F)Y = C(F)*x/(1+x), over F_2.
    for n in range(N):
        lhs=0
        for j in range(E.bit_length()):
            if ((E>>j)&1) and n%(1<<j)==0:lhs^=y[n>>j]
        rhs=0
        if n:
            for j in range(C.bit_length()):
                if ((C>>j)&1) and n%(1<<j)==0:rhs^=1
        assert lhs==rhs,(d,mask,n,lhs,rhs)
    return E.bit_length()-1

def main():
    total=0
    for d in range(1,8):
        for mask in range(1<<d):
            coeff_check(d,mask)
            total+=1
    degs={}
    for mask in range(8):
        bits=''.join(str(mask>>j&1) for j in range(3))
        degs[bits]=1<<coeff_check(3,mask)
    assert degs=={'000':1,'100':8,'010':8,'110':4,'001':8,'101':4,'011':4,'111':2}
    # Independent digit-DFAO comparison for Campbell-Cloitre M2.
    trans=((0,1,3,2),(2,3,1,0),(3,2,0,1),(1,0,2,3))
    for n in range(65536):
        ds=[];k=n
        while k: ds.append(k%4);k//=4
        state=0
        for digit in reversed(ds):state=trans[state][digit]
        direct=sum((n>>j)&1 for j in range(n.bit_length()) if j%3!=2)&1
        assert state%2==direct,n
    print('PASS: 254 nonzero/zero periodic masks (periods 1..7), 2048 coefficients each')
    print('PASS: 65536 terms compared with independent four-state M2 DFAO')
    print('period-3 exact algebraic degree predictions:', degs)
    print('M2: A(T)=1+T, B(T)=1+T^3, E(T)=1+T+T^2, C(T)=1')
    print('M2 verified equation: Y^4+Y^2+Y=x/(1+x), Y=(1+x)U')

if __name__=='__main__':main()
