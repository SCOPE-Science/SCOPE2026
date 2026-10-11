---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Exact elimination gives \(y=x\), \(z=x^2/c\), \(w=dx^3\), and the single condition \(x[(b-1)+(d-1/c)x^2]=0\). This yields the complete case split, including the singular locus \(dc=1\). At the source parameters \(R=-144\). Direct symbolic reconstruction of the origin Jacobian factors its characteristic polynomial by \((\lambda-1)\), so the universal linear instability is exact. The packaged rational checker was inspected but is only corroborative.

## originality

PASS

The source paper itself contains an internal inconsistency: it calls the entire parametrized curve an equilibrium curve, yet its later sign test says the showcased negative-ratio parameters have only one equilibrium, and its displayed nonzero coordinates omit the required square roots. The audited theorem resolves this inconsistency, supplies the omitted singular parameter locus, and adds the universal eigenvalue-one statement. Targeted Resultary and public-literature searches located the source and unrelated equilibrium corrections, but no prior correction of this system.

## value

PASS

This is a complete correction of a published equilibrium geometry used in subsequent local-stability discussion. It identifies exactly when the advertised continuum actually exists and prevents applying a curve-based stability argument at parameters where no such curve is present.

The dated certificate retains the supplied scientific assessment, sources and limitations.
