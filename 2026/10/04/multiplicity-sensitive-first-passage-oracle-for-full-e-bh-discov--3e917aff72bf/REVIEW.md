# Same-model scientific review

## Correctness
**PASS.** The proof reduces terminal full discovery to the deterministic e-BH rank condition. Because null e-values are exactly \(1\) and \(\alpha<1\), no rank above \(m\) can qualify. Full discovery therefore forces rank \(m\) and forces every nonnull terminal value above \(K/(\alpha m)\). This makes each stream's first-passage count an unavoidable coordinatewise lower bound, while parking exactly at first passage attains the sum. The sharpness example for every lower common parking level is exact. The likelihood-ratio expectation formula uses Wald's identity only under explicitly stated integrability assumptions and retains the overshoot.

The finite verifier uses exact rational arithmetic and exhaustively checks a nonmonotone example; it is corroboration, not the proof of the general theorem.

## Originality
**PASS.** The closest recent primary source, Lin–Ma–Ren–Wei (arXiv:2609.26651v1), analyzes the same full-discovery objective but uses a per-nonnull crossing boundary \(\log(K/\alpha)\) in its simple-alternative upper and expected-stopping analyses. Its lower bound has \(\log(1/\alpha)\) scale but does not identify the exact multiplicity interpolation. Wang–Ramdas (2022) stops a bandit arm when the rejection set actually grows, rather than parking latent evidence at \(K/(\alpha m)\). Wang–Dandapanthula–Ramdas (2025) studies filtration validity of stopped e-BH rather than sample-optimal parking. Searches for equivalent first-passage, pooled-threshold, and multiplicity-sensitive formulations found no covering result.

A related prior result about preserving already-rejected e-BH coordinates was compared by implication. It starts after a rejection set exists and gives a floor for maintaining those rejections under future betting. It neither supplies the pre-rejection pooled boundary nor the exact oracle full-discovery sample cost here.

Residual originality risk remains because the proof is a short but sharp consequence of the e-BH step-up rule; no stronger priority claim is made than the completed searches and source inspections support.

## Value
**PASS.** The result addresses a motivated gap exposed by the 2026 sample-complexity analysis. The exact oracle boundary \(\log(K/(\alpha m))\) interpolates between its one-signal upper-style boundary \(\log(K/\alpha)\) and the dense-signal information scale \(\log(1/\alpha)\). This cleanly separates multiplicity pooling supplied by e-BH from the extra cost of identifying signals and managing live evidence. The exact sum-of-first-passages identity and sharp common parking threshold provide a reproducible benchmark for future adaptive methods.

## Closest literature and limitations
The theorem is deliberately narrower than the adaptive algorithms in the cited papers. It assumes oracle knowledge of the nonnull set and count, fixes null evidence at \(1\), and does not claim an implementable method attains the oracle boundary. The mean formula also requires Wald conditions and retains the overshoot. These restrictions are essential to the statement rather than post-hoc disclaimers.

Same-model review: passed. Independent audit: not yet performed.
