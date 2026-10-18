# Sharp slice-averaged vertex counts for fan graphical zonotopes

## Finding

For each integer \(n\ge 3\), form the fan graph \(F_n\) by adjoining a hub \(0\) to every vertex of the path \(1-2-\cdots-n\). Its standard graphical zonotope is
\[
Z_n=\sum_{\{i,j\}\in E(F_n)}[e_i,e_j]\subset\mathbb R^{n+1},
\]
with its intrinsic \(n\)-dimensional affine geometry. For a nonzero intrinsic hyperplane normal \(u\), let \(N_u(t)\) be the number of vertices of the section \(Z_n\cap\{y:u\cdot y=t\}\), for almost every \(t\) between the minimum and maximum support levels. Set
\[
\mathcal A_n(u)=\frac{1}{t_+(u)-t_-(u)}\int_{t_-(u)}^{t_+(u)}N_u(t)\,dt.
\]
Writing \(x_i=u_i-u_0\), the *complete directional profile* is
\[
\boxed{\displaystyle
\mathcal A_n(u)=2\cdot3^{n-2}
-2\cdot3^{n-3}\,
\frac{\sum_{i=2}^{n-1}|x_i|}
{\sum_{i=1}^n|x_i|+\sum_{i=1}^{n-1}|x_{i+1}-x_i|}.}
\]
Consequently its exact range is
\[
\boxed{\displaystyle
\frac{4(n+1)}n3^{n-3}\ \le\ \mathcal A_n(u)\ \le\ 2\cdot3^{n-2}.}
\]
Every intermediate value occurs. **All minimizing normals** are exactly those for which there is a nonzero real \(a\) such that \(x_2=\cdots=x_{n-1}=a\) and \(x_1,x_n\) both belong to the closed interval with endpoints \(0,a\). **All maximizing normals** are exactly those for which \(x_2=\cdots=x_{n-1}=0\), with \((x_1,x_n)\ne(0,0)\). Normals are understood modulo adding a constant coordinate vector and positive rescaling; negation also leaves the averaged section count unchanged. The sharp maximum/minimum ratio is \(3n/[2(n+1)]\), tending to \(3/2\).

A structural extension underlying the result applies to **every** tree \(T\) on \(n\ge2\) labeled vertices. Let \(H=K_1\vee T\) be its cone, write \(d_v\) for the degree of vertex \(v\) in \(T\), and put \(x_v=u_v-u_0\). The corresponding graphical zonotope has
\[
\boxed{\displaystyle
\mathcal A_{H}(u)=
\frac{2\cdot3^{n-2}\sum_{\{v,w\}\in E(T)}|x_v-x_w|
 +\sum_{v\in V(T)}2^{d_v}3^{n-1-d_v}|x_v|}
{\sum_{\{v,w\}\in E(T)}|x_v-x_w|+\sum_{v\in V(T)}|x_v|}.}
\]
This tree-cone formula and the complete fan extremum/equality classification constitute one connected finding about section complexity; no uniqueness statement for unexamined literature is asserted.

## Assumptions and scope

Graphs are finite and simple before contraction. Parallel edges arising under contraction are identified for chromatic and acyclic-orientation counting. The zonotope uses **one unit-coordinate segment** \([e_i,e_j]\) for each graph edge, with no extra weights. All sections and normals are taken intrinsically in the affine hyperplane \(\sum_{i=0}^{n} y_i=|E(F_n)|\); therefore a normal is defined modulo the all-ones vector. The parameter \(t\) in the average is uniform on the full projected support interval for each fixed normal, not a random plane chosen uniformly by orientation. The section dimension is \(n-1\) at generic interior levels. At finitely many exceptional levels, its vertex count may be defined arbitrarily without changing the integral.

## Proof

**1. Section-edge identity.** For a full-dimensional polytope \(P\) and any nonzero intrinsic \(u\), a generic-level section has one vertex for each edge \([a,b]\) whose endpoint projections strictly straddle the level. The set of levels crossed by this edge has length \(|u\cdot(a-b)|\). Integrating and dividing by the support width gives
\[
\mathcal A_P(u)=\frac{\sum_{E\in\mathcal E(P)}|u\cdot \Delta_E|}{w_P(u)}.
\]
The identity also follows by continuity at nongeneric directions. For a graphical zonotope, all edges parallel to the coordinate-root segment corresponding to a given graph edge have that same vector length, while Minkowski additivity of support functions gives
\[
w_{Z_G}(u)=\sum_{\{v,w\}\in E(G)}|u_v-u_w|.
\]

**2. Edge-direction multiplicities.** For any simple graph \(G\) and graph edge \(e=\{v,w\}\), the faces of \(Z_G\) parallel to \(e_v-e_w\) correspond to chambers of the graphical arrangement restricted to \(u_v=u_w\). Identifying these two coordinates produces the graphical arrangement of the contraction \(G/e\). Consequently the exact number of zonotope edges parallel to that root is
\[
M_e=a(G/e)=|\chi_{G/e}(-1)|,
\]
where \(a\) counts acyclic orientations and \(\chi\) is the chromatic polynomial (parallel edges may be suppressed). This is an exact face-normal-fan correspondence, not a statistical approximation.

**3. Cones over trees.** Let \(T\) have \(n\ge2\) vertices, and take \(H=K_1\vee T\). Contracting a tree edge leaves a cone over a tree on \(n-1\) vertices. Its chromatic polynomial is \(q(q-1)(q-2)^{n-2}\), giving the multiplicity \(2\cdot3^{n-2}\) for every tree-edge direction. Contracting the spoke from the hub to vertex \(v\) leaves a cone over the forest \(T-v\). That forest has \(n-1\) vertices and \(d_v\) components; its chromatic polynomial is \(q^{d_v}(q-1)^{n-1-d_v}\). Thus the cone has polynomial \(q(q-1)^{d_v}(q-2)^{n-1-d_v}\), giving multiplicity \(2^{d_v}3^{n-1-d_v}\). Substitution into the section-edge identity proves the displayed universal tree-cone formula.

**4. Fan formula and lower/upper bounds.** For the path \(T=P_n\), the two endpoints have degree \(1\), and the \(n-2\) internal vertices have degree \(2\). Hence tree-edge and endpoint-spoke multiplicities are \(C=2\cdot3^{n-2}\), whereas internal-spoke multiplicities are \(2C/3\). Put
\[
D=\sum_{i=1}^n|x_i|+\sum_{i=1}^{n-1}|x_{i+1}-x_i|,
\qquad J=\sum_{i=2}^{n-1}|x_i|.
\]
Then \(D>0\) for every valid normal and \(\mathcal A_n(u)=C(1-J/(3D))\). Since \(J\ge0\), the upper bound is attained exactly when \(J=0\), or equivalently all internal differences \(x_i\) vanish. Its normal is nonzero precisely when at least one endpoint difference is nonzero.

To prove the sharp lower bound, write
\[
B=|x_1|+|x_n|+\sum_{i=1}^{n-1}|x_{i+1}-x_i|,
\qquad D=J+B.
\]
For every \(2\le i\le n-1\), applying the triangle inequality along the path from each endpoint to \(i\) gives
\[
2|x_i|\le
\left(|x_1|+\sum_{j<i}|x_{j+1}-x_j|\right)
+\left(|x_n|+\sum_{j\ge i}|x_{j+1}-x_j|\right)=B.
\]
Summing yields \(2J\le(n-2)B\) and therefore \(J/D\le(n-2)/n\). Substitution gives precisely \(C[1-(n-2)/(3n)]=4(n+1)3^{n-3}/n\).

**5. Equality conditions.** Equality in \(2J\le(n-2)B\) requires \(2|x_i|=B\) for every internal \(i\). Since \(J>0\) at a lower-bound minimizer, all internal magnitudes are the same positive number. Every sign change between consecutive internal values would contribute twice that magnitude to path variation, while each of the two endpoint-to-interior paths already contributes at least that magnitude. This would force \(B\) to exceed twice that magnitude, a contradiction. Thus all internal coordinates share one nonzero value \(a\). The two remaining endpoint triangle inequalities reduce to \(|x_1|+|x_1-a|=|a|\) and \(|x_n|+|x_n-a|=|a|\), each equivalent to its endpoint belonging to the interval between \(0\) and \(a\). These conditions are also sufficient, giving the full minimizing family. The maximizing family was classified in step 4. Finally, the intrinsic unit-normal sphere is connected when \(n\ge3\); continuity of the displayed quotient therefore makes its image the full closed interval between the extrema.

## Verification

The included standalone `verify_fan.py` uses exact integer and rational arithmetic. It exhaustively enumerates all acyclic orientations and all orientation-flip zonotope edges for fan sizes \(n=3,4,5,6,7\), checks their direction multiplicities and the predicted \(2\cdot3^{n-1}\) vertices, and independently integrates actual edge crossings between consecutive vertex-projection levels in small rank. It checks 19,496 nonconstant small-integer normal directions against **both** equality classifications, and additionally checks the contraction multiplicities of eight cones over non-path trees. All these finite checks passed. The proof for all dimensions is the preceding analytic argument; exhaustive finite checks alone do not establish it.

Reproduce with `python3 verify_fan.py` using only the Python standard library. The script is included in full with this finding.

## Relationship to prior work

Bárány and Domokos (2023 preprint, 2024 journal) introduced the slice-averaged vertex-count problem, established an edge-projection expression for the average and classified constant-average centrally symmetric polytopes. Their general formula is foundational here; their inspected treatment does not identify the sharp directional range or equality normals of the fan graphical zonotope. Grujić (2016) gave the acyclic-orientation and contraction framework for graphical-zonotope face counts, but did not study slice-average extrema. The present result derives explicit cone-over-tree edge-direction weights and solves the resulting sharp directional optimization for the full fan family. It does **not** claim novelty for the section-edge identity, the chromatic evaluation, or the graph–zonotope correspondence.

## Limitations

The exact sharp range and equality-normal classifications are proved for the unit-weight fan graphical zonotopes only. The broader cone-over-tree statement is an exact formula, not a closed-form extremal classification for every tree or a statement about independently random orientation. Generic-level conventions exclude finitely many exceptional section levels. Literature searches cannot rule out every earlier equivalent formula; in particular older stereological or graph-arrangement terminology might conceal an equivalent special case. No independent mathematical audit has been performed.

## References

1. I. Bárány and G. Domokos, *Same average in every direction*, arXiv:2310.18960v1 (first publicly submitted 2023-10-29); revised v2 2024-02-01, *Bulletin Mathématique de la Société des Sciences Mathématiques de Roumanie* **67** (2024), 125–138. In particular Sections 2–4 and equation (3.1). https://arxiv.org/html/2310.18960v2
2. V. Grujić, *Counting faces of graphical zonotopes*, arXiv:1604.06931 (first submitted 2016-04-23), especially Sections 2 and 4. https://arxiv.org/abs/1604.06931
3. R. P. Stanley, *Acyclic orientations of graphs*, *Discrete Mathematics* **5** (1973), 171–178, DOI:10.1016/0012-365X(73)90108-8.
