# Self-review

## Correctness — PASS

The object is a uniform involution on \([n]\), \(n\ge3\). The statistic \(D_j\) compares values at two adjacent positions and \(I_i\) marks a prescribed fixed label. The explicit descent-complementing map pairs each involution with one of opposite local descent status **without changing any remotely indexed fixed-site indicator**. It is genuinely involutive, including both exceptional two-local-fixed and two-local-transposed cases. Exact one-point conditioning counts \((j-1)T_{n-3}\) and \((n-j-1)T_{n-3}\) favorable involutions. Subtraction using \(\mathbb E D_j=1/2\) proves the matrix entry formula; summation via \(T_m=T_{m-1}+(m-1)T_{m-2}\) gives every stated covariance and its signs. The same recurrence bounds \(T_{n-1}/T_n\) and proves the limit. The standalone checker passed 345,599 exact assertions, including exhaustive remote-status conditionals through size 10. The finite checks support but do not establish the universal results.

## Originality — PASS (qualified)

Targeted searches for conditional fixed-site/descent independence and telephone-number covariance matrices did not retrieve a matching result. Guo–Zeng (2005) and Chow (2008) study aggregate involution descents. Reutenauer's fully inspected 1989 theorem—and the related Gessel–Reutenauer 1993 paper—count given cycle **types** with descent sets, but cycle type cannot recover the *locations* of fixed sites. Forrester–Nagao–Rains (2005) study fixed-count random involutions via increasing subsequences, rather than descent events. A prior fixed-transposition-class inversion-gap formula determines local descent probabilities given the number of transpositions and can already imply the **aggregate** fixed-count/descent covariance after mixing the classes; the aggregate identity alone is therefore not a novelty claim. It does not retain which sites are fixed or give independence within every remote fixed/nonfixed status fiber. The most directly comparable public uniform-*permutation* theorem has sitewise interior cancellation and total covariance \(-1/n\); its hypothesis is different, so it does not imply the present strictly negative interior effects and limit \(-1\). The 1985 Désarménien–Foata full text and 1993 joint final paper were not completely accessible in this assessment; a hidden refined specialization and other unlocated earlier work remain priority risks. Search failure alone is not proof of novelty.

## Mathematical value — PASS

A single local combinatorial involution proves exact independence from an entire vector of remote fixed/nonfixed statuses, not merely a vanishing mixed moment. It provides a full finite-size site-versus-descent covariance matrix, distinguishes boundary versus interior contributions, and isolates a substantial model change in global dependence compared with all random permutations. These are natural probability statistics for random matchings with unmatched points (involutions), and the theorem makes all normalizations and boundary cases explicit. It does not purport to reprove aggregate classical Eulerian enumerators as a new result.

## Scope and priority limitations

Uniform involutions only; \(n\ge3\) for the mixed matrix, with \(n=3\) interior covariance exactly zero and strict interior negativity only for \(n\ge4\). No claim of joint independence among the different descents, or of independence from arbitrary remote non-fixed permutation data. Distinguish earlier full-text inspections from bibliography-only sources. Historical priority and the universal proof have not received independent review.

Self-review: passed. Independent audit: not yet performed.
