# Scientific review: exact minimal-Roman census of graph joins

## Correctness
**PASS.** The private-zero characterization is proved in both directions directly from pointwise minimality. The four possible placements of label-\(2\) vertices across the two shores are exhaustive, and each branch is counted without overlap. Boundary cases involving one-vertex graphs, isolates, universal vertices, and equal-weight terms are explicitly included. An independent program tested every labeling for 281 small graph joins, comparing the full bivariate polynomial; all tests passed. Finite tests corroborate but do not establish the infinite theorem.

## Originality
**PASS on examined evidence; publication priority not certified.** The 2022 private-neighbor theorem of Abu-Khzam, Fernau, and Mann characterizes minimal Roman functions on arbitrary graphs but supplies no join coefficient identity in the inspected text. Their *Roman Census* paper enumerates on several graph classes and counts paths; its full accessible preprint did not provide this join formula. The closest public Roman polynomial record examines *all* Roman dominating functions on complete multipartite graphs, which is a different enumerated class. The present claim is the exact two-factor join identity for arbitrary factors, including its mixed-support term. Residual risk: unindexed, unavailable or more recent equivalent literature remains possible, especially within a later journal revision of the census paper.

## Mathematical value
**PASS.** An arbitrary graph join is a canonical graph operation, and exact counting of pointwise-minimal Roman functions is not equivalent to evaluating the Roman domination number or counting all feasible functions. The theorem gives every bivariate coefficient, isolates the exceptional mixed-defense configurations through the product of nonuniversal-vertex counts, and turns a potentially exponential enumeration into a simple compositional formula. Together with componentwise multiplication, it provides a polynomial-time exact coefficient recurrence on cographs; this is a motivated structural and computational gain, not an arbitrary parameter slice.

## Boundaries
The formula is for complete joins and pointwise-minimal standard Roman functions. It does not claim a general efficient algorithm for arbitrary graphs or establish publication priority. The verifier tests finitely many instances. The self-review is not independent mathematical certification.

Self-review: passed. Independent audit: not yet performed.
