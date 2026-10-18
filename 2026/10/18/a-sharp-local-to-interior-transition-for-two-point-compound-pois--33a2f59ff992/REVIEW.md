# Scientific review

## Correctness — PASS
The centered compound-Poisson law has variance \(\lambda(1+24q)\) and an exact entire exponential transform. The first three decisive coefficients of the optimizer derivative were derived and checked with symbolic arithmetic. A uniform lower bound on **all** higher coefficients produces a rigorous one-crossing argument. The positive branch is a strict global maximum, not just a stationary point, while the other branch has no positive optimizer. The implicit-function calculation supplies exact transition exponents. The program `verify.py` reproduces the identities and numerical benchmark; the infinite proof is analytical.

## Originality — PASS, with residual risks
The closest primary treatment is Y. Chen (2026), arXiv:2610.00032v1, Section 7.2. It gives the exact variational formula, the illustrative mixture at \(q=1/40\), and an interior numerical optimum, but explicitly does not establish uniqueness. The present theorem extends to an explicit parameter interval, proves unique optimizer or strictly monotone behavior, and determines a critical transition law. The earlier Zhang–Wu compound-Poisson concentration theorem supplies general Bernstein bounds, not the exact tangency classification. Klar–Müller's M-class abstract concerns MGF order, but its complete text was not read. Indexed record and primary-literature searches found no stronger covering statement; differently phrased or inaccessible earlier work remains possible.

## Mathematical value — PASS
This resolves a specifically stated uniqueness gap in the motivating treatment, gives an unambiguous optimizer throughout a continuous family, and identifies a sharp local-to-interior concentration-scale transition with an explicit probability threshold. The linear collapse of the optimizer and quadratic gain describe how the sharp pole separates from the local cumulant obstruction. This does not claim a complete phase diagram for all two-point laws.

## Scope and scientific limitations
Only jump sizes \(1\) and \(5\) and mixture probabilities \(q\ge q_-\) are classified; no optimality assertion is made about the lower cutoff \(q_-\). The exact proof does not depend on numerical sampling. Independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
