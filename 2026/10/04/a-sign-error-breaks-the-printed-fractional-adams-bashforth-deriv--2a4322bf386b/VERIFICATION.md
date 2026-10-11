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

The two consecutive Caputo-Volterra identities differ by subtraction, so the earlier-time history integral must enter with a minus sign. The source instead prints a plus sign in equation (4.5). For constant forcing, exact integration gives the true increment proportional to \(((v+1)^h-v^h)\) and the printed increment proportional to \(((v+1)^h+v^h)\); at \(h=1,v=1,\Delta=1\) these are 1 and 3. An independent replay of the fixed-horizon printed recurrence for \(h=1,0.7,0.3\) shows growth proportional to \(1/\Delta\), while the exact terminal value is finite.

## originality

PASS

Best-of-knowledge searches and direct source reading found the source-specific sign error but no published erratum or prior correction. Standard fractional Adams theory supplies the correct nonlocal-history baseline, not this article-specific equation correction or its constant-forcing divergence certificate.

## value

PASS

The defect occurs before the discretization approximation and makes the printed parent recurrence inconsistent even for constant forcing, so it materially changes what the numerical derivation can support. Distinguishing the invalid printed scheme from an unknown implementation is a useful reproducibility correction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
