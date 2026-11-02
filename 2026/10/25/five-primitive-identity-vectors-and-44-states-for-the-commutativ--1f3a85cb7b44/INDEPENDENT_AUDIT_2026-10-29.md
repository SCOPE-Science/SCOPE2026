# Independent mathematical audit

## correctness

PASS

The group law a,b was materialized on all 24 permutations. For identity words of length>24, 25 prefix positions force an identity subword of length<=24, so induction decomposes the Parikh vector into identity vectors from bounded length. The exact P_ij right-multiplication DP through total length24 independently reconstructs all 325 Parikh coordinates and agrees with the proposed five generator monoid; generator irredundancy and its even/odd modulus-4 membership normal form follow from nonnegative semigroup bounds. Periodic folding (i mod 4 beyond 9, j mod 2 beyond 3) gives 65 reachable canonical count states. Independently computing the complete DFA successor partition yields exactly 44 pairwise distinguishable right-congruence classes, with 33 classes size1, nine size2 and two size7. The finite group reduction and automaton partition exhaust all infinite words, unlike an arbitrary truncated simulation.

## originality

PASS

The general regularity and state-complexity upper bounds for commutative closures of group languages are prior theory. Hoffmann 2020 Example 4 uses the same type of 4-point permutation generators but a different accepting language based on state subsets; regular-action identity words require the full 24-element group. The five identity-count primitive vectors and exact 44-state Myhill–Nerode quotient are not supplied by the inspected general result.

## value

PASS

S4 with a 4-cycle and transposition is a standard smallest nonabelian symmetric-group test case. The exact five primitive identity-count vectors and 44-class minimal recognizer are independently useful sharp benchmarks for commutative closure/state complexity beyond qualitative regularity and broad bounds. The evidence is a complete natural exact invariant, not an arbitrary choice of finite sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
