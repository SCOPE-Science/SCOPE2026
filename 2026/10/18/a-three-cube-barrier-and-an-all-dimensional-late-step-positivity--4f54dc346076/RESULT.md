# A three-cube barrier and an all-dimensional late-step positivity law for fourth-order Gauss diffusion

## Finding
On every unit-rate hypercube of dimension \(d\ge3\), the fourth-order two-stage Gauss--Legendre endpoint update eventually has a **negative nearest-neighbor entry**, even though the exact heat semigroup is strictly positive and the numerical update remains symmetric, mass preserving and positive definite. Dimensions one and two are positive at every positive timestep, so the first obstruction is the eight-vertex three-cube. On that cube the exact allowable interval is \([0,\tau]\), where \(\tau\approx8.58376346373336\) is the unique positive solution of
\[
 h^4-6h^3-20h^2-18h-6=0.
\]
The claim concerns the completed numerical time step, not its internal Runge--Kutta stages.

## Assumptions and scope
For each integer \(d\ge1\), index vertices by binary strings \(x\in\{0,1\}^d\). Let \(F_i\) flip coordinate \(i\) and let \(Q_d=\sum_{i=1}^d(F_i-I)=-L_d\), the conservative rate-one-at-each-coordinate generator. Use the standard rational function
\[
 R(z)=\frac{1+z/2+z^2/12}{1-z/2+z^2/12},\qquad T_d(h)=R(hQ_d),\quad h\ge0.
\]
The matrix denominator is invertible for every \(h\ge0\) because its scalar denominator is positive at each real nonpositive eigenvalue. Entrywise nonnegativity means every matrix entry is nonnegative; it is not implied by positive definiteness.

## Proof
**Walsh reduction.** The characters \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\) diagonalize \(Q_d\), with eigenvalues \(-2|S|\). Consequently, for vertices at Hamming distance \(j\), the common entry is
\[
 p_{d,j}(h)=2^{-d}\sum_{k=0}^d K_k(j)\,r_k(h),\qquad
 K_k(j)=\sum_{\ell=0}^k(-1)^\ell\binom j\ell\binom{d-j}{k-\ell},\quad
 r_k(h)=\frac{1-kh+k^2h^2/3}{1+kh+k^2h^2/3}.
\]
The rational function has positive denominator; its numerator is positive since \(1-x+x^2/3>0\) for every real \(x\). Thus every spectral multiplier is positive, every \(T_d(h)\) is positive definite, and \(r_0=1\) makes it mass preserving.

**All-dimensional late-step obstruction.** For \(k\ge1\), \(r_k(h)=1-6/(kh)+O_k(h^{-2})\) as \(h\to\infty\). The Walsh coefficients satisfy \(\sum_{k=0}^d K_k(1)=0\), \(K_k(1)=\binom{d-1}{k}-\binom{d-1}{k-1}=\binom dk(1-2k/d)\). Therefore
\[
 p_{d,1}(h)=-\frac{6}{2^dh}S_d+O_d(h^{-2}),\qquad
 S_d=\sum_{k=1}^d\frac{\binom dk}{k}-\frac{2(2^d-1)}d.
\]
Using \(\sum_{k=0}^d\binom dk/(k+1)=(2^{d+1}-1)/(d+1)\) yields the **exact** recurrence
\[
 S_{d+1}-S_d=\frac{2^{d+1}-d-2}{d(d+1)}.
\]
Its numerator is positive for each \(d\ge2\); direct calculation gives \(S_3=1/6\). Hence \(S_d>0\) for every \(d\ge3\), proving strictly negative nearest-neighbor entries for all sufficiently large timesteps, with no dimension-uniform bound asserted.

**Sharp first dimension.** For \(d=1\), \(p_{1,1}(h)=h/(1+h+h^2/3)>0\). For \(d=2\), direct substitution into the Walsh formula gives strictly positive distance-one and distance-two entries whenever \(h>0\); the diagonal is positive by positivity of all multipliers, so those two dimensions have no positivity failures.

**Complete three-cube threshold.** For \(d=3\), let
\[
 D(h)=2(h^2+3h+3)(3h^2+3h+1)(4h^2+6h+3)>0.
\]
Exact simplification gives the four Hamming-shell entries
\[
\begin{aligned}
 p_{3,0}(h)&=(24h^6+45h^5+44h^4+36h^3+66h^2+54h+18)/D(h),\\
 p_{3,1}(h)&=-3h(h^4-6h^3-20h^2-18h-6)/D(h),\\
 p_{3,2}(h)&=3h^2(7h^3+18h^2+18h+6)/D(h),\\
 p_{3,3}(h)&=3h^3(11h^2+18h+6)/D(h).
\end{aligned}
\]
All except distance one are positive for positive \(h\). The distance-one quartic has exactly one positive root by Descartes' rule of signs (its coefficient signs are \(+,-,-,-,-\)), and changes from negative to positive there. Hence its negative multiple has the prescribed unique positivity cutoff. The zero step is the identity and is nonnegative. Exact real-root isolation, or bisection using this one-root fact, yields the reported approximation.

## Verification
The included standalone `verify.py` reproduces the Walsh rational identities in dimensions one through three, checks the three-cube four-shell rational formulas, proves the stated binomial recurrence symbolically, computes root isolation numerically, and checks the stated sign patterns for representative exact rational timesteps. These are corroborative finite symbolic calculations; the induction and Walsh diagonalization above prove the claims for all \(d\).

## Relationship to prior work
Zappavigna, Colaneri, Kirkland and Shorten (2010) gave general positivity-preservation conditions and counterexamples for diagonal Padé approximations of positive systems. The published eight-state directed pure-birth obstruction to the same fourth-order map concerns **arbitrarily small timesteps**. Published work on a seven-dimensional hypercube concerns a different, higher-dimensional small-step sign obstruction and its disconnected positivity set. In contrast, the present claim identifies **the first hypercube dimension with any positive-step failure**, the exact threshold in that dimension, and a universal large-step nearest-neighbor sign law over all hypercube dimensions at least three. General Walsh diagonalization is standard prior mathematics; its spectral formula is not presented as new.

## Limitations
There is no claim of novelty for generic positivity failure of Padé approximations or for Walsh/Krawtchouk diagonalization. No all-timestep classification is asserted for dimensions \(d\ge4\). Numerical or symbolic checks of finitely many cubes are not an infinite-dimensional proof, and the result makes no assertion of independent audit.

## References
Zappavigna, A., Colaneri, P., Kirkland, S. and Shorten, R., *On the preservation of co-positive Lyapunov functions under Padé discretization for positive systems*, MTNS 2010, deposited 15 October 2010. https://mural.maynoothuniversity.ie/id/eprint/2195/

Zappavigna, A., Colaneri, P., Kirkland, S. and Shorten, R., *A scaling and squaring method for the discretisation of positive switched systems*, CDC 2011. https://www.researchgate.net/publication/241636964_A_scaling_and_squaring_method_for_the_discretisation_of_positive_switched_systems

*Eight-state barrier for Markov positivity of the [2/2] Padé map*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab
