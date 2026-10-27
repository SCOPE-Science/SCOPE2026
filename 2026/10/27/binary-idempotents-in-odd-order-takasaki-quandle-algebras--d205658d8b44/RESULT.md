# Binary idempotents in odd-order Takasaki quandle algebras

## Finding
Let \(A\) be any finite abelian group of odd order, including the trivial group. Let \(T(A)\) be its Takasaki quandle with \(a\triangleright b=2b-a\), and let \(E_A=\mathbb F_2[T(A)]\) be the binary quandle algebra. The algebra multiplication is bilinear and need not be associative. Define \(I(A)=\{u\in E_A:u\triangleright u=u\}\), including zero.

On the characters \(\widehat A=\operatorname{Hom}(A,\overline{\mathbb F}_2^{\times})\), let \(F\chi=\chi^2\). Write \(\mathcal O\) for the set of \(F\)-orbits, and \(d_O=|O|\). Inversion acts on these orbits by \(O\mapsto -O=\{\chi^{-1}:\chi\in O\}\). Let \(\mathcal S\) be the nontrivial orbits with \(-O=O\); let \(\mathcal P\) be the unordered two-element sets \(\{O,-O\}\) with \(O\ne -O\). Every \(d_O\) for \(O\in\mathcal S\) is even, and the two orbits in each pair have equal lengths.

**The complete count is**
\[
|I(A)|=2\prod_{O\in\mathcal S}(2^{d_O/2}+2)\prod_{\{O,-O\}\in\mathcal P}2^{d_O}.
\]
More precisely, there is a canonical componentwise classification after finite-field identifications: on the trivial-character component one chooses \(0\) or \(1\); on every nontrivial inversion-stable orbit component one chooses \(0\) or one of the \(2^{d_O/2}+1\) elements of norm one in \(\mathbb F_{2^{d_O}}/\mathbb F_{2^{d_O/2}}\); and on each paired orbit component one chooses the zero pair or a unique inverse-linked pair indexed by \(\mathbb F_{2^{d_O}}^{\times}\).

For cyclic \(A=C_n\) with odd \(n\ge1\), factor \(t^n-1\) over \(\mathbb F_2\) into distinct monic irreducibles. The factor \(t+1\) contributes \(2\); each other self-reciprocal irreducible \(f\) of degree \(2e\) contributes \(2^e+2\); and each unordered pair of distinct reciprocal irreducibles of degree \(d\) contributes \(2^d\). In particular, for \(n=1,3,5,7,9,11,13,15\) respectively, the counts are \(2,8,12,16,80,68,132,768\). For \(A=C_3\times C_3\) the count is \(512\); indeed every element of its binary quandle algebra is idempotent.

## Assumptions and scope
The coefficient ring is exactly \(\mathbb F_2\); the abelian group is finite of **odd** order. Quandle idempotence \(u\triangleright u=u\) is not ordinary idempotence in the auxiliary associative group algebra. Counts include zero. There is no claim about even-order abelian groups, arbitrary coefficient fields of characteristic two, or integral quandle rings.

## Proof
Write the finite abelian group multiplicatively only in the auxiliary group algebra \(B=\mathbb F_2[A]\), identifying the quandle basis element \(e_a\) with its group-algebra basis symbol \([a]\). For \(x=\sum_{a\in A}c_a[a]\), let \(x^*=\sum_ac_a[a^{-1}]\), an involutive algebra automorphism of the **commutative associative** algebra \(B\). In characteristic two,
\[
x^2=\sum_{b\in A}c_b[b^2],\qquad x^*x^2=\sum_{a,b}c_ac_b[b^2a^{-1}].
\]
The latter basis index is exactly the Takasaki product \(a\triangleright b=2b-a\). Thus the quandle square of the element represented by \(x\) is the ordinary group-algebra product \(x^*x^2\). Consequently,
\[
u\triangleright u=u\quad\Longleftrightarrow\quad x=x^*x^2\quad\Longleftrightarrow\quad x(1-xx^*)=0\text{ in }B.
\]
The last equivalence uses commutativity of \(B\), not associativity of the quandle algebra.

Because \(|A|\) is odd, \(B\) is a finite product of finite fields. One way to see the decomposition is to extend scalars to \(\overline{\mathbb F}_2\): evaluation at characters diagonalizes \(B\), and descent under the Frobenius \(z\mapsto z^2\) groups characters into its orbits \(O\). Each orbit yields one component \(\mathbb F_{2^{d_O}}\). The involution \(*\) carries the component of \(O\) isomorphically to the component of \(-O\).

On an inversion-stable orbit, \(*\) restricts to a field involution. At the trivial character it is the identity of \(\mathbb F_2\), so \(x(1-xx^*)=0\) has exactly two solutions \(0,1\). If \(O\ne\{1\}\) is stable, inversion has no fixed nontrivial character because \(A\) has odd order. Thus its action on the length-\(d_O\) Frobenius cycle is a nonidentity element of order two, necessarily the half-turn; \(d_O\) is even and \(*\) acts as \(z\mapsto z^{2^{d_O/2}}\). In the field, \(x(1-xx^*)=0\) means \(x=0\) or \(xx^*=1\). The norm map from \(\mathbb F_{2^{d_O}}^{\times}\) onto \(\mathbb F_{2^{d_O/2}}^{\times}\) has kernel of order \((2^{d_O}-1)/(2^{d_O/2}-1)=2^{d_O/2}+1\); hence this component has \(2^{d_O/2}+2\) solutions.

For a pair \(O\ne -O\), choose an identification of its two fields with \(K=\mathbb F_{2^{d_O}}\) for which \(*\) swaps the coordinates. The two scalar equations are \(x(1-xy)=0\) and \(y(1-xy)=0\). Either both coordinates vanish or \(xy=1\). There are exactly \(1+(|K|-1)=2^{d_O}\) possibilities, and every nonzero solution is determined by either coordinate. Multiplying the independent component counts proves both the stated classification and the formula.

For cyclic \(A=C_n\), the component fields are the quotients by irreducible factors of \(t^n-1\), and inversion exchanges each polynomial with its monic reciprocal, giving the displayed factorization version. For \(C_3\times C_3\), every one of the eight nontrivial characters lies in a Frobenius orbit of size two stable under inversion; this gives \(2\cdot4^4=512\). Equivalently, the quandle product is commutative when \(3A=0\), so in characteristic two all cross terms of a square cancel, leaving \(u\triangleright u=u\) for every \(u\).

## Verification
The self-contained Python program `verify.py` uses exact polynomial division over \(\mathbb F_2\), reciprocal-polynomial pairing, and separate brute-force bilinear multiplication on every coefficient mask. For each odd \(n\in\{1,3,5,7,9,11,13,15\}\), it independently compares the product formula with exhaustive enumeration of all \(2^n\) binary vectors. It also checks all \(512\) vectors of \(\mathbb F_2[T(C_3\times C_3)]\), using a separate two-coordinate quandle multiplication table. Run `python3 verify.py` with Python 3 standard library only; success ends with `VERIFY_OK`. No finite test is used as the proof for arbitrary \(A\).

## Relationship to prior work
Bardakov–Passi–Singh (2022) developed quandle rings and computed integral idempotents for small dihedral quandles, including \(\mathbb Z[R_3]\). Sangare–Ta (2026), Section 3, studies idempotents of quandle algebras and proves restrictions for coefficient characteristic other than two; its Proposition 3.3 supplies general idempotent examples, not the binary all-order count here. Elhamdadi–Ta–Virgin (2026) uses Fourier methods for complex/integral quandle algebras of finite odd-order Takasaki quandles, establishing integral rigidity; its finite-characteristic-two numerical count is not stated in the inspected full text. Zhang (2026) describes group-ring methods and integral idempotents; its accessible abstract does not state this binary finite-field classification, but the full manuscript was not available for comparison. Thus the new claim is the explicit \(\mathbb F_2\) norm-one/reciprocal-orbit classification over **all finite odd-order abelian groups**, rather than integral idempotent rigidity or the small-quandle cases.

## Limitations
Originality has only been checked against identified accessible literature and indexed research records. Unindexed equivalent classifications remain possible. Zhang's relevant full text could not be inspected, so any unnoticed characteristic-two consequence therein is a specific remaining priority risk. No result is asserted for groups of even order (where the group algebra is generally not semisimple) or for coefficient fields larger than \(\mathbb F_2\).

## References
1. B. Sangare and L. Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550v2 (first public 2026-08-03), https://arxiv.org/html/2608.01550v2.
2. M. Elhamdadi, L. Ta and B. Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799v1 (2026-09-03), https://arxiv.org/html/2609.03799v1.
3. V. G. Bardakov, I. B. S. Passi and M. Singh, *Zero-Divisors and Idempotents in Quandle Rings*, Osaka J. Math. 59 (2022), 611–637, doi:10.18910/88489.
4. Z.-L. Zhang, *Group-ring methods for Alexander quandle rings*, arXiv:2610.08204 (2026-10-06), https://arxiv.org/abs/2610.08204.
