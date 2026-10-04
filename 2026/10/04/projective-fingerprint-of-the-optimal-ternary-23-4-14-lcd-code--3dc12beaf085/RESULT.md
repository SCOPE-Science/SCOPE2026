# Projective fingerprint of the optimal ternary \([23,4,14]\) LCD code
## Finding

For the explicit ternary distance-optimal LCD code \(C_{3,1}\) with parameters \([23,4,14]\) published by An, Hong, Kim, and Lim, the \(23\) generator columns are pairwise nonproportional and hence define a projective point set \(S\subset\mathrm{PG}(3,3)\). Its complete Hamming weight enumerator is
\[
W_C(z)=1+18z^{14}+28z^{15}+22z^{16}+6z^{17}+4z^{18}+2z^{22}.
\]
Among the \(130\) projective lines, exactly
\[
10,\ 11,\ 43,\ 62,\ 4
\]
meet \(S\) in \(0,1,2,3,4\) points respectively. Moreover,
\[
\operatorname{Stab}_{\mathrm{PGL}(4,3)}(S)\cong C_2\times C_2.
\]

## Assumptions and scope

The code \(C_{3,1}\) is the specific code whose \(4\times23\) generator matrix is printed in the cited 2026 paper and in its public dataset. Arithmetic is over \(\mathbb F_3\). A generator column represents its one-dimensional projective span; because no two columns are proportional, the code is projective and gives a \(23\)-point set \(S\) in \(\mathrm{PG}(3,3)\).

The projective stabilizer means the subgroup of \(\mathrm{PGL}(4,3)\) preserving \(S\) setwise. The line spectrum counts all \(130\) projective lines of \(\mathrm{PG}(3,3)\), not only lines meeting \(S\).

## Proof

Direct row reduction gives \(\operatorname{rank}(G)=4\). The Euclidean Gram matrix is
\[
GG^{T}=
\begin{pmatrix}
1&1&0&2\\
1&2&1&1\\
0&1&0&0\\
2&1&0&0
\end{pmatrix},
\]
whose determinant is \(1\) in \(\mathbb F_3\); hence the reconstructed code is LCD.

Enumerating all \(3^4=81\) linear combinations of the rows gives
\[
A_0=1,\quad A_{14}=18,\quad A_{15}=28,\quad A_{16}=22,\quad
A_{17}=6,\quad A_{18}=4,\quad A_{22}=2,
\]
with all other coefficients zero. Thus the minimum distance is \(14\).

Normalize every nonzero vector of \(\mathbb F_3^4\) by scaling its first nonzero coordinate to \(1\). The \(23\) columns normalize to \(23\) distinct points. Exhausting all two-dimensional vector subspaces gives the \(130\) projective lines, whose intersection spectrum with \(S\) is
\[
(N_0,N_1,N_2,N_3,N_4)=(10,11,43,62,4).
\]
The incidence checks
\[
\sum_jN_j=130,\qquad
\sum_jjN_j=23\cdot13,\qquad
\sum_j\binom{j}{2}N_j=\binom{23}{2}
\]
hold exactly.

For the stabilizer, color each pair of points of \(S\) by the number \(2,3,\) or \(4\) of points of \(S\) on their joining projective line. Every projective linear stabilizer preserves this colored complete graph. Exact backtracking gives four color-preserving automorphisms. Each is independently lifted to an explicit invertible \(4\times4\) matrix over \(\mathbb F_3\) and checked on all \(23\) projective columns. Thus the projective stabilizer has exactly four elements. Its three nonidentity elements all have order \(2\), so it is the Klein four group.

As a separate check, the \(40\) projective planes meet \(S\) in \(1,5,6,7,8,9\) points with multiplicities \(1,2,3,11,14,9\). Every projective plane corresponds to two nonzero scalar multiples of a linear functional, reproducing the weight enumerator above.

## Verification

`artifacts/verify.py` uses only the Python standard library. It reconstructs the printed generator matrix, verifies rank and the LCD Gram determinant, enumerates all \(81\) codewords, constructs all \(40\) projective points and all \(130\) projective lines of \(\mathrm{PG}(3,3)\), and recomputes the line and hyperplane spectra.

For the stabilizer, the verifier builds the line-intersection-colored complete graph on the \(23\) code points and exhaustively enumerates its color-preserving automorphisms by exact backtracking. It then checks that every surviving automorphism is induced by the explicit projective matrix stored in `artifacts/certificate.json`. Successful replay ends with `VERIFY_OK`.

## Relationship to prior work

An, Hong, Kim, and Lim introduced the shortest-LCD-embedding construction and reported \(C_{3,1}\) as a new distance-optimal ternary \([23,4,14]\) LCD code. Their paper gives the generator matrix and minimum distance and reports many inequivalent codes with the same new parameters, but it does not give a weight enumerator, projective line spectrum, or automorphism group for the displayed representative.

The earlier small-field LCD work of Li, Shi, and Liu gives the pre-existing bound
\[
13\le d_3(23,4)\le14
\]
and constructions for neighboring parameters. It does not contain the later distance-\(14\) representative and therefore does not determine its projective fingerprint.

The present invariants are useful for comparing inequivalent optimal representatives: the weight enumerator records the complete hyperplane spectrum, while the line spectrum and stabilizer add lower-dimensional incidence and symmetry information.

## Limitations

The result concerns the displayed representative \(C_{3,1}\), not all ternary distance-optimal LCD \([23,4,14]\) codes. The line spectrum and projective stabilizer do not by themselves form a complete equivalence invariant. No claim is made that every inequivalent code reported by the source has the same weight enumerator or symmetry. Literature searches covered exact parameters, the numerical weight spectrum, projective/secant terminology, and automorphism-group terminology; an equivalent computation in an unindexed source remains a residual risk.

## References

1. Junmin An, Ji-Hoon Hong, Jon-Lark Kim, and Haeun Lim, *Shortest LCD embeddings of binary, ternary and quaternary linear codes*, arXiv:2601.20600v1, first public version 2026-01-28; Advances in Mathematics of Communications 25 (2026), 192-202, DOI 10.3934/amc.2026048.
2. Junmin An, *Shortest LCD embeddings of binary, ternary and quaternary linear codes with dataset*, public data repository accompanying the paper.
3. Shitao Li, Minjia Shi, and Huizhou Liu, *Several constructions of optimal LCD codes over small finite fields*, Cryptography and Communications 16 (2024), 779-800.
