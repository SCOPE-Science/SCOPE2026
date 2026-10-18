---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For every coprime 1≤p<q≤65, the normalized toric surface Nash blowup is computed by the Hilbert basis, consecutive adjacent sums, essential vertices of C+conv(sums), and primitive tangent cone normalizations using the cited exact 2D fan theorem. The Hilbert basis rectangle enumeration is exhaustive by the fundamental parallelogram decomposition, not mere sampling. The recursion is finite for the checked states, and all 1307 primitive representatives occur. Independently implemented Hilbert-basis/fan recursion and regenerated every depth: all 1307 agree with the complete artifact CSV, maxima ceil(log2 q) uniquely at p=q−1 for each q=2..65. Depth-seven first occurs q=65, with explicit seven-step chain (64,65)→(63,65)→(31,33)→(15,17)→(7,9)→(3,5)→(1,3)→(0,1). The range q>65 is unproved.

## originality

PASS

The full Atanasov et al primary paper supplies the exact normalized Nash fan construction and termination. It does not state the checked finite indexed depth table or unique maximizer for q≤65. The 2025–26 computational Nash literature distinguishes ordinary non-normalized surface blowup from the normalized iteration here; its complete later manuscript was not retrieved.

## value

PASS

The first determinant requiring seven normalized Nash rounds at 65 is an intrinsically motivated sharp finite complexity threshold, coupled to a complete primitive-cone classification rather than an arbitrary finite list; this does not claim the all-index trend.

The dated certificate retains the supplied scientific assessment, sources and limitations.
