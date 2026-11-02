# Unique superattracting period three and a rigorous stability window in a rational interval map

## Finding
For the interval map
\[
K_\mu(x)=\frac{\mu x(1-x)}{1+x},\qquad x\in[0,1],\quad 0<\mu\le 3+2\sqrt2,
\]
there is **exactly one** admissible parameter at which a critical point belongs to a primitive superattracting three-cycle. It is the unique positive root \(\mu_\star>4\) of
\[
Q(\mu)=\mu^6-(5+3\sqrt2)\mu^5+(9+6\sqrt2)\mu^4+(20+14\sqrt2)\mu^3
 -(51+36\sqrt2)\mu^2-(75+53\sqrt2)\mu-(99+70\sqrt2),
\]
and satisfies \(5.6449<\mu_\star<5.645\), numerically \(\mu_\star=5.644927675246680156\ldots\). The unique critical point is \(c=\sqrt2-1\), and the critical orbit at this parameter is approximately
\[
(c,K_{\mu_\star}(c),K_{\mu_\star}^{\,2}(c))
 =(0.4142135623730950,\;0.9685164718418778,\;0.08743991668213845).
\]
Moreover, for **every** real parameter in the entire explicit interval
\[
\boxed{\quad 56449/10000\le\mu\le1129/200\quad}
\]
the map has a locally exponentially attracting primitive three-cycle; its three points belong respectively to the disjoint intervals
\[
J=[413/1000,415/1000],\quad
A=[9685/10000,9686/10000],\quad
B=[872/10000,875/10000].
\]
The three-step derivative on \(J\) has modulus smaller than \(11/100\); hence the three-cycle possesses an open attracting basin. The parameter band is a certified subinterval of a stability window, **not** an asserted maximal stability interval. Uniqueness refers only to the superattracting period-three *parameter* and to the orbit inside these trapping intervals, not to all primitive three-cycles for arbitrary parameters.

## Assumptions and scope
The parameter is real and satisfies \(0<\mu\le3+2\sqrt2\); states lie in \([0,1]\). The given upper parameter bound is exactly the interval-invariance threshold: \(K_\mu\) is nonnegative on \([0,1]\), has a unique critical point \(c=\sqrt2-1\), and its maximum is \(\mu(3-2\sqrt2)\le1\). A primitive three-cycle has least period exactly three. A superattracting cycle has three-step multiplier zero. Local exponential attraction means an open neighborhood of the cycle converges to it geometrically along the appropriate iteration subsequences. No global basin or chaotic-invariant-set classification is asserted.

## Proof
**1. Critical orbit and exact polynomial.** Direct differentiation gives
\[
K_\mu'(x)=\mu\frac{1-2x-x^2}{(1+x)^2},\qquad
K_\mu''(x)=-\frac{4\mu}{(1+x)^3}.
\]
Thus the sole critical point in \([0,1]\) is \(c=\sqrt2-1\). Any superattracting primitive three-cycle must contain \(c\), since its multiplier is the product of derivatives at its three entries and \(K_\mu'\) vanishes nowhere else.

Set \(s=\sqrt2\), \(k=3-2s=c^2\), \(u=k\mu\), \(V=\mu u(1-u)\), \(W=1+u\). Then \(K_\mu(c)=u\), \(K_\mu^2(c)=V/W\), and
\[
K_\mu^3(c)-c
 =\frac{\mu V(W-V)-cW(W+V)}{W(W+V)}.
\]
On the physical parameter range, \(0\le u\le1\), \(V\ge0\), and the denominator is positive. Polynomial expansion in the quadratic field \(\mathbb Q(\sqrt2)\) yields the exact factorization
\[
\mu V(W-V)-cW(W+V)
 =(-577+408\sqrt2)(\mu-1-\sqrt2)Q(\mu).
\]
The leading factor is strictly negative, since \(577^2-2\cdot408^2=1\).

**2. Exhaustive root count.** Let \(P(t)=(1+t)^6Q(4t/(1+t))\). Its coefficients from constant to degree six are
\[
\begin{split}
&-99-70s,\;-894-632s,\;-3801-2686s,\;-6964-4928s,\\
&-3237-2402s,\;-2030-1096s,\;1345-1498s.
\end{split}
\]
All are strictly negative, so \(Q(\mu)<0\) for \(0\le\mu\le4\), including the endpoint by direct evaluation. The coefficients of \(Q(4+t)\), again in ascending powers, are
\[
1345-1498s,\quad2525-1973s,\quad1693-1212s,\quad
644-370s,\quad149-54s,\quad19-3s,\quad1.
\]
Their signs are \((-,-,-,+,+,+,+)\), so Descartes' rule of signs allows at most one positive root of \(Q(4+t)\). Since \(Q(4)<0\) and its leading coefficient is positive, the intermediate value theorem supplies exactly one such root. Exact substitutions show
\[
Q(56449/10000)<0<Q(1129/200),
\]
so the root belongs to the displayed physical parameter band. The other critical-return factor is \(\mu=1+s\); here \(K_\mu(c)=c\), so its critical point has least period one. At the unique root of \(Q\), the trapping argument below places the successive critical images in three pairwise disjoint intervals; hence its least period is exactly three. This proves uniqueness of the admissible superattracting primitive three-cycle parameter.

**3. Uniform stable three-cycle band.** For the entire closed parameter interval \(I=[56449/10000,1129/200]\), exact rational endpoint inequalities give the three strict inclusions
\[
K_\mu(J)\subset\operatorname{int}(A),\qquad
K_\mu(A)\subset\operatorname{int}(B),\qquad
K_\mu(B)\subset\operatorname{int}(J),\quad\mu\in I.
\]
To justify the finite endpoint checks, \(K_\mu\) increases on \([0,c]\), decreases on \([c,1]\), and is increasing in \(\mu\) for \(0<x<1\). Its maximum on \(J\) occurs at \(c\); its minimum there is at one of the two endpoints. The interval \(A\) lies to the right of \(c\), and \(B\) to the left. Thus it suffices to verify
\[
\begin{array}{ll}
\min\{K_{\mu_-}(413/1000),K_{\mu_-}(415/1000)\}>9685/10000,&
\mu_+(3-2\sqrt2)<9686/10000,\\
K_{\mu_-}(9686/10000)>872/10000,&
K_{\mu_+}(9685/10000)<875/10000,\\
K_{\mu_-}(872/10000)>413/1000,&
K_{\mu_+}(875/10000)<415/1000,
\end{array}
\]
where \(\mu_-=56449/10000\) and \(\mu_+=1129/200\). These are exact rational inequalities except for the single expression containing \(\sqrt2\), which is also certified by exact quadratic-field arithmetic.

Because \(K_\mu''<0\), the derivative decreases with \(x\); at each fixed endpoint its absolute value grows linearly with \(\mu\). Exact endpoint evaluations establish uniformly
\[
\sup_{I\times J}|K_\mu'|<1/100,\qquad
\sup_{I\times A}|K_\mu'|<11/4,\qquad
\sup_{I\times B}|K_\mu'|<4.
\]
Consequently \(K_\mu^3:J\to\operatorname{int}(J)\) is a strict contraction with Lipschitz constant at most \(11/100\). The contraction mapping theorem produces a unique point \(p_\mu\in J\) fixed by the third iterate. Its first and second images are in \(A\) and \(B\), which are pairwise disjoint from \(J\); thus it is a primitive three-cycle. Strict contraction and continuity provide an open local attracting basin, completing the proof.

## Verification
Run the standalone Python 3 standard-library program `verify.py`. It checks the factorization coefficient-by-coefficient in \(\mathbb Q(\sqrt2)\), verifies the transformed-polynomial Descartes signs and the exact root bracket, and certifies each strict interval inclusion and derivative bound using rational arithmetic and exact signs of quadratic surds. Its auxiliary high-precision decimal orbit calculation is illustrative only. The analytic proofs of uniqueness, existence, and stability above do not use finite orbit sampling or floating-point bounds.

## Relationship to prior work
Kumar, Alzabut, Kumari, Rani, and Chugh (2022) introduced this rational map and studied fixed points, period-doubling, bifurcation diagrams, and numerical chaos indicators. The present statement supplies an exact algebraic primitive-period-three critical return and a complete rigorous attracting three-cycle parameter **subinterval**, not supplied by their numerical diagrams. Conejero, Lizama, and Quijada (2025) studied the larger family \(\mu x(1-x)/(1+\lambda x)\), and estimated first bifurcation locations numerically; their presented results do not imply the sextic root uniqueness or the exact stable-three-cycle band for \(\lambda=1\). Renu, Ashish, and Chugh (2024) studied a different higher-power family \(\rho x(1-x)^\beta/(1+x)\) with \(\beta>1\), including numerical period-three observations for other powers. Liu and Zhong (2025) investigated period-doubling for a broader rational family and did not establish the present period-three certificate. General results on unimodal maps can ensure that a critical periodic orbit is superattracting, but do not supply the explicit uniqueness and exact band for this rational family.

## Limitations
The displayed attracting band is not claimed to be maximal. Other period-three cycles, other attractors, and chaotic invariant repellers may coexist; this result does not exclude chaos elsewhere. A local attracting three-cycle disproves only a blanket assertion of uniformly chaotic/no-attracting-cycle behavior over the entire high-parameter range. The algebraic calculations have been checked with a standalone executable certificate but not by an independent mathematical auditor. An unindexed equivalent result remains a publication-priority risk.

## References
1. A. Kumar, J. Alzabut, S. Kumari, M. Rani, R. Chugh, “Dynamical properties of a novel one dimensional chaotic map,” *Mathematical Biosciences and Engineering* 19 (2022), 2489–2505. DOI: 10.3934/mbe.2022115. Public full text: https://www.aimspress.com/aimspress-data/mbe/2022/3/PDF/mbe-19-03-115.pdf.
2. J. A. Conejero, C. Lizama, D. Quijada, “Dynamical Properties for a Unified Class of One-Dimensional Discrete Maps,” *Mathematics* 13 (2025), 518. DOI: 10.3390/math13030518. Open manuscript: https://riunet.upv.es/server/api/core/bitstreams/187e1322-d70a-46c0-9fe1-6eb964e699cc/content.
3. Renu, Ashish, R. Chugh, “Discrete superior dynamics of a generalized chaotic system,” *Arabian Journal of Mathematics* (2024). DOI: 10.1007/s40065-024-00464-1.
4. L. Liu, X. Zhong, “Analysis and anti-control of period-doubling bifurcation for the one-dimensional discrete system with three parameters and a square term,” *AIMS Mathematics* (2025). DOI: 10.3934/math.2025150.
