# Fourier-monomial automorphisms of complex odd core-quandle algebras

## Finding

Let \(A\) be any finite abelian group of odd order, let \(X=\widehat A\) be its character group, and let \(E=\mathbb C[\operatorname{Core}(A)]\) be the nonassociative complex algebra with basis \(e_a\), \(a\in A\), and multiplication \(e_a e_b=e_{2b-a}\). Write \(m=\operatorname{exp}(A)\) and let \(H=\langle 2,-1\rangle\) be the subgroup of \((\mathbb Z/m\mathbb Z)^\times\) acting by scalar multiplication on \(X\). For the trivial group the same statement is interpreted with \(H=1\).

For each \(\chi\in X\) put \(b_\chi=|A|^{-1}\sum_{a\in A}\chi(a)e_a\). Every complex algebra automorphism of \(E\) has **exactly one** form
\[
F(b_\chi)=c_\chi b_{\sigma(\chi)},
\quad \sigma\in C_{\operatorname{Sym}(X)}(H),
\quad c_0=1,\quad c_{-\chi}=c_\chi^{-1},\quad c_{2\chi}=c_\chi^2.
\]
Conversely every such form is an automorphism. Thus the full group is the finite semidirect product
\[
\operatorname{Aut}_{\mathbb C}(E)\cong
T\rtimes C_{\operatorname{Sym}(X)}(H),
\quad T=\{(c_\chi)_{\chi\in X}\text{ satisfying the displayed constraints}\}.
\]

More explicitly, for each nonzero \(H\)-orbit \(O\) choose \(\chi\in O\), and let \(\ell\) be the least positive integer with \(2^\ell\chi=\chi\). If \(-\chi\) lies in the doubling cycle of \(\chi\), then \(|O|=\ell\), the doubling length \(\ell\) is even, and the contribution of \(O\) to \(T\) is \(\mu_{2^{\ell/2}+1}\). Otherwise \(|O|=2\ell\) and the contribution is \(\mu_{2^\ell-1}\). Here \(\mu_d\) is the group of complex \(d\)th roots of unity, and \(T\) is the direct product of these factors over all nonzero \(H\)-orbits.

Let \(K\) run over stabilizers of the \(H\)-action on \(X\), and let \(r_K\) denote the number of \(H\)-orbits whose stabilizer is \(K\). Then
\[
C_{\operatorname{Sym}(X)}(H)\cong\prod_K (H/K)\wr S_{r_K},\qquad
|\operatorname{Aut}_{\mathbb C}(E)|
=|T|\prod_K |H/K|^{r_K}r_K!.
\]

In particular, for an odd prime \(p\), write \(\ell=\operatorname{ord}_p(2)\) and set
\[
(h,M)=\begin{cases}
(\ell,2^{\ell/2}+1),&\ell\ \text{even},\\
(2\ell,2^\ell-1),&\ell\ \text{odd}.
\end{cases}
\qquad r=(p-1)/h.
\]
Then
\[
|\operatorname{Aut}_{\mathbb C}(\mathbb C[R_p])|=(Mh)^r r!,\qquad
[\operatorname{Aut}_{\mathbb C}(\mathbb C[R_p]):\operatorname{Aut}(R_p)]
=\frac{(Mh)^r r!}{p(p-1)}.
\]
The orders for \(p=3,5,7,11,13,17\) are respectively \(6,20,42,330,780,36992\). Thus \(R_{11}\) has \(330\) algebra automorphisms versus \(110\) quandle automorphisms; \(R_{17}\) has \(36992\) versus \(272\). In particular, base-quandle permutations do not exhaust the complex algebra automorphisms.

## Assumptions and scope

All automorphisms are invertible **complex-linear** maps preserving the indicated bilinear, generally nonassociative multiplication. The core quandle is the finite Latin quandle on odd-order \(A\) with \(a\triangleright b=2b-a\). The character group is written additively; its zero is the trivial character. The prime formula refers to the cyclic additive group \(A=\mathbb Z/p\mathbb Z\). The subgroup of algebra automorphisms induced by quandle automorphisms acts faithfully because the canonical basis elements are linearly independent. No conclusion about integral quandle-ring automorphisms is claimed.

## Proof

**1. Fourier multiplication.** The characters form a basis over \(\mathbb C\), by orthogonality. On taking the coefficient of \(e_z\) in the product \(b_\chi b_\psi\) and changing variables \(a=2b-z\), the inner sum is \(\sum_{b\in A}(2\chi+\psi)(b)\). Consequently,
\[
b_\chi b_\psi=
\begin{cases}b_{-\chi},&\psi=-2\chi,\\0,&\psi\ne-2\chi.\end{cases}
\tag{1}
\]
This is a complete, exact multiplication table, not an asymptotic identity.

**2. Intrinsic rank forces monomiality.** Let \(v=\sum_{\chi}v_\chi b_\chi\), and denote left multiplication by \(L_v\). Formula (1) gives
\[
L_v(b_{-2\chi})=v_\chi b_{-\chi}.
\]
Since both index maps are bijections on \(X\), \(\operatorname{rank}(L_v)=|\{\chi:v_\chi\ne0\}|\). For any algebra automorphism \(F\), the identity \(L_{F(v)}=F L_v F^{-1}\) preserves this rank. Therefore \(F\) permutes the lines comprising the rank-one locus \(\bigcup_{\chi}\mathbb C b_\chi\). As \(F\) is invertible, its matrix in the Fourier basis is monomial: \(F(b_\chi)=c_\chi b_{\sigma(\chi)}\) with \(\sigma\) a permutation and every \(c_\chi\ne0\).

**3. Exact compatibility.** Formula (1), including its zero cases, shows that monomial \(F\) is multiplicative if and only if
\[
\sigma(-2\chi)=-2\sigma(\chi),\qquad
\sigma(-\chi)=-\sigma(\chi),\qquad
c_{-\chi}=c_\chi c_{-2\chi}.
\tag{2}
\]
Since doubling is invertible, the first two equations say precisely that \(\sigma\) commutes with the scalar actions of \(2\) and \(-1\). Setting \(\chi=0\) in the scalar equation gives \(c_0=1\). Using the scalar equation both at \(\chi\) and at \(-\chi\) and canceling nonzero coefficients gives \(c_{2\chi}c_{-2\chi}=1\). Surjectivity of doubling yields \(c_{-\chi}=c_\chi^{-1}\). Substituting back gives \(c_{2\chi}=c_\chi^2\). All implications are reversible. In particular, no additional permutations, scaling families, or components are possible.

**4. Scalar and permutation factors.** Repeated doubling forces \(c_\chi^{2^\ell-1}=1\). If \(-\chi=2^k\chi\) occurs, the unique order-two element of the cyclic doubling action is the half-turn, so \(\ell\) is even and \(k\equiv\ell/2\pmod\ell\); the root condition sharpens to \(c_\chi^{2^{\ell/2}+1}=1\). If negation creates a separate doubling cycle, the original \(2^\ell-1\) root condition is sharp. Given any allowed root at one representative, all coefficients in its \(H\)-orbit are uniquely forced and compatible. Choices for distinct orbits are independent, proving the claimed product decomposition of \(T\).

A permutation commuting with \(H\) may exchange only isomorphic transitive \(H\)-orbits. Because \(H\) is abelian, the stabilizer \(K\) determines the transitive \(H\)-set up to isomorphism, and its equivariant self-permutation group is \(H/K\). Permuting \(r_K\) isomorphic orbits gives the wreath product \((H/K)\wr S_{r_K}\). Their product gives the full centralizer. Diagonal automorphisms form a normal subgroup, and every commuting permutation is itself an automorphism, proving the semidirect product.

**5. Prime case and strict extension.** On nonzero characters of \(\mathbb Z/p\mathbb Z\), multiplication by \(H\) is free, so all nonzero \(H\)-orbits have size \(h=|H|\) and number \(r=(p-1)/h\). If \(\ell=\operatorname{ord}_p(2)\) is even then \(-1=2^{\ell/2}\pmod p\); if odd, \(-1\notin\langle2\rangle\). The orbit formula then gives \(T\cong\mu_M^r\) and the centralizer \(H\wr S_r\), proving the order and index formulas. The ordinary quandle automorphisms are \(x\mapsto ux+v\), with \(u\in(\mathbb Z/p\mathbb Z)^\times\), \(v\in\mathbb Z/p\mathbb Z\), giving \(p(p-1)\) distinct permutations. At \(p=11\), \(\ell=10\), \(h=10\), \(M=33\), \(r=1\), hence \(330\) versus \(110\). Explicitly, choosing a primitive \(33\)rd root \(\zeta\), taking \(c_{2^k}=\zeta^{2^k}\) for \(k=0,\ldots,9\) and fixing \(\sigma\) produces an algebra automorphism of order \(33\); no quandle translation can have that order. This is an explicit non-quandle-induced automorphism.

## Verification

The accompanying standalone `verify.py` uses integer modular arithmetic and exact root-exponent congruences; it does not depend on numerical approximations to roots of unity. Its tests compute doubling/negation orbit decompositions for odd cyclic orders \(3,5,7,9,11,13,15,17,19,21,25\), check every defining scalar relation for each orbit generator, independently enumerate all commuting permutations in degrees at most \(9\), verify the closed prime formulas through \(31\), and construct the order-\(33\) witness for \(R_{11}\). Run `python3 verify.py` from this directory. These bounded computations supplement the complete proof above; they cannot alone verify its universal quantifiers.

## Relationship to prior work

Sangare and Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550v2, §4.2, Proposition 4.6, determine the automorphism group of the **integral** dihedral quandle algebra for odd order and identify it with the affine quandle group. Their abstract uses broader wording, but the inspected proposition explicitly has coefficient ring \(\mathbb Z\); it cannot imply the complex automorphism count because, for example, the complex \(R_{11}\) algebra has three times as many automorphisms as its affine subgroup. Their arbitrary-ring theorem in §4.1 concerns **trivial** quandles, whose algebras have different multiplication; Theorem 4.13 expresses automorphisms of even dihedral quandle algebras in terms of \(\operatorname{Aut}(k[R_n])\) for odd \(n\), retaining the latter as an input rather than computing it over \(\mathbb C\).

Elhamdadi, Ta, and Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799v1, §3, give Fourier-analytic multiplication and idempotent tools for Latin Alexander quandles, not this complete automorphism group. Zhang, *Group-ring methods for Alexander quandle rings*, arXiv:2610.08204v1, studies integral augmentation and commutator subalgebras as well as complex Peirce spectra, not the present automorphism classification. Fourier transformation itself is prior technique: the new step is the rank-one characterization followed by its full group-theoretic consequence.

The standard affine automorphism group of the underlying core quandle is also prior. It forms a subgroup of the algebra automorphism group here, but the two differ at many primes.

## Limitations

The argument requires the Fourier character basis over a splitting coefficient field where \(|A|\) is invertible; it is proved here only over \(\mathbb C\). Odd order is essential to the bijective doubling map and the left-multiplication rank argument. No generalization to characteristic dividing \(|A|\), even-order groups, arbitrary Alexander parameters, or nonabelian cores is established. Equivalent group-theoretic descriptions could in principle exist using other Fourier conventions; the asserted group is the full complex-linear automorphism group in the stated scope.

## References

1. B. Sangare and L. Ta, *Idempotents, automorphism groups, and commutator widths of quandle algebras*, arXiv:2608.01550v2 (2026), https://arxiv.org/html/2608.01550v2.
2. M. Elhamdadi, L. Ta, and B. Virgin, *Fourier Analysis and Idempotents in Quandle Algebras*, arXiv:2609.03799v1 (2026), https://arxiv.org/abs/2609.03799.
3. Z.-L. Zhang, *Group-ring methods for Alexander quandle rings*, arXiv:2610.08204v1 (2026), https://arxiv.org/abs/2610.08204.
4. M. Elhamdadi, et al., *The derivation problem for quandle algebras*, arXiv:2106.08289 (2021), https://arxiv.org/abs/2106.08289 (derivation question rather than algebra automorphism classification).
