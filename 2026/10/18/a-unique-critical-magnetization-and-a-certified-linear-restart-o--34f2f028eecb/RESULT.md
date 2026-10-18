# A unique critical magnetization and a certified linear restart-onset coefficient for voter consensus

## Finding

Consider the neutral voter-diffusion consensus model with generator
\[
(\mathcal L f)(m)=(1-m^2)f''(m),\qquad -1<m<1,
\]
absorbing endpoints \(m=\pm1\), initial state \(m\in(-1,1)\), and independent Poisson resets at rate \(r\geq0\) to that same initial state until absorption. Let \(R_m(r)\) be the mean elapsed time to either consensus state, including reset episodes. Set \(T_m\) to be the absorption time without resets and \(M_j(m)=\mathbb E_m[T_m^j]\). Define
\[
U=M_1,\quad V=M_2/2,\quad W=M_3/6,\quad
F=U^2-V,\quad B=U^3-2UV+W.
\]
Then there is **exactly one** \(m_c\in(0,1)\) satisfying \(F(m_c)=0\), and it obeys the certified bound
\[
0.63058<m_c<0.63062.
\]
The weak-reset slope \(\partial_rR_m(0)=F(m)\) is positive for \(|m|<m_c\) and negative for \(m_c<|m|<1\). Moreover \(B(m_c)>0\), with a certified interval \(0.003668<B(m_c)<0.003730\). There exists \(\eta>0\) and a unique smooth **local stationary minimizer branch** \(r_{\mathrm{loc}}(m)>0\) for \(m_c<m<m_c+\eta\), satisfying
\[
r_{\mathrm{loc}}(m)=C(m-m_c)+o(m-m_c),\qquad
C=-\frac{F'(m_c)}{2B(m_c)},\qquad 33.56<C<35.22.
\]
High-precision evaluation gives \(m_c\approx0.63059725\), \(C\approx34.3863\) in the stated diffusion time units. The result is **local**: it does not assert that this small-rate minimum is the global optimizer over all restart rates.

## Assumptions and scope

The diffusion is understood as the Wright–Fisher-type one-dimensional martingale diffusion \(dM_t=\sqrt{2(1-M_t^2)}\,dB_t\) until first hitting \(\{-1,1\}\), then absorbed. Start at a fixed \(m\) with \(0\le m<1\). Poisson resetting is instantaneous, state-independent at rate \(r\), and returns to \(m\). The original discrete-time complete-graph voter model has one update per step; on its weak-shock diffusion scale, elapsed time is measured in updates divided by the square of population size. Consequently its per-update reset probability corresponds to \(r/N^2\) when the rescaled reset rate is \(r\). No uniform-in-\(N\) or optimization-limit interchange is asserted. Symmetry extends the result to negative \(m\).

All \(M_j\) are finite and continuous on the closed interval and smooth in the interior. The time-unit normalization is fixed by the displayed generator; changing it rescales \(C\) inversely.

## Proof

**Moment recursion and renewal identity.** Let \(G\) be the Green operator of the killed diffusion. Its action on a bounded input \(g\) is the solution of \(\mathcal L Gg=-g\), zero at \(\pm1\). First-event decomposition and the strong Markov property give
\[
M_0\equiv1,\quad M_j=jG M_{j-1},\quad
M_j''=-\frac{jM_{j-1}}{1-m^2},\quad M_j(\pm1)=0.
\]
Thus \(\lVert Gg\rVert_\infty\le(\log2)\lVert g\rVert_\infty\), and \(M_j\le j!(\log2)^j\). This guarantees a positive exponential moment and an analytic Laplace transform \(\Phi_m(r)=\mathbb E_m[e^{-rT_m}]\) near zero. Since reset epochs are independent exponential clocks, renewal decomposition yields
\[
R_m(r)=\frac{1-\Phi_m(r)}{r\Phi_m(r)}\quad (r>0),\qquad R_m(0)=M_1(m).
\]
The Taylor expansion \(\Phi=1-Ur+Vr^2-Wr^3+O(r^4)\) therefore gives
\[
R_m(r)=U(m)+F(m)r+B(m)r^2+O(r^3).
\]

**Uniqueness of the threshold.** Solving the first moment equation gives
\[
U(m)=-\frac{1+m}{2}\log\frac{1+m}{2}-\frac{1-m}{2}\log\frac{1-m}{2},\qquad U'(m)=-\operatorname{artanh}m.
\]
Write \(V=M_2/2\), so \(V''=-U/(1-m^2)\), \(V'(0)=0\), and \(V(1)=0\). Therefore
\[
F''(m)=2\operatorname{artanh}^2m-\frac{U(m)}{1-m^2}.
\]
For \(a(m)=\operatorname{artanh}m\), set
\[
K(m)=(1-m^2)F''(m)=2(1-m^2)a(m)^2-U(m).
\]
Direct differentiation gives \(K'(m)=a(m)[5-4ma(m)]\). Since \(ma(m)\) strictly increases from zero to infinity, \(K\) increases and then decreases exactly once; \(K(0)=-\log2<0\) and \(K(1-)=0\). The latter decreasing segment is strictly above zero, so \(K\) has exactly one zero. Consequently \(F''\) changes sign exactly once, from negative to positive.

At zero, \(F'(0)=0\), while
\[
V(0)=\int_0^1\frac{U(s)}{1+s}\,ds<(\log2)^2=U(0)^2,
\]
so \(F(0)>0\). At the right endpoint, \(U^2{}'(1-)=0\) and \(V'(1-)=-\int_0^1 U(s)/(1-s^2)\,ds<0\), hence \(F'(1-)>0\) and \(F(1)=0\). Thus \(F\) first decreases, then increases to zero from below. It has exactly one interior zero \(m_c\), necessarily with \(F'(m_c)<0\), and the asserted global sign pattern for \(F\) follows.

**Certified quadratic coefficient.** For \(j\ge1\) define
\[
b_{1,j}=\frac1{2j(2j-1)},\qquad
b_{n,j}=\frac{n}{2j(2j-1)}\sum_{i=j}^{\infty} b_{n-1,i}\quad(n=2,3).
\]
The moment boundary equations imply the absolutely convergent positive series
\[
M_n(m)=\sum_{j\ge1}b_{n,j}(1-m^{2j}),\qquad n=1,2,3.
\]
The alternating-harmonic tail gives \(\sum_{i\ge j}b_{1,i}\le1/(2j-1)\), hence \(b_{2,j}\le j^{-3}\) and, for \(j\ge2\), \(b_{3,j}\le3/[4(j-1)^4]\). For truncation at \(N\), the respective omitted coefficient sums are at most \(1/(2N^2)\) and \(1/[4(N-1)^3]\). Propagating that tail into \(b_{3,j}\) yields explicit enclosing sums, not unqualified numerical truncations.

The supplied standalone integer fixed-point interval checker uses \(N=2048\), a rational geometric enclosure for \(\log2\), and the above coefficient-tail bounds. It certifies \(F(0.63058)>0\), \(F(0.63062)<0\), and across that bracket
\[
0.003668<B(m)<0.003730,\qquad
-0.25841<F'(m)<-0.25039.
\]
These are certified inequalities, with the detailed rational intervals printed by the checker. In particular \(B(m_c)>0\) and \(33.56<C<35.22\).

**Linear onset.** By the expansion, \(\partial_rR_m(r)=F(m)+2B(m)r+O(r^2)\). At \((m_c,0)\), its derivative in \(r\) is positive and its derivative in \(m\) is negative. The implicit-function theorem gives a unique smooth stationary curve through this point, with derivative \(-F'(m_c)/(2B(m_c))>0\). The second derivative of \(R\) in \(r\) stays positive along the curve sufficiently close to the threshold, so it comprises strict local minimizers for \(m>m_c\). This establishes the claimed linear law and no global optimality conclusion.

## Verification

Run `python3 verify.py` using Python 3.9 or later; it has no third-party dependencies. It performs exact rational fixed-point enclosures with outward integer rounding, bounds omitted moment coefficients analytically, and asserts the certified sign, positivity, and slope intervals. Replaying the file from its delivered package is the intended verification. An independent high-resolution floating-point moment calculation gives the indicative decimal values, but those decimals are not relied upon for the proof.

## Relationship to prior work

Argany Herrera, Alvarez-Zuzek and Artime (arXiv:2609.39858, first posted 30 September 2026) formulate voter dynamics under exogenous resets and numerically report a critical absolute magnetization near \(0.630\). Their paper states that deriving the observed near-critical optimal-rate scaling analytically remains open. Their Markov reset framework, restart-renewal setup, and empirical threshold are prior work.

Pal and Prasad (arXiv:1904.07590; Phys. Rev. Research 1, 032001(R), 2019) already obtain a general Landau-like moment expansion and the generic linear critical exponent in restart problems. No generic exponent is claimed here as new. The present model-specific contribution is an analytical **uniqueness theorem** for the Wright–Fisher voter-diffusion threshold together with a rigorously positive quadratic coefficient and a certified coefficient of the local optimal branch. Related constant-diffusivity interval resetting treated by Pal and Prasad (arXiv:1812.03009) has a different diffusion generator; its full text was not assessed in this examination.

## Limitations

The theorem rigorously concerns the limiting neutral diffusion with Poisson resetting. It does not prove that the **global** minimizer of mean consensus time equals the local branch, nor does it supply finite-population error bounds or prove the discrete voter model has the same optimality transition without scaling limits. Generic restart scaling and the empirical source threshold are established prior facts. Historical-priority comparisons remain limited to accessible inspected literature and recorded searches.

## References

1. G. Argany Herrera, L. G. Alvarez-Zuzek, and O. Artime, *Opinion dynamics under large-scale exogenous events*, arXiv:2609.39858v1 (2026), https://arxiv.org/html/2609.39858.
2. A. Pal and V. V. Prasad, *Landau theory of restart transitions*, arXiv:1904.07590 (2019); published as *Landau-like expansion for phase transitions in stochastic resetting*, Physical Review Research 1, 032001(R) (2019), DOI:10.1103/PhysRevResearch.1.032001.
3. A. Pal and V. V. Prasad, *First passage under stochastic resetting in an interval*, arXiv:1812.03009 (2018), Physical Review E 99, 032123 (2019), DOI:10.1103/PhysRevE.99.032123.
