# Mathematical assessment

## Correctness — PASS
The three side-occupancy probabilities \(1/9,2/3,2/9\) are exact. For the mixed-edge case, the two base angles impose \(x<t/2<y\) and the third angle imposes a quadratic product bound; this gives a one-dimensional logarithmic density with a transition at \(t=1/2\). In the all-distinct case, obtuseness at one point is equivalent to a clipped rational parameter bound; piecewise integration and the fact that at most one angle is obtuse recover the tabulated result. The unconditional mixture is algebraically exact, and collinearity has mass \(1/9\). Boundary equality events away from same-side collinearity have measure zero.

## Originality — PASS for the narrowed evaluated law, with risk
The most directly relevant 2024 public question already states the precise full-perimeter experiment and gives a triple-integral description. It does not supply the evaluated elementary constant or the mixed-edge conditional law. The published OEIS A394836 already gives the exact probability when there is one point on each side; that component is explicitly attributed and not claimed as new. Other inspected works concern tangent-defined random triangles, interior-random triangles, or pairwise moments. The new content is the evaluation of the precise full-perimeter probability and its two-side conditional distribution, not the problem statement, implicit integrals, or the known three-side component. Unindexed earlier evaluations remain possible.

## Mathematical value — PASS
A posted exact geometric-probability question is resolved in elementary closed form. The natural distinction between one, two, and three occupied sides changes the answer: one-side samples are degenerate, the two-side law is \(4\log(4/3)-5/6\), and the three-side law is the known \((27/2)\log(4/3)-7/2\). The nontrivial two-side integration explains why a previously published approximately \(0.27\) estimate differs from the exact value near \(0.296865\), and the formulas provide an exact reproducibility benchmark for boundary-sampling geometry. This is an exact finite-dimensional integral-geometry invariant, not a claim about random triangles generally.

## Sources and limitations
The full problem and its unevaluated integral were inspected at https://puzzling.stackexchange.com/questions/128400/three-points-on-the-sides-of-an-equilateral-triangle . The exact one-on-each-side probability is given by https://oeis.org/A394836 . Finch's full publicly available paper arXiv:1101.3931v1 treats circumscribed tangent triangles, so its probability does not imply the perimeter sampling law. A published boundary second-moment analysis concerns two sampled boundary points, not the acuteness of three. All cited comparisons are limited to the inspected passages and sources, and no exhaustive literature claim is made. Numerical checks are supporting checks, not infinite proof.

Self-review: passed. Independent audit: not yet performed.
