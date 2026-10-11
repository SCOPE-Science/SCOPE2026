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

For p>=2, choose in each nonzero coordinate a vector of the same norm orthogonal to x_gamma; both distances are exactly sqrt(2). For p<=2, every fixed ell_p vector has coordinates of arbitrarily small norm, so placing a unit orthogonal vector in such a coordinate yields both distances tending to 2^(1/p). The one-coordinate base vector gives the matching upper bound: one sign has first-fibre norm at most sqrt(1+a^2), and monotonicity of (1+a^2)^(p/2)-a^p yields 2^(1/p) below p=2 and sqrt(2) above it. All quantifiers and p=2 boundary check out.

## originality

PASS

Full primary inspection of the paper defining s(X) shows only the Hilbert base value and qualitative sum restrictions; checked vector-valued literature is qualitative, and no exact sequence-space formula was found.

## value

PASS

The exact formula shows a genuine vector-valued effect above p=2, where Hilbert fibres raise the index to sqrt(2), and gives the sharp infinite-coordinate limit below p=2. It is a natural structural classification of the invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
