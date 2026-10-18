# Two-sheeted skeletons and hidden regularity of complete multipartite transportation balls

## Finding

Let \(k\ge3\), let \(n_1,\ldots,n_k\) be arbitrary positive integers, and let \(G=K_{n_1,\ldots,n_k}\) have its unit-edge shortest-path metric. Put \(N=\sum_i n_i\), \(M=\sum_{i<j}n_i n_j\). The unit ball \(P\) of the real Lipschitz-free space over \(V(G)\) has \(2M\) vertices, the signed edge molecules \(m_{uv}=e_u-e_v\) for ordered adjacent vertices \(u,v\).

**Complete adjacency rule.** Distinct \(m_{uv}\) and \(m_{st}\) are adjacent vertices of \(P\) precisely when either (a) \(u=s\) or \(v=t\); or (b) \(u,v,s,t\) are pairwise distinct and either \(u,t\) belong to the same part or \(s,v\) belong to the same part. All other pairs, including antipodes and consecutive directed edges, are nonadjacent.

Identify the two antipodal molecules over each undirected edge \(e\) as a two-point fiber. Let \(H\) be the graph whose vertices are edges of \(G\), with two distinct edges adjacent exactly when their respective *pairs of multipartite parts* intersect. The one-skeleton of \(P\) is a signed two-sheeted covering of \(H\): over each edge of \(H\), there is one perfect matching between the two fibers, and there are no other cross-fiber edges. The base \(H\) is the clique blow-up of the line graph of the complete graph on the \(k\) parts, with each vertex \(\{i,j\}\) replaced by a clique of \(n_i n_j\) vertices.

For a molecule between parts of sizes \(a\) and \(b\), its exact one-skeleton degree is
\[
 d_{ab}=N(a+b)-a^2-ab-b^2-1.
\]
Consequently the number of one-dimensional faces is
\[
 f_1(P)=\sum_{i<j}n_i n_j\bigl[N(n_i+n_j)-n_i^2-n_i n_j-n_j^2-1\bigr].
\]
The skeleton is regular **if and only if** \(k=3\) or all part sizes are equal. In particular, every (possibly highly unbalanced) complete tripartite metric has a \((M-1)\)-regular, \(2M\)-vertex skeleton with precisely \(M(M-1)\) edges. Moreover its unweighted combinatorial Laplacian contains the eigenvalue \(M\) with multiplicity at least \(M-1\), in addition to its zero eigenvalue.

## Assumptions and scope

Every part is nonempty and there are at least three parts. All graph edges have length one; nonadjacent vertices are at distance two. All statements concern the *primal* transportation unit ball and its ordinary combinatorial one-skeleton; graph edges refer to one-dimensional polytope faces, not graph-metric edge lengths. The ambient zero-sum hyperplane has dimension \(N-1\), and \(m_{uv}\) is normalized because \(d(u,v)=1\). The covering is graph-theoretic, with no metric or topological covering-space structure implied. Laplacian eigenvalues use unit weights and algebraic multiplicity.

## Proof

**Step 1: vertices and exposed edges.** The finite transport ball is the convex hull of all normalized two-point molecules. In a complete multipartite shortest-path metric, every nonedge pair lies on a two-edge geodesic and its normalized molecule is a convex combination of two edge molecules. Conversely an edge molecule has a strictly shorter metric segment with no third vertex; hence it is extreme (or directly expose it using its endpoint distance profile). This leaves precisely \(2M\) vertices. Two distinct vertices \(m_{uv},m_{st}\) form a polytope edge exactly when a real potential \(f\) satisfies \(|f(x)-f(y)|\le1\) on every graph edge, attains \(f(u)-f(v)=f(s)-f(t)=1\), and has strict inequalities on all other undirected graph edges. Indeed these inequalities say that the maximizing face of the dual functional consists of exactly those two extreme molecules. Every polytope edge is an exposed face.

**Step 2: classify coincident endpoints.** If \(u=s\), set \(f(u)=1\), \(f(v)=f(t)=0\), and \(f=1/2\) at all other vertices. The only tight graph edges are the two prescribed edges. The case \(v=t\) follows after replacing \(f\) by \(-f\). Antipodal molecules cannot lie in the same proper supporting face. If instead \(v=s\), the desired equalities force \(f(u)-f(t)=2\). If \(u,t\) lie in different parts the direct edge makes this impossible. Otherwise every vertex outside their shared part must have the midpoint potential \(f(v)\) (by the two edge inequalities). As \(k\ge3\), at least one such vertex differs from \(v\) and gives extra tight edges. The case \(u=t\) is identical after reversing the two directed edges. Thus consecutive directed edges are never adjacent in this family.

**Step 3: classify disjoint endpoints.** Fix \(f(v)=0\), \(f(u)=1\), write \(f(t)=\delta\), \(f(s)=1+\delta\). If both cross edges \(ut\) and \(sv\) exist, their Lipschitz constraints respectively imply \(\delta\ge0\) and \(\delta\le0\); hence \(\delta=0\), and the two cross edges become additional tight edges. No two-vertex exposed face exists. If \(sv\) is absent, take \(\delta=1/2\) and give every other vertex potential \(3/4\). All unprescribed existing edge differences are strictly less than one. If \(ut\) is absent, take \(\delta=-1/2\) and give every other vertex potential \(1/4\). Again all other edges are strictly slack. In a complete multipartite graph, the absence of \(sv\) means that \(s,v\) are in the same part, and the absence of \(ut\) means that \(u,t\) are in the same part. This proves the complete adjacency rule.

**Step 4: the signed covering.** For distinct undirected graph edges \(e,g\), each orientation of \(e\) has *exactly one* neighboring orientation of \(g\) if their unordered part pairs intersect, and none if the part pairs are disjoint. When the original edges share an endpoint, the unique adjacent orientations put this vertex in the same tail or head role; when endpoints are disjoint, the unique adjacent orientation makes the common part an opposite tail/head role. Inversion gives the complementary matching for opposite orientations. Thus each allowed pair of fibers is joined by a perfect matching, proving the signed two-cover description. The graph \(H\) is the claimed clique blow-up because each interpart edge corresponds to one choice of its endpoints in a fixed unordered pair of parts.

**Step 5: degrees and regularity.** For any edge joining parts \(i,j\) of sizes \(a,b\), its base-neighbors are all other graph edges incident to either *part*, rather than merely to either endpoint. Inclusion–exclusion gives
\[
 a(N-a)+b(N-b)-ab-1=N(a+b)-a^2-ab-b^2-1.
\]
Each base-neighbor lifts to exactly one polytope-skeleton neighbor. Summing degrees over the two orientations of each original graph edge, then dividing by two, yields the stated \(f_1(P)\) formula. When \(k=3\), the three part pairs intersect pairwise, so \(H=K_M\). Hence every degree is \(M-1\). For \(k\ge4\), fixing distinct parts of sizes \(a,b,c\), comparison of the first two types yields
\[
 d_{ab}-d_{ac}=(b-c)(N-a-b-c).
\]
The second factor is strictly positive. Therefore regularity forces every two parts other than any specified part to have equal sizes, hence all parts equal. Conversely equal part sizes visibly give equal degrees.

**Step 6: tripartite spectral block.** For \(k=3\), identify real vectors on the \(2M\) lifted vertices constant along each antipodal fiber with vectors on the \(M\) vertices of \(H=K_M\). The two-cover property makes the adjacency operator act on this invariant subspace as \(J_M-I_M\); the degree is \(M-1\). Thus the Laplacian restriction is \(MI_M-J_M\), which has eigenvalue zero once and eigenvalue \(M\) with multiplicity \(M-1\). The other \(M\) Laplacian eigenvalues are not claimed or evaluated.

## Verification

Run `python3 verify_skeleton.py` and `python3 verify_hull.py` from the same directory with Python, NumPy and SciPy available. The first independently maximizes the strict-support margin of each pair of oriented vertices by linear programming, comparing every pair with the theorem for nine small multipartite graphs. It checks degrees and the two-fiber matching rule. The second uses convex-hull supporting hyperplanes and rank of their common equality space, rather than support-margin linear programming, on five of the cases. Both programs terminate with all checks passing. These numerical experiments support the finite examples only; the preceding symbolic argument proves all \(k\ge3\) and all positive part sizes.

## Relationship to prior work

Aliaga and Pernecká establish the general metric-segment characterization of extreme molecules of Lipschitz-free spaces; identifying the vertex set is an application of that prior criterion. Higashitani, Jochemko and Michałek classify *facets* of complete multipartite symmetric edge polytopes but do not give the two-vertex face covering and the all-parameter one-skeleton regularity theorem. D'Alì, Delucchi and Michałek compute whole face posets for *cycles* (including the four-cycle) and other graph families, not the present complete tripartite or general multipartite family. D'Alì, Juhnke-Kubitzke and Koch establish broad regular-matroid invariance and a facet description, without evaluating this skeleton. A separate existing complete-*bipartite* two-cover and full skeleton Laplacian theorem is a close predecessor; it applies to two parts of size at least two and does not cover the triangle-containing three-part case or the sharp four-part regularity boundary. The graph-metric and root-polytope formulations of the present theorem are mathematically equivalent and are not claimed separately.

## Limitations

The claim excludes bipartite stars and does not assert the analogous formula for every graph, arbitrary edge lengths, higher-dimensional faces, the full odd-subspace Laplacian spectrum, or Euclidean geometry. The finite computations use floating-point convex hulls and linear programs, but the infinite theorem has an exact construction and proof independent of numerical tolerances. The one-skeleton regularity is not a claim of vertex transitivity or of isomorphic polytope faces. Unindexed alternative treatments of lower face lattices remain a literature risk.

## References

1. R. J. Aliaga and E. Pernecká, *Supports and extreme points in Lipschitz-free spaces*, arXiv:1810.11278, v1 first public 2018-10-26, Theorem 1.1, primary MSC 46B20.
2. A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678, v1 first public 2018-07-20, especially Proposition 3.5.
3. A. D'Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193, v1 first public 2019-10-11, especially Proposition 4.3 and Section 4.
4. A. D'Alì, M. Juhnke-Kubitzke and M. Koch, *On a generalization of symmetric edge polytopes to regular matroids*, arXiv:2307.04933, v1 first public 2023-07-10, Theorem 4.6 and Remark 5.10.
5. *Laplacian spectrum and tree complexity of complete-bipartite symmetric edge polytopes*, published-finding corpus record `2026/10/11/SCOPE-laplacian-spectrum-and-tree-complexity-of-complete-bipartite-sym--3feaadaf9c02`, RESULT.md, particularly its adjacency and signed-two-lift results for \(K_{p,q}\).
