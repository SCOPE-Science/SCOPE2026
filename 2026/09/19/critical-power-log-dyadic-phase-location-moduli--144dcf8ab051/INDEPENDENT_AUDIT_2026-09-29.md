# Independent audit — 2026-09-29

Record: `2026/09/19/critical-power-log-dyadic-phase-location-moduli--144dcf8ab051`  
Assigned and audited source tree: `89ea12649db4cc4360e9929e393c308a0e44cd54`  
Audited repository: `SCOPE-Science/SCOPE2026` branch `main`  
Current RESULT.md blob: `765eea3e10d2479a59000dab35805b6a6149f6b7`  
Disposition: **passed**

## Correctness

**independently_supported**. Near an endpoint, f(1-s)~a s log(1/s)^(-kappa) and (sqrt(f))'^2~a/(4s)log(1/s)^(-kappa); the two endpoints and shift d=2r give exactly the stated Hellinger laws, including a r^2 log log(1/r) at kappa=1 and (I/2)r^2 for kappa>1. Endpoint-mass inversion gives the stated quantile scale, and regular variation plus the dyadic harmonic sum yields the displayed Delta constants and the ratio (sqrt(2)-1)sqrt(log 2). For Laplace noise all dyadic gaps equal log 2, so the exact geometric sum gives the stated phase intervals. The phase-averaging identity follows by u=2^t p.

## Originality

**qualified_with_inaccessible_legacy_source**. Wang-Gao introduce the dyadic functional but do not state this alpha=1 slowly varying trichotomy or the Laplace lattice-phase obstruction in the public source summary. Smith's 1985 abstract confirms the classical critical power endpoint and a nonstandard rate, but open-access searches yielded no full text and authorized Oxford retrieval returned no verified PDF; the paper is therefore not claimed as read. This leaves a residual risk for the old Hellinger refinement, but it cannot contain claims about the 2026 dyadic functional.

## Scientific value

**meaningful_critical_refinement_and_efficiency_obstruction**. The result resolves the logarithmic boundary between infinite and finite Fisher information, computes a sharp relative constant for the new multiscale statistic, and shows by an exact regular-model example that the fixed dyadic lattice need not have a single asymptotic efficiency constant.

## Literature and evidence checked

- https://arxiv.org/abs/2609.20749
- https://doi.org/10.1093/biomet/72.1.67
- https://eml.berkeley.edu/wp/mcfadden1007.pdf
## Access note

Smith (1985) was searched through open-access channels first. Authorized Oxford institutional retrieval was then attempted and returned no verified PDF. The full text is not claimed as read.

## Limitations

- No remainder uniform in kappa is proved.
- The finite-Fisher phase profile is not shown nonconstant for every compact-support member.
- Smith (1985) could not be inspected in full after OA and authorized institutional attempts.
- No estimator or optimality theorem is attached to phase averaging.
