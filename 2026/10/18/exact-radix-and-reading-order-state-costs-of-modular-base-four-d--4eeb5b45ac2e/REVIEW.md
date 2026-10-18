# Scientific review

## Correctness — PASS

The proof constructs one complete output automaton for each of the three input conventions and checks its semantics, including all allowed zero padding. For binary MSD, the coordinates are right-aligned and alternate-aligned counts of adjacent \(11\) pairs; a bit swaps their roles and adds the new adjacency when appropriate. The two explicit four-bit words increment these coordinates independently at third-bit value zero, proving reachability of every residue pair; suffixes exposing the two coordinates and final-bit memory prove pairwise state distinguishability. For binary LSD, completed pairs and the pending low bit give a three-phase automaton with all states reachable; the two families of suffixes \((11)^t\) and \(1(11)^t\) force incompatible residual identities if different phases were equivalent. Base-four MSD residue counting is immediately minimal. The independently run finite automaton minimizer corroborates all formulas for eight moduli and compares outputs with direct digit counting, but the infinite claim rests on the constructions and lower-bound proofs.

## Originality — PASS within examined sources

The closest primary source, Allouche–Rampersad–Rigo–Shallit–Stipulanti, arXiv:2610.03837v1, Section 2 (Lemma 6) and Section 3, introduces the \(r=3\) automatic sequence and studies its Abelian complexity, without displaying minimal DFAO counts or the three-convention general-modulus law. Zantema–Bosma (2020) develops automatic-sequence state complexity and the distinction between input conventions, whereas Moradi–Rampersad–Shallit, arXiv:2512.10017, treats state complexity of other numerical relations and linear subsequences. The exact formulas here, especially the MSD/LSD quadratic/linear separation for every \(r\ge2\), are not obtained as a statement of those works. Searches for base-four digit-three modular counting, paired-binary-block automata, equivalent residue formulations, and the exact \(2r^2\)/\(3r\) parameters found no identifiable stronger prior result. This is a best-knowledge comparison, not a claim that indexing exhausts all literature; an earlier differently phrased digit-count minimization remains the principal risk.

## Value — PASS

Minimal DFAO size is a standard structural invariant of an automatic sequence. The motivating 2026 counterexample is exhibited through a base-four uniform construction, but exact binary resource requirements had not been supplied in the examined source. Resolving them over the full natural family of modular digit counts gives a sharp, unbounded quadratic difference between MSD and LSD reading and an exact base-conversion cost. This is a motivated uniform classification, not an arbitrary finite table or an assertion that computable automata are intrinsically novel. It helps compare representations and construct minimal recognizers for the example; it does not claim a new theorem about Abelian complexity.

## Limits

The result concerns only digit \(3\) in base four, zero-indicator output, and the three specified complete automaton conventions. No broader class is classified. Earlier equivalent formulations might have escaped discovery, and no independent mathematical audit was performed.

Self-review: passed. Independent audit: not yet performed.
