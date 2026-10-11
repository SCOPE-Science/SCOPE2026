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

The proof has four logically separate components.

First, the two order-continuity identities imply Hausdorff continuity of the nested compact family. The left-limit argument uses compact finite approximation of the increasing union; the right-limit argument uses compactness and the decreasing-intersection identity.

Second, centers of compact centrally symmetric sets are continuous under Hausdorff convergence. Any subsequential center limit is a symmetry center of the limit set, and bounded central symmetry has a unique center.

Third, the finite vector-rounding lemma is exact. Starting with coefficients \(1/2\), nullspace moves preserve the represented vector while reducing the number of fractional coefficients to at most \(d\). Rounding those final coefficients costs at most
\[
\frac d2\max_i\|v_i\|.
\]
The packaged checker performs this reduction with rational arithmetic on several nontrivial families.

Fourth, two central reflections satisfy
\[
R_b(R_a(x))
=
x+2(b-a).
\]
Thus selected center increments can be realized by legal symmetry operations while remaining inside the nested family. The rounding error tends to zero because center continuity makes the maximum increment tend to zero.

The universal theorem is proved analytically; finite computation is used only to replay the algebraic certificates.
