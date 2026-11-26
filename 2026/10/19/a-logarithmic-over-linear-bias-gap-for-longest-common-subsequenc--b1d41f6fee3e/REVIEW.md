# Independent mathematical audit

## correctness

PASS

Concatenation gives superadditivity in n at each fixed d. Greedy embedding of a fixed target is equivalent to embedding by any index sequence, and after each first hit the remaining i.i.d. stream is independent, so successive waiting times are independent Geom(pᵢ) variables on {1,2,…}. Their negative Laplace transforms are Mᵢ(t) as stated. Markov's inequality and independence across sources give an e^{dtn} factor; summing over all length-ℓ targets gives exactly S_d(t)^ℓ. Choosing any fraction above dt/(−log S_d) gives vanishing tails and the finite-d bound. With t_d=log d/(dΔ), the nonmaximal-letter terms relative to the maximal one total O(1/d), including a tie among second-largest letters. Also Λ₁=t/p₁−(1−p₁)t²/(2p₁²)+O(t³), so the finite-d bound at t_d is p₁+(1−p₁)t_d/2+O(t_d²+1/(d log d)). The minimum of the d mode-letter counts yields the lower baseline by the strong law at fixed d. The limiting inequality is one-sided and does not assert sharpness or an asymptotic equivalent. Reviewed frozen binary enumeration and recorded numerical checks without executing the supplied code; they corroborate finite instances only.

## originality

PASS

Best-of-knowledge pass for the letter-specific finite-d transform bound and the strict-bias implication at fixed alphabet and fixed probabilities. The checked precedents cover nonuniform finite embedding probabilities and uniform many-word LCS, not this rate statement or variational bound.

## value

PASS

The finite-d upper bound keeps the entire letter law and can be optimized by a one-variable search without calculating any subsequence probabilities. Its quantified strict-bias implication is substantially smaller than the benchmark order in the tied, uniform binary case and describes a meaningful distributional distinction. Credit is for the upper bound and usable variational expression, not an optimal rate or optimum coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
