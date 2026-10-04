# Same-model review

## Correctness
PASS. The proof reduces the projection-free update to an explicit \(2\times2\) matrix, verifies the exact quadratic invariant, and identifies positive definiteness for \(\tau\sigma<4\). The two completed-square identities locate the exact lowest invariant level on each projection boundary. This proves both forward projection-freeness of the strict sublevel and sharpness of the stated threshold. The characteristic polynomial then yields the exact resonance periods. The embedded checker reproduces the algebra and representative orbits.

## Originality
PASS with a stated residual risk. He--You--Yuan supply the constrained scalar recurrence and the \(r=s=1\) six-cycle. Bailey--Gidel--Piliouras later supply a broader unconstrained conserved-energy theorem whose scalar specialization is exactly the interior invariant, so that invariant is expressly treated as prior art. The finding is the exact largest invariant-energy neighborhood avoiding the projections and the constrained exact-period family that follows from it. Targeted searches found no source stating that threshold or family. The main residual risk is unindexed expository material carrying out the same elementary boundary calculation.

## Value
PASS. The result gives a rigorous mechanism for nonconvergence at arbitrarily small fixed steps in the canonical published counterexample, replacing finite-horizon numerical evidence by an exact theorem on an open set of starts. The sharp boundary also identifies precisely where projection effects can first enter, which is useful for understanding why a constraint can hide or reveal the conservative alternating-gradient dynamics.

## Closest literature and limitations
The closest conceptual predecessor is arXiv:1907.04392, which explains conserved energy and recurrence for unconstrained alternating gradient descent--ascent. The primary constrained example is DOI 10.1137/140963467. Modern PDHG-for-LP analysis such as arXiv:2307.03664 concerns a different extrapolated/convergent regime. The present theorem remains local and does not classify global projected dynamics or the zero-start orbit for every small step.

Same-model review: passed. Independent audit: not yet performed.
