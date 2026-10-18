# Scientific review

## Correctness
PASS. The completed-step identity reduces off-diagonal positivity to the graph resolvent. Walsh diagonalization gives the stated exact subset-sum return. The monotone cutoff, strict pair-balancing order, uniform-dimension comparison via random deletion, asymptotic binomial expansion, and two-rate cubic are proved with explicit hypotheses and normalizations in `RESULT.md`. The standalone verification program separately corroborates the Fourier kernel, exact moment identities, finite majorization inequalities, scalar signs, and finite-dimensional matrix inversions. Computation alone is not offered as an infinite proof.

## Originality
PASS on available scientific evidence, with explicit residual risk. The general diagonal-resolvent test and reversible-chain cutoff are published prior results and are not attributed as new. Reisinger–Whitley address Fourier convergence for one-dimensional heat evolution; Higueras–Roldán establish finite-grid Chebyshev thresholds for a one-dimensional Dirichlet problem. The closest accessible historical cycle-torus classification varies graph periods, not rates on weighted Boolean products. Searches of published research records, those primary papers, and targeted web queries did not identify the strict rate-majorization result or its sharp dimension corrections. An unindexed specialized theorem could still cover some or all of the contribution; absence of a hit is not a proof of novelty.

## Mathematical value
PASS. The result classifies, for every dimension and every nonnegative direction-rate allocation, which completed timesteps preserve a physically meaningful positive cone. It identifies an exact budget-constrained optimizer, a strict majorization order, a dimension-dependent sharp threshold with two finite-size corrections, and the singular divergence at loss of full connectivity. These facts distinguish a genuine rate-design phase law from merely evaluating an already known fixed-matrix positivity criterion. Accuracy, stage positivity, and arbitrary edgewise optimization remain outside scope.

## Sources and limits
The decisive known generalized identity is the published *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains* (research record d475df91cd2a), whose full result text was compared to the present theorem. The source-specific mathematical comparison is documented in `AUDIT.json`. Additional primary mathematical context: Reisinger–Whitley (arXiv:1210.5487), Higueras–Roldán (arXiv:2301.01066), and Horváth (1998, DOI 10.1016/S0168-9274(98)00050-6). A full independent originality review has not been performed.

Self-review: passed. Independent audit: not yet performed.
