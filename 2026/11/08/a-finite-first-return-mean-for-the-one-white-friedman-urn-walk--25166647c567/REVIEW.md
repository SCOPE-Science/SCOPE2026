# Scientific review

## Correctness

PASS. The one-step law follows exactly from the opposite-color urn composition. The nonnegative potential \(V(t,x)=tF(x/\sqrt t)\), with \(F(z)=48z+16z/(1+z)\), has an explicit differential drift bounded above by \(-64/27\). Third-order spatial and second-order time Taylor remainders yield the true discrete conditional drift bound \(-64/27+130/\sqrt{n+1}\), at most \(-1\) from \(n=9999\) onward on survival. Stopped-potential telescoping and the exact moment \(\mathbb E X_n^2=(n+4)/3\) give the finite numerical bound. No diffusion-limit heuristic is used in place of the discrete proof. Residual risk: arithmetic or a hidden endpoint assumption would affect this argument; the derivative ranges and endpoints were explicitly checked.

## Originality

PASS under the cited-record comparison, subject to historical-priority uncertainty. Balaji and Mahmoud expressly conjecture finite first-return mean for their opposite-color one-white Friedman walk, while proving only recurrence (arXiv:2504.14813, Sections 4–5). Bertoin's elephant walk return estimates (arXiv:2105.09569) are closely relevant, but they concern returns to the elephant walk's own zero, not the one-white Friedman walk's first return, which becomes a shifted-level hitting problem. Menshikov and Volkov (arXiv:0711.2373) study different urn reinforcement/drift regimes. Literature and mathematical-record searches did not reveal a directly dominating statement. The possibility of an unindexed theorem or a reduction through existing general first-passage estimates remains a residual risk.

## Value

PASS. The model and question are independently motivated by a stated open conjecture. An exact, fully quantitative first-return integrability proof closes the gap between recurrence and finite expected return, which cannot be deduced from a divergent sum of unconditional return probabilities. The upper bound is coarse but is not a mere minor numerical refinement: it establishes the previously unproved qualitative property.

## Limitations and closest sources

The theorem does not furnish the sharp mean, exact first-return distribution, almost-sure frequency of returns, or results for several urns. Closest primary sources are Balaji–Mahmoud, Bertoin, and Menshikov–Volkov. The mathematical proof has been reviewed without independent validation.

Self-review: passed. Independent audit: not yet performed.
