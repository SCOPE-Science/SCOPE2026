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

# Reproducibility and limits

Execute `python verify.py` using only the Python 3 standard library. The verifier generates the actual output set for every ternary input word through length nine, reconstructs the 21-state quotient graph and checks all length-six local transitions. It then independently computes the graph determinant by the Newton-trace identities in exact integers and tests the polynomial annihilation of the initial row vector. These finite integer identities justify the full rational generating function for infinitely many lengths. It also verifies the graph's strongly connected structure and one self-loop.

The complete verification output is in `verification_output.txt`; successful execution ends with `VERIFY_OK`. The analytic reason that six-symbol locality extends to arbitrary lengths is the changed-support overlap argument in the proof. Finite samples alone would not suffice. Numerical eigenvalues are used only to approximate the already exactly specified Perron root. There is no independent audit or external mathematical certification.
