# Scientific review

## Correctness — PASS

The statement quantifies over every finite directed acyclic graph with at least two distinct source-to-sink route vertices, and uses the affine hull and the natural integral flow lattice. The proof derives the width lower bound from arc-coordinate nonnegativity and an antichain that no route can intersect twice. Dilworth's theorem yields a route cover of cardinality equal to width, and averaging this cover gives the explicit upper-bound center. The proof separately establishes that the displayed coordinate inequalities characterize **all** minimizers and that positive integral route decompositions calculate codegree. The attached exact-integer verifier checks 1,393 finite graphs, independently of the general proof. There is no claim that finite testing proves the infinite result.

## Originality — PASS, with literature qualification

The closest source is von Bell et al., *Triangulations of Flow Polytopes, Ample Framings, and Gentle Algebras* (arXiv:2203.01896), which develops strength-one DAG flow polytopes, route vertices, triangulations and Gorenstein criteria. Braun–Cornejo, *Equatorial Flow Triangulations of Gorenstein Flow Polytopes* (arXiv:2408.05320), gives special balanced-network route-partition/codegree results. Their inspected statements do not imply the all-DAG Minkowski-asymmetry identity and complete center characterization: an edge-disjoint partition in a Gorenstein case differs from a possibly overlapping covering in an arbitrary DAG. The arc-poset form of Dilworth's theorem is classical, but its reflection containment and complete-center consequences are not supplied by the combinatorial result alone. General affine-symmetry literature may contain an unrecognized equivalent statement; no independent priority certification is claimed.

## Mathematical value — PASS

Minkowski asymmetry is a natural affine invariant of convex bodies and is generally nontrivial to calculate. This theorem gives it exactly for a substantial graph-polytope family, classifies its optimal centers, equates it with a natural lattice threshold, and makes it polynomial-time computable through poset matching. It applies beyond strongly planar or Gorenstein subclasses and supplies an explicit geometric explanation using coverings and antichains. The result is a complete infinite-family classification, not a finite census or trivial restatement of a pre-existing formula.

## Limits and evidence

Only acyclic unit-flow polytopes of positive dimension are covered, with no statement for capacitated, cyclic, or arbitrary-demand networks. Primary material inspected: von Bell et al., arXiv:2203.01896, Proposition 2.3 and Gorenstein sections; Braun–Cornejo, arXiv:2408.05320, definitions and Theorem 4.1. The supplied `verify.py` can be run without external dependencies. Complete literary novelty and independent verification remain open.

Self-review: passed. Independent audit: not yet performed.
