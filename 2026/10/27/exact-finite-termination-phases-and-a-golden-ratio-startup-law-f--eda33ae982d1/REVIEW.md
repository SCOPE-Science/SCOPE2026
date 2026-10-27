# Self-review

**Correctness — PASS.** An explicit normalized transition recovers the source algorithm exactly on all real isotropic quadratics. The exhaustive symbolic branch split supplies each termination index, with no reliance on simulation for continuum claims. The post-reset strict inequality and the convergent iterated-radical product establish the delicate endpoints and asymptotic constant. The standard-library verifier performed high-precision checks of over ten thousand cases.

**Originality — PASS, best-knowledge only.** The original AdaBB Algorithm 1 and its source-specified informed initialization are credited. Source Lemma 4.1 gives lower-step bounds, not the exact finite termination partition. The original source Table 1 contains an iterated radical for a different algorithm and does not imply the precise AdaBB stopping count without further analysis. Huang et al. (2022) have a finite-termination theorem for a different accelerated BB scheme with an extra spectral step. Focused equivalent-formulation, broader-coverage, parameter/table and implication comparisons of the published source, the earlier BB paper and mathematical research records did not find the exact claim. A specialized equivalent recurrence could still exist; independent priority review is outstanding.

**Value — PASS.** Warmup cost is directly motivated by the source's special step initialization. This result completely classifies the smallest nontrivial spectral model, demonstrates a sharp seven-versus-four iteration switching boundary, and computes a genuine asymptotic coefficient for the uninformed delay. It is not a claim of a new faster algorithm or of dimension/condition-number-independent finite termination for arbitrary quadratics.

**Limitations.** Exact arithmetic, scalar-Hessian real quadratic, original Option II AdaBB only. The very-small-step phase is sensitive to finite-precision rounding. The classical BB method itself solves the same isotropic example more quickly, so the comparison is about this safeguarded algorithm's internal warmup penalty, not superiority. Independent proof/priority auditing remains to be performed.

**Sources.** Zhou–Ma–Yang, arXiv:2401.08024 (Algorithm 1, equation (36), Lemma 4.1, Table 1); Huang–Dai–Liu–Zhang, DOI:10.1007/s10589-022-00349-z (Theorem 1); targeted published mathematical research records and earlier related mathematical claims.

Self-review: passed. Independent audit: not yet performed.
