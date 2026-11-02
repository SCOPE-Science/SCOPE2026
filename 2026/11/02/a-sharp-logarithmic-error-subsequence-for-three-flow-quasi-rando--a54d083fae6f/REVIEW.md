# Mathematical review

**Correctness — PASS.** Matrix units square to zero, making each flow linear in the step size. The \((1,3)\) entry is exactly a signed within-step count with no higher-order remainder. The four-digit reversal identity and odd-prefix three-case split prove the signed count \(1-2k\) for every integer \(k\ge1\), and the exact asymptotic follows. The accompanying checker independently confirms arithmetic in full matrix products, but no infinite claim rests on finite samples.

**Originality — PASS within reviewed literature.** The originating revised 2026 paper proves an \(O(h^2\log N)\) upper bound, not a matching lower bound for the direct decoder. Classical discrepancy results describe van der Corput counting functions, not an explicit product-of-three-flows global-error witness. Earlier implementations employing multiple points and Fisher–Yates shuffles are a different mathematical algorithm and do not imply this result. The possible derivability of the scalar signed count from classical discrepancy formulas is acknowledged; the asserted contribution is the exact sharp operator-splitting realization, not a new general discrepancy theorem.

**Value — PASS.** An identified recently proposed deterministic low-cost integrator has a logarithmic factor in its main guarantee. Establishing that factor's necessity under the actual direct decoder, with an exact subsequence and smallest natural nontrivial three-operator nilpotent chain, is a motivated boundary result. It rules out unconditional second-order convergence for this decoder without asserting limitations of other quasi-random designs.

**Closest literature and limitations.** Li–Liu–Wan, arXiv:2603.27654v2, Section 2 and bounded-linear theorem; Beretti, *On the distribution of the van der Corput sequences* (2023), on classical distribution questions. The v1 and v2 source algorithms differ; exact bibliographic priority remains subject to specialized further review. This is a deliberately narrow worst-case matrix example, not a statement about typical performance or nonlinear stability.

Self-review: passed. Independent audit: not yet performed.
