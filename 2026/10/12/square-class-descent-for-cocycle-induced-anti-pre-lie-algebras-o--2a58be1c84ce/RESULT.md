# Square-class descent for cocycle-induced anti-pre-Lie algebras on the affine line

## Finding

Fix any field \(K\) with \(\operatorname{char}K\ne 2\), and the two-dimensional nonabelian Lie algebra \(\mathfrak a=Ke_1\oplus Ke_2\) given by
\[
[e_1,e_2]=e_2.
\]
For each nondegenerate symmetric bilinear form \(B\) on \(\mathfrak a\), let \(\circ_B\) be the product defined by
\[
B(x\circ_B y,z)=B(y,[x,z])\quad\text{for all }x,y,z\in\mathfrak a.
\]
Every symmetric form here is a commutative \(2\)-cocycle, and the resulting product is anti-pre-Lie. We classify **only the products arising by this cocycle construction**, not all two-dimensional anti-pre-Lie algebras.

The complete isomorphism-class set over \(K\) is
\[
\boxed{\{P_\infty\}\;\sqcup\;K^\times/(K^\times)^2.}
\]
The exceptional class \(P_\infty\) has nonzero products
\[
e_1\circ e_1=e_1,\qquad e_2\circ e_1=-e_2,
\]
while, for each \(t\in K^\times\), the class \(P_t\) has nonzero products
\[
e_1\circ e_2=e_2,\qquad e_2\circ e_2=t e_1.
\]
Thus \(P_t\cong P_{t'}\) if and only if \(t/t'\) is a nonzero square, and \(P_\infty\) is isomorphic to none of the \(P_t\).

The automorphism groups are
\[
\operatorname{Aut}(P_\infty)\cong K^\times,
\qquad
\operatorname{Aut}(P_t)=\{I,\operatorname{diag}(1,-1)\}.
\]
The natural transformation from nondegenerate symmetric forms to cocycle-induced products has precisely scalar-multiple fibers.

Over every odd finite field \(\mathbf F_q\), there are exactly **three** induced isomorphism classes; exactly \(q^2\) distinct induced products on the fixed basis; and their algebra-isomorphism orbit sizes are
\[
\boxed{q,\qquad \frac{q(q-1)}2,\qquad \frac{q(q-1)}2}.
\]
If the forms themselves are retained, rather than their induced products, the affine Lie automorphism group has exactly
\[
\boxed{2q-1}
\]
orbits of nondegenerate symmetric forms. The counts distinguish the moduli of cocycle data from the moduli of its induced multiplication.

## Assumptions and scope

The original construction is Theorem 2.19 of Liu–Bai, whose paper was publicly posted on 13 July 2022 with primary MSC \(17A36\). That theorem is formulated in characteristic zero; the explicit calculation and polynomial identities below independently establish this two-dimensional result in every characteristic different from \(2\).

The complex classification of the induced family is **not** claimed as new: Liu–Bai's Example 2.20 already identifies its two complex types with classes \((A1)\) and \((A4)_0\). The new content is the arbitrary-field square-class descent, complete cocycle/product quotient distinction, automorphism stabilizers and exact finite-field orbit arithmetic.

An isomorphism here is an isomorphism of anti-pre-Lie algebras. It must preserve the commutator Lie bracket, so it is necessarily an automorphism of \(\mathfrak a\). No bilinear form is considered part of the algebraic structure unless explicitly stated.

## Proof

**1. All forms and the induced multiplication.** The commutative-cocycle condition is the cyclic sum
\[
B([x,y],z)+B([y,z],x)+B([z,x],y)=0.
\]
This expression is alternating in three arguments, hence vanishes on the two-dimensional space (the claim is also checked directly on basis triples). Write
\[
B=\begin{pmatrix}a&b\\b&c\end{pmatrix},\qquad
\Delta=ac-b^2\ne0.
\]
The defining equation and inversion of \(B\) give
\[
\begin{aligned}
e_1\circ_B e_1&=\frac{-b^2e_1+ab e_2}{\Delta},&
e_1\circ_B e_2&=\frac{-bc e_1+ac e_2}{\Delta},\\
e_2\circ_B e_1&=\frac{-bc e_1+b^2e_2}{\Delta},&
e_2\circ_B e_2&=\frac{-c^2e_1+bc e_2}{\Delta}.
\end{aligned}
\]
The commutator is always \([e_1,e_2]_{\circ_B}=e_2\). The two anti-pre-Lie identities,
\[
x\circ(y\circ z)-y\circ(x\circ z)=[y,x]_{\circ}\circ z,
\]
\[
[x,y]_{\circ}\circ z+[y,z]_{\circ}\circ x+[z,x]_{\circ}\circ y=0,
\]
follow by direct substitution of these four products, without invoking any restriction on the characteristic besides the stated assumptions. A symbolic expansion of all basis triples is included in the verifier.

**2. Normal forms and their exhaustiveness.** The Lie automorphisms are exactly
\[
F(e_1)=e_1+u e_2,\qquad F(e_2)=s e_2,
\quad u\in K,\ s\in K^\times.
\]
Their pullback action on forms is
\[
(a,b,c)\longmapsto
\bigl(a+2bu+cu^2,\;s(b+cu),\;s^2c\bigr).
\]
If \(c=0\), then \(b\ne0\), and we may choose \(u=-a/(2b)\), \(s=1/b\) to obtain \(B_\infty=\begin{pmatrix}0&1\\1&0\end{pmatrix}\). Substitution into the table yields \(P_\infty\).

If \(c\ne0\), choose \(u=-b/c\) to make the off-diagonal term zero. The remaining diagonal form has entries \(\delta=a-b^2/c=\Delta/c\ne0\) and \(s^2c\). Multiplication of \(B\) by any nonzero scalar does not change \(\circ_B\); after scalar normalization we obtain \(B_t=\operatorname{diag}(1,-t)\) with \(t\ne0\), giving exactly \(P_t\). Varying \(s\) changes \(t\) by a nonzero square. Hence every induced product belongs to the listed isomorphism classes.

**3. Separation, automorphisms, and scalar fibers.** Every algebra isomorphism preserves the commutator \([e_1,e_2]=e_2\) and so is of the above affine form. For \(P_t\), the condition \(F(e_1\circ e_1)=F(e_1)\circ F(e_1)\) forces \(u=0\); comparison of \(F(e_2\circ e_2)\) then gives \(t=s^2t'\) for an isomorphism from \(P_t\) to \(P_{t'}\). Thus the parameter is exactly its square class. Its automorphisms are \(s^2=1\), i.e. \(s=\pm1\). For \(P_\infty\), comparison of \(e_1\circ e_1=e_1\) gives \(2u=0\), hence \(u=0\), while \(s\) is arbitrary. The exceptional algebra cannot be one of the \(P_t\): its right annihilator is the derived Lie ideal \(Ke_2\), while the right annihilator of \(P_t\) is \(Ke_1\), transverse to that ideal.

To see that the construction has *only scalar fibers*, recover all symmetric forms \(B'\) satisfying \(B'(x\circ y,z)=B'(y,[x,z])\) for each canonical product. For \(P_\infty\), the equations give \(B'_{11}=B'_{22}=0\), hence \(B'\) is a multiple of \(B_\infty\). For \(P_t\), they give \(B'_{12}=0\) and \(B'_{22}=-tB'_{11}\), so \(B'\) is a multiple of \(B_t\). Transporting by the normal-form isomorphisms proves the assertion for every induced product.

**4. Finite-field orbit counts.** Over \(\mathbf F_q\) with \(q\) odd, there are
\[
q^2(q-1)
\]
nondegenerate symmetric \(2\times2\) forms: for each nonzero \(c\), one has \(q(q-1)\) choices for \((a,b)\), giving \(q(q-1)^2\) forms; when \(c=0\), one must have \(b\ne0\), giving another \(q(q-1)\). Each induced product has exactly \(q-1\) scalar form representatives, giving \(q^2\) distinct fixed-bracket products.

The affine automorphism group has order \(q(q-1)\). The stabilizer of \(P_\infty\) has order \(q-1\); each \(P_t\) stabilizer has order \(2\). Over \(\mathbf F_q\), the group \(\mathbf F_q^\times/(\mathbf F_q^\times)^2\) has size \(2\). Orbit-stabilizer therefore gives exactly the three stated product-orbit sizes, summing to \(q^2\).

For the *forms without scalar identification*, when \(c=0\) they form one orbit. When \(c\ne0\), the quantity \(\delta=a-b^2/c\in\mathbf F_q^\times\) is invariant under the affine action, and so is the square class of \(c\). Conversely these two invariants distinguish and exhaust all such orbits. There are therefore \(2(q-1)\) orbits with \(c\ne0\), plus one with \(c=0\), for a total of \(2q-1\).

## Verification

`artifacts/verify.py` symbolically reconstructs the full multiplication from a generic symmetric form and independently evaluates the commutator and **both** anti-pre-Lie identities on every basis triple. It also reconstructs the four structure coefficients.

For \(q\in\{3,5,7,11\}\), the program exhaustively enumerates every nondegenerate symmetric form, checks scalar fibers, tests the identities of every induced product, and independently computes isomorphism orbits and automorphism stabilizers by every affine Lie automorphism. It computes orbits on the unprojectivized forms separately. The output reports respectively \(9,25,49,121\) induced products; \(5,9,13,21\) form orbits; and the exact predicted three product orbits. It terminates with `VERIFY_OK`.

Finite enumeration is reproducibility evidence, not a proof for all fields. The arbitrary-field statement is established by the displayed normal-form and invariant arguments.

## Relationship to prior work

Liu–Bai, Theorem 2.19, supplies the nondegenerate commutative-cocycle construction. Their Example 2.20 and Proposition 2.10 classify the associated **complex** two-dimensional types; that result is explicitly prior coverage for the geometric two-class statement. They do **not** in the inspected source classify the arithmetic forms of this family over arbitrary non-algebraically-closed fields or count the finite-field cocycle and product orbits.

The full text of Normatov's later complex-field classification of compatible anti-pre-Lie algebras was inspected at its relevant low-dimensional classification and parameter sections; it does not provide these finite-field cocycle orbit counts.

Petersson's general classification of all two-dimensional nonassociative algebras over arbitrary fields is stronger in scope on *abstract isomorphism types*. His work could label the classes \(P_t\) under a different taxonomy, so the bare square-class classification is not claimed to be isolated from general low-dimensional classification. The cocycle-induced restriction, distinction between form and induced-product quotients, stabilizer arithmetic, and exact fixed-bracket product counts are the present contribution. The abstract of the general work was accessible, but its full interior was not; the possibility of an equivalent specialized orbit calculation is retained as a risk. Petersson–Scherer's total count of all two-dimensional algebras over a finite field likewise does not directly identify this source-specific subset.

Searches included anti-pre-Lie classifications under square-class, affine Lie algebra, nondegenerate symmetric cocycle, finite-field, and low-dimensional general-algebra formulations, with exact counts and group-action variants.

## Limitations

The theorem is limited to products *induced by nondegenerate symmetric commutative \(2\)-cocycles* on the specified nonabelian two-dimensional Lie algebra. It does not enumerate every anti-pre-Lie product on a two-dimensional vector space.

Characteristic \(2\) is excluded. The source's complex classification is not new; the arbitrary-field orbit and finite-field arithmetic assertions are the added results.

General two-dimensional algebra classifications may encode some of the normal forms under other names. The inaccessible interior of Petersson's work remains a concrete originality risk. An unsuccessful literature search cannot establish absolute novelty.

## References

1. G. Liu and C. Bai, “Anti-pre-Lie algebras, Novikov algebras and commutative 2-cocycles on Lie algebras,” *Journal of Algebra* 609 (2022), 337–379; arXiv:2207.06200v1 (posted 13 July 2022); DOI `10.1016/j.jalgebra.2022.07.004`.
2. I. Normatov, “Compatible anti-pre-Lie algebras,” arXiv:2412.16273v1 (2024).
3. H. P. Petersson, “The Classification of Two-dimensional Nonassociative Algebras,” *Results in Mathematics* 37 (2000), 120–154, DOI `10.1007/BF03322518`.
4. H. P. Petersson and M. Scherer, “The Number of Nonisomorphic Two-dimensional Algebras over a Finite Field,” *Results in Mathematics* 45 (2004), 137–152, DOI `10.1007/BF03323003`.
