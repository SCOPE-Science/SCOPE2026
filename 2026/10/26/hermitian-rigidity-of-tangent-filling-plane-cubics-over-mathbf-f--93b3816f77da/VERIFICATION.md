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

# Reproduction

From this package directory, execute `sh scripts/verify.sh` using a C++17 compiler and Python 3 with NumPy. The programs use only exact arithmetic in \(\mathbf F_4=\mathbf F_2[\alpha]/(\alpha^2+\alpha+1)\). No network or third-party database is needed to rerun the finite calculations. The raw line-separated file `tangent_noline_codes.txt` contains the 280 normalized cubics and is recreated by both incidence implementations; the two code lists are compared byte-for-byte by `cmp`.

The expected complete counts are 349525 normalized cubics; 11368 tangent-filling; 11088 of those with a rational line factor and 280 without one. Geometric smoothness is checked by exact row-reduction on the Jacobian-quadrics-to-quartics matrix: ranks 11 (5040 cubics), 13 (6048), and 15 (280). The invertible-matrix enumeration gives \(|\operatorname{GL}_3(\mathbf F_4)|=181440\), Hermitian stabilizer size 648 in \(\operatorname{GL}_3\), hence stabilizer size 216 in \(\operatorname{PGL}_3\) and orbit size 280. The generated orbit equals the 280 no-line cubics and the 280 geometrically smooth tangent-filling cubics. Full program output is included as `verification_output.txt`.

# Limits

The verification is exhaustive only for ternary homogeneous cubics over \(\mathbf F_4\), including their 21 rational projective points, 21 rational lines, and rational change-of-coordinate matrices. It does not by itself establish publication priority. No independent audit or formal certification has been performed.
