# Self-review of finite caterpillar-tree finite-variable theories

## Correctness — PASS

The proof reconstructs the unique degree-at-least-two path, includes the singleton and two-vertex exceptions, and proves the four \(\mathrm{FO}^{2}\) phases by a permanent two-pebble strategy. Three reusable variables define all fixed distances on the spine. A \(k\)-variable recycling argument counts leaves up to and including \(k\), and a permanent \(k\)-pebble strategy proves the converse for arbitrarily high quantifier rank. Reversal gives the exact Burnside enumerator; clipping gives minimum representatives and sharp class-relative defining widths. Two independent standalone checks reproduced 4,935 finite logical comparisons, 3,203 structural constructions, 45,180 leaf-witness configurations and 15 orbit counts. Finite tests are corroboration, not universal proof.

## Originality — PASS (qualified)

Pikhurko–Verbitsky (arXiv:1003.4865, Section 5.1.1) bounds the individual-tree logical width and gives a sharp star example. This does not identify the infinite family of all caterpillar \(\mathrm{FO}^{k}\)-theories, unrestricted-depth equivalence, orbit counts, or least representatives. Immerman–Kozen's original/full work studies bounded-degree rooted trees in an ancestry language; the differing signature and hypotheses do not imply the claimed adjacency-language classification. The closest found mathematical research records concern directed-path bounded-rank logic and complete multipartite logical width. A separate rooted-tree fan-morphism result is about counting bounded morphisms, not \(\mathrm{FO}^{k}\)-equivalence of undirected trees. Residual risk: an unidentified general tree-composition theorem may imply all or part of the result; no exhaustive historical-priority claim is made.

## Mathematical value — PASS

The result answers the natural complete classification problem for every variable width on an infinite unbounded-degree graph family, including zero-leaf interior spine positions; it establishes a strict hierarchy, a canonical finite minimum per equivalence class and an exact reversal-orbit counting formula. The sharp variable-recycling threshold is structurally informative, not a lone computational curiosity.

## Scope and independent validation

The study excludes counting quantifiers, rooted or ordered expansions, disconnected forests and noncaterpillar trees. Full provenance and scripts are in the accompanying result and verification files.

Self-review: passed. Independent audit: not yet performed.
