# Near-balanced signature maximizers for complete-intersection surfaces in projective four-space
## Finding
Let \(S\ge6\), and let
\[
X_{a,b}\subset\mathbb P^4_{\mathbb C}
\]
be a smooth complete-intersection surface of bidegree \((a,b)\), where
\[
2\le a\le b,\qquad a+b=S.
\]
Then
\[
\sigma(X_{a,b})=\frac{ab(5-a^2-b^2)}{3}<0.
\]
For fixed \(S\), the absolute signature has a sharp and unexpectedly near-balanced maximum.

If \(S\) is even, the unique maximizing bidegree is
\[
\left(\frac S2-1,\frac S2+1\right),
\]
and
\[
\max |\sigma(X_{a,b})|
=\frac{S^4-10S^2+24}{24}.
\]

If \(S\) is odd, the only maximizing bidegrees are
\[
\left(\frac{S-3}{2},\frac{S+3}{2}\right)
\quad\text{and}\quad
\left(\frac{S-1}{2},\frac{S+1}{2}\right),
\]
and both have
\[
\max |\sigma(X_{a,b})|
=\frac{S^4-10S^2+9}{24}.
\]
Thus the signature maximum is not attained by the exactly balanced even bidegree: it is shifted to gap two. For odd total degree, gaps one and three tie exactly.

## Assumptions and scope
The ground field is \(\mathbb C\). The surface is a smooth transverse intersection of hypersurfaces of degrees \(a\) and \(b\) in \(\mathbb P^4\), with both degrees at least two. The condition \(S\ge6\) is the natural general-type range because adjunction gives
\[
K_X\cong\mathcal O_X(S-5).
\]
Therefore fixing \(S\) fixes the canonical-polarization exponent while allowing the bidegree to vary.

The statement concerns the oriented topological signature of the underlying smooth four-manifold. It does not classify the surfaces up to deformation, homeomorphism, or diffeomorphism.

## Proof
For a smooth complete intersection \(X_{a,b}\subset\mathbb P^4\), the normal bundle sequence gives
\[
c(T_X)=\frac{(1+H)^5}{(1+aH)(1+bH)},
\]
where \(H\) is the hyperplane class restricted to \(X\). Hence
\[
c_1(T_X)=(5-a-b)H
\]
and
\[
c_2(T_X)=\left(10-5(a+b)+a^2+ab+b^2\right)H^2.
\]
Since \(p_1(T_X)=c_1(T_X)^2-2c_2(T_X)\), this simplifies to
\[
p_1(T_X)=(5-a^2-b^2)H^2.
\]
Moreover
\[
\int_X H^2=ab.
\]
The Hirzebruch signature theorem therefore gives
\[
\sigma(X_{a,b})
=\frac13\int_Xp_1(T_X)
=\frac{ab(5-a^2-b^2)}3.
\]
For \(a,b\ge2\), the quantity \(a^2+b^2\) is at least eight, so the signature is negative.

Now fix \(S=a+b\) and put
\[
g=b-a\ge0.
\]
Then \(g\equiv S\pmod2\), \(g\le S-4\), and
\[
a=\frac{S-g}{2},\qquad b=\frac{S+g}{2}.
\]
A direct substitution gives
\[
-3\sigma(X_{a,b})
=ab(a^2+b^2-5)
=\frac{S^4-10S^2+10g^2-g^4}{8}.
\]
Thus, for fixed \(S\), maximizing \(|\sigma|\) is exactly the problem of maximizing
\[
f(g)=10g^2-g^4
\]
over the admissible gaps.

If \(S\) is even, the admissible gaps are even. We have
\[
f(0)=0,\qquad f(2)=24,
\]
while for every even \(g\ge4\),
\[
f(g)=g^2(10-g^2)<0.
\]
Hence \(g=2\) is the unique maximizer, giving the stated bidegree and value.

If \(S\) is odd, the admissible gaps are odd. We have
\[
f(1)=f(3)=9,
\]
while for every odd \(g\ge5\), \(f(g)<0\). Hence gaps one and three are exactly the maximizers. Substitution gives the stated common value.

## Verification
A standalone exact-integer checker recomputes the signature from the Chern-class formula and independently from the closed bidegree formula. It exhaustively evaluates every nondecreasing bidegree with fixed sum \(6\le S\le200\), covering 9,799 bidegrees. For every even \(S\), it finds exactly the predicted gap-two maximizer; for every odd \(S\), it finds exactly the predicted gap-one/gap-three tie. It also checks the two closed formulas for the maximal absolute signature.

The finite replay is regression evidence for the algebra and boundary cases. The proof above is uniform for every \(S\ge6\).

## Relationship to prior work
The topology of smooth complete intersections is classical, and the signature is an important invariant in their homotopy and homeomorphism classification. A full-text source on complete-intersection topology records the stable tangent-bundle formula from which the displayed Pontryagin and signature formula follows. Earlier work specifically studies congruences for signatures of complete intersections.

The new claim is not the signature formula itself. It is the complete fixed-\(S\) extremal classification for bidegree surfaces in \(\mathbb P^4\): the unique even gap-two maximizer and the odd gap-one/gap-three tie. Claim-specific searches for fixed-sum, fixed-canonical-class, balanced-bidegree, and signature-extremal formulations did not locate this classification. The closest retrieved work studies signature congruences or topological classification, not optimization over bidegrees with fixed sum.

## Limitations
The result is restricted to codimension-two complete-intersection surfaces in \(\mathbb P^4\). In higher codimension the signature is a higher symmetric polynomial in the squared defining degrees, so the one-variable gap reduction used here no longer applies directly.

The 1980 signature-congruence paper was inspected in full and does not state the fixed-sum extremal classification. A residual literature risk remains because older complete-intersection topology literature is dispersed and an unindexed source could contain an equivalent observation.

## References
A. Libgober, J. Wood, D. Zagier, *Congruences modulo powers of 2 for the signature of complete intersections*, Quarterly Journal of Mathematics 31 (1980), 209--218. DOI: 10.1093/qmath/31.2.209. Published 1 June 1980.

L. Astey, S. Gitler, E. Micha, G. Pastor, *On the homotopy type of complete intersections*, Topology 44 (2005), 249--260. DOI: 10.1016/j.top.2004.04.001. The article lists MSC 14M10 and 55P15 and records the stable tangent-bundle description used here.
