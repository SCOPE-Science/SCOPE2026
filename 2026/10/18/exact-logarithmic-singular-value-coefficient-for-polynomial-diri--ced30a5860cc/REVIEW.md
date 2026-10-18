# Scientific review

## Correctness — PASS

The formula \(T_g=DB\) is verified directly on the dense Dirichlet-polynomial subspace. The ordered singular values of \(D\) are exactly \(1/\log(n+1)\), furnishing the upper bound. The multiplier operator \(B\) has norm equal to the supremum of the finite-torus polynomial, by the analytic Hardy multiplier norm identity. For a norm-approximating finite-support vector, the elementary conflict-graph bound supplies at least \((R+1)/(|H|^2+1)\) orthogonal multiplicative translates in every interval of size \(R+1\), with mutually disjoint images. This gives the matching min--max lower bound at every sufficiently large singular-value index. The example is maximized by an exact completed square. The checker passed 194,050 finite assertions; infinite quantifiers are proved, not inferred from tests.

## Originality — PASS, conditional on external priority review

Brevig–Perfekt–Seip's Theorem 7.2 (2016) establishes absence of finite Schatten membership for *all* nonconstant symbols, but does not state an exact singular-value leading constant. Chen–Wang–Yuan's 2026 paper characterizes compactness and essential norms, not singular-value asymptotics. The present statement is a strictly finer limit under the additional finite-symbol hypothesis. A 2024 paper concerns Volterra operators on Bergman spaces, not the specified Hardy Hilbert space. Targeted searches did not identify identical or stronger finite-polynomial singular-value equivalents. An older generalized compact-diagonal/multiplicative-Toeplitz theorem may cover this as a special case; the searches do not constitute certification of absolute novelty.

## Mathematical value — PASS

The theorem replaces a qualitative compact/non-Schatten dichotomy by the exact asymptotic distribution scale and computes its constant for every finite Dirichlet symbol. The constant is the Hardy multiplier norm of the symbol derivative, which reflects arithmetic frequency collisions and complex phase cancellation. The explicit three-term example shows that substituting the sum of coefficient magnitudes overestimates the sharp constant. The result gives a natural calibrated approximation-number benchmark for Dirichlet Volterra operators, rather than a single isolated numerical value.

## Scope and residual risks

The result requires fixed finite symbols, and it is confined to the Hilbert exponent. No higher-order remainder is claimed. Complete publication-priority searches remain desirable, particularly under alternative multiplicative convolution terminology. The monomial and non-Schatten facts are acknowledged as pre-existing or elementary boundary cases. The finite checker is diagnostic only.

Self-review: passed. Independent audit: not yet performed.
