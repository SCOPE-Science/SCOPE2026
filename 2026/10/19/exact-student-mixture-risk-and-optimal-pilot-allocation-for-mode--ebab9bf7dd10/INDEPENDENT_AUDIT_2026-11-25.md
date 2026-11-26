# Independent mathematical audit

## correctness

PASS

Subtract the realized finite-population mean: the error is (M/N) times the difference between the correction-sample and complement residual means, M=N−a. For every fixed population and nonsingular pilot, its finite randomization mean is zero and the design variance factor is M(M−b)/(N²b). This is a conditional design statement, not a claim of joint integrability at a=p. Conditional on the pilot and a particular correction set, the remaining Gaussian residuals have variance σ²+||δ||² for δ=β̂−β; the squared sum of their signed coefficients is γ for each set. With a rotational Gaussian design, the reciprocal of any unit-direction quadratic form of the inverse Gram matrix is χ²_(a−p+1) by residualizing one design column on the others. Cramér–Wold gives the full vector law σW/√U, and the correction's standardized Gaussian is independent of the pilot. Thus ||δ||²/σ²=V/U in law, and U/(U+V) is beta with shapes ν/2,p/2. Its inverse q/2 moment exists exactly for q<ν, with logarithmic divergence at equality, yielding the displayed gamma ratio and infinite MSE at a=p,p+1. Applying the same realized-target correction to the plain sample gives its reported risk and the strict ratio test at finite risk. In t=a−1 the derivative numerator is (L−c−p)t²+2pct−pcL, strictly increasing between its opposite endpoint signs; the rationalized root is the unique continuous minimum and monotonicity gives the two clipped integer neighbors. The singleton feasible split at B=p+3 is included. For fixed p and N/B→∞ with B→∞, t*/√(pB)→1; the factorization C_N=[(1−a/N)/(1−a/B)]/[1−p/(a−1)] then gives C_N−1~2√(p/B) at either minimizing rounded neighbor. Separately, at fixed p,B the N→∞ relaxation gives the stated exact lower envelope.

## originality

PASS

The general difference estimator and its exact randomization unbiasedness are prior work. The supported distinct content is the exact moment and equal-budget allocation analysis for this finite-population Gaussian specialization, especially the optimized risk comparison, not the Student or inverse-Wishart ingredients. The closest inspected prior sampling results cover the design, not the combined distribution, moment cutoff and optimized risk. An equivalent unconditional Gaussian prediction calculation in older survey literature remains possible; the unavailable Sitter article is a bounded access risk, not a novelty verdict.

## value

PASS

Design unbiasedness alone conceals infinite joint MSE at two feasible pilot sizes. The exact law and optimized signal threshold quantify when spending gradient evaluations on a pilot helps at a fixed evaluation budget versus plain sampling, with an explicit integer allocation rather than a heuristic. The practically interpretable control is for the stylized Gaussian experiment, not a claim about wall-clock time, regularization or SGD convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
