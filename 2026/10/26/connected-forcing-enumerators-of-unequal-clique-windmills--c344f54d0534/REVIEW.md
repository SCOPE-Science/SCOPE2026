# Self-review

## Correctness — PASS

The statement quantifies every integer \(r\ge2\), all blade sizes \(m_i\ge2\), and \(k\ge1\). With the hub black, nonempty blades must each have at most \(k\) initially white vertices or no force can enter them; empty blades have no initial peripheral forcer and require total order at most \(k\) for the hub to finish them. Both conditions are sufficient by explicitly first filling occupied blades. Without the hub, initial connectivity confines black vertices to one blade and the two sequential inequalities are necessary and sufficient. This is a full infinite-family argument; the homogeneous cases and sharp thresholds follow algebraically. The actual packaged Python verifier separately checked 671 graph/forcing parameter tuples and 1,458,592 subsets, with all comparisons passed. Finite tests do not substitute for the proof.

## Originality — PASS, with limitations

The closest paper is Premodkmuar–Dominic–Chacko (2020), Proposition 7 (DOI 10.28919/jmcs/4446). It determines the **scalar minimum** for the friendship subfamily \(m=2\); that scalar result is acknowledged. The paper's primary PDF was examined at its definition and Proposition 7/proof and searched for clique/windmill material. It does not state the distribution of all connected sets, heterogeneous blade conditions, or minimum-set multiplicities. The 2019 paper with DOI 10.26438/ijsrmss/v6i3.121127 treats different scalar forcing problems. Indexed research records for friendship zero-forcing polynomials and complete-multipartite \(k\)-forcing do not cover the same connected predicate and graph family. Targeted aliases, implication comparisons and prior-file claims were checked. Inaccessible or unindexed equivalent literature remains a residual priority risk; indexed silence is not a novelty proof.

## Mathematical value — PASS

The 2020 result gives only the number of initially black vertices required in a friendship graph. The exact polynomial now measures how many *connected initial configurations* exist at every budget, including heterogeneous clique profiles where the allowable empty blades obey an integer knapsack constraint. The equal-blade specialization exposes a sharp two-unit drop of the optimum from \(3\) to \(1\) at a precisely defined forcing threshold and distinguishes peripheral versus hub singleton optimizers. This is a complete natural invariant whose budget counts cannot be obtained from the scalar minimum alone; it is not merely a renamed definition or a small isolated numerical improvement.

## Closest literature and remaining risks

The published friendship-graph minimum is stronger than a mere bound for one subfamily, but it does not imply the new cardinality counts without additional structural classification. General \(k\)-forcing bounds (Amos et al., 2014) and an indexed ordinary zero-forcing polynomial do not determine connected \(k\)-forcing ensembles. Unindexed papers, alternative terminology for windmill graphs, or an unstated derivation in related propagation literature remain possible.

Self-review: passed. Independent audit: not yet performed.
