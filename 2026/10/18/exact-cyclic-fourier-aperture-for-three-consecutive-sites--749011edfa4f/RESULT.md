# Exact cyclic Fourier aperture for three consecutive sites

## Finding

For an integer \(N\ge3\), put \(\zeta_N=e^{2\pi i/N}\). A nonnegative Fourier quadrature in the integer aperture \([0,D]\), where \(0\le D<N\), consists of weights \(w_0,\ldots,w_D\ge0\), not all zero, satisfying
\[
\sum_{j=0}^{D}w_j\zeta_N^{kj}=0\quad(k=1,2).
\]
After normalizing \(\sum_jw_j=1\), these equations are exactly the Parseval conditions for positively weighted restricted Fourier characters on the three consecutive sites \(\{0,1,2\}\subset\mathbb Z/N\mathbb Z\). Define the *cyclic Fourier aperture* to be the smallest \(D\) for which such weights exist, permitting translation of the interval of allowed frequencies.

**Theorem.** For every integer \(N\ge3\), the exact minimum aperture is
\[
\boxed{D_{\min}(N)=\left\lceil\frac{2N}{3}\right\rceil.}
\]
At the minimum aperture there exists a nonnegative quadrature supported on at most **five** distinct frequency bins, with both aperture endpoints carrying positive weight. An explicit symmetric six-bin rule and a finite affine-pruning step construct such a rule. If \(3\mid N\), the optimal rule is unique after fixing the interval: it puts weight \(1/3\) at each of the three frequencies \(0,N/3,2N/3\). No minimal-number-of-frequencies assertion is made for the nondivisible orders.

## Assumptions and scope

The Fourier aperture measures the length of the *shortest consecutive cyclic interval containing the support*, not the number of active frequencies. Translating the interval multiplies each Fourier moment by a unimodular factor and does not affect its vanishing. Nonnegative inactive weights are allowed, while all weights assigned to the constructed nonempty support are positive. The frequency grid is the \(N\)-th roots of unity; the three spatial sampling sites are consecutive and have common step one. The theorem is not asserted for arbitrary spatial sites, higher moment orders, or prescribed equal weights.

The Parseval equivalence follows because the Gram matrix of the vectors \(\sqrt{w_j}(1,\zeta_N^j,\zeta_N^{2j})\) is the identity precisely when the zeroth Fourier moment is one and the first two moments vanish. The conjugate moment equations then follow automatically.

## Proof

**1. The sharp lower bound and equality at the continuous threshold.** Fix an admissible interval of integer length \(D\), translate it to \([0,D]\), and rotate its points by \(e^{-\pi iD/N}\). The resulting angles \(\theta_j=\pi(2j-D)/N\) lie in \([-R,R]\), where \(R=\pi D/N<\pi\). The first two centered complex moments still vanish. With \(u=\cos\theta\), this implies
\[
\mathbb E[u]=0,\qquad \mathbb E[u^2]=\tfrac12,
\]
for the normalized nonnegative discrete measure. The quadratic dual certificate
\[
Q(u)=(1-u)(u+\tfrac12)=\tfrac12+\tfrac12u-u^2
\]
therefore has expectation zero. If \(D<2N/3\), then \(R<2\pi/3\), so \(u\in[\cos R,1]\) with \(\cos R>-1/2\). Hence \(Q(u)\ge0\), with equality only at \(u=1\). Its zero expectation would force all measure onto \(\theta=0\), contradicting \(\mathbb E[u]=0\). Consequently every admissible integer length satisfies \(D\ge\lceil2N/3\rceil\).

If equality \(R=2\pi/3\) is possible, then \(3\mid N\) and the zeros of \(Q\) in the interval occur only at \(\theta=0,\pm2\pi/3\). The first and second moment equations force their three weights to be \(1/3\) each: they are the inverse three-point discrete Fourier transform of the vector \((1,0,0)\). This proves uniqueness at divisible orders.

**2. The explicit symmetric construction.** Put \(D=\lceil2N/3\rceil\), \(R=\pi D/N\), and \(u_0=\cos R\le-1/2\). Let
\[
u_\star=-\frac1{2u_0}\in[1/2,1],\qquad r_\star=\arccos u_\star\in[0,\pi/3].
\]
The endpoint frequency pair \(j=0,D\) has centered angles \(\pm R\). Every internal symmetric frequency pair has centered angles \(\pm r\), where
\[
r=\frac{\pi q}{N},\qquad q\equiv D\pmod2,\quad 0\le q\le D-2.
\]
For \(q=0\), the pair reduces to a single center frequency. Choose internal grid radii \(r_a\le r_\star\le r_b\) that are either adjacent or identical if \(r_\star\) is itself a grid radius. Their existence is proved in Step 3. Set \(u_1=\cos r_b\le u_\star\) and \(u_2=\cos r_a\ge u_\star\).

If \(u_1<u_2\), define the *total* masses assigned to the three symmetric groups by
\[
\begin{aligned}
W_0&=\frac{\frac12+u_1u_2}{(u_0-u_1)(u_0-u_2)},\\
W_1&=\frac{\frac12+u_0u_2}{(u_1-u_0)(u_1-u_2)},\\
W_2&=\frac{\frac12+u_0u_1}{(u_2-u_0)(u_2-u_1)}.
\end{aligned}
\]
These are the three-node Lagrange weights representing the linear functional \(L(1)=1\), \(L(u)=0\), \(L(u^2)=1/2\), so
\[
\sum_{i=0}^2W_i=1,\qquad \sum_{i=0}^2W_i u_i=0,\qquad
\sum_{i=0}^2W_i u_i^2=\tfrac12.
\]
All are nonnegative. Indeed \(u_0<0\), \(u_1\le -1/(2u_0)\le u_2\), and the denominator signs give \(W_1,W_2\ge0\). Moreover \(u_1,u_2\ge0\) by Step 3, so \(W_0>0\). Assign half of each group mass to each member of its symmetric pair, or all of it to a central singleton. Odd sine moments cancel, and \(\cos(2\theta)=2u^2-1\); the three displayed identities therefore give both required complex Fourier moments zero. Omit any zero-mass groups. The initial explicit symmetric construction has no more than six active frequencies, including both endpoints.

If \(r_\star\) lies on the internal grid, take only the endpoint group and that internal group, with respective masses
\[
W_0=\frac{u_\star}{u_\star-u_0}>0,\qquad
W_\star=\frac{-u_0}{u_\star-u_0}>0.
\]
Their first moment is zero and their second cosine moment is zero because \(u_0u_\star=-1/2\). The special order \(N=4\) has \(D=3\), internal radius \(\pi/4\), and the construction assigns weight \(1/4\) to each of the four frequencies. At \(3\mid N\), it reduces to the three equally weighted cube-root positions of Step 1.

**3. Internal-grid bracketing and positive endpoint mass.** If \(D\) is even, the internal grid includes radius zero. If \(D\) is odd, then \(N\equiv1\pmod3\). Its smallest internal radius is \(\pi/N\), and we claim \(r_\star\ge\pi/N\). Here \(R=2\pi/3+\pi/(3N)\). Write \(x=\pi/(3N)\) and \(y=\tan x\). The claimed inequality is equivalent to
\[
(\cos x+\sqrt3\sin x)\cos(3x)\ge1,
\]
which, after multiplying by \((1+y^2)^2\), is exactly
\[
y(y+\sqrt3)(2-\sqrt3-y)(y+2+\sqrt3)\ge0.
\]
This holds since \(0\le x\le\pi/12\) for \(N\ge4\), and therefore \(0\le y\le2-\sqrt3\). Thus the smallest internal radius never exceeds \(r_\star\).

For \(N\ge6\), the largest internal radius equals \(\pi(D-2)/N\ge\pi/3\ge r_\star\). The remaining order \(N=5\) has largest internal radius \(2\pi/5>\pi/3\), while \(N=4\) was handled separately. Hence two bracketing internal grid radii always exist.

Finally, both bracketing internal radii are at most \(\pi/2\). For \(N\ge12\), the upper bracket is at most \(r_\star+2\pi/N\le\pi/2\). The nondivisible cases \(5\le N<12\) are \(N=5,7,8,10,11\); direct inspection of their internal radius grids gives respective upper bounds \(2\pi/5,3\pi/7,\pi/4,3\pi/10,4\pi/11\), all below \(\pi/2\). Hence \(u_1,u_2\ge0\), as used above.

**4. Five-bin compression without enlarging the aperture.** For every allowed frequency \(j\), form the moment point
\[
\Phi_j=(\operatorname{Re}\zeta_N^j,\operatorname{Im}\zeta_N^j,
\operatorname{Re}\zeta_N^{2j},\operatorname{Im}\zeta_N^{2j})\in\mathbb R^4.
\]
The symmetric rule expresses the origin as a convex combination of at most six such points. Carathéodory's theorem reduces this combination to at most five points inside the *same* aperture. More explicitly, if six positive weights are present, find a nonzero real null vector \((h_j)\) of the five-row matrix whose columns are \((1,\Phi_j)\). Since \(\sum h_j=0\), the vector has positive and negative entries. Increase the weights along this null vector until the first becomes zero; no other weight becomes negative and all five moment equations are preserved. Thus at most five nonzero weights remain. Both endpoints must remain in the support: otherwise the resulting support would fit into an interval of length at most \(D-1\), contradicting Step 1. This is a finite constructive compression, not an assertion that five is always the least possible number of nodes. The theorem follows.

## Verification

The accompanying standalone `verify.py` generates the displayed pre-compression nonnegative symmetric weights using 80-decimal-place arithmetic for every integer \(3\le N\le400\), and checks normalizations, positive active weights, occupied endpoints, at most six support nodes, and both complex Fourier moments to tolerance \(10^{-49}\). It performs 796 high-precision complex-moment comparisons and checks the strict dual-certificate prerequisite for every smaller integer aperture. The program returned `VERIFY_OK`. These finite checks are supplementary; Steps 1–4 prove the result for every integer \(N\ge3\).

## Relationship to prior work

The classical trigonometric moment problem, positive quadrature, and positive Fourier frames supply the background, but prescribe neither this finite-grid aperture invariant nor the constructive threshold formula. Tan and Zhang give a 2026 sharp *cyclotomic-divisibility* diameter theorem and emphasize a lower-bound mechanism from initial vanishing moments. Their published abstract does not state the finite-grid two-moment construction established here. Cyclotomic divisibility requires all primitive-conjugate zeros and is stronger than the two specified moment equations in composite orders. Kunis discusses positive generalized trigonometric quadrature and covering radii, but the abstract inspected does not determine this consecutive finite-grid aperture. A published result titled *Sharp positive Fourier sampling on three consecutive cyclic sites* determines the **minimum number of nonzero sampling frequencies**, which is a distinct optimization from the **smallest consecutive arc containing the sample frequencies**; its full mathematical statement, proof, and limitations were compared.

## Limitations

This is a discrete two-moment theorem, not a general higher-order moment-width result. It does not classify all minimal-aperture supports or minimize their number of active frequencies for \(3\nmid N\). The proof needs positive adjustable weights; equal-weight rules may have a larger minimum aperture. The relevant 2026 preprints and a classical positive-quadrature survey were available only in abstracts during this examination; equivalently formulated earlier arc-constrained quadrature results remain a historical-priority risk. The numerical checker is not a substitute for the all-orders analytic proof. Independent scientific validation has not been performed.

## References

1. Hu Tan and Ying Zhang, *Sharp Diameter Bounds for Nonnegative Cyclotomic Multiples*, arXiv:2609.07646v1, first public 2026-09-07. https://arxiv.org/abs/2609.07646
2. Stefan Kunis, *Positive quadrature and mobile sampling of multivariate trigonometric polynomials*, arXiv:2608.11915v1, first public 2026-08-12. https://arxiv.org/abs/2608.11915
3. F. Peherstorfer, *Positive trigonometric quadrature formulas and quadrature on the unit circle*, Mathematics of Computation 80 (2011), arXiv:1001.2451. https://arxiv.org/abs/1001.2451
4. *Sharp positive Fourier sampling on three consecutive cyclic sites* (online mathematical research record, 2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-positive-fourier-sampling-on-three-consecutive-cyclic-site--29fa16b8c55a
