# Self-review

**Correctness: PASS.** The draw-rank convention is matched directly to the source definition. Exponential races provide the exact expectation integral; an at-most-two-index identity bounds its tails. A uniform Fourier adjacent-mass inequality, variance asymptotics and Chebyshev localization prove the pointwise rescaled integrand limit, and dominated convergence yields the claimed \(1/e\) logarithmic coefficient. The proof covers all integers tending to infinity. Exact checks for sizes \(1\) through \(7\) and 32 separate Bernoulli-integrand checks agree; finite checks do not substitute for the asymptotic proof.

**Originality: PASS, with historical-priority risk.** The motivating Borga--Chatterjee--Diaconis paper explicitly leaves fixed-point growth for these singular weights unresolved (Section 5.2). Mukherjee's general fixed-point Poisson limit requires a continuous bounded density and uniform local asymptotics not present here. Paguyo's conditional uniform double-coset theorem is a different probability law, and the Borga--Dubach 2026 study concerns longest increasing subsequences. A full statement/implication comparison and targeted database searches found no directly covering logarithmic coefficient. Earlier size-biased-permutation literature could still encode the identity indirectly.

**Mathematical value: PASS.** The exact growth constant and logarithmic scale address a highlighted natural open observable, correcting the inability to extract a finite diagonal integral from the singular permuton. The auxiliary Bernoulli localization has a structural role: it turns a sum of dependent rank-equality events into two possibilities for each Bernoulli configuration. Only the expectation is solved; concentration and distribution remain open.

The closest earlier results and remaining risks are in the accompanying `AUDIT.json`, and the proof/finite tests are self-contained in `RESULT.md` and `verify.py`.

Self-review: passed. Independent audit: not yet performed.
