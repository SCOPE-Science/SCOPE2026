# Sharp \(\Lambda(p)\) constants for order-four character pairs
## Finding
Let \(G\) be a compact abelian group with normalized Haar measure and let \(\lambda_0,\lambda_1\in\widehat G\) be distinct characters such that \(\chi=\lambda_1\overline{\lambda_0}\) has order exactly \(4\). For every real \(p>2\), define
\[
K_p=\sup_{(a,b)\ne(0,0)}\frac{\|a\lambda_0+b\lambda_1\|_{L^p(G)}}{(|a|^2+|b|^2)^{1/2}}.
\]
Then
\[
K_p^p=
\begin{cases}
2^{p/2-2}+\tfrac12,&2<p<4,\\[1mm]
\tfrac32,&p=4,\\[1mm]
\tfrac12\!\left[(1+2^{-1/2})^{p/2}+(1-2^{-1/2})^{p/2}\right],&4<p<6,\\[1mm]
\tfrac52,&p=6,\\[1mm]
2^{p/2-2}+\tfrac12,&p>6.
\end{cases}
\]
Every nonzero extremizer has \(|a|=|b|\). If \(\phi=\arg(b\overline a)\), understood modulo \(\pi/2\), then equality requires \(\phi\equiv0\pmod{\pi/2}\) for \(2<p<4\) and for \(p>6\), requires \(\phi\equiv\pi/4\pmod{\pi/2}\) for \(4<p<6\), and permits every relative phase at \(p=4\) and \(p=6\). Thus the order-four character pair has two exact phase transitions, with a re-entrant axis/diagonal/axis extremizer pattern across \(p=4\) and \(p=6\).

## Assumptions and scope
The Haar measure on \(G\) is normalized to mass one. The relative character \(\chi=\lambda_1\overline{\lambda_0}\) is assumed to have exact order \(4\), so the pushforward of Haar measure by \(\chi\) is the uniform measure on \(\{1,i,-1,-i\}\). The claim concerns the sharp \(L^p/L^2\) constant of this two-dimensional character span for every real \(p>2\); it does not assert a formula for character pairs of arbitrary torsion order.

## Proof
Factor out \(\lambda_0\), which has modulus one. Normalize \(|a|^2+|b|^2=1\), put \(s=p/2>1\),
\[
t=2|a||b|\in[0,1],\qquad \phi=\arg(b\overline a),
\]
and use that \(\chi\) is uniform on the fourth roots of unity. Then
\[
\|a+b\chi\|_p^p=\frac14\sum_{k=0}^3\left(1+t\cos(\phi+k\pi/2)\right)^s.
\]
The expression is invariant under \(\phi\mapsto\phi+\pi/2\), \(\phi\mapsto-\phi\), and \(\phi\mapsto\pi/2-\phi\), so it suffices to take \(0\le\phi\le\pi/4\). Write \(c=\cos\phi\), \(d=\sin\phi\), and
\[
g_s(u)=\frac{(1+u)^s+(1-u)^s}{2}.
\]
Then
\[
F_s(t,\phi)=\frac12\bigl(g_s(tc)+g_s(td)\bigr).
\]
For \(s>1\), \(g_s'(u)>0\) for \(u>0\). Hence \(F_s(t,\phi)\) is strictly increasing in \(t\) on \((0,1]\), and every nonzero extremizer must have \(t=1\), equivalently \(|a|=|b|\).

For balanced coefficients set
\[
H_s(\phi)=F_s(1,\phi)=\frac12\bigl(g_s(c)+g_s(d)\bigr).
\]
On \(0<\phi<\pi/4\),
\[
H_s'(\phi)=\frac{cd}{2}\bigl(q_s(d)-q_s(c)\bigr),
\qquad
q_s(u)=\frac{g_s'(u)}u.
\]
A direct integral identity gives
\[
q_s(u)=s(s-1)\frac1{2u}\int_{-u}^u(1+x)^{s-2}\,dx.
\]
Thus \(q_s(u)\) is a positive multiple of the symmetric-interval average of \((1+x)^{s-2}\). By the Hermite--Hadamard inequality, such averages increase strictly with the interval radius when the integrand is strictly convex and decrease strictly when it is strictly concave. Therefore \(q_s\) is strictly increasing for \(1<s<2\), strictly decreasing for \(2<s<3\), and strictly increasing for \(s>3\). At \(s=2\) the integrand is constant, while at \(s=3\) it is affine, so the symmetric average is constant in both critical cases.

Since \(0<d<c<1\), it follows that \(H_s\) decreases on \((0,\pi/4)\) for \(1<s<2\), increases there for \(2<s<3\), and decreases there for \(s>3\). At \(s=2\) and \(s=3\), \(H_s\) is independent of \(\phi\). Hence the maximizing phases are exactly the classes stated in the finding.

At the axis phase \(\phi=0\), the four squared sample magnitudes are
\[
(2,1,0,1),
\]
so
\[
H_s(0)=\frac{2^s+2}{4}=2^{s-2}+\frac12.
\]
At the diagonal phase \(\phi=\pi/4\), they are
\[
(1+2^{-1/2},1+2^{-1/2},1-2^{-1/2},1-2^{-1/2}),
\]
so
\[
H_s(\pi/4)=\frac12\left[(1+2^{-1/2})^s+(1-2^{-1/2})^s\right].
\]
Substituting \(s=p/2\) gives the displayed piecewise formula. At \(s=2\) these values both equal \(3/2\), and at \(s=3\) they both equal \(5/2\); the derivative argument shows that in each critical case every relative phase is extremal.

## Verification
The proof above is analytic and covers every real \(p>2\). For a reproducible stress test, run `python3 verify_order4_lambda.py`. The packaged replay sampled \(208656\) coefficient-balance/phase points over sixteen exponents spanning all five regimes, checked both critical phase-flat moments on a separate phase grid, and returned

`VERIFY_OK grid_checks=208656 max_excess=8.882e-16 max_formula_err=0.000e+00`.

The finite floating-point grid is corroborative only; it is not used as a proof of the continuum statement.

## Relationship to prior work
Michels' archive-era paper defines \(\Lambda(p)\)-sets and their sharp constants \(K_p(\Lambda)\) for character systems, and its main theorem concerns infinite sets that are \(\Lambda(p)\)-sets for all \(p>2\) via limit orders of operator ideals. The inspected six-page full text does not state a sharp finite two-character constant, an order-four relative-character calculation, or the two-transition extremizer classification proved here. Targeted searches were also made under the equivalent fourth-root random-variable formulation and under two-dimensional Fourier-subspace terminology; no statement implying the piecewise formula or the \(p=4,6\) phase transitions was located.

The structural point is not merely another even-moment evaluation. The maximizing phase changes from an axis phase to a diagonal phase and then back to an axis phase, with the two changes forced by the convexity/concavity changes of \((1+x)^{p/2-2}\). This yields the complete real-\(p\) profile, including the non-even interval \(4<p<6\).

## Limitations
The theorem treats relative character order exactly \(4\) and two characters only. It does not classify sharp constants for arbitrary finite character order or for larger character sets. The originality assessment is search-based and cannot exclude an unindexed equivalent calculation under different terminology, especially in finite-dimensional \(L^p\) or roots-of-unity inequality literature.

## References
1. C. Michels, *\(\Lambda(p)\)-sets and the limit order of operator ideals*, arXiv:math/9904176, first posted 1999-04-30.
