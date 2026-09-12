# Flip-graph of minimum-genus orientable embeddings of K(4,7) is disconnected: two explicit isolated genus-3 rotation systems

## Context and motivation

The admitted target asks whether the flip-graph of minimum-genus orientable
cellular embeddings of the complete bipartite graph K(4,7) is connected. The
graph K(4,7) has bipartition sizes 4 and 7 (11 vertices, 28 edges) and minimum
orientable genus g = ceil((4-2)(7-2)/4) = 3, a classical Ringel formula. Its
cellular embeddings are encoded by rotation systems (cyclic order of neighbours
at each vertex), with faces traced by the standard Heffter-Edmonds rule. The
target defines the flip-graph with vertices the non-isomorphic minimum-genus
orientable rotation systems and edges single-vertex rotation flips that keep
the embedding cellular of genus 3, taken up to relabelling. The question is
whether this reconfiguration graph is connected. This is a natural exact
two-sided decision problem in topological graph theory: either an explicit
genus-preserving flip path connects representatives, or a flip-invariant (here,
isolation of distinct vertices) separates components. Reconfiguration and
re-embedding questions for cellular embeddings are recognised topics (rotation
systems, face tracing, isomorphism under S4 x S7 relabelling), so the object
(K(4,7)), the invariant (flip-graph connectedness / isolated vertices), and the
method (rotation-system enumeration) were all motivated before computation.

## Definitions

- K(4,7): bipartition A = {a0..a3}, B = {b0..b6}; V = 11, E = 28.
- Minimum orientable genus g(K(4,7)) = ceil((4-2)(7-2)/4) = 3. By Euler,
  V - E + F = 2 - 2g, so cellular genus 3 is equivalent to F = 13 faces.
- Since K(4,7) is bipartite, every face has even length >= 4. With 2E = 56
  face-edge incidences and F = 13, excess = 56 - 4*13 = 4, so exactly two
  face-length multisets are possible: type A (eleven 4-faces and two 6-faces)
  and type B (twelve 4-faces and one 8-face).
- A rotation system lists, at each A-vertex, a cyclic order of the 7 B-neighbours
  (7! = 5040 linear orders) and, at each B-vertex, a cyclic order of the 4
  A-neighbours (4! = 24 linear orders). Faces are traced by the standard rule:
  arrive at v along (u,v), depart toward the predecessor of u in rot(v); the
  successor convention gives the same face count (both tested by the authors and
  the auditor).
- A single-vertex flip means an arbitrary reordering of the rotation at exactly
  one vertex. Cyclic shifts of the original row represent the same rotation
  system (6 shifts at an A-vertex, 3 at a B-vertex) and are trivial self-loops.
  A flip-graph edge requires a genuinely different rotation at that vertex that
  still yields F = 13, taken up to graph relabelling (S4 x S7).
- Isomorphism is via S4 x S7 relabelling preserving cyclic orders; mirror-image
  (globally reversed) pairs were additionally checked and do not affect the verdict.

## Result (headline claim)

The flip-graph of non-isomorphic minimum-genus (genus 3) orientable rotation
systems of K(4,7), with edges given by single-vertex rotation reorderings
preserving cellular genus 3 up to S4 x S7 relabelling, is DISCONNECTED. The two
explicit genus-3 embeddings E1 and E2 below (both with face lengths eleven 4s
and two 6s) are non-isomorphic and each is an isolated vertex: exhaustive
enumeration of every single-vertex reordering shows every genus-3 reordering is
a cyclic shift of the original row, so no genus-3 flip path connects them.

Witness rotation systems (A-rows are permutations of b0..b6; B-rows of a0..a3):

- E1 rotA = [[6,5,4,2,1,0,3],[6,3,0,5,1,2,4],[6,0,3,4,2,1,5],[3,6,4,5,0,1,2]]
- E1 rotB = [[1,2,0,3],[0,1,2,3],[3,2,1,0],[3,2,1,0],[3,1,2,0],[1,3,0,2],[1,3,2,0]]
- E1 faces: F = 13, lengths eleven 4s and two 6s, genus 3.
- E2 rotA = [[2,6,0,4,5,3,1],[5,0,6,1,3,2,4],[4,1,3,5,6,2,0],[4,0,2,3,1,6,5]]
- E2 rotB = [[2,3,0,1],[0,1,3,2],[2,0,1,3],[1,0,2,3],[1,2,0,3],[2,0,1,3],[1,0,2,3]]
- E2 faces: F = 13, lengths eleven 4s and two 6s, genus 3.

Full machine-readable witnesses are in output/artifacts/witnesses.json.

## Proof / evidence

1. Genus: an independent directed-edge face tracer (auditor-written, separate from
   the authors' verify_final.py) gives F = 13 faces with sum 56 and sorted lengths
   [4]*11 + [6]*2 for both E1 and E2 under both predecessor and successor
   conventions. Hence g = 1 - (11 - 28 + 13)/2 = 3 by Euler. Both face types A and
   B were observed in the authors' wider census, but the witnesses are both type A.
2. Non-isomorphism: canonical labels under the full S4 x S7 relabelling (minimised
   tuple of min-cyclic-normalised rows) differ between E1 and E2. The auditor
   recomputed this by brute force over all 24 * 5040 = 120960 relabellings, so no
   fast-canonicaliser bug can explain the distinction. Mirror images (all rotations
   reversed) were also compared under the same brute-force canonicaliser and are
   distinct from each other and cross-distinct (E1-mirror != E1, E2-mirror != E2,
   E1-mirror != E2, E2-mirror != E1), so the conclusion holds under either the
   orientation-preserving or the unoriented isomorphism convention.
3. Isolation: exhaustive enumeration of every single-vertex reordering excluding the
   identity row (4*(5040-1) + 7*(24-1) = 20317 candidates per embedding; 20321
   including identity rows) with recomputation of F each time. The auditor's
   independent enumeration (fresh face counter plus cyclic-shift test, no
   canonical-label comparison needed) finds exactly 45 genus-3 reorderings per
   embedding, and all of them are cyclic shifts of the original row
   (6 per A-vertex x 4 = 24, 3 per B-vertex x 7 = 21; 24 + 21 = 45). Zero
   non-shift genus-3 reorderings exist for either embedding. Hence no single-vertex
   flip leaves the isomorphism class: both E1 and E2 are isolated vertices.
   The authors' verify_final.py independently reproduces genus3flips = 45 and
   nonself = 0 (canonical label of every genus-3 neighbour equals the original).
4. Disconnectedness follows: E1 and E2 are non-isomorphic minimum-genus embeddings
   and each has no genus-3 flip to any other isomorphism class, so no genus-3 flip
   path connects them. The flip-graph therefore has at least two components (in fact
   each witness is its own singleton component).
5. Census context (not part of the headline proof): about 110 annealing seeds
   produced 70+ distinct isomorphism classes covering both face types A and B; most
   sampled type-A classes are likewise isolated while a minority of type-B classes
   have 2-4 neighbouring classes. This context shows the isolation phenomenon is
   typical, but no complete census or exact component count is claimed.

Note on "flip" reading: "flip" is interpreted as any single-vertex rotation
reordering, the strongest (most permissive) reading. Since even under this reading
E1 and E2 are isolated, disconnectedness also holds for narrower readings such as
adjacent transpositions.

## Limitations

- No complete census of minimum-genus embeddings of K(4,7) and no exact number of
  flip-graph components or isomorphism classes is claimed; disconnectedness is
  proved by two isolated vertices only.
- The result is specific to K(4,7), orientable cellular minimum-genus (genus 3)
  rotation systems, single-vertex rotation reorderings, and isomorphism up to
  S4 x S7 (with mirror pairs additionally checked).
- Verification is computational but exact: integer face-tracing and canonical
  labelling over finite rotation systems, reproducible via
  output/artifacts/verify_final.py with output/artifacts/witnesses.json.
  The auditor independently re-verified genus, non-isomorphism (brute force),
  and isolation (exhaustive non-shift test) with separately written code.

## Reproducibility

- Read output/artifacts/witnesses.json for E1 and E2 rotation systems.
- Run output/artifacts/verify_final.py: it traces faces (F = 13, genus 3),
  computes canonical labels (E1 != E2), and exhaustively enumerates all
  single-vertex reorderings (45 genus-3 each, all cyclic shifts, nonself = 0).
- Independently: implement any directed-edge face tracer with either the
  predecessor or successor convention, count faces, enumerate all
  4*(5040-1)+7*(24-1) = 20317 non-identity single-vertex reorderings per
  embedding, and test whether each genus-3 neighbour is a cyclic shift of the
  original row. Expected: 45 genus-3, 0 non-shift, for each of E1 and E2.

## References

- J. L. Gross and T. W. Tucker, Topological Graph Theory (rotation systems,
  face tracing, genus formula methods).
- B. Mohar and C. Thomassen, Graphs on Surfaces (cellular embeddings,
  Heffter-Edmonds-Ringel correspondence, Euler formula).
- G. Ringel and J. W. T. Youngs / Ringel, genus formulas
  g(K(n)) = ceil((n-3)(n-4)/12) and g(K(m,n)) = ceil((m-2)(n-2)/4).
- M. Conder and K. Stokes, New methods for finding minimum genus embeddings of
  graphs on orientable and non-orientable surfaces (2019) -- general minimum-genus
  embedding methods; does not study the K(4,7) flip-graph.
- J. H. Kwak and Y. S. Kwon, Regular orientable embeddings of complete bipartite
  graphs (2005) -- classification of regular embeddings of K(n,n); different object
  class (regular, balanced case), does not imply the K(4,7) flip-graph result.
- V. P. Korzhik and H.-J. Voss; H. Ren et al.; T. Sun -- exponential families and
  face distributions of genus embeddings of complete / complete bipartite graphs;
  asymptotic multiplicity results, no K(4,7) flip-reconfiguration theorem.
- U. Wagner and E. Welzl, Connectivity of Triangulation Flip Graphs in the Plane
  (2022) -- flip-graph connectivity for planar point-set triangulations
  (edge/point flips); different flip object from rotation-system re-embeddings.
