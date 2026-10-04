import math

def simpson(f,a,b,n):
    assert n%2==0
    h=(b-a)/n
    s=f(a)+f(b)
    s+=4*sum(f(a+(2*k-1)*h) for k in range(1,n//2+1))
    s+=2*sum(f(a+2*k*h) for k in range(1,n//2))
    return s*h/3

I=simpson(lambda u: math.sqrt((1-u)/(1+u)),0.0,1.0,200000)
s_num=2*I/math.pi
s_exact=1-2/math.pi
ls=math.pi/(math.pi-2)
lc=math.pi/(4-math.pi)
L=1/lc
assert abs(s_num-s_exact)<2e-8
assert abs(1/ls-s_exact)<1e-14
assert abs((1-L)/2-s_exact)<1e-14
assert abs(ls-2*lc/(lc-1))<1e-13
muA=2+2/(ls-1)
muB=2+2/(lc-1)
assert abs(muA-math.pi)<1e-13
assert abs(muB-ls)<1e-13
print('VERIFY_OK',f's={s_exact:.15f}',f'lambda_s={ls:.15f}',f'lambda_c={lc:.15f}',f'A_mu={muA:.15f}',f'B_mu={muB:.15f}')
