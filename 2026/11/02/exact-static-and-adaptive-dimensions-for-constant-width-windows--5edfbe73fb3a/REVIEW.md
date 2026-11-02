# Scientific review

## Correctness — PASS

For every finite path and cycle parameter, upper adaptive bounds follow from the total number of concepts and the least root-branch population. The lower bounds use a fully specified constructive binary tree: select equal-size consecutive blocks of possible start positions in both branches, then query successive midpoints. For cycles the no-wrap guarantee uses both \(k\) and \(n-k\). The static VC result follows from the consecutive-ones obstruction for three sites and sharp pair-labeling thresholds. All boundary cases were checked independently. The proof is unrestricted; the brute-force census is corroboration only.

## Originality — PASS under accessible sources

Guingona, Kolesnikov, Nierwinski and Soucy (arXiv:2109.04805v1, Theorem 3.10, Section 6) prove equal dimensions for complete families of zeros of nonzero linear combinations, not the fixed-width window families here. Their equality theorem cannot yield the arbitrarily large strict separations in this result. Chase, Freitag and Reyzin (arXiv:2310.04812v1, Sections 2–4) use Littlestone dimension for equivalence-query learning and give a disjoint-interval example, but do not provide exact cyclic or path window formulas. Searches for sliding-window, unit-interval, cyclic-arc, neighborhood-incidence and equal-length interval variants identified no covering statement. Prior accessible findings were compared by claim rather than wording; the closest topical published record is about graph cover-free-family numbers, not shattering dimensions. Uninspected historical notes on finite-domain online learning remain a priority risk.

## Mathematical value — PASS

The result gives a sharp all-integer two-topology phase diagram, not a finite-table increment. Exact finite-width formulas exhibit saturation of the adaptive dimension, while the static VC thresholds differ between paths and cycles. The path case shows unbounded logarithmic adaptive complexity already when VC dimension is precisely one; the cycle case has complementary-width symmetry and similarly unbounded separation with VC dimension two. These statements quantify a natural fixed-window learning task and are not implied by generic cardinality or VC bounds alone.

## Scope and limitations

Single fixed-cardinality window, binary vertex queries, finite paths/cycles only. The code checks all sizes through sixteen, not infinitely many sizes. Comparison coverage is limited to retrieved published-finding corpus records, accessible local claim ledgers and named primary texts; the literature search is not exhaustive. Independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
