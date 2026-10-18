# Scientific review: odd-length circular universality extremizers

## Correctness — PASS

The proof establishes equivalence between \(k\) mixed-letter arches in a length-\(2k+1\) rotation and a near-perfect matching of unlike cyclic edges. Deleting equal-letter edges leaves paths whose exact matching capacities imply a unique even-run parity defect. A canonical distinguished equal-letter edge gives a bijective rooted enumeration, and exactly two binary lifts exist per even-parity transition vector. Any nontrivial power would repeat the unique defect, so all maximizers are primitive. The fixed-cut arch enumeration then gives the rescued count. Both inequalities and endpoint \(k=1\) are explicitly treated. The packaged checker corroborates all binary words through length \(16\) and seeded longer cases; finite checks are not used as a substitute for proof.

## Originality — PASS, with specified residual risk

Barker et al. (2020), arXiv:2003.04629, introduce circular universality and the necessary arch framework. Schnoebelen and Veron (2023), arXiv:2304.11932, compute the circular index of an individual word and generalize arch tools. Their complete accessible texts were examined. The known exact linear-universality enumeration counts words with an optimal *fixed* reading origin, not the union of optimal rotations. The inspected sources do not state the unique odd-cycle parity defect, exact odd-length maximizing necklace count, or blanket primitivity. Published research-record searches and available earlier claims did not expose an equivalent or dominating result. The full text of Fleischmann, Germann, and Nowotka (2021), arXiv:2104.09063, was inaccessible; an equivalent theorem elsewhere remains possible. No external novelty certification is asserted.

## Mathematical value — PASS

Odd length \(2k+1\) is a sharp one-letter slack regime for \(k\) mixed-letter arches. Rather than merely counting a special example, the theorem classifies *every* maximizing cyclic word, proves that orbit stabilizers vanish, and quantifies rotation-rescued words exactly. The difference between fixed-cut and cyclic universality is a natural mathematical gap, and the complete parity/matching/necklace description is a nontrivial finite-alphabet classification valid for all \(k\ge1\).

## Scope and verification limits

The claim is binary and odd-length only; even-length and larger-alphabet analogues, and nonmaximal index distributions, are not asserted. The unavailable 2021 full text is an originality risk. The verification program is a finite cross-check; the all-length conclusions rely on the proof in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
