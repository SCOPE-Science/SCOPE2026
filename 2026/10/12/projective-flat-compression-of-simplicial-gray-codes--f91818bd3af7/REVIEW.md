# Self-review

## Correctness — PASS
The Gray coordinate maps are invertible over every finite field. Their excluded images are coordinate-linear subspaces of dimensions \(a+b\), intersecting in dimension \(b+|A\cap B|\); projective inclusion-exclusion yields the heavy/light counts. The complement spans and has sharp Grassmannian dimension-intersection bounds, which supply the full compressed-core generalized Hamming-weight hierarchy. Proportional columns account for every weight-two dual word. The binary quotient-space argument constructs a weight-three parity relation at every light coordinate. The accompanying verifier exhaustively reproduces the asserted counts and all core generalized weights in seven cases, including the four-element field. There is no unproved step being inferred from finite tests.

## Originality — PASS, with residual search risk
The 2026 Yadav--Tiwari--Sarma paper defines the complement-product code and proves its Lee-weight distributions, not the projective flat core, exact heavy/light multiplicities or the unreduced dual-locality classification. The earlier Chen--Xu--Hu--Li--Zeng construction uses factorwise complement products rather than the whole-product complement. An abstract punctured-simplex generalized-weight calculation is classical and is *not* treated as a novel independent theorem; identifying this family with that geometry and resolving the original coordinate multiplicities/repair profiles is the distinct result. A previously examined special finite example does not imply the uniform theorem; an unindexed equivalent statement cannot be excluded.

## Value — PASS
The projective compression gives a canonical minimal set of projective evaluation directions, determines every generalized support threshold of this core, and quantifies exactly how the original length is expanded into one- versus two-level repeated projective coordinates. The sharp locality distinction in the binary and nonbinary cases is relevant to repair properties of the newly constructed code family.

## Closest literature and limits
Yadav--Tiwari--Sarma (arXiv:2609.11783v1), Theorem 3.3, and Chen et al. (arXiv:2407.10074v1) were the closest inspected sources. The generalized weights describe the compressed core only; the longer Gray image can have different support weights. Verification is not an all-field exhaustive census and does not substitute for independent audit.

Self-review: passed. Independent audit: not yet performed.
