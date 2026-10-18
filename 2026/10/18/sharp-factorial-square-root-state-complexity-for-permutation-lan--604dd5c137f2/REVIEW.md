# Scientific review

## Correctness: PASS
A complete DFA for the fixed-word square root acts on the input permutation group, so the general upper bound is \(n!\). The binary witness uses a cycle and transposition, which generate all permutations; the original DFA is minimal. The key lower-bound lemma is checked directly in both cases for \(d(0)\): every nonidentity right translation changes the characteristic function of \(\{g:g^2(0)=0\}\). Consequently all \(n!\) reachable group states are pairwise distinguishable. The two-state boundary and optimality of a binary rather than unary alphabet are separately proved. Exact finite group enumeration and direct state-pair separation independently corroborate the proof. Risk: the finite checks are not a proof for unbounded \(n\); the complete argument is written in RESULT.md.

## Originality: PASS within examined evidence
Caron et al., *New tools for state complexity*, Section 5.2, Theorem 3, compute \(n^n-\binom n2\) for unrestricted deterministic automata and note alphabet restrictions; this result uses a full transformation monoid, so neither their upper-bound extremizer nor their binary-alphabet obstruction gives the exact restricted-permutation maximum. Onishchenko's 2026 result gives a nondeterministic \(n^3\) theorem, not a restricted deterministic one. Hospodár–Mlynárčik study the concatenation square, which differs from \(\{w:ww\in L\}\), and treat other operations on permutation languages. The named primary texts and scientific-record similarities inspected yielded no implication establishing this \(n!\) bound or its two-letter optimality. Risk: no finite set of searches proves absence of an unindexed or differently worded theorem.

## Value: PASS
This determines a natural operational state-complexity extremum on a major automata subclass for all \(n\), including the previously ambiguous small-state cases, and proves the optimal input-alphabet size. The factorial-versus-unrestricted \(n^n-\binom n2\) contrast is structural: invertible transitions force the input transition monoid to a group, and the right-stabilizer argument shows the upper bound cannot be reduced.

Self-review: passed. Independent audit: not yet performed.
