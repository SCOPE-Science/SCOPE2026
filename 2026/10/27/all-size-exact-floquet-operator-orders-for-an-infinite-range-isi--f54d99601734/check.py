#!/usr/bin/env python3
"""Integer Walsh-cube checks of an all-to-all spin Floquet identity."""
def parity(x):
    return x.bit_count() & 1

def phase_q(x,n):
    m=(n-1)//2
    k=x.bit_count()
    return -1 if (m*(m+1)//2 + m*k + k*(k-1)//2) & 1 else 1

def hadamard(v):
    a=v[:]
    n=len(a); stride=1
    while stride<n:
        for i in range(0,n,2*stride):
            for j in range(i,i+stride):
                x,y=a[j],a[j+stride]
                a[j]=x+y;a[j+stride]=x-y
        stride*=2
    return a

def cube_action(n,source):
    d=1<<n; z=[0]*d;z[source]=1
    for _ in range(3):
        z=hadamard(z)
        z=[phase_q(x,n)*v for x,v in enumerate(z)]
    return z

def run():
    for n in (3,5,7,9):
        coeff=1<<((3*n-1)//2)
        for x in range(1<<n):
            actual=cube_action(n,x)
            expected=[0]*(1<<n)
            expected[x]+=((-1)**parity(x))*coeff
            expected[x^((1<<n)-1)]+=coeff
            assert actual==expected, (n,x)
        print('EXACT_INTEGER_IDENTITY_OK',n)
    print('CHECK_OK')

if __name__=='__main__':run()
