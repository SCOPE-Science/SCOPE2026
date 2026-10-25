# Scientific review

## Correctness
**PASS.** The proof reconstructs all quantifiers and the original generating set. It uses the published optimal-greedy and Apéry-set formulas at the verified parameters, independently proves monotonicity of the weighted greedy function, identifies the high greedy digits of \(M=m2^n\) with the binary digits of \(m\), and establishes the final constant-weight plateau and its first index. The resulting unique Apéry maximizer yields the exact displayed Frobenius formula without extrapolation. The separately written shortest-path implementation verifies 161 admissible semigroups over 1,072,169 residue vertices and three examples outside the previously explicit regimes. Finite checks are not substituted for proof.

## Originality
**PASS in the inspected literature, with residual risk.** The 2023 Proth-number paper has an explicit special-parameter formula. Liu–Xin–Ye–Yin supply the general Apéry and genus infrastructure, but their explicitly evaluated Theorems 5.4 and 5.5 apply only when the first greedy coefficient is positive or the second is positive; their discussion explicitly leaves \(q=63\) outside them. The present formula works for all odd parameters, gives a previously absent popcount compression and exact maximizing residue, and is not implied by those two stated special-case conclusions. Searches for the complete formula, alternate binary-coin descriptions, stronger semigroup classifications and numerical tables yielded no equivalent statement. Existing full-parameter Wilf inequalities concern a different invariant. Remaining risk: an unindexed published theorem or a later treatment could contain an equivalent implication.

## Mathematical value
**PASS.** The motivating literature formulates the arbitrary odd-parameter Frobenius problem explicitly. The result gives an exact closed-form answer for the whole family using only a tiny greedy decomposition of the binary digit count, including infinitely many parameter choices with two or more initially vanishing greedy coefficients. It upgrades a partial special-case solution to an all-parameter one and additionally locates a unique maximizing Apéry class. This is a natural invariant and a motivated outstanding case, not an arbitrary finite statistic.

## Boundaries and scientific integrity
No statement is made about generalized bases, genus beyond previously available expressions, or independent priority. The proof depends on the published full-family Apéry reduction and greedy optimality theorem; these premises were inspected at their actual formulas. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
