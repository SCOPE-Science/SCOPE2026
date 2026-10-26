# Scientific review

## Correctness — PASS

The statement uses the original model's weighted stochastic matrix, positive heterogeneous biases, connected nonbipartite support, and compatible positive initialization. The strict-odds/Jensen argument does not presuppose coordinatewise ordering of two equilibria. A maximizing odds ratio forces maximality through all edges; equality in a strictly concave Jensen inequality and odd-cycle connectivity force a constant fixed point, which contradicts \(\Gamma\ne I\). Perron sub/supersolutions establish existence when both radii exceed one; monotone bracketing gives all-interior convergence for the auxiliary iteration. Tang et al.'s Theorems 3–4 and vanishing urn increments yield almost-sure selection of the unique interior equilibrium. The exact rational three-node witness and Perron certificates are independently replayable by `verify.py`. The finite witness is a check, not a proof for arbitrary networks.

## Originality — PASS (qualified)

Tang et al. (arXiv:2308.09275, Sec. V; discussion of Thm. 3) explicitly leave arbitrary-network interior uniqueness/isolation open and already prove the endpoint conditions. Their follow-up arXiv:2310.17171 proves inference results but not an all-network interior uniqueness result. Jadbabaie et al. arXiv:2104.11172 restrict the principal analysis to complete graphs. Lins arXiv:2207.14098 concerns general order-preserving subhomogeneous iterates and does not itself identify the equilibrium count or nonrandom stochastic opinion limit for this model. Searches for the original authors, odds transforms, primitive nonlinear maps, Perron thresholds, and comparable claims found no direct statement in the reviewed research corpus. Related general uniqueness theorems may provide another proof; this remains a publication-priority risk. The novelty claim is confined to the graph-specific uniqueness and its precise stochastic selection consequence, not the published endpoint obstruction or generic monotonicity principles.

## Value — PASS

The model paper identifies interior isolation and uniqueness on arbitrary networks as an unresolved mathematical question. Proving there can be only one such equilibrium turns a set-valued asymptotic prediction into a single deterministic vector, with a constructive monotone fixed-point algorithm and sharp spectral regime classification. This affects the interpretation and computation of nonconsensus outcomes, rather than adding a routine parameter substitution or numerical instance.

## Scope and remaining uncertainties

The result assumes finite connected undirected nonbipartite weighted networks and the stated model's response kernel and urn initialization. No stochastic rate, disconnected/bipartite classification, or independent validation is established. Nonlinear Perron–Frobenius literature is a residual priority risk; standard general convergence principles were compared at the implication level but are not claimed as original.

Self-review: passed. Independent audit: not yet performed.
