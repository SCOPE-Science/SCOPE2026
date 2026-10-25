"""Independent numerical checks of finite-circle Gaussian spectral asymptotics.
Only checks finite examples; analytic asymptotic proof is supplied separately.
"""
import mpmath as mp
mp.mp.dps=100


def eigen(n,k,c):
    t=mp.mpf(c)/n
    val=mp.mpf(1)
    for j in range(1,(n-1)//2+1):
        val+=2*mp.exp(-t*j*j)*mp.cos(2*mp.pi*k*j/n)
    if n%2==0:
        val+=(-1)**k*mp.exp(-t*(n//2)**2)
    return val


def poisson(n,k,c,images=5):
    q=mp.mpf(k)/n
    return mp.sqrt(mp.pi*n/c)*sum(mp.exp(-mp.pi**2*n*(q-j)**2/c) for j in range(-images,images+1))


def defect(n,k,c,images=5):
    lo=-(n-1)//2 # for even n -> -n/2, valid shortest rep
    reps=list(range(lo,lo+n))
    t=mp.mpf(c)/n
    return sum(sum(mp.exp(-t*(j+L*n)**2) for L in range(-images,images+1) if L!=0)*mp.cos(2*mp.pi*k*j/n) for j in reps)

# Independent numerical decomposition by unfolded images and theta transform.
max_error=mp.mpf('0')
for n in (13,16,17,18,23,24,31,32,40):
    for c in (mp.mpf('2.4'),mp.mpf('3.15'),mp.mpf('3.7')):
        for k in (0,1,2,2*(n//4),n//2):
            if k>n//2:continue
            difference=abs(poisson(n,k,c)-defect(n,k,c)-eigen(n,k,c))
            max_error=max(max_error,difference)
assert max_error < mp.mpf('1e-70'), max_error
print('max finite-cycle Poisson-image identity error',mp.nstr(max_error,6))

# Witness across residue classes; test positive definiteness by ALL eigenvalues.
for n in (40,41,42,43,60,61,62,63,80,81):
    k=2*(n//4)
    lo=mp.mpf('2.6');hi=mp.mpf('3.6')
    assert eigen(n,k,lo)<0,(n,k)
    positives=[eigen(n,j,hi) for j in range(n//2+1)]
    assert min(positives)>0,(n,mp.nstr(min(positives),8))
    print('n=',n,'negative witness k=',k,'negative lambda=',mp.nstr(eigen(n,k,lo),8), 'smallest eigenvalue at c=3.6=',mp.nstr(min(positives),8))

# Refined root, n divisible by 4.
C=2*mp.log(2/mp.tanh(mp.pi/2))
for n in (40,80,120,160,200):
    approx=mp.pi-(mp.log(n)+C)/n
    root=mp.findroot(lambda z:eigen(n,n//2,z),(approx-mp.mpf('.01'),approx+mp.mpf('.01')),solver='secant',tol=mp.mpf('1e-85'),maxsteps=100)
    assert abs(eigen(n,n//2,root))<mp.mpf('1e-70')
    print('n=',n,'c_N=',mp.nstr(root,23),'constant estimator=',mp.nstr(n*(mp.pi-root)-mp.log(n),18))
print('predicted constant C =',mp.nstr(C,22))
print('ALL FINITE CHECKS PASS')
