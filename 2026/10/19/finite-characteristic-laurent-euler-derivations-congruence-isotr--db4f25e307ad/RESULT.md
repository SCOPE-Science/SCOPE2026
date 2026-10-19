# Finite-characteristic Laurent Euler derivations: congruence isotropy and conjugacy orbits

## Finding
Let \(K\) be a field of characteristic \(p>0\), let \(n\ge1\), and let \(R=K[x_1^{\pm1},\dots,x_n^{\pm1}]\). For \(\mu=(\mu_1,\dots,\mu_n)\in K^n\), define the **Euler derivation** \(D_\mu(x_i)=\mu_i x_i\). Write
\[
W_\mu=\operatorname{span}_{\mathbb F_p}(\mu_1,\dots,\mu_n),\quad r=\dim_{\mathbb F_p}W_\mu,\quad \delta_p=|\{1,-1\}\subset\mathbb F_p^\times|.
\]
Thus \(0\le r\le n\); \(\delta_2=1\) and \(\delta_p=2\) for odd \(p\). Every \(D_\mu\) is locally finite. The following are exact.

1. The lattice \(L_\mu=\{a\in\mathbb Z^n:\sum_i a_i\mu_i=0\}\) has index \(p^r\). The constant ring is \(\ker D_\mu=K[L_\mu]\), a Laurent polynomial algebra in \(n\) variables. The module \(R\) is free of rank \(p^r\) over \(\ker D_\mu\). Its fraction-field extension is purely inseparable of exponent at most one and degree \(p^r\).
2. Every \(K\)-automorphism of \(R\) is a scalar-monomial substitution. The subgroup commuting with \(D_\mu\) is
\[
\operatorname{Aut}_K(R)_{D_\mu}\cong (K^\times)^n\rtimes G_\mu,\qquad
G_\mu=\{M\in\operatorname{GL}_n(\mathbb Z):\mu^{\mathsf T}M=\mu^{\mathsf T}\}.
\]
The kernel \(\Gamma_n(p)=\{M\in\operatorname{GL}_n(\mathbb Z):M\equiv I_n\pmod p\}\) is contained in \(G_\mu\). The **exact index** is
\[
[\operatorname{GL}_n(\mathbb Z):G_\mu]=
\begin{cases}
\displaystyle\prod_{i=0}^{r-1}(p^n-p^i),&0\le r<n,\\
\delta_p|\operatorname{SL}_n(\mathbb F_p)|,&r=n.
\end{cases}
\]
The empty product is one, and \(|\operatorname{SL}_1(\mathbb F_p)|=1\). For \(r=n\), in fact \(G_\mu=\Gamma_n(p)\).
3. Suppose \(K=\mathbb F_{p^f}\). If \(r<n\), two Euler derivations are conjugate by \(K\)-algebra automorphisms exactly when their \(\mathbb F_p\)-weight spans coincide. If \(r=n\), they must have the same weight span, and their two corresponding ordered \(\mathbb F_p\)-bases lie in the same determinant-\(\pm1\) orbit; equivalently their transition matrix has determinant in \(\{1,-1\}\). Consequently the total number of conjugacy classes, **including the zero derivation**, is
\[
\boxed{1+\sum_{r=1}^{\min(f,n-1)}{f\brack r}_p+
\mathbf 1_{n\le f}\frac{p-1}{\delta_p}{f\brack n}_p},
\]
where \({f\brack r}_p=\prod_{i=0}^{r-1}(p^f-p^i)/\prod_{i=0}^{r-1}(p^r-p^i)\) is the Gaussian binomial coefficient.

For instance the formula gives \(9\) conjugacy classes over \(\mathbb F_{25}\) in two variables, including the zero derivation. The determinant-orientation term is essential: for full-rank weights in odd characteristic \(p\ge5\), one weight span splits into \((p-1)/2\) classes rather than one.

## Assumptions and scope
All automorphisms are \(K\)-linear; the characteristic is prime \(p>0\), and the group \(\operatorname{GL}_n(\mathbb Z)\) acts through honest integral exponent matrices. We classify **Euler derivations**, not all derivations and not all locally finite derivations. The weight span is an \(\mathbb F_p\)-space even if \(K\) is larger or nonperfect. The finite-field conjugacy count assumes \(K=\mathbb F_{p^f}\). The first two assertions hold over arbitrary characteristic-\(p\) fields.

## Proof
**Units and the exact isotropy equation.** Units in a Laurent polynomial algebra over a field are precisely \(c x^a\), with \(c\in K^\times\) and \(a\in\mathbb Z^n\). Indeed, for an invertible Laurent polynomial, a generic integral linear functional separating its finitely many exponent vectors makes the extreme terms of a product visible, forcing both supports to be singletons. Therefore every automorphism has \(\varphi(x_j)=c_j\prod_i x_i^{M_{ij}}\) with \(M\in\operatorname{GL}_n(\mathbb Z)\). Since \(D_\mu(x^a)=(\sum_i a_i\mu_i)x^a\), the equation \(D_\mu\varphi(x_j)=\varphi D_\mu(x_j)\) is exactly \(\sum_i M_{ij}\mu_i=\mu_j\). Scalars are unrestricted; hence the asserted semidirect product and isotropy equation. On any Laurent polynomial, iterates of \(D_\mu\) stay in its finite-dimensional monomial support, proving local finiteness.

**The invariant lattice.** The homomorphism \(\theta:\mathbb Z^n\to (K,+)\) given by \(a\mapsto\sum_i a_i\mu_i\) has image \(W_\mu\), an elementary abelian \(p\)-group of order \(p^r\). By the first isomorphism theorem, \(\mathbb Z^n/L_\mu\cong(\mathbb Z/p\mathbb Z)^r\), so \([\mathbb Z^n:L_\mu]=p^r\) and \(p\mathbb Z^n\subseteq L_\mu\). Distinct Laurent monomials are linearly independent and are eigenvectors of \(D_\mu\); hence a Laurent polynomial lies in its kernel if and only if all exponent vectors lie in \(L_\mu\). This proves \(\ker D_\mu=K[L_\mu]\). Because \(L_\mu\) is a free abelian group of rank \(n\), its group algebra is a Laurent polynomial ring on \(n\) units. Choosing coset representatives in \(\mathbb Z^n/L_\mu\) decomposes \(R\) as a direct sum of \(p^r\) rank-one free modules over \(K[L_\mu]\). Each \(x_i^p\) lies in the constant ring, giving purely inseparable exponent at most one; passing to fraction fields preserves the displayed degree because the coset-monomial basis remains independent.

**The integral determinant restriction.** In any \(\mathbb F_p\)-basis of \(W_\mu\), form the \(r\times n\) matrix \(C_\mu\) of weight coefficients, of row rank \(r\). The condition for \(M\) is \(C_\mu\overline M=C_\mu\), where the bar means reduction modulo \(p\). The image of \(\operatorname{GL}_n(\mathbb Z)\) under this reduction is exactly
\[
H_{n,p}=\{B\in\operatorname{GL}_n(\mathbb F_p):\det B\in\{1,-1\}\}.
\]
For \(n\ge2\), elementary matrices over \(\mathbb Z\) reduce onto elementary generators of \(\operatorname{SL}_n(\mathbb F_p)\); a diagonal integral sign matrix supplies determinant \(-1\). The reverse inclusion follows because an integral invertible matrix has determinant \(\pm1\). For \(n=1\), the statement is immediate.

The right action of \(H_{n,p}\) on full-row-rank \(r\times n\) matrices is transitive for \(r<n\): any invertible change between two ordered rank-\(r\) covector frames can have its determinant adjusted arbitrarily by a change on the nonempty complementary subspace. Its orbit therefore consists of all ordered linearly independent \(r\)-tuples of row vectors, numbering \(\prod_{i=0}^{r-1}(p^n-p^i)\). For \(r=n\), each full-rank square matrix has trivial right stabilizer and its orbit size is \(|H_{n,p}|=\delta_p|\operatorname{SL}_n(\mathbb F_p)|\). Since \(G_\mu\) is the full inverse image of a frame stabilizer, these orbit sizes equal its indices, and \(\Gamma_n(p)\subseteq G_\mu\). At \(r=n\), the only matrix satisfying \(C_\mu B=C_\mu\) is \(I_n\), giving equality with \(\Gamma_n(p)\).

**Classification over finite fields.** A monomial substitution transforms the weight list by right multiplication by an element of \(H_{n,p}\) (up to inversion, which does not change the orbit). Accordingly the weight span \(W_\mu\) is invariant. For a fixed \(r\)-space \(W\subseteq\mathbb F_{p^f}\), its ordered \(n\)-tuple of spanning weights is represented by a full-row-rank \(r\times n\) matrix in a fixed basis of \(W\). If \(r<n\), the transitivity above gives one conjugacy class. If \(r=n\), its square-matrix determinant is preserved modulo the subgroup \(\{1,-1\}\); conversely, equality of determinant cosets gives a connecting element of \(H_{n,p}\). Hence precisely \((p-1)/\delta_p\) classes belong to each \(n\)-dimensional span. There are \({f\brack r}_p\) subspaces of dimension \(r\) in \(\mathbb F_p^f\). Summing over ranks and including the zero span gives the displayed formula. This completes the proof.

## Verification
Run `python verify.py` from the extracted package. The script independently enumerates every finite matrix in \(H_{n,p}\) and its action on all \(n\)-weight lists drawn from an \(f\)-dimensional \(\mathbb F_p\)-vector space. For nine configurations \((p,n,f)\), it checks exact image-group cardinality, all orbit sizes, stabilizer indices, all invariant-lattice image indices, and the number of orbits against the closed formula. These finite enumerations validate the tested cases; the proof above establishes the arbitrary-parameter theorem. For \((p,n,f)=(5,2,2)\), the enumerator finds exactly nine classes.

## Relationship to prior work
Porto and Veloso (2026) study isotropy and locally finite derivations of Laurent polynomial rings **over characteristic-zero fields**. Their general monomial automorphism viewpoint and exponent-commutation criterion are useful antecedents and are not claimed as new here. Their torsion-free weight-group rank and subsequent stabilizer decomposition do not cover the positive-characteristic, finite-index congruence isotropy proved here. In characteristic \(p\), the weight image is a finite elementary abelian group rather than a free abelian group, and the determinant restriction on reductions of integer automorphisms creates additional full-rank finite-field conjugacy classes. Bavula (2016) likewise establishes a Laurent automorphism-group description in a characteristic-zero Lie-algebra context; these general unit arguments are classical. This result does **not** establish any novelty for the basic scalar-monomial automorphism lemma.

## Limitations
The classification is specific to diagonal Euler derivations and \(K\)-linear automorphisms, not arbitrary algebraic vector fields or field-semilinear automorphisms. The exact conjugacy class count requires finite \(K\). Prior work on torus actions or modular logarithmic derivations using a different vocabulary may yield equivalent statements; no independent literature audit has been performed. The included finite tests do not certify arbitrary parameters by themselves.

## References
1. Porto and Veloso, *Isotropy groups of locally finite derivations of Laurent polynomial algebras*, arXiv:2610.12777v1 (first public version October 8, 2026); https://arxiv.org/abs/2610.12777.
2. V. V. Bavula, *The groups of automorphisms of the Witt \(W_n\) and Virasoro Lie algebras* (2016), accessible preprint used for the established characteristic-zero Laurent automorphism framework.
3. W. Zhao, *The LFED and LNED conjectures for Laurent polynomial algebras* (2017), background on locally finite Laurent derivations; abstract consulted, not the complete paper.
