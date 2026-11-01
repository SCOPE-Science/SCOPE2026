# Integral Euclidean Vietoris–Rips filtration of the eighteen type-\(B_3\) roots

## Finding
Let \(R\subset\mathbb R^3\) be the standard eighteen-root system of type \(B_3\), consisting of six short roots \(\{\pm e_i:1\le i\le3\}\) and twelve long roots \(\{\pm e_i\pm e_j:1\le i<j\le3\}\). Equip \(R\) with ordinary Euclidean distance, and use the **inclusive** Vietoris–Rips convention: \(K_r=\{\emptyset\ne\sigma\subseteq R:\operatorname{diam}(\sigma)\le r\}\) for \(r\ge0\).

The complete integral homotopy filtration is
\[
K_r\simeq
\begin{cases}
\bigvee^{17}S^0,&0\le r<1,\\
\bigvee^{7}S^1,&1\le r<\sqrt2,\\
\bigvee^{9}S^2,&\sqrt2\le r<\sqrt3,\\
S^2,&\sqrt3\le r<2,\\
\ast,&r\ge2.
\end{cases}
\]
The complete **reduced integral** persistence barcode comprises seventeen degree-zero intervals \([0,1)\), seven degree-one intervals \([1,\sqrt2)\), eight degree-two intervals \([\sqrt2,\sqrt3)\), and one degree-two interval \([\sqrt2,2)\). No other reduced intervals occur. In particular, the degree-two inclusion map from the stage at \(\sqrt2\) to that at \(\sqrt3\) is split-surjective onto \(\mathbb Z\); its surviving primitive class is the oriented boundary of the cuboctahedron subdivided at its six square-face centers.

## Assumptions and scope
The three coordinate vectors \(e_i\) form an orthonormal basis. Long roots have norm \(\sqrt2\) and short roots have norm \(1\); the two shells are **not** independently normalized. Distances are Euclidean chord distances, not distances along the convex hull, a graph metric, or the geodesic metric on a sphere. All assertions concern exactly this finite eighteen-point configuration and real thresholds \(r\ge0\). The homotopy types and barcodes are over \(\mathbb Z\), and hence give corresponding statements with field coefficients.

## Proof
**Distance and first stage.** The possible nonzero squared distances between distinct roots are \(1,2,3,4,5,6,8\). Their unordered-pair multiplicities are respectively \(24,36,24,15,24,24,6\), as follows by evaluating squared coordinate differences. Below distance \(1\), the vertices are isolated. At squared threshold \(1\), every edge joins a short root to a long root, and the long root \(\varepsilon_i e_i+\varepsilon_j e_j\) joins the two short roots \(\varepsilon_i e_i\) and \(\varepsilon_j e_j\). Thus \(K_1\) is the once-subdivided octahedral graph, with six original vertices, twelve subdivision vertices, and twenty-four edges. This connected graph has cycle rank \(24-18+1=7\), giving \(\bigvee^7S^1\).

**The nine-sphere stage.** Let \(B\subseteq K_{\sqrt2}\) be the triangulated geometric boundary of the cuboctahedron whose twelve vertices are the long roots. Its eight triangular faces remain triangles; subdivide each of its six square faces by the short root at the square's center, producing four triangles per square. Hence \(B\cong S^2\), with face vector \((18,48,32)\). For each long root \(\ell=\varepsilon_i e_i+\varepsilon_j e_j\), add the triangle with vertices \(\ell,\varepsilon_i e_i,\varepsilon_j e_j\) and its short-to-short edge. Call the resulting subcomplex \(Y\). There are twelve such bridging triangles. In \(Y\), every new short-to-short edge is a free face of its unique bridging triangle; twelve elementary collapses therefore retract \(Y\) to \(B\). An exact classification of all squared-distance-two cliques shows that \(K_{\sqrt2}\) consists of \(Y\) plus precisely eight additional two-simplices: the triangular facets of the octahedron on the six short roots. Each is attached along a loop in \(Y\simeq S^2\), and every such loop is null-homotopic. Attaching the eight two-cells therefore gives
\[
K_{\sqrt2}\simeq S^2\vee\bigvee^8 S^2\simeq\bigvee^9 S^2.
\]
This argument is integral and uses the attaching maps, not merely ranks over a field.

**The surviving boundary sphere.** At squared threshold \(3\), the full flag complex has \(426\) nonempty faces and face vector \((18,84,148,120,48,8)\). The complete ordered certificate in `collapse_to_boundary.json` has \(164\) free-face/coface pairs, removes exactly the \(328\) faces outside \(B\), and never removes a face of \(B\). The standalone verifier independently regenerates the metric complex and checks the unique-coface condition immediately before every removal. Thus \(K_{\sqrt3}\searrow B\cong S^2\). If \(i:B\hookrightarrow K_{\sqrt2}\), \(j:K_{\sqrt2}\hookrightarrow K_{\sqrt3}\), and \(p:K_{\sqrt3}\to B\) is the collapse retraction, then \(pji\simeq\operatorname{id}_B\). Consequently the map on degree-two integral homology induced by \(j\) is split-surjective, with a primitive rank-one image represented by the oriented cuboctahedral boundary. The other eight degree-two classes die exactly at \(\sqrt3\).

**Contractibility at all later thresholds.** At squared thresholds \(4,5,6\), exact vertex-toggle matchings of the complete face posets produce respectively \(357\), \(2783\), and \(23327\) matched pairs, leaving exactly one critical vertex in each case. The verifier exhaustively checks all \(2484\), \(29742\), and \(326574\) directed Hasse incidences for acyclicity. By discrete Morse theory each of these complexes is homotopy equivalent to a point. At squared threshold \(8\), all root pairs are allowed, so the complex is the full simplex. There are no other pairwise distances, proving every stage and all interval endpoints stated above.

## Verification
Run `python3 verify_b3_rips.py` with `collapse_to_boundary.json` in the same directory. The standard-library-only program reconstructs the eighteen coordinates, all distances and all simplices, proves the listed relative free-face collapses directly from the current face set, checks the boundary sphere's links and Euler characteristic, verifies the exact decomposition at squared threshold \(2\), independently computes mod-two ranks at the three early stages, and checks directed-Hasse acyclicity of the later Morse matchings. The recorded expected run is `verification_output.txt`, ending in `VERIFY_OK`. The JSON certificate stores vertex indices in the lexicographically sorted coordinate list and each pair as integer bitmasks \((a,b)\), where \(b\) is the unique codimension-one coface of \(a\) at the time of removal. Finite checks are exhaustive for this specified eighteen-point set; they are not extrapolated to other root systems.

## Relationship to prior work
Adamaszek and Adams (first public 2015-03-12) provide a foundational archive-period classification and persistence framework for Rips complexes of subsets of a circle; their cyclic-graph hypotheses do not apply to this non-cocircular root set. Saleh, Titz Mite, and Witzel classify the five Platonic-solid vertex sets, and Saleh's thesis treats that class and several other point-cloud experiments, but neither establishes the homotopy filtration of the union of the two type-\(B_3\) root shells. The published calculation *Complete Vietoris–Rips filtration of the Euclidean cuboctahedron* treats only the twelve **long** roots, giving a different filtration; inclusion of all six short roots changes the squared-distance levels and creates the eight additional ephemeral two-spheres. The result on Rips filtrations of subdivided complete graphs is about the graph shortest-path metric on a different family, not the Euclidean distances here. The same-object and broader-statement searches recorded in `AUDIT.json` found no theorem implying this exact eighteen-point filtration. This is a best-knowledge literature comparison, not a proof of publication priority.

## Limitations
The theorem depends on the fixed relative lengths of short and long roots and on the inclusive Euclidean metric. It does not cover independent radial deformation of the two root shells, other finite Coxeter types, equivariant integral persistence modules, or the continuous surface of the cuboctahedron. The exact certificate establishes the stated finite result; a separately indexed equivalent source could still exist.

## References
1. M. Adamaszek and H. Adams, *The Vietoris–Rips complexes of a circle*, arXiv:1503.03669, first public March 12, 2015; *Pacific Journal of Mathematics* 290 (2017), 1–40.
2. N. Saleh, T. Titz Mite, and S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388, first public February 28, 2023; *Innovations in Incidence Geometry* 21 (2024), 17–31.
3. N. Saleh, *On Vietoris-Rips Complexes of the 2-Sphere*, dissertation (2023), DOI 10.22029/jlupub-17950; especially Chapter 3, Theorem 3.2.1.
4. *Complete Vietoris–Rips filtration of the Euclidean cuboctahedron*, published research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-complete-vietoris-rips-filtration-of-the-euclidean-cuboctahedron--c10ad684de7e.
5. *The Rips filtration of the complete-graph subdivision has two consecutive sphere wedges*, published research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-rips-filtration-of-the-complete-graph-subdivision-has-two-co--fb5f0359b702.
