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

# Reproduction and limits

Execute `python3 verify_all.py` in the directory containing that file. Python 3 standard library is the only dependency. Compare terminal output to `verification_output.txt`.

The program rebuilds each equal-arm spider from its defining edges, computes shortest-path distances, and checks all off-diagonal positions of the polynomial in the adjacency matrix against the exact graph-power adjacency relation. It checks numerical eigenvector residuals using each of the first \(k\) path modes on independent differences of arms, and independently simulates the explicit initial zero forcing set. Its 108 parameter instances include the three exceptional arm-length cases and selected longer-arm values. Five small cases enumerate all subsets of one fewer vertex than the claimed zero forcing number; their total of 91,793 candidates contained no zero forcing set.

This is a floating-point finite check with tolerances, not a certificate for every parameter. The analytical argument in `RESULT.md` derives strict nonvanishing from sign-consistent walk sums or exact four-term expansions, and proves all-parameter kernel multiplicities from distinct sine modes. The previously published forcing upper bound is reproduced with an explicit forcing sequence. The exact theorem and its range are mathematical, not computational extrapolations. Independent external validation has not been performed.
