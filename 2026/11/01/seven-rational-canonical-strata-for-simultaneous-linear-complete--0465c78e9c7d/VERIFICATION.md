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

# Reproducibility and scope

Run `python verify.py` using Python 3.10 or later; no packages are required. The program enumerates all invertible \(2\times2\) matrices as possible relative automorphisms and all possible linear mates for \(q=2,3,4,5\). Its finite-field implementation directly computes operations in the prime fields and in \(\mathbb F_4=\mathbb F_2[z]/(z^2+z+1)\).

The checker compares brute-force determinants with the exact formula using projective invariant lines, and separately verifies the seven rational-canonical multiplicity formulas. In all four fields the program terminates with `VERIFY_OK`. This is an exhaustive check in those four fields only. The result for all prime powers follows from the symbolic proof in `RESULT.md`, and the test code is not an external certificate or independent audit.
