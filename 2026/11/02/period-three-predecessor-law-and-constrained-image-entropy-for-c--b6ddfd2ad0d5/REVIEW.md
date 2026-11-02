# Scientific review

## Correctness — PASS

The Rule-22 local rule is exactly the three single-one neighborhoods; the complete zero- and one-edge de Bruijn graph is explicitly enumerated. A positive ones run between output zeros restricts the ring-predecessor path to two states, whose three residue matrices can be verified directly by following the one-edge three-cycle. Every closed path determines exactly one fixed-period input, even on one- and two-cell rings. Partial-permutation rank establishes the exact zero/one/two fiber classification, and the all-ones exception is counted independently. Weighted trace cycles convert marked gaps to indexed outputs using the exact \(n/m\) factor; the only duplicated fibers are all-residue-two even gap lists. Exact formal determinant differentiation yields the count. The standalone checker enumerates every input through ring length 17 and checks coefficients through length 120, independently of the proof. No finite experiment is treated as an all-length proof.

## Originality — PASS, qualified

Jen (1989) already supplies a general Rule-22 linear-preimage framework. Voorhees (1997) **already computes the numerical growth constant** of a zero-labelled Rule-22 de Bruijn fragment. Gravner and Griffeath (2010) develop the exactly-one rule from finite seeds. Martínez et al. (2019) supply Rule-22 de Bruijn and subset diagrams and explicit forbidden-pattern families. These overlap the mathematical ingredients but the inspected results do not assert the exact all-length *distinct fixed-ring image count constrained by avoiding cyclic `00`*, the multiplicity-two classification, or the precise gap-residue predecessor test. The 2019 regular-language approach could imply algorithmic computability of the constrained count, and the 1997 matrix is a close numerical match. Historical priority is consequently qualified; this review does not assert uniqueness across all literature.

## Value — PASS

High-density outputs avoiding adjacent zeros are a natural forbidden-pattern constraint. Even though one-step predecessor existence is decidable by classical de Bruijn methods, a complete closed-form reachability law and the complete fiber-ambiguity cutoff identify exactly which such targets can be synthesized with the same periodic boundary and quantify the exponential loss of attainable constrained configurations. The explicit all-length formula and sharp two-predecessor characterization are the substantive outcomes, not the already-known growth constant alone.

## Closest literature and limitations

E. Jen, *Complex Systems* 3 (1989), 421–456; B. Voorhees, *Complex Systems* 11 (1997), 373–385; J. Gravner and D. Griffeath, *Journal of Statistical Physics*, online December 10, 2010, DOI 10.1007/s10955-010-0103-9; G. J. Martínez et al., *Complex Systems* 28 (2019), 125–174, DOI 10.25088/ComplexSystems.28.2.125. The archive date is anchored to a verified online publication date, not guessed for the older sources. Only one step and cyclic `00`-avoiding indexed outputs are treated, and the published regular-language results create a nonzero residual priority risk.

Self-review: passed. Independent audit: not yet performed.
