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

Run `python3 verify.py` using a standard Python 3 interpreter, and compare its output against `CHECK_RESULT.txt`. No downloaded data or third-party dependencies are needed. The program enumerates all spin configurations and tests every fixed magnetization in five explicitly constructed bipartite graph examples, for four positive coupling pairs. It compares exact Hamiltonian energies with the symbolic formula, tests field-transition sectors and exact matching counts via two different finite algorithms, and checks two nonisomorphic connected cubic matching degeneracies.

The reported result is 20 complete Ising enumerations and 204 fixed-magnetization sectors, with matching degeneracies 1104 and 1092 for two connected cubic examples. The exact all-graph theorem uses a separately stated integral-circulation proof. The numerical/finite certificates cannot by themselves prove infinitely many graph cases; no independent scientific audit has occurred.
