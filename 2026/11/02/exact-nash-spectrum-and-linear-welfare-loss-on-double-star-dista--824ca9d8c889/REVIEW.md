# Scientific review

## Correctness — PASS

The induced-coalition distance model, singleton and disconnected-coalition conventions, strict unilateral deviations, and Nash conditions match the definitions of Ganian et al. [1]. The proof exhausts the only connected-coalition possibilities in a two-hub tree. When hubs are separated, every leaf must be attached to its hub, and that configuration is stable. When joined, every nonhub agent outside the central coalition is singleton; the four rationality/no-entry inequalities are necessary and sufficient, with exactly three possible occupancy types. Counting labeled leaf choices gives \(ab+3\); the exact pairwise score accounting yields the complete welfare spectrum. Global welfare follows by considering both hub placements and bounding \(1+p+q-pq\). Direct independent brute-force validation passed 217,219 labeled set partitions; only the mathematical proof establishes the infinite result.

## Originality — PASS with remaining priority risk

The 2023 primary source [1] establishes the non-normalized model, with the same example scoring vector, plus general algorithms and complexity results. Its full 2023 conference version and expanded December 2023 preprint were inspected, including their definitions, lemmas, theorems and appendices. No exact double-star equilibrium spectrum, Nash price-of-anarchy formula, or labeled classification was identified. The 2020 distance-hedonic model [2] uses a coalition-size-normalized utility and finite score at disconnected pairs; its price-of-anarchy observations do not imply the present formulas. Previous inverse-distance models [3,4] likewise have different utilities. Relevant mathematical-record searches found no matching classified theorem; indexing coverage does not prove absolute priority. Exact source distinctions, representative search strings and residual risks are recorded in the accompanying scientific audit.

## Value — PASS

The two-hub tree is a natural minimal topology exhibiting three distinct distance scores. The theorem is a complete rather than selective equilibrium classification, gives the exact labeled count and welfare multiset, and sharply isolates an unbounded linear efficiency loss even with diameter fixed at three and treewidth one. It distinguishes the existence of an efficient Nash equilibrium from the possible severity of other Nash equilibria; this is not a consequence of an existence algorithm or a normalization change.

## Scope and limits

The result assumes positive integers \(a,b\), scoring vector exactly \((1,0,-1)\), no coalition-size normalization, and strict unilateral deviations. It establishes no classification on arbitrary trees or for other preference rules. Exhaustive computation supports only the tested sizes; specialist priority uncertainty and lack of independent external validation remain.

Self-review: passed. Independent audit: not yet performed.

## Literature

[1] Ganian et al., *Maximizing Social Welfare in Score-Based Social Distance Games* (2023), https://arxiv.org/html/2307.05061v1; extended treatment https://arxiv.org/html/2312.07632v1.

[2] Flammini et al., *Distance Hedonic Games* (2020), https://aamas.csc.liv.ac.uk/Proceedings/aamas2020/pdfs/p1846.pdf.

[3] Balliu et al., *Nash Stability in Social Distance Games* (2017), https://doi.org/10.1609/aaai.v31i1.10608.

[4] Balliu et al., *On Non-Cooperativeness in Social Distance Games* (2019), https://doi.org/10.1613/jair.1.11808.
