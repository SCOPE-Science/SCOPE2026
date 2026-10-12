# Review
## Correctness
PASS. The one-step recursive-tree identities are exact. The Wiener increment is \(n+D_n(U_n)\), the leaf increment is \(1-J_n\), and the only new mixed term is \(J_nD_n(U_n)\). Introducing the leaf-transmission sum closes that term exactly. Its own conditional recursion closes through \(L_n\) and \(W_n\). The resulting harmonic formulas satisfy the initial conditions and recurrences, and exhaustive tree enumeration through \(n=9\) agrees exactly.

## Originality
PASS, with a specific older-literature risk. Complete primary text for the leaf process contains no Wiener-index treatment, while complete primary text for recursive-tree Wiener tails contains no leaf treatment. The foundational Wiener paper's accessible abstract discusses covariance with internal path length rather than leaves. Exact-form and alias searches found no displayed leaf-Wiener identity.

A prior exact result for leaf count versus internal path length is not stronger: Wiener growth depends on the transmission of the random attachment vertex, and the proof here requires a separate leaf-transmission statistic.

## Value
PASS. Leaves and the Wiener index measure complementary local branching and global metric spread. The theorem gives their full finite covariance, a strict negative-sign threshold, and a nonzero normalized covariance limit. The auxiliary transmission closure provides a reusable mechanism rather than a one-off numerical moment.

## Closest literature and limitations
The closest leaf literature gives marginal Markov-chain laws, while the closest Wiener literature gives moments, limit laws, tails, and dependence with internal path length. The result is restricted to uniform recursive attachment and unit edges, and it asserts second-moment dependence rather than stochastic ordering or a joint limit law.

Self-review: passed. Independent audit: not yet performed.
