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

# Reproducibility

Run `python3 verify_cuboctahedral.py` using a standard Python 3 interpreter. No nonstandard dependencies are required. The program enumerates every one of the \(2^{12}\) cube-edge subsets; independently identifies all eight triangles of the line graph as cube stars; generates all 1699 augmented faces and all 49 facets; constructs 847 matching pairs; checks acyclicity on the full 1699-node directed Hasse incidence graph; and computes the critical reduced signed integral boundary \((-1,1,-1,-1)\).

The program also forms independent mod-two simplicial boundaries on every dimension and checks reduced Betti numbers, then computes the alternating signed chain trace on all forty-eight cube automorphisms and checks the rational fifth-homology character against the formula for the sign-twisted signed coordinate representation. `verification_output.txt` is the actual captured stdout from running the program provided in this package.

The proof uses the standard finite acyclic-matching theorem and the classification \(\pi_4(S^4)\cong\mathbb Z\) of 5-cell attachments on a 4-sphere. These conceptual theorems are not inferred from the finite tests. The check addresses this one finite complex and does not certify uniqueness in the literature or independent external scientific validation.
