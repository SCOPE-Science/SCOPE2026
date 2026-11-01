# Scientific review: diameter partitions of the regular 24-cell

## Correctness

The claim uses the 24 distinct roots of type \(D_4\), hence exactly four positive distance shells. The key non-obtuse classification checks every one of the \(\binom{24}{6}=134596\) six-element subsets in exact integer arithmetic, identifies precisely the 24 coordinate/diagonal classes, and checks each for possible seventh extensions. An analytic sign-vector argument then rules out four disjoint such classes; a five-facet covering provides the matching upper bound. A signed-edge intersection argument rules out four mutually positive roots, while an explicit eight-class star assignment supplies the optimal partition. The 7,656 enumeration is a complete, disjoint, integer exact-cover recurrence over all 96 admissible triangles. The full source of the finite proof is in `verify.py`, which was executed from the actual package source, and its logical coverage is described in RESULT.md. Finite enumeration is used only for finite 24-vertex assertions, never to infer an unrestricted theorem.

## Originality

The closest mathematical comparison is Voronov's 2026 quantitative Borsuk framework and finite examples, whose full accessible text was examined: it does not provide these 24-cell values. The older full text of Cohn–Conway–Elkies–Kumar concerns the same \(D_4\) roots but a different invariant, spherical energy/design optimality. The MathWorld and 24-cell geometry tables give known structural data but not the five-color threshold or the 7,656 enumeration. Searches also checked the explicit diameter ratios, chromatic threshold aliases, eight-face partitions, and existing quantitative diameter spectra for three-dimensional Platonic vertex sets. Those older three-dimensional spectra do not imply the exceptional four-dimensional five-color obstruction. Remaining priority risk: an unindexed or historical specialized 24-cell coloring enumeration could contain some of the finite counts; failure to locate one is not proof of priority.

## Mathematical value

This is the first exceptional self-dual regular four-dimensional polytope, and its exact distance graph exhibits a nontrivial gap between the naive cardinality lower bound (four) and true chromatic threshold (five). The full \(k\)-partition law and the face-exact-cover polynomial give structural, finite and reproducible benchmarks for quantitative Borsuk partition theory. The total count is a natural exact invariant of this canonical configuration rather than an arbitrary sample or isolated numerical experiment. The signed-coordinate refinement distinguishes two natural root-support patterns, while its dependence on coordinates is disclosed.

## Scope of assessment

Correctness, originality relative to inspected material, and mathematical value pass the self-review. This is not an independent external certification, and historical priority is not guaranteed.

Self-review: passed. Independent audit: not yet performed.
