# Review

## Correctness

PASS. Every centered increasing coding is a positive combination of centered cumulative-cut indicators. Their covariance is explicit:
\[
\operatorname{Cov}(H_j,H_k)
=
P_{\min(j,k)}
\left(1-P_{\max(j,k)}\right).
\]
The normalized cut correlation is minimized uniquely at the two most separated cuts, producing the endpoint-mass constant.

Applying this minimum ray correlation to the positive bilinear gap expansion, then using the \(L^2\) triangle inequality for each score vector, proves the lower bound. Positive gaps make the bound strict for at least three categories. Opposite one-dominant-gap limits prove sharpness. Cauchy--Schwarz gives the upper endpoint and its exact affine equality condition.

## Originality

PASS, with a residual classical association/isotonic-cone risk. Karlin's complete article was inspected through the association-array definition, the indicator-function reduction for monotone functions, examples, and extensions. It provides the relevant cone decomposition but does not state the fixed-profile Pearson-correlation floor or its endpoint-mass formula.

Cuadras--Cuadras provide a covariance-kernel framework for correlations between functions, while Barbiero studies attainable correlations by changing couplings with fixed ordinal margins. Neither accessible statement solves the present problem, where the common category probabilities are fixed and both order-preserving numerical score vectors vary.

The closest prior fixed-profile ridit theorem fixes one score vector and therefore has a different, stronger profile-dependent lower bound. It does not imply the two-free-score minimum, and the present result does not imply the ridit-specific constant.

Exact-formula, alias, and semantic searches did not locate the claimed endpoint-mass floor.

## Value

PASS. Numerical coding of ordinal categories is inherently nonunique. The theorem gives the complete worst-case Pearson agreement between any two order-preserving codings once category frequencies are known. It identifies a simple endpoint-frequency robustness certificate, characterizes the extremal recodings, and gives the transparent equal-frequency benchmark
\[
\frac1{m-1}.
\]
This is a natural complete classification of coding sensitivity rather than a selected finite example.

Same-model review: passed. Independent audit: not yet performed.

Exact-rational replay: `VERIFY_OK decomposition_checks=5000 cut_covariance_checks=97406 cut_minimum_checks=2500 global_lower_checks=2127 affine_checks=2500 binary_checks=373 boundary_checks=2127 equal_mass_checks=98`.
