# Scientific review — a threefold-oval triangle-area crossover

## Correctness
**PASS.** The global maximum follows from containment in a disk; the threefold oval touches that disk at only three bulges. The fixed-positive-deformation tail comes from six isolated nondegenerate quadratic maxima. The simultaneous scaling is a dimension-two tubular integration around the two components of the circular equilateral-configuration manifold. The curvature condition, exact Hessian coefficients, Jacobian and positive-part phase integral are established in `RESULT.md`. The bundled checker independently tests eigenvalues, local area integrals and the cutoff function. Residual mathematical risk: the finite tests cannot certify an infinite limit; the analytical localization and dominated-convergence argument are controlling.

## Originality
**PASS relative to inspected sources.** Koroleva and Nikitin (arXiv:1301.1360) already prove the circular coefficient and this is credited. Nikitin and Simarova (arXiv:2010.04460) prove a more general fixed **rotation-invariant** circle-kernel result; assumption A1 and Example 5.2 were inspected, not bypassed. The present positive-deformation area kernel depends on absolute orientation, while the simultaneous limit varies the kernel with the threshold. Neither inspected text states the explicit crossover or the sharp rotation-phase cutoff. Related recorded results on small circumradii and triangle moments have different events and sampling spaces. Priority risk remains for less accessible literature; the original method of Gaussian neighborhood volume is not itself claimed new.

## Mathematical value
**PASS.** The third angular harmonic is the lowest-order perturbation matching the three maximizer directions of an equilateral triangle. It naturally resolves the rotational zero mode of the circular geometry. Exact analysis reveals a change of rare-event exponent and a nonanalytic, quantitative crossover between two geometric regimes. The formula can calibrate the near-maximal area statistics of nearly circular convex ovals. It makes no unsupported claim about general curves or maximum-area statistics from growing point samples.

## Limits and evidence
Reproducibility checks: `python verify_trilobe.py` with Python 3, NumPy, SciPy. The scripts confirm finite-difference Hessians for three positive deformations, direct local rare-event integrals at two thresholds each, and the crossover at six phase parameters. The proof is self-contained for the specified family. The 2008 foundational reference could be inspected only via accessible publisher excerpts and is not used to infer full-document noncoverage. Independent external audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
