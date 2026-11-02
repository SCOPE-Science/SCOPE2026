# Scientific assessment

## Correctness — PASS

The stated domain is every forbidden word of exactly four bits, all orders \(4\le n\le15\), and one circular covering word with unconstrained extra windows. The proof converts a candidate cover into a balanced augmentation of the complete binary de Bruijn graph. In each of 72 cases, `certificates.json` contains explicit nonnegative integer arc multiplicities and integer vertex potentials. `verify.py` reconstructs every mandatory edge, checks all vertex-balance equations, all dual inequalities, exact primal/dual equality, strong connectivity, and Eulerian witness coverage. It reported `VERIFY_OK 72 exact optima`. Independent brute-force indexed-circle enumeration at order four reported `CROSSCHECK_OK`. No all-order extrapolation is involved.

## Originality — PASS, with priority qualification

The closest inspected works are Moreno–Matamala (arXiv:0711.1695v1), which handles exactly-once periodic subshift words and lexicographically minimum sequences, and Cazaux–Rivals (2016), whose general shortest-cyclic-cover algorithm optimizes sets of circles and supplies criteria for equality with one-circle solutions. Neither inspected text supplies the 72 integer values or the finite balance/connectivity certifications for the six forbidden-four-factor symmetry types. General Chinese-postman theory gives algorithms, not this explicit numerical classification. Searches of accessible prior claims and the indexed research database identified no implication that fixes these particular table entries; unindexed tables and specializations remain risks. Failure to find an entry is not treated as a proof of uniqueness.

## Value — PASS

The six classes exhaust all sixteen binary forbidden length-four factors. Their exact single-circle covering lengths through order fifteen provide a coherent suite of natural constrained-string benchmarks and show nontrivial changes in relative extremality: `0000` yields the unique fifteen-window optimum at order four but is the largest of the six minima by order fifteen. Determining the mandatory overhead beyond the simple count of avoiding words requires the global balancing optimization, not a textbook enumeration or renaming. Exact small-order optima are useful as benchmarks for restricted-string constructions and generalization attempts.

## Closest literature and remaining limitations

The 2007 preprint was inspected in full, with attention to its definition of periodic admissibility and lexicographic objective. The 2016 accepted manuscript was inspected in its introduction, problem definitions and Section 4.2, including the distinction between a collection of cyclic strings and a single circle. Related bidirected postman work was checked at the abstract level only, not used to assert whole-document exclusion. No exact formula for orders beyond fifteen, no census of all optimum circles and no independent external audit are claimed. Historical priority remains qualified by potentially unindexed tables or published applications of general algorithms.

Self-review: passed. Independent audit: not yet performed.
