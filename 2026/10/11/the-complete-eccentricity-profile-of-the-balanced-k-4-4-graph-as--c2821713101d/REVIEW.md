# Independent mathematical audit

## correctness

PASS

The recursive root/component model and colored-broom model both enumerate 29,616 maximal tubings of K4,4, with exactly 70 S4×S4 color-spine patterns and orbit sizes summing to 29,616. Every tubing has 8 nested tubes including full mask 255; deleting any proper tube produces precisely two completions, yielding 7-regular graph with 103,656 undirected edges. Independent integer implementation rebuilt this entire flip graph and ran breadth-first shortest paths from ALL 70 pattern representatives (not partial sampling), obtaining eccentricity 15+s at each pattern; aggregate counts ecc19:48,20:768,21:5760,22:23040 and exact diameter22. The actual package verify.py performs a second generic-search versus broom enumeration and compares each representative to orbit_certificate.json, providing farthest witnesses. Since symmetry orbits exhaust the finite vertex set and BFS explores all 29,616 nodes each time, this is a rigorous bounded finite determination.

## originality

PASS

Exact diameter 22 of balanced K4,4 and the full 70-orbit eccentricity law are not given by the checked published graph-associahedron diameter papers. They explicitly leave the balanced regime or provide lower bounds and K2,q cases. No published SCOPE/resultary finding covering that exact flip metric was returned by relevant semantics searches. Best-of-knowledge novelty with bounded residual table-index risk.

## value

PASS

Diameter of balanced complete-bipartite graph associahedra is a specifically motivated open subfamily in published work. Resolving the canonical first genuinely balanced K4,4 at diameter 22, and classifying all 29,616 vertices by their full eccentricities, gives an independently useful exact finite metric baseline. The 70-orbit symmetry reduction makes the certificate finite and reusable; no general family theorem is needed for the value of this natural named case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
