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

## Reproducible finite checks

From this directory run `python3 verify.py` with Python 3 standard library only. It constructs the finite field as \(\mathbb F_2[t]/(t^8+t^4+t^3+t^2+1)\) and verifies its element \(t\) has order \(255\); the selected seventeenth root is \(\epsilon=t^{15}\). It verifies the \(16\)-element subfield and enumerates all \(2380\) four-subsets of the norm-one group of order \(17\).

The exact zero-count vector for the divided-difference tests, indexed by exponents \(0\) through \(16\), is `(2380,2380,2380,0,0,68,34,0,34,0,0,34,0,34,68,0,0)`. The exact universal-nonzero set is `(3,4,7,9,10,12,15,16)`. Of the \(256\) pairs of nonzero residue exponents, exactly \(16\) meet all four necessary conditions, and they form two symmetry orbits of size \(8\). For the two representatives \((3,6)\) and \((6,8)\), the script directly verifies the distinctness of all four support locations, the nonzeroness and subfield membership of coefficients, and the vanishing of the Fourier sums at all four representative defining-zero frequencies. Terminal marker: `VERIFY_OK`.

The analytic ingredients, including the base distance bound, interpolation formula, subfield coefficient normalization, and coordinate-inversion symmetries, are proved in `RESULT.md`. The script is a finite certificate for the remaining cases, not an oracle for code equivalence or an infinite proof. This result has undergone the recorded self-review only; no independent audit is reported.
