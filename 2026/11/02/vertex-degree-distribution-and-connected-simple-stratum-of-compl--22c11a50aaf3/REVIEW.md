# Independent mathematical audit

## correctness

PASS

For K_r join independent s vertices, every acyclic orientation determines a clique total order and one of r+1 gaps for each independent vertex; hence r!(r+1)^s vertices. One-skeleton edge flips are precisely cover-arc reversals in the acyclic reachability order. Each end-gap occupant contributes one cover edge, interior occupant two, and a clique consecutive edge contributes one iff its gap is empty: d(c)=c_0+c_r+2Σc_i(interior)+Σ1[c_i=0]. Thus d−(r+s−1)=Σ max(c_i−1,0), and exponential generating functions give D_{r,s}(z)=r!s![x^s] e^{2xz}(z+e^{xz²}−1)^{r−1}. Simple orientations have distinct occupants in interior gaps; injective placement yields r!Σ_{j≤min(r−1,s)}binom(r−1,j)s!/(s−j)! 2^{s−j}. Sliding interior occupants left across empty gaps and then right-end occupants left, followed by adjacent clique-label swaps with all independent vertices in an end gap, gives connectedness through only simple orientations. Constructed degree support [r+s−1,r+2s−2] for s≥2, maximum r!(r−1); for s=1 every vertex has degree r. Independently enumerated all orientations and cover degrees for r,s=(2,1),(2,2),(3,2), matching exact histograms. No finite enumeration replaces the gap/cover proof.

## originality

PASS

Global graphical-zonotope face enumerations and global simplicity criteria are established, but neither yields this complete vertexwise degree histogram, simple vertex count and connectivity of the simple subgraph in a generally nonsimple complete-split family.

## value

PASS

A complete natural degree distribution, exact count of simple vertices, and connectivity of their induced graph together describe the local combinatorial geometry and accessible simple stratum of an infinite, nontrivial family of generally nonsimple zonotopes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
