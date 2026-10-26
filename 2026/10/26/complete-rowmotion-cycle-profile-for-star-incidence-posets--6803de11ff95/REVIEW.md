# Scientific review: complete rowmotion cycle profile for star-incidence posets

## Correctness — PASS
The three transition rules are reconstructed from the minimal-complement definition. Every ideal has exactly one normal form; the two constant-word cycles, the all-three-symbol ternary rotations, and the eight-cycles indexed by complementary nontrivial leaf-subset pairs are disjoint and exhaustive. Counting gives \(2^n+3^n\) ideals and the exact claimed orbit multiplicities for all integers \(n\ge2\). The independent bitmask verifier examines every ideal for \(1\le n\le8\) directly from poset inequalities; this is a finite check, not the reason the unbounded result follows.

## Originality — PASS (with limits)
The closest primary paper is Grinberg–Roby, *Iterative properties of birational rowmotion I* (2016, first public arXiv 2014-02-25): its Propositions 94 and 101–105 give one level orbit and period relations on skeletal posets. Those do not assert or imply the precise number of all nonlevel \(3\)- and \(8\)-cycles proved here. The fuller arXiv preprint Section 10 was checked for additional coverage. Dangwal et al. (2022) covers uniquely rooted trees, unlike either orientation of \(P_n\) when \(n\ge2\). The ideal-count sequence \(2^n+3^n\) is already known as OEIS A007689 and is not claimed as novel. Semantic searches found no directly covering result; unindexed or undiscovered statements remain possible.

## Value — PASS
A graph-incidence family of mixed-orientation trees has its *entire* rowmotion cycle distribution classified in simple closed form for arbitrary size. This identifies nonlevel orbit multiplicities unavailable from the existing general period method, giving a motivated dynamical benchmark beyond one isolated finite experiment.

## Limitations and closest literature
The statement concerns classical rowmotion on this specific graph-incidence family, not all orientations of trees and not birational orbit classification. Computer verification covers \(n\le8\); the proof applies to every \(n\ge2\). Related sources are Grinberg–Roby (2016, arXiv:1402.6178), Striker–Williams (2012, arXiv:1108.1172), Dangwal et al. (2022, *Rowmotion on Rooted Trees*), and OEIS A007689. No independent expert review is claimed.

Self-review: passed. Independent audit: not yet performed.
