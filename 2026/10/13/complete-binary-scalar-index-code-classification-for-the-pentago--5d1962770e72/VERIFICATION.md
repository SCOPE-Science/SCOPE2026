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

Run `python3 artifacts/verify.py` from the package root. The script is standard-library-only and exactly enumerates the finite domain.

It checks all subspaces of \(\mathbb F_2^5\), obtaining Gaussian-binomial counts \(1,31,155,155,31,1\), and verifies the receiver criterion on every subspace. It independently enumerates all \(1024\) fitting matrices using a different rank routine and subset-XOR span construction. The rank distribution is \(45,537,442\) in ranks \(3,4,5\), and the rank-three matrices generate exactly the same \(20\) optimal row spaces as the subspace route.

The verifier also exhausts the ten dihedral coordinate symmetries, checks four orbits each of size \(5\), verifies stabilizer order \(2\), records representative bases and weight enumerators, and checks the \(3360\) full-rank \(3\times5\) encoding-matrix count.

The verification is finite and exhaustive for the stated scalar binary problem. It does not test nonlinear, vector, or asymptotic index codes.
