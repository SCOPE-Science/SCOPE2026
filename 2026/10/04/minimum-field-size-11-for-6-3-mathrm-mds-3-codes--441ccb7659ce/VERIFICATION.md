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

Using the published projective characterization for \([n,3]\)-\(\mathrm{MDS}(3)\), every six-point ordinary-MDS configuration can be normalized by an ordered projective frame. The inspected verifier constructs each finite field of order below eleven, enumerates all normalized candidate pairs, checks all twenty collinearity determinants and all fifteen perfect-matching concurrence determinants, and exhausts exactly 1502 normalized pairs below eleven with no survivor. Over \(\mathbb F_{11}\) it checks the displayed witness and finds 72 good normalized pairs. The normalization is symmetry-complete, so this is an exhaustive finite proof rather than a sample.

## originality

PASS

The higher-order MDS literature identifies the \((n,3)\)-\(\mathrm{MDS}(3)\) case as the smallest nontrivial one and gives asymptotic field-size lower and upper bounds plus explicit constructions. For \((n,k)=(6,3)\), the general lower bound reaches only a field-size lower bound of five, while the audited exhaustive finite-geometry classification closes the exact threshold at eleven. Current Resultary and targeted searches did not reveal an earlier six-point threshold theorem.

## value

PASS

This is the first length where the order-three condition adds a genuinely new projective constraint in dimension three, and exact small-field thresholds are natural benchmark data for a current coding-theory construction problem. The exhaustive symmetry-reduced proof closes every smaller finite field and gives an explicit minimal witness, so the finite result is mathematically motivated and complete.

The dated certificate retains the supplied scientific assessment, sources and limitations.
