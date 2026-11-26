# Independent mathematical audit

## correctness

PASS

The full-length Parikh vector fixes the labelled multiplicities. Common renaming therefore reduces completeness to the 22 partitions of eight with all their canonical labelled multiset permutations; the frozen checker generates each recursively, sorts all factor vectors retaining multiplicities, and compares whole fibers. Independently, if S_k sums the Parikh vectors of length k, then for k<=ceil(n/2) position i occurs min(i,n+1-i,k) times. Thus S_k-S_{k-1} gives the sum on the positions of mirror depth at least k, and a second difference recovers each unordered mirror pair and the center if any. I enumerated each word up to common symbol renaming by restricted-growth strings, tested every orientation of those pairs (at most 16 per word), and compared exact spectra using noncarrying base-9 codes with one digit per letter. All 48,816 candidate comparisons for lengths 1–8 agreed, including all 4,140 length-eight renaming representatives; private replay /workspace/branches/replay/length8.py and length8.txt. For the four-word template, swapping the inserted letters reciprocates the bracket in the prefix polynomial while reversal preserves spectra; the four words are distinct iff both pairs have distinct entries. The positions recover both unordered pairs separately, even when they intersect. Reversal implies every singleton is a palindrome and the classification makes every palindrome a singleton. Thus there are q^4 singletons and binom(q,2)^2 quadruples; the remaining words pair off, giving the stated fiber and zero-error code counts. The first-ambiguity statement is in the q>=2 regime.

## originality

PASS

Supported for the complete arbitrary-alphabet fiber classification and exact census at length eight, not for the interleaving mechanism, the binary maximum fiber size, or the first-ambiguity boundary as standalone results.

## value

PASS

Length eight is the first intrinsically ambiguous length, not an arbitrary cutoff. The result gives the entire deterministic channel at that transition up to its observation fibers, including the overlap types of the symbol pairs and the exact loss of distinguishable words compared with reversal alone, for every finite alphabet. This is usable both as an exact benchmark for reconstruction and to determine the maximum zero-error code size at the boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
