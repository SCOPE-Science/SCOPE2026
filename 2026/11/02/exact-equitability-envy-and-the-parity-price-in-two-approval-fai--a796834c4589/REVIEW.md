# Self-review

## Correctness (PASS)

The Hall target \(\kappa=\min_{S\ne\varnothing}\lfloor|\Gamma(S)|/|S|\rfloor\) is both a necessary upper bound on exactly equal utility and a sufficient target for \(\kappa\)-slot matching. Uniform approval degree and rank-two goods yield \(\kappa\ge\lfloor d/2\rfloor\); with at least three agents, any leftover good can be assigned to a nonapprover without altering utility. Each agent approves at most \(d-\kappa\le\kappa+1\) goods outside her own bundle, proving EF1 and full EF whenever \(d\) is even. In the exact-two case, the handshake identity \(m=nd/2\) forces \(\kappa=\lfloor d/2\rfloor\) and the exact EQ welfare loss; Euler orientation supplies efficient even- and odd-degree alternatives. The assertions include empty goods, zero degree, multigraph parallel edges, and boundaries. The extracted standard-library checker corroborates 362 finite normalized instance-type configurations; the proof is analytical.

## Originality (PASS, residual priority risk)

Relevant primary mathematical texts were examined, including Hosseini et al. (2026) Section 3.3, its laminar Theorem 5 and Hall-based three-agent Appendix C, and Freeman et al. (2019) Sections 3.2–3.3 and Appendix 6.7. These establish weaker or different logical statements: EF1+EQ1 for up to seven agents or laminar families, and algorithms conditional on EQ/PO feasibility plus the known implication EQ+PO to EF; none in the inspected material establishes the present arbitrary-population rank-two exact-EQ+EF1 theorem with optimal equal utility and parity welfare frontier. Graphical EFX work is relevant but has a different fairness target. Targeted searches of mathematical research records and the accessible previous claims located no equivalent or stronger coverage. This remains a best-knowledge originality judgment, not proof of worldwide uniqueness; some ancillary graphical work was only partially accessible.

## Value (PASS)

This resolves exact equity and approximate envy simultaneously for a concrete, natural sparse-approval family outside the laminar scope, with arbitrarily many agents. More importantly, it quantifies the unavoidable loss from *exact* equity: with a regular two-approver incidence graph, parity alone gives the complete additive welfare frontier, while relaxing equity by one unit restores Pareto optimality. That comparison explains a structural fairness–efficiency tradeoff, not a trivial renaming or isolated example.

## Limits and references

The result is restricted to identical approval degrees and binary, rank-two good incidences with at least three agents. It does not imply the stronger all-goods EFX condition, nor exact EQ+PO at odd degree. Closest primary sources: Hosseini et al., arXiv:2608.26410v1 (Theorems 3, 5, 13); Freeman et al., arXiv:1905.10656 (Theorems 2 and 4); Christodoulou et al., DOI:10.1145/3580507.3597764; Hsu, DOI:10.3233/FAIA251259. Priority risks include unindexed or inaccessible equivalent combinatorial formulations.

Self-review: passed. Independent audit: not yet performed.
