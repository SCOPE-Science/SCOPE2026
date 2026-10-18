# Mathematical review

## Correctness — PASS
The lower length bound is forced by \(k\) occurrences of each of three letters. The arch characterization at equality gives exactly \(k\) permutation triples at one of three phases. Pair intersections have size \(3\cdot2^k\), triple intersection consists of the six permutations repeated cyclically, and inclusion-exclusion gives the labeled formula. A fixed-point argument for rotations and Burnside's lemma yield the necklace formula; Möbius inversion yields primitive classes. The checker confirms the phase, labeled, necklace, and primitive counts by exhaustive enumeration through \(k=4\), with an independent pattern-by-pattern subsequence test through \(k=3\). Infinite validity comes from the proof, not these finite observations.

## Originality — PASS, subject to literature risk
Barker et al. (arXiv:2003.04629v1) establish circular universality and arch-based characterization. Fleischmann et al. (arXiv:2104.09063v1) study remainder chains and repetitions. Adamson (arXiv:2304.04583v1) develops linear fixed-length counting algorithms. Their relevant accessible primary sections were compared by claim implication, not just title: none inspected directly supplies the ternary cyclic phase intersections, enumeration, rotation fixed-point classification, or primitive count. Related earlier result on *binary odd-length* circular maximizers does not imply these ternary formulas. Unindexed equivalent results remain a risk; no claim of uniqueness from search absence is made.

## Mathematical value — PASS
This is the first nontrivial fixed-alphabet cyclic overlap problem beyond the binary minimum-length case: three phase partitions interact, while generic linear counting does not account for their overlaps. The result completely resolves an infinite natural family at the sharp shortest length and determines its labeled, necklace, primitive, and phase-multiplicity spectra, providing structural information useful for cyclic universality enumeration.

## Limits
No assertion is made for longer lengths, larger alphabets, dihedral equivalence, or alphabet-relabeling quotients. Computations stop at \(k=4\). The literature review cannot rule out unindexed equivalent formulations. No independent audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
