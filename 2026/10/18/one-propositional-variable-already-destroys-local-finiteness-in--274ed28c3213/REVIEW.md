# Scientific review

## Correctness — PASS

The claim is restricted to deterministic monotone dynamics on nonempty Alexandrov preorders. The explicit infinite model decodes the original two observations from one atom by a temporal change/no-change test. The published two-observation obstruction is independently reproved for arbitrary subformula substitutions, with the finite-upset alternating chain and a two-case eventuality contradiction. The variable-free sharpness proof uses induction on semantics. Both the order direction and temporal persistence were checked, and the executable reproducer performs separate finite tests.

## Originality — PASS (with residual priority risk)

The 2026 LICS paper's Lemma 3.1 gives a two-variable obstruction, rather than sharp one-variable minimality. The primary 2006 treatment establishes local finiteness in a syntactically restricted fragment, not in the full-language unary fragment. Targeted record and literature queries for temporal single-variable encodings and equivalent local-finiteness obstructions did not reveal an equivalent theorem. Search absence is not a priority certificate; older unary-variable modal encodings remain a possible source of subsumption.

## Value — PASS

The precise number of required atomic observations is a natural expressiveness parameter for finite-model obstructions. Replacing two independent colors by a single toggling temporal signal changes the variable-resource boundary, and variable-free sharpness supplies a complete minimum-resource classification. The construction is not a renaming or special-case computation; it creates a definable temporal marker and uses it to reconstruct both required observations.

## Closest literature and limitations

Vooijs–Fernández-Duque (2026), §3, Lemma 3.1, supplies the source obstruction for two atoms; Konev–Kontchakov–Wolter–Zakharyaschev (2006), §§2–3, proves a locally finite result only for a restricted fragment. The present result does not assert a bound on satisfiability complexity, extend to arbitrary topologies, or rule out all equivalent older sources. The finite checker is supporting evidence, not an infinite proof.

Self-review: passed. Independent audit: not yet performed.
