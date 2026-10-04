# Same-model review

## Correctness
PASS. The cubic is rewritten exactly in the nonnegative increments of the monotone data. On the central cell its increment coefficients satisfy
\[
q_0\ge1\ge q_1\ge0\ge q_2,
\]
with the nontrivial upper bound on \(q_1\) supplied by an exact factorization. Linear optimization over the full admissible simplex therefore reduces both range extremes to single vertices. The two remaining cubic shape factors are reflections, and exact differentiation gives the unique extremal value \(\sqrt3/27\). The strictly increasing positive witness is obtained by direct substitution. The packaged exact checker returns `VERIFY_OK`.

## Originality
PASS with explicit residual risk. Classical literature establishes Lagrange interpolation on equally spaced nodes, the general oscillation problem, data-bounded adaptive remedies, and monotone cubic Hermite conditions. Direct searches for four-point cubic Lagrange monotonicity, range preservation, negative basis mass, the exact constant \(\sqrt3/27\), and equivalent local central-cell formulations did not locate a statement implying the sharp theorem. The full Fritsch--Carlson and Berzins articles were inspected and do not state the result. A survey chapter on equidistant Lagrange interpolation was only partially accessible, and older interpolation tables may encode the same coefficient extrema without the monotone-data interpretation; these are retained as residual risks.

## Value
PASS. Data-boundedness and positivity are established design goals for interpolation on equal grids, and the four-point cubic is the smallest standard local polynomial where negative Lagrange weights appear on the central cell. The theorem replaces a qualitative warning about overshoot by a complete dimensionless worst-case law, equality cases, and a strict-positive sign-reversal example. The exact constant is directly usable as a guardrail and regression benchmark for local cubic interpolation.

Same-model review: passed. Independent audit: not yet performed.
