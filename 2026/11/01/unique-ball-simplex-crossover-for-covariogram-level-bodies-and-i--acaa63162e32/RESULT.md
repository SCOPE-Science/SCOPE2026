# Unique ball–simplex crossover for covariogram level bodies and its dimension law

## Finding
Let \(d\ge2\) be an integer and define \(c_d=\tfrac12\binom{2d}{d}^{1/d}\). For a convex body \(K\subset\mathbb R^d\), put \(C_\theta K=\{z:|K\cap(K+z)|\ge\theta|K|\}\) and
\[
Q_d(K,s)=\frac{|C_{s^d}K|^{1/d}}{2|K|^{1/d}},\qquad0\le s\le1.
\]
For any nondegenerate simplex \(\Delta\), the known exact value is \(Q_d(\Delta,s)=c_d(1-s)\). For any Euclidean ball \(B\), write \(Q_d(B,s)=r_d(s)\). The radius \(r_d(s)\in(0,1)\) is uniquely determined by
\[
I_{1-r_d(s)^2}\!\left(\frac{d+1}{2},\frac12\right)=s^d,
\]
where \(I_z(a,b)=B_z(a,b)/B(a,b)\) is the regularized incomplete beta integral.

**Theorem.** There exists exactly one \(s_d\in(0,1)\) at which the ball and simplex values agree. It is the unique nontrivial solution of
\[
I_{1-c_d^2(1-s_d)^2}\!\left(\frac{d+1}{2},\frac12\right)=s_d^d,
\qquad 0<c_d(1-s_d)<1.
\]
For every \(0<s<s_d\), \(Q_d(B,s)<Q_d(\Delta,s)\); the reverse strict inequality holds for every \(s_d<s<1\). Moreover, with \(\sigma_d=(c_d^2-1)/(c_d^2+1)\),
\[
s_d>\sigma_d,
\qquad s_d=\frac35-\frac{7\log(\pi d)+18\log3-27\log2}{50d}
+O\!\left(\frac{(\log d)^2}{d^2}\right).
\]
Consequently the ball–simplex crossover volume fraction satisfies
\[
(s_d)^d\sim\frac{2^{9/10}}{\pi^{7/30}3^{3/5}}\left(\frac35\right)^d d^{-7/30}.
\]
In particular, every parameter \(0<\theta<(s_d)^d\) gives an explicit ball witness strictly below the simplex value in the normalized \(\theta\)-convolution inequality. This is a two-family comparison, **not** a determination of the global infimum over all convex bodies.

## Assumptions and scope
A convex body is compact, convex, and has nonempty interior. Volume is \(d\)-dimensional Lebesgue measure. The relevant convolution body uses the *same body twice*: in the standard two-body notation \(K+_\theta L\), take \(L=-K\). All affine images of a simplex, respectively all ellipsoids, have their respective common normalized values. The theorem holds for every integer \(d\ge2\), for all \(s\in(0,1)\), and for the specified crossover \(s_d\). Endpoint equalities at \(s=1\) are not an additional crossover: both ratios vanish there.

## Proof
**1. Exact lens profile.** Let \(B\) be the unit Euclidean ball, let \(\kappa_j=\pi^{j/2}/\Gamma(1+j/2)\), and let the two ball centers be separated by \(2r\), \(0\le r\le1\). Their overlap is the union of two equal caps, so its normalized volume is
\[
\Theta_d(r)=\frac{2\kappa_{d-1}}{\kappa_d}\int_r^1(1-t^2)^{(d-1)/2}\,dt
=I_{1-r^2}\!\left(\frac{d+1}{2},\frac12\right).
\]
Direct differentiation gives \(\Theta'_d(r)=-(2\kappa_{d-1}/\kappa_d)(1-r^2)^{(d-1)/2}<0\) for \(0<r<1\). As \(C_{s^d}B=2r_d(s)B\), its normalized ratio is exactly \(r_d(s)\), and \(r_d\) is real analytic on \((0,1)\). The classical Rogers–Shephard simplex identity yields \(Q_d(\Delta,s)=c_d(1-s)\).

**2. Exactly one nontrivial crossing.** The Brunn–Minkowski inequality applied to intersections shows that the \(d\)-th root of the normalized covariogram is concave on its support. Thus its superlevel balls satisfy
\[
(1-\lambda)(2r_d(s)B)+\lambda(2r_d(t)B)
\subseteq 2r_d((1-\lambda)s+\lambda t)B,
\]
so \(r_d\) is concave and continuous on \([0,1]\). Since \(r_d(1)=0\), the quotient \(h_d(s)=r_d(s)/(1-s)\) is nondecreasing for \(s<1\). It is strictly increasing: if it were constant on an interval, concavity together with \(r_d(1)=0\) would force an affine segment, and analyticity would force \(r_d\) affine on \((0,1)\), contradicted by the distinct endpoint slopes below. In fact \(r_d(0)=1\), so \(h_d(0)=1<c_d\). Differentiating the inverse lens equation at \(s=1\),
\[
\lim_{s\uparrow1}h_d(s)=\ell_d:=\frac{d\kappa_d}{2\kappa_{d-1}}>c_d.
\]
For this last inequality, \(c_d<2\). For odd \(d\ge3\), \(\ell_d\ge\ell_3=2\); for even \(d\ge4\), \(\ell_d\ge\ell_4=3\pi/4>2\), by \(\ell_{d+2}/\ell_d=(d+1)/d\); the remaining case has \(\ell_2=\pi/2>c_2=\sqrt{3/2}\). By strict monotonicity and continuity, \(h_d(s)=c_d\) has a unique solution \(s_d\in(0,1)\), giving both strict comparison directions and the asserted implicit equation.

**3. Strict improvement over the simple spherical bound.** The intersection of balls centered at \(\pm ru\) lies strictly in volume inside \(\sqrt{1-r^2}B\) whenever \(0<r<1\). Hence the level parameter obeys \(s^d< (1-r_d(s)^2)^{d/2}\), so \(r_d(s)<\sqrt{1-s^2}\). The expression \(\sqrt{1-s^2}\) equals \(c_d(1-s)\) at \(s=\sigma_d=(c_d^2-1)/(c_d^2+1)\). Therefore \(h_d(\sigma_d)<c_d\); strict increase gives \(s_d>\sigma_d\).

**4. High-dimensional asymptotics.** The central binomial coefficient expansion implies
\[
c_d=2-\frac{\log(\pi d)}d+O\!\left(\frac{(\log d)^2}{d^2}\right).
\]
Uniformly for \(r\) in a compact subinterval of \((0,1)\), endpoint integration by parts and the gamma-ratio asymptotic yield
\[
\Theta_d(r)=\sqrt{\frac{2}{\pi d}}\,
\frac{(1-r^2)^{(d+1)/2}}r\bigl(1+O(d^{-1})\bigr).
\]
For completeness, integration by parts bounds the correction to \(\int_r^1(1-t^2)^{(d-1)/2}dt\) by a relative \(O(d^{-1})\), uniformly if \(r\ge r_0>0\). At any fixed \(s\in(1/2,1)\), the sign of \(\Theta_d(c_d(1-s))-s^d\), when defined, converges to that of \(\sqrt{1-4(1-s)^2}-s\). Its unique non-endpoint zero in this interval is \(s=3/5\), so the strict unique crossing satisfies \(s_d\to3/5\).

Set \(s_d=3/5+\delta_d\), \(r_d=c_d(1-s_d)\), and \(q_d=1-r_d^2\). Taking logarithms in \(s_d^d=\Theta_d(r_d)\) gives
\[
d\left(\log s_d-\tfrac12\log q_d\right)=
-\tfrac12\log d+\tfrac12\log(2/\pi)+\tfrac12\log q_d-\log r_d+O(d^{-1}).
\]
At \((s,c)=(3/5,2)\), the function \(f(s,c)=\log s-\tfrac12\log(1-c^2(1-s)^2)\) has derivatives \(f_s=-25/9\), \(f_c=8/9\), and the remaining constant on the right is \(\log(3/4)+\tfrac12\log(2/\pi)\). An initial mean-value estimate gives \(\delta_d=O((\log d)/d)\); Taylor expansion then yields
\[
\delta_d=-\frac{7\log(\pi d)+18\log3-27\log2}{50d}
+O\!\left(\frac{(\log d)^2}{d^2}\right).
\]
Exponentiation of \(d\log(s_d/(3/5))\) gives the displayed sharp crossover-volume constant and polynomial correction.

## Verification
The bundled `CHECK.py` independently compares the regularized beta representation with direct one-dimensional cap integration, checks the explicit planar disk-lens formula, verifies the derivative formula, solves the nontrivial crossing across multiple dimensions, checks the strict improvement beyond \(\sigma_d\), and compares the asymptotic formula against increasing dimensions. It passed 749 numerical consistency checks in the tested environment; numerical tests serve only as corroboration. The proof above is analytic for all \(d\ge2\).

## Relationship to prior work
Langharst and Wang (first public 17 September 2026) characterize simplices via mixed-volume inequalities and use covariogram arguments; this motivates comparing their geometric fingerprint with that of the Euclidean ball at every overlap level. Alonso-Gutiérrez, Jiménez and Villa (2013) introduced the relevant \(\theta\)-convolution-body framework. Alonso-Gutiérrez and Martín Goñi (2023/2024) established its sharp simplex branch on a high-overlap interval. Martín Goñi's 27 October 2026 preprint, specifically Section 4.2, obtains the simpler ball witness \(r_d(s)<\sqrt{1-s^2}\) and the exclusion range \(s\le\sigma_d\); that paper does **not** state the unique *exact* ball–simplex crossing or its high-dimensional second-order law. Haddad's 2024 preprint / 2025 article treats volume maximization for planar self-convolution bodies and does not compare these two canonical families at all levels. The comparison here is between the actual two family-specific values, not a claim that either family globally minimizes the functional.

## Limitations
This theorem determines the relative ordering of Euclidean balls (equivalently ellipsoids) and simplices only. It does not identify the global minimizing convex body below the established sharp simplex interval. The crossing is implicit for general dimension, not expressed in elementary constants. The precise high-dimensional statement holds as integer \(d\to\infty\). A full historical priority assessment, especially older spherical-lens level-set studies, remains open; no independent audit has been performed.

## References
- D. Langharst and S. Wang, *The Bézout inequality for mixed volumes characterizes simplices*, arXiv:2609.20380v1 (first submitted 2026-09-17), https://arxiv.org/abs/2609.20380.
- J. Martín Goñi, *Improved Brunn–Minkowski inequality for θ-convolution bodies*, arXiv:2610.37066v1 (first submitted 2026-10-27), https://arxiv.org/html/2610.37066v1; Sections 2 and 4.2.
- D. Alonso-Gutiérrez and J. Martín Goñi, *Brunn–Minkowski inequality for θ-convolution bodies via Ball's bodies*, J. Geom. Anal. 34, 58 (2024), first online 2023-12-29, https://pmc.ncbi.nlm.nih.gov/articles/PMC10756892/.
- J. Haddad, *On the volume of convolution bodies in the plane*, arXiv:2405.00212 (first submitted 2024-04-30), later J. Geom. Anal. 35, 314 (2025), https://link.springer.com/article/10.1007/s12220-025-02143-9.
- D. Alonso-Gutiérrez, C. H. Jiménez and R. Villa, *Brunn–Minkowski and Zhang inequalities for convolution bodies*, Adv. Math. 238 (2013), 50–69, DOI 10.1016/j.aim.2013.01.013.
