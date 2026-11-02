# A three-layer facet law for weighted book metrics

## Finding
Fix an integer \(n\ge2\) and a real parameter \(0<t\le2\). Let \(M_{n,t}=\{a,b,z_1,\ldots,z_n\}\) have distances
\[
 d(a,b)=t,\qquad d(a,z_i)=d(b,z_i)=1,\qquad d(z_i,z_j)=2\quad(i\ne j).
\]
Let \(\mathcal F(M_{n,t})\) denote the real Lipschitz-free Banach space, based at \(a\), and let \(F_n(t)\) count the facets of its unit ball. Then the **exact** count is
\[
\boxed{F_n(t)=\begin{cases}3\cdot 2^n,&0<t<2,\\2^n+2,&t=2.\end{cases}}
\]
In particular, shortening the common edge of the \(n\)-page triangular book to *any positive length below two*, including lengths smaller than one, produces a stable extra \(2^{n+1}-2\) facets relative to the endpoint where that edge is metrically redundant.

The dual extreme Lipschitz potentials have a complete classification. Write \(s=f(b)\) and \(x_i=f(z_i)\), with \(f(a)=0\). For \(0<t<2\) they are precisely the following three disjoint families, with all leaf choices independent:
\[
\begin{array}{c|c|c}
\text{layer}&s&x_i\ \text{for each}\ i\\\hline
\mathrm{I}&0&-1\ \text{or}\ 1\\
\mathrm{II}&t&t-1\ \text{or}\ 1\\
\mathrm{III}&-t&-1\ \text{or}\ 1-t.
\end{array}
\]
At \(t=2\), layers II and III each collapse to one extreme point, while layer I still contains \(2^n\) points.

## Assumptions and scope
All scalars are real. There are exactly two designated hubs and \(n\) distinct leaves; \(n\ge2\) and \(0<t\le2\). The assignment is a metric: the only potentially tight triangle inequalities are the hub-to-hub edge compared with a two-edge route through any leaf, \(t\le1+1\), and a leaf-to-leaf distance compared with their two unit routes through a hub, \(2\le1+1\). No continuum of points along the edges is included: \(M_{n,t}\) is the finite vertex metric, not the full metric graph.

The dual unit ball \(P_t=B_{\operatorname{Lip}_0(M_{n,t})}\) consists exactly of the tuples \((s,x_1,\ldots,x_n)\in\mathbb R^{n+1}\) satisfying
\[
|s|\le t,\qquad |x_i|\le1,\qquad |x_i-s|\le1 \quad(1\le i\le n).
\]
The inequalities \(|x_i-x_j|\le2\) are implied by \(|x_i|\le1\), so no metric inequalities have been omitted. In particular, \(P_t\) has dimension \(n+1\) and has zero in its interior for every \(t>0\). By the finite-dimensional Lipschitz-free duality and polarity, the number of vertices of \(P_t\) equals the number of facets of the primal unit ball.

## Proof
**Step 1: fibers over the hub difference.** For fixed \(s\in[-t,t]\), the feasible interval for each leaf is the intersection \([-1,1]\cap[s-1,s+1]\). Hence
\[
I_s=\begin{cases}[s-1,1],&0\le s\le t,\\[-1,s+1],&-t\le s\le0.
\end{cases}
\]
These formulas remain valid throughout \(0<t\le2\), since every interval is nonempty. The fiber \(\{s\}\times I_s^n\) is a product of closed intervals.

**Step 2: all vertices lie over three hub levels.** If \((s,x_1,\ldots,x_n)\) is a vertex, every leaf coordinate \(x_i\) must be an endpoint of \(I_s\): an interior leaf coordinate can be independently perturbed by a sufficiently small positive and negative amount while retaining feasibility. Suppose \(0<s<t\) and every coordinate is a fiber endpoint. Choose \(\varepsilon>0\) so that \(0<s-\varepsilon<s+\varepsilon<t\). For each \(i\), set \(x_i^\pm=1\) if \(x_i=1\), and set \(x_i^\pm=s\pm\varepsilon-1\) if \(x_i=s-1\). Both \((s\pm\varepsilon,x_1^\pm,\ldots,x_n^\pm)\) belong to \(P_t\), are distinct, and have midpoint the original point. Thus it cannot be a vertex. The argument for \(-t<s<0\) is identical, replacing the moving endpoint \(s-1\) with \(s+1\) and the fixed endpoint \(1\) with \(-1\). Consequently every vertex has \(s\in\{-t,0,t\}\).

**Step 3: all listed endpoint patterns are vertices.** At \(s=t\), the constraint \(s\le t\) is active, and each independent leaf coordinate reaches an endpoint of \(I_t=[t-1,1]\). Thus any midpoint decomposition in \(P_t\) forces both summands to have \(s=t\), and then forces each leaf coordinate to equal its prescribed endpoint; the point is extreme. The same reasoning applies at \(s=-t\), using \(I_{-t}=[-1,1-t]\). At \(s=0\), every prescribed leaf coordinate satisfies \(x_i=\pm1\). Given any midpoint decomposition, each leaf equality \(x_i=\pm1\) holds in both summands. Pick any leaf, whose value is either \(1\) or \(-1\); its two hub-distance inequalities then force the hub coordinate of both summands to be \(s=0\): for \(x_i=1\), \(|1-s|\le1\) entails \(s\ge0\), while the midpoint hub coordinate zero and the sign of each summand imply each is zero; likewise \(x_i=-1\) entails \(s\le0\) for each. Every coordinate is therefore fixed in both summands, so the point is extreme. (This conclusion holds already when \(n=1\), although only \(n\ge2\) is stated.)

**Step 4: the count and its transition.** If \(0<t<2\), the two endpoints of each interval \(I_0\), \(I_t\), and \(I_{-t}\) are distinct. Each of the three possible hub coordinates supports exactly \(2^n\) different vertex points, and the layers are disjoint because \(t>0\). Hence \(|\operatorname{vert}P_t|=3\cdot2^n\). At \(t=2\), the intervals \(I_t=[1,1]\) and \(I_{-t}=[-1,-1]\) shrink to singletons; the zero layer remains \([-1,1]^n\) with its \(2^n\) corners, making \(|\operatorname{vert}P_2|=2^n+2\). Polarity transfers these counts to facets of \(B_{\mathcal F(M_{n,t})}\). \(\square\)

## Verification
The argument proves the theorem for every real parameter in the stated range and every integer \(n\ge2\). Its essential computations are the explicit inequalities for \(P_t\), the two affine fiber formulas, the elementary midpoint exclusion for interior hub levels, and extremality at the three remaining levels. No approximate arithmetic or finite extrapolation is used in the general proof.

The standalone `check_theta_facets.py` independently enumerates every spanning tree of potentially tight distance inequalities for finite examples, solves both orientations of every tree's tight equations over rational numbers, and retains exactly the feasible potentials. Their complete sets agree with the three-layer classification for each \(n\in\{2,3,4\}\) and each \(t\in\{1/4,1/2,1,3/2,7/4,2\}\), eighteen exact checks in total. Run `python check_theta_facets.py` using Python's standard library. These finite tests check the formulas but are not substituted for the analytic proof.

## Relationship to prior work
The **unweighted** graph whose leaves each form a triangle with the common hub edge is the classical book graph. Braun and Bruegge, *Facets of Symmetric Edge Polytopes for Graphs with Few Edges* (arXiv:2201.13303, Section 4), enumerate facets for graph families built from internally disjoint paths between two hubs, including the appropriate \(t=1\) unweighted instance. That instance is therefore **not claimed as a new facet count**. The result here concerns the continuum of **weighted shortest-path metrics** with a variable hub edge, including \(0<t<1\), and identifies the persistence and the singular loss of facets at the redundant-edge boundary \(t=2\). A theorem about a fixed unweighted graph does not by itself imply this parameter-sensitive vertex classification.

Higashitani, Jochemko and Michałek, *Arithmetic aspects of symmetric edge polytopes* (arXiv:1807.07678, Section 3), treat unweighted graph symmetric-edge polytopes, which include the endpoint \(t=2\) via the complete bipartite graph \(K_{2,n}\). That endpoint is also prior art, not a new result. Gordon and Petrov, *Combinatorics of the Lipschitz Polytope* (arXiv:1608.06848), provide general polyhedral methods and generic-metric phenomena. The metric family here is nongeneric, having multiple exact tight two-edge routes, so generic vertex formulas alone do not produce the weighted piecewise count.

Cobollo, Guirao and Montesinos, *The numerical index of 2-dimensional Lipschitz-free spaces* (arXiv:2304.13183v1, first public 25 April 2023, primary MSC 46B20), motivate metric dependence of Lipschitz-free Banach-space geometry, but investigate three-point spaces and numerical indices rather than this higher-dimensional face enumeration. The claimed contribution here is **only** the exact continuous weighted transition and full dual-vertex classification; the general duality, endpoint graph examples, and elementary polyhedral tools are not claimed as new.

Published enumerations for complete bipartite snowflake metrics and complete multipartite interpolations vary all within-part distances simultaneously, while the present family keeps distinct leaf-leaf distances fixed at two and varies only the single hub-hub distance. Neither parameter specialization yields this family throughout \(0<t<2\). A separate enumeration for equilateral metrics with disjoint shortened pairs has all other distances one; it is similarly inapplicable.

## Limitations
The theorem does not determine other entries of the face vector, Banach-space numerical indices, or metrics with arbitrarily weighted spokes. At \(t=0\) the hubs would coincide and the number of metric points changes, so that nonmetric endpoint is excluded. When \(t=1\) and \(t=2\), the facet numbers are specializations of known graph-polytope results; their rederivation is part of the proof but not a novelty assertion. The key open bibliographic risk is an earlier equivalent weighted-book polytope treatment outside the inspected literature. No independent mathematical audit has been performed.

## References
1. B. Braun and C. Bruegge, *Facets of Symmetric Edge Polytopes for Graphs with Few Edges*, arXiv:2201.13303, first posted January 2022, Section 4, https://arxiv.org/abs/2201.13303 .
2. A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678, Section 3, https://arxiv.org/abs/1807.07678 .
3. Ch. Cobollo, A. J. Guirao and V. Montesinos, *The numerical index of 2-dimensional Lipschitz-free spaces*, arXiv:2304.13183v1, 25 April 2023, https://arxiv.org/abs/2304.13183 .
4. R. J. Gordon and F. Petrov, *Combinatorics of the Lipschitz Polytope*, arXiv:1608.06848, https://arxiv.org/abs/1608.06848 .
5. M. Alexander, M. Fradelizi, L. C. García-Lirola and A. Zvavitch, *Geometry and volume product of finite dimensional Lipschitz-free spaces*, arXiv:1911.10642, https://arxiv.org/abs/1911.10642 .
