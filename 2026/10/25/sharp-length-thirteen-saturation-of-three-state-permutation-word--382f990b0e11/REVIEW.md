# Review of the three-state permutation-equivalence profile

## Correctness — PASS

Every three-state permutation is an affine map on \(\mathbb F_3\). Four choices of letter-sign parameters determine a complete same-length evaluation invariant of one mod-six and three mod-three coordinates. The stated recurrence is derived from the signed-prefix definitions. Two direct exhaustive implementations agree through length thirteen: one iterates the 162-state recurrence, and the other evaluates all words under all 36 pairs of permutations. The 162-row certificate gives an independently replayable witness for each signature at length thirteen. Both letter transitions are bijections of the full signature space, proving stabilization for all higher lengths. No finite-to-infinite inference is assumed without the bijection lemma.

## Originality — PASS within examined evidence

Xu–Regan (2026, arXiv:2610.11098v1, full HTML) studies asymptotic separation bounds and positive identities, not the complete number of three-state indistinguishability classes at each length. Bulatov–Karpova–Shur–Startsev (2017, full PDF, Section 3) gives the shortest \(S_3\) identity, not a complete quotient-growth or saturation theorem. Searches for affine signatures, relatively free \(S_3\) word evaluations, numerical count sequences, and related indexed mathematical records did not identify an equivalent result. Karpova–Shur (2021) is a relevant source with only its abstract inspected: it remains an explicitly acknowledged possible overlap risk, not an asserted negative full-text finding. The affine representation itself is standard and is not claimed as new.

## Mathematical value — PASS

The result resolves the complete length-dependent classification of all binary word behaviors visible to any three-state permutation automaton. Its sharp length-thirteen threshold distinguishes eventual saturation from merely bounding the number of evaluation functions; the exact finite growth sequence and constructive 162-type signature provide concrete benchmarks for the words-separation problem recently sharpened asymptotically. This is a natural quotient of a standard automata-equivalence relation, not an arbitrarily chosen word slice or a small numerical improvement. The contribution does not assert progress on asymptotic separation or larger groups.

## Risks and scope

The exact profile is limited to the binary alphabet and three-state permutation actions. A fully available version of Karpova–Shur (2021), or unindexed work on relatively free groups, might give an equivalent count. Independent checking by a different investigator remains outstanding.

Self-review: passed. Independent audit: not yet performed.
