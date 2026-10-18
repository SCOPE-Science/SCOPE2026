# Independent mathematical audit

## correctness

PASS

The complete 90-tetrahedra Björner–Lutz list is available in Lutz 1999 thesis, printed p.17, Theorem 1.5, and the package verify.py reproduces its labelled 90 facet tuples. Inspection of the verifier’s actual Python assertions shows f=(16,106,180,90), all vertex incidence counts with unique degree-8 vertex 16, eight opposite triangles giving an octahedral sphere on {9,10,11,13,14,15}, and precisely missing pairs (9,13),(10,14),(11,15). Those edges all belong to tetrahedra of the deletion. Pure combinatorial argument: an octahedron’s 1-skeleton K_{2,2,2} has clique number3, so every tetrahedron on the six vertices uses at least one opposite pair. As this pair already lies in the unchanged deletion and is absent from the boundary link, any replacement 3-ball intersects deletion beyond the link, impossible by the stated local-replacement definition. Deletion of an open vertex star from the published closed triangulated homology sphere is a homology 3-ball with octahedral boundary and unchanged binary icosahedral pi1 by excision/Mayer–Vietoris and van Kampen. Source topological identification credited, not recomputed. The executable finite verifier itself is not a proof of the external topological identification.

## originality

PASS

Original primary Theorem 1.5 of Lutz (1999, printed p.17) explicitly supplies the 90 facets, f-vector and link-equivalence observations but does not state the unique minimum tetra-incidence at vertex 16, its octahedral opposite pairs all occurring in deletion, or this exact local non-refill consequence. This exact new one-step obstruction follows by meaningful but nontrivial combinatorial extraction from known data. Search in named triangulation and vertex-elimination formulations identified the current public Resultary record, not a distinct theorem subsuming the proposed local obstruction.

## value

PASS

Vertex removability and minimal local retriangulation are substantive natural obstacles in the 16-vertex combinatorial triangulation of a homology sphere. The distinguished minimal-degree vertex is the most plausible simplification target, so a precise octahedral-diagonal no-go result is an independently useful combinatorial boundary. It does not claim global minimum or a full census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
