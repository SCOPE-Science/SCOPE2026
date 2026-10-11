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

Fresh exact enumeration of all 64 ambient words reproduces the pointwise certificate: for every word x, the sum of the stated received-word weights over its two-deletion descendants, plus the 2/5 endpoint correction for 000000 or 111111, is at least one. The eight weights sum to 16/5, so any list-size-two code has size at most 2(16/5)+4/5=36/5<8. Independently, the seven displayed codewords have maximum received-word multiplicity exactly two. This proves the upper bound and attainment without extrapolating from finite experiments.

## originality

PASS

Best-of-knowledge originality passes for the exact finite value. Lin's recent paper establishes asymptotic lower bounds for list-decodable deletion codes and explicitly highlights the 2-list, 2-deletion regime, but the accessible primary material does not state the length-six optimum. Exact-value searches returned no independent prior finite theorem. The complete Lin body could not be retrieved through the open routes used in this run, and the single authorized institutional fallback returned a transport-level unavailable/request-invalid error, so a hidden finite example remains an explicit residual risk rather than being declared absent.

## value

PASS

This is a natural first exact finite benchmark in the recently studied 2-list, 2-deletion regime. The short rational dual certificate and explicit extremizer provide a reusable test instance for future finite and asymptotic methods rather than an arbitrary isolated computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
