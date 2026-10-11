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

The symbolic proof has two independent checkpoints.

First, \(|\Delta_K(1)|=1\) implies that \(I-\bar h_*\) is invertible over \(\mathbf F_2\). Under the even-subset model of \(H_1(\Sigma_2;\mathbf F_2)\), a nonzero fixed class exists exactly when a nonempty proper union of Weierstrass cycles has even cardinality. The only partitions of six avoiding such a union are \((6)\), \((5,1)\), and \((3,3)\).

Second, for cycle lengths \(\ell_j\), the characteristic polynomial on the four-dimensional quotient is
\[
\frac{\prod_j(t^{\ell_j}-1)}{(t-1)^2}.
\]
This gives \(t^4+t^3+t^2+t+1\) for \((5,1)\) and \(t^4+t^2+1\) for both \((6)\) and \((3,3)\).

The included script `artifacts/verify_branch_partitions.py` exhausts all \(720\) permutations of six points and reconstructs their induced four-dimensional actions. It verifies exactly the three fixed-point-free types and the two characteristic polynomials. Its successful output is:

`VERIFY_OK allowed_types=(6),(5,1),(3,3) counts=120,144,40 total=304`

`CHAR_OK (5,1)=t^4+t^3+t^2+t+1; (6),(3,3)=t^4+t^2+1`

The permutation counts are verification data only; they are not counts of knots or realizability statements. No claim is made that all three permitted branch patterns occur for actual genus-two fibered knots.
