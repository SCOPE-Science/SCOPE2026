# Independent mathematical audit

## correctness

PASS

Original proof: FAIL at RESULT.md line 51, not a refutation of the claimed bound. The frozen argument does not exhibit an LCL whose decoding enforces collisions between markers on different branches. A binary common-base rule of the referenced type is insufficient: on the positive shifts of X={(i,j):i,j≥0}∪{(i,j):i≥1,j≥−1}, p=(0,0) and q=(1,−1) have a common future via different generators but no common predecessor. Mark p,q and the lattice (2k,2l+1), k≥1,l≥0; every point reaches a lattice marker in at most three moves inside the radius-two forward box, and the only close marker pair is p,q, unseen from a common base. Thus even actual binary feasible local patterns need not be globally forward-independent. Repaired proof: PASS. An explicit clopen greedy maximal box net in every free continuous group action gives the centered budget 2nr; its clopen construction uses a countable clopen independent cover, with the final complement the open union of nonzero neighbor translates. Each group point has at most one predecessor marker at offset α∈[0,r]^n since two would be box-adjacent. Label each point by that offset or an unmatched symbol. A forward-window predicate requires a zero label within the budget and requires every zero-labeled marker to propagate its offset to its future box. The group labeling is continuous since its offset classes are disjoint clopen translates. Shinko–Weilacher–Yu Theorems 1.7/3.24 and Proposition 3.22 apply to this explicit finite-alphabet M-LCL, with Γ=Z^n, M=N^n and a free bounded-to-one Borel action on the free part; the free part is Borel and forward invariant. A collision forces equal offsets because the shared future has one label; if the offsets are coordinatewise disjoint, equality forces both zero and the two bases to coincide. The proof works for n=1 and r=1 as well as larger positive integers, and for noninjective actions. The revised proof establishes the full original bound, not just the group case.

## originality

PASS

The strongest same-hypothesis comparison, Gao–Hu–Zou Theorem 3.1, states 2n²r, with the ℓ¹-net estimate in Proposition 3.4, not the linear 2nr bound. The originating LOCAL transfer supports arbitrary finite-alphabet problems but does not state this bound or the offset propagation for colliding markers. Both the conflict-box centering and a correct forward encoding are needed to obtain the repaired conclusion under the original noninvertible hypotheses. Catalogue searches for the exact theorem, coordinate-box aliases, quantitative improvement, and the repaired shared-future offset encoding returned no material overlapping statement in their bounded results. The positive distinction is based on inspecting the closest primary results, not on the misses alone.

## value

PASS

The repaired theorem reduces the dependence on the number of commuting generators from quadratic to linear at the same separation scale and under the same Borel hypotheses, an unbounded improvement factor when dimension varies. Centering by the coordinate conflict box accounts quantitatively for the gain, and carrying offset labels supplies a reusable way of enforcing an exclusion condition at a common future without assuming a common past. The result is not just a group-model exercise because the repair proves global marker independence after the monoid transfer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
