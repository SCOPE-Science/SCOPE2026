# A sharp length-\(9\) dual-weight-two witness for Euclidean weight over \(\mathbb F_5\)

## Finding

Let the Euclidean weight on \(\mathbb F_5\) be
\[
e(0)=0,\qquad e(1)=e(4)=1,\qquad e(2)=e(3)=4.
\]
There are two dimension-\(2\), effective-length-\(9\) linear codes \(C,D\subseteq\mathbb F_5^9\) with generator matrices
\[
G_C=\begin{pmatrix}
2&1&2&1&1&1&1&2&2\\
3&3&1&1&1&1&1&2&2
\end{pmatrix},
\qquad
G_D=\begin{pmatrix}
2&1&1&2&1&1&2&2&2\\
4&4&4&3&3&3&2&2&2
\end{pmatrix}.
\]
They have the same Euclidean-weight enumerator,
\[
1+2y^6+2y^9+2y^{13}+2y^{17}+2y^{18}+4y^{21}+2y^{22}+2y^{23}+4y^{24}+2y^{27},
\]
but their duals already differ at Euclidean weight \(2\):
\[
A_2(C^\perp)=14,\qquad A_2(D^\perp)=10.
\]
Moreover, among all dimension-\(2\) linear codes over \(\mathbb F_5\) of effective length at most \(8\), equality of Euclidean-weight enumerators forces equality of the dual Euclidean weight-\(2\) coefficient. Thus \(9\) is the minimum effective length for a dimension-\(2\) failure of Euclidean-weight duality that is visible in dual Euclidean weight \(2\).

## Assumptions and scope

Effective length means that a generator matrix has no zero column; zero columns are excluded because they do not contribute to the primal Euclidean weight and create a separate, trivial coordinate-extension issue. The claim concerns dimension-\(2\) codes and the first dual coefficient \(A_2\). It does not assert that length \(9\) is the minimum possible duality counterexample in arbitrary dimension or when the first discrepancy is allowed to occur at a larger dual weight.

Two generator columns that differ by multiplication by \(-1\) are identified because coordinate multiplication by \(-1\) preserves the Euclidean weight. There are exactly \((5^2-1)/2=12\) resulting nonzero column orbits in \(\mathbb F_5^2\).

## Proof

For the displayed matrices, direct enumeration of the \(5^2=25\) messages gives the same multiset of Euclidean weights for \(C\) and \(D\), namely the coefficients in the displayed enumerator.

For a dimension-\(2\) code with no zero generator column, normalize each column modulo the Euclidean symmetry group \(\{\pm1\}\). Fix the twelve representatives
\[
(0,1),(0,2),(1,0),(2,0),(1,2),(2,4),(1,4),(2,3),(1,3),(2,1),(1,1),(2,2).
\]
After coordinate permutation, the code is represented by a multiplicity vector \(\eta=(\eta_1,\ldots,\eta_{12})\) with \(\sum_j\eta_j=n\). Every effective dimension-\(2\) code occurs in this census; the same code may occur more than once under different row bases, which is harmless for an exhaustive nonexistence check.

A dual word of Euclidean weight \(2\) must have exactly two nonzero coordinates, both equal to \(\pm1\), because the nonzero symbol weights are \(1\) and \(4\). Such a dual word supported on coordinates \(i,j\) exists exactly when the corresponding generator columns agree up to sign. Each unordered equal-or-opposite column pair gives precisely two dual words. Therefore
\[
A_2(C^\perp)=2\sum_{j=1}^{12}\binom{\eta_j}{2}.
\]
For the two displayed matrices, their normalized multiplicities are
\[
\eta_C=(0,0,0,0,0,0,0,1,1,1,4,2),
\]
\[
\eta_D=(0,0,0,0,0,1,2,1,2,0,0,3),
\]
which give \(A_2(C^\perp)=14\) and \(A_2(D^\perp)=10\).

For sharpness, enumerate every twelve-part nonnegative multiplicity vector of total length \(n\) for each \(2\le n\le8\), retain exactly those whose occupied representatives span \(\mathbb F_5^2\), compute the exact Euclidean-weight multiset of all \(24\) nonzero messages, and group multiplicity vectors by that multiset. The numbers of retained normalized full-rank states are
\[
60,\ 340,\ 1335,\ 4332,\ 12334,\ 31776,\ 75528
\]
for lengths \(2,3,4,5,6,7,8\), respectively. In every group at every one of those lengths, the quantity \(2\sum_j\binom{\eta_j}{2}\) is constant. Hence no shorter effective dimension-\(2\) pair with equal primal Euclidean enumerator can differ at dual Euclidean weight \(2\).

## Verification

`artifacts/verify.py` uses only exact integer arithmetic and the Python standard library. It reconstructs both matrices, checks rank \(2\), recovers the two normalized multiplicity vectors, enumerates all \(25\) primal messages, and verifies the common Euclidean-weight enumerator.

It independently computes each full dual Euclidean-weight enumerator by dynamic programming over the \(25\) syndromes in \(\mathbb F_5^2\). Each dual contains exactly \(5^7=78125\) words, and the weight-\(2\) coefficients are \(14\) and \(10\). It then exhausts every normalized full-rank multiplicity vector through effective length \(8\) and verifies the sharpness statement. Successful replay prints `VERIFY_OK`.

## Relationship to prior work

Wood studies failures of MacWilliams duality for weights on finite fields and uses dimension-\(2\) multiplicity-function constructions. For the Euclidean weight on \(\mathbb F_5\), Example 9.1 gives an explicit length-\(18\) pair with equal primal Euclidean-weight enumerators whose duals differ at Euclidean weight \(2\); it also gives a length-\(30\) pair. The present result supplies a smaller explicit witness for exactly that low-dual-weight mechanism and proves the length-\(9\) threshold within dimension \(2\).

Related work on Lee and Euclidean weights studies extension theorems and alternative refined partitions that restore MacWilliams-type identities. Those results do not give the length-\(9\) pair or the dimension-\(2\), dual-weight-\(2\) minimality statement above.

Focused searches using the exact Euclidean weight, \(\mathbb F_5\), equal primal enumerators, dual Euclidean weight \(2\), length \(9\), multiplicity functions, and the source identifier found no prior statement implying this result. The source itself contains no length-\(9\) or shortest-witness claim.

## Limitations

The minimality theorem is deliberately restricted to effective dimension-\(2\) codes and discrepancy in the coefficient \(A_2\). It does not rule out a shorter counterexample in another dimension or a shorter dimension-\(2\) pair whose dual enumerators first differ at a Euclidean weight greater than \(2\).

The exhaustive cutoff is finite and exact, but the originality conclusion remains literature-dependent; an unindexed computation could contain an equivalent pair. No classification of all length-\(9\) witness pairs is claimed.

## References

1. Jay A. Wood, *Weights on finite fields and failures of the MacWilliams identities*, arXiv:2601.02608v1, first public version 5 January 2026.
2. H. Langevin and J. A. Wood, *The extension problem for Lee and Euclidean weight codes*, Designs, Codes and Cryptography 82 (2017), 329--345.
3. J. Tang, C. Zhu, and X. Kai, *The existence of MacWilliams-type identities for the Lee and Euclidean weight enumerators for linear codes over integer residue rings*, Linear Algebra and its Applications 516 (2017), 147--159.
