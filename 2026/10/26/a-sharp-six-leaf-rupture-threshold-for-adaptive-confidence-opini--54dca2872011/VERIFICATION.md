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
The proof derives a graph-metric Kantorovich–Rubinstein extremal formula and proves its necessity by constructing admissible strictly receptive profiles. For stars it derives the exact edge matrix, its first-step infinity norm, an exact second-power contraction, and the sharp one-step witness. Stationary weighted averaging proves the consensus statement.

Execute `python3 verify.py` with Python 3 and no external modules. The packaged program reported 24,931 recorded exact-rational finite checks passed. These include matrix identities for stars through twenty-five leaves, first-step strict rupture witnesses, sign-pattern tests through nine leaves, and exact stationary-mean invariance. Those tests support but cannot replace the analytical all-degree proof.

Unproved/out-of-scope: full-resolution publication priority; universal necessity without the reciprocal-diameter bound; persistent separation or failure of consensus below the critical reinforcement; directed, asynchronous, or heterogeneous-bound variants. This package has no independent scientific audit.
