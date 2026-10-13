# Review: an exact quadrangulation of \(H(8,3)\)

## Correctness — PASS

The witness is an explicit full ten-cycle for the order-56 affine group over \(\mathbb F_8\). All graph labels, 1120 darts, and 280 simple four-faces are accounted for by `verify_rotation.py`, while `verify_local.py` independently tests the ten local closure and group-product conditions. With 112 vertices and 560 edges, Euler gives genus 85. The graph is bridgeless and bipartite, so every possible orientable cellular embedding has faces of length at least four and genus at least 85. These are exhaustive checks for this fixed graph, not extrapolations from samples.

## Originality — PASS, subject to ordinary literature risk

The closest primary source, Metzger–Ulrigg (2026), proves a general theorem for \(H(h,2)\) and expressly reports only \(85\le\gamma(H(8,3))\le143\) in Section 9. Its invariant rotation formalism is acknowledged; the actual affine ten-cycle and the resulting genus-85 embedding do not follow from the previously stated bounds or the different \(k=2\) theorem. Alias, domination, and covering-implication searches did not identify an equivalent earlier embedding. Residual possibility: an unindexed or newly posted table/certificate.

## Value — PASS

The result closes a specifically recorded natural genus gap, attains the best possible Euler bound, and gives a highly symmetric constructive embedding at the first exceptional three-subset case. No generalization to other \(H(n,k)\) is claimed.

## Limits of review

External, independent mathematical validation has not been performed; code execution and this review are not a substitute. The proof and certificate address only orientable genus of the stated graph.

Self-review: passed. Independent audit: not yet performed.
