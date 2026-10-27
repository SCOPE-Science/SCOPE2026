# Two cyclotomic fixed-locus collisions on the Klein cubic in characteristic five

## Finding
Let \(R=\mathbb Z_{(5)}\) and let
\[
X_R=V(F)\subset\mathbb P^4_R,\qquad F=\sum_{i\in\mathbb Z/5\mathbb Z}x_i^2x_{i+1}.
\]
Write \(\sigma([x_0:\cdots:x_4])=[x_1:\cdots:x_4:x_0]\), and let \(S_R=F_1(X_R)\) be the relative Fano scheme of lines. The threefold is smooth over \(R\), and its cyclic automorphism preserves the Fano surface.

**Theorem.** Both fixed schemes are finite flat over \(R\), with canonical explicit presentations
\[
\operatorname{Fix}_{X_R}(\sigma)\simeq R[t]/(t^4+t^3+t^2+t+1),
\qquad
\operatorname{Fix}_{S_R}(\sigma)\simeq R[a]/(a^2-a-1).
\]
Their generic geometric fibers comprise respectively four points and two invariant lines. Over an algebraic closure of \(\mathbb F_5\), each support consists of exactly one point; the intrinsic fixed scheme of the threefold is curvilinear of length \(4\), and that of the Fano surface is curvilinear of length \(2\):
\[
\operatorname{Fix}_{X_{\overline{\mathbb F}_5}}(\sigma)\simeq\operatorname{Spec}\overline{\mathbb F}_5[\epsilon]/(\epsilon^4),\quad
\operatorname{Fix}_{S_{\overline{\mathbb F}_5}}(\sigma)\simeq\operatorname{Spec}\overline{\mathbb F}_5[\eta]/(\eta^2).
\]
The respective generic fields are the fifth cyclotomic field and its real quadratic subfield, with discriminants \(5^3\) and \(5\). At the unique fixed point of the special-fiber threefold, the differential of \(\sigma\) on its three-dimensional tangent space is a single unipotent Jordan block of size \(3\); at the unique invariant line, the differential on the two-dimensional Fano tangent space is a single block of size \(2\).

## Assumptions and scope
The base is the localization of the integers at \(5\), with no choice of a primitive fifth root in the base. Fixed schemes mean the scheme-theoretic equalizers of the identity and the specified **constant cyclic order-five automorphism**, not fixed loci of a multiplicative group scheme. The Fano scheme is the projective Hilbert scheme of lines on the smooth threefold. Every assertion about a geometric special fiber is after extension to an algebraic closure. No classification of the full automorphism group or of its quotient is asserted.

## Proof
**Smoothness.** The five partial derivatives are \(F_i=2x_ix_{i+1}+x_{i-1}^2\). If one coordinate of a common zero vanishes, the derivative at its index forces the preceding coordinate to vanish; repeating forces all coordinates to vanish, impossible in projective space. Otherwise, multiplying the five equations \(x_{i-1}^2=-2x_ix_{i+1}\) implies \((-2)^5=1\). This fails both in characteristic zero and in characteristic five, so the total family is smooth over \(R\).

**Fixed points on the cubic.** A line in the ambient five-dimensional representation fixed by the cyclic shift admits a unit eigenvalue \(t\) with \(t^5=1\). Its normalized coordinates are \([1:t:t^2:t^3:t^4]\). Thus the ambient projective fixed scheme is \(\operatorname{Spec}R[t]/(t^5-1)\). On this scheme,
\[
F(1,t,t^2,t^3,t^4)=\sum_{i=0}^4t^{3i+1}
=t(1+t+t^2+t^3+t^4),
\]
where the last identity is modulo \(t^5-1\) because multiplication by \(3\) permutes the exponents modulo \(5\). Writing \(\Phi_5(t)=t^4+t^3+t^2+t+1\), and using \(t^5-1=(t-1)\Phi_5(t)\), proves the first presentation scheme-theoretically. The special fiber has \(\Phi_5(t)=(t-1)^4\); its unique support is \(P=[1:1:1:1:1]\).

**Invariant lines.** Let \(W\subset R^5\) be a rank-two invariant direct summand, on the Grassmann chart where projection to the first two coordinates is invertible. Put \(x_0=U,x_1=V\) and write
\[
x_{i+2}=-a x_{i+1}-b x_i\quad (i=0,1,2).
\]
The shift preserves \(W\) exactly when the monic polynomial \(q(T)=T^2+aT+b\) divides \(T^5-1\), equivalently the two coefficients of the remainder vanish. The additional condition \(W\subset X_R\) is exactly the vanishing of all four coefficients of \(F(x_0(U,V),\ldots,x_4(U,V))\) in \(U,V\). Let \(I\subset R[a,b]\) be this explicitly defined six-generator ideal.

Exact polynomial division and Gröbner elimination give
\[
I\otimes\mathbb Q=(b-1,a^2-a-1),\quad
I\otimes\mathbb F_5=(b-1,(a+2)^2).
\]
The six displayed defining polynomials already vanish identically upon substituting \(b=1\) and \(a^2=a+1\) over \(\mathbb Z\); these three finite algebraic assertions are independently replayed by `verify.py`. Thus \(\operatorname{Spec}R[a]/(a^2-a-1)\) is a closed subscheme of the fixed Fano locus.

For completeness, the above chart exhausts the fixed scheme: in characteristic zero, any invariant two-plane is the span of two distinct eigenlines, whose projections to coordinates \(0,1\) are independent; in characteristic five, the regular unipotent five-cycle has a unique invariant two-plane, \(\ker(\sigma-1)^2\), whose first two coordinates are independent. The fixed Fano locus is projective with finite geometric fibers, hence finite over \(R\). Its special fiber is the length-two local algebra computed above, and the proposed quadratic subscheme has the same special fiber. The surjection from the finite coordinate algebra to the free rank-two quadratic algebra therefore has zero kernel by Nakayama's lemma (using flatness of the target to tensor the exact sequence). The second presentation follows, without relying on rational-fiber point counts alone.

In the special fiber the unique invariant line is explicitly
\[
L=\{[U:U+H:U+2H:U+3H:U+4H]\mid [U:H]\in\mathbb P^1\}.
\]
The existence of its nonreduced length-two Fano fixed scheme is intrinsic, not a duplicate geometric line.

**Tangent actions.** In characteristic five the permutation on \(V=k^5\) is one regular unipotent block of size five. The tangent space of the cubic at \(P\) is \(\ker(\sum x_i)/k(1,1,1,1,1)\), identified with \(\operatorname{im}(\sigma-1)/\operatorname{im}(\sigma-1)^4\); this is one block of size three. The Fano scheme of a smooth cubic threefold is smooth of dimension two: along a line the surjection \(\mathcal O(1)^3\to\mathcal O(3)\) has kernel splitting as \(\mathcal O\oplus\mathcal O\) or \(\mathcal O(1)\oplus\mathcal O(-1)\), both with vanishing first cohomology. The Fano fixed scheme has one-dimensional tangent space from \(k[\eta]/\eta^2\), so its order-five differential on the two-dimensional ambient tangent is one size-two unipotent block.

**Ramification.** The translations \(t=1+s\) and \(a=3+u\) give respectively
\[
\Phi_5(1+s)=s^4+5s^3+10s^2+10s+5,\qquad
(3+u)^2-(3+u)-1=u^2+5u+5.
\]
Both are Eisenstein at \(5\); their ramification indices are \(4\) and \(2\), and their polynomial discriminants are \(125\) and \(5\). In characteristic five these equations become \(s^4\) and \(u^2\), proving the stated lengths and explaining the nested cyclotomic degeneration.

## Verification
The standalone exact script `verify.py` uses Python 3 and SymPy; run `python verify.py`. It verifies the two polynomial discriminants and Eisenstein shifts, the point-eigenline identity, all six invariant-line equations, their reductions to the quadratic model, and the characteristic-zero and characteristic-five Gröbner ideals. Output on execution: `VERIFY_OK: eigenline phi5/discriminant125/length4; Fano fixed-line quadratic/discriminant5/length2; smoothness and Eisenstein shifts`. The geometric finiteness, Nakayama comparison, and tangent arguments are proved above rather than inferred from finite tests.

## Relationship to prior work
Klein's classical cubic is the model; Roulleau's 2010 preprint explicitly records the order-five coordinate automorphism and studies the complex Fano surface and its period lattice. The present result concerns instead the integral fixed **schemes** and their characteristic-five collision, including both the cubic and its Fano surface. Neither the complex automorphism description nor general Fano-scheme theory, by itself, specifies the two special-fiber local lengths and simultaneous quadratic/cyclotomic presentations. An alternative treatment of these same fixed equalizers under different cyclic coordinates would cover the result; no such treatment was identified in the inspected sources.

## Limitations
These presentations apply only to this chosen cyclic order-five subgroup and the displayed integral equation localized at five. The quotient singularities, its integral minimal models, and other automorphism subgroups are not determined. The originality comparison is relative to the literature actually inspected; no literature search proves absolute uniqueness of the calculation.

## References
1. X. Roulleau, *The Fano surface of the Klein cubic threefold*, arXiv:1001.4853 (first arXiv version 2010-01-27), especially Sections 1 and 3. https://arxiv.org/abs/1001.4853
2. A. B. Altman and S. L. Kleiman, *Foundations of the theory of Fano schemes*, Compositio Mathematica 34 (1977), 3–47. https://www.numdam.org/item/CM_1977__34_1_3_0.pdf
3. A. Adler, *On the automorphism group of a certain cubic threefold*, American Journal of Mathematics 100 (1978), 1275–1280; historical automorphism-group background, as cited by Roulleau.
