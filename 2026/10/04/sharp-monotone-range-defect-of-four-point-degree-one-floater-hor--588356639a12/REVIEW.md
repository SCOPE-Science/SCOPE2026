# Same-model review

## Correctness
PASS. The published \(d=1\) weight formula gives the uniform weights \((-1,2,-2,1)\). Rewriting monotone data by nonnegative increments converts the range problem exactly into optimization of four rational coefficient functions over \([0,3]\). Sign analysis reduces the global defect to a single edge coefficient \(g(x)\); its derivative has a quartic numerator that is strictly decreasing on \([0,1]\), so the maximizer is unique. A separate analytic bound proves that the middle-cell defect is strictly smaller. Exact arithmetic replay checks all stated rational identities, the algebraic brackets, and the strict witness.

## Originality
PASS with residual shape-preserving-literature risk. The primary Floater–Hormann paper covers construction, pole-freeness, approximation order, and barycentric weights. Later work covers Lebesgue constants and numerical stability. Searches for monotonicity, shape preservation, range preservation, overshoot, positive-data behavior, and equivalent cardinal-coefficient formulations did not locate the exact four-node monotone-range theorem or its algebraic sharp constant. The original full text was searched directly for the most plausible aliases and contains no matching shape-preservation statement.

## Value
PASS. Floater–Hormann interpolation is specifically attractive on equispaced data because it avoids real poles and high-degree polynomial oscillation. The result shows quantitatively that this does not control an independent practical failure mode: a bounded increasing data table can produce a value more than \(18\%\) outside its range. The theorem gives a complete sharp guardrail for the smallest genuinely rational uniform \(d=1\) stencil, including an exact extremizer and a strict-data witness.

Same-model review: passed. Independent audit: not yet performed.
