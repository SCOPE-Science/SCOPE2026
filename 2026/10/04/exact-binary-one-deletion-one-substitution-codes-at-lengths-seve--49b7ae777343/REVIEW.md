# Same-model review

## Correctness
PASS. The channel ball matches the primary source: one deletion and at most one substitution. Valid codes are cliques in the compatibility graph. At length seven an explicit three-word code is checked and an exhaustive four-clique search returns none. At length eight all five-cliques are enumerated: exactly 12 occur, and none has a common extending neighbor, proving that no six-clique exists. The classification and symmetry counts are read from this exhaustive list. A second implementation using different data structures and recursion reproduces the key counts.

## Originality
PASS with a residual indexing risk. The inspected 2020 primary paper defines the parameter and proves broad non-asymptotic bounds/constructions, not the exact binary values at lengths seven and eight. The inspected 2024 follow-up improves asymptotic redundancy and likewise does not state the finite classification. Targeted published-finding corpus and web searches for the exact notation, values, channel aliases, and length-eight classification returned no equivalent claim. The closest exact-small-parameter published-finding corpus records concern different deletion channels or different coding problems.

## Value
PASS. The claim pins down the first binary blocklength capable of carrying a full two-bit payload under simultaneous synchronization and substitution protection, and it completely classifies every optimum at that threshold. The 12-code census and four symmetry classes give reusable finite benchmarks for constructions and search algorithms, rather than only a single witness.

## Closest literature and limitations
The closest source is Smagloy--Welter--Wachter-Zeh--Yaakobi, arXiv:2005.09352 / ISIT 2020 / IEEE TIT 2023, which introduces the model and notation and supplies general upper bounds and constructions. Sun--Ge, arXiv:2403.11766, improves asymptotic constructions for the same binary error pattern. Neither inspected source gives the exact length-seven/length-eight values or classifies optimal length-eight codes. The result remains finite and computational and makes no general-\(n\) claim.

Same-model review: passed. Independent audit: not yet performed.
