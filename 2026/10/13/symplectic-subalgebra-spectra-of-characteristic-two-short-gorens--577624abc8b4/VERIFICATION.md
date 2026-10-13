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

# Reproduction and scope

Use `python3 artifacts/verify.py`; no third-party Python packages are needed. The implementation enumerates actual subspaces, not just a formula or a partial sample. It independently tests product closure in the radical for small finite fields and classifies each closed subspace using its symplectic restriction matrix.

The full subalgebra enumerations over \((m,q)=(1,2),(1,4),(1,8),(2,2),(2,4),(3,2)\) give \(12,28,84,158,2230,5292\) respectively. Full group-orbit traversals are performed for \((1,2),(1,4),(2,2),(3,2)\) using symplectic transvections and basis central shears. The last case has fourteen orbits with sizes \(1,1,1,63,63,126,135,315,315,336,336,1080,1260,1260\). The script prints `VERIFY_OK` upon successful completion.

These are exact finite checks. The theorem for arbitrary \(m\ge1\) and every field of order \(2^e\) is established by the algebraic proof and classical symplectic-space counting arguments. No independent audit or external verification is claimed.
