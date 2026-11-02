# Sharp Hilbert distortion and rigidity for bridge-linked cliques

## Finding

For integers \(m,n\ge2\), let \(G_{m,n}\) consist of disjoint cliques on \(m+1\) and \(n+1\) vertices, connected by exactly one edge between distinguished vertices \(u\) and \(v\), respectively. Give its vertices the unweighted shortest-path metric. Put
\[
 a=\frac{m-1}{2m},\qquad b=\frac{n-1}{2n},\qquad
 F_{a,b}(c)=\bigl(\sqrt{c^2-a}+c+\sqrt{c^2-b}\bigr)^2+a+b.
\]
There is a unique \(c_{m,n}>1\) satisfying \(F_{a,b}(c_{m,n})=9\), and the exact least bi-Lipschitz distortion into any real Hilbert space is
\[
 \boxed{c_2(G_{m,n})=c_{m,n}.}
\]
After normalization so that all Hilbert distances are at least the graph distances, **every optimal embedding has the same pairwise distances, hence is unique up to Euclidean isometry**. Its affine dimension is exactly \(m+n-1\). More precisely, its two nondistinguished vertex classes are regular simplices of side length one in mutually orthogonal subspaces; their centroids and the two bridge vertices lie on one perpendicular line, with the three consecutive gaps \(\sqrt{c_{m,n}^2-a}\), \(c_{m,n}\), and \(\sqrt{c_{m,n}^2-b}\).

The constant increases strictly with either clique size. In the balanced family, \(m=n=k\), it is explicitly
\[
 c_{k,k}=\frac{2\sqrt{9+(k-1)/(2k)}-\sqrt{8+1/k}}{3}.
\]
The sharp supremum over finite clique pairs is \((\sqrt{38}-2\sqrt2)/3\), approached as both sizes tend to infinity and not attained for finite \(m,n\).

## Assumptions and scope

The vertex classes are \(\{u\}\sqcup A\sqcup\{v\}\sqcup B\), where \(|A|=m\), \(|B|=n\). The distinct pairwise graph distances are \(1\) inside \(A\) or \(B\), from \(A\) to \(u\), from \(B\) to \(v\), and from \(u\) to \(v\); distance \(2\) from \(A\) to \(v\) or \(B\) to \(u\); and distance \(3\) between \(A\) and \(B\). The target Hilbert space can have arbitrary dimension. The distortion of an injective map \(f\) is the ratio of the largest to smallest values of \(\|f(x)-f(y)\|/d(x,y)\) over distinct vertices; scaling permits the normalization \(d(x,y)\le\|f(x)-f(y)\|\le c\,d(x,y)\).

## Proof

**1. The universal two-centroid bound.** Let a normalized embedding of distortion at most \(c\ge1\) be given, write \(x_i=f(A_i)\), \(y_j=f(B_j)\), and let \(L=m^{-1}\sum_i x_i\) and \(R=n^{-1}\sum_j y_j\). Define the two variances
\[
 V_A=\frac1m\sum_i\|x_i-L\|^2
 =\frac1{2m^2}\sum_{i,j}\|x_i-x_j\|^2,
 \qquad
 V_B=\frac1n\sum_j\|y_j-R\|^2.
\]
Since all within-class graph distances are one, \(V_A\ge a\) and \(V_B\ge b\). Averaging the upper bounds for the edges from the first class to \(u\) gives
\[
 \|L-f(u)\|^2+V_A
 =\frac1m\sum_i\|x_i-f(u)\|^2\le c^2.
\]
Likewise \(\|R-f(v)\|\le\sqrt{c^2-V_B}\), and the bridge has length at most \(c\). Hence
\[
 \|L-R\|\le\sqrt{c^2-V_A}+c+\sqrt{c^2-V_B}.
\]
Every pair between the classes has graph distance three, so the cross-class centroid identity and the last inequality give
\[
 9\le\frac1{mn}\sum_{i,j}\|x_i-y_j\|^2
 =\|L-R\|^2+V_A+V_B
 \le H_c(V_A,V_B),
\]
where \(H_c(X,Y)=(\sqrt{c^2-X}+c+\sqrt{c^2-Y})^2+X+Y\). For \(0\le X,Y\le c^2\), this function is **strictly decreasing** in either argument (in the interior its derivative with respect to \(X\) is \(1-(\sqrt{c^2-X}+c+\sqrt{c^2-Y})/\sqrt{c^2-X}<0\); the endpoint follows by continuity). Thus \(9\le H_c(a,b)=F_{a,b}(c)\). The function \(F_{a,b}\) strictly increases for \(c\ge1\), and
\[
 F_{a,b}(1)\le F_{1/4,1/4}(1)=\frac92+2\sqrt3<9,
 \qquad F_{a,b}(2)>9.
\]
There is consequently exactly one root \(c_{m,n}\in(1,2)\), and no embedding has smaller distortion.

**2. Constructing an embedding meeting the lower bound.** Put \(c=c_{m,n}\), \(s=\sqrt{c^2-a}\), and \(t=\sqrt{c^2-b}\). In mutually orthogonal Euclidean summands choose centered regular simplices \(p_1,\ldots,p_m\) and \(q_1,\ldots,q_n\) with side length one. Their squared radii are \(a\) and \(b\). In an additional perpendicular one-dimensional summand with unit vector \(e\), set
\[
 f(u)=0,\quad f(v)=ce,\quad f(A_i)=-se+p_i,\quad
 f(B_j)=(c+t)e+q_j.
\]
Distances along the bridge and from each class to its own hub are exactly \(c\); within either class they are exactly one. The squared cross-class distance is \((s+c+t)^2+a+b=9\), hence exactly three. Distances from \(A\) to \(v\) and \(B\) to \(u\) have respective squares
\[
 Q_A=(s+c)^2+a=2c^2+2cs,\qquad
 Q_B=(t+c)^2+b=2c^2+2ct.
\]
Because \(s,t\le c\), each is at most \(4c^2\). For the required **lower** bounds \(Q_A,Q_B\ge4\), note that \(Q_A=4\) occurs at \(c_A=2/\sqrt{4-a}\). At this point
\[
 F_{a,b}(c_A)
 =4+\frac4{4-a}+2\sqrt{4-b(4-a)}
 \le4+\frac87+\frac5{\sqrt2}<9,
\]
using \(1/4\le a,b<1/2\). Strict increase of \(F_{a,b}\) implies \(c>c_A\) and therefore \(Q_A>4\). Interchanging \(a,b\) gives \(Q_B>4\). Thus every pair satisfies \(d\le\|f(x)-f(y)\|\le cd\), proving the exact constant.

**3. Uniqueness and dimension.** In any optimal embedding the lower-bound chain in Step 1 must consist entirely of equalities. Strict monotonicity of \(H_c\) forces \(V_A=a\), \(V_B=b\), so all within-class squared distances are one. The averaged upper bounds force every own-hub edge and the bridge to have length \(c\); equality in the centroid triangle inequality places \(L,f(u),f(v),R\) in that order on a line. Equality in the cross-class average forces every \(A\)-to-\(B\) distance to be exactly three. The own-hub equalities force each class's centered simplex deviations to be perpendicular to this line. Constancy of all cross-class distances then forces the two deviation spans to be mutually orthogonal (center and average the inner-product identities). Therefore all pairwise distances agree with the construction, proving congruence. The two simplices have dimensions \(m-1\) and \(n-1\); the centroid line adds one independent dimension, giving the precise affine dimension \(m+n-1\).

**4. Parameter consequences.** At fixed \(c\), \(F_{a,b}(c)\) strictly decreases as either \(a\) or \(b\) increases; since \(a=(m-1)/(2m)\) and \(b=(n-1)/(2n)\) strictly increase in the corresponding integer, the root increases in either size. If \(a=b\), writing \(2\sqrt{c^2-a}+c=\sqrt{9-2a}\) and solving the resulting quadratic yields \(c=[2\sqrt{9+a}-\sqrt{9-2a}]/3\). Taking both sizes to infinity gives the stated sharp limit.

## Verification

The attached standalone `check_barbell.py` uses high-precision decimal bisection to reproduce the defining root, checks all eight distinct squared-distance orbits for \(2\le m,n\le38\) and the balanced radical identity, and separately constructs explicit coordinates and verifies every unordered vertex pair for \(2\le m,n\le14\). These are finite consistency checks; the preceding argument proves the statement for all permitted integers. Run with `python3 check_barbell.py` using Python's standard library.

## Relationship to prior work

Robertson's 2023 formulation of distorted negative type supplies a general semidefinite characterization of Euclidean metric distortion, including exact results for complete bipartite graphs and Hamming cubes, not the bridge-linked clique constants here. Duda and Wong (2024) analyze the same bridge-barbell graph family with quantum-walk operators, not the shortest-path Hilbert-distortion optimization. Baskoro and Obata (2023) calculate quadratic embedding constants of graphs made from two *overlapping* maximal cliques; their invariant and graph construction differ. The present theorem is about a single bridge between two disjoint cliques, which has three maximal cliques, including the bridge edge. The theorem is also distinct from exact Hilbert distortion of double-star trees: the within-class distances here are one rather than two, and the two-hop constraints must be established separately, rather than inferred from a formal parameter substitution.

## Limitations

Only finite unweighted bridge-linked cliques with at least two nondistinguished vertices in each clique are covered. The formula does not claim a result for weighted bridges, longer bridge paths, arbitrary clique trees, other target norms, or minimum distortion into prescribed low-dimensional Hilbert spaces. The result and novelty comparison have not been independently mathematically audited. Earlier equivalent formulas under alternative metric embedding terminology remain possible.

## References

1. G. Robertson, *Negative Type and Bi-lipschitz Embeddings Into Hilbert Space*, first publicly submitted 2023-09-27, arXiv:2309.16070, https://arxiv.org/abs/2309.16070.
2. J. Duda and T. G. Wong, *Searching Weighted Barbell Graphs with Laplacian and Adjacency Quantum Walks*, first publicly submitted 2024-08-15, arXiv:2408.08244, https://arxiv.org/abs/2408.08244.
3. E. T. Baskoro and N. Obata, *A Classification of Graphs through Quadratic Embedding Constants and Clique Graph Insights*, first publicly submitted 2023-11-06, arXiv:2311.03342, https://arxiv.org/abs/2311.03342.
