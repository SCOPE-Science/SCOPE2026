# Self-review

## Correctness — PASS

The domain is every positive odd integer. Step 1 counts possible supports and drops the total-sum constraint to obtain a uniform upper bound. Step 2 constructs a disjoint, injectively parameterized family of exact partitions: parity makes the residual multiplicity of ones integral, and the prescribed ranges keep it nonnegative. With \(s\) respectively a fixed fraction of \(k\) and \(k-O(\log k)\), this gives the claimed matching exponents and error terms. Step 4 applies the established largest-part-overlined correspondence and concentration away from sparse supports. The argument does not extrapolate an infinite theorem from finite computation. The independent coefficient/recurrence comparison checked \(2048\) positive indices.

## Originality — PASS within inspected evidence

The motivating Ballantine–Beck article introduces the semi-Pell overpartition model and poses asymptotic comparisons of its odd-index sequences as an interesting question; its stated theorems and concluding discussion do not derive the support large-deviation exponent or the \(n^{1+o(1)}\) ratio. Andrews proves the unweighted odd-binary partition interpretation and parity. Keith–Munagi studies semi-Pell composition bijections, generating functions and congruences rather than asymptotic support concentration. Individual OEIS sequences record recurrences and numerical tables; none supplies the cross-sequence separation theorem. Relevant nearby mathematical-record results treat different partition models (including weighted representation-balance partitions and unrestricted overpartition minima) and do not dominate this exact-support statement. Earlier unindexed or indirect coverage is a residual risk; novelty is not inferred solely from a failed search.

## Mathematical value — PASS

This gives a sharp global asymptotic comparison explicitly raised in the source literature and a distributional explanation for why the weighted and unweighted counts diverge by an essentially full factor of \(n\). The nontrivial \(\varepsilon^2/2\) support large-deviation rate adds information beyond classical leading binary-partition growth. The result is a complete, natural logarithmic-rate statement, not an arbitrary finite cutoff or a restatement of the defining recursion.

## Remaining scientific limitations

The results are restricted to odd indices, are logarithmic-scale rather than exact multiplicative asymptotics, and leave comparisons with other self-similar sequences open. Independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
