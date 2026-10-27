# Scientific review

## Correctness — PASS

For fixed \(n\), conditioning on one occurrence of a designated letter makes its location uniform and all other letters iid with renormalized masses. This proves the exact covariance formula. In the induction, adding probability \(\varepsilon\) contributes a new-letter term with positive limit after normalization by \(\sqrt\varepsilon\) at length \(\lfloor\varepsilon^{-1/2}\rfloor\), and negative limit \(-4Se^{-2}\) at length \(\lfloor2/\varepsilon\rfloor\). Every old-letter contribution is exponentially smaller. Thus two strict sign changes can be appended without disturbing finitely many earlier changes. An separate exhaustive exact-rational checker corroborates the identity and the three-letter witness (1050 assertions). The checker is corroboration, not a proof for arbitrary \(q\).

## Originality — PASS (provisional historical priority)

Primary literature concerning multi-state runs and patterns was compared at the level of implications. The 2014 Johnson–Fu article covers general run-pattern distributions. Kong's 2018 joint generating functions track all letter frequencies and run statistics and therefore dominate fixed-length joint-moment *computability*. Their inspected results do not state a lower bound increasing linearly with alphabet size for the *number of covariance sign reversals over word lengths*, or a rare-letter perturbation construction. The finite covariance expression is not asserted to be novel. General joint-generating-function methods could conceal an implicit derivation; this is explicitly retained as a historical-priority risk. Relevant published research summaries on composition-conditioned transition dependence and richness–occupancy covariances concern different statistics.

## Value — PASS

The dependence between global vocabulary rarity (single-occurrence letters) and local fragmentation (adjacent-letter runs) is a natural two-scale question. A single covariance sign does not capture the relationship: the constructive theorem shows that any proposed alphabet-independent one-switch principle fails dramatically, and explains the mechanism via separated rare-letter scales. The binary rigidity and concrete ternary witness identify the minimal qualitative boundary. Neither computing moments alone nor making a generic minor parameter change is the asserted value.

## Limitations

The construction gives at least \(2q-3\), not the exact maximum. No claim of independent audit, priority certification, finite verification of the induction, or generalization beyond iid finite-alphabet words is made.

Self-review: passed. Independent audit: not yet performed.
