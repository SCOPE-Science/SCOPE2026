# Review

## Correctness — PASS

The exact projected matrix and characteristic discriminant are derived from the specified positive-definite matrix, without approximations. Integrating the two-variable real Gaussian least-squares Student density gives the probability. Both limit laws follow from justified dominated-convergence transformations and exact beta/polar integrations. The standalone checker independently tests symbolic identities, normalizations, constants, an explicit SPD nonreal example, and reproducible sketch simulations. Its finite trials are supporting checks, not proofs.

## Originality — PASS, with residual risk

The source already states that unmodified sketched Rayleigh–Ritz may produce complex eigenpairs even for symmetric positive-definite inputs. That qualitative observation is prior work, as is the Student law for Gaussian least-squares regression. The new claim is the exact finite-sketch Gaussian complex-pair probability for a motivated smallest-dimensional coupled SPD family and the universal, sharp near-collision square-root and oversampled large-gap power laws. Inspected primary treatments do not state this distributional classification; previously established deterministic coordinate-sketch examples do not imply the Gaussian probability. Earlier specialized probabilistic non-Hermitian compression calculations might contain an equivalent formula and remain a bibliographic risk. A negative literature search is not proof of novelty.

## Value — PASS

The probability of a real-Schur two-by-two block is operationally relevant to when real symmetric eigensolvers must handle nonsymmetric sketched projections. The exact law and its distinct asymptotic exponents quantify a genuine stochastic stability/representation boundary that qualitative counterexamples and worst-case spectral perturbation bounds do not provide. The sharp fixed exponent near compression eigenvalue collision explains why oversampling changes one tail without eliminating the near-collision mechanism.

## Scientific limits

The model is a fixed three-state SPD family, a two-vector trial subspace, and dense independent real Gaussian sketch rows. It does not cover sparse embeddings, dynamic Krylov subspaces, real-Schur postprocessing correctness, or solver convergence. Independent review is outstanding.

Self-review: passed. Independent audit: not yet performed.
