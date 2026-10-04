# Review

## Correctness
PASS. The final claim is represented exactly as two clique numbers in the compatibility graph on all self-non-overlapping ternary words of lengths \(2\) through \(5\). The standalone verifier regenerates all \(216\) vertices, proves the unrestricted clique number is \(17\), proves every clique containing a short vertex has size at most \(16\), and directly checks explicit witnesses of both sizes. The pruning bound is a proper coloring bound, so no branch capable of improving the incumbent is discarded.

## Originality
PASS. The 2023 fixed-length study supplies the nearby exact fixed-length frontier, while the 2024 variable-length paper proves the general comparison with fixed-length codes and poses/studies the average-length question. Neither source inspected gives the exact ternary \(n=5\) short-word threshold. Focused database searches for the formulations “every \(17\)-word ternary variable-length code has length five” and “maximum with a short word is \(16\)” returned the fixed-length records and a general stationary-occupancy bound as closest matches, not an implication-equivalent result. The 2025 generalized-construction paper concerns constructions and cardinality bounds rather than this exact extremal classification.

## Value
PASS. This is a natural complete small-parameter boundary for the minimum-average-length problem: it identifies the first extremal ternary length-five cardinality and shows exactly how much cardinality is lost by admitting any shorter word. The statement is stronger than merely recomputing the fixed-length optimum because it classifies the entire variable-length frontier at cardinality \(17\).

## Closest literature and limitations
The closest fixed-length result is Stanovnik–Moškon–Mraz, arXiv:2307.12593 / DOI 10.1007/s10623-023-01344-z. The closest variable-length framework is Wang–Wang, arXiv:2402.18896. A later construction paper is Qin–Luo, DOI 10.1007/s10623-025-01585-0. The result remains specific to the ternary alphabet and maximum word length five, and the upper bounds are computer-assisted finite proofs.

Same-model review: passed. Independent audit: not yet performed.
