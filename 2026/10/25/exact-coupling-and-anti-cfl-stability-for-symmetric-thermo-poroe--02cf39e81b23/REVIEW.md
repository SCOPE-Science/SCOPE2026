# Independent mathematical audit

## correctness

PASS

Specializing the source (5.4) matrix to A=C=Ctilde=1, D=Dtilde=d, B=Btilde=b and Chat=c yields precisely u^{n+1}=d(p^n+theta^n), (1+t)p^{n+1}=d(u^n-u^{n+1})+p^n+c(theta^n-theta^{n-1}) and the symmetric theta update. Symmetric/antisymmetric coordinates produce one zero eigenvalue and quadratics [(1+t)z^2-(1-K)z-K] and [(1+t)z^2-(1-c)z-c], K=2d^2-c. The three strict Jury/Schur inequalities for symmetric factor simplify to t>0, 2+t-2K>0, and 1+t+K>0 (latter automatic from K>-1); antisymmetric factor is Schur for every t>0. This proves sharp threshold, -1 boundary and below-bound instability. Constant histories give both scalar first-step values v1=v0/(1+t); root expansions yield O(h) physical and O(h) parasitic coefficients for K<1. At K=1 the exact parity formula v_n=v0(1+t)^(-ceil(n/2)) gives O(h) convergence even with root approaching -1; at K>1 coefficient on the root near -K is proportional to h for nonzero symmetric initial mode and grows like h K^(T/h). Independent SymPy characteristic determinant and 144 spectral root tests corroborated, not replacing proof.

## originality

PASS

The directly relevant Altmann–Maier–Schmeck 2026 full text Section 5.4 specifies the fully decoupled scheme; Theorem 5.4 supplies a sufficient weak-coupling condition and Section 6.4 reports numerically stable regions outside it. Its scalar sufficient condition 2d^2+c<=1 plus d^2>c does not give the sharp necessary-and-sufficient 2d^2<=1+c or anti-CFL step-size reversal. Altmann–Maier 2021 is two-field poroelastic; Chen–Cui–Zhou 2025 uses a distinct stabilized DG method. The scalar spectral computation is elementary in isolation but exact sharp interpretation for this contemporary physical split and correct marginal convergence are not stated in inspected prior primary results.

## value

PASS

The precise stability and convergence boundary resolves a gap between sufficient analytic theory and observed numerical stable regions for a motivated three-field discretization. It exposes an anti-CFL regime where decreasing step size destabilizes a consistent method, and proves convergence at a marginal limiting -1 mode. This has actionable mathematical implications for analyzing this numerical scheme, beyond a generic textbook quadratic-root test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
