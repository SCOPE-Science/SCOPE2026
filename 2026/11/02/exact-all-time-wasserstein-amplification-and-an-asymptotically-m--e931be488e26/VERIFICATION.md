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

# Computational verification and limitations

Run `python verifier.py` with Python 3, NumPy and SciPy. A successful execution prints `VERIFICATION_OK 254 independent LP/heat/predicted-edge/peak/asymptotic checks`.

The program constructs complete graph edges and the unique bridge, computes graph shortest paths by breadth-first search, constructs the Markov generator directly from those edges, and compares independent matrix-exponential transport laws obtained by an optimal-transport linear-program solver with the claimed closed formulas. It tests all graph-edge orbits for six sizes and seven times, plus the shape of the peak and large-size expansions. Solver tolerances and finite sampling are explicitly distinguished from the analytical theorem. In particular, finite numerical agreement is not proof of all-time ordering or asymptotics. Independent audit: not performed.
