# Self-review

## Correctness — PASS
For \(n=N-1\), the hypergeometric law has exactly two atoms because the sample is obtained by omitting one population item. Both corresponding binomial masses equal the \(\operatorname{Bin}(N,L/N)\) mass at its integer mean, yielding the exact density-ratio formula \(\max\{p,1-p\}/M_N(L)\). On the half-range \(L\le N/2\), the adjacent quotient reduces to \(C_{N-L-1}/A_L\). The strict increase of \(C_m\), together with the exact brackets \(C_{3k+1}<A_k<C_{3k+2}\), gives the iff criterion \(H_N(k+1)>H_N(k)\iff N\ge4k+3\). This proves the unique half-range maximum and, by reflection, exactly two global maximizers. All quantifiers and boundary cases \(N\ge3\) are covered analytically.

Risk: the finite checker does not prove the infinite theorem and is used only as a regression check.

## Originality — PASS
The closest primary paper studies the identical hypergeometric/binomial maximal density ratio. Its Theorem 2 gives the composition maximizer only under \(n-1\le N/2\), where it is the edge composition \(L=1\) or \(N-1\). The leave-one-out regime \(n=N-1\) is outside that hypothesis for \(N\ge4\), and the inspected proof does not state the quarter-population outer maximizer. Candidate-specific searches under maximal density ratio, relative error, likelihood ratio, sampling without replacement, leave-one-out, and hypergeometric/binomial aliases found no covering result. The nearest indexed records concern different hypergeometric asymptotics or different discrepancies.

Risk: because the new proof is elementary after the leave-one-out reduction, an equivalent older calculation under different finite-population terminology remains possible.

## Value — PASS
The sample size \(N-1\) is a canonical endpoint, not an arbitrary slice: sampling without replacement is literally “omit one item”. It complements the published half-sample theorem at the opposite extreme and reveals a qualitative reversal of the worst population composition from the edge to asymptotic quarter population. Since maximal density ratio supplies uniform multiplicative event control and acceptance-rejection constants, the exact extremizer is mathematically informative for the approximation problem itself.

The result does not claim a full phase diagram in sample size; that intermediate problem remains outside scope.

Self-review: passed. Independent audit: not yet performed.
