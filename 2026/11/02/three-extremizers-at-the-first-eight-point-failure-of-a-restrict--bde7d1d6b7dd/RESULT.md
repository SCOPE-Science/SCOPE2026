# Three extremizers at the first eight-point failure of a restricted-sumset bound

## Finding
For an integer \(L\in\{7,8,\ldots,16\}\), let \(A\subseteq\{0,1,\ldots,L\}\) have exactly eight distinct elements, contain \(0\) and \(L\), and satisfy \(\gcd(A)=1\). Define
\[
4^{\wedge}A=\{a_1+a_2+a_3+a_4:a_i\in A\text{ pairwise distinct}\}.
\]
Then the exact minimum over all such \(A\) is
\[
\min_A|4^{\wedge}A|=\begin{cases}L+10,&7\le L\le15,\\25,&L=16.\end{cases}
\]
At \(L=16\), equality holds **if and only if** \(A\) is one of the following three sets:
\[
\begin{aligned}
A_1&=\{0,1,2,3,13,14,15,16\},\\
A_2&=\{0,1,5,6,10,11,15,16\},\\
A_3&=\{0,3,6,7,9,10,13,16\}.
\end{aligned}
\]
Thus \(L=16\) is the *first* diameter for which the recently proved lower bound for at least nine elements fails when formally extended to eight elements with four distinct summands. The three extremizers are distinct even after reflection: each individually satisfies \(16-A_i=A_i\).

## Assumptions and scope
The ambient group is the integers, with no modular reduction. The normalization is \(\min A=0\), \(\max A=L\), \(|A|=8\), and \(\gcd(A)=1\); this removes translation and nontrivial common dilation. The result concerns only \(7\le L\le16\) and only sums of four **distinct** members, not unrestricted or signed sums. Finite exact enumeration is a complete proof because the domain is explicitly finite.

## Proof
**Enumeration lemma.** For fixed \(L\ge7\), every normalized candidate is uniquely
\[
A=\{0,b_1,b_2,b_3,b_4,b_5,b_6,L\},\qquad1\le b_1<\cdots<b_6<L.
\]
Thus there are exactly \(\binom{L-1}{6}\) candidates before the primitive-set test. Evaluate \(\gcd(L,b_1,\ldots,b_6)\), discarding a candidate unless it equals one. The following two *independent, exact* descriptions of the restricted four-sum support agree on every remaining candidate:

1. Enumerate each of the \(\binom84=70\) four-element subsets of \(A\), sum its elements, and take the resulting set's cardinality.
2. Form \(\prod_{a\in A}(1+t z^a)\). Its coefficient of \(t^4\) is a nonnegative integer polynomial whose support is exactly \(4^{\wedge}A\). The attached executable computes this support using integer bitsets and the recurrence \(D_j\leftarrow D_j\,\mathbin{\mathrm{OR}}\,(D_{j-1}\ll a)\), for \(j=4,3,2,1\) as successive \(a\in A\) are processed. Initial supports are \(D_0=\{0\}\), \(D_j=\varnothing\) for \(1\le j\le4\); descending updates prevent reusing any element.

The completely bounded sweep of all \(L=7,\ldots,16\) gives the following exact minimum and number of minimizing primitive candidates:

| \(L\) | Minimum \(|4^{\wedge}A|\) | Number of minimizers |
|---:|---:|---:|
| 7 | 17 | 1 |
| 8 | 18 | 2 |
| 9 | 19 | 3 |
| 10 | 20 | 4 |
| 11 | 21 | 5 |
| 12 | 22 | 6 |
| 13 | 23 | 7 |
| 14 | 24 | 8 |
| 15 | 25 | 12 |
| 16 | 25 | 3 |

These numbers are finite exact results of the exhaustive, fully specified algorithm in `verify.py`, not statistical inferences. At \(L=16\), exactly \(\binom{15}{6}=5005\) normalized candidates occur and precisely seven are imprimitive (all six interior elements are even), leaving \(4998\). The histogram's lowest terms are three candidates of size \(25\) and ten of size \(26\). The exhaustive equality list is exactly \(A_1,A_2,A_3\); the code asserts set equality rather than checking only their number.

For a direct independent upper-bound explanation when \(7\le L\le15\), take \(A=\{0,1,\ldots,6,L\}\). Its restricted four-sumset is the union of intervals \([6,18]\cup[L+3,L+15]\), which overlap or abut in this range and therefore have \(L+10\) elements. For \(L=16\), the three displayed candidates each have exactly \(25\) sums, as verified by direct evaluation; they are primitive. Consequently the exact minima and the complete equality classification follow.

## Verification
Run `python3 verify.py` with a standard Python 3 interpreter; no third-party modules, input files, databases, random seeds, or external services are needed. The program tests every candidate at each diameter, compares the direct-combination and generating-polynomial supports exactly, and asserts all ten minima and the complete three-member equality list at diameter sixteen. The execution printed `VERIFY_OK`, with \(5005\) normalized candidates, \(4998\) primitive candidates and three extremizers at diameter sixteen. All comparisons use arbitrary-precision integer arithmetic. There is no timeout-based exclusion.

## Relationship to prior work
Yujie Wang's *A sharp lower bound for h-fold restricted sumsets of integers* (first posted 2026-10-18, arXiv:2610.25073v1), Theorem 1.8, gives \(|4^{\wedge}A|\ge10+\min(L,16)\) **when \(|A|\ge9\)** by the general formula. Wang explicitly gives the eight-element set \(A_1\) at \(L=16\) with \(25\) sums, proving the cardinality hypothesis cannot be reduced to eight. The source does not state the first-failure minimum and complete equality classification: in particular it does not identify \(A_2\) or \(A_3\) as the other sharp configurations. The previously known existence witness \(A_1\) is therefore **not** claimed as original.

Manna, Mohan, and Pandey's *Extended inverse results for restricted h-fold sumset in integers* (arXiv:2505.07415) classifies certain low-cardinality cases; its four-fold theorems require much larger \(k\) (at least twelve, or higher) and involve cardinalities close to \(4k-16\), not this eight-element boundary. Mohan and Pandey's 2024 inverse work similarly addresses low-cardinality extremizers with different parameter thresholds. None of the statements inspected supplies the complete three-set classification at \((k,h,L)=(8,4,16)\). This comparison does not assert that an unindexed or implicit earlier derivation is impossible.

## Limitations
This is an exact **finite** boundary classification at the first obstructing diameter, not a general theorem for eight-element sets of unrestricted diameter. The original paper already supplies one of the three minimizers and the failure of its broader bound at that parameter. The new information is the exact minimum as the diameter first reaches sixteen and the exhaustive classification of all sharp sets there. The proof is an independently runnable finite enumeration, not a conceptual parameter-free inverse theorem. Earlier implicit equivalent coverage remains a priority risk; no independent audit has been performed.

## References
1. Yujie Wang, *A sharp lower bound for h-fold restricted sumsets of integers*, arXiv:2610.25073v1 (2026-10-18), https://arxiv.org/html/2610.25073v1.
2. Debyani Manna, Mohan and Ram Krishna Pandey, *Extended inverse results for restricted h-fold sumset in integers*, arXiv:2505.07415 (2025), https://arxiv.org/pdf/2505.07415.
3. Mohan and Ram Krishna Pandey, *Extended inverse theorems for restricted sumset in integers*, Bulletin of the Korean Mathematical Society 61 (2024), 1339–1367, doi:10.4134/BKMS.b230631.
