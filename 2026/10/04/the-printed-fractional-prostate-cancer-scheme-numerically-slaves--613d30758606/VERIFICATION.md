---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

The published six-state model defines different androgen and PSA fields H5 and H6, but the printed final PSA recurrence repeats H5 in the same local and history operator used for androgen. Subtracting the two displayed recurrences therefore forces P_n-A_n to equal its initial difference exactly. At the source's integer-order endpoint and the admissible state X1=X2=0, A=a0=10, P=1, u=0 with gamma1=delta3=0.08, an independent exact-rational replay gives H5=0 and H6=-0.08, so the continuous model has derivative of P-A equal to -0.08. The printed invariant is consequently inconsistent with the source vector field, and replacing H5 by H6 in the PSA recurrence is the correct componentwise repair.

## originality

PASS

The motivating article presents the six-component biological model and the fractional numerical scheme, but targeted searches found no published correction of the duplicated H5 in the PSA update. The later author correction to the underlying numerical-method paper repairs a separate finite-sum identity and does not address this prostate-cancer component substitution. Resultary searches using the article identity, PSA/androgen aliases and H5/H6 terminology returned no prior equivalent finding.

## value

PASS

The duplicated field forces a global numerical invariant tying PSA to androgen even though the biological model makes them distinct and an exact admissible state violates that invariant immediately. Because the paper connects its figures to the printed scheme, the correction is directly relevant to reproducibility and interpretation rather than a harmless symbol typo.

The dated certificate retains the supplied scientific assessment, sources and limitations.
