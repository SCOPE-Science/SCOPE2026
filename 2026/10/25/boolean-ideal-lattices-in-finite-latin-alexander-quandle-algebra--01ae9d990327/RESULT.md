# Boolean ideal lattices in finite latin Alexander quandle algebras

## Finding

**Theorem (complete two-sided ideal classification).** Let \(A\) be a finite abelian group, let \(\varphi\in\operatorname{Aut}(A)\) with \(\psi=1-\varphi\in\operatorname{Aut}(A)\), and let \(K\) be a field whose characteristic does not divide \(|A|\) and that contains all roots of unity of order dividing \(\exp(A)\). Equip \(A\) with the latin Alexander quandle operation \(x\triangleright y=\varphi(x)+\psi(y)\), and put \(E=K[\operatorname{Alex}(A,\varphi)]\).

Let \(\widehat A=\operatorname{Hom}(A,K^\times)\), let \(\Phi(\chi)=\chi\circ\varphi\) and \(\Psi(\chi)=\chi\circ\psi\), and let \(H=\langle\Phi,\Psi\rangle\le\operatorname{Aut}(\widehat A)\). For every orbit \(O\in\widehat A/H\), set
\[
E_O=\{u\in E:\operatorname{supp}(\widehat u)\subseteq O\}.
\]
Then every two-sided \(K\)-linear ideal of \(E\) is uniquely \(\bigoplus_{O\in\mathcal T}E_O\), where \(\mathcal T\) is a subset of the \(H\)-orbit set. Each \(E_O\) is a simple, nonzero, two-sided ideal with \(\dim_K E_O=|O|\). Different orbit ideals annihilate one another in both orders, and \(E_OE_O=E_O\), where products of subspaces mean linear spans of products. Consequently the two-sided ideal lattice is Boolean of rank \(r=|\widehat A/H|\), with precisely \(2^r\) ideals, and \(E\) is their internal direct sum.

For the odd-prime dihedral quandle \(R_p\), write \(h_p=|\langle-1,2\rangle\le\mathbb F_p^\times|\). The complete ideal count over every eligible \(K\) is
\[
\#\operatorname{Id}_{2\mathrm{s}}(K[R_p])=2^{1+(p-1)/h_p},
\]
with one simple block of dimension \(1\) and \((p-1)/h_p\) blocks each of dimension \(h_p\). For \(p=31\), these dimensions are \(1,10,10,10\), yielding \(16\) two-sided ideals.

## Assumptions and scope

All ideals in this theorem are \(K\)-vector subspaces closed under multiplication on **both** sides by arbitrary elements of \(E\). This is the ordinary ideal notion for a nonassociative \(K\)-algebra; it is not a classification of one-sided ideals, subquandles, additive-only subgroups, or integral ideals. The splitting-field and cross-characteristic conditions ensure the full Fourier-coordinate basis exists. The statement includes the trivial one-element group, for which \(r=1\) and the ideal lattice is \(\{0,E\}\). No claim is made for fields lacking roots of unity or having characteristic dividing \(|A|\).

The original (generally nonassociative) multiplication on \(E\) is the bilinear extension of \(x\triangleright y\). The Fourier transform uses \(\widehat u(\chi)=\sum_{x\in A}u_x\chi(x)\) for \(u=\sum_{x\in A}u_x e_x\). The two actions \(\Phi,\Psi\) are commuting permutations because \(\varphi\) and \(1-\varphi\) commute.

## Proof

**Fourier coordinates.** Character orthogonality and invertibility of \(|A|\) in \(K\) give a linear isomorphism \(\mathcal F:E\longrightarrow K^{\widehat A}\), with inverse \(u_x=|A|^{-1}\sum_{\chi\in\widehat A}\widehat u(\chi)\chi(x)^{-1}\). A direct computation (also the known Fourier multiplication identity in the references) yields
\[
\widehat{u*v}(\chi)=\widehat u(\Phi\chi)\,\widehat v(\Psi\chi).
\tag{1}
\]
Write \(\delta_\chi\) for the standard coordinate vector in \(K^{\widehat A}\). We work in these coordinates from now on.

**Extracting individual Fourier coordinates.** Let \(I\) be a two-sided ideal and \(f\in I\). If \(f(\alpha)\ne0\), take \(\beta=\Phi^{-1}\alpha\) and choose the arbitrary right multiplier \(g=\delta_{\Psi\beta}\). By (1), \(f*g=f(\alpha)\delta_\beta\). Thus \(\delta_\beta\in I\). This step uses injectivity of \(\Psi\), so no other output coordinate can survive.

**Propagation along both generators.** Whenever \(\delta_\beta\in I\), applying (1) with appropriate coordinate multipliers gives
\[
\delta_\beta*\delta_{\Psi\Phi^{-1}\beta}=\delta_{\Phi^{-1}\beta},\qquad
\delta_{\Phi\Psi^{-1}\beta}*\delta_\beta=\delta_{\Psi^{-1}\beta}.
\]
Both products belong to \(I\); hence \(I\) contains the basis vectors on the entire orbit of \(\beta\) under the inverse permutations. Because these permutations have finite order, their inverse semigroup generates the same group \(H\). In particular, \(\alpha=\Phi\beta\) belongs to that orbit, and so \(\delta_\alpha\in I\). Doing this for each nonzero coordinate of each \(f\in I\) proves that \(I\) is spanned by precisely the Fourier coordinate basis vectors it contains. Its coordinate set is a union of \(H\)-orbits.

**Converse and simplicity.** For any \(H\)-orbit \(O\), both \(\Phi\) and \(\Psi\) carry \(O\) bijectively onto itself. Thus if \(f\) is supported in \(O\), formula (1) shows \(f*g\) and \(g*f\) are supported in \(O\) for every \(g\). Therefore \(E_O\) is a two-sided ideal. If \(O\ne O'\), then \(E_OE_{O'}=E_{O'}E_O=0\). Conversely, for each \(\chi\in O\), the identity \(\delta_{\Phi\chi}*\delta_{\Psi\chi}=\delta_\chi\) shows \(E_OE_O=E_O\). Any nonzero two-sided ideal of \(E_O\) is also a two-sided ideal of \(E\), since other blocks annihilate it. The extraction-and-propagation argument forces it to contain all basis vectors of \(O\); hence it equals \(E_O\). The coordinate basis now proves the unique direct-sum decomposition, dimensions, Boolean lattice, and total count.

**Prime dihedral specialization.** For \(A=\mathbb F_p\) additively and \(\varphi=-1\), the dual group identifies with \(\mathbb F_p\). The actions \(\Phi,\Psi\) multiply a character index by \(-1\) and \(2\), respectively. The zero index is a singleton orbit; each nonzero orbit is a coset of the multiplicative subgroup \(\langle-1,2\rangle\), hence has size \(h_p\), giving the formulas. For \(p=31\), \(2\) has order \(5\) modulo \(31\) and \(-1\notin\langle2\rangle\), so \(h_{31}=10\).

## Verification

Run `python verify.py` with the Python standard library. It checks equation (1) by exact finite-field arithmetic in eight cyclic dihedral cases and one distinct Alexander operation, checks noncyclic \(A=C_3\times C_3\), determines all claimed character orbits and their dimensions, and exhaustively enumerates every \(\mathbb F_7\)-linear subspace of the three-dimensional algebra \(\mathbb F_7[R_3]\) to verify there are exactly four two-sided ideals. The output ends `VERIFY_OK`. These finite calculations test the derivation; the proof above establishes the claim for all stated finite abelian groups and fields.

## Relationship to prior work

Elhamdadi, Ta and Virgin (2026), Theorem 3.2, and Ta (2026), Proposition 5.1, establish the Fourier multiplication identity (1); it is not claimed here as new. Ta's paper addresses zero-divisor and augmentation conjectures, not a complete list of two-sided ideals. Elhamdadi, Fernando and Tsvelikhovskiy (2018), Proposition 4.18, and Kaur and Singh (2023, 2024), provide decompositions into **right** simple ideals or right regular-representation constituents. One-sided constituents need not be two-sided ideals: already for \(R_7\) the right-simple decomposition has three nontrivial two-dimensional pieces while the present two-sided nontrivial block has dimension \(6\). Bardakov and Elhamdadi (2026) compute powers of particular augmentation ideals, not the global two-sided ideal lattice. Previous work on square-zero elements in Alexander quandle algebras addresses a different invariant.

The new conclusion is the complete two-sided ideal lattice, all simple two-sided constituents, their multiplication and dimensions, and the associated arithmetic count. Prior Fourier identities and module decompositions provide critical input but are not represented as unknown or as disproved. This description is not a proof of literature-wide novelty; equivalent coverage through another formulation of ideal closure or nonassociative module theory remains possible.

## Limitations

The theorem is limited to finite **latin** Alexander quandles and splitting fields of cross-characteristic. It says nothing about classification of individual idempotents or one-sided ideals. Its nonassociative simple blocks are not asserted to be associative-simple rings; their nonassociative multiplication is given by (1). The computational checks are exact but finite and do not independently certify the general theorem. The statement has not undergone independent mathematical audit. Existing work on the full structure of one-sided ideals and representation-theoretic decompositions is the closest residual priority risk.

## References

1. Lực Ta, *The zero divisor and augmentation conjectures for medial quandle rings*, arXiv:2610.20306v1 (14 October 2026), especially Section 5, Proposition 5.1. https://arxiv.org/html/2610.20306v1
2. Mohamed Elhamdadi, Lực Ta, Bryce Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799v1 (3 September 2026), Theorem 3.2. https://arxiv.org/html/2609.03799v1
3. Mohamed Elhamdadi, Neranga Fernando, Boris Tsvelikhovskiy, *Ring Theoretic Aspects of Quandles*, arXiv:1805.05908v6 (2018), especially Section 4, Proposition 4.18. https://arxiv.org/pdf/1805.05908
4. Dilpreet Kaur, Pushpendra Singh, *Decomposition of quandle rings of Takasaki quandles*, arXiv:2303.06948v1 (2023), Theorem 6.3. https://arxiv.org/pdf/2303.06948
5. Dilpreet Kaur, Pushpendra Singh, *Tensor product and quandle rings of connected quandles of prime order*, arXiv:2401.03738v2 (2024), Theorems 6.2 and 8.10. https://arxiv.org/pdf/2401.03738
6. Valeriy Bardakov, Mohamed Elhamdadi, *Idempotents and Powers of Ideals in Quandle Rings*, arXiv:2601.07057v1 (2026), Sections 4–5. https://arxiv.org/html/2601.07057v1
