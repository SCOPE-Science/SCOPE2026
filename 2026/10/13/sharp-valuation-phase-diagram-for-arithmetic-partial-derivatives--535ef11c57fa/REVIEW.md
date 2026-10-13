# Self-review

## Correctness
**PASS.** Writing \(x=b p^m\) with \(p
mid b\) gives the exact identities \(D_p(x)=b m p^{m-1}\) and \(
u_p(D_p(x))=m-1+
u_p(m)\). For \(m<p\) and for \(p<m<2p\), the current valuation is not divisible by \(p\), so the claimed factorial iterates follow by induction. At \(m=p\) the orbit is fixed. For \(m\ge2p\), the valuation region is forward invariant, including the exceptional boundary \(p=2,m=4\), and the magnitude ratio is always at least two. Signed coefficients cause no issue because the argument uses absolute value only in the divergent regime. The checker independently replayed 786314 finite assertions.

## Originality
**PASS.** The closest source is Emmons–Xiao's 2022 paper. Its Theorem 10 proves only the eventual alternatives zero / fixed \(a p^p\) / divergence after developing eventual periodicity of the valuation sequence; it does not give the sharp initial-valuation thresholds \(p\) and \(2p\), the exact extinction and landing times, the explicit fixed value reached from the middle band, or the per-step doubling bound. The authors' 2024 local-field extension again studies valuation periodicity and does not state this integer Archimedean phase diagram. published-finding corpus searches using the threshold, basin, fixed-point, landing-time, and doubling formulations found no implication-equivalent result. The nearest owned findings concern the full arithmetic derivative or the two-prime arithmetic subderivative and do not imply this statement.

## Value
**PASS.** The focal literature gives an eventual trichotomy whose case selection is expressed through valuation-sequence dynamics. The new statement collapses the integer case to two sharp thresholds visible immediately from the initial valuation and adds exact stopping/landing times plus a quantitative divergent lower bound. This turns an eventual qualitative result into a complete elementary phase diagram and isolates precisely why the single-prime system is far simpler than full arithmetic-derivative dynamics.

Closest-literature limitation: the result is a short structural strengthening of a well-developed dynamical analysis, so an unindexed note could contain the same threshold observation. No claim is made for multi-prime subderivatives or the full arithmetic derivative.

Self-review: passed. Independent audit: not yet performed.
