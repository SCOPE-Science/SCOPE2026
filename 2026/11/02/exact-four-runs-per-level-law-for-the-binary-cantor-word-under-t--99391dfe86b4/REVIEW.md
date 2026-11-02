# Scientific review

## Correctness — PASS

The binary-selector indexing gives the cyclic gap identity \(g_j=3^{\nu_2(j+1)}\) for nonterminal gaps, with one zero closing gap. The proof covers every possible rotation (leading zeros or a leading one), and identifies all group-internal preceding bits through a first-differing-gap comparison, including the terminal marker exception. It then counts exactly \(2k\) one-runs and \(2k\) zero-runs for every \(k\ge2\). Independent literal sorting and suffix-doubling sorting corroborate finite cases; no experimental extrapolation is used for the general theorem.

## Originality — PASS, with priority uncertainty

The 2022 nonprimitive-morphism theorem already supplies \(\Theta(k)\) BWT-run growth for broad morphic families, so that order estimate is expressly excluded from any novelty claim. The additional result specifies **the exact factor four at every level** and explicitly determines the BWT output of every leading-zero group. The 2019 and 2023 full texts inspected concern other morphic constructions or generic morphism effects, and the 2016 source studies permutation complexity instead of BWT. Semantic mathematical-record searches found no equivalent formula; absence of a match is not a proof of priority. An unindexed or differently phrased earlier exact result is a residual risk, especially since the entire 2016 paper was not accessible.

## Value — PASS

The Cantor substitution is a classical nonprimitive morphism, a test case for the difference between combinatorial structure and compressibility. The precise run constant and explicit ordered block decomposition show **how** an input with \(2^{k+1}-1\) ordinary runs reorganizes into only \(4k\) BWT runs, sharpening known generic logarithmic-order statements and providing an exact all-level benchmark for cyclic text-index construction.

## Limitations

The finding concerns only finite iterates of the stated binary substitution, standard lex order, and sentinel-free circular BWT. Independent historical-priority validation is not performed. The complete 2016 permutation-complexity article was not read, and equivalence under another name cannot be ruled out.

Self-review: passed. Independent audit: not yet performed.
