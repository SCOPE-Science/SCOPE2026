# The exact 852-phase flop graph of the \(3\times2\) lattice rectangle

## Finding
For the affine Gorenstein toric threefold \(X_P\) attached to \(P=[0,3]\times[0,2]\), consider all torus-equivariant smooth crepant resolutions projective **over the affine base** \(X_P\), without quotienting by symmetries of the rectangle. Join two vertices when their fans differ by one elementary quadrilateral-diagonal exchange, i.e. by a single local toric flop. Their graph \(G_P\) has
\[
 |V(G_P)|=852,\qquad |E(G_P)|=2626,\qquad \operatorname{rad}(G_P)=10,\qquad \operatorname{diam}(G_P)=20.
\]
Its degree-multiplicity vector is
\[
(2:2,\ 3:48,\ 4:108,\ 5:176,\ 6:180,\ 7:132,\ 8:128,\ 9:34,\ 10:30,\ 11:12,\ 13:2).
\]
There is a unique unordered pair of vertices at distance \(20\), encoded by internal-edge bitmasks `0x8c3c04117` and `0x71885e0820` in the coordinate convention below. In particular any two such resolutions are linked by at most 20 elementary toric flops, and the bound is attained.

## Assumptions and scope
Work over an algebraically closed field of characteristic zero. Index the twelve lattice points of \(P\) as \((x,y)\mapsto 4y+x\), where \(0\le x\le3\) and \(0\le y\le2\). List internal primitive lattice segments in increasing lexicographic order of their endpoint-index pairs; exclude the ten unit boundary edges. A triangulation is encoded by the bitmask of its thirteen internal edges. Each fine unimodular triangulation determines a smooth, crepant toric fan subdividing the cone of \(X_P\). Regularity of the triangulation is equivalent to projectivity of the resolution over \(X_P\). A diagonal exchange between two regular fine unimodular triangulations is counted as an elementary flop precisely when its coarsened quadrilateral subdivision has a convex integral lifting certificate.

## Proof
A primitive segment joins two distinct grid vertices exactly when the coordinate differences have gcd one. Two such nonincident segments cross in their relative interiors precisely when their two strict orientation tests have opposite signs. Start with the triangulation of all six unit squares by northeast diagonals and repeatedly exchange an internal segment for a crossing primitive one, only retaining sets of thirteen pairwise compatible internal segments. Because the ten fixed boundary edges are present, a maximal compatible set of thirteen internal edges yields a triangulation: Euler's formula gives twelve triangular bounded faces of total area six and hence every face is unimodular. Explicitly checking the twelve faces and their determinant-one condition for each enumerated mask avoids reliance on this inference alone.

The exhaustive traversal produces 852 distinct masks, and every candidate swap is regenerated and checked in both directions. The independently published equality \(f(2,3)=852\) [2] proves that the traversal contains **every** fine unimodular triangulation, not merely those connected to the seed. The published width-two regularity theorem, Proposition 3.4(ii) of [2], already proves that all 852 are regular. Additionally, the file `CERTIFICATES.json` supplies an explicit integer height vector for every one of the 852 triangulations. For each of its twelve triangles and every other lattice point, the exact barycentric height defect is a strictly positive integer. Hence each triangle is a strict lower face, yielding an independent, checkable regularity certificate.

The traversal's 2626 unordered swaps are exhaustive because every allowable single diagonal exchange replaces exactly one primitive edge by the other crossing diagonal and the algorithm tests every such candidate. For **each** of the 2626 swaps the certificate file also supplies an integer height vector with the four vertices of the exchanged quadrilateral coplanar, every other lattice point strictly higher than the quadrilateral plane, and all non-exchanged triangles strict lower faces. This proves the shared coarsening is a regular subdivision and the swap represents a genuine relative toric flop wall, rather than merely an abstract combinatorial adjacency. The verifier checks all these inequalities with exact integer arithmetic, not floating-point tolerances.

Finally, breadth-first search from all 852 vertices in the resulting finite undirected graph proves radius 10 and diameter 20. The degree histogram and uniqueness of the diameter pair follow from an exact traversal of the entire adjacency dictionary. The two antipodal masks are as stated.

## Verification
Run `python3 VERIFY.py` with `CERTIFICATES.json` in the same directory, using only the Python standard library. The verifier reconstructs the point set, primitive edges, intersection tests, seed, reachable triangulations, all flip edges, every unimodular triangle, and all strictly positive integer lifting inequalities. It checks all 2626 wall certificates and independently recomputes graph distances by 852 breadth-first searches. The certificate file contains 852 strict-height vectors and 2626 quadrilateral-wall vectors, without relying on any external optimization software. Its successful exact assertions establish the stated finite counts once the standard enumeration equality \(f(2,3)=852\) from [2] is used for completeness.

## Relationship to prior work
The **number 852 is not new**: Kaibel and Ziegler [2] give \(f(2,3)=852\); their Proposition 3.4(ii) proves all width-two lattice triangulations regular. Eppstein [4] discusses the 64-triangulation \(2\times2\) case and its flip geometry. Gasparim, Simpson, Suzuki and Talha [1] provide the modern Calabi–Yau crepant-resolution interpretation and a primitive-triangulation enumeration method. Lee and Santos [3] explain secondary polytopes and regular coarsening walls. The contribution here is the complete exact \(3\times2\) elementary-flop edge, degree and shortest-path profile, including independently checkable integral wall data.

## Limitations
This is a finite, torus-equivariant, **relative-projective** classification for a single rectangle, not a classification of arbitrary nontoric resolutions or of arbitrary proper crepant birational morphisms. Known total triangulation counts and width-two regularity are expressly not claimed as new. Some equivalent tabulation might exist in external software datasets; the literature and searchable-record checks did not locate one. Independent audit has not been performed.

## References
[1] E. Gasparim, C. Simpson, B. Suzuki and R. Talha, *Calabi–Yau Threefold Singularities and their Universal Quilts*, arXiv:2609.00021v1 (first public 2026-08-21), especially §§1–3. https://arxiv.org/html/2609.00021v1

[2] V. Kaibel and G. M. Ziegler, *Counting Lattice Triangulations*, arXiv:math/0211268v2 (2002); Surveys in Combinatorics (2003), §1 and Proposition 3.4(ii). https://arxiv.org/abs/math/0211268

[3] C. W. Lee and F. Santos, *Subdivisions and Triangulations of Polytopes*, Handbook of Discrete and Computational Geometry, Chapter 16 (2017), §16.4. https://www.csun.edu/~ctoth/Handbook/chap16.pdf

[4] D. Eppstein, *Triangulations of a 3x3 grid*, September 22, 2006. https://11011110.github.io/blog/2006/09/22/triangulations-of-3x3.html
