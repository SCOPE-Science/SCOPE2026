# Review status

Independent mathematical audit completed on 2026-10-01 UTC.

Scientific disposition: **passed**.

- Correctness: **PASS**. For a fixed smooth hard trial with a simple boundary zero, \(\widehat u(y,d)=a(y)d+O(d^2)\) with \(a(y)>0\), while \(\Delta\widehat u=O(1)\). Hence the singular source dominates and \(R\sim-a(y)^{-\alpha}d^{-\alpha}\). Multiplying \(R^2\) by \(1+\beta\widehat u^{-p}\) gives \(d^{-(2\alpha+p)}\), and a codimension-one collar is integrable exactly when \(2\alpha+p<1\). The one-dimensional grid laws are the standard harmonic-sum asymptotics, and differentiating \(d^{2-\alpha}\) verifies the proposed leading boundary correction.
- Originality: **PASS**. Best-of-knowledge originality survives. General warnings about least-squares residuals with singular data and hard PINN boundary factors are prior art, but the exact source-specific thresholds \(\alpha=1/2\) and \(\alpha=1/3\), fixed-trial resolution laws, and fractional boundary-correction mechanism were not found in the searched literature or published archive.
- Scientific value: **PASS**. The result identifies a precise failure mode in the population objective exactly where the proposed weighting is intended to focus, quantifies its resolution growth, and points to the missing boundary regularity. This is a motivated numerical-analysis boundary rather than a generic warning that singular data can be difficult.

Detailed evidence is recorded in `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
