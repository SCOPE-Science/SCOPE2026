# Review: Exact \(k\)-avoiding thresholds of the Wielandt automata

## Correctness
**PASS.** The claim is reduced to a complete inverse-action analysis. For \(W_n\), \(c^{-1}\) differs from \(b^{-1}\) only at state \(0\); this gives an exact criterion for a unit cardinality drop. The normalization argument is inclusion-safe: an enlarging inverse \(c\)-step may be replaced by the inverse \(b\)-step producing a subset, and later inverse actions preserve inclusion. Hence a shortest avoidance path can be taken to have exactly \(k\) deleting \(c\)-steps. The boundary cost and update are then exact, forcing cost \(n+(k-1)(n-1)\) for \(B_{n,k}\), while every other target admits \(k\) deletions costing at most \(n-1\) each.

The explicit witness is replayed directly, and exact power-automaton breadth-first search independently checks all targets for every \(3\le n\le11\). Finite checks are supporting evidence only; the proof covers all \(n\ge3\).

Risk: the main correctness risk is an orientation error between forward words and inverse blocks. It was addressed both algebraically and by direct witness replay across the finite range. No unproved computational extrapolation remains in the theorem.

## Originality
**PASS.** Direct statement/implication comparisons were made under avoiding, included-reachability, total-extension, preimage, subset-reachability, and exact-formula terminology. The 2010 and 2014 Wielandt sources prove reset thresholds, not prescribed-subset avoiding thresholds. The 2016 extension paper treats different automata. The 2021 avoiding-threshold paper defines the invariant and gives general results but contains no Wielandt occurrence. Volkov's survey treats \(W_n\) and avoidability separately without the claimed all-\(k\) formula. The closest published published-finding corpus item proves the analogous exact \(kn\) profile for the Černý family, which does not logically cover \(W_n\).

Residual risk: an older unindexed paper on subset reachability or total extension may contain an equivalent \(W_n\) distance formula without modern avoiding-threshold terminology. The inspected extension and 1-contracting literature lowers this risk but cannot eliminate it absolutely.

## Value
**PASS.** The \(k\)-avoiding threshold is an established synchronization invariant used in compression methods, and the Wielandt automata are a canonical slowly synchronizing family tied to extremal primitive digraphs. Determining the entire profile \(k(n-1)+1\), not just one small parameter, identifies a simple but nontrivial geometry of the hardest forbidden sets and contrasts sharply with the related Černý profile \(kn\). The unique-maximizer statement and rigid boundary proof add structural information beyond a numerical computation.

The result is not a routine table extension: it is uniform in both \(n\) and \(k\), and its proof isolates the mechanism responsible for every extremal target. Its value is nevertheless scoped to this classical family; no general upper bound for arbitrary synchronizing automata is claimed.

## Closest literature and limitations
The closest family source is Ananichev–Gusev–Volkov (2010), which defines \(W_n\) and proves its reset length. Gusev–Pribavkina (2014) generalizes the family by cycle lengths. The closest invariant source is Ferens–Szykuła–Vorel (2021). The closest exact published comparison is the published-finding corpus record on Černý \(k\)-avoiding thresholds. Equivalent extension terminology was checked against Kisielewicz–Szykuła (2016), Don (2016), and Volkov's survey.

Same-model review: passed. Independent audit: not yet performed.
