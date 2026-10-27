# Research review

## Correctness

**PASS.** The model, quota, and criticality probability are stated explicitly. The proof separates the delegator, recipient, and every outsider; uses the two relevant binomial events; simplifies their ratio; and derives the total-power identity. Exact enumeration over all action profiles for 25 \( (n,r) \) cases agrees with the formulas. No finite enumeration is used as the infinite-family proof.

## Originality

**PASS, with a stated scope risk.** The closest source is Colley, Delemazure, and Gilbert (arXiv:2301.02462; IJCAI 2023), whose general a-priori index is the same framework and whose complete-bipartite and complete-graph cases are explicitly prior art. Their inspected paper does not state the closed form for the sparse graph with exactly one allowed delegation edge or the exact law \(nB_{n,r}+2s^2B_{n,r}/(3m)\). Zhang–Grossi (2021) and D’Angelo–Delfaraz–Gilbert (2021) use different delegation-power models. Searches of mathematical-result records and accessible prior claims returned related voting-power and delegation results but no matching one-edge quota formula. Because the general index definition determines this case, the originality claim is intentionally restricted to the explicit structural evaluation; a broader formulation may already exist outside the inspected sources.

## Value

**PASS.** The result gives an exact benchmark for a central design question in delegated voting: whether adding one permitted delegation option redistributes or increases aggregate criticality. It isolates simple majority as the unique conservation point and quantifies the supermajority excess by a quadratic term in the quota distance. This is stronger than a single numerical example and can serve as a check on more general power-index computations, while making no welfare or fairness claim.

## Closest literature and residual limits

- Colley, Delemazure, and Gilbert (2023): same a-priori measure; their explicit tractable graph classes and numerical examples are acknowledged as prior art.
- Zhang and Grossi (2021): fixed delegation profiles, delegative Banzhaf index, and strategic power-seeking; a different measure.
- D’Angelo, Delfaraz, and Gilbert (2021): delegative simple games and graph-change bribery; a different power construction.
- Berinsky et al. (2021): random delegation, concentration, and truth-tracking accuracy, rather than quota-pivotality power.

The general model is not claimed as new. The result does not address arbitrary graph edits, weighted voters, even electorates, or normalized-power conservation outside the stated case.

Self-review: passed. Independent audit: not yet performed.
