# Self-review

## Correctness

PASS. In every equation for a variant compartment, each gain and loss term contains a variant variable. Setting the complete variant subvector to zero therefore makes its derivative identically zero, independently of the healthy and primary-virus variables. Standard uniqueness preserves the coordinate face, and the source's normalized population conservation bounds the trajectory. The symbolic replay verifies the dependency pattern directly.

## Originality

PASS. Coordinate-face invariance is standard ODE theory, so no methodological novelty is claimed. The accepted result is the source-specific consequence that system (12), despite being presented as a mutation/variant model, cannot create a variant from variant-free data. Targeted DOI, exact-title, initialization, mutation-source, correction, and implication searches did not locate an equivalent published correction.

## Value

PASS. Endogenous creation of a new variant and competition after an exogenous introduction are scientifically different mechanisms. The source explicitly describes mutations as generating variant onset, while its printed equations preserve zero variant mass and its simulations begin with a positive variant seed. The invariant therefore changes the precise interpretation of what system (12) demonstrates and identifies the structural ingredient any endogenous-mutation extension must add.

## Closest literature and limitations

Earlier active-particle work explicitly models virus mutation, and a closely related 2022 article by the same authors discusses mutating viruses and variants. These establish broader context but do not supply the source-specific correction to system (12).

The conclusion concerns the printed equations. It does not determine whether unavailable code contained an extra mutation coupling, and it does not invalidate the study of an already-seeded variant.

Self-review: passed. Independent audit: not yet performed.
