# Idempotents of the characteristic-two dihedral quandle algebra of order eight

## Finding
Let \(K\) be **any field of characteristic \(2\)**. Let \(R_8=\mathbb Z/8\mathbb Z\) be the dihedral quandle with \(i*j=2j-i\pmod 8\), and let \(K[R_8]\) have basis \(e_0,\ldots,e_7\) and bilinear multiplication \(e_i e_j=e_{(2j-i)\bmod8}\). Define
\[
W_0=\operatorname{span}_K\{e_0+e_4,\ e_2+e_6,\ e_1+e_3+e_5+e_7\},
\]
\[
W_1=\operatorname{span}_K\{e_1+e_5,\ e_3+e_7,\ e_0+e_2+e_4+e_6\}.
\]
Then the **complete** set of idempotents \(u^2=u\) is the disjoint union
\[
\operatorname{Idem}(K[R_8])=
\{0\}\ \sqcup\ (e_0+W_0)\ \sqcup\ (e_2+W_0)\ \sqcup\ (e_1+W_1)\ \sqcup\ (e_3+W_1).
\]
Each of the four nonzero pieces is an affine three-space over \(K\). In particular, for every power \(q\) of \(2\),
\[
\bigl|\operatorname{Idem}(\mathbb F_q[R_8])\bigr|=1+4q^3.
\]
There is a sharper quotient-lifting interpretation: under reduction of subscripts modulo \(4\), precisely the zero idempotent and four basis idempotents of \(K[R_4]\) lift to idempotents in \(K[R_8]\). Zero has a unique idempotent lift; each of the four basis idempotents has an affine three-space of lifts. Although \(K[R_4]\) has two nonzero affine two-space families of idempotents, none of its other idempotents lift.

## Assumptions and scope
The product is the bilinear extension of the quandle product, **not** an associative group-algebra product. The coefficient domain is a field of characteristic \(2\), finite or infinite; there is no assumption on its degree over \(\mathbb F_2\). An idempotent means \(u\cdot u=u\). The first-public date of the motivating 2026 study is \(2026\text{-}08\text{-}03\). No statement is made for coefficient rings with zero divisors, odd characteristic, or other dihedral quandle orders.

## Proof
**Step 1 (quotient).** Set \(\pi:K[R_8]\to K[R_4]\) by \(\pi(e_i)=e_{i\bmod4}\). This is a surjective algebra homomorphism, since the defining quandle multiplication respects reduction modulo \(4\). Its kernel is spanned by \(e_j+e_{j+4}\), \(0\le j<4\). The right multiplications by \(e_j\) and \(e_{j+4}\) are identical, so \(v\cdot w=0\) for every \(v\in K[R_8]\) and \(w\in\ker\pi\). In particular, a lift \(u\) with \(\pi(u)=0\) satisfies \(u^2=0\), whence the only idempotent lift of zero is zero.

**Step 2 (all idempotents downstairs).** Write \(b=\sum_{i=0}^3 b_i e_i\), put \(A=b_0+b_2\), \(B=b_1+b_3\), and let \(\tau_j\) be the basis permutation \(e_i\mapsto e_{(2j-i)\bmod4}\). Then
\[
b^2=A\tau_0(b)+B\tau_1(b).
\]
Every nonzero idempotent has augmentation \(A+B=1\): the augmentation of an idempotent is \(0\) or \(1\); when it is zero, the even and odd coefficient sums of \(b^2\) vanish, forcing \(A=B=0\), hence \(b^2=0\) and \(b=0\). With \(A+B=1\), the coefficient equation at \(e_0\) gives \(AB=0\). Since \(K\) is a field, \((A,B)=(1,0)\) or \((0,1)\). Solving the four coefficient equations yields, respectively,
\[
b=(t,h,1+t,h),\qquad b=(t,h,t,1+h),\qquad t,h\in K,
\]
where a tuple denotes coefficients of \(e_0,e_1,e_2,e_3\). These two affine two-spaces are disjoint, and zero is the only remaining downstairs idempotent.

**Step 3 (the obstruction to lifting).** First consider \(b=(t,h,1+t,h)\). Every \(u\in\pi^{-1}(b)\) has unique coordinates
\[
u=(a,b',c,d,\ a+t,\ b'+h,\ c+1+t,\ d+h),
\qquad a,b',c,d\in K.
\]
Directly expand \(u^2-u\) using \(e_i e_j=e_{2j-i}\). In characteristic \(2\), the coefficients at indices \(0,4\) are \(h(t+1)+t^2+t\); at indices \(2,6\) they are \(ht+t^2+t\); and at indices \(1,3,5,7\) they are \(h^2+ht+b'+d\). Subtracting the first two equations (which equals adding them in characteristic \(2\)) forces \(h=0\). Both even equations then give \(t(t+1)=0\), so \(t\in\{0,1\}\). The odd equation reduces to \(d=b'\). Hence exactly \(b=e_0\) and \(b=e_2\) lift. Their lifts are precisely \(e_0+W_0\) and \(e_2+W_0\), since \(a,b',c\) are free.

**Step 4 (odd family).** The cyclic shift \(e_i\mapsto e_{i+1\bmod8}\) is a quandle-algebra automorphism; it carries the just-analyzed even family downstairs to \(b=(t,h,t,1+h)\) and shifts \(W_0\) onto \(W_1\). Thus exactly \(e_1\) and \(e_3\) lift, with fibers \(e_1+W_1\) and \(e_3+W_1\). Each \(W_j\) has the three linearly independent displayed generators, and images under \(\pi\) separate all four affine pieces and zero. This proves the disjoint classification and the finite-field count.

## Verification
Run the included standalone `verify.py` with Python \(3\). It symbolically computes all eight residual coefficient identities in the free polynomial ring \(\mathbb F_2[a,b,c,d,t,h]\) and verifies the two even equations differ by \(h\). Separately, it exhaustively enumerates all \(2^8\) and \(4^8\) coefficient tuples over \(\mathbb F_2\) and \(\mathbb F_4\), and checks equality of the full computed idempotent sets with the four displayed affine families plus zero. The observed counts are \(33\) and \(257\), respectively, with exactly \(8\) and \(64\) lifts above each permissible nonzero quotient idempotent. These finite checks corroborate the symbolic computation; the proof above supplies the all-fields conclusion.

## Relationship to prior work
Sangare–Ta (2026, arXiv:2608.01550v1) studies idempotents of commutative quandles, automorphisms of dihedral-quandle algebras, and commutator widths. Its characteristic-two Proposition \(3.11\) treats commutative quandles; \(R_8\) is not commutative. Its even-dihedral calculations address automorphisms, rather than this complete idempotent spectrum. Elhamdadi–Nunez–Singh–Swain (2022, arXiv:2204.11288v1), Theorem \(4.3\), describes lifts across coverings only when the quotient algebra has **only trivial** idempotents. That hypothesis fails here because \(K[R_4]\) has \(1+2q^2\) idempotents over \(\mathbb F_q\). Their Corollary \(4.4\) treats even dihedral orders twice an odd order and does not apply to \(8\). The later Elhamdadi–Ta–Virgin (2026, arXiv:2609.03799v1) abstract addresses integral quandle-ring idempotents by Fourier methods; its full text was not available for comparison, so overlap beyond its stated integral setting remains a research risk.

## Limitations
The full derivation is characteristic-specific. The classification and count are proved for fields, not arbitrary characteristic-two rings. This work does not assert analogous descriptions for larger dihedral quandles, automorphism groups, or arbitrary Alexander quandles. The novelty comparison cannot eliminate historically equivalent formulations or undocumented extensions in sources whose full text was unavailable. No independent audit has been performed.

## References
1. Birama Sangare and Luc Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550v1 (first public 2026-08-03), https://arxiv.org/abs/2608.01550.
2. Mohamed Elhamdadi, Brandon Nunez, Mahender Singh, and Dipali Swain, *Idempotents, free products and quandle coverings*, arXiv:2204.11288v1 (2022), https://arxiv.org/abs/2204.11288.
3. Mohamed Elhamdadi, Luc Ta, and Bryce Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799v1 (2026), https://arxiv.org/abs/2609.03799.
