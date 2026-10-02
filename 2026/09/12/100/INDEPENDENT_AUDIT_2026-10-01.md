---
audit_date_utc: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

For infinitely many q=\(r^2\) with r=\(3^k\), there are equal N-point/N-plane configurations in \(\mathbb{F}_q^3\) with every line carrying at most \(\(N^{1/4}\)\) selected points and planes, yet with Omega(\(N^{3/2}\)) incidences; hence no absolute C can make an \(N^{3/2-\delta}\) bound hold under this cap for any fixed delta>0.

## Correctness — PASS

The subfield starter has |P0|=\(r^3\), |Pi0|=\(\(r^3\)+\(r^2\)+r\) and \(r^5+r^4+\(r^3\)\) incidences. Independent variance counting gives only same-point and same-plane covariance contributions, safely below the package's \(4r^5\) majorant. Chernoff plus a union bound controls every F-line, and low-degree deletion to N=floor(\(3\(r^2\)/4\)) on both sides preserves at least one quarter of the thinned incidences. At r=6561 the package majorant evaluates to about 0.00247349<1, while the cap threshold condition is amply satisfied. The asymptotic ratio against C \(N^{3/2-\delta}\) diverges.

**Evidence inspected:** artifacts/check_bounds.py; https://arxiv.org/abs/1806.03534

**Residual risk:** The artifact docstring contains an obsolete 56/\(r^2\) phrase, while the executable calculation and proof use 16/r; this documentation typo is not used in the argument.

## Originality — PASS

Rudnev's point-plane theorem gives the familiar |Pi|(sqrt(|P|)+k) estimate only under the positive-characteristic restriction |P|<\(p^2\). Here p=3 while N grows like \(r^2\), so that theorem does not cover this subfield regime. No inspected source gave the \(\(N^{1/4}\)\)-capped thinned-subfield counterexample or an implication yielding it.

**Equivalent formulations:** Compared the line cap with Rudnev's maximum-collinearity parameter and with balanced equal-size incidence formulations.

**Broader coverage:** Rudnev's theorem is broader geometrically but restricted to |P|<\(p^2\) in positive characteristic; it does not imply a bound in the constructed regime.

**Exact database or table:** No table is relevant; published-corpus searches found no matching capped construction.

**Claim versus prior implication:** Known point-plane incidence bounds do not imply the disproof because their characteristic-size hypotheses fail here.

**Primary/technical sources inspected:** https://arxiv.org/abs/1806.03534

**Residual risk:** A similar subfield-thinning witness may exist in specialist folklore or non-indexed notes.

## Value — PASS

The construction isolates a sharp structural obstruction: a line-load cap of order \(\(N^{1/4}\)\) alone cannot force any power saving below \(N^{3/2}\). This is a motivated boundary result for finite-field incidence theory rather than an arbitrary finite example.

**Context inspected:** Rudnev point-plane incidence framework.

**Residual risk:** The probabilistic witness is existential and does not identify the optimal theorem under stronger anti-subfield hypotheses.

## Disposition

PASS. The final claim clears correctness, originality, and value as stated. No change to `RESULT.md` or `SLOGAN.txt` is required.
