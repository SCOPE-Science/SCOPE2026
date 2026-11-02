# Review of the exact variable-width alphabet spectrum

## Correctness

PASS. The proof separates every alphabet size below the stated cutoff by explicit formulas, including the special one- and two-variable cases. The only nonstandard step is the complete two-pebble response-pattern table above the threshold three; every pattern is witnessed using three distinct alphabet letters, and the complete list follows from the four possible equality constraints on the two vertex coordinates. For widths at least three, the defined predicates \(F\) and \(S\) compare the first and second letters of two vertices using just one locally bound third variable. Shadowing an otherwise occupied variable within a conjunct is legal because its outer assignment remains available in every sibling conjunct. The infinite strategy preserves the full coordinate-equality pattern under arbitrary pebble movement, with up to two fresh symbols needed and at least two available. The two verification programs independently check finite instances of the crucial claims. Finite computations are supporting checks, not the proof of the theorem.

## Originality

PASS, qualified by historical-priority limits. Du–Lyuu–Hsu (1993) and Hasunuma–Nagamochi (2001) concern de Bruijn and iterated line digraph network properties, not finite-variable logical indistinguishability. Grohe–Otto (2012) gives the unrestricted-depth pebble-game criterion as a general tool but no exact size cutoff for these structures. Etessami–Vardi–Wilke (1997) concerns two-variable logic on linearly ordered words with unary labels; the class and binary relation are different. Fàbrega–Martí-Farré–Muñoz (2023) determines orbit and distance-layer data under alphabet permutations, not the set of all bounded-variable first-order theories. The reviewed searches of equivalent phrasings, stronger characterizations, and published records found no direct or dominating result. A previously unrecognized stronger general theorem about line digraphs or first-order interpretations could imply the finding; that risk is not settled by negative searches.

## Mathematical value

PASS. This is a complete, sharp variable-resource spectrum for a classical network digraph family, not a finite or arbitrary parameter slice: it treats every alphabet size and every positive variable width at unlimited quantifier depth. It identifies a genuine nonuniform threshold—the two-variable cutoff is three, whereas widths at least three reveal two alphabet symbols per available vertex variable. The result yields exact theory counts, canonical smallest representatives, and the minimum distinguishing width between any two family members. Those logical invariants are natural questions for graph encodings and finite-variable model theory.

## Scope and remaining risk

The pure directed adjacency relation, including loops, is essential; stronger languages and different de Bruijn word lengths are not covered. The proof is a self-review reconstruction, not independent validation. Source-date provenance follows the earliest exact publisher date verified among the cited graph sources; undated earlier historical material may exist.

Self-review: passed. Independent audit: not yet performed.
