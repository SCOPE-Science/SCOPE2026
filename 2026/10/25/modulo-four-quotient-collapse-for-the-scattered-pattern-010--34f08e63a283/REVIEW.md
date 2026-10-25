# Scientific review

**Correctness: PASS.** The proof gives exact integer-modulus update maps, a commutator-based reachability argument, and a suffix-test classification. It derives the parity obstruction \(z\equiv(x-1)y\pmod2\), proves it is sufficient for reachability, and computes the right-language equivalence classes for every modulus and target residue. The standalone minimizer tests every residue for moduli \(2\) through \(14\) and directly counts selected subsequences independently for all binary words through length \(11\). The only infinite conclusions arise from the symbolic argument, not from the test sample.

**Originality: PASS, with residual risk.** The 2019 subsequence-pattern automata paper studies frequency distributions and fixed occurrence counts rather than congruence-targeted minimal DFA sizes. The 2023 Parikh-matrix paper handles equality of ordered scattered counts and ambiguity under substitution, not modular counts of \(010\). An already established modular formula for the different pattern \(0^r1\) does not imply this palindromic three-letter result. The exact quotient criterion and the factor-four parity dependence were not located in checked sources or semantic searches. Unindexed finite-semigroup or formal-language work may nevertheless contain equivalent formulas.

**Value: PASS.** The question is a natural exact descriptional-complexity invariant for a simple three-letter scattered pattern. The answer exhibits a previously unidentified threshold based jointly on the modulus and the acceptance residue, not simply a bound or a one-modulus census. Fourfold Nerode collapse occurs exactly for odd target residues at moduli divisible by four, giving a complete structural explanation of a robust infinite-family phenomenon.

**Closest literature and limits.** See the 2019 occurrence-enumeration work and 2023 Parikh-matrix work in RESULT.md. Neither supplies the modular quotient formula by its stated hypotheses and results. Publication overlap cannot be excluded absolutely. No claim about other patterns or syntactic-monoid cardinalities is made.

Self-review: passed. Independent audit: not yet performed.
