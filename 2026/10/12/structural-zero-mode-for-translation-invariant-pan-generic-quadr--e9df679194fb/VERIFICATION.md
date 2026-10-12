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

The general proof was checked line by line from the two translation-invariance block equations and the cited block factorization. The only computation-dependent part of the claim is the displayed integral example.

`verify.py` checks, using only Python standard-library exact arithmetic:

- \(a=I_4\), \(b=-2I_4\), and the displayed symmetric integral matrix \(c\);
- \(M(u,u)^T=0\);
- \(\Delta=c-I_4\) and \(\Delta u=0\);
- four independent Hadamard eigenvectors with eigenvalues \(0,-4,4,8\);
- exact rational rank \(7\) of the \(8\times8\) block matrix;
- one positive value and one negative value of \(Q\), proving indefiniteness of the witness.

The computation is a witness check only. It does not establish the general theorem by sampling or enumeration.
