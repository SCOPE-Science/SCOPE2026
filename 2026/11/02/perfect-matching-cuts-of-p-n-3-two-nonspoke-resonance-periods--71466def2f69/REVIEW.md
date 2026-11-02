# Scientific review: perfect matching cuts of \(P(n,3)\)

## Correctness — PASS

Every claimed cut is a bipartition for which each cubic vertex has exactly one opposite-colored neighbor. The outer-neighbor equations determine the inner bits, and the complete local nine-bit constraint is exactly equivalent to the remaining inner equations. The de Bruijn shift encodes every cyclic outer word, including wraparound, as a closed walk. The induced recurrent core of its finite 256-state graph has two loops, one 4-cycle, and two 5-cycles, so the infinite-family enumeration follows by closed-walk counting, not extrapolation. The attached `verify.cpp` checks all 512 possible Boolean transitions, the 16-state certificate, and an independent complete vertex-coloring census on 11,182,080 assignments for \(7\le n\le12\). It returned `VERIFY_OK` after compilation and execution.

## Originality — PASS, with a priority risk

The 2021 Le–Telle primary paper defines the exact same cut object and studies complexity and algorithms; their conclusion explicitly raises counting and enumeration as further directions; the 2023 Bonnet–Chakraborty–Duron paper proves hardness on cubic bipartite planar graphs and explains the cycle-union interpretation. Neither inspected paper supplies a numerical cut classification for \(P(n,3)\). Comparisons included the stronger-formulation search (monochromatic cycle partitions), the difference from disconnected perfect matchings, and the nearby jump-two family: even at order eight, the jump-two and jump-three cut counts differ. No equivalent exact result was identified in the examined literature and mathematical research records. This is not proof of publication priority; unindexed work remains possible.

## Mathematical value — PASS

The theorem completely classifies a natural, well-studied cubic graph family for an invariant with difficult general recognition. The nonspoke cuts exist at precisely two independent divisibility periods, and their spoke usage distinguishes geometrically different classes. The simultaneous primitive 4- and 5-period behavior is a substantive structural distinction from the adjacent jump-two family, not a routine parameter substitution. An exact natural finite-state classification is a legitimate combinatorial result without a general-jump theorem.

## Scope and residual limitations

The theorem concerns simple \(P(n,3)\), \(n\ge7\), and perfect matching edge cuts themselves. It neither counts disconnected perfect matchings nor addresses arbitrary generalized Petersen jump parameters. The mathematical proof is supplied with an exhaustive finite-state certificate, but publication priority and independent mathematical validation remain open.

Self-review: passed. Independent audit: not yet performed.
