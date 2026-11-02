# Independent mathematical audit

## correctness

PASS

For D,b,mu>0, stationary Cox-reset survival satisfies S(t)=E exp(-int_0^t lambda_u du)=<1,e^{-tH}1> where H=(lambda+mu)I-mu P on L^2(exponential(mean b)); H is positive self-adjoint and its essential spectrum is [mu,infty). A rank-one bound state below mu has eigenvector (lambda+s)^-1 and equation mu F_b(s)=1. F_b strictly decreases from infinity with mu F_b(mu)<1, yielding one s* in (0,mu), eigenvalue a*=mu-s*. Spectral atom mass B*=1/(mu^2 M_2(s*))=b s*/[mu(mu-s*)] lies (0,1). The stationary backward reset-age density -S'(t), Gaussian heat kernel and positive spectral measure give p(x)=(B*/2)sqrt(a*/D) exp(-sqrt(a*/D)|x|)+R(x), with 0<=R<=(sqrt b)/(2sqrt D) exp(-sqrt(mu/D)|x|). Stieltjes inversion gives the stated nonnegative continuum rho(q); E1 small-argument expansion yields s*~b exp(-gamma_E-b/mu) and exponentially small residue. The variance is 2D F_b(mu)/(1-mu F_b(mu)), giving MSD effective a=1/F_b(mu)-mu ~ b/log(b/mu), distinct from a*~mu. Independently numerically solved the eigencondition and checked B* and variance for mu=0.3,1,3 with b=D=1. These checks supplement the spectral proof.

## originality

PASS

Arutkin–Reuveni (2025), primary author-posted full text, already gives the exact Fourier transform of precisely this model (eqs.23–24), and suggests a far-tail scale by expanding it near k=0. It does not separately establish the isolated subcontinuum pole, its positive spectral mass, uniform remainder separation, nonperturbative weight, or exact contrast with the moment-based surrogate; indeed the latter need not equal the strict tail exponent. Constant-rate resetting spectral results do not directly cover the Cox intensity environment. Best-of-knowledge originality for correcting a subtle asymptotic interpretation of a previously known transform, not for the transform itself.

## value

PASS

In random-rate diffusion, the apparent spatial exploration length from second moments can disagree arbitrarily with the actual strict far-tail decay length, yet the extremal mode has exponentially tiny weight. This distinction prevents an observable inference error in the precise source model and is captured by explicit pole/residue formula and controlled continuum remainder. It is a motivated mathematical refinement, not an arbitrary parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
