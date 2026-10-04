# Review

## Correctness

PASS. After range normalization, conditioning on whether the observation is one of the two endpoint atoms gives an unavoidable variance contribution
\[
\frac{p_1p_m}{p_1+p_m}.
\]
The equality conditions force every interior atom to the endpoint conditional mean, which is compatible with strict support only for a single interior atom.

For the upper side, every ordered support is a positive gap combination of centered cumulative-cut indicators. Their standard deviations are
\[
\sqrt{P_j(1-P_j)}.
\]
The \(L^2\) triangle inequality therefore gives the cumulative-cut maximum, and strictness follows for every support with at least two positive gaps. Explicit collapse sequences prove both sharp limits, and connectedness fills every intermediate value.

## Originality

PASS, with an explicit older weighted-inequality residual risk. The complete Sharma--Gupta--Kapoor variance paper was inspected through its statement of the Popoviciu, von Szokefalvi-Nagy, and Bhatia--Davis bounds and through its main range-based refinements. Its finite-universe setup is equal-weight and does not state a fixed arbitrary probability-profile range.

Afendras--Balakrishnan--Papadatos provide a broad discrete variance-bound framework for cumulative Ord laws, but their accessible abstract and classification show a difference-operator/orthogonal-polynomial program rather than support-geometry optimization at prescribed arbitrary masses.

Targeted semantic database and web searches using weighted variance, fixed probabilities, range normalization, endpoint masses, cumulative cuts, Popoviciu, and von Szokefalvi-Nagy did not locate the two-sided fixed-profile attainable interval.

## Value

PASS. Popoviciu's upper bound and the von Szokefalvi-Nagy lower bound are classical complementary constraints on variance relative to range. A fixed frequency profile contains strictly more information than support size alone. The theorem gives the exact amount of additional information on both sides, identifies the extremal support geometries, and reduces under equal masses to the classical lower constant while sharpening the upper constant whenever an exact half-mass cut is unavailable.

Same-model review: passed. Independent audit: not yet performed.


Exact-rational replay: `VERIFY_OK random_lower_checks=30000 random_upper_checks=25620 two_point_checks=4380 three_point_lower_checks=10000 equal_mass_checks=198 lower_path_checks=6000 upper_path_checks=6000`.
