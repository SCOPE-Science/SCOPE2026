# Independent Audit — 2026-09-29

**Record:** `2026/09/18/sharp-recovery-diffusion-threshold-fitzhugh-nagumo-barriers--9fc4488cfb37`  
**Title:** Curvature gives the exact proportional recovery-diffusion threshold for FitzHugh--Nagumo barriers  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `ff58cb21a2f37dd514266f10c0fe09dba06651cb`  
**Disposition:** **PASSED**

## Independent checks

- Checked that negative-curvature points are automatic only after c>1/gamma, explaining the positive-curvature hypothesis.
- Checked interface jump signs are preserved by positive constant proportionality.
- Checked the record does not claim exclusion of nonproportional barriers above D_sharp.

## Three-axis assessment

- **Correctness — PASS**: For W=cV the barrier inequalities reduce exactly to c<=c_* for the activator and delta c V'' <= (gamma c-1)V for recovery. Positive curvature somewhere forces c>1/gamma; on positive-curvature points the latter is equivalent to kappa_delta<=gamma-1/c, and monotonicity in c makes c=c_* optimal. The constant-diffusion threshold and the exponential-tail saturation c_*=1/tilde_gamma then follow directly. The explicit piecewise profile also reproduces the claimed unbounded ratio between the exact proportional threshold and the source sufficient bound.
- **Originality — PASS**: The 2026 source publicly gives persistence under sufficiently small recovery diffusion but not the fixed-profile necessary-and-sufficient proportional criterion. Kajiwara (2018) is genuinely adjacent: its public bibliographic page/abstract introduces a Rayleigh quotient for a heterogeneous FHN subsolution problem. No accessible evidence located the present source-specific c_* / positive-normalized-curvature criterion or its tail saturation. The Kajiwara full article body could not be inspected in this run, so the novelty conclusion is qualified rather than absolute.
- **Scientific Value — PASS**: Within the explicitly delimited proportional family, the result replaces an unspecified small-diffusion condition by a computable exact budget and identifies positive normalized curvature as the only local recovery bottleneck. The tail ceiling and conservatism example make the sharpening practically interpretable without overclaiming a global propagation threshold.

## Findings

- Current source tree exactly matches the assigned SHA.
- Independently reduced all four barrier inequalities to the two scalar constraints and checked the monotonicity argument.
- Independently checked exponential-tail saturation and the piecewise e^x/constant example.
- Kajiwara 2018 was inspected at its lawful public metadata/abstract; no exact overlap was found, but the complete article body was not available through the current retrieval path.

## Sources compared

- Courdurier and Paduro, Propagation failure in heterogeneous FitzHugh--Nagumo systems via coupled upper and lower solutions: https://arxiv.org/abs/2609.14944 — Primary source for the stationary-barrier mechanism and its sufficient small-recovery-diffusion persistence theorem.
- Kajiwara, The sub-supersolution method for the FitzHugh-Nagumo type reaction-diffusion system with heterogeneity: https://doi.org/10.3934/dcds.2018101 — Closest located older work; public abstract introduces a Rayleigh quotient in a related heterogeneous FHN subsolution problem.
- Klaasen and Troy, Stationary wave solutions of a system of reaction-diffusion equations derived from the FitzHugh--Nagumo equations: https://doi.org/10.1137/0144008 — Earlier double-diffusive stationary-wave context, not the source-specific proportional barrier criterion.

## Limitations

- Exactness is only for a fixed V and constant-proportional W=cV; it is not a global dynamical propagation threshold.
- The source paper's nondivergence recovery operator and interface convention are essential.
- The complete Kajiwara 2018 article body was not inspected in this run; only the lawful public article page/abstract was available, leaving a residual originality risk.

This audit is independent of the repository’s pre-existing audit material. GitHub was read only as evidence; no repository changes were made by this audit run.
