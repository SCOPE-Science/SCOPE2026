# Scientific review

**Correctness (PASS).** The stochastic adoption model is a finite acyclic continuous-time Markov chain. Its exponential-race recurrence gives unique expectations because every nonterminal total rate is at least the number of unadopted vertices times \(a>0\). Exact symbolic substitution proves the six reflection-class formulas, positivity of eight comparison differences, and a single quadratic crossover. Smaller paths are checked by explicit positive expressions. The bundled standard-library `verify.py` independently checks all stated symbolic identities against the recurrence plus 152 exact-rational evaluations. The proof is exact; finite tests are supplementary.

**Originality (PASS with historical priority risk).** The model mechanism is not new: Bass (1969). Bertotti–Modanese (2019) treat heterogeneous mean-field adoption peaks rather than finite-path complete-adoption hitting times; Kreindler–Young (2014) use a different diffusion model; Rossman–Fisher (2021) examine advertising and seed centrality via simulations. The compared claims do not imply the exact five-path two-seed switch or its minimality. Full access to the Rossman–Fisher main text was limited, so a hidden equivalent theorem cannot be ruled out. Broader pure-birth Markov-chain algebra also could subsume this case; a direct exact-result match was not found in inspected sources.

**Value (PASS).** The two natural placements—peripheral endpoints versus nearly peripheral spaced seeds—trade off competing route coverage and fast imitation. The exact switch at a nontrivial algebraic threshold establishes an interpretable structural failure of a fixed placement recommendation at the minimal network size and supplies a reproducible benchmark for seeding algorithms with spontaneous advertising. This is not a policy estimate or a claim for general graphs.

The main residual scientific uncertainty concerns historical priority rather than the finite algebra. The date January 1, 1969 is supported by the publishing journal's issue listing and places the motivating model in the archive literature cohort.

Self-review: passed. Independent audit: not yet performed.
