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

The proof uses the exact full-text identities
\[
\mathcal S_WT_W=T_I\mathcal S_W
\]
and
\[
\mathcal S_W\Omega_{BB}(H)=\Omega_{BB}(H).
\]
The matched product norm is defined so that \(\mathcal S_W\) is an isometry. This converts the source's conjugacy into equality of every finite-horizon normalized gain ratio and therefore equality of the corresponding suprema.

`artifacts/verify_matched_bb_conjugacy.py` checks this identity numerically for representative diagonal positive-definite Hessians, several positive spectral weights, compatible starting states, and multiple horizons. It also verifies the weighted and transformed BB steps agree.

The computation is finite and does not prove the all-horizon statement. The theorem is proved by the exact conjugacy and cone bijection. Iteration-dependent weights, nonlinear objectives, and comparison in a single common Euclidean norm are outside scope.
