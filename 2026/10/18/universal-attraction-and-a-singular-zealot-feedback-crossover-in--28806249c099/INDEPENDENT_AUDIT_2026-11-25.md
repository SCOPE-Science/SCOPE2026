# Independent mathematical audit

## correctness

PASS

The inward endpoint signs and the log ratio of the two positive interior fluxes are correct. To check monotonicity independently, put v=u(1-u) on Z<u<1/2. Then R_Z=A_Z/B equals sqrt(1-4v) times the integral from 0 to Z of 1/[(v-t(1-t))(-log v)]. The denominator in the integrand has v-derivative -log v-1+t(1-t)/v>0, so R_Z has strictly negative derivative, with limits infinity and zero. At a root the drift derivative is the positive reverse flux times B R'_Z<0. The flux signs, reflection, and the exact neutral drift Z(1-2u) give global attraction including endpoints; differentiating the original drift at neutrality gives -(1-2Z)log(4)/(8Z). For rho/Z→c the rescaled drift converges locally uniformly in the interior to 1-2u+c u(1-u)log(u(1-u)); the sign change at its unique zero brackets the finite-Z root, including c=0. Implicit differentiation of this limiting drift at (u,c)=(1/2,0) gives U'(0)=-log(4)/8. For fixed rho>0 the root tends to zero because the limiting zero-commitment drift is strictly negative on compact subintervals of (0,1/2]. With x=u_*-Z its stationary equation gives x/(x+Z)=[(1-2Z-x)/(1-Z-x)^(1-rho)](x+Z)^rho→0, then x/Z^(1+rho)→1. An independent bisection on the original and limiting drifts reproduced 0.3068815408197915 for u_*(0.225,0.6) and 0.3329154617472118 for U(1).

## originality

PASS

The source supplies the model and an equilibrium curve at one fixed commitment. The all-parameter monotonicity and global attraction, and especially the singular moving-parameter equilibrium limits, are distinct. No examined related general model or indexed result was shown to imply them.

## value

PASS

The question is motivated by the source's numerical equilibrium curve. The result rules out bistability across the frozen parameter domain and shows why a vanishing absolute bias can still yield a finite shift when the bias and commitment are comparable. The limiting profile and distinct fixed-bias minority law give quantitative predictions that a fixed-commitment plot cannot supply.

The dated certificate retains the supplied scientific assessment, sources and limitations.
