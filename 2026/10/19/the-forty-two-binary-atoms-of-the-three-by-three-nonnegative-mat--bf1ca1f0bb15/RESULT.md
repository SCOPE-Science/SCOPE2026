# The forty-two binary atoms of the three-by-three nonnegative matrix monoid

## Finding

Let \(S=M_3(\mathbb N_0)\) be the multiplicative monoid of nonnegative-integer matrices. A **unit** is a permutation matrix; an **atom** is a nonunit which cannot be expressed as a product of two nonunits in \(S\). Put \(\mathcal B=\{0,1\}^{3\times3}\), let \(\mathcal P\) be the six permutation matrices, and let \(J\) be the all-ones matrix.

**Theorem.** Exactly **42** of the **512** matrices in \(\mathcal B\) are atoms in the full monoid \(S\), not just in the finite binary set. They comprise precisely the two disjoint double orbits
\[
\operatorname{Atoms}(S)\cap\mathcal B
=\{P(I+E_{12})Q:P,Q\in\mathcal P\}
\ \sqcup\ \{P(J-I)Q:P,Q\in\mathcal P\}.
\]
The orbit cardinalities are respectively \(36\) and \(6\). There are six units and **464** composites among the 512 matrices. The first atom orbit consists of single-entry shears up to independent permutations of rows and columns; the second comprises the six complementary permutation matrices \(J-P\), characterized among binary matrices by absolute determinant \(2\).

## Assumptions and scope

Ordinary **integer arithmetic** is used in all matrix products. Products are **not** Boolean (OR/AND) products and are **not** computed modulo a prime. Both factors are arbitrary elements of the infinite monoid \(M_3(\mathbb N_0)\): they are *not* assumed binary. We classify only target matrices whose nine entries belong to \(\{0,1\}\). The theorem makes no assertion about atoms with entries greater than one, or higher matrix orders.

## Proof

**Lemma 1 (binary reduction).** If a nonsingular binary matrix \(A\) has a factorization \(A=BC\) with \(B,C\in M_3(\mathbb N_0)\), then both factors are binary. Indeed, nonsingularity forces every column of \(B\) and every row of \(C\) to contain a positive entry. If \(B_{ij}\ge2\), choose \(k\) with \(C_{jk}>0\); then \(A_{ik}\ge B_{ij}C_{jk}\ge2\), contradiction. Likewise, if \(C_{jk}\ge2\), choose \(i\) with \(B_{ij}>0\). This argument applies to an arbitrary nonnegative-integer factorization, so testing binary nonunit factors is exhaustive for nonsingular binary targets.

**Lemma 2 (support inequality).** For nonsingular binary matrices \(B,C\) whose product \(A=BC\) is binary, write \(w(X)\) for the number of ones in \(X\). Since nonzero determinant guarantees a nonvanishing Leibniz term, \(B\) and \(C\) contain permutation matrices \(P\) and \(Q\) entrywise. Write \(B=P+U\), \(C=Q+V\) with nonnegative integer \(U,V\), each having zero entries wherever the respective permutation matrix has a one. In
\[
A=PQ+PV+UQ+UV,
\]
no two positive summands can overlap at any position because \(A\) is binary. Consequently
\[
w(A)\ge 3+w(U)+w(V)=w(B)+w(C)-3.
\]
A nonsingular binary nonunit has at least four ones: a nonsingular binary matrix with three ones must be a permutation.

**The proposed atoms are irreducible.** Every matrix in the shear orbit has four ones; a product of two nonsingular binary nonunits would have at least five by Lemma 2. The matrix \(J-I\) has six ones and absolute determinant \(2\). Exhaustive classification of binary \(3\times3\) determinants (fully implemented in the verifier) shows that every binary matrix with absolute determinant \(2\) belongs to the six-element orbit of \(J-I\) and has six ones. If \(J-I=BC\) with nonunits, Lemma 1 makes the factors binary; determinant multiplicativity makes one factor have absolute determinant \(2\) and the other \(1\). Their support counts are at least six and four, so Lemma 2 would force \(w(J-I)\ge7\), contradiction. Row/column permutations preserve atomicity because they are units.

**Exhaustiveness.** All binary singular matrices are composite. In order three, a singular binary matrix has a zero row/column or a repeated row/column (this finite assertion is exhaustively checked on all \(512\) binary matrices by `verify.py`). In the row cases, write \(A=DA\), where \(D\) deletes a zero row or copies one identical row to another while fixing the remaining rows. In the column cases, write \(A=AD\) with the analogous column operation. In every case, \(D\) is a singular nonunit, as is \(A\).

It remains to classify the nonsingular matrices. The verifier evaluates all \(512\) binary matrices, their exact integer determinants and the action of all \(36\) pairs of row and column permutations, producing precisely eight nonsingular double orbits. They are fully described by the following table (the support size is the number of ones):

| Support size | Double-orbit size | Absolute determinant | Classification |
| ---: | ---: | ---: | --- |
| 3 | 6 | 1 | units |
| 4 | 36 | 1 | atoms (shears) |
| 5 | 18 | 1 | composite |
| 5 | 18 | 1 | composite |
| 5 | 36 | 1 | composite |
| 6 | 6 | 2 | atoms (complementary permutations) |
| 6 | 36 | 1 | composite |
| 7 | 18 | 1 | composite |

For each of the five composite orbits, the program supplies an explicit product of two binary nonunits for its lexicographically least representative and verifies that product. Independent row/column permutations transport these factorizations to the entire orbit. The count is therefore six units, \(36+6=42\) atoms, \(126\) nonsingular composites and \(338\) singular composites, totaling \(512\).

For completeness, `verify.py` also directly multiplies **every ordered pair** of binary nonunits. It finds exactly 464 binary products, confirms that none belongs to the two proposed atom orbits, and independently verifies the orbit structure and the singular witness criterion. Lemma 1 makes this direct finite certificate logically exhaustive for nonsingular targets; the explicit singular decompositions cover the rest. All loops, matrices, determinant formulas and classification assertions are included in the standalone standard-library verifier.

## Verification

Run `python3 verify.py` from the directory containing this report and the standalone script. It prints `VERIFY_OK` and the eight nonsingular double-orbit rows. The verifier requires Python 3 standard library only. It exhaustively checks \(512\) matrices, \(506^2\) ordered binary nonunit pairs, the full six-by-six permutation action, and exact determinants over the integers. It does not extrapolate from samples. The computer enumeration proves only finite assertions; the reduction in Lemma 1 and the explicit singular decompositions justify the move from finite binary factor searches to primality in the full infinite nonnegative-integer monoid.

## Relationship to prior work

Bell, Foster, Reidenbach and Semukhin (first public September 22, 2026) define nonnegative matrix primes under precisely the nonunit-factor criterion used here, and develop an algorithm for the \(2\times2\) case. Their full manuscript does not enumerate binary \(3\times3\) atoms. Baeth, Chen, Heilbrunn, Liu and Young (published online 2021) give general factorization theory and special atom families in nonnegative-integer matrix semigroups; their introduction explicitly says a complete classification of atoms of the general full matrix monoid is unavailable, while their explicit classification focuses substantially on order two. Chen (2015) classifies atoms of an upper-triangular order-three subsemigroup, a different factorization domain, and does not imply the six-element cyclic support orbit found here. Literature on nonnegative *rank* or Boolean-semiring products uses different objects or operations. The standard shear family is already known; novelty asserted here concerns the **complete binary order-three boundary**, including the exceptional nontriangular determinant-two orbit and exact counts.

## Limitations

A possible earlier exhaustive binary \(3\times3\) factorization census under alternate terminology has not been ruled out. The mathematical claim is deliberately limited to order three and zero-one target matrices. The result is not a classification of all nonnegative-integer matrix atoms in dimension three. The computer verification is a transparent finite certificate and is not independent expert auditing.

## References

1. P. C. Bell, E. Foster, D. Reidenbach and P. Semukhin, *Factorisability of Low Dimensional Non-Negative Integer Matrices* (2026), arXiv:2609.26033, https://arxiv.org/abs/2609.26033 (first public 2026-09-22).
2. N. R. Baeth, H. Chen, G. Heilbrunn, R. Liu and M. Young, *Semigroups of non-negative integer-valued matrices*, Communications in Algebra 50 (2022), 1199–1219, https://doi.org/10.1080/00927872.2021.1979569 (first online 2021-10-09).
3. H. Chen, *On Factorizations of Upper Triangular Nonnegative Matrices of Order Three*, Discrete Dynamics in Nature and Society (2015), article 960182, https://doi.org/10.1155/2015/960182.
4. L. Dever, E. G. Goedhart, G. S. Heilbrunn and T. W. H. Wong, *Atoms in the Semigroup of Non-Negative Integer Matrices* (2026), arXiv:2606.14914, https://arxiv.org/abs/2606.14914 (order-two nonsingular semigroup).
