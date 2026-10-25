# Scientific review: degree–leaf covariance by birth age

## Correctness — PASS
The independent uniform-parent construction gives the exact probability that each nonroot vertex survives as a rooted leaf. Conditioning on a later attachment gives the positive off-diagonal covariance; the product of a child's outdegree and its own leaf indicator vanishes, giving the negative diagonal. Summing proves the full birth-age profile. Its exact positive second difference, negative penultimate endpoint, and zero final endpoint imply ordered covariance signs with a possibly empty early positive block; the harmonic-sum limit gives the unique interior root near \(0.284668137\). Exact-rational finite enumeration supplements the unrestricted analytical proof.

## Originality — PASS, with stated priority risk
The previously published root-degree/leaf-count note proves the entire root row and root-total covariance, which are credited and explicitly excluded from the novelty claim. The present theorem's nonroot rows, strict convexity and complete birth-age sign classification are not stated there. Inspected primary writings on recursive-tree leaves, labeled degrees and leaf-degree counts do not directly supply the nonroot theorem. The mathematical comparison concerns propositions and implications rather than titles; older implicit moment identities remain a risk and no independent priority examination is claimed.

## Value — PASS
This is a natural full cross-covariance between local birth-labeled outdegrees and global leaf count in the canonical recursive tree. The nonroot signs reverse across a sharp asymptotic fraction of birth times, so the known positive root correlation masks late-vertex negative dependence. The full array and strict convexity identify the age mechanism and a precise asymptotic cutoff; they are not merely a re-expression of the published root result.

## Reproducibility and limitations
`python verify.py` uses exact rational arithmetic, exhaustive independent parent arrays for \(2\le n\le9\), and algebraic checks through \(n=200\). The program returned `VERIFY_OK 34860 exact assertions; 46233 enumerated trees`. The theorem is specific to rooted leaves defined by outdegree zero and uniform parent choice. It does not imply independence from vanishing covariance, general stochastic association, or preferential-attachment analogues. Numerical checks cannot replace the proof.

Self-review: passed. Independent audit: not yet performed.
