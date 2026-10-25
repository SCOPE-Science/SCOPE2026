# Mathematical review

## Correctness — PASS
The observation is exactly the first two power sums of the ordered counts of preceding \(a\)'s at the \(b\) markers. The proof handles \(m\le2\), \(k\le2\), the exhaustive first-collision length-seven frontier, and the all-\(r\) norm shell with residue and boundary conditions. The classical six-unit prime-factor count in \(\mathbb Z[\omega]\) gives the exact claimed preimage cardinality. The supplied independent direct-subsequence and moment-encoding check agrees at lengths zero to ten; a separate norm-shell word-construction check agrees for \(1\le r\le9\). Finite tests do not prove the unbounded statement; the unique-factorization and sector argument does.

## Originality — PASS (with residual risk)
The closest source, Fleischmann–Lejeune–Manea–Nowotka–Rigo (arXiv:2001.11218, Section 3), introduces the relevant RBB reconstruction and integer-equation framework, supplies a general sufficient query bound, and treats one-query uniqueness. The paper's inspected Sections 3–5 do not present the two-moment length-seven collision frontier, the norm-shell classification for exactly three \(b\)'s, or growing explicit fiber sizes. Richomme–Rosenfeld (STACS 2023) addresses adaptive queries rather than this fixed projection. Classical Eisenstein factorizations supply only the number-theoretic ingredient. Further indexing limitations and alternate terminology remain a risk; these are not proofs of priority.

## Mathematical value — PASS
A natural minimal fixed observation in scattered-subword reconstruction has a surprisingly sharp marker-count dichotomy (at most two \(b\)'s always unique versus exactly three with arbitrarily large ambiguity). The theorem supplies an exact first-collision boundary and a parametrized exact family of fiber cardinalities, furnishing concrete lower bounds for ambiguity in a weak reconstruction channel. This is more informative than a routine example or a mere computation.

## Limits
No classification of all ambiguity fibers or general maximum multiplicity formula is claimed. A published equivalent reformulation not indexed or inspected remains possible. The norm representation lemma is classical.

Self-review: passed. Independent audit: not yet performed.
