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
The proof was checked from the definitions rather than inferred from computational data. The critical steps are:

- the secure-domination occupancy criterion for \(K_{s,t}\);
- the exact four-block upper construction for \(s=2\);
- the one-shore hub constructions for \(3\le s\le5\);
- the two mixed-hub construction for \(s\ge6\);
- the excess lower bound, including the equality case for a six-vertex shore with no singleton block.

`verify.py` independently enumerates every set partition for all complete bipartite graphs of total order at most \(9\), tests secure domination directly from the defender-exchange definition, and confirms the stated maximum partition order. It also checks the occupancy characterization on \(1110\) profiles and the explicit constructions on all \(820\) profiles with \(1\le s\le t\le40\).

The computation is finite and does not establish the theorem for arbitrary orders. The unrestricted claim is supported by the analytic proof in `RESULT.md`.
