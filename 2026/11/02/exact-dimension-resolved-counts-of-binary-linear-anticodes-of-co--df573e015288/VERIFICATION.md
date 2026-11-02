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
# Finite checks and scope

`count_anticodes.py` computes the exact finite Gaussian–Möbius formula using integer products, and exhaustively enumerates each reduced-row-echelon parity-check subspace for every \(n\in\{2,3,4,5,6,7,8\}\) and \(1\le r\le n\), checking the syndromes of the \(n+1\) excluded high-weight words. Its recorded output ends `ALL CHECKS PASS`.

`count_anticodes_direct.py` independently enumerates the candidate linear subspaces by generator matrices for every \(n\in\{2,3,4,5,6,7\}\), then explicitly constructs the entire subspace and tests the maximum Hamming weight. It calls the formula evaluator only for numerical comparison, not for generating or testing the candidate codes. Its recorded output ends `DIRECT WEIGHT CHECKS PASS`.

The exact row-reduced enumeration is finite and covers only the specified lengths. The analytic proof establishes the unrestricted statement. The derived leading-term asymptotic is for fixed codimension \(r\ge2\). The verification does not certify originality, external reproducibility, or independent mathematical validation.
