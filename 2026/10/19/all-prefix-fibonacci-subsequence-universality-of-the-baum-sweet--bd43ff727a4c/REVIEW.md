# Self-review

## Correctness — PASS
The argument is an infinite proof: a digit-carry analysis gives exactly the adjacent `11` pairs, greedy arch factorization equates the universality index with the arch count, and each one beyond the fixed eight-symbol prefix contributes one completed arch except at a precisely characterized unfinished pair. A separate regular-language count proves the Fibonacci specialization. Independent literal and automaton generators and a next-occurrence shortest-absent dynamic program checked all prefixes through length \(2048\) and larger selected cutoffs; no finite check is extrapolated to infinity.

## Originality — PASS against inspected material
The closest general result is the arch/universality identity in Schnoebelen–Veron, already implicit in prior work. It supplies the *method*, not an all-prefix formula for the Baum–Sweet automatic word. Hofman–Martens studies separability of regular languages using short subsequences, a distinct implication direction. Specific semantic literature and database searches for Baum–Sweet subsequence universality and its precise Fibonacci/cutoff formula did not locate stronger coverage. A generic linear-time algorithm evaluated on arbitrary input is not a formula for this fixed infinite sequence. Risk: an unindexed sequence-specific result could already contain the formula.

## Mathematical value — PASS
Subsequence universality is a natural measure of the richness of a finite word's scattered factors; the exact index for *every* prefix of a classical sparse automatic sequence, with an explicitly identified exceptional set and Fibonacci growth along powers of two, exposes a nontrivial interaction between the automatic digit language and combinatorial coverage. The finding is not a finite table or an arbitrary cut-off. It also supplies an exact shortest-absent-length law for all prefixes, but deliberately does not count the absent words.

Self-review: passed. Independent audit: not yet performed.
