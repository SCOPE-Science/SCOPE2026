# Minimum-distance triangles force numerical index one half for finite graph free spaces

## Finding
Let \(G=(V,E)\) be any finite connected simple graph, with every edge of length \(1\) and its shortest-path metric \(d_G\). If \(G\) contains a triangle, then the real Lipschitz-free Banach space over its vertex metric satisfies
\[
\boxed{n\bigl(\mathcal F(V,d_G)\bigr)=\frac12.}
\]
The equality holds without restrictions on the remaining graph: adjoining vertices, paths, chords, or other cycles cannot change this value while the triangle persists. The upper bound is realized by an explicitly defined **rank-two operator** whose operator norm is \(1\) and whose numerical radius is exactly \(1/2\).

More generally, the same operator gives a metric obstruction: if \((M,d)\) is any finite metric space possessing three distinct points \(a,b,c\) such that
\[
d(a,b)=d(a,c)=d(b,c)=\min_{x\ne y}d(x,y),
\]
then \(n(\mathcal F(M))\le 1/2\). The unrestricted metric statement is an upper bound only. The graph theorem combines this obstruction with the sharp lower bound for unit-edge graph metrics.

## Assumptions and scope
All vector spaces, operators and functionals are **real**. The graph is finite, connected, undirected, simple, and unweighted; the hypothesis requires an actual three-edge cycle, not merely an odd cycle. Choose one vertex \(a\) of a triangle as distinguished basepoint, and write \(\delta_x\in\mathcal F(V)\) for point evaluations, with \(\delta_a=0\). The choice of basepoint does not affect the space up to canonical linear isometry.

For a real Banach space \(X\), define
\[
v(T)=\sup\{|f(Tx)|:\|x\|=\|f\|=1,\ f(x)=1\},\qquad
n(X)=\inf_{\|T\|=1}v(T).
\]
The dual of \(\mathcal F(V)\) is the space of functions \(f:V\to\mathbb R\) with \(f(a)=0\), equipped with the Lipschitz norm. For an edge \(uv\), its directed molecule is \(m_{uv}=\delta_u-\delta_v\). Its norm is \(1\), and the free-space unit ball is the convex hull of the finitely many directed edge molecules: every normalized molecule between nonadjacent vertices is an average of edge molecules along any shortest path.

## Proof
**1. A minimum-distance triangular obstruction.** Scale the metric so its minimum nonzero distance is \(1\), and choose \(a,b,c\) as in the finding. Define a linear map on the point-evaluation basis by
\[
T\delta_a=0,\qquad
T\delta_b=\delta_c-\frac12\delta_b,\qquad
T\delta_x=\frac12\delta_c\quad(x\notin\{a,b\}).
\]
In particular, \(T\delta_c=\delta_c/2\), and every other point outside \(\{a,b\}\) has this same image. Because point evaluations other than the basepoint are a basis, these prescriptions define an operator. Its range is exactly the span of \(\delta_b,\delta_c\); thus \(\operatorname{rank}T=2\).

For any ordered pair \(u,v\) other than \(\{a,b\}\), direct subtraction shows that \(T(\delta_u-\delta_v)\) is either zero, \(\pm\delta_c/2\), or \(\pm(\delta_c-\delta_b)/2\). Its norm is therefore at most \(1/2\), since \(d(a,c)=d(b,c)=1\). As every \(d(u,v)\ge1\), this gives
\[
\bigl\|T m_{uv}\bigr\|\le\frac12\quad(\{u,v\}\ne\{a,b\}).
\]
For the remaining molecule, the triangle inequalities give
\[
\bigl\|T m_{ba}\bigr\|=\left\|\delta_c-\frac12\delta_b\right\|=1.
\]
Indeed, a transport plan taking half a unit of mass from \(a\) to \(c\) and half from \(b\) to \(c\) costs \(1\); conversely, the function on \(\{a,b,c\}\) with values \(0,0,1\) extends to a real \(1\)-Lipschitz function on \(M\) and witnesses norm \(1\). The unit ball is the convex hull of all normalized molecules, so \(\|T\|=1\).

Fix a normalized molecule \(m_{uv}\) and a norm-one functional \(f\) with \(f(m_{uv})=1\). When \(\{u,v\}\ne\{a,b\}\), the preceding norm bound gives \(|f(Tm_{uv})|\le1/2\). Otherwise, after orienting the edge so \(f(b)-f(a)=1\), we have \(f(a)=0\), \(f(b)=1\), and the other two edges of the minimum-distance triangle force \(0\le f(c)\le1\). Consequently
\[
|f(Tm_{ba})|=\left|f(c)-\frac12\right|\le\frac12.
\]
The reverse orientation is identical after replacing \(f\) by \(-f\). Any norming pair \((x,f)\) on the unit sphere has a molecular convex decomposition \(x=\sum_j\lambda_jm_j\). Since \(1=f(x)=\sum_j\lambda_j f(m_j)\) and \(f(m_j)\le1\), every molecule with \(\lambda_j>0\) is normed by \(f\). Thus \(|f(Tx)|\le1/2\) by convexity. Finally, \(T m_{bc}=(\delta_c-\delta_b)/2=-m_{bc}/2\), so a norming functional for \(m_{bc}\) gives absolute pairing \(1/2\). Therefore
\[
\|T\|=1,\qquad v(T)=\frac12,
\]
proving the stated bound for arbitrary finite metrics with a minimum-distance equilateral triple.

**2. Universal lower bound for unit-edge graph metrics.** Let \(S:\mathcal F(V)\to\mathcal F(V)\) have norm \(1\). The finite edge-molecule convex hull ensures that some oriented edge \(uv\) satisfies \(\|Sm_{uv}\|=1\). Choose an **extreme** unit Lipschitz functional \(f\) with \(f(Sm_{uv})=1\); such an extreme maximizer exists because the dual unit ball is a finite-dimensional polytope.

We first verify an elementary graph-polytope lemma: if \(f\) is extreme, its subgraph of **tight edges** \(ij\) with \(|f(i)-f(j)|=1\) is connected. Otherwise, moving the values of \(f\) by a sufficiently small common \(\pm\varepsilon\) on a tight-edge component that omits the basepoint leaves all inequalities \(|f(i)-f(j)|\le1\) valid and expresses \(f\) as a nontrivial midpoint. Therefore tight edges contain a spanning tree. Since \(f(a)=0\), propagation along that tree proves \(f(x)\in\mathbb Z\) for every vertex. In particular \(f(u)-f(v)\in\{-1,0,1\}\).

If \(|f(u)-f(v)|=1\), then either \(f\) or \(-f\) norms \(m_{uv}\), and \(|f(Sm_{uv})|=1\) directly gives \(v(S)\ge1\). It remains to consider \(f(u)=f(v)\).

Give each graph edge \(ij\) the auxiliary length
\[
w_{ij}=2-|f(i)-f(j)|\in\{1,2\}.
\]
Because \(uv\) has auxiliary length \(2\), while any different path from \(u\) to \(v\) uses at least two edges each of auxiliary length at least \(1\), the shortest-path distance \(h\) from \(u\) for these new lengths satisfies \(|h(u)-h(v)|=2\), and \(|h(i)-h(j)|\le w_{ij}\) on every original edge. Subtract the constant \(h(a)\) and put
\[
g_+=\frac{f+h-h(a)}2,\qquad g_-=\frac{f-h+h(a)}2.
\]
For every original edge \(ij\),
\[
|g_\pm(i)-g_\pm(j)|\le\frac{|f(i)-f(j)|+w_{ij}}2=1.
\]
Thus \(g_+\) and \(g_-\) are norm-one dual functionals, and both norm the edge molecule \(m_{uv}\) up to sign because their increments on \(uv\) equal \(\pm1\). Since \(g_++g_-=f\),
\[
1=f(Sm_{uv})=g_+(Sm_{uv})+g_-(Sm_{uv})\le2v(S).
\]
It follows for every \(S\) that \(v(S)\ge\|S\|/2\), proving \(n(\mathcal F(V,d_G))\ge1/2\). Combining this with the rank-two triangle operator proves the graph equality.

## Verification
The preceding argument is a proof for every finite order; it does **not** extrapolate from finite enumeration. Reproduce exact finite-graph checks using `python3 artifacts/verify.py` with Python 3 and the standard library only. The checker independently enumerates all **770 connected labeled graphs on three through five vertices**, identifies the **541** containing triangles, enumerates the extreme integral Lipschitz potentials via tight-edge connectivity, and verifies \(\|T\|=1\), \(v(T)=1/2\), and every auxiliary-distance decomposition for flat edges using integer and rational arithmetic. Its expected output is

`VERIFY_OK connected_graphs=770 triangle_graphs=541 dual_extremes=13376 norming_tests=58372 splittings=24466 n=3..5 exact=True`

The checker does not certify the infinite family; that role belongs to the two exact steps above. Its direct norming-pair calculation agrees with the analytic proof independently of floating-point optimization.

## Relationship to prior work
Cobollo, Guirao, and Montesinos computed the numerical index of Lipschitz-free spaces over **three-point** metrics. In particular, their Corollary 5.3 characterizes the equilateral triple as the three-point numerical-index-one-half case. Their Theorem 5.7 discusses **subspaces** of larger Lipschitz-free spaces; numerical index is not generally inherited by a containing space from a subspace. The present theorem instead constructs an operator **on the whole free space** that works for every finite unweighted graph containing a triangle.

Existing published computations treat all finite equilateral metrics and a five-vertex wheel as separate numerical-index-one-half cases; both are subsumed by the triangular graph statement. Published parity and bipartiteness criteria determine the index for cycles and the threshold for index one, respectively, but do not give this value for arbitrary triangle-containing graph metrics. General polyhedral numerical-index methods do not automatically imply the explicit operator-level obstruction. The sharp lower bound for all unit-edge finite graph metrics is included with a self-contained argument above so the conclusion does not rely on any separate numerical-index certificate.

## Limitations
The conclusion \(n=1/2\) is proved only for **real**, **finite**, **simple unweighted graph** vertex metrics containing a triangle. We do not claim it for graphs with no triangles, general positive edge weights, infinite graphs, or complex scalars. For arbitrary finite metrics with a minimum-distance equilateral triple, only the upper bound is proved. A triangle need not be necessary for achieving numerical index one half in other metric classes. Searches of indexed literature and published records cannot exclude equivalent statements under alternate terminology.

## References
1. Ch. Cobollo, A. J. Guirao, V. Montesinos, *The numerical index of 2-dimensional Lipschitz-free spaces*, arXiv:2304.13183v1 (first public 25 April 2023), later J. Math. Anal. Appl. 538 (2024), 128333, DOI:10.1016/j.jmaa.2024.128333. Primary MSC2020 46B20.
2. D. Sain, K. Paul, P. Bhunia, S. Bag, *On the numerical index of polyhedral Banach spaces*, arXiv:1809.04778 (2018), Linear Algebra Appl. 577 (2019), 121–133.
3. R. J. Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, arXiv:2102.01219 (2021), Mediterr. J. Math. 19 (2022), 32. The edge-molecule and finite metric background is also proved directly where used above.
4. *Numerical index one half for every finite equilateral Lipschitz-free space*, publicly accessible mathematical finding cc7060df7211 (2026).
5. *A five-point non-equilateral Lipschitz-free space with numerical index one half*, publicly accessible mathematical finding 9265557f0f91 (2026).
6. *Bipartiteness exactly characterizes numerical index one for finite graph metrics*, publicly accessible mathematical finding 1ca1185831c4 (2026).
7. *Numerical-index parity law for Lipschitz-free spaces over cycles*, publicly accessible mathematical finding 06885f9d5f05 (2026).
