# Scientific review

## Correctness — PASS

The exact scope is fixed by binary words of lengths three and four, both represented, and Kraft equality. The equation \(2a+b=16\) gives seven exhaustive cases; choosing the two word sets accounts for exactly 1,901,636 potential codes with no duplicates. Literal Sardinas--Patterson suffix-set iteration and an independently written bitmask transition-graph implementation both examined every case, produced identical seven uniquely decodable totals and the same four exceptional word sets. The first exceptional representative has repeating nonempty remainder sets \(\{1\}\) and \(\{10,101,111\}\), disjoint from its codewords. Reversal and bitwise complementation generate the other three. Counting ordinary prefix and suffix completions and using strong connectivity of the binary de Bruijn graph proves the two 254-member classes do not intersect. The nonprefix infinite-delay deduction uses Schützenberger's existing theorem, not experimental extrapolation.

## Originality — PASS

Woryna's arXiv:1608.08381 presents the general counting problem and exact results for a different three-word profile and for divisible-length profiles with one longer word. The specific Kraft-equality word-set count for lengths three and four is not an instance of those formulas. Woryna's arXiv:1804.02531 supplies upper/lower proportion estimates and an exact two-word count, neither determining the present multiword distribution or the four mixed exceptions. The classical Kraft--McMillan, Sardinas--Patterson, and Schützenberger theorems are used but not claimed as novel. Related fixed-length and fix-free enumerations cover different code properties. A prior unindexed exact census cannot be excluded.

## Value — PASS

Prescribed-length uniquely decodable code counts are a recognized mathematical question, and equality in Kraft--McMillan singles out maximal, zero-slack designs. The exact 512-element classification isolates only four noncanonical codes between the 254 prefix and 254 suffix completions; they form a single complement-and-reversal orbit. This identifies and exhausts the exception to the natural prefix-or-suffix construction at a complete, variable-length binary profile, while separating immediate from unbounded-delay decoding. The case is finite but natural, complete, and not implied by the known general inequalities. No broader theorem or application is asserted.

## Closest literature and limitations

Primary comparisons: Woryna (2016), arXiv:1608.08381 (sections 1--4); Woryna (2018), arXiv:1804.02531 (introduction and exact two-word theorem); Berstel--Perrin--Reutenauer, *Codes and Automata*, chapter 5, Theorem 5.2.4 (known finite-delay restriction). Direct comparisons to associated published fix-free and non-overlapping results find stronger code constraints, not an implication of these uniquely decodable counts. The Derencourt (1996) study of prefix/suffix-composition of three-word codes was not accessible in full and is retained as a bibliographic risk, though it does not purport to enumerate the stated many-word Kraft boundary. The enumeration is certified by two reproducible finite methods, not by independent external audit.

Self-review: passed. Independent audit: not yet performed.
