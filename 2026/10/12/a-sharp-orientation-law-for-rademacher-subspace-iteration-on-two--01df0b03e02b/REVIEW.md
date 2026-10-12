# Self-review

## Correctness — PASS

A sign sketch in two dimensions has exactly two equiprobable projective directions. Independent columns give two disjoint all-one-direction events of probability \(2^{-\ell}\) each, and a complementary full-span event. For any singular-vector orientation, the power-sketch output in a rank-one event has left-singular coordinate weights proportional to \(a^{4q+2}c\) and \(b^{4q+2}(1-c)\). The resulting exact captured Frobenius energy gives the advertised rational risk formula. The strict concavity proof establishes the *unique* central minimum and endpoint maxima over the entire orientation interval. The Gaussian comparison follows from full row rank almost surely. Direct exact-rational enumeration checked 410 combinations. No finite enumeration is invoked as an infinite proof. Limitations: exact arithmetic, rank two, iid dense signs, specific truncated output and squared Frobenius risk.

## Originality — PASS

The closest defining analysis is Saibaba–Międlar, arXiv:2308.05814v1, §§2–4 and Appendix B, which covers independent sub-Gaussian sketches (including signs) by structural/distributional bounds but does not compute unconditional rank-one-truncated rank-two expected risk over all singular frames. Saibaba, arXiv:1804.02614v2, §§2–4 treats truncation and full-rank structural bounds, while Diouane et al., arXiv:2206.08793v2, consider deterministic bounds and Gaussian expected errors. The new statement identifies a sharp orientation extremizer, an exact finite-sample all-power failure mass, and a sharp uniform expectation guarantee; those conclusions are not direct special cases of the cited claims. Risk: a separate elementary 2D sign-sketch calculation could exist outside searched/indexed literature; no independence or universal novelty certification is implied.

## Value — PASS

A sign sketch is inexpensive and included in the non-Gaussian methods studied in the defining source. The theorem gives a **complete, sharp** two-dimensional risk classification for arbitrary singular frames rather than a single counterexample: spectral-gap amplification cannot repair an exactly missed leading direction, but repeated independent sign columns lower the worst-case risk by an exact exponential law. This distinguishes algorithmic benefit of repeated power steps from genuinely new sampling directions and quantifies when distribution choice matters. The exact worst- and best-orientation comparison is useful for evaluating non-Gaussian randomized low-rank approximation guarantees. It makes no general high-dimensional or numerical-stability claim.

Self-review: passed. Independent audit: not yet performed.
