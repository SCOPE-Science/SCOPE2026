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

The claim is verified analytically and by the accompanying exact-arithmetic script.

The exact checks are:

1. The four squared amplitudes sum to \(58\).
2. The Schmidt purity across \(A_1A_2:B_1B_2\) is \(737/1682\).
3. The direct-pair coherences give concurrence \(24/29\) for both \(A_1B_1\) and \(A_2B_2\).
4. The order-\(2\) two-qubit Rényi factor is \(553/841\).
5. The strong-superadditivity residual is \(\log_2(611618/619817)\), and \(611618<619817\).
6. The two cross-pair reductions are diagonal because their traced-out labels are pairwise distinct.

Running `python verify.py` from the package directory prints `VERIFY_OK`.

The script does not establish uniqueness, global optimality, or statements for Rényi orders other than \(2\). Those are outside the claim.
