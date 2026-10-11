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

Reid--Tai on the two heavy charts gives exactly \(0\le d=b-a\le r,\ 1\le a\le r+d\) in the canonical case and the strict inequalities in the terminal case. The standard weighted-projective volume is \((r+a+b)^{r+1}/(ab)\). For fixed \(d\), the logarithmic derivative has one positive zero, so the maximum on the allowed \(a\)-interval is at an endpoint; the submitted derivative calculations then make the outer endpoint monotone in \(d\), while the lower endpoint is strictly smaller except for the stated canonical \(r=2\) tie. I independently enumerated the exact rational feasible regions for \(2\le r\le40\), reproducing every formula and equality case; this is corroboration, not the infinite proof.

## originality

PASS

Kasprzyk gives general canonical/terminal weight restrictions and Bäuerle gives sharp anticanonical-degree bounds with dimension and Gorenstein index as parameters. The published same-family SCOPE triangular classification supplies the feasible parameter triangle but not a volume optimization. None of the inspected stronger/general statements determines these unrestricted two-heavy extrema or their equality cases.

## value

PASS

Anticanonical volume is a central Fano invariant. The theorem gives a complete all-dimensional extremal law with exact equality cases on a natural infinite family, including a genuine low-dimensional tie, rather than a finite census or normalization check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
