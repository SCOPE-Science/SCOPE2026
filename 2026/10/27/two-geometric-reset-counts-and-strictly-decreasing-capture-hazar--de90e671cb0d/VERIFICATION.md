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

The analytical argument is self-contained in `RESULT.md`. The included `verify.py` independently discretizes the one-attempt mixed Dirichlet/Neumann backward resolvent, performs exact symbolic two-state matrix calculations, and verifies mixture and moment identities for 1,500 parameter suites. The checker has 24,018 assertion groups. Numerical checks confirm sampled parameter instances and do not establish a theorem for all rates; the proof supplies the global inequalities. Discretization uses a distant Neumann boundary to approximate a bounded half-line solution, with a specified finite tolerance. No external verification has been performed.
