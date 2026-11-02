# Scientific review

## Correctness — PASS
The harmonic equations follow directly from relative-fitness reproduction and uniform-neighbor replacement; self-loops cancel. All 14 nonabsorbing equations for each four-vertex graph were independently solved and checked in exact rational functions. The six insertion differences have globally positive denominators and signed numerators with explicit positive factors, except the ninth-degree crossing polynomial. Descartes' one-sign-change bound, exact endpoint signs, and a rational interval prove a unique positive root; canonical graph enumeration is exhaustive through order four. The three-vertex difference is an explicit strictly negative rational function. The standalone exact-arithmetic verifier passed. Risk: transcription errors in long polynomial coefficients are mitigated by reproducible full symbolic recomputation; no general higher-order result is inferred.

## Originality — PASS, with qualified historical priority
Broom–Rychtář–Stadler (2009, DOI 10.1080/09720502.2009.10700618) **already describe the qualitative reversal between the path and paw** at selected fitnesses. The proposed advance is not this observation, but an exact algebraic crossover, a rigorous proof of uniqueness for all positive fitness advantages, an exhaustive classification of all six four-vertex edge insertions, and the sharp minimal order. Their inspected numerical comparisons and Hindersin–Traulsen (2015, DOI 10.1371/journal.pcbi.1004437) do not provide this all-fitness classification. Broom–Rychtář (2008, DOI 10.1098/rspa.2008.0058) was accessible only at the abstract/bibliographic level; a broader exact theorem elsewhere may imply part of the result. The novelty assessment is provisional and not independently certified.

## Value — PASS
The complete small-graph answer and sharp minimum settle a natural structural boundary for the counterintuitive effect of adding a contact edge under fixed per-individual reproduction-to-neighbor selection. The exact continuous fitness interval is important where finite fitness sampling misses or mislabels rank changes; the result turns previously numerical graph-ordering evidence into a complete provable phase diagram in the first nontrivial graph size. This is a finite natural classification, not a claim of a universal large-network theorem.

## Closest literature and limitations
Lieberman–Hauert–Nowak (2005), Broom–Rychtář (2008), Broom–Rychtář–Stadler (2009), and Hindersin–Traulsen (2015). The 2009 work is closest because it explicitly reports qualitative rank reversal. The exact full 2008 text was not inspected. Only uniform single-mutant birth–death processes on connected, undirected, unweighted graphs of order at most four are covered.

Self-review: passed. Independent audit: not yet performed.
