---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The positive ODE has negative homogeneous trace and positive determinant, so the calibrated limiting complex response is well defined. Eliminating the deep layer gives impedance Z(s)=λ+Cs+γτs/(1+τs), with τ=C_D/γ. Independently, write (1+τs)Z(s)=P_0+P_1s+P_2s². At the two positive frequencies the imaginary equations divided by frequency read J_j+τR_j=P_1, giving τ=b/a, while the real equations read R_j−ω_j²τJ_j=P_0−ω_j²P_2; these uniquely determine λ=P_0 and C=P_2/τ. The forward differences give a=γτ²(ω₂²−ω₁²)/[(1+ω₁²τ²)(1+ω₂²τ²)], so a,b>0 are necessary and ensure positive τ,γ,C_D in the reconstruction. The two remaining inequalities are exactly C>0 and λ>0; together these conditions reproduce all four real equations and hence the original nonzero phasors. For example, ω=(1,2), Z=(1+i,2) has a=b=1 yet reconstructs C=λ=−2/3, demonstrating the need for the last tests. At one tone fixing R,J permits freely varying τ,γ near any positive solution and reconstructing C,λ continuously; fixing DC determines λ and then γ from τ, leaving one local degree of freedom. The stated perturbation inequality follows from |Δa|≤2ε_R and |Δb|≤2ε_J and needs no assumption about raw-temperature errors; even when the ratio is positive, C and λ still need checking. The rational witness in RESULT.md line 82 is exact and its two inverse phasors agree with direct substitution. Frozen verify.py is a supplementary finite replay (inspected, not executed); the witness is checked there in floating point despite being specified rationally, and the final commented negative-data case actually rechecks a positive case. Neither limitation undermines the algebraic certificate or the independent negative example above. The proof is only for this constant positive model with known forcing magnitude and phase, two distinct positive frequencies, and finite nonzero complex response ratios.

## originality

PASS

The transfer model, its analog passive network and the rational-interpolation uniqueness principle are prior or standard and are not credited as new. The supported distinct result is the explicit strict feasibility test directly in two calibrated phasors, with closed reconstruction, one-tone-plus-DC sharpness throughout the positive region, and the stated contrast-based bound. No inspected statement covers that package or the explicit feasible data set. This is a bounded comparison, particularly because two historical papers were not fully accessible.

## value

PASS

At the minimum number of measured harmonics, the strict inequalities decide whether the data have a positive fit at all, rather than merely fitting a rational function or estimating four parameters from four numbers. This yields a test directly in calibrated observations, states why even an equilibrium measurement cannot replace a second tone, and identifies the contrast controlling noise amplification of τ. It is practically interpretable within the model; it does not assert robustness to model error, noisy uncalibrated observations, or validity for the real climate system.

The dated certificate retains the supplied scientific assessment, sources and limitations.
