# Independent Audit — 2026/09/19/gauge-nonidentifiability-nonautonomous-moose-wolf-models--0adfd4c49c72

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `e085128b80a646c4545175b41802a8fc8a83d996`
- Disposition: **PASSED**

## Correctness

**PASS** — The gauge transformation is exact. Direct symbolic substitution into the Holling type-II equations gives zero residual in both state equations; the ratio-dependent formulas follow identically after replacing b+x by by+x. Thus, when alpha(t) and delta(t) are unrestricted unknown functions, any admissible nearby constant triple (A,B,C) can be compensated by new time-dependent rates while preserving the full observed trajectory. Local persistence under the paper's open constant-parameter constraints and a uniform positive margin for delta follows by continuity. The known-alpha repair is also correct: the reciprocal predation term is affine in x for Holling and affine in (x,y) for the ratio-dependent model, so two generic time points determine a,b and known delta then determines c. The record carefully distinguishes nonidentifiability of the underlying functional ODE model from identifiability of a fixed finite neural architecture.

## Originality

**PASS** — General theory already treats time-varying parameters as unknown inputs and supplies abstract identifiability tests, so that general insight is not new. The September 2026 Singh-Kumari source nevertheless explicitly presents a non-autonomous model with temporally varying intrinsic growth and natural death rates and states that structural identifiability was checked before joint estimation of time-dependent and constant parameters. The submitted record supplies explicit three-constant trajectory-preserving gauges for both exact Moose-Wolf functional responses, directly exhibiting the obstruction in this source model. Targeted searches found no prior public correction or the same gauge family for these equations. The source-specific algebraic correction is therefore original enough despite resting on well-known unknown-input principles.

## Scientific value

**PASS** — The result corrects a consequential modeling inference: dense noiseless observation of both populations cannot identify the three interaction constants if two rates are left as unrestricted functions. The explicit gauge makes the ambiguity transparent, shows it survives local positivity constraints, and identifies what extra information can break it. This is scientifically useful for interpreting inverse-model/PINN parameter estimates because it separates structural information in the ODE from representative selection caused by architecture or regularization.

## Sources

- A physics-informed inverse modeling framework for Moose-Wolf dynamics from limited and noisy data in Isle Royale National Park (Anurag Singh; Nitu Kumari): https://arxiv.org/abs/2609.20793 — Primary 2026 source: a non-autonomous prey-predator model with time-varying intrinsic growth and death rates; the abstract states that structural identifiability was analyzed before estimating both time-dependent and constant parameters.
- Identifiability of nonlinear ODE Models with Time-Varying Parameters: the General Analytical Solution and Applications in Viral Dynamics (Agostino Martinelli): https://arxiv.org/abs/2211.13507 — General prior art treating time-varying parameters as unknown inputs and analyzing their identifiability.
- Observability and Structural Identifiability of Nonlinear Biological Systems (Alejandro F. Villaverde): https://doi.org/10.1155/2019/8497093 — General structural-identifiability background for nonlinear biological ODE models.

## Limitations

- The conclusion is for the ODE model with alpha(t), delta(t) treated as unrestricted unknown functions, not for a particular fixed finite neural-network architecture.
- The displayed reconstruction assumes positive states, nonzero denominators, and avoids x=1 where the alpha term vanishes.
- No claim is made about forecast quality, ecological adequacy, or practical regularized identifiability.
- The correction is source-specific and does not constitute a new general identifiability theory.

## Independent checks

```json
{
  "symbolic_holling_residuals": [
    0,
    0
  ],
  "ratio_dependent_algebra_checked": true,
  "source_abstract_identifiability_claim_verified": true,
  "general_unknown_input_prior_art_checked": true,
  "source_tree_unchanged": true
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Open-access/preprint sources were checked first. The scientific conclusions above are independent of the record's same-model review.
