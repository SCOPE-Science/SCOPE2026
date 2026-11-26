# Independent mathematical audit

## correctness

PASS

Independent derivation: for 0<m<=1, condition on the event M_n<=m, of probability m^n. The observations are then iid uniform on [0,m]. For t<m use E[F_n(t)]=t/m and Var(F_n(t))=(t/m)(1-t/m)/n; for t>=m use F_n(t)=1. Integrating n E[(F_n(t)-t)^2] yields P(m)=n(1-m)^2/3+m/6. Differentiate m^n P(m) and divide by n m^(n-1) to get E[W_n^2|M_n=m], then replace m with 1-b. This gives exactly the quoted quadratic, with positive leading term and minimizer strictly inside [0,1]. Interpret the values at b=0,1, and the pointwise regression generally, as the continuous version, not as values uniquely fixed by conditioning on probability-zero events. Integrating m^n P(m) over [0,1] gives E[B_n W_n^2]; subtracting 1/[6(n+1)] gives (n-1)/[2(n+1)(n+2)(n+3)]. Independently, the off-diagonal kernel second moment is the double integral of (min(s,t)-st)^2, which is (2/3) integral_0^1 t^3(1-t)^2 dt=1/90. The one-variable diagonal variance is 1/180. Degeneracy cancels all covariances except those of a pair with itself (or its reversal in the ordered sum), giving variance [n/180+2n(n-1)/90]/n^2. This also identifies the intended fraction at RESULT.md line 139, where a form-feed corrupts the LaTeX command but not the separately stated identity. Beta variance yields the stated positive correlation and asymptotic. Exact replay: python3 /workspace/checks/4.py checks coefficients and moments for n=2..50; the all-n identities are analytic. The frozen script checks correlation in floating point, not exact rational arithmetic, but it follows algebraically from the exact covariance and variances.

## originality

PASS

Pass for the specific conditional endpoint profile and induced mixed moments at the frozen record's October catalogue date, not for the classical marginal variances. The most substantial indexed overlap is a November catalogue record with an extrema-conditioned mean that implies the entire endpoint result. It is not disregarded as merely about the range, but there is no evidence that this later entry or its extrema-conditioned formula predated the October record. Earlier checked material and the same-day Watson coupling do not establish the endpoint result. Older joint-distribution coverage remains unexcluded; access limits do not determine the verdict.

## value

PASS

The gap has an independent, natural endpoint interpretation, while W_n^2 measures integrated global discrepancy. The exact conditional regression shows an initially decreasing response, then an increasing one, even though linear covariance is strictly positive at every n>=2. The interior optimum and exact rate of vanishing correlation give finite-null benchmarks for comparing a tail-coverage diagnostic and an integrated test. This is not a computation of a known marginal CvM variance, and routine maximum moments alone do not determine the coupling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
