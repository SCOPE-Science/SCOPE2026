# First-order angular transition law for central dodecahedron section types

## Finding

Let \(\varphi=(1+\sqrt5)/2\) and define the regular dodecahedron \(D\subset\mathbb R^3\) as the convex hull of
\[ (\pm1,\pm1,\pm1),\quad (0,\pm\varphi^{-1},\pm\varphi),\quad (\pm\varphi^{-1},\pm\varphi,0),\quad (\pm\varphi,0,\pm\varphi^{-1}). \]
Choose \(U\) uniformly on \(S^2\); independently conditional on \(U\), choose \(T\) uniformly on the circle of unit tangent vectors at \(U\). For \(0<t\ll1\), put \(U_t=\cos(t)U+\sin(t)T\). Let \(N(u)\) be the number of sides of the central section \(D\cap u^\perp\) for a generic plane normal \(u\).

Set
\[ h=\arccos\!\left(\frac{3+\sqrt5}{4\sqrt2}\right),\qquad p=\arccos\!\left(\frac{1+3\sqrt5}{8}\right). \]
Then the complete off-diagonal first-order *joint* transition law is
\[
\begin{aligned}
\Pr(N(U)=6,N(U_t)=8)&=\Pr(N(U)=8,N(U_t)=6)=\frac{30h}{\pi^2}t+O(t^2),\\
\Pr(N(U)=8,N(U_t)=10)&=\Pr(N(U)=10,N(U_t)=8)=\frac{15p}{\pi^2}t+O(t^2),\\
\Pr(N(U)=6,N(U_t)=10)&=\Pr(N(U)=10,N(U_t)=6)=O(t^2).
\end{aligned}
\]
Consequently, because \(2h+p=\pi/3\),
\[ \Pr\bigl(N(U_t)\ne N(U)\bigr)=\frac{10}{\pi}t+O(t^2). \]
The exact one-way coefficients are approximately \(1.17980265347013\) and \(0.41174677744883\), respectively. The transition graph has no \(6\leftrightarrow10\) edge at linear order: generic section types form the path \(6\leftrightarrow8\leftrightarrow10\).

## Assumptions and scope

Both section planes pass through the origin. The orientation \(U\) has rotation-invariant surface measure and the perturbation follows a geodesic through \(U\) in a uniformly random tangent direction, at deterministic geodesic distance \(t\). The geometric shape and scale are fixed by the displayed coordinates; scaling the solid does not change its section counts. Normals giving a section containing a polyhedron vertex form ten great circles of measure zero. All statements involving \(N\) are understood almost surely away from this exceptional set. The \(O(t^2)\) constants are absolute for the fixed displayed solid.

## Proof

**1. Exact chamber model.** The 20 vertices form ten antipodal pairs. Fix representatives \(w_0,\ldots,w_9\) (the code lists the explicit algorithm for constructing them). A generic normal has the ten-bit sign mask of \(\langle u,w_i\rangle\). Crossing a great circle \(\langle u,w_i\rangle=0\) changes one bit. Because the ten axes are pairwise distinct and every three are linearly independent, the ten great circles are in general position: they yield exactly \(10^2-10+2=92\) spherical chambers and 180 spherical edges.

The exact finite certificate `verify_dodeca.py` enumerates every one of the \(2^{10}\) sign masks and every oriented candidate corner \(\pm(w_i\times w_j)\), with all sign decisions in \(\mathbb Q(\sqrt5)\). The corner criterion is necessary and sufficient: on a sphere, a polyhedral chamber vertex must lie on two independent bounding great circles, and with no triple intersections the candidate list is exhaustive. The checker derives 20 six-corner chambers whose sections have six sides, 60 three-corner chambers whose sections have eight sides, and 12 five-corner chambers whose sections have ten sides. It does not infer a global statement from random samples. For every potential dodecahedral edge it tests squared distance \(6-2\sqrt5\), recovering all 30 edges; the section side count equals the number of edges whose endpoint signs differ.

**2. Shared-interface classification.** Each spherical chamber edge lies on exactly one of the ten great circles and is bounded by consecutive candidate crosses with that circle's index. Its two adjacent masks differ in precisely that bit. Repeating this exact test for every mask certifies 120 unordered shared edges between six- and eight-sided section chambers, 60 between eight- and ten-sided section chambers, and none between six- and ten-sided chambers. Across every edge of the first class, the spherical length is
\[ h=\arccos((3+\sqrt5)/(4\sqrt2)), \]
and across every edge of the second, the spherical length is
\[ p=\arccos((1+3\sqrt5)/8). \]
Both lengths follow from the normalized scalar products of the two crossing vectors at the edge's endpoints; the checker verifies the exact quadratic-field values for all 180 edges. Hence the two total interface lengths are \(L_{6,8}=120h\) and \(L_{8,10}=60p\), and \(L_{6,10}=0\). Each of the ten distinct great circles has length \(2\pi\); counting its arc segments gives \(120h+60p=20\pi\) and therefore \(2h+p=\pi/3\) exactly.

**3. Spherical crossing flux.** Let \(\Gamma\) be any finite union of smooth nonintersecting open great-circle arcs, with finite endpoints and total arclength \(L\), separating two labeled regions \(A\) and \(B\) on the normal sphere. For small \(t\), local signed normal coordinates \((s,r)\) along \(\Gamma\) give the first-order one-way crossing area \(t\int_\Gamma (\nu\cdot T)_+\,ds\), averaged over the direction \(T\). Since \(T\) has uniform bearing, \(\mathbb E(\nu\cdot T)_+=1/\pi\). Dividing by total spherical area \(4\pi\) yields
\[ \Pr(U\in A,U_t\in B)=\frac{L}{4\pi^2}t+O(t^2). \]
The reverse flux has the same leading term. Smooth arc normal coordinates have uniformly bounded second-order errors; the finitely many arc endpoints contribute at most \(O(t^2)\). Two sections separated by nonadjacent chambers must cross at least two arrangement edges, which likewise requires starting within \(O(t)\) of one of finitely many arrangement vertices and therefore has probability \(O(t^2)\). Apply the flux formula to the two interface length sums and use the total-circle identity to obtain all formulas in the Finding.

## Verification

Run `python3 verify_dodeca.py` with Python 3 and SymPy installed. It checks all 1024 masks, all 90 oriented pairwise great-circle intersections, exact nonconcurrency for all 120 triples, all 30 dodecahedron edges, all 92 chamber polygons, their section side counts, all 180 shared boundary edges and their exact lengths. Its last line is `COMPLETE_EXACT_DODECAHEDRON_SECTION_CERTIFICATE_OK`. This exhaustive exact finite certificate supplies the explicit arithmetic in Steps 1–2. Step 3 is an analytic local-geometric argument valid for every sufficiently small positive \(t\); a finite calculation is not used as an infinite asymptotic proof.

## Relationship to prior work

The ten-great-circle tessellation of the normal sphere and its total of 60 spherical triangles, 20 hexagons and 12 pentagons, including numerical *areas* of those chambers, are explicitly reported in the MathPages article *N Points On Sphere all in One Hemisphere*. Those chamber counts and areas are not claimed here as new. Joseph O'Rourke's 2014 discussion identifies several cross-section polygon types in the dodecahedron but does not provide the two-view small-rotation transition law. The public paper *Exact Haar polygon-type law for central icosahedron sections* treats a different Platonic solid and a single orientation, not paired nearby orientations. The added result here is the type-marked geodesic interface classification, its two distinct exact length contributions and the first-order two-view joint transition law. A semantically equivalent formula in older spherical or stereological literature remains possible.

## Limitations

This is a first-order asymptotic for the fixed central-section model. No finite-angle transition kernel, conditional distribution of section areas or random offset-plane law is asserted. The \(O(t^2)\) direct six-to-ten bound does not identify a nonzero second-order coefficient. The tessellation cell counts were known; only its newly evaluated *marked interfaces and two-view transition law* are presented as proposed additional information. Independent scientific validation and definitive historical-priority assessment have not been performed.

## References

1. J. O'Rourke, *Regular cross-sections of a dodecahedron; analogous sections of 4-polytopes*, MathOverflow, March 30, 2014, https://mathoverflow.net/questions/161877/regular-cross-sections-of-a-dodecahedron-analogous-sections-of-4-polytopes.
2. *N Points On Sphere all in One Hemisphere*, MathPages, https://www.mathpages.com/home/kmath327/kmath327.htm, final section on the ten dodecahedral great circles (initial public date not verified).
3. *Exact Haar polygon-type law for central icosahedron sections*, October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-haar-polygon-type-law-for-central-icosahedron-sections--65970a533c4f.
