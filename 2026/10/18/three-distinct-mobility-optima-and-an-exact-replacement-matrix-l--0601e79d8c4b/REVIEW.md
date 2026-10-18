# Scientific assessment: regular-network replacement weights and mobility optima

## Correctness — PASS

The result concerns independent territorial-raider movement with one resident per vertex of a finite connected \(d\)-regular simple undirected graph for every integer \(d\ge2\) and every \(h>0\). The group-sum definition gives two distinct encounter-site types for an ordered pair: the two home sites when the bases are adjacent, and each common-neighbor site. Conditional additional-group sizes are exactly \(\operatorname{Bin}(d-1,p)\) and \(\operatorname{Bernoulli}(q)+\operatorname{Bin}(d-2,p)\), respectively. Averaging the exact \(1/(k-1)\) weight derives the claimed matrix polynomial and the precise diagonal probability. Stochastic normalization holds in each realized group, and symmetry holds after averaging.

The displayed derivative of the self-weight has the sign of \(h-1\); a strictly decreasing scalar equation gives the unique positive edge-weight optimizer, and Bernoulli's inequality establishes \(h_d^*>d\). The degree-two radical and the limiting Lambert parameter are derived from these equations. The all-degree argument is analytic; the independent rational-arithmetic checker verifies 1,044 actual matrix entries and row sums for six representative finite graphs, including triangular and triangle-free cases. No numerical experiment is substituted for the general theorem.

## Originality — PASS, with residual risk

The 2026 article by Pires and Broom studies completely mixed populations and numerical regimes with varying home fidelity, but does not give the entire adjacency-polynomial replacement matrix for arbitrary regular graphs or the sharp temperature/encounter/replacement three-peak hierarchy. Broom, Erovenko and Rychtář (2020/2021) define the general group-sum replacement weights, and Schimit, Pattni and Broom (2019) calculate network characteristics and fixation behaviour mainly through simulations. These general formulas are acknowledged as foundational and in principle allow graph-by-graph computation; they do not themselves state or classify the all-degree optimizer. The 2024 community study emphasizes asymptotically large fidelity and the 2025 predictor analysis considers complete networks. Thus familiar definitions, the special complete-mixing benchmark, the role of temperature, and known empirical correlations are explicitly excluded from the novelty claim.

Targeted published research-record searches for regular-graph territorial mobility, matrix-square replacement laws, common-neighbor corrections, and home-fidelity maximizers returned results about different graph invariants or evolutionary game dynamics, with no statement implying this formula and sharp peak hierarchy. Search failure alone does not prove novelty. An earlier but unlocated closed-form regular-network specialization of the universal group-sum definition remains the principal risk.

## Mathematical value — PASS

The sharp classification distinguishes three objective functions that are often conflated in evolutionary mobility models: an individual's total interaction temperature, an adjacent pair's raw probability of meeting, and that pair's normalized replacement weight after multiplayer crowd dilution. Their optima are provably different at **every** degree \(d\ge2\) in triangle-free regular networks, with an exact finite-degree threshold and a nontrivial high-degree limit. The full matrix reduction additionally exposes hidden heterogeneity: edges participating in triangles have larger replacement weights despite equal degree and identical vertex temperatures. The triangular prism supplies an exact rational witness. This is a motivated structural benchmark for analyzing social-interaction kernels, not a routine isolated parameter substitution or a claim about maximizing cooperation.

## Closest literature and limits

The closest general predecessor is the universal weight formula in Broom, Erovenko and Rychtář (2020/2021), itself based on earlier territorial-raider formulations. The nearest recent specialized comparison is Pires and Broom (2026), *Journal of Mathematical Biology* 93:51. The numerical broad-network predecessor is Schimit, Pattni and Broom (2019), *Physical Review E* 99:032306. The 2024 community study and 2025 complete-network predictor analysis provide additional checks. These sources support the model but do not establish fixation-probability effects of optimizing pair weights.

The theorem is limited to independent, memoryless one-resident regular graphs and the stated group-size normalization. Triangle-free hypotheses apply only to the adjacent-pair peak hierarchy; the matrix formula includes graphs with triangles. A generalized, less discoverable regular-graph formula remains an originality risk, and no independent scientific assessment has been performed.

Self-review: passed. Independent audit: not yet performed.
