# Scientific review

**Correctness — PASS.** The result is an exact event-probability calculation, not an asymptotic extrapolation: the random side triangle partitions its host into three disjoint corner triangles plus its own interior; integrating the two independent side fractions gives each corner probability explicitly. Summing yields the barycentric expression. The derivative identities prove strict Schur concavity on the open simplex (including unequal coordinates on opposite sides of one-half), hence the unique centroid maximum. The stated vertex expansion follows by Taylor bounds on the displayed scalar function. The independent numerical checker passed all tests, which are corroborative only.

**Originality — PASS, with residual bibliographic risk.** The closest paper with the same sampling distribution, Maesumi (arXiv:1804.11007), solves the law of inscribed **area** and does not provide a spatial point-inclusion map or its Schur order. Reitzner–Schütt–Werner (arXiv:1911.05917) treat boundary-pooled sampling and asymptotic face and volume expectations. Ismailov (arXiv:2601.02929) treats a circle rather than one sample per straight side. Targeted exact-formula, containment, centroid, source-ID, and geometric random-hull searches revealed no same-object equivalent; existence of a neglected elementary derivation cannot be excluded.

**Value — PASS.** A natural pointwise geometric observable—the probability that a random inscribed convex hull covers a given host point—is completely classified throughout the host, not just averaged. The strict Schur order singles out the centroid as the uniquely most robust point in every triangle, and the binary-entropy boundary law quantifies how robustness is lost toward a vertex. The spatial integral recovers the known mean area as a consistency check without being equivalent to the new profile.

**Limits.** Exactly three independent edge-stratified samples, not perimeter-pooled samples or higher polygons. No independent mathematical audit or exhaustive bibliographic certification.

Self-review: passed. Independent audit: not yet performed.
