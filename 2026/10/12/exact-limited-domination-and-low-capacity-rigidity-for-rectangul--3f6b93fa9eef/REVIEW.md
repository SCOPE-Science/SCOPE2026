# Mathematical assessment: limited domination in rectangular rook graphs

## Correctness — PASS
For a selected square `(i,j)`, the number of outside neighbors is `(n−ρ_i)+(m−κ_j)`. Domination forbids the simultaneous existence of an empty row and empty column. If every row is met, the capacity inequality forces each row occupancy to be at least `max(1,n−k)`; if every column is met, its occupancy is at least `max(1,m−k)`. Full-column and full-row slabs attain the smaller resulting bound. For `1≤k<min(m,n)`, equality forces every occupied line in the opposite orientation to be full, classifying all optimizers and giving the stated binomial counts. The endpoints are covered separately. Bounded exhaustive tests support, but do not establish, this universal proof.

## Originality — PASS, with residual risks
The original full version of Tepeh, *On k-limited domination: complexity and Cartesian products* (arXiv:2606.22428v1), proves the Cartesian-product upper bound and establishes a special diagonal equality `K_{k+2} □ K_{k+2}`; it does not provide a matching lower bound for all pairs of complete graph factors or the low-capacity optimizer classification. Božović et al., *On k-limited domination in graphs* (published September 11, 2026), define the invariant and its regular-graph `(1,t)` equivalence, but their exact listed families are not rook products. Comparisons also considered `(0,k)`-pitchfork domination, the line graph `L(K_{m,n})` alias, and k-tuple total domination, the last being a different invariant.

The revised October 2026 text of arXiv:2606.22428v2 was not available in full. Its abstract alone does not settle whether it covers the present general case. This creates a material novelty risk, as does possible older unindexed `(1,t)`-domination work. Search absence is not a proof of universal novelty.

## Mathematical value — PASS
The exact three-parameter rook family is natural and explicitly motivated by the prior Cartesian-product sharpness problem. The all-capacity minimum and complete low-capacity extremizer classification are exact structural invariants, not merely a table of small examples. No statement is made about higher products or classification at all larger capacities.

## Scientific evidence
Tepeh arXiv:2606.22428v1, Theorem 7 and Proposition 8 (public full first version); Božović et al., *Computational and Applied Mathematics*, DOI 10.1007/s40314-026-03902-2, introduction, Proposition 1 and regular-graph equivalence; revised arXiv:2606.22428v2 abstract and version metadata; inspected source proof and independent bounded verifier. No formal verification or expert attestation is claimed.
