# A sharp apex-screening transition for the circumradius of graph-cone stable-set polytopes

## Finding

For a finite vertex-transitive simple graph \(H\) on \(N\ge2\) vertices with at least one edge and independence number \(a=\alpha(H)\), form its **cone** \(G=K_1\vee H\) by adding a vertex adjacent to every vertex of \(H\). Write the hub coordinate last and put
\[
Q=a-\frac{a^2}{N},\qquad D=1+\frac{a^2}{N},\qquad
\delta=D-Q=1-a+\frac{2a^2}{N},\qquad
\lambda=\frac{\max\{0,\delta\}}{2D}.
\]
The **unique minimum enclosing Euclidean ball** of \(P=\operatorname{STAB}(G)\) has center and squared radius
\[
\boxed{c=\left((1-\lambda)\frac aN\mathbf1_N,\ \lambda\right),\qquad R^2=Q+\frac{\max\{0,\delta\}^2}{4D}.}
\]
Its contact vertices are exactly \((\mathbf1_I,0)\) for maximum independent sets \(I\) of \(H\), together with the hub indicator \((\mathbf0,1)\) precisely when \(\delta\ge0\). Every other stable-set indicator lies strictly inside the ball. For a rim independent set of cardinality \(k<a\), the exact squared-radius clearance is
\[
R^2-\| (\mathbf1_I,0)-c\|^2=(a-k)\left(1-2(1-\lambda)\frac aN\right)>0.
\]
When \(\delta<0\), coning does not change either the rim center or the squared radius \(Q\); the hub lies strictly inside at squared-radius clearance \(-\delta\). For \(a>1\), this occurs exactly when \(N>2a^2/(a-1)\). At equality the hub is tangent with no radius increase; below the threshold (or when \(a=1\)) it is tangent and the squared radius increases by \(\delta^2/(4D)\).

For an explicit sharp boundary, take \(H=\overline{C_N}\), the complement of a cycle, with \(N\ge5\) and \(a=2\). At \(N=8\) the hub is tangent with zero radius increment, but at every \(N\ge9\) the hub lies strictly inside and the radius is unchanged. The family of ordinary wheels \(K_1\vee C_N\) is also covered (both parities), as are cones over many other vertex-transitive graphs not of complete-multipartite type.

## Assumptions and scope

The ambient scalar product is the standard Euclidean product in \(\mathbb R^{N+1}\); no affine change of coordinates is implicit. An independent set is a vertex subset containing no edge. The polytope is exactly the convex hull of its \(0/1\) incidence vectors: every independent set of the cone is either an independent set contained in \(H\) or the singleton hub. The graph is finite, simple, vertex-transitive, nonempty, and has at least one edge; in particular \(1\le a\le N/2\). Vertex-transitivity is used to obtain an exact uniform barycenter of maximum independent sets, not merely to assume the optimum is symmetric.

## Proof

**Uniform contact barycenter.** Let \(\mathcal A\) be the nonempty collection of maximum independent sets of \(H\) and \(v_I=(\mathbf1_I,0)\) their incidence vectors in \(\mathbb R^{N+1}\). Every coordinate occurs equally often in \(\mathcal A\), by vertex-transitivity. Since each set has size \(a\), their mean is
\[
q=\frac1{|\mathcal A|}\sum_{I\in\mathcal A}v_I=\left(\frac aN\mathbf1_N,0\right).
\]
The squared distance of each \(v_I\) from \(q\) is \(\|v_I-q\|^2=Q\), and the hub vertex \(h=(\mathbf0,1)\) satisfies \(\|h-q\|^2=D\). Average squared distances to the rim contacts obey the exact variance identity
\[
\frac1{|\mathcal A|}\sum_{I\in\mathcal A}\|y-v_I\|^2=\|y-q\|^2+Q
\quad\text{for every }y\in\mathbb R^{N+1}.
\]
The existence of an edge gives \(2a/N\le1\): averaging the disjointness inequality \(\mathbf1_I(u)+\mathbf1_I(v)\le1\) along any fixed edge \(uv\) yields the bound.

**Feasible radius and contacts.** Set \(t=(1-\lambda)a/N\). The definition gives \(0\le\lambda<1/2\) and \(0<t<1/2\) (if \(\lambda=0\), strictness follows from \(\delta\le0\), which excludes \(a/N=1/2\)). For any independent set \(I\subseteq V(H)\) of size \(k\),
\[
\|(\mathbf1_I,0)-c\|^2=Nt^2+\lambda^2+k(1-2t).
\]
Because \(1-2t>0\), this expression is maximized precisely when \(k=a\). For those vertices, the squared distance is \(Q+D\lambda^2\). The hub's squared distance is \(D(1-\lambda)^2\). If \(\delta\le0\), then \(\lambda=0\), and the hub's squared distance \(D\le Q\). If \(\delta>0\), the equation
\[
Q+D\lambda^2=D(1-\lambda)^2
\]
is equivalent to \(\lambda=(D-Q)/(2D)\), so all listed contacts lie on the proposed sphere. Therefore every vertex, and hence the entire polytope, lies in the proposed closed ball. The deficit formulas and exact contact classification follow.

**Global lower bound and uniqueness.** For every proposed competing center \(y\) and \(0\le\lambda<1\), weighting the maximum rim vertices by \((1-\lambda)/|\mathcal A|\) each and the hub by \(\lambda\), the weighted squared-distance identity gives
\[
\frac{1-\lambda}{|\mathcal A|}\sum_{I\in\mathcal A}\|y-v_I\|^2+\lambda\|y-h\|^2
=\|y-c\|^2+(1-\lambda)Q+\lambda(1-\lambda)D.
\]
For \(\delta\le0\), \(\lambda=0\) and the constant is \(Q=R^2\). For \(\delta>0\), equality of the rim and hub squared distances at \(c\) shows \((1-\lambda)Q+\lambda(1-\lambda)D=R^2\). Since the maximum squared distance from \(y\) to the vertices is at least this weighted average, every \(y\ne c\) has maximum squared distance strictly larger than \(R^2\). Hence the asserted sphere is the unique minimum enclosing sphere.

## Verification

The accompanying `verify.py` uses only the Python standard library and exact rational arithmetic. Execute `python3 verify.py`. It enumerates all independent sets for cycles, complements of cycles, complete graphs, and balanced complete multipartite graphs with small parameters; tests all distance inequalities, equality/strictness of every contact, exact parameter identities, and the contact barycenter and moment identity. The tested families include all three screening regimes and the sharp \(\overline{C_8}\) to \(\overline{C_9}\) transition. These finite tests are not used as a proof for arbitrary vertex-transitive graphs.

## Relationship to prior work

Merino and Mütze study the graph of \(0/1\)-polytopes and Hamiltonian traversal of their vertices; their polytope framework includes stable-set incidence polytopes, but their structural claims concern Hamilton paths and enumeration, not minimum Euclidean balls. Ohsugi and Tsuchiya's open-access treatment defines stable-set polytopes in the anti-blocking setting and studies Ehrhart \(h^*\)-polynomials and related lattice invariants, not the Euclidean circumcenter or the apex transition. General minimum-enclosing-ball methods provide optimization and weighted-contact characterizations, but do not by themselves state the graph-theoretic \((N,a)\) formula, the exact threshold, or the complete strict-contact description. A previously studied complete-multipartite stable-set subfamily admits its own radius formula; it does not cover cones over arbitrary vertex-transitive graphs, including odd wheels or the complement-cycle screening examples. The present theorem concerns a standard coordinate metric, not an affine-invariant quantity.

## Limitations

The result assumes vertex-transitivity and at least one edge; it does not determine circumcenters for arbitrary asymmetric graph cones or weighted Euclidean norms. Computing \(a=\alpha(H)\) may itself be difficult in general. The formula identifies geometric properties conditional on this exact graph invariant. No claim of novelty is made for generic weighted-variance identities or for complete-multipartite special cases considered elsewhere. The full scope of equivalent formulations under geometric pyramid terminology has not been exhaustively excluded; independent literature priority verification remains outstanding.

## References

1. A. Merino and T. Mütze, “Traversing combinatorial 0/1-polytopes via optimization,” arXiv:2304.08567, first public version 17 April 2023; freely accessible full text: https://arxiv.org/html/2304.08567v2 .
2. H. Ohsugi and A. Tsuchiya, “The \(h^*\)-Polynomials of Locally Anti-Blocking Lattice Polytopes and Their \(\gamma\)-Positivity,” *Discrete & Computational Geometry* 66 (2021), 701–722; freely accessible full text: https://link.springer.com/article/10.1007/s00454-020-00236-6 .
3. G. Dahl, “Stable Set Polytopes for a Class of Circulant Graphs,” *SIAM J. Optimization* 9 (1999), 493–503, https://doi.org/10.1137/S1052623497321973 . Only the accessible abstract was compared; no full-document exclusion is claimed for this source.
