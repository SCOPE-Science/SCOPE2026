# Scientific review

## Correctness — PASS

The Hessian normalization is invertible for both diagonal entries positive; positive definiteness forces \(0\le c<1\). Each update is an exact linear map, so the four replacement paths and two permutation paths exhaust their respective laws. The two generalized Rayleigh quotients of the expectation-matrix difference have been reconstructed and checked symbolically. Their common positive factor and the two sign factors prove the universal quantifiers, the equality case, and both reverse witnesses. The exact worst-case example uses simultaneous diagonalization and rational fractions, not a floating-point optimization. Exact energy decrement proves individual-update monotonicity. No multiepoch assertion is inferred.

## Originality — PASS with residual risks

Recht and Ré, arXiv:1202.4184, Section 3.1, treat positive-semidefinite matrix-product factors and two-factor norm inequalities, but do not imply a sharp statewise energy comparison for overrelaxed coordinate maps with negative nontrivial eigenvalues. Oswald and Zhou, arXiv:1510.04727, Sections 1 and 3, treat shuffled SOR convergence estimates but not the exact two-variable comparison with independent replacement draws. Sun–Luo–Ye, arXiv:1503.06387, treat randomly permuted coordinate descent through expected operators, and Gürbüzbalaban–Ozdaglar–Vanli–Wright, arXiv:1803.08200, treat exact coordinate minimization, not the overrelaxation reversal. The closest accessible literature gives the framework but does not imply the computed sharp threshold. Residual risk: a specialized historical two-coordinate SOR comparison not retrieved could be equivalent.

## Value — PASS

The result is a complete, exact ordering comparison for a basic relaxation method, identifying the largest stepsize interval where reshuffling is uniformly preferable and a precise regime of opposing initial-state preferences. The limiting value has structural meaning: \(\omega(1+c)=2\) is also the nonexpansion threshold of the simultaneous normalized-gradient step. The exact example overturns even worst-case one-epoch preference at sufficiently strong overrelaxation, while each elementary step remains contractive. This is more informative than a generic convergence guarantee or a numerical illustration, but is not asserted to predict arbitrary later epochs.

## Scope and limitations

No full-corpus novelty certification is possible; comparison risk persists for older specialized literature. Program checks are exact but finite; completeness comes from the two-dimensional symbolic identity and the sign proof. External independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
