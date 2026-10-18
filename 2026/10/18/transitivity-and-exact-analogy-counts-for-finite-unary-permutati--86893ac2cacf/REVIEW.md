# Review: Transitivity and exact analogy counts for finite unary permutations

## Correctness — PASS

The theorem assumes a nonempty finite algebra in the language of one bijective unary operation, and uses Antić's exact four-directed, term-justification semantics. An internal arrow on an \(n\)-cycle has justifications \((u,v)\) precisely when the exponent difference is congruent to its cycle displacement modulo \(n\); an arrow crossing cycles has none. Generalized Chinese remainder compatibility therefore establishes the full analogy predicate. Target substitutions have disjoint nonempty congruence intersections, proving the required inclusion-maximality, and the four orientations preserve compatibility. The singleton trivial-justification boundary is handled. Counting compatible residue classes gives the stated exact quadruple formula; the equal-cycle equivalence classes prove sufficiency for transitivity, and unequal lengths give an explicit three-arrow counterexample. These arguments apply to all positive finite cycle lengths, not just tested sizes.

The self-contained `verify.py` independently enumerated term-witness justifications for all 127 compositions of totals one through seven, then checked the full four-directed definition for 207,541 ordered quadruples; all predictions, counts, transitivity and equivalence class sizes agreed. The finite check corroborates but does not replace the proof.

## Originality — PASS, qualified

Antić's 2022 public preprint, subsequently published in 2024 as *Analogical proportions in monounary algebras*, formulates the general monounary transitivity characterization as explicit Problem 7; its relevant definitions and results were inspected in full. That source treats general nontransitivity, finite elementary examples, congruences, and difference proportions for the infinite successor algebra, not the arbitrary finite-permutation cycle-length criterion or exact gcd enumeration proved here. Antić's earlier *Analogical proportions* gives general justification semantics but not this finite-bijective solution. A source/alias search and comparisons with published mathematical research records and accessible previous claims did not reveal stronger coverage. Related work on monounary homomorphisms and polymorphism-homogeneity concerns distinct properties. Residual risk: a published but unidentified equivalent finite-permutation treatment could exist. The result does not resolve the open general nonbijective case, and originality has not been independently certified.

## Mathematical value — PASS

The theorem answers the natural finite-bijective subclass of a precise published classification problem. It identifies exactly when an algebraic analogical-proportion relation becomes an equivalence relation, determines a least nontransitive example, and provides an exact invariant counting all proportions from the cycle-length multiset. The finite-permutation hypothesis is a canonical structural regime of monounary algebras, not an arbitrary parameter restriction; the gcd phenomenon reveals actual interaction between disjoint cycles. Neither a renaming nor an immediate textbook substitution establishes the full directed-maximality predicate, transitivity boundary, and count together.

## Sources, limitations, and review status

Inspected primary literature: C. Antić, *Analogical proportions in monounary algebras*, arXiv:2208.06829, 14 August 2022, and DOI:10.1007/s10472-023-09921-7, especially Definition 1, Theorem 5, Problem 7, and the successor difference theorem; C. Antić, *Analogical proportions*, arXiv:2006.02854 and DOI:10.1007/s10472-022-09798-y, on the general framework. Supplementary published mathematical research on unary-algebra structures was compared. The proof excludes nonpermutations; exhaustive verification only covers up to seven elements. Alternative literature terminology and stronger unlocated prior coverage remain possible.

Self-review: passed. Independent audit: not yet performed.
