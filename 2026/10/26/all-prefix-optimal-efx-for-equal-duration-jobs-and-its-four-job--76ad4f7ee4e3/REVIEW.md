# Scientific review

**Correctness — PASS.** The exchange proof establishes that accepting every job that does not exceed the simultaneous capacity is cardinality optimal when durations are equal; cycling accepted jobs among machines is feasible and keeps all cumulative loads within one. The rational four-interval witness has exactly three EFX-compatible accepted jobs versus four unrestricted jobs, and triangle-free graphs on three vertices show that fewer jobs cannot witness a gap. The standalone checker confirms 19,305 equal-length grid instances, four exact perturbations, and 455 smaller two-machine examples; the universal proof does not rely on enumeration.

**Originality — PASS, with remaining priority risk.** The 2026 motivating study proves general \(3/2\) offline and \(2-1/m\) online bounds, and its constructions do not establish the exact zero-loss irreversible policy for equal-duration unweighted intervals or the near-equal-duration four-job boundary. An older claw-free equitable-coloring theorem already implies static balanced coloring for equal-duration interval conflict graphs, and this previously known consequence is not claimed as new. The 2012 equal-length online-scheduling paper was available only as an abstract, leaving some residual uncertainty about equivalent unweighted online subresults.

**Value — PASS.** The exact separation answers a motivated question about whether temporal uniformity eliminates the efficiency cost of a fairness constraint. The answer is affirmative even without revocation when durations coincide, but fragile: any positive allowable relative duration spread creates a fixed two-machine gap. A cardinality-minimal witness identifies the smallest boundary phenomenon; this is not a parameter relabeling of the standard general-interval lower bound.

**Limitations.** No upper bound matching \(4/3\) is asserted for perturbed durations. The theorem assumes equal unit values, common duration for the positive direction, and nondecreasing start-time arrival. Publication priority remains qualified by the unavailable complete 2012 paper and possible unindexed equivalents.

Self-review: passed. Independent audit: not yet performed.
