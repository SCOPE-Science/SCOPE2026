# Independent mathematical audit

## correctness

PASS

For n>=3, h>0 the upper/lower bases and three adjacent side facets give exactly four active facet normals per vertex: (0,0,+1), (e_j,-k), (c e_j +/-q t_j,+k) on top, with vertical signs reversed below; k=(1-c)/(2h), c=cos(pi/n), q=sin(pi/n). An illuminating direction at the upper base requires negative vertical component and the lower base requires positive: it cannot cover both layers. Eliminating the vertical component gives the strict necessary angular condition |angle(e_j,-w)|<pi/2-pi/(2n), so one direction covers at most floor(n/2) top (or bottom) vertices. Conversely each consecutive block of <=floor(n/2) vertices admits a vertical parameter strictly between max(0,-c cos(alpha)+q sin(alpha)) and cos(alpha), producing one direction. Disjoint consecutive block partitions prove I=2ceil(n/floor(n/2)); cyclic maximal blocks weighted by 1/floor(n/2) per direction attain I*=2n/floor(n/2), matching vertex-sum lower bound. Vertex illumination implies face illumination since each face has fewer active facet constraints than an incident vertex. Independent facet-plane and constructed-block tests checked n=3,4,5,7,8,9,12 at two nonzero heights; the symbolic all-n cap and interval, not finite tests, establish universality.

## originality

PASS

Best-of-knowledge originality passes for the exact directed/fractional antiprism classification and parity gap, after distinguishing undirected X-ray lines and universal convex-body upper bounds from the precise two-layer illumination constraints. A very closely related antiprism full primary research note was read; it proves a different invariant, not the asserted parity or fractional values.

## value

PASS

Ordinary versus fractional illumination is an established convex-geometric covering invariant. The exact integral/fractional gap for a natural infinite family, abrupt even/odd dichotomy, and independence from positive aspect ratio provide meaningful structural information; no downstream theorem is necessary for this exact classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
