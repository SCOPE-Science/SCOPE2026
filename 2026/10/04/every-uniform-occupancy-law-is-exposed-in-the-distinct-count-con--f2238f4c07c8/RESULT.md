# Every uniform occupancy law is exposed in the distinct-count convex hull
## Finding
For every integer \(n\ge 3\), let \(K_{n,m}\) be the number of occupied boxes after \(n\) independent draws from the uniform distribution on \(m\) boxes, and let
\[
\boldsymbol v_{n,m}=\bigl(\Pr\{K_{n,m}=k\}:1\le k\le n\bigr),\qquad m=1,2,\ldots,
\]
with \(\boldsymbol v_{n,\infty}=(0,\ldots,0,1)\). Put \(V_n=\{\boldsymbol v_{n,m}:m=1,2,\ldots,\infty\}\). Then every point of \(V_n\) is an exposed point of \(\operatorname{conv}(V_n)\). Consequently,
\[
\operatorname{ext}\bigl(\operatorname{conv}(V_n)\bigr)=V_n
\]
for every \(n\ge 3\). This proves Conjecture 2(i) of Zhu for all \(n\ge3\).

## Assumptions and scope
The sample size \(n\) is any fixed integer at least \(3\). For finite \(m\), sampling is independent and exactly uniform on \(m\) boxes. The point \(m=\infty\) denotes the limiting non-atomic law, so \(K_{n,\infty}=n\) almost surely. The statement concerns only the extreme-point assertion for the convex hull of the uniform occupancy laws. It does not assert Zhu's stronger Conjecture 2(ii), which asks whether every possible law of the distinct-count statistic for an infinite exchangeable sequence lies in this convex hull.

## Proof
Zhu records the exact coordinates
\[
\Pr\{K_{n,m}=k\}=\frac{S(n,k)(m)_{k\downarrow}}{m^n},
\]
where \(S(n,k)\) is a Stirling number of the second kind. Write \(x=1/m\) and define, for \(1\le k\le n\),
\[
p_{n,k}(x)=S(n,k)x^{n-k}\prod_{j=1}^{k-1}(1-jx).
\]
For finite \(m\), the \(k\)-th coordinate of \(\boldsymbol v_{n,m}\) is \(p_{n,k}(1/m)\). At \(x=0\), one has \(p_{n,n}(0)=1\) and \(p_{n,k}(0)=0\) for \(k<n\), so the same polynomial parametrization includes \(\boldsymbol v_{n,\infty}\).

Each \(p_{n,k}\) has degree at most \(n-1\), and its lowest nonzero power of \(x\) is exactly \(x^{n-k}\), with coefficient \(S(n,k)>0\). Hence the \(n\) polynomials
\[
p_{n,1},p_{n,2},\ldots,p_{n,n}
\]
are linearly independent. Since the space of real polynomials of degree at most \(n-1\) also has dimension \(n\), they form a basis.

Fix a finite \(m_0\). Because \(n\ge3\), the quadratic polynomial
\[
h_{m_0}(x)=-\left(x-\frac1{m_0}\right)^2
\]
has degree at most \(n-1\). Therefore there are real coefficients \(c_1,\ldots,c_n\) such that
\[
h_{m_0}(x)=\sum_{k=1}^n c_k p_{n,k}(x).
\]
Define the linear functional on \(\mathbb R^n\)
\[
L_{m_0}(q_1,\ldots,q_n)=\sum_{k=1}^n c_k q_k.
\]
Then for every finite \(m\),
\[
L_{m_0}(\boldsymbol v_{n,m})=-\left(\frac1m-\frac1{m_0}\right)^2,
\]
and
\[
L_{m_0}(\boldsymbol v_{n,\infty})=-\frac1{m_0^2}.
\]
Thus \(L_{m_0}\) has a unique maximum, equal to \(0\), at \(\boldsymbol v_{n,m_0}\). Hence every finite-\(m\) point is exposed.

For \(m=\infty\), use \(h_\infty(x)=-x\), which also has degree at most \(n-1\) and therefore is a linear combination of the \(p_{n,k}\). The corresponding linear functional equals \(-1/m<0\) on every finite \(m\) and equals \(0\) at \(\boldsymbol v_{n,\infty}\), so the limiting point is exposed as well.

Finally, every extreme point of \(\operatorname{conv}(V_n)\) must belong to \(V_n\). Indeed, any point of the convex hull not in \(V_n\) is, by definition, a finite convex combination involving at least two distinct points of \(V_n\), and grouping one term against the remainder gives a nontrivial segment decomposition. Therefore the exposed points just constructed are exactly all the extreme points.

## Verification
The argument is symbolic. The only structural input is Zhu's occupancy formula and the elementary triangular-basis observation. The accompanying checker independently reconstructs the Stirling-coordinate polynomials, verifies their distinct lowest degrees and the identity \(\sum_k p_{n,k}(x)=1\), solves for supporting functionals representing the quadratic and linear exposing polynomials over exact rational arithmetic for a range of \(n\) and \(m\), and checks the expected strict inequalities on sample grid points. These finite checks are consistency tests; the proof above establishes the theorem for every \(n\ge3\) and every allowed \(m\).

## Relationship to prior work
Zhu's paper formulates, for every \(n\ge3\), the conjecture that the extreme points of \(\operatorname{conv}(V_n)\) are exactly \(V_n\), proves it only for \(n=3\), and later calls the higher-dimensional extreme-point assertion a first step toward the stronger exchangeability conjecture. The paper gives the same Stirling-number coordinate formula used above and reports only numerical convex-hull verification for \(1\le m\le30\) and \(n\le7\). The current arXiv text still presents this assertion as Conjecture 2(i).

Targeted searches for the exact conjecture, the coordinate formula together with convex-hull extremality, occupancy-law moment-curve formulations, and later work citing Zhu found no source proving the all-\(n\) exposed-point statement. Related work on occupancy, exchangeability, Stirling numbers, and random polytopes concerns different convex sets or different probabilistic constraints and does not imply the result here.

## Limitations
This result settles only Conjecture 2(i), the geometry of the convex hull generated by uniform occupancy laws. It does not prove that all laws of \(K_n\) arising from infinite exchangeable sequences lie in that convex hull, so Conjecture 2(ii) remains outside the claim. The originality search cannot exclude an equivalent argument hidden under different terminology for occupancy polytopes or Stirling-coordinate curves, although no such covering result was located and the current version of the motivating paper still labels the assertion conjectural.

## References
1. Theodore Zhu, *The distribution of the number of distinct values in a finite exchangeable sequence*, arXiv:2103.07518, first public version 2021-03-12; Electronic Journal of Probability 27 (2022), DOI:10.1214/22-EJP815.
2. The same paper, Conjecture 2 and Section 4, especially the uniform-occupancy coordinate formula \(\boldsymbol v_{n,m}=\bigl(S(n,k)(m)_{k\downarrow}/m^n:1\le k\le n\bigr)\) and the discussion of numerical verification for \(n\le7\), \(m\le30\).
