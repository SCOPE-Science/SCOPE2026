# Automorphisms of heterogeneous truncated coordinate-cross algebras over finite fields

## Finding
For any prime power \(q\), integer \(n\ge2\), and integers \(d_1,\ldots,d_n\ge3\) **not all equal**, consider
\[
A=\mathbb F_q[x_1,\ldots,x_n]/(x_ix_j\ (i\ne j),\ x_i^{d_i}\ (1\le i\le n)).
\]
For each integer \(r\), put \(m_r=|\{i:d_i=r\}|\). Every \(\mathbb F_q\)-algebra automorphism is uniquely expressible as
\[
\phi(x_i)=f_i(x_{\sigma(i)})+\sum_{j\ne\sigma(i)}c_{ij}x_j^{d_j-1},
\]
where \(\sigma\in S_n\) satisfies \(d_{\sigma(i)}=d_i\), \(f_i(T)=\sum_{s=1}^{d_i-1}a_{i,s}T^s\) with \(a_{i,1}\ne0\), and \(c_{ij}\in\mathbb F_q\) are arbitrary. Thus
\[
|\operatorname{Aut}_{\mathbb F_q}(A)|=\left(\prod_r m_r!\right)(q-1)^n q^{\sum_i(d_i-2)+n(n-1)}.
\]
Its action on the cotangent space is precisely the subgroup of monomial matrices whose underlying permutations preserve the branch-length labels \(d_i\); the kernel has the displayed \(q\)-power order.

## Assumptions and scope
The algebra is commutative, unital, finite-dimensional, and local over \(\mathbb F_q\). All \(d_i\ge3\), the number of branches \(n\ge2\), and at least two branch lengths are unequal. Automorphisms fix \(\mathbb F_q\) elementwise. The basis is \(1\) and \(x_i^s\) for \(1\le s<d_i\). The maximal ideal \(\mathfrak m\) is the span of all nonconstant basis monomials.

## Proof
(1) Every automorphism preserves \(\mathfrak m\) and induces an invertible matrix on \(\mathfrak m/\mathfrak m^2\). Write its linear coefficients as \(b_{ij}\) in the image of \(x_i\). For distinct \(i,k\), the relation \(x_ix_k=0\) forces \(b_{ij}b_{kj}=0\) for every \(j\), because the \(x_j^2\) are linearly independent in \(\mathfrak m^2/\mathfrak m^3\), using \(d_j\ge3\). Each column therefore has at most one nonzero entry. Invertibility gives exactly one in each row and column: \(b_{i,\sigma(i)}\ne0\) for a permutation \(\sigma\).

(2) For each \(i\), the component of \(\phi(x_i)\) along branch \(x_{\sigma(i)}\) has order one. If \(j\ne\sigma(i)\), let \(k\ne i\) be the unique index with \(\sigma(k)=j\). The relation \(\phi(x_i)\phi(x_k)=0\) forces the component of \(\phi(x_i)\) in the \(x_j\)-branch to be divisible by \(x_j^{d_j-1}\), since \(\phi(x_k)\) has a nonzero linear term on that branch. This yields the claimed shape.

(3) Since \(\phi(x_i)^{d_i}=0\), the nonzero linear term on branch \(\sigma(i)\) implies \(d_{\sigma(i)}\le d_i\). The permutation preserves the sum of these integers, so all inequalities are equalities. Hence \(\sigma\) preserves the full length profile.

(4) Conversely, every displayed assignment respects the mixed-product relations: its cross-branch terms lie in branch socles, which annihilate all positive-degree terms of their own branches; terms from distinct branches multiply to zero. It respects the power relations because the principal target branch has the same nilpotency index, and socle terms square to zero. Its linear part is invertible on \(\mathfrak m/\mathfrak m^2\), hence it generates \(\mathfrak m\) and defines a surjective endomorphism of a finite-dimensional local algebra; it is therefore an automorphism. Coefficients are unique in the stated basis.

(5) There are \(\prod_r m_r!\) admissible permutations, \((q-1)q^{d_i-2}\) choices of each \(f_i\), and \(q^{n(n-1)}\) choices of the socle-shear coefficients. Multiplication gives the formula and kernel size.

## Verification
The accompanying Python 3 standard-library program `verify_branch.py` independently enumerates pairs of candidate images for four asymmetric two-branch finite-field cases. It tests all power and mixed-product relations and invertibility of the cotangent linear map. Results: for \((q;d_1,d_2)=(2;3,4),(2;3,5),(2;4,5),(3;3,4)\) the counts are respectively \(32,64,128,972\), in exact agreement. An additional \((2;3,3,4)\) parameter calculation checks the closed count. These finite calculations do not prove the universal statement; steps (1)--(5) do.

## Relationship to prior work
Díaz--Lucchini Arteche--Manzano-Flores (arXiv:2609.13741, originally public September 12, 2026) analyze automorphism groups of zero-dimensional monomial algebras in characteristic zero. Díaz--Liendo--Manzano-Flores--Regeta (arXiv:2408.02197, originally public August 5, 2024) provide broader characteristic-zero structure. A previously published theorem on **uniform-length** truncated coordinate-cross algebras over arbitrary fields (published-finding corpus record listed below) treats the all-equal case. The present heterogeneous-length formula does not claim that case as new; the branch-label-preservation criterion, mixed-length normal form, and its finite-field enumeration are the specific scope here. The older structural studies and the uniform-length case motivate, but do not directly state, this heterogeneous positive-characteristic count.

## Limitations
The case of nilpotency length two is excluded because square terms vanish in the cotangent multiplication test and linear mixing changes qualitatively. No claim is made for arbitrary monomial ideals, semilinear field automorphisms, or infinite rings. The most relevant newer characteristic-zero preprint was accessible at abstract level, not in full text, during comparison; a hidden equivalent mixed-length specialization remains possible. Independent review has not been carried out.

## References
1. R. Díaz, G. Lucchini Arteche, G. Manzano-Flores, *The structure of automorphism groups of zero-dimensional monomial algebras*, arXiv:2609.13741 (first public 2026-09-12).
2. R. Díaz, A. Liendo, G. Manzano-Flores, A. Regeta, *The Automorphism groups of zero-dimensional monomial algebras*, arXiv:2408.02197 (first public 2024-08-05).
3. *Automorphisms of truncated coordinate-cross algebras over arbitrary fields*, published published-finding corpus record `2026/10/4/SCOPE-automorphisms-of-truncated-coordinate-cross-algebras-over-arbitr--625ba30274cb` (uniform-length case).
