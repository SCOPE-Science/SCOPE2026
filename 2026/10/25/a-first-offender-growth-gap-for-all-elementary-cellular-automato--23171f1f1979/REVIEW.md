# Review of the first-offender growth classification

## Correctness — PASS

The finding is an exact, finite, exhaustive result. The four-pair de Bruijn graph faithfully accepts finite words of each one-step image. Factoriality makes the allowed-prefix/allowed-suffix criterion necessary and sufficient for minimal forbidden words. The two-letter-ended product graph is deterministic, uniquely represents each offender, and has at most 256 pair-of-subset vertices before reachability and productive trimming. The SCC criteria distinguish finite, bounded, polynomial, and exponential accepted-path counts; all cases are mutually exclusive and complete. Exhaustive enumeration finds no polynomial case among all 256 rules. Every finite cutoff is a longest path in a directed acyclic productive graph. Integer transfer-vector repetition proves each bounded all-length formula. Independent finite-block enumeration checks counts at lengths one through nine for all 256 rules. All reproduced checks completed successfully.

## Originality — PASS under inspected evidence

The closest primary literature includes Abram–Lagarias (arXiv:1207.5004, graph descriptions of sofic symbolic systems), Béal et al. (DOI:10.1006/aama.2000.0682, minimal-forbidden-word growth as an invariant), and Salo (DOI:10.1007/s11047-022-09935-w, especially Section 6.2 on SFT/proper-sofic images and explicit offenders for certain elementary rules). Those works provide constructions, decidability, and specific cases but the available substantive text does not state the 176/28/52 all-rule trichotomy, exclusion of polynomially unbounded counts, or four exact bounded sequence families. Literature searches and available related scientific records were compared by mathematical implication, including earlier one-step image and periodic-lifting claims. Lack of a matching search result is not itself proof of novelty. Earlier equivalent unpublished or unindexed classifications remain a priority risk; an older conceptual paper was not available in full for inspection.

## Value — PASS

The growth of minimal forbidden words is an established natural invariant used to distinguish symbolic dynamical systems up to conjugacy, not an arbitrary selected statistic. This all-rule theorem splits proper-sofic elementary images into two sharply different regimes: finite-width obstruction families versus exponentially proliferating minimal obstructions. It proves the absence of intermediate polynomial growth and gives an exact cutoff for every finite-type image. The four bounded cases and all 256 classification entries are replayable without third-party computation. The result is not claimed for larger-radius cellular automata.

Self-review: passed. Independent audit: not yet performed.
