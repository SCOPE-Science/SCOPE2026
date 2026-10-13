from math import gcd

N=1000
P=[0,1]
Q=[1,1]
while len(P)<N:
    P.append(2*P[-1]+P[-2])
    Q.append(2*Q[-1]+Q[-2])
B=[0,1]
C=[1,3]
while len(B)<300:
    B.append(6*B[-1]-B[-2])
    C.append(6*C[-1]-C[-2])

identity_checks=0
gcd_checks=0
for n in range(0,250):
    assert B[n] == P[2*n]//2
    assert C[n] == Q[2*n]
for k in range(1,200,2):
    target=gcd(B[k],k)
    gb=0; gc=0
    for n in range(0,40):
        sb=sum(B[n+i]**2 for i in range(1,k+1))
        sc=sum(C[n+i]**2 for i in range(1,k+1))
        q=Q[4*n+2*k+2]
        assert sb == (B[k]*q-k)//16
        assert sc == (B[k]*q+k)//2
        identity_checks += 2
        gb=gcd(gb,sb); gc=gcd(gc,sc)
    assert gb == target, (k,gb,target)
    assert gc == target, (k,gc,target)
    gcd_checks += 2
print(f"VERIFY_OK identity_checks={identity_checks} gcd_checks={gcd_checks} odd_k_max=199 starts=40")
