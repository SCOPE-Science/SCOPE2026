# Scientific assessment: fan graphical-zonotope slice averages

## Correctness — PASS

The directional average is explicitly defined over uniform offsets across the support interval, so it must not be confused with averaging over random orientations. The proof first counts section vertices by integrated edge crossings, then uses the graphical-arrangement contraction correspondence to obtain each edge-direction multiplicity exactly. Contracting a tree edge of a cone over a tree yields a smaller tree cone and gives multiplicity \(2\cdot3^{n-2}\); contracting the apex spoke at a vertex of degree \(d\) gives a cone over a \(d\)-component forest and multiplicity \(2^d3^{n-1-d}\). Both follow directly from chromatic polynomials evaluated at \(-1\). For the fan the exact quotient is \(2\cdot3^{n-2}(1-J/(3D))\). Two applications of the path triangle inequality at each internal vertex yield \(2J\le(n-2)(D-J)\). Equality forces one common nonzero internal coordinate difference and endpoints between that value and zero; the upper equality is \(J=0\). Finite verifier checks 19,496 integer normals for both equality descriptions, exact zonotope edge enumerations at five sizes, direct slicing integrals at three sizes, and eight non-path tree cones. These checks support but do not replace the all-dimensional proof.

## Originality — PASS, with limits

Bárány and Domokos, *Same average in every direction* (first arXiv submission 2023-10-29), establish the section-edge average formula and conditions for a **constant** average, not fan-specific sharp nonconstant minima/maxima with equality normal sets. Grujić, *Counting faces of graphical zonotopes* (2016), provides chamber, acyclic-orientation and contraction face-count machinery; its face-number results are not optimized directional slicing averages. An accessible comparison with recorded mathematical claims about graphical-zonotope widths, minimum-radius cut quotients, and fan-graph symmetric-edge polytopes concerns different bodies or invariants and does not imply the exact averaged fan-section extrema. This is not a claim that the general section-edge identity, Stanley's chromatic evaluation or the contraction correspondence is new. An equivalent special-case theorem in older stereological or graph-arrangement literature remains an identifiable bibliographic risk. Exact problem and formula searches did not reveal it, but that is not a uniqueness proof.

## Mathematical value — PASS

Uniform-offset section complexity is the central invariant of the motivating 2023 problem. The fan family produces zonotopes of unbounded dimension with exponentially many vertices \(2\cdot3^{n-1}\), yet its entire sharp directional average range, the ratio tending to \(3/2\), and all optimal normal families are now explicit. The general cone-over-tree degree formula shows why this behavior arises and provides exact directional data for every tree cone, not an arbitrary isolated numerical slice. The result resolves a natural complete family rather than only incrementally estimating a constant.

## Limits and closest literature

The scalar range and optimizer classifications apply to unweighted path-cone graphical zonotopes; the tree-cone extension supplies a profile, not arbitrary-tree optimizers. All supporting numerical checks are finite. The primary literature sections were read in accessible arXiv HTML; the identified noncovering comparisons remain subject to the residual possibility of differently phrased earlier work. Independent mathematical validation has not taken place.

Self-review: passed. Independent audit: not yet performed.
