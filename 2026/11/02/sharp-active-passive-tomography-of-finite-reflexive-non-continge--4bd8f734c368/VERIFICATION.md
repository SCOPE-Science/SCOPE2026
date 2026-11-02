---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

Run `python3 checker.py` from the directory containing the standalone checker. The script uses only Python's standard library. It checks direct truth-table semantics instead of substituting the proposed formulas as axioms: it enumerates every directed relation on one to three worlds, every reflexive relation on one to four worlds, and all query-family subsets up to four worlds. It tests the exact adaptive-adversary distinguishability calculation for sizes three through seven, reconstructs 1,200 pseudorandom five-world reflexive relations, and independently counts short uniform-query sequences against the inclusion–exclusion expression. A successful execution ends with `ALL_CHECKS_OK`.

The universal claims are supported by the complete written proof: singleton-query edge reconstruction, the universal/one-deleted-edge adversary, the decision-tree transcript argument, and elementary factorial moments for the random-query law. The checker does not purport to enumerate infinitely many frame sizes or prove asymptotics by computation. Formal proof-assistant certification and independent audit have not been performed.
