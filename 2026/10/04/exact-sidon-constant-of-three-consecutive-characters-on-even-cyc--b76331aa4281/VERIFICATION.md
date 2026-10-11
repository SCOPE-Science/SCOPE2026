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

The upper bound follows from pairing the grid samples at \(k\) and \(k+N/2\), the parallelogram identity, nearest-root alignment of the outer coefficients, and one weighted Cauchy--Schwarz inequality. Equality is attained by the explicit phase choice in RESULT.md, for which the outer sum and middle term are orthogonal at every phase and the grid maximum is exact. I independently evaluated the extremizer at representative even orders and obtained the stated constant; the infinite proof is analytic, not numerical.

## originality

PASS

Neuwirth's exact theorem for three integer frequencies uses the supremum over the continuous circle and gives \(\sqrt2\) for \(\{0,1,2\}\). The finite cyclic problem samples only N roots and has a strictly larger residue-dependent value. Graham's whole-group Sidon constant is a different invariant. No prior finite-grid formula was found.

## value

PASS

The theorem exactly quantifies the finite-sampling penalty relative to a classical continuous Sidon constant for every even cyclic order, with an explicit extremizer and asymptotic limit. This is a natural all-parameter harmonic-analysis invariant, not an arbitrary finite instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
