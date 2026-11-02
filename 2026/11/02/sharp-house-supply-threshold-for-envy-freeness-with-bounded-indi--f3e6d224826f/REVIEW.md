# Assessment of the sharp bounded-tier house-supply threshold

## Correctness — PASS

The domain is finite house assignment with complete transitive weak preferences, at most \(k\) nonempty tiers per agent, and one distinct house per agent. Inclusion-minimal Hall-deficient agent sets have exactly one fewer neighboring top-choice houses. Each participating agent exhausts one tier and can participate at most \(k-1\) times. With \(T\) eliminations, \(R\le\min\{(n-1)T,n(k-1)-T\}\le(n-1)(k-1)\), leaving at least \(n\) houses. Hence a top-choice matching must exist. Identical rankings with \(k\) tiers of \(n-1\) houses demonstrate sharpness. Finite exact assignment searches and a separate peeling implementation agree on \(39,329\) complete-domain profiles, with additional boundary and randomized checks. The invariant and construction are proved for every \(n,k\) by the symbolic argument; computation alone is not used as an infinite certificate.

## Originality — PASS, with residual risk

The 2019 Gan–Suksompong–Voudouris Hall-elimination algorithm is explicitly prior art; no claim is made to invent the algorithm, Hall's theorem, or envy-free house assignment. Comparison to its algorithm and structural results, the 2022 unweighted-graph envy-free matching work of Aigner-Horev and Segal-Halevi, the 2024 uncertain-preference work of Aziz et al., and the 2026 subsidy papers of Dai et al. and Teh et al. found no sharp universal formula \(k(n-1)+1\) in terms of the number of individual indifference tiers, nor the tight tier-incidence counting invariant. The result is logically neither implied by the general existence decision algorithm alone nor by positive-subsidy upper bounds without the new counting argument. An unindexed equivalent observation or a standard unpublished consequence of the 2019 algorithm is the principal priority risk.

## Value — PASS

The result supplies an exact resource-capacity law for coarse ordinal housing markets without requiring common rankings, utilities, randomness, or financial transfers. It separates a robust, always-feasible region from sharp worst-case impossibility, and yields a constructive guarantee for binary preferences at \(2n-1\) houses. It is a natural quantitative strengthening of existing matching-based envy-freeness methods, rather than an arbitrary enumeration or a renamed special case.

## Prior-work limits

The established peeling algorithm is not original here. The subsidy papers solve different optimization/online questions and do not by themselves imply the zero-subsidy supply threshold. The 2024 uncertain-preference paper concerns possible/certain envy under tie refinements, not this deterministic weak-order sharp existence guarantee. Searches cannot exclude unindexed equivalent results. The computational checker is finite-scope.

Self-review: passed. Independent audit: not yet performed.
