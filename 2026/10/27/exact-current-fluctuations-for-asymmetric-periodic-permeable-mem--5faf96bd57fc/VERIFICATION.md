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

# Verification record

Run `python verify.py` with SymPy, NumPy and SciPy installed. Its exact calculations reconstruct the first two derivatives of the entire scalar function defining the tilted eigenvalue and assert an identically zero difference with the main text's transport formula. They also algebraically check the stated expression for the discrepancy from the primary article's printed equation (26).

The one-way renewal calculation is independent: for unit cell length, unit bulk diffusivity and unit forward permeability, the reflecting-to-Robin crossing transform is \(1/[\cosh\sqrt{s}+\sqrt{s}\sinh\sqrt{s}]\); its first terms give \(\mathbb ET=3/2\) and \(\operatorname{Var}(T)=11/6\). The renewal central limit relation gives \(22/81\), while direct substitution into the printed formula gives \(43/162\). An eigenvalue approximation uses finite reversible interior diffusion and tilted right/left membrane jumps, and checks convergence towards the root at a nonzero counting tilt.

This exact-symbolic/finite-dimensional verification is internal consistency evidence, not independent certification. The proof of the continuum SCGF and large deviations relies on the analytic compact-semigroup argument in `RESULT.md`, not on finite numerical enumeration. Earlier symmetric and related literature does not establish an exhaustive novelty guarantee.
