# Same-model review

## Correctness
PASS. The proof was reconstructed from the exact H-descriptions in the cited survey. For a facet supported on a \(k\)-set, the intrinsic normal in the affine hyperplane has norm \(\sqrt{k(n-k)/n}\), and the common barycenter has slack \(k(n-k)/2\). Hence its facet distance is \(\frac12\sqrt{nk(n-k)}\), minimized exactly at \(k=1\) or \(k=n-1\). Singleton facets give the sharp all-center bound and uniqueness for the permutahedron and associahedron. The two parallel endpoint facets give the same sharp upper bound for the parallelepiped; its complete center set follows by solving all prefix/suffix distance inequalities. Low-dimensional duplicate facet families are handled separately.

## Originality
PASS. The closest source, Pilaud--Santos--Ziegler's *Celebrating Loday's Associahedron*, was inspected in full at the relevant sections and page images. It gives the common affine hyperplane, the three facet descriptions, removahedron nesting, and the previously known common vertex barycenter. It contains no occurrence of “inradius,” “circumradius,” “Chebyshev,” or “radius.” Direct, exact-formula, and shared-barycenter searches found no covering metric theorem. The older center-of-gravity theorem concerns vertex barycenters and does not imply an inradius statement. Current and prior own ledgers contain no associahedron/Loday radius result.

## Value
PASS. The literature presents these three polytopes as a canonical nested trio and calls their common vertex barycenter a surprising geometric property. The finding shows that they also share the exact inradius
\[
\frac{\sqrt{n(n-1)}}2
\]
and that the same distinguished point is an incenter in all three. It further separates their optimal-center geometry: the permutahedron and associahedron have unique incenters, while the parallelepiped has an explicit \((n-3)\)-dimensional incenter family for \(n\ge4\).

## Closest literature and limitations
The structural inputs are published and strong enough to make the metric proof short, but the metric conclusion was not located in the inspected or searched literature. A folklore or differently phrased generalized-permutahedron observation remains a residual risk. The theorem is specific to the canonical Loday realization and intrinsic Euclidean metric; other associahedron realizations are outside the claim.

Same-model review: passed. Independent audit: not yet performed.
