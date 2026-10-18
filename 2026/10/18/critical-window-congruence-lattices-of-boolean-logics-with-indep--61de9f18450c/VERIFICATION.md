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
The included `artifacts/verify.py` uses Python 3 standard library only. Run `python3 artifacts/verify.py` after extracting the file. It exhausts every ordered tuple of maps for Boolean algebras of two and three atoms with one and two negations, and checks congruence compatibility directly from the unary operation truth tables against the graph support condition. It also exhausts the corresponding occupancy factorial-moment identities. Additional fixed-seed small finite graph probes are diagnostic only. None of those finite tests proves convergence for unbounded \(n\); the unrestricted convergence proof is in RESULT.md. Independent audit is not performed.
