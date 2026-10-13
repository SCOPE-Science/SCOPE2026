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

# Finite reproduction and limitations

Run `python3 verify.py` with Python 3.9 or later, standard library only. Its output should match `verify_output.txt` byte for byte. The program reconstructs each Mycielskian from its defining edges, performs independent breadth-first searches from every vertex, enumerates every subset for \(n=2,3,4,5,6,7,8\), directly rejects subsets containing a triple on any shortest path, and compares counts to the claimed formula. The number of enumerated subsets is \(174752\). It also checks the exact integer coefficients and strict log-concavity for each \(2\le n\le250\).

The graph-distance calculations and subset enumeration are independent of the graph-structural counting argument. The latter, and the infinite log-concavity inequalities, are established in the written proof, not by extrapolating the finite checks. The program does not assert real-rootedness or generality beyond Mycielskians of complete graphs.
