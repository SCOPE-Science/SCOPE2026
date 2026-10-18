# Scientific review

## Correctness — PASS

The seasonal exponential is an exact nilpotent shear times common exponential recovery. The proof treats all dimensions \(n\ge2\), permutations, arbitrary positive individual exposures and all strict Floquet regimes. An eigenvector-component recurrence, justified in both directions, yields the monic characteristic polynomial for generic parameters; continuity handles exceptional multiplicity. Primitivity gives a simple positive Perron eigenvalue. The monotonicity of the defining scalar root gives the strict threshold ranking and the special cases at \(n=2\) and \(n=3\). The averaged-versus-ordered counterexample is exact and uses rational comparisons. The standalone checker reproduced all 152 permutation polynomials through dimension five using rational arithmetic. Finite checks do not supply the general proof.

## Originality — PASS with bounded literature risk

Qu and Ashwath, arXiv:2609.13668, analyze reproduction-number shapes for compartmental models, but their cyclic case is disease relapse rather than time ordering of directed host contacts. Valdano et al. (2015) already give general temporal infection-propagator threshold methods, and Valdano, Colombi, Poletto and Colizza (2023) explicitly give the time-ordered matrix exponential and spectral threshold. These older general statements are not claimed as new. The result instead gives the exact polynomial \((\lambda-1)^n-P\lambda^k\), the reduction to the cyclic ascent of a permutation, and sharp opposite seasonal-order outcomes with identical mean contact rates. Relevant accessible research records on seasonal SIR and population-pulse ordering address different state models and do not imply this particular polynomial. The older 2015 article was consulted at abstract level, not full text; a published elementary-matrix product result or a hidden specialization of the general epidemic threshold framework could subsume the exact result. No search proves absolute novelty.

## Mathematical value — PASS

Chronological network data can change disease-free invasion even when all seasonal generators and their arithmetic average are stable. The theorem gives a complete, dimension-independent classification using only a cyclic ascent statistic and the product of exposure strengths, making the sharp three-population example reproducible rather than anecdotal. The difference starts at three groups, and the exact stability thresholds can be used to test approximations based on time-averaged contact data. This value comes from the sharp structural classification and quantitative reversal, not from the already-known existence of spectral Floquet thresholds.

## Limitations and closest literature

The equal recovery and exclusive one-link seasonal assumptions are essential to the exact shear reduction. Nothing is claimed about nonlinear global attraction or stochastic epidemic outcomes. The directly inspected open research contains the general time-ordering framework but not the cyclic-ascent formula. Review of the earlier 2015 threshold paper was restricted to the accessible public abstract, and broad older matrix-product coverage cannot be excluded.

Self-review: passed. Independent audit: not yet performed.
