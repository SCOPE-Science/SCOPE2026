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

# Reproducible checks

Run `python3 verify.py` from the extracted package directory. The script uses only the Python standard library and prints `VERIFY_OK` after its assertions.

The script independently generates every \(n\times n\) matrix over \(\mathbb F_p\), for the tested prime fields \(p=2,3\), at dimensions \(n=2,3\), and \(p=2,n=4\). It selects those with \(A^2=0\), computes the induced exterior-square matrix \(T_A\), and independently determines the dimension of the solution space \(T_AB+BA=0\) by row reduction. Rank-by-rank counts and Hom dimensions are compared with the asserted Gaussian-binomial identities, and total weighted sums are compared. Boundary checks at \(n=2\) test the method but are not part of the stated theorem.

Expected principal totals: \(N_3(2)=1184\), \(N_3(3)=44955\), and \(N_4(2)=19357696\). The \(n=4,p=2\) matrix search covers all \(65536\) matrices \(A\), not all corresponding \(B\); the linear-kernel check supplies each fiber dimension. This finite computation independently checks selected instances, but the proof of all finite fields and arbitrary rank is the written argument in `RESULT.md`. No external or independent audit was performed.
