# Exact three-survivor multiset deletion codes over arbitrary alphabets

## Finding

Let \(S_q(n,t)\) be the largest cardinality of a code of \(n\)-element multisets over \(q\) labeled symbols that corrects up to \(t\) deletions. For every integer \(q\ge2\) and every integer \(n\ge q+2\),

\[
S_q(n,n-3)=
\begin{cases}
q+1,&q+2\le n\le2q,\\
q,&n\ge2q+1.
\end{cases}
\]

The first threshold is sharp: at \(n=q+1\) there exists a code of at least \(q+2\) multisets. Moreover every maximum code in the stated range has exactly \(q\) codewords containing a symbol with multiplicity at least three, and each alphabet symbol is the unique such high-multiplicity symbol of precisely one of these codewords. For \(q+2\le n\le2q\), one additional codeword occurs, with all multiplicities at most two. For \(n\ge2q+1\), there is no additional codeword.

## Assumptions and scope

An input multiset is represented by its multiplicity vector \(x=(x_1,\ldots,x_q)\in\mathbb Z_{\ge0}^{q}\) with \(\sum_i x_i=n\). A deletion reduces one positive multiplicity by one. Codewords are distinct vectors, and the receiver must reconstruct the transmitted vector following any sequence of at most \(n-3\) deletions. Write \(I(x,y)=\sum_i\min(x_i,y_i)\) for multiplicity intersection. The domain \(q\ge2,n\ge q+2\) ensures that the deletion budget \(n-3\) is nonnegative.

## Proof

**1. Confusability criterion.** Two size-\(n\) multisets have a common \(3\)-element submultiset if and only if \(I(x,y)\ge3\). Therefore a code corrects \(n-3\) deletions if and only if \(I(x,y)\le2\) for every distinct pair \(x,y\) in the code. Indeed any output after at most \(n-3\) deletions has size at least three, so a shared output contains a shared three-element submultiset. Conversely a shared three-element submultiset is obtained after exactly \(n-3\) deletions from each input.

**2. Heavy-word bound.** Call \(x\) *heavy* if at least one coordinate is at least three, and *light* otherwise. For each heavy codeword choose any coordinate \(i\) with \(x_i\ge3\). Two heavy codewords cannot choose the same coordinate, because their intersection would be at least three. Thus the number of heavy codewords is at most \(q\). In fact their sets of high-multiplicity coordinates are pairwise disjoint.

**3. Light-word bound.** For light vectors \(x,y\), each coordinate is between zero and two. The elementary inequality \(\min(x_i,y_i)\ge x_i+y_i-2\) gives

\[
I(x,y)\ge 2n-2q\ge4
\]

when \(n\ge q+2\). Consequently no code in the stated range contains two light codewords. This gives the upper bound \(q+1\). If \(n\ge2q+1\), a light vector of sum \(n\) cannot exist (its sum is at most \(2q\)), so the upper bound improves to \(q\).

**4. Optimal constructions.** For every \(q\ge2\), the \(q\) pure vectors \(n e_i\), where \(e_i\) is the \(i\)-th standard basis vector, form a valid code: their pairwise intersections are zero. When \(q+2\le n\le2q\), add the light vector having exactly \(n-q\) coordinates equal to two and the remaining \(2q-n\) coordinates equal to one. Its sum is \(n\); its intersection with each \(n e_i\) is at most two. This constructs \(q+1\) codewords. For \(n\ge2q+1\), the pure vectors give \(q\) codewords and already meet the upper bound.

**5. Structure of all equality cases.** In the first regime, equality forces exactly one light and \(q\) heavy codewords. In the second, equality forces \(q\) heavy codewords and no light. For \(q\) heavy words with pairwise-disjoint nonempty sets of high-multiplicity coordinates in a \(q\)-symbol alphabet, every such set must be a singleton and these singleton coordinates must cover all symbols. This proves the asserted heavy-coordinate structure without classifying all remaining small coordinates.

**6. Sharpness of the lower domain boundary.** Put \(n=q+1\). In addition to the \(q\) pure vectors, take two distinct light vectors as follows. For odd \(q=2r+1\), use \((2,2^{[r]},0^{[r]})\) and \((2,0^{[r]},2^{[r]})\). For even \(q=2r+2\), use \((2,1,2^{[r]},0^{[r]})\) and \((1,2,0^{[r]},2^{[r]})\). Here \(a^{[r]}\) denotes \(r\) consecutive entries equal to \(a\), not a power. In either case the vectors each sum to \(q+1\), have entries at most two, and have mutual intersection exactly two. Together with the pure vectors, they form a \((q+2)\)-word code, so the \(q+1\) upper bound cannot extend to \(n=q+1\).

## Verification

Two standalone programs accompany this result. `verify_small.py` enumerates all multiplicity vectors, builds the exact pairwise compatibility graph using the intersection criterion, and computes exact maximum cliques independently of the proof for all \(q\in\{2,3,4,5\}\) and \(q+2\le n\le2q+1\), additionally checking the first excluded length \(n=q+1\). Its output records all 18 checked parameter pairs, including \(S_5(7,4)=6\) and \(S_5(11,8)=5\). `verify_witnesses.py` independently constructs and pairwise checks all sharp constructions and boundary witnesses for \(2\le q\le40\), covering 897 parameter pairs. Both scripts use Python's standard library; run them with `python3 verify_small.py` and `python3 verify_witnesses.py` in a directory containing the scripts. These are finite corroborations; the all-parameter proof is Steps 1–6.

## Relationship to prior work

Kreindel, Barouch Essayag and Zabokritskiy's January 2026 preprint formalizes this same deletion-channel extremum and, in Proposition 12 of its July 2026 revision, proves \(S_q(n,n-3)\le q+\binom q2\) when \(n\ge q+2\). Its treatment does not give the sharp two-regime formula. The present proof improves that bound to the exact \(q+1\) or \(q\) throughout its entire domain; at \(q=5,n=7\), for example, the prior bound is 15 while the exact value is 6. The binary case and the known isolated ternary and quaternary size profiles are not new and are included as special cases, not independent discoveries. Kovačević and Tan's earlier discrete-simplex framework establishes the appropriate metric and general code bounds, but does not state the uniform formula. The 2026 companion paper studies deletion-ball geometry rather than this exact all-alphabet maximum.

## Limitations

The formula concerns **unordered multisets**, not ordinary ordered strings; it requires three surviving symbols, and \(n\ge q+2\). The heavy-coordinate conclusion is a necessary feature of every optimal code, not a complete classification of all optimal codebooks. An unpublished or unindexed earlier derivation cannot be ruled out; independent mathematical assessment has not been performed.

## References

1. A. Kreindel, I. Barouch Essayag, A. L. Zabokritskiy, *Multiset Deletion Codes: Cyclic Constructions, Bounds, and Exact Results*, arXiv:2601.05636, first made public 2026-01-09, v2 2026-07-13, especially Section 4.4, Proposition 12. https://arxiv.org/html/2601.05636v2
2. M. Kovačević and V. Y. F. Tan, *Codes in the Space of Multisets—Coding for Permutation Channels with Impairments*, arXiv:1612.08837 (2016), especially the channel model and general bounds. https://arxiv.org/abs/1612.08837
3. A. Kreindel, I. Barouch Essayag and A. L. Zabokritskiy, *Polynomial Constructions and Deletion-Ball Geometry for Multiset Deletion Codes*, arXiv:2603.18322 (2026). https://arxiv.org/abs/2603.18322
