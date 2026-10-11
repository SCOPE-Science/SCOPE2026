# Sharp finite-order coordinate Sidon constants
## Finding
For integers \(m\ge3\) and \(n\ge2\), set \(\omega=e^{2\pi i/m}\) and let \(r_j(k_1,\ldots,k_n)=\omega^{k_j}\) be the coordinate characters on \((\mathbb Z/m\mathbb Z)^n\). Define
\[
S_{m,n}=\sup_{a\ne0}\frac{\sum_{j=1}^n|a_j|}{\max_{k\in(\mathbb Z/m\mathbb Z)^n}\left|\sum_{j=1}^n a_j\omega^{k_j}\right|}.
\]
Then
\[
S_{m,n}=\frac{n\sin(\pi/(mn))}{\sin(\pi/m)}.
\]
The nonzero extremizers are exactly the coefficient vectors for which, after a permutation, there are \(r>0\), \(\theta\in\mathbb R\), and \(\eta_j\in\mu_m\) such that
\[
a_j=r\eta_j\exp\!\left(i\left(\theta+\frac{2\pi(j-1)}{mn}\right)\right),\qquad 1\le j\le n.
\]
Thus all coefficient moduli are equal, while their arguments modulo \(2\pi/m\) are equally spaced by \(2\pi/(mn)\).

## Assumptions and scope
The result is for finite cyclic order \(m\ge3\) and finite cardinality \(n\ge2\). The order-two Rademacher case is deliberately outside the claim. The norm in the denominator is the uniform norm on the finite compact group \((\mathbb Z/m\mathbb Z)^n\), so the displayed quotient is the ordinary Sidon constant of the coordinate-character set.

## Proof
Let \(\mu_m=\{1,\omega,\ldots,\omega^{m-1}\}\) and put
\[
P_j=a_j\,\operatorname{conv}(\mu_m),\qquad P=P_1+\cdots+P_n.
\]
Each nonzero \(P_j\) is a regular \(m\)-gon centered at the origin. Because the norm is convex, its maximum on \(P\) occurs at a vertex, and every vertex of a Minkowski sum is a sum of vertices of the summands. Hence, with
\[
R=\max_{k\in(\mathbb Z/m\mathbb Z)^n}\left|\sum_{j=1}^n a_j\omega^{k_j}\right|,
\]
we have \(P\subseteq\{z:|z|\le R\}\).

Perimeter is additive under planar Minkowski addition. Since a regular \(m\)-gon of circumradius \(|a_j|\) has perimeter \(2m|a_j|\sin(\pi/m)\),
\[
\operatorname{per}(P)=2m\sin(\pi/m)\sum_{j=1}^n|a_j|.
\]
The edge directions of \(P\) are drawn from the union of the \(m\) edge directions of each summand, so \(P\) has at most \(mn\) sides.

We use the sharp polygon-in-a-disk perimeter lemma: a convex polygon with at most \(N\) sides contained in a disk of radius \(R\) has perimeter at most \(2NR\sin(\pi/N)\), with equality only for a regular \(N\)-gon on the boundary circle. For completeness, a perimeter maximizer exists. Any interior vertex of a maximizing convex polygon can be moved a small distance in the outward gradient direction of the sum of its two incident edge lengths, increasing perimeter while preserving convexity, so every maximizing vertex lies on the circle. If the successive central angles are \(\alpha_1,\ldots,\alpha_N\), then \(\sum\alpha_j=2\pi\) and the perimeter is \(2R\sum_j\sin(\alpha_j/2)\); concavity of sine gives the bound and forces \(\alpha_j=2\pi/N\) at equality. Adding unused zero-angle vertices shows the same bound for at most \(N\) sides.

Applying the lemma with \(N=mn\) gives
\[
2m\sin(\pi/m)\sum_j|a_j|\le2mnR\sin(\pi/(mn)),
\]
and therefore
\[
\frac{\sum_j|a_j|}R\le\frac{n\sin(\pi/(mn))}{\sin(\pi/m)}.
\]

Take equal moduli and choose the coefficient arguments modulo \(2\pi/m\) to be \(0,2\pi/(mn),\ldots,2\pi(n-1)/(mn)\). The edge directions of the \(n\) regular \(m\)-gons then interlace into all \(mn\) equally spaced directions, with equal edge lengths. Their Minkowski sum is a regular \(mn\)-gon, so equality is attained.

Finally suppose equality holds. The disk-perimeter lemma forces \(P\) to have exactly \(mn\) sides and to be regular. Thus no two summands share an edge direction. Every edge of \(P\) comes from exactly one summand and has length \(2|a_j|\sin(\pi/m)\); regularity forces all \(|a_j|\) to be equal. The \(m\) edge directions contributed by a fixed summand occur every \(n\)-th edge of the regular \(mn\)-gon. Consequently the \(n\) summand orientations occupy the \(n\) residue classes modulo \(2\pi/m\), which is precisely the displayed extremizer form, up to permutation, a common phase, and multiplication of each coefficient by an \(m\)-th root of unity.

## Verification
The proof is analytic for every \(m\ge3\) and \(n\ge2\). The accompanying verifier independently enumerates all group points for the displayed extremizers for \(3\le m\le7\) and \(2\le n\le4\), checks the closed formula numerically, and stress-tests random complex coefficient vectors against the sharp bound. These finite checks corroborate but do not replace the all-parameter proof.

Two limiting checks are also structurally consistent. For fixed \(m\),
\[
S_{m,n}\longrightarrow\frac{\pi/m}{\sin(\pi/m)}
\]
as \(n\to\infty\), while for fixed \(n\), \(S_{m,n}\to1\) as \(m\to\infty\).

## Relationship to prior work
Bourgain and Lewko develop qualitative Sidon and Rademacher-Sidon principles for bounded orthonormal systems and characters; their result supplies the archive-era Sidon framework but does not compute this finite cyclic-coordinate constant. Hare and Ramsey study finite-root Kronecker approximation and prove Sidonicity from suitable \((\varepsilon,n)\)-Kronecker control; their theorem is qualitative with respect to the present exact constant and does not give the extremizer class. Seigner proves that the infinite Rademacher system has Sidon constant \(\pi/2\) and uses finite root-of-unity configurations in the order-two setting to approach that limit. The present claim instead treats every finite order \(m\ge3\) and finite size \(n\), with an exact constant and complete equality classification.

Cartwright, Howlett, and McMullen study extreme values of Sidon constants for finite subsets and finite groups. Their general extremal theory is relevant background, but the available statement does not imply the specific intermediate constant above or its regular-polygon equality mechanism.

## Limitations
The order-two case is not claimed here. No claim is made for arbitrary dependent character sets, unequal coordinate orders, or non-coordinate subsets. The originality comparison has a residual risk that an older result in convex geometry or finite-order character theory states the same formula under a polygonal or vector-balancing formulation rather than Sidon terminology.

## References
1. J. Bourgain and M. Lewko, *Sidonicity and variants of Kaczmarz's problem*, arXiv:1504.05290, first posted 21 April 2015.
2. K. E. Hare and L. T. Ramsey, *The Relationship Between \(\varepsilon\)-Kronecker Sets and Sidon Sets*, Canadian Mathematical Bulletin 59 (2016), 521–527, DOI 10.4153/CMB-2016-002-3.
3. J. A. Seigner, *Rademacher variables in connection with complex scalars*, Acta Mathematica Universitatis Comenianae 66 (1997), 329–336.
4. D. I. Cartwright, R. B. Howlett, and J. R. McMullen, *Extreme values for the Sidon constant*, Proceedings of the American Mathematical Society 81 (1981), 531–537.
