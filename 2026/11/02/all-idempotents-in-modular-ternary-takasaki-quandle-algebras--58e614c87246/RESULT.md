# All idempotents in modular ternary Takasaki quandle algebras

## Finding

For every field \(K\) of characteristic \(3\) and every integer \(d\ge2\), the entire idempotent set of the Takasaki quandle algebra of \(G=(\mathbb F_3)^d\) has an explicit polynomial parametrization. Let \(R=K[G]\) be the **ordinary associative, commutative** group algebra, let \(\varepsilon:R\to K\) be augmentation, let \(\sigma(e_g)=e_{-g}\) be the inversion involution, and define
\[
W=\{w\in\ker\varepsilon:\sigma(w)=-w\}.
\]
Then, with products and powers in \(R\) unless a star is displayed,
\[
\operatorname{Idem}(K[T(G)])
=\{0\}\;\sqcup\;\{1-w-w^2:w\in W\}.
\]
The parametrization is bijective, with inverse \(u\longmapsto u-\sigma(u)\). Also,
\[
\dim_K W=\frac{3^d-1}{2}.
\]
Therefore, for any finite coefficient field \(K=\mathbb F_q\) of characteristic three, the exact number of star-idempotents, **including zero**, is
\[
\boxed{1+q^{(3^d-1)/2}}.
\]
The nonzero idempotents are closed under the star product and form a Takasaki quandle, isomorphic to the core of an elementary abelian exponent-three unit group. If \(q=3^f\), this unit group is isomorphic to \((C_3)^{f(3^d-1)/2}\).

## Assumptions and scope

Fix an integer \(d\ge2\). Write \(G=(\mathbb F_3)^d\) additively, and choose the standard basis \(\{e_g:g\in G\}\) of the \(K\)-vector space \(R\). The Takasaki quandle operation is \(x*y=2y-x\), hence \(x*y=-x-y\) because every element has order dividing three. The quandle algebra \(Q=K[T(G)]\) uses the bilinear multiplication \(e_x\star e_y=e_{-x-y}\); no associativity of \(\star\) is assumed. The ordinary group-algebra multiplication \(\cdot\) is separately defined by \(e_x\cdot e_y=e_{x+y}\), with unit \(1=e_0\). The linear map \(\sigma(e_g)=e_{-g}\) is an automorphism of the ordinary group algebra satisfying \(\sigma^2=\mathrm{id}\).

All fields here have characteristic three, but need not be perfect, finite, or algebraically closed. The count and elementary-abelian finite-group identification require a finite coefficient field. The \(d=1\) case of the same formula follows by this proof but is **not** asserted to be a new case.

## Proof

**1. Reduction to an associative involution.** For basis elements, \(e_x\star e_y=e_{-x-y}=\sigma(e_x\cdot e_y)\), and bilinearity gives
\[
u\star v=\sigma(u\cdot v)
\]
for all \(u,v\in R\). Accordingly, \(u\star u=u\) if and only if \(\sigma(u)=u^2\), where the square is the ordinary group-algebra square.

**2. Cubes and augmentation.** The group algebra is commutative and has characteristic three, so the Frobenius identity and the exponent of \(G\) give
\[
\left(\sum_{g\in G} a_g e_g\right)^3
=\sum_g a_g^3e_{3g}
=\left(\sum_g a_g\right)^3 1
=\varepsilon(u)^3 1.
\]
Applying augmentation to the idempotency equation shows \(\varepsilon(u)^2=\varepsilon(u)\), hence \(\varepsilon(u)\in\{0,1\}\). If \(\varepsilon(u)=0\), then \(u^3=0\). Applying \(\sigma\) to \(\sigma(u)=u^2\) yields \(u=(\sigma(u))^2=u^4\), whence \(u=u\cdot u^3=0\). If \(\varepsilon(u)=1\), then \(u^3=1\), so \(u\) is a unit with \(u^{-1}=u^2\), and the idempotency equation is precisely \(\sigma(u)=u^{-1}\).

**3. Parametrization by the minus eigenspace.** Let \(J=\ker\varepsilon\) and \(W=\{w\in J:\sigma(w)=-w\}\). Every \(w\in W\) has \(w^3=0\). Set \(u_w=1-w-w^2\). Since \(\sigma(w^2)=w^2\), we have \(\sigma(u_w)=1+w-w^2\). Expanding in characteristic three and using \(w^3=0\) gives
\[
 u_w^2=(1-w-w^2)^2=1+w-w^2=\sigma(u_w).
\]
Thus \(u_w\star u_w=u_w\) and \(\varepsilon(u_w)=1\). Moreover,
\[
 u_w-\sigma(u_w)=-2w=w
\]
in characteristic three, which proves injectivity of the parametrization.

For surjectivity, let \(u\) be any nonzero star-idempotent. By Step 2, \(u^3=1\) and \(\sigma(u)=u^2\). Put \(w=u-\sigma(u)=u-u^2\). Its augmentation is zero, and \(\sigma(w)=-w\), so \(w\in W\). Since \(u^3=1\) and \(u^4=u\),
\[
 w^2=(u-u^2)^2=u^2-2u^3+u^4=u^2+1+u.
\]
Therefore \(1-w-w^2=1-(u-u^2)-(u^2+1+u)=-2u=u\). This proves the stated inverse and completeness.

**4. Dimension and exact count.** Every nonzero \(g\in G\) belongs to a two-element inversion orbit \(\{g,-g\}\), and the identity basis vector is fixed. Because \(2\) is invertible in \(K\), the elements \(e_g-e_{-g}\), one for each such orbit, form a \(K\)-basis of \(W\). They all have augmentation zero. Hence \(\dim_K W=(3^d-1)/2\). For finite \(K=\mathbb F_q\), the bijection in Step 3 gives \(q^{(3^d-1)/2}\) nonzero star-idempotents and precisely one additional zero idempotent.

**5. Structure of the nonzero idempotent quandle.** The set of nonzero idempotents is exactly
\[
H=\{u\in R^\times:\varepsilon(u)=1,\ \sigma(u)=u^{-1}\}.
\]
It is a subgroup of the abelian unit group \(R^\times\), and every member has cube equal to \(1\). For \(u,v\in H\),
\[
u\star v=\sigma(uv)=u^{-1}v^{-1}=u^{-1}v^2,
\]
the Takasaki operation on the abelian group \(H\), written multiplicatively. Hence the set is closed under \(\star\) and is a quandle. When \(K=\mathbb F_{3^f}\), its order is \(3^{f(3^d-1)/2}\) and its exponent divides three. Therefore \(H\cong(C_3)^{f(3^d-1)/2}\). This completes the proof.

## Verification

The accompanying `verify.py` uses only Python's standard library and implements the quandle multiplication directly from the basis table, separately from the ordinary group-algebra convolution. It exhaustively enumerates all \(3^3=27\) elements for \((q,d)=(3,1)\), all \(9^3=729\) for \((9,1)\), and all \(3^9=19\,683\) for \((3,2)\), confirming counts \(4\), \(10\), and \(82\) respectively and exact equality with the parametrized sets. It separately checks all \(9^4=6\,561\) parameters for \((9,2)\), and a reproducible set of 100 parameters for \((3,3)\), without claiming full enumeration of those much larger ambient algebras. Its final output is `VERIFY_OK`. The proof above, not the bounded experiments, establishes the all-field and all-dimension statements.

## Relationship to prior work

Elhamdadi, Ta, and Virgin (2026, arXiv:2609.03799; first public 2026-09-03) study Fourier analysis and integral idempotent questions for Takasaki and Alexander quandles; their principal positive results treat integral coefficient rings and Fourier methods in complex coefficients. The present characteristic-three group-algebra involution is a different modular regime where nontrivial idempotents abound. Sangare and Ta (2026, arXiv:2608.01550) consider idempotents of commutative quandle algebras and orderable examples. Bardakov and Elhamdadi (2026, arXiv:2601.07057) treat augmentation ideals and idempotents, including specific dihedral and commutative quandles. Bardakov, Passi, and Singh (2020, arXiv:2001.06843) treat certain small quandle rings and integral coefficients. Kaur and Singh (2023, arXiv:2303.06948) examine real/complex Takasaki decompositions. A previously available exact prime-order dihedral-quandle formula already covers the \(d=1\), \(p=3\) count \(q+1\); this boundary count is not new.

The additional result here is a complete explicit classification for **every** higher-dimensional elementary ternary Takasaki quandle over every coefficient field of characteristic three, including the nonzero idempotent-quandle structure. Searches and comparisons of accessible literature and records did not locate equivalent higher-dimensional coverage. Historical priority is not independently certified.

## Limitations

The field characteristic must be exactly three, and the underlying additive group must be elementary abelian of exponent three. The result says nothing about integral or complex idempotents for these same quandles, about other exponent groups, or about arbitrary finite quandles. The count \(1+q^{(3^d-1)/2}\) applies only to finite fields \(\mathbb F_q\) of characteristic three. The provided finite checks are exhaustive only for their expressly identified small ambient algebras; the symbolic proof covers all parameters. The one-dimensional case was already known and is not claimed as novel. A classification in older specialized literature could imply this theorem; no independent historical-priority certification has been obtained.

## References

1. M. Elhamdadi, L. Ta, B. Virgin, *Fourier Analysis and Idempotents in Quandle Algebras* (2026), arXiv:2609.03799, https://arxiv.org/abs/2609.03799 (originally public 2026-09-03).
2. B. Sangare, L. Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras* (2026), arXiv:2608.01550, https://arxiv.org/abs/2608.01550.
3. V. Bardakov, M. Elhamdadi, *Idempotents and Powers of Ideals in Quandle Rings* (2026), arXiv:2601.07057, https://arxiv.org/abs/2601.07057.
4. V. G. Bardakov, I. B. S. Passi, M. Singh, *Zero-divisors and idempotents in quandle rings* (2020), arXiv:2001.06843, https://arxiv.org/abs/2001.06843.
5. D. Kaur, P. Singh, *Decomposition of quandle rings of Takasaki quandles* (2023), arXiv:2303.06948, https://arxiv.org/abs/2303.06948.
