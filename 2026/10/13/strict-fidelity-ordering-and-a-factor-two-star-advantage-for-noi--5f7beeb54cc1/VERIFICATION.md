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

# Reproducible checks and their limits

Run `python3 verify.py` from this directory. Python 3.10 or newer and no third-party packages are required. The script independently constructs stabilizer supports using bit masks of the explicit complete-bipartite adjacency graph and sums exact rational Pauli expectations. It cross-checks the closed expression over total orders \(2\)–\(11\), five rational channel strengths, and every split. It tests strict partition ordering for \(4\le n\le59\) at four rational strengths, the known star/GHZ formula, two exact four-qubit values, and large-order convergence at rational strengths. The run printed `VERIFY_OK 3612`.

The exact proof does not depend on the finite tests. In particular, the full family of integers \(n\ge4\) and all real \(0<q<1\) is established analytically by a strict factor bound, rather than inferred from sampling. The numerical large-order tests are only sanity checks for the proved limit. No independent audit has been performed.
