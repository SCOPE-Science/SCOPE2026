# Independent mathematical audit

## correctness

PASS

The Euclidean weight on F5 assigns e(0)=0,e(±1)=1,e(±2)=4. The explicit 2-by-9 full-rank matrices C,D have identical 25-message primal Euclidean weight enumerators, yet dual A2=14 and 10. A dual weight-two word has exactly two nonzero ±1 entries; its two generator columns therefore coincide modulo sign, yielding A2=2 sum over the 12 normalized ±column classes of binom(eta_j,2). Independent C++ exhaustive reconstruction algorithmically generated the 12 nonzero F5^2/± orbits, computed every normalized multiplicity vector of effective length 2 through 8 with rank2, grouped by the complete sorted weight multiset for 24 nonzero messages, and found no conflicting dual A2. Full-rank state counts were exactly 60,340,1335,4332,12334,31776,75528. The displayed n=9 pair was independently recalculated. Since every no-zero-column rank2 generator is covered up to sign/permutation and any row basis, this finite enumeration is exhaustive for the stated sharpness domain, not an asymptotic extrapolation.

## originality

PASS

Wood 2026 Example 9.1 is the highly relevant same-field, same-weight, same-dimension, same-dual-A2 primary source; it constructs length-18 and length-30 pairs and does not prove minimality at length nine. The present displayed shorter code pair and exhaustive exact <=8 cutoff are not the same conclusion and are not implied by existence of longer pairs.

## value

PASS

MacWilliams duality failures for non-Hamming weights are natural in coding theory; the first dual weight-two coefficient is structurally tied to repeated/opposite generator columns and is an especially interpretable failure mechanism. The smallest effective length for the original explicit dimension-two F5 mechanism is mathematically meaningful, since it quantifies minimal size of a duality obstruction and is certified exhaustively rather than merely suggesting a smaller pair. A complete fixed finite cutoff can be intrinsically useful without a broader coding theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
