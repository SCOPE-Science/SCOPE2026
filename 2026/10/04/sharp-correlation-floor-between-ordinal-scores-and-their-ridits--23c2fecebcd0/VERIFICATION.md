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

The proof is analytic. The accompanying checker uses exact rational arithmetic for all identities and inequalities before the final display-only square roots.

For random rational probability profiles and strictly increasing rational score vectors it verifies:

- \(\mathbb EQ=1/2\);
- \(\operatorname{Var}(Q)=(1-\sum_i p_i^3)/12\);
- every cut covariance \(\operatorname{Cov}(H_j,Q)=P_j(1-P_j)/2\);
- the strict lower correlation inequality for \(m\ge3\);
- exact correlation one for positive affine ridit scores;
- the equal-mass lower constant;
- convergence of one-dominant-gap score families toward each predicted minimizing cut.

The finite replay is supplementary. The universal result follows from the exact cut decomposition and Hilbert-space triangle inequality.

Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK variance_checks=44000 cut_checks=175354 lower_checks=40827 upper_equality_checks=22000 boundary_checks=18827 equal_mass_checks=98`.
