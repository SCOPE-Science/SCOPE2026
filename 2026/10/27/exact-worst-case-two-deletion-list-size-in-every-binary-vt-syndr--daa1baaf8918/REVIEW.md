# Scientific review

**Correctness — PASS.** The perfect single-insertion syndrome partition has a direct checksum proof. Counting intermediate words gives \(2L\le n+s_1\), and a singleton parent must have one of two doubled-run forms. Their checksum progressions permit at most two singleton fibers, proving the universal bound. The parity-specific explicit support lists attain the bound for every syndrome. Independent finite checks examine every received word for \(3\le n\le13\) and all explicit witnesses up to \(n=80\), returning `VERIFY_OK`; finite experiments do not substitute for the proof.

**Originality — PASS with residual risk.** Banerjee et al. (arXiv:2610.15767v1) address average list sizes; Wachter-Zeh (arXiv:1701.02612v4) gives a two-deletion VT list upper bound of \(n\). Neither of the inspected full texts establishes the sharp per-syndrome maximum, and nearby finite code optima do not imply this conclusion. Earlier unindexed equivalent work is possible.

**Value — PASS.** Exact worst-case ambiguity is a fundamental decoding parameter, and achieving the same sharp formula in every checksum class settles the natural finite-length problem uniformly rather than providing an arbitrary instance or routine corollary.

Scope is binary VT codes with two exact deletions. The result makes no polynomial-time decoding claim. There is no independent scientific validation.

Self-review: passed. Independent audit: not yet performed.
