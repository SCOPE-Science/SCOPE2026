# Independent mathematical audit

## correctness

PASS

The operator factors through the contractive E_d and is determined by its finite matrix on equal-measure atoms; dyadic automorphisms give identical absolute column sums. Prefix-shell multiplicities 2^(d−ℓ−1), entries 2^(−d)(A_ℓ−b_(ℓ+1)2^ℓ) and the diagonal 2^(−d)A_d give the control objective. The two Bellman branches with k≥2 differ by (1−c)(t−1/2) when the preceding value function is a+c|t−1/2|; the update c↦(1−c)/2 preserves c<1. For one remaining step the value from digit 1 is 1 versus t from digit 0, so 1 is forced for every reachable t<1. If the depth is at least two, the first digit forces t=1/2; only at the second digit and d≥3 does a tie occur. Each subsequent strict action maps an interior state to the opposite open half and cannot hit 1/2, proving alternation and excluding every other candidate. The cases d=1,2 have sole optima (1),(1,1). The update for a recovers the stated (known) sharp value. Xoring the initial frequency segment by N shifts it exactly to the selected blocks, and Walsh multiplication is an L¹ isometry, giving the index classification without changing norms. Summing the digit patterns gives the two listed indices. Replay: repaired RESULT.md, or original lines 24–80; checker.py was inspected, not executed. Finite regression tests are not the all-depth proof.

## originality

PASS

The numerical maximum in the frozen result is covered: the Walsh reduction makes it the exact dyadic-block maximum of the Walsh–Paley Lebesgue constants; Dick–Pillichshammer give that expression via the binary van der Corput discrepancy, citing Faure. The repair expressly credits the known value and keeps full equality classification only. The inspected statement supplies one attaining index, not an exclusion of all the others. The repaired strict Bellman comparison proves that exclusion. No priority is asserted for a witnessing digit pattern, the value, or the pointwise norm formula; older full equality results remain a real access risk.

## value

PASS

The binary dyadic filtration and Walsh Lebesgue constants are standard exact endpoint objects. Knowing one high-norm selector and the sharp value does not say whether many distinct scale patterns tie, or which alterations are possible. The all-depth necessity-and-sufficiency theorem answers that structural question: one binary tie, forced alternation among subsequent nonterminal choices, and a forced terminal digit. Through the isometry it also gives a complete optimizing-index classification for the discrepancy/Walsh formulation. This distinct equality question, not the recomputation of the known maximum, justifies retention.

The dated certificate retains the supplied scientific assessment, sources and limitations.
