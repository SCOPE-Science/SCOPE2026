# Independent three-axis audit — 2026-09-22

Review date (UTC): 2026-09-23. Reviewer: separate AI audit. Source tree: `ad5e5991a083af600819280aa7855b045519babc`, verified unchanged before review.

## Correctness

I independently rebuilt all five displayed polytopes and recomputed their face data and illumination set-cover problems. The displayed representatives have `(V,F)` values `(8,6),(12,8),(14,12),(18,12),(24,14)` with the stated quadrilateral/hexagonal facet counts. Enumerating realizable strict sign cells of the facet-normal arrangements and solving the exact vertex-covering problems reproduces illumination numbers `8,6,6,5,4`; the listed direction sets also pass direct strict-dot checks. I additionally varied zonotope generator lengths on the three zonotopal non-cube examples and found the same numbers in sampled deformations, but that sampling is not a proof of type-wide constancy.

The accepted record contained one material logical overreach: it said the values attach to each entire Fedorov type by affine invariance. Fedorov types are combinatorial types, not affine-equivalence classes; after affine transformations are factored out, non-cube types retain continuous shape parameters. Affine invariance therefore proves the result only for affine images of each displayed representative, not for every realization of the combinatorial type. The repair narrows the title, theorem, slogan, metadata, and limitation to the five explicit canonical representatives.

## Originality

I searched illumination/covering literature using `Fedorov`, `parallelohedron`, each solid name, `illumination number`, `Hadwiger`, `Boltyanski`, and zonotope terminology. The relevant surveys and recent papers provide general illumination bounds or study other symmetry classes; I found no published exact table `8,6,6,5,4` for these five displayed representatives. The repaired claim is therefore supportably original without asserting an unproved type-wide theorem.

## Scientific value

The repaired result remains useful: it supplies five exact, independently checkable benchmark instances spanning the classical three-dimensional parallelohedron representatives, with explicit illuminating directions and complete real-direction lower-bound certificates. It is more than a sampled numerical observation because the sign-cell enumeration closes the continuum of possible directions.

## Disposition

**PASSED AFTER BOUNDED REPAIR.** The repair removes only the unjustified extension from explicit representatives to whole combinatorial types; all computed representative values and certificates are retained.
