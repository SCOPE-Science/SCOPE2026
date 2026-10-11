---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The stationary calculation is correct under the stated frozen-basis, constant-gradient assumptions. With the \(45^\circ\)-rotated SPD family, entrywise SOAP normalization gives \(p=(\kappa+1)/(\kappa+1+2\varepsilon)\) and \(r=(\kappa-1)/(\kappa-1+2\varepsilon)\), so the singular values are \(p+r\) and \(p-r\). Direct algebra gives \(\kappa_2=\kappa+(\kappa^2-1)/(2\varepsilon)\) and \(\sigma_{\min}=4\varepsilon/((\kappa+1+2\varepsilon)(\kappa-1+2\varepsilon))\). In the refreshed eigenbasis the update is diagonal and has condition number \(\kappa(1+\varepsilon)/(\kappa+\varepsilon)\). The angular half-saturation law follows directly from the rotated off-diagonal entry. The assigned verifier independently replays these identities over randomized parameters; the proof itself is exact algebra, not numerical evidence.

## originality

PASS

The defining SOAP paper gives the same rotate-normalize-rotate-back algorithm and explicitly permits an eigenbasis to remain stale between preconditioner refreshes, while the later large-scale paper identifies stale preconditioner statistics as an empirical instability mechanism. Neither inspected primary source states the exact \(2\times2\) stationary singular-value collapse, the closed condition-number law, the half-saturation angle, or the noncommuting angle-regularizer limits. Current Resultary searches found no implication-equivalent same-object theorem.

## value

PASS

Basis-refresh frequency is an explicit SOAP design parameter and has current empirical stability relevance. The theorem isolates a sharp spectral failure mode: arbitrarily small fixed basis error can become nearly rank-one when \(\varepsilon\) is smaller than the induced off-diagonal scale, while a refreshed basis remains well conditioned. The closed condition-number and angular boundary-layer formulas provide a natural diagnostic benchmark rather than an arbitrary toy computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
