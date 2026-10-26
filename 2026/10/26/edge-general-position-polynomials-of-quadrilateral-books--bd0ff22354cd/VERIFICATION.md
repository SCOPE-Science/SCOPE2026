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

# Reproduction notes

Run `python3 verify.py` in a directory containing that standalone script. It uses the Python standard library only. The expected console output is included verbatim in `verify_output.txt`.

The graph is built from the specified spine and three page-edge types. For each pair of vertices, the verifier first computes breadth-first distances and then constructs all distance-monotone shortest paths, extracting every selected-edge triple contained in a geodesic. It enumerates every edge subset for \(1\le r\le5\), independently of the symbolic counting argument. A separate routine evaluates the displayed binomial-sum polynomial. A third routine enumerates the structural \(A,B,C\) configurations under their necessary-and-sufficient conditions for \(1\le r\le6\). All three procedures agree where their ranges overlap. The integer total-count formula and extremizer multiplicities are also checked for these finite sizes.

Geodesic brute force is not attempted beyond five pages, and the finite calculations do not certify the claimed identities for every \(r\). The general proof is the mathematical argument in `RESULT.md`; the script provides reproducible sanity checks, including small boundary cases, without relying on any external solver or network access.
