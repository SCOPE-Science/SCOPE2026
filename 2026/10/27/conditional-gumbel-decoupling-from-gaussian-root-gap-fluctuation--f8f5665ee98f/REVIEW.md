# Scientific assessment: conditional Gumbel decoupling in cyclic deposition

## Correctness — PASS

The proof fixes the model as independent rate-one exponential first-arrival clocks and defines the completed root set via three-site strict minima. Conditional memorylessness yields a **random conditional Poisson mean** \(\mu_K=p_K S_K\), where the observable count \(S_K\) of three-site survivors has exact variance and mean. The variance shows \(\mathbb E|\mu_K-e^{-x}|=O_x(K^{-1/8})\). A conditional dependency-graph Chen–Stein comparison, with mutually exclusive adjacent roots and joint probability \((2/15)e^{-5t}\) at distance two, gives a smaller Poissonization error. The early root set is measurable and differs from the final one by only \(O_{L^1}(K^{1/4})\) sites; adding a root changes each fixed gap statistic by at most two. This makes the known Gaussian gap limit asymptotically early-measurable. Conditioning proves factorization; known tightness and de-Poissonization transfer it to the process and discrete steps. Exact finite checks corroborate the local identities without being used as infinite proofs.

## Originality — PASS (best-knowledge comparison)

The nearest literature, Matijasevick (arXiv:2610.21094v1, Theorems A–B and Proposition 7.3), derives the marginal final-gap Gaussian process and the marginal last-root Gumbel law, but no conditional distribution after an expanding early history and no joint independence statement. Mansour–Rastegar–Roitershtein (arXiv:1903.12548v2) concerns root counts/gaps, without this completion-time joint law. Dörr–Heiny (arXiv:2309.17314v2) treats bivariate extreme-value limits for permutation-count statistics over independent-permutation arrays rather than a root stabilization time within a single cyclic process. Related generic normal/extreme limit theorems or established Chen–Stein techniques could imply part of the argument; none identified in the targeted primary-text and scholarly-record comparisons actually states this conditional result. This is not an independence certification against every possible general theorem.

## Mathematical value — PASS

The quantitative conditional Poisson-to-Gumbel theorem gives an **observable early-history predictor** with explicitly vanishing error, whereas two separate marginal limits cannot decide whether late completion and final spatial fluctuations remain correlated. It implies a product limit for infinitely many natural root-gap statistics and the exact normal–Gumbel decoupling for the root count. This addresses joint formation morphology versus final stabilization timing and uses a nontrivial survival-censoring argument rather than a parameter rename or trivial corollary. Restriction: uniform site rates and fixed threshold \(x\); no independent assessment.

## Closest literature and outstanding scope

Sources: Matijasevick (2026), arXiv:2610.21094v1; Mansour, Rastegar and Roitershtein (2019), arXiv:1903.12548v2; Dörr and Heiny (2024), arXiv:2309.17314v2; and the classical local-dependence Poisson approximation of Arratia, Goldstein and Gordon (1989). General joint extreme/central limit theory is an explicit priority risk. The analytical proof requires the 2026 marginal Gaussian-process limit as an input.

Self-review: passed. Independent audit: not yet performed.
