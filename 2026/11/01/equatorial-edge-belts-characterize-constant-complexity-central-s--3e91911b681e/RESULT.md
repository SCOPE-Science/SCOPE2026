# Equatorial edge belts characterize constant-complexity central sections

## Finding
Let \(P\subset\mathbb R^3\) be a full-dimensional centrally symmetric convex polytope with center \(0\), and let \(N_P(u)\) count vertices of \(P\cap u^\perp\) for a unit normal \(u\) perpendicular to no vertex of \(P\). The following conditions are equivalent.

1. \(N_P(u)\) has the same value for all such \(u\).
2. For every vertex \(v\), the directions of the orthogonal projections onto \(v^\perp\) of its neighboring vertices, counted with multiplicity, are invariant under reversal. Equivalently, the incident edges at \(v\) pair in common two-dimensional linear planes containing \(0\).
3. The edges of \(P\) partition into \(r\) edge-disjoint equatorial belts, each consisting of all sides of the centrally symmetric convex polygon \(P\cap H\) in some two-dimensional linear plane \(H\) through \(0\).

When these conditions hold, \(N_P(u)=2r\). In particular every vertex of \(P\) has even degree, and the property is invariant under nonsingular linear transformations. For the regular octahedron, cuboctahedron and icosidodecahedron, the belt patterns are, respectively, \(3\) squares, \(4\) hexagons and \(6\) decagons; consequently their generic central sections have, respectively, \(6\), \(8\) and \(12\) sides. This equisection property is distinct from constant-size planar orthogonal projections (equiprojectivity): for example, a cube is equiprojective but has both quadrilateral and hexagonal generic central sections.

## Assumptions and scope
All polytopes are compact, convex, three-dimensional, centrally symmetric about the origin, which lies in their interiors. A direction is **generic for central sections** when \(\langle u,v\rangle\neq0\) for every vertex \(v\) of \(P\); this excludes finitely many great circles. A belt \(H\) is a two-dimensional linear plane containing \(0\) such that every edge along the perimeter of \(P\cap H\) is also an edge of \(P\). Here the partition is of actual polytope edges, not of edge incidences. No claim is made about section polygons in non-generic directions, whose vertices may themselves be vertices of \(P\).

For a vertex \(v\), let \(\mathcal N(v)\) denote its neighboring vertices. Write \(\pi_v(w)=w-\langle w,v\rangle v/\langle v,v\rangle\) for the projection onto \(v^\perp\). It is nonzero for every \(w\in\mathcal N(v)\): two different vertices of a convex body containing \(0\) in its interior cannot lie on the same ray, and antipodes cannot share an edge. The normalized projected directions are \(\pi_v(w)/\|\pi_v(w)\|\), with multiplicities.

## Proof
**1. Edge-crossing formula.** For generic \(u\), no vertex lies on \(u^\perp\). A central section vertex is the unique intersection with an edge of \(P\) joining vertices with opposite signs of \(\langle u,\cdot\rangle\), and every such edge contributes one section vertex. Thus, denoting the edge set by \(E(P)\),
\[
N_P(u)=\#\{\{v,w\}\in E(P):\operatorname{sgn}\langle u,v\rangle\ne\operatorname{sgn}\langle u,w\rangle\}.
\]
Convexity and transversality ensure no such crossing lies along a complete face or coincides with another crossing.

**2. Local jumps.** Fix a vertex \(v\) and choose a point \(u_0\) on the great circle \(v^\perp\cap S^2\), perpendicular to no other vertex except \(-v\). Such points exist: no other vertex is collinear with \(v\). Move the normal transversely across this circle, from \(\langle u,v\rangle<0\) to \(\langle u,v\rangle>0\). All signs except those at \(v,-v\) remain unchanged. Since antipodal edges occur in pairs, the change in \(N_P\) equals
\[
-2\sum_{w\in\mathcal N(v)}\operatorname{sgn}\langle u_0,w\rangle.
\]
Hence condition 1 implies that this sum vanishes for every admissible \(u_0\in v^\perp\cap S^2\).

**3. Planar sign-balance lemma.** Given a finite multiset of nonzero vectors \(p_j\) in a two-dimensional Euclidean plane, the function \(\sum_j\operatorname{sgn}\langle t,p_j\rangle\) vanishes for every direction \(t\) avoiding its finitely many zeros if and only if the multiset of *oriented* directions \(p_j/\|p_j\|\) is invariant under antipodes. The reverse implication follows by cancellation in pairs. For the forward implication, fix a line spanned by one \(p_j\), and cross one of the two perpendicular directions. The jump of the sign sum is twice the difference between the multiplicities of the two opposite orientations on that line. Since the sum vanishes on both sides, those multiplicities agree. Repeating for every unoriented line proves the lemma. Applying it to \(p_j=\pi_v(w)\) gives condition 2.

**4. From local pairs to belts.** Every edge \(\{v,w\}\) spans a unique plane \(H=\operatorname{span}(v,w)\) through \(0\), since its endpoints cannot be collinear with \(0\). Condition 2 pairs this edge, at \(v\) and separately at \(w\), with exactly one other incident edge in the same plane \(H\). There can be at most two incident polytope edges in \(H\): all lie on the boundary of the convex polygon \(P\cap H\), where exactly two polygon sides meet at \(v\). Consequently the subgraph formed by polytope edges in any fixed such \(H\) is a finite, degree-two graph. It is a disjoint union of cycles. Each cycle lies along the boundary of the convex polygon \(P\cap H\), so it must be the entire polygon boundary (no proper subcycle can be embedded in a simple boundary cycle). Thus the edges in \(H\) form exactly one equatorial belt. Every edge belongs to its unique span plane, so distinct belts have disjoint edge sets, and together they exhaust all edges. Central symmetry makes every polygon \(P\cap H\) centrally symmetric. This proves condition 3.

**5. Counting the belts.** Conversely, for every generic \(u\), the line \(u^\perp\cap H\) through \(0\) meets the boundary of each centrally symmetric belt polygon \(P\cap H\) in exactly two points. Genericity guarantees that each lies in the relative interior of a polygon edge and hence at a crossing of a genuine edge of \(P\). Since the belts partition the edge set, the crossing formula gives exactly \(2r\) section vertices independently of \(u\). This establishes condition 1, and the equivalence of all three conditions follows.

**6. Examples and transformation invariance.** The regular octahedron's twelve edges split into three square belts. Rectifying it produces the cuboctahedron, whose twenty-four edges split into four hexagonal belts. Rectifying the regular icosahedron produces the icosidodecahedron, whose sixty edges split into six decagonal belts. All three assertions can be checked using exact vertex and edge coordinates, as supplied in the standalone program. Every invertible linear map takes origin planes to origin planes and preserves polygon edges and their counts, proving affine-linear invariance. A generic cube section can have either four or six sides, which excludes it despite its known constant-size generic shadows.

## Verification
Run `python3 verify_central_belts.py` using Python 3 standard library. The program uses exact integer arithmetic in \(\mathbb Z[\sqrt5]\), independently constructs the regular icosahedron and both rectifications, reconstructs their planar edge-belt cycles, tests representative integer normal directions without vertex degeneracies, and gives a cube counterexample. Its recorded output was:

```
constant_sections 6 12 sides 6 normals 1000
constant_sections 12 24 sides 8 normals 720
constant_sections 30 60 sides 12 normals 960
cube_witness 4 6
VERIFICATION_OK
```

These tests confirm finite combinatorial instances. The equivalence for every centrally symmetric convex polytope and every generic normal is established by the preceding proof, not by finite experiments.

## Relationship to prior work
Cousaert's 2026 characterization of *equiprojective* polytopes (arXiv:2601.13095, Theorem 1.2) and the Hasan–Lubiw projection characterization it generalizes concern orthogonal **shadows** and compensate edge–face contributions. They do not establish a characterization of fixed-complexity **central sections**. Brandenburg, De Loera, Luo and Meroni (arXiv:2603.25643) develop a piecewise-algebraic theory of polyhedral slice moments, not the above edge-belt equivalence. Equatorial decagons of the icosidodecahedron and equatorial hexagons of the cuboctahedron are classical geometry and are not claimed as newly discovered configurations. The claimed result is the iff criterion with its local vertex-sign formulation and exact section-size consequence, not the individual equator identities.

## Limitations
This is a three-dimensional, centrally symmetric classification; it is not asserted for noncentrally symmetric polytopes, arbitrary affine sections, or higher dimensions. The theorem gives the constant **number** of edges of generic central sections, not equal metric shapes or areas. It does not classify all possible combinatorial types satisfying the criterion up to isomorphism. Although relevant searches and two primary full texts revealed no equivalent prior statement, historical priority is not independently certified; differently named results in older convex-polytope literature remain possible. Independent mathematical audit has not been performed.

## References
1. Alice Cousaert, *Equiprojective polytopes in higher dimension*, arXiv:2601.13095, first public January 19, 2026, https://arxiv.org/abs/2601.13095 .
2. Marie-Charlotte Brandenburg, Jesús A. De Loera, Yu Luo and Chiara Meroni, *Critical moments of slices and slabs of the cube (and other polyhedral norms)*, arXiv:2603.25643, first public March 26, 2026, https://arxiv.org/abs/2603.25643 .
3. Anna Birkemeyer, Anouk E. Brose, Marie-Charlotte Brandenburg and Niklas Prün, *Combinatorial slicing problems of polytopes: How (not) to reconstruct a polytope from its slices*, arXiv:2609.16195, September 14, 2026, https://arxiv.org/abs/2609.16195 . Only public abstract was accessible for comparison.
4. G. C. Shephard, *Twenty problems on convex polyhedra, Part II*, Mathematical Gazette 52 (1968), 1968. Its generic section problems concern attainable section sizes, not a fixed centered-section criterion.
