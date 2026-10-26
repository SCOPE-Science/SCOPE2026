# Scientific review: finite star-forest rank-three classification

## Correctness — PASS

The three-round Duplicator strategy gives the uniform reduction from all nonempty star forests to 255 canonical component-count vectors. The six equality/adjacency bits on triples are complete quantifier-free types, and iterating extension sets three times is exactly the Ehrenfeucht–Fraïssé rank-three invariant. Re-running the attached exact checker gives 22 different invariant values and a sharp maximum minimal representative order of nine. A second implementation of the actual game refutes equivalence for all 231 pairs of different class representatives. The nine-vertex lower bound applies to arbitrary forests by the size-nonincreasing reduction, not merely to the finite census.

## Originality — PASS with residual risk

Searches for rank-three star-forest theory counts, small-model bounds, forest game profiles and equivalent aliases revealed no directly matching published calculation. The closest method source, Immerman's 1999 chapter on Ehrenfeucht–Fraïssé games, explains the game theorem but the inspected chapter does not present a star-forest census. The Algor–Alon paper concerns edge-cover star arboricity, not quantifier-rank semantics. A broad comparison with earlier low-rank equivalence-relation and graph-family classifications does not logically imply this exact 22-class count: components of a star forest cannot be replaced by ordinary equivalence classes without changing the atomic relation and potentially the quantifier rank. Unknown textbook exercises or folklore remain a live risk; a search is not a uniqueness proof.

## Value — PASS

Star forests are the components used in star arboricity and a natural sparse graph class. Their complete rank-three first-order profile was not determined by the generic finite-type theorem: this finding gives a concrete twenty-two-state quotient and a sharp nine-point kernel for evaluating every rank-three sentence uniformly on arbitrary members of the class. The precise cardinal and minimal kernel, including the extremizing three-component forest, are the natural invariant and boundary; neither computation correctness alone nor an unmotivated small example is the basis for value.

Self-review: passed. Independent audit: not yet performed.
