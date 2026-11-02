# Scientific review

## Correctness
**PASS.** The theorem uses the explicit integer thresholds \(r_n=\lceil\phi(n-1)\rceil\) and \(R_n=\lceil\phi n\rceil\). Its local unassisted/rescuable dichotomy accounts for every arrangement of ordinary seeds and the bridge seed, including the high-threshold \(R_n=n\) gateway obstruction. The global product formula excludes precisely the mutually blocked case. Algebraic expansion yields the coefficientwise gain/neutral/loss classification and the exact minimum-seed formula. Direct exhaustive adjacency-based iteration in `verify.py` checks \(2{,}211\) exact finite assertions on \(16\) ordered community-size pairs and \(46\) rational thresholds. Infinite scope follows from the proof, not enumeration.

## Originality
**PASS within searched evidence; historical priority remains provisional.** The 2012 dynamic-monopoly primary paper gives general threshold bounds and terminology, not the exact two-clique seed enumeration. The 2013 multiple-initiator primary paper studies community contagion and numerical tipping, not the bridge-addition polynomial. The 2017 collective-influence study optimizes seeds on broad networks using approximate cavity paths rather than deriving all successful seed sets of a finite bridge barbell. The published zero-forcing barbell polynomial concerns a distinct color-change process and does not imply the result. Earlier related published findings and semantic mathematical-record results were compared for structural overlap. Residual risk includes an unindexed equivalent result or a different formulation in graph contagion literature.

## Value
**PASS.** A lone cross-community tie can promote consensus, be inert, or obstruct it because it simultaneously exposes a gateway to influence and raises its degree-normalized adoption requirement. The exact all-seed-size polynomial resolves this tradeoff in a canonical two-community network and distinguishes loss of one viable seed configuration from the gain of a full class of configurations; a sharp minimum-seed consequence follows. This makes exact seeding reliability and the structural effects of one bridge evaluable at any finite community size, beyond a numerical instance. It does not assert practical predictions for incomplete social networks.

## Closest literature and scope
See the four comparisons and source inspections in `AUDIT.json`, and the formal definitions, countervailing effects, examples and limitations in `RESULT.md`. A same-rule earlier single-seed one-edge inhibition result on connected graphs addresses a different extremal question and does not determine the polynomial here.

Self-review: passed. Independent audit: not yet performed.
