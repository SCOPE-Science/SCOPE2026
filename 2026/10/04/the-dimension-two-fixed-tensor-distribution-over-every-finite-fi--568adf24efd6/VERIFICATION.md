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
The proof is symbolic and uses the rational-canonical classification of invertible \(2\times2\) matrices.

The packaged checker `artifacts/verify.py` independently constructs
\[
M^T\otimes M^T\otimes M^{-1}-I_8
\]
for every invertible matrix over
\[
\mathbf F_2,\mathbf F_3,\mathbf F_4,\mathbf F_5,\mathbf F_7.
\]
It computes nullities by finite-field Gaussian elimination and compares the resulting histogram with the closed formulas.

The exact checked histograms are
\[
\mathbf F_2:\quad \{2:2,4:3,8:1\},
\]
\[
\mathbf F_3:\quad \{0:27,3:8,4:12,8:1\},
\]
\[
\mathbf F_4:\quad \{0:104,2:20,3:40,4:15,8:1\},
\]
\[
\mathbf F_5:\quad \{0:285,1:60,2:20,3:84,4:30,8:1\},
\]
and
\[
\mathbf F_7:\quad \{0:1519,1:112,2:56,3:272,4:56,8:1\}.
\]

The checker also verifies that each histogram sums to the exact order of the corresponding general linear group and that the weighted Burnside sum equals the classical characteristic-dependent number of two-dimensional algebra isomorphism classes.

The \(\mathbf F_4\) arithmetic is implemented as
\[
\mathbf F_2[t]/(t^2+t+1).
\]

The checker returns `VERIFY_OK`.

Finite enumeration is not used to prove the formulas.
