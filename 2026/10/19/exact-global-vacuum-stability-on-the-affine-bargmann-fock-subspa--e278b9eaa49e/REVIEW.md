# Scientific review of exact affine Bargmann–Fock vacuum stability

## Correctness — PASS

The normalized complex Gaussian variables satisfy \(\mathbb E|Z|=\sqrt\pi/2\) and \(\mathbb E|Z|^2=1\). The proof differentiates the modulus variance of a displaced circular Gaussian and expresses the derivative as twice a covariance. Conditioning on radius yields a strictly increasing angular cosine mean, because its derivative is a positive multiple of an angular variance. The independent-copy covariance formula makes this a rigorous global inequality, not an extrapolation from a parameter grid. Gaussian rotation collapses all affine functions in arbitrary dimension to this two-parameter bound. Squaring nonnegative quantities, orthogonality of constants and first-degree monomials, and evaluation at the normalized first Hermite function complete the proof. Both pure-component equality families and strict mixed-component cases are accounted for. The 64-point SciPy checker corroborated the identities and boundary cases. Risk: None of the finite tests can replace the analytic argument; the specified Gaussian and modulus normalizations are essential.

## Originality — PASS with residual historical-priority risk

The most directly relevant full-text result (Bertolini et al., arXiv:2605.20527v1, Theorems 1.3–1.5 and Theorem 2.1) proves existence of a finite vacuum phase-retrieval stability constant in the full Fock space, using a nonoptimized coercivity constant, not the sharp affine constant or the equality-and-remainder theorem. Full text of Bortolotto–Ramos, arXiv:2608.26365v1 (introduction, principal square-coercivity theorem, and discussion), concerns a different squared-amplitude functional and likewise does not supply this exact affine profile. Searches for degree-one / first-Hermite / Gaussian-affine / Rician formulations and for stronger covering statements returned no equivalent formula. The 2025 Cheeger–RKHS paper addresses general Cheeger stability mechanisms; its full argument was not inspected, so historical priority is not absolute. An indexed real Mercedes-frame sharp stability result concerns a different frame and does not imply the present complex Gaussian calculation. General Rice distribution moments are previously known: the claim is their sharp **phaseless Fock application** and the explicit global remainder, not discovery of the Rician law.

## Value — PASS

A recently proved global vacuum stability principle in an infinite-dimensional coherent-state inverse problem naturally asks for a sharp benchmark. The vacuum plus first-Hermite band is the smallest nontrivial complex finite-dimensional coherent-state truncation, and its exact global constant provides a calibrated baseline rather than an arbitrary finite slice. The dimension-free theorem simultaneously computes an optimal quantitative constant, proves a sharp radial error remainder, and classifies all equality cases; its monotone-covariance proof is structural. The value does not depend on a claim about the optimal full-space constant or a generalization to all reference signals.

## Residual risks

A pre-existing specialized Gaussian–Rician inequality could entail the two-parameter mean bound; even if so, the full affine phase-retrieval remainder may already have been worked out in a source not surfaced by the searches. The Cheeger manuscript's full body was not inspected. The work has had no independent scientific audit; these caveats should not be construed as a novelty certificate.

Self-review: passed. Independent audit: not yet performed.
