# Scientific review — four-letter one-deletion graph triangles

**Correctness — PASS.** The theorem has a precise vertex set, edge relation, strict distinct-vertex triangle convention, and range \(n\ge1\). Its proof specifies the NFA alignment semantics, the complete determinized transition enumeration, the exact finite-state matrices, and an integer-only Cayley–Hamilton certificate. The certificate proves the recurrence at all later indices, and the closed forms satisfy the recurrence and initial conditions. Independent direct deletion-ball graph enumeration verifies small block lengths. Machine checks must be rerun from the embedded `verify.py`; the reported counts are not a substitute for the certificate.

**Originality — PASS against inspected sources; residual risk retained.** Alon et al. (arXiv:2209.11882, 2022-09-23) work on the same general-alphabet deletion graph but obtain asymptotic triangle upper bounds, not exact quaternary enumeration. A public exact result for binary one-deletion graphs has a different fixed alphabet and does not determine four-letter coefficients. Targeted searches for the exact number, a four-letter formula, and q-ary analogues found no prior result with statement-level coverage. A differently phrased or unindexed equivalent formula cannot be ruled out.

**Mathematical value — PASS.** The exact count concerns the natural four-symbol alphabet used in coding and DNA-sequence models. It sharpens the known triangle bound by providing the complete all-length count and the precise \((45/32)\) leading constant. Unlike a simple change of notation in the binary result, the transition multiplicities and 1549-state certificate genuinely depend on the larger alphabet. This is a structural graph invariant, not a claim of a downstream code-size improvement.

**Limitations and closest work.** No general-alphabet formula, higher-deletion-radius result, or coding bound is asserted. The prior binary theorem uses a related automaton strategy; the present result supplies the distinct four-symbol coefficients and their certified all-length proof.

Self-review: passed. Independent audit: not yet performed.
