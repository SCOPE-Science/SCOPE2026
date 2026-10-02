# Independent mathematical audit — SCOPE-20260920-88aa83bd21bc

Final disposition: **PASS**.

## Correctness
**PASS** — The line-graph arm-state count is correct and yields the displayed general tripod formula. Substituting the path count \(q_t=(2tF_{t+1}-(t+1)F_t)/5\) into the \([P_2,P_2,P_c]\) and \([P_3,P_3,P_c]\) specializations reduces the gap to \(2(d-1)F_{d+1}-3dF_d\), with \(d=n-7\). Direct arithmetic gives positive gaps 26 and 186 at \(d=14,15\); for \(d\ge16\), \(5F_{d+1}-8F_d=F_{d-5}>0\) gives \(F_{d+1}/F_d>8/5\) and hence strict positivity. A fresh independent calculation reproduced the first several gaps and the closed formula. The finite all-tripod scan is correctly treated as supplementary only.

## Originality
**PASS** — The primary Andriantiana–Shozi preprint explicitly states Conjecture 1 with \([P_3,P_3,P_{n-7}]\) after computations only through order 20. Resultary searches found no earlier or later published correction or counterfamily matching \([P_2,P_2,P_{n-5}]\). The assigned exact Fibonacci comparison therefore supplies a genuine counterexample family to the stated conjecture, to the best of current knowledge.

### Equivalent formulations
The counterexample is to the literal source conjecture, not to a proxy invariant.

### Broader coverage
The source's finite evidence does not imply the conjecture or the audited counterexample family.

### Exact database or table
The conclusion is supported by the direct source comparison; absence is not used alone.

### Claim versus prior implication
No stronger inspected theorem covers the counterfamily.

## Value
**PASS** — An infinite exact counterfamily to an explicit recent extremal-tree conjecture is mathematically worthwhile. The result locates the first failure at \(n=21\), gives a closed gap formula, and supplies a reusable tripod counting formula while carefully avoiding the stronger unproved claim that the replacement family is globally second-largest.

## Source inspections
- **The number of 1-nearly independent edge subsets** (https://arxiv.org/abs/2405.17154): primary arXiv PDF sections containing the path formula, Theorem 6, and Conjecture 1 Method: primary PDF inspection. Assessment: PRIMARY_SOURCE_STATES_REFUTED_CONJECTURE. Evidence: The source reports computational support through order 20 and states \([P_3,P_3,P_{n-7}]\) as the universal second-largest candidate for \(n\ge12\).

## Residual risks
- A differently indexed correction or independent observation outside the searches remains possible.
- The theorem does not prove that \([P_2,P_2,P_{n-5}]\) is the true global second-largest tree for all \(n\ge21\).
