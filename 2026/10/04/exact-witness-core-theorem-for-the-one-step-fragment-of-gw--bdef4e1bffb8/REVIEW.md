# Review

## Correctness

PASS. For a depth-one modal subformula, its scope is propositional, so restricting the carrier does not change that scope's value at any retained world. A box value in the restricted finite model is the minimum of the same pointwise quantities over the retained worlds; it equals the original witnessed infimum exactly when an original minimizer is retained. The diamond argument is the dual maximum statement. Applying this independently to all modal subformulas gives the exact transversal characterization. Structural induction then preserves every formula in the finite family at the root.

The sharpness model has one unique crisp witness for each \(\Diamond p_i\). Omitting any one witness changes that modal value from \(1\) to \(0\), and hence changes the conjunction. The lower and upper bounds therefore coincide at \(m+1\).

## Originality

PASS. The primary 2026 paper proves completeness and finite-model behavior by a recursive proof-search construction that introduces witness worlds for modal assignments, but the inspected full text does not state an induced-submodel minimization theorem, a one-step transversal characterization, or an exact sharp \(m+1\) root-core bound. The 2025 crisp predecessor likewise develops witnessed finite-model semantics without the checked statement.

Targeted published-finding and literature searches for one-step Gödel-modal small models, induced witness cores, modal-depth-one witnessed semantics, and hitting-set formulations did not locate an equivalent result. Depth-bounded fuzzy bisimulation literature concerns behavioral comparison rather than minimum induced cores.

## Value

PASS. Witnessedness is the central semantic restriction of GW, and the source's proof search explicitly spends worlds to realize modal extrema. The theorem identifies exactly how much of an arbitrary witnessed model must be retained for the canonical one-step fragment: the problem is a finite transversal invariant, with a sharp universal linear bound. This gives a clean benchmark for countermodel extraction, finite test generation, and any later recursive treatment of deeper modal nesting.

## Closest literature and limitations

Ferrari--Fiorentini--Giardini--Rodriguez (2026) is the direct source for witnessed fuzzy modal semantics and the general finite-model construction. Ferrari--Fiorentini--Rodriguez (2025) is the closest witnessed-crisp predecessor. Nguyen (2024) is relevant depth-bounded fuzzy-modal literature but studies bisimulation rather than induced core minimization.

A broader one-step or coalgebraic analogue may exist under different terminology. The accepted claim is restricted to the exact GW semantics and modal depth one.

Same-model review: passed. Independent audit: not yet performed.
