# Review status

Independent mathematical audit completed on 2026-10-01 UTC.

Scientific disposition: **repaired**.

- Correctness: **PASS**. Plancherel and the same-sign quadrant multiplier give the exact kernel identity. Since \(0\le J(s)\le s\) and \(J(s)/s\to1\), dominated convergence gives the finite half-Sobolev limit and Fatou gives divergence outside the half-Sobolev class. For finitely many jumps, the distributional derivative has a finite atomic part; diagonal atomic terms contribute the logarithmic coefficient and off-diagonal terms are oscillatory lower order. The constants reduce correctly to the hard interval cutoff.
- Originality: **PASS**. Originality passes only for the repaired arbitrary-cutoff half-Sobolev theorem and finite-jump law; the hard-strip leading constant is prior coverage.
- Scientific value: **PASS**. The repaired result identifies the exact regularity threshold governing an entire natural cutoff family and explains the jump logarithm structurally. This is a reusable analytic law, not a recomputation of the already-known single indicator constant.

Detailed evidence is recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and
`INDEPENDENT_AUDIT_2026-10-01.json`. Earlier same-model evidence remains identified
as such in `AUDIT.json` and is not relabeled as independent evidence.
