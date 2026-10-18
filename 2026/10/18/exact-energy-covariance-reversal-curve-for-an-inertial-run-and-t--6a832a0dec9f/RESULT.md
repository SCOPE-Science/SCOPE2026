# Exact energy-covariance reversal curve for an inertial run-and-tumble oscillator

## Finding

The stationary potential and kinetic energies of a telegraph-forced, harmonically confined inertial particle can be positively or negatively correlated even though position and velocity are uncorrelated. Their covariance has a sharp, unique sign-reversal curve.

Write \(g>0\) for dimensionless viscous damping and \(\rho>0\) for dimensionless direction-flipping rate. Define
\[
\begin{aligned}
P(g,\rho)={}&48\rho^4+192g\rho^3+(288g^2+104)\rho^2\\
&+(138g^3+136g)\rho+3(6g^2-1)(g^2+3),\\
H(g,\rho)={}&g(3g^2+4)(1+2g\rho+4\rho^2)^2\\
&\quad\cdot(9+6g\rho+4\rho^2)(1+2g^2+6g\rho+4\rho^2).
\end{aligned}
\]
For the dimensionless stationary position and velocity \((q,p)\),
\[
\boxed{\operatorname{Cov}(q^2,p^2)=-\frac{4\rho P(g,\rho)}{H(g,\rho)}.}
\]
Every factor of \(H\) is strictly positive on \(g,\rho>0\). There is positive covariance precisely in the region
\[
0<g<\frac1{\sqrt6},\qquad 0<\rho<\rho_*(g),
\]
where \(\rho_*(g)\) is the unique positive zero of \(P(g,\cdot)\). On the curve the covariance is zero; everywhere else it is strictly negative. The curve is strictly decreasing and has limiting endpoints
\[
\lim_{g\downarrow0}\rho_*(g)=\frac1{2\sqrt3},\qquad
\lim_{g\uparrow1/\sqrt6}\rho_*(g)=0.
\]
In particular, for \(g\ge1/\sqrt6\), the stationary kinetic and potential energies are strictly negatively correlated at every positive switching rate.

## Assumptions and scope

Fix particle mass \(m>0\), trap stiffness \(k>0\), viscous coefficient \(\gamma>0\), nonzero drive amplitude \(a>0\), and flipping rate \(\alpha>0\). The physical dynamics are
\[
\dot x=v,\qquad m\dot v=-kx-\gamma v+a\sigma(t),
\]
where the independent stationary telegraph process \(\sigma(t)\in\{-1,+1\}\) changes sign at rate \(\alpha\). There is no translational thermal forcing. Normalize time by \(\sqrt{m/k}\), position by \(a/k\), and velocity by \(a/\sqrt{mk}\). Then the normalized equations are
\[
\dot q=p,\qquad\dot p=-q-gp+\sigma,\qquad
 g=\frac{\gamma}{\sqrt{mk}},\quad \rho=\alpha\sqrt{\frac mk}.
\]
The unique stationary distribution is used throughout. Its ordinary position–velocity covariance is zero, \(\mathbb E[qp]=0\). For physical energies \(E_{\rm pot}=kx^2/2\) and \(E_{\rm kin}=mv^2/2\), the displayed normalized covariance is multiplied by the strictly positive factor \(a^4/(4k^2)\). Consequently the complete sign classification holds for physical energy covariance without dependence on the drive amplitude.

## Proof

**Existence, uniqueness, and moments.** Let \(A=\left(\begin{smallmatrix}0&1\\-1&-g\end{smallmatrix}\right)\) and \(b=(0,1)^{\mathsf T}\). For every \(g>0\), the two eigenvalues of \(A\) have negative real part. If \(\sigma\) is the stationary two-sided telegraph chain, then
\[
(q_t,p_t)^{\mathsf T}=\int_{-\infty}^t e^{A(t-s)}b\,\sigma_s\,ds
\]
exists absolutely, is uniformly bounded, and defines a stationary solution. Exponential stability eliminates dependence on any initial position and velocity; ergodicity of the driving chain gives the unique stationary law of the joint process.

**Closed generator equations.** For nonnegative integers \(i,j\), write \(M_{ij}=\mathbb E[q^ip^j]\) and \(L_{ij}=\mathbb E[\sigma q^ip^j]\). The stationary generator, applied to these polynomials, gives
\[
\begin{aligned}
0={}&iM_{i-1,j+1}-jM_{i+1,j-1}-gjM_{ij}+jL_{i,j-1},\\
0={}&iL_{i-1,j+1}-jL_{i+1,j-1}-(gj+2\rho)L_{ij}+jM_{i,j-1}.
\end{aligned}
\]
Negative subscripts mean zero. Reflection symmetry gives \(M_{ij}=0\) when \(i+j\) is odd, and \(L_{ij}=0\) when \(i+j\) is even; also \(M_{00}=1\). The equations are triangular by total degree: first solve signed moments of degree one, ordinary moments of degree two, signed moments of degree three, and ordinary moments of degree four. The corresponding coefficient-matrix determinants (with unknowns ordered by increasing position exponent) are \(B\), \(-4g\), \((9+6g\rho+4\rho^2)(1+2g^2+6g\rho+4\rho^2)\), and \(-32g(3g^2+4)\), respectively. They never vanish on the stated domain.

Put \(B=1+2g\rho+4\rho^2\). Degree one gives \(L_{10}=1/B\) and \(L_{01}=2\rho/B\), while degree two gives
\[
M_{20}=\frac{g+2\rho}{gB},\qquad M_{02}=\frac{2\rho}{gB},\qquad M_{11}=0.
\]
Solving the two subsequent degree systems gives
\[
M_{22}=\frac{2\rho N(g,\rho)}{g^2(3g^2+4)B(9+6g\rho+4\rho^2)(1+2g^2+6g\rho+4\rho^2)},
\]
where
\[
\begin{aligned}
N(g,\rho)={}&18g^5+66g^4\rho+72g^3\rho^2-3g^3+24g^2\rho^3\\
&+58g^2\rho+72g\rho^2+54g+32\rho^3+72\rho.
\end{aligned}
\]
Subtraction of \(M_{20}M_{02}\) and exact common-denominator simplification produce the covariance formula in the finding. All these equalities are reproducible by the accompanying exact symbolic script, which builds the generator systems afresh.

**Complete sign classification.** Since \(H>0\), the covariance has sign opposite to \(P\). For every \(g>0\),
\[
\frac{\partial P}{\partial\rho}=192\rho^3+576g\rho^2+2(288g^2+104)\rho+(138g^3+136g)>0.
\]
At \(\rho=0\), \(P(g,0)=3(6g^2-1)(g^2+3)\). Therefore if \(g\ge1/\sqrt6\), \(P>0\) for every \(\rho>0\); if \(g<1/\sqrt6\), the polynomial begins negative and tends to positive infinity, crossing zero exactly once. Moreover \(\partial_gP>0\) in the positive quadrant, so the implicit curve is strictly decreasing. Setting \(g=0\) yields \(P(0,\rho)=48\rho^4+104\rho^2-9\), with unique positive zero \(1/(2\sqrt3)\). Continuity, strict monotonicity and \(P(1/\sqrt6,0)=0\) yield the two stated endpoint limits. Endpoints themselves are limiting parameter values, not additional stationary cases.

Finally \(\frac d{dt}\mathbb E[q^2]=2\mathbb E[qp]=0\) establishes zero linear position–velocity covariance, and physical energy scaling preserves the sign result. This finishes the proof.

## Verification

Run `python verify.py` with SymPy installed. The program independently reconstructs all degree-one through degree-four stationary moment equations by exact matrix inversion, checks the displayed rational covariance identity, verifies the factorization and monotone-sign argument symbolically, and separately solves 54 rational parameter instances. The program checks 135 exact assertions. The finite parameter checks are supplementary: the proof of the all-parameter sign theorem is the symbolic factorization together with the positive-coefficient derivative argument.

## Relationship to prior work

Dutta, Kundu, Sabhapandit, and Basu (2024) analyze exactly this inertial run-and-tumble model. Their Section III derives general polynomial-moment recurrences and displays stationary second moments; later sections reconstruct individual position and velocity marginals and their non-Gaussian structures. The recurrences are the established starting point, not a newly claimed method. The new claim is the explicit mixed fourth-order **energy** covariance and the global, unique, monotone sign-reversal boundary, which do not follow from the displayed second-order or marginal distribution classifications without the additional calculation and sign proof.

Patel and Chaudhuri (2024) analyze fourth moments of a different model, an inertial active Brownian particle with diffusing continuous orientation and translational thermal noise; their marginal-kurtosis phase diagrams do not imply this telegraph-process kinetic–potential energy covariance. Smith and Farago (2022) investigate a rapid-active-noise large-deviation limit rather than the complete positive-rate mixed fourth-moment sign diagram.

## Limitations

The theorem assumes a symmetric Poisson telegraph drive, linear confinement, positive damping, and no added thermal diffusion. It does not cover biased switching, other driving laws, nonlinear traps, or statements about the full joint density. Formulaic derivability from previously published general moment recurrences is acknowledged; independent investigation of publication priority has not occurred. The exact full-parameter classification is a mathematical result, not a claim about finite-data statistical detectability.

## References

- D. Dutta, A. Kundu, S. Sabhapandit, and U. Basu, *Harmonically trapped inertial run-and-tumble particle in one dimension*, arXiv:2406.06120 (first public 2024-06-10), especially Section III, Eqs. (17)–(36), and Appendices A–C.
- M. Patel and D. Chaudhuri, *Exact moments for trapped active particles: inertial impact on steady-state properties and re-entrance*, arXiv:2404.01107 (first public 2024-04-01), Sections 4–5 and Appendix A.
- N. R. Smith and O. Farago, *Nonequilibrium steady state for harmonically confined active particles*, Physical Review E 106, 054118 (2022), DOI: 10.1103/PhysRevE.106.054118.
