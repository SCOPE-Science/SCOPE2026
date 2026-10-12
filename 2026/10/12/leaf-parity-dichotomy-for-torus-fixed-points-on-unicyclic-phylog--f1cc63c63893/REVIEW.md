# Review of the leaf-parity classification

## Correctness

PASS. Buczyńska's degree-one polytope is exactly the intersection of local tripod tetrahedra. The proof establishes that fractional support of an extreme point cannot contain a tree component or a cycle-with-tail component, because those subgraphs have more fractional edges than independent active constraints. The sole remaining fractional support is the unique cycle, where an odd number of unit side legs uniquely forces every cycle coordinate to one half. Binary assignments propagate from leaves through rooted attachments, yielding exactly two binary solutions for each even-parity leaf assignment and one fractional solution for each odd-parity assignment. The toric orbit decomposition then gives the Euler characteristic. Exhaustive bounded vertex checks for three graph shapes agree. The argument is symbolic for all graph sizes in scope.

## Originality

PASS with residual literature risk. The closest source is Buczyńska, arXiv:1004.1183, especially its cone definition, semigroup generator theorem, and equal-Hilbert-function theorem. Buczyńska–Wiśniewski (2007) concerns trees; Buczyńska–Buczyński–Kubjas–Michałek (2013) concerns minimal generator degrees for arbitrary graphs. The degree-two generator theorem **already supplies odd cycle-leg parity** and is not claimed as new. The inspected passages do not identify which of those generators span extremal rays, nor supply the all-unicyclic torus-fixed-point count, the even/odd *leaf*-assignment fiber sizes, or the Euler formula. In particular, a fixed Hilbert function does not determine the number of vertices of a polytope (for instance, the unit square and the area-one lattice triangle with vertices \((0,0),(2,0),(0,1)\) have the same Ehrhart polynomial \((k+1)^2\) but four versus three vertices). Semantic and exact-phrase searches did not identify a dominating published result, but negative search evidence is not a proof of global novelty.

## Value

PASS. The genus-one phylogenetic toric model is a natural class used to study graph-based group models and degenerations. Its complete shape-independent fixed-point count yields an exact topological invariant that cannot be read off merely from the known Hilbert-function invariance. More importantly, the proof identifies the two kinds of torus-fixed points and gives a natural parity-indexed description, which is useful for subsequent orbit-localization and singularity investigations. The calculation is a genuine structural classification, rather than a recomputation of a known Hilbert table or an arbitrary parameter cutoff.

## Boundaries and sources

The theorem concerns simple connected unicyclic trivalent graphs and ordinary complex Euler characteristic only, and does not determine higher Betti numbers. See the three papers cited in `RESULT.md`; a full external literature audit and independent validation are outstanding.

Self-review: passed. Independent audit: not yet performed.
