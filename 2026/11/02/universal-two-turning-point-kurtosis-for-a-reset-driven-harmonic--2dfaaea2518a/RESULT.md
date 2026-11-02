# Universal two-turning-point kurtosis for a reset-driven harmonic oscillator

## Finding
Consider a mass \(m>0\) attached by equal springs \(k>0\) to two independently moving walls, with viscous damping \(\gamma>0\). Each wall is a Brownian motion of common diffusivity \(D>0\) that is reset to zero at its own independent Poisson times of common rate \(\lambda>0\). The oscillator position obeys
\[
m\ddot x+\gamma\dot x+2kx=k(Z_L+Z_R).
\]
In the unique stationary regime, set \(a=2km/\gamma^2>0\), \(r=\lambda m/\gamma>0\), and let \(E_a(r)=\mathbb E[v^4]/\mathbb E[v^2]^2-3\) be the stationary velocity excess kurtosis. Define
\[
Q(a,r)=r(r+1)(4a+r^2+2r)(9a+r^2+3r)(a+r^2+3r+2)
\]
and
\[
\begin{aligned}
N(a,r)={}&a^4(9r+27)+a^3(91r^3+87r^2+108r+54)\\
&+a^2(199r^5+535r^4+510r^3+204r^2+18r)\\
&+a(21r^7+47r^6+37r^5+11r^4-18r^3-18r^2)\\
&+21r^7+93r^6+141r^5+87r^4+18r^3.
\end{aligned}
\]
Then the exact formula is
\[
\boxed{E_a(r)=\frac{3N(a,r)}{(4a+3)Q(a,r)}.}
\]
For **every** \(a>0\), this function has exactly two positive critical rates \(r_-(a)<\sqrt a<r_+(a)\), both simple. It decreases strictly on \((0,r_-)\), increases strictly on \((r_-,r_+)\), then decreases strictly on \((r_+,\infty)\). The first critical point is a strict minimum and the second is a strict maximum. Thus a single excess-kurtosis observation strictly between these extremal values corresponds to exactly three distinct positive resetting rates, even with all mechanical parameters known.

## Assumptions and scope
All five physical constants are strictly positive, each reset clock and driving Brownian motion is independent, and resets change the wall positions but not the oscillator position or velocity. Both walls have the same diffusion constant and resetting rate; this equality is part of the theorem. Time normalization \(s=\gamma t/m\) reduces every mechanical triple to damping coefficient one and stiffness \(a\); a common force scale does not affect kurtosis. The mechanical poles lie in the open left half-plane, giving a unique stationary causal solution with finite moments of every finite order. The theorem concerns exact stationary ensemble moments, not noisy estimates or unequal wall clocks.

## Proof
For one unit-intensity wall, write \(u'=v\), \(v'=-au-v+z\), with \(z\) a Brownian motion with generator \(\partial_{zz}\) that resets to zero at rate \(r\). For polynomials \(f\), its stationary generator is
\[
\mathcal L f=v\partial_u f+(-au-v+z)\partial_v f+\partial_{zz}f+r\{f(u,v,0)-f(u,v,z)\}.
\]
Stationarity gives \(\mathbb E[\mathcal L(u^iv^jz^k)]=0\). At each total degree \(n=2,4\), this is a closed linear system of respectively 6 and 15 equations, with degree-four right-hand side determined by degree-two moments. Eliminating these systems yields
\[
\mathbb E[v^2]=\frac2{a+r+r^2},\qquad
\frac{\mathbb E[v^4]}{\mathbb E[v^2]^2}-3=\frac{6N(a,r)}{(4a+3)Q(a,r)}.
\]
The attached verification program reconstructs the polynomial-generator matrices and tests these exact expressions by rational linear algebra. The general expressions were obtained by exact symbolic elimination; the formula can also be verified by substituting the moment recurrences. Two independent, identically distributed wall contributions add their second and fourth cumulants, so the standardized fourth cumulant for their sum is half the single-wall value. Multiplication of the inputs by the common physical factor changes neither normalized fourth cumulant. This establishes the boxed formula.

For global critical-point counting, put \(P(a,r)=N(a,r)\partial_rQ(a,r)-Q(a,r)\partial_rN(a,r)\). Differentiation gives
\[
\partial_r E_a(r)=-\frac{3P(a,r)}{(4a+3)Q(a,r)^2}.
\]
Write \(P=\sum_{j=0}^{14}c_j(a)r^j\). Exact expansion shows that \(c_{14},c_{13},c_{12}>0\), \(c_9,\ldots,c_4<0\), and \(c_2,c_1,c_0>0\) for all \(a>0\). The only potentially variable signs occur at indices 11, 10, and 3. Specifically,
\[
c_{11}=2(1013a^2-2564a+372),\qquad c_{10}=154a^3+4111a^2-22121a-453.
\]
The coefficient \(c_{12}=3(101a^2-137a+203)>0\) by its negative discriminant. The two possibly troublesome negative terms in \(c_5\) and \(c_4\) are dominated, respectively, by the positive pairs \(30771a^3+10922a\) and \(25601a^3+6720a\), by arithmetic-geometric mean; all other terms in these brackets are positive. If \(c_{11}<0\), then \(0<a<3\); on \([0,3]\), the cubic defining \(c_{10}\) is convex and negative at both endpoints, hence is negative throughout. Thus the coefficients from degree 14 down through degree 4 undergo exactly one transition from positive to negative. The uncertain sign of \(c_3\) cannot add a further transition before the strictly positive final coefficients. Hence the coefficient sequence of \(P\) has exactly **two sign variations**, so Descartes' rule gives at most two positive roots, counted with multiplicity.

To show both roots exist for every \(a\), note \(P(a,0)=972a^5(a+2)^2>0\) and its leading coefficient is \(21(a+1)>0\). With \(t=\sqrt a\), exact substitution gives
\[
P(t^2,t)=-t^6H(t),
\]
where
\[
\begin{aligned}
H(t)={}&27200t^{10}+112720t^9+196248t^8+179452t^7+99362t^6\\
&+84520t^5+125063t^4+117810t^3+60009t^2+15588t+1620.
\end{aligned}
\]
Every coefficient of \(H\) is positive. Thus \(P\) is positive near zero, negative at \(r=\sqrt a\), and positive for sufficiently large \(r\). It has at least two distinct positive roots, one on each side of \(\sqrt a\), and by Descartes no others and neither can have multiplicity greater than one. Their derivative signs prove the asserted strict monotonicity. Finally, \(E_a(r)\sim9a/[4(4a+3)r]\) as \(r\downarrow0\), and \(E_a(r)\sim63(a+1)/[(4a+3)r]\) as \(r\to\infty\); the three-solution statement follows from these endpoint limits and the two strict turning points.

## Verification
Run `python verify_sympy.py` with SymPy installed. The program derives the stationary degree-two and degree-four moment systems at exact rational sample parameters, checks the displayed fourth-moment expression, and verifies the full two-variable derivative polynomial identities including the positive-coefficient witness \(H\). The exact general moment elimination, rather than finite checks, is the mathematical basis of the formula. At the equal-spring canonical value \(a=2\), the critical rates are approximately \(0.8494190914\) and \(4.9714274213\); the corresponding excess-kurtosis values are approximately \(0.672329598\) and \(1.060046851\). These decimal approximations are not used to prove root counts.

## Relationship to prior work
Sarkar and Roy (2023, arXiv:2307.06127, especially Sections 2–4 and the appendices) introduced the boundary-reset harmonic-chain mechanism, obtained velocity covariances and numerical finite-size non-Gaussianity, and noted high-reset Gaussianization. Those established observations are not claimed as new. The new claim is the exact **all-stiffness two-turning-point classification** and its exact threefold inverse-statistic consequence for the minimal symmetric two-wall oscillator. Santra and Basu (2022) and Sarkar, Santra and Basu (2023) study other active reservoirs and their bulk statistics, not this Poisson-reset-Brownian two-wall fourth-moment reentrance. General polynomial-generator methods are standard; the precise rational formula and universal Descartes/witness argument are the substantive specialization.

## Limitations
The explicit result applies to one oscillator, not a theorem for all chain sizes. The wall reset rates and diffusivities must agree. Ideal population excess kurtosis may be poorly conditioned near the two critical points; no finite-sample inverse theorem is established. A later or more general published moment calculation could imply the formula and extremum classification; independent priority review has not been performed.

## References
1. R. Sarkar and P. Roy, *Stationary state of harmonic chains driven by boundary resetting*, arXiv:2307.06127 (first posted 12 July 2023), J. Stat. Mech. (2023) 103204. https://arxiv.org/html/2307.06127v3
2. I. Santra and U. Basu, *Activity driven transport in harmonic chains*, arXiv:2201.00796 (2022). https://arxiv.org/abs/2201.00796
3. R. Sarkar, I. Santra and U. Basu, *Stationary states of activity-driven harmonic chains*, arXiv:2210.09035 (2022). https://arxiv.org/abs/2210.09035
