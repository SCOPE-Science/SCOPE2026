# Exact inertia of the mutual-annihilation matrix of the rook monoid

## Finding

Let \(n\geq1\), and let \(\mathcal I_n\) be the symmetric inverse monoid of all partial bijections of an \(n\)-element set, including the empty map \(0\). Define a real symmetric matrix \(Z_n\), with rows and columns indexed by **all** elements of \(\mathcal I_n\), by
\[
(Z_n)_{\alpha,\beta}=\begin{cases}1,&\alpha\beta=\beta\alpha=0,\\0,&\text{otherwise.}\end{cases}
\]
**The diagonal is retained:** if \(\alpha^2=0\), its diagonal entry is one. This is the matrix of the mutual-zero-product relation, not the adjacency matrix of a simple graph obtained by deleting loops or zero.

Put
\[
N_n=\sum_{r=0}^n\binom nr^2r!,\qquad M_n=\binom{2n}{n},\qquad
F_n=\begin{cases}\binom n{n/2},&n\text{ even},\\0,&n\text{ odd}.\end{cases}
\]
Then, for every \(n\ge1\), the numbers of strictly positive, strictly negative, and zero **real** eigenvalues of \(Z_n\), counted with multiplicity, are exactly
\[
\boxed{\left(\frac{M_n+F_n}{2},\frac{M_n-F_n}{2},N_n-M_n\right).}
\]
In particular, \(\operatorname{rank}_{\mathbb R}Z_n=M_n\), so the rank is the central binomial coefficient although the matrix order is \(N_n\). Moreover, the product of all nonzero eigenvalues (with algebraic multiplicity) is exactly
\[
\boxed{(-1)^{(M_n-F_n)/2}\prod_{r=0}^n(r!)^{\binom nr^2}.}
\]
This product is the real pseudo-determinant; it is not the product of only positive eigenvalues.

## Assumptions and scope

The monoid elements are injective partial functions, not arbitrary partial transformations. The underlying set can be any set of cardinality \(n\); relabeling only permutes the rows and columns. Composition order does not affect the stated simultaneous-zero-product condition. The matrix is symmetric, is indexed by the full monoid including \(0\), and includes all diagonal entries as defined. No assertion is made about the inertia of the loopless zero-divisor graph with zero removed. Inertia is interpreted over the real numbers.

## Proof

**1. The relation depends only on domain and image.** For a partial bijection \(\alpha\), write \(D_\alpha=\operatorname{dom}(\alpha)\) and \(R_\alpha=\operatorname{im}(\alpha)\). The composite \(\alpha\beta\) is empty precisely when \(R_\alpha\cap D_\beta=\varnothing\). Similarly \(\beta\alpha=0\) precisely when \(R_\beta\cap D_\alpha=\varnothing\). Hence neither condition involves how the bijections are matched internally.

Let
\[
\mathcal P_n=\{(D,R):D,R\subseteq[n],\ |D|=|R|\}.
\]
Define the real \(N_n\)-by-\(M_n\) incidence matrix \(P\) by \(P_{\alpha,(D,R)}=1\) if and only if \((D_\alpha,R_\alpha)=(D,R)\). On \(\mathcal P_n\), define the symmetric \(M_n\)-by-\(M_n\) matrix
\[
K_{(D,R),(E,F)}=\mathbf1_{R\cap E=\varnothing}\mathbf1_{D\cap F=\varnothing}.
\]
Then \(Z_n=PKP^{\mathsf T}\). The columns of \(P\) have pairwise disjoint supports; the support of a column indexed by a rank-\(r\) pair has exactly \(r!\) members. Consequently
\[
P^{\mathsf T}P=\operatorname{diag}_{(D,R)\in\mathcal P_n}(|D|!),
\]
which is positive definite. By an orthogonal change of basis, \(Z_n\) is congruent to \((P^{\mathsf T}P)^{1/2}K(P^{\mathsf T}P)^{1/2}\) direct-summed with a zero matrix of order \(N_n-M_n\). Thus it has the same nonzero inertia as \(K\). Its nonzero eigenvalue product equals \(\det K\cdot\det(P^{\mathsf T}P)\) (equivalently, use equality of the nonzero eigenvalues of \(PKP^{\mathsf T}\) and \(K P^{\mathsf T}P\)).

**2. A rank-antitriangular deformation.** Order the elements \((D,R)\in\mathcal P_n\) by \(r=|D|=|R|\). If a row has rank \(a\) and a column has rank \(b\), then its entry in \(K\) vanishes when \(a+b>n\). When \(a+b=n\), both disjointness conditions force
\[
E=R^c,\qquad F=D^c,
\]
so the entire block from rank \(a\) to rank \(n-a\) is the permutation matrix of the complement-and-swap bijection. The numbers of rows and columns in these blocks agree, because \(\binom na^2=\binom n{n-a}^2\).

For \(0\le t\le1\), define \(K(t)\) by retaining the entries of \(K\) on \(a+b=n\), multiplying the entries on \(a+b<n\) by \(t\), and retaining zeros on \(a+b>n\). Each \(K(t)\) is real symmetric. Upon reversing the order of the column-rank blocks, \(K(t)\) is block triangular with permutation-matrix diagonal blocks. Therefore \(\det K(t)\neq0\) for every \(t\). No eigenvalue can cross zero in this continuous family, so the real inertia is constant along it; likewise its determinant is the product of the fixed diagonal-block determinants.

At \(t=0\), \(K(0)\) is exactly the permutation matrix of the involution
\[
T:(D,R)\longmapsto(R^c,D^c).
\]
Its fixed points satisfy \(R=D^c\) and \(|D|=|R|=n/2\). There are none when \(n\) is odd and exactly \(\binom n{n/2}\) when \(n\) is even. Every transposition of \(T\) contributes one eigenvalue \(+1\) and one eigenvalue \(-1\); every fixed point contributes \(+1\). Hence, writing \(M_n=|\mathcal P_n|\), the inertia of \(K(0)\), and thus of \(K(1)=K\), is
\[
\left(\frac{M_n+F_n}{2},\frac{M_n-F_n}{2},0\right),
\quad \det K=(-1)^{(M_n-F_n)/2}.
\]

**3. Counting and the spectral product.** For each \(r\), there are \(\binom nr^2\) ordered domain-image pairs and exactly \(r!\) bijections between the selected sets. Therefore
\[
|\mathcal I_n|=N_n=\sum_{r=0}^n\binom nr^2r!,
\qquad
|\mathcal P_n|=\sum_{r=0}^n\binom nr^2=\binom{2n}{n},
\]
the second equality being Vandermonde's identity. Finally
\[
\det(P^{\mathsf T}P)=\prod_{r=0}^n(r!)^{\binom nr^2}.
\]
Substituting these values into Step 1 proves both displayed formulas, including nullity and the nonzero eigenvalue product. This completes the proof for every integer \(n\ge1\).

## Verification

The accompanying `verify.py` (Python standard library only) independently constructs partial bijections as lists of matched coordinates and tests both compositions directly for every ordered pair when \(n=1,2,3\). It compares each entry with the separate domain-image disjointness kernel, computes the exact symmetric inertia of the compressed kernel using rational congruence pivots for these sizes, and checks its determinant modulo two distinct primes for \(n=1,2,3,4\). The resulting tuples \((\text{positive},\text{negative},\text{zero})\) for the full matrix are respectively
\[
(1,1,0),\quad (4,2,1),\quad (10,10,14),\quad(38,32,139).
\]
Run `python3 verify.py` from the directory containing the extracted source. The program reports `VERIFY_OK_ROOK_MUTUAL_ANNIHILATION_INERTIA` if all checks pass. Modular checks and finite enumerations are corroboration, not a proof for unbounded \(n\); the proof above is exact and uniform.

## Relationship to prior work

Grood [1] gives a representation-theoretic construction for the rook monoid and records its rank-cardinality formula; Solomon [2] gives an extensive representation theory of the same monoid. Malandro [3] develops Fourier/spectral analysis of the rook monoid algebra, but that use of “spectral” concerns Fourier decompositions rather than eigenvalues of the simultaneous-zero-composition relation matrix. Araújo, Bentz and Konieczny [4] study the commuting **simple** graph of the symmetric inverse semigroup, including clique numbers and diameters; that graph contains pairs with nonzero equal compositions. Toker [5] studies a loopless zero-divisor graph for the larger monoid of **all partial transformations**, including vertex degrees and connectivity, rather than the loop-retaining spectral form on partial bijections here. These inspected statements do not supply the present exact inertia and nonzero spectral product, though indirect implications from other literature remain possible.

## Limitations

The kernel includes the zero map and diagonal loops; deleting either generally changes the inertia. Only the signs and product of the nonzero real eigenvalues are determined, not each eigenvalue separately. The result does not classify the spectra of arbitrary partial-transformation semigroups or other inverse semigroups. Complete historical priority beyond the inspected sources has not been established. No independent mathematical audit has been performed.

## References

1. C. Grood, *A Specht Module Analog for the Rook Monoid*, Electronic Journal of Combinatorics 9 (2002), R2, published online 18 December 2001. DOI: https://doi.org/10.37236/1619 .
2. L. Solomon, *Representations of the rook monoid*, Journal of Algebra 256 (2002), 309–342. DOI: https://doi.org/10.1016/S0021-8693(02)00004-2 .
3. M. E. Malandro, *Inverse semigroup spectral analysis for partially ranked data*, arXiv:1110.5679, first posted 25 October 2011; https://arxiv.org/abs/1110.5679 .
4. J. Araújo, W. Bentz, J. Konieczny, *The Commuting Graph of the Symmetric Inverse Semigroup*, arXiv:1205.1664, first posted 8 May 2012; https://arxiv.org/abs/1205.1664 .
5. K. Toker, *Zero-divisor graphs of partial transformation semigroups*, Turkish Journal of Mathematics 45 (2021), 2323–2330. DOI: https://doi.org/10.3906/mat-2012-94 .
