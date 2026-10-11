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

The identity \(X(H)=0\) follows by differentiating \(H=xz-y^2/2+x|x|^q y\), using \((x|x|^q)'=(q+1)|x|^q\). The divergence is \(-|x|^q\), and the level change \(w=z+|x|^q y\) converts \(H=-h\) to \(V^2+2y^2-U^2=4h\). The coarea/Liouville identity and Stokes establish uniqueness without finite enumeration. The multiplier equation follows from the surface Liouville formula, while the scaling is checked term by term. Poincaré–Bendixson is used only on compact omega limits of bounded trajectories.

To replay the finite algebraic sanity checks, install the dependency in `requirements.txt` and run `python check_chazy.py`; the expected final output is `CHECK_OK`. The program checks both signs of the coordinate, several parameter values, conservation/divergence, and the scaling covariance. It cannot certify the general topological argument, an infinite parameter family by enumeration, or publication priority.

The 2023 primary source's Theorem 1 analytically supplies existence for \(q=2,3\). Its extension through \(q=100\) is a separately stated computational corollary, not a computation repeated here. The inaccessible relevant 2024 full text is a priority limitation. Independent audit has not been performed.
