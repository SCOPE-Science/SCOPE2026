# Exact binary two-deletion covering numbers through length eight

## Finding

Let \(\Sigma=\{0,1\}\). For integers \(n\ge 2\), let \(D_2(n)\) be the minimum number of length-\(n\) words required so that **every** binary word of length \(n-2\) is a scattered subsequence of at least one selected word. Then the complete initial profile is
\[
\bigl(D_2(2),D_2(3),D_2(4),D_2(5),D_2(6),D_2(7),D_2(8)\bigr)
=(1,1,1,2,3,4,7).
\]
In particular, precisely seven length-eight words are necessary and sufficient to cover all \(64\) length-six words under two arbitrary deletions. This is the usual **deletion covering** problem, not deletion error correction, insertion covering, or contiguous-burst deletion covering.

## Assumptions and scope

For \(w\in\Sigma^n\), put
\[
\mathcal D_2(w)=\{w_{i_1}\cdots w_{i_{n-2}}:1\le i_1<\cdots<i_{n-2}\le n\}.
\]
Repeated outcomes are counted only once. A covering set \(\mathcal C\subseteq\Sigma^n\) satisfies \(\bigcup_{w\in\mathcal C}\mathcal D_2(w)=\Sigma^{n-2}\). All claims concern the labeled binary alphabet, exactly two deletions, and integer lengths \(2\le n\le8\). For \(n=2\), the only output is the empty word.

## Proof

**Upper bounds.** The following complete word sets are valid covers; each is verified by direct enumeration of all deleted-coordinate pairs in `verify.py`:

| \(n\) | Cover \(\mathcal C_n\) | Size |
|---|---|---:|
| 2 | `00` | 1 |
| 3 | `110` | 1 |
| 4 | `1010` | 1 |
| 5 | `01010`, `10101` | 2 |
| 6 | `001001`, `011011`, `101010` | 3 |
| 7 | `0001010`, `0111010`, `1010010`, `1010111` | 4 |
| 8 | `00010101`, `01010000`, `01011010`, `01101111`, `10011001`, `10100101`, `11101010` | 7 |

**Lower bounds at lengths 2–5.** Every cover is nonempty. At \(n=5\), a single length-five word cannot contain both `000` and `111` as subsequences: together they demand at least six positions. Hence \(D_2(5)\ge2\).

**Weighted-shadow lemma.** Fix a length \(n\in\{6,7,8\}\). For a nonnegative integer weight function \(\lambda:\Sigma^{n-2}\to\mathbb Z_{\ge0}\), define \(T=\sum_{u\in\Sigma^{n-2}}\lambda(u)\) and \(B=\max_{w\in\Sigma^n}\sum_{u\in\mathcal D_2(w)}\lambda(u)\). Every covering set has at least \(\lceil T/B\rceil\) words, because
\[
T\le\sum_{w\in\mathcal C}\sum_{u\in\mathcal D_2(w)}\lambda(u)\le |\mathcal C|B.
\]
This inequality holds regardless of overlaps among the deletion shadows.

**Exact dual certificates.** Assign the stated weight to each *distinct* member of the orbit of the listed representative under word reversal and bit complementation; assign zero to all unlisted orbits. This fully defines three integer weight functions:

| \(n\) | Representatives with integer weights | \(T\) | \(B\) |
|---|---|---:|---:|
| 6 | `0000`:1, `0001`:1, `0011`:1 | 8 | 3 |
| 7 | `00000`:1, `00001`:1, `00011`:1 | 10 | 3 |
| 8 | `000000`:5, `000001`:2, `000011`:3, `000100`:2, `000111`:4, `001100`:1, `001101`:1, `001110`:2, `010001`:1, `010110`:1, `011001`:2, `011110`:1 | 74 | 12 |

The orbit specifications are disjoint. The finite claims \(T=(8,10,74)\) and \(B=(3,3,12)\) are established by **exhausting every source word** (64, 128, and 256 words respectively) and listing its complete *set* of two-deletion descendants. This is exhaustive finite verification, not a sample or heuristic search. `verify.py` implements the precise definitions using only the Python standard library and additionally compares every source–target pair against a separately coded greedy subsequence test.

The weighted-shadow lemma gives
\[
D_2(6)\ge\lceil8/3\rceil=3,\quad
D_2(7)\ge\lceil10/3\rceil=4,\quad
D_2(8)\ge\lceil74/12\rceil=7.
\]
Together with the displayed covers, these are equalities. The seven-entry profile follows.

## Verification

Run `python verify.py` from the directory containing the embedded files; the recorded output appears in `verification_output.txt`. The exact checker reconstructs every two-deletion set independently of any optimization solver; tests each cover against **all** targets; constructs the reversal/complement orbit weights; checks all \(2^n\) candidate source words for each certificate; verifies both dual totals and maxima; and cross-checks all 21,844 source/target incidence decisions by greedy matching. All operations are integers, sets, and direct string comparisons; there are no tolerances or randomly sampled cases. The program terminates with `ALL_EXACT_CHECKS_PASSED`.

## Relationship to prior work

Lenz, Rashtchian, Siegel and Yaakobi (arXiv:1911.09944, first public November 22, 2019; IEEE Transactions on Information Theory 2021) define insertion and deletion covering and establish general bounds, including asymptotic multiple-deletion covering results (Theorem 14). Their bounds do not provide the exact seven-term binary radius-two profile.

Xie, Sun and Ge (arXiv:2606.15379, June 13, 2026) show, among other results, that the elementary deletion-covering lower bound is asymptotically sharp when the alphabet grows with fixed length and radius (Theorem V.1), and study a different two-**burst**-deletion covering problem (Section VI). Their Section V hypergraph method does not give the small fixed-binary exact values here. The elementary bound at \((q,n,R)=(2,8,2)\) is only \(D_2(8)\ge\lceil64/28\rceil=3\), whereas the orbit-weight certificate proves seven.

The related exact ternary length-five **single**-deletion covering value concerns a different alphabet, radius, and target dimension and does not imply these results. The contribution is the complete initial finite profile and the short explicit integral lower certificate, not the general covering definitions or asymptotic existence theorems.

## Limitations

This is a finite-length result. No value at \(n\ge9\), nonbinary alphabet, or other deletion radius is claimed. Optimal covering families have not been classified. The verification is exhaustive for the stated finite domains but is not an independent mathematical audit, and publication-priority uncertainty remains for unindexed earlier tables or equivalent formulations.

## References

1. A. Lenz, C. Rashtchian, P. H. Siegel, E. Yaakobi, *Covering Codes using Insertions or Deletions*, arXiv:1911.09944 (first submitted November 22, 2019), https://arxiv.org/abs/1911.09944. Published in IEEE Transactions on Information Theory 67(6), 3376–3388 (2021).
2. C. Xie, Y. Sun, G. Ge, *New bounds for covering codes under insertions or deletions*, arXiv:2606.15379 (first submitted June 13, 2026), https://arxiv.org/abs/2606.15379.
