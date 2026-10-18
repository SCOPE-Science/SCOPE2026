# Crosspolytopal highest-root deletion and a power-of-two volume loss

## Finding
For every integer \(m\ge2\), let \(v_{ij}\) be the indicator of the nonempty integer interval \([i,j]\subseteq[1,m]\). Define
\[
P_m=\operatorname{conv}\{v_{ij}:1\le i\le j\le m\},\quad
u=v_{1m}=(1,\ldots,1),\quad
P_m^-=\operatorname{conv}\{v_{ij}:(i,j)\ne(1,m)\}.
\]
The linear functional \(h(x)=x_1+x_m\) gives the exact dissection
\[
P_m\cap\{h\le1\}=P_m^-,\qquad
P_m\cap\{h\ge1\}=\operatorname{conv}(u,F_m),
\]
where
\[
F_m=\operatorname{conv}\{v_{1j},v_{j+1,m}:1\le j<m\}
\]
is an \((m-1)\)-dimensional crosspolytope in the hyperplane \(h=1\), with opposite pairs summing to \(u\). These pieces have disjoint interiors. The exact deleted corner has lattice-normalized volume
\[
\boxed{m!\bigl(\operatorname{vol}_m(P_m)-\operatorname{vol}_m(P_m^-)\bigr)=2^{m-2}.}
\]
Under the unimodular identification \(v_{ij}\leftrightarrow e_i-e_{j+1}\), this is the positive type-\(A_m\) root polytope of a transitively oriented complete graph. Thus deleting its longest arrow, from vertex \(1\) to vertex \(m+1\), causes the exact normalized volume loss \(2^{m-2}\).

## Assumptions and scope
All volumes are ordinary Euclidean coordinate volumes in \(\mathbb R^m\), with *normalized volume* defined as \(m!\) times coordinate volume. This convention agrees with the type-\(A_m\) root lattice because the simple roots \(e_i-e_{i+1}\), for \(1\le i\le m\), are a lattice basis. For \(m=2\), \(P_m^-\) is lower-dimensional and is assigned zero \(m\)-dimensional volume. The assertion concerns deletion of the one distinguished longest interval; it does not cover deletion of arbitrary root vertices.

## Proof
**Hyperplane and vertex partition.** Write \(p_j=v_{1j}\) and \(s_{j+1}=v_{j+1,m}\) for \(1\le j<m\). The highest-root vertex \(u\) is the only interval incidence vector with \(h=2\). Every prefix and suffix other than \(u\) has \(h=1\), while every strict interior interval \(q=v_{ij}\), where \(1<i\le j<m\), has \(h=0\). The crucial identity is
\[
u+v_{ij}=v_{1j}+v_{i,m}=p_j+s_i\qquad(1<i\le j<m).
\]
The right-hand vectors both belong to \(F_m\).

**Exact dissection.** Express any \(x\in P_m\) as a convex combination of interval vectors. Let \(\lambda\) be the coefficient of \(u\), let \(\mu\) be the sum of coefficients of strict interior interval vectors, and let the remaining coefficient be assigned to prefix and suffix vertices. Then \(h(x)=1+\lambda-\mu\). If \(h(x)\le1\), pair all the mass \(\lambda\) on \(u\) with equal mass drawn from interior intervals, using the displayed identity to replace each pair by two points of \(F_m\). This leaves no mass on \(u\); hence \(x\in P_m^-\). Conversely, all vertices of \(P_m^-\) have \(h\le1\), proving the first equality. If \(h(x)\ge1\), pair all mass \(\mu\) on interior vertices with equal mass drawn from \(u\), leaving only \(u\) and points in \(F_m\). Thus \(x\in\operatorname{conv}(u,F_m)\). The reverse inclusion follows from \(h\ge1\), proving the second equality. The common section is \(F_m\), so the two full-dimensional interiors are disjoint. Both parts' containment inequalities are exact even at \(h=1\).

**The section is a crosspolytope.** For each \(1\le j<m\),
\[
p_j+s_{j+1}=u,\qquad w_j=p_j-u/2.
\]
Thus \(F_m=u/2+\operatorname{conv}\{\pm w_1,\ldots,\pm w_{m-1}\}\). Work in the lattice-coordinate chart \((x_1,\ldots,x_{m-1})\) on \(h=1\), so that \(x_m=1-x_1\). In this chart \(w_{j+1}-w_j=e_{j+1}\) for \(1\le j\le m-2\), and \((w_1)_1=1/2\). Subtracting successive columns shows that the determinant of the \((m-1)\)-column matrix of the \(w_j\) in this chart has absolute value \(1/2\). In particular they are linearly independent and \(F_m\) is the asserted crosspolytope.

**Volume calculation.** The standard \((m-1)\)-crosspolytope \(\operatorname{conv}\{\pm e_1,\ldots,\pm e_{m-1}\}\) has volume \(2^{m-1}/(m-1)!\). The linear chart determinant is \(1/2\), hence
\[
\operatorname{vol}_{m-1}^{\mathrm{chart}}(F_m)=\frac{2^{m-2}}{(m-1)!}.
\]
The full chart \((x_1,\ldots,x_{m-1},h)\) is unimodular, since \(h=x_1+x_m\). The apex \(u\) has \(h(u)=2\), exactly one primitive lattice unit above the base \(h=1\). The pyramid therefore has volume \(2^{m-2}/m!\). By the exact dissection this is precisely the removed volume. Finally, the map from the standard interval-coordinate lattice to the type-\(A_m\) root lattice sends \(e_k\) to the simple root \(e_k-e_{k+1}\) and is unimodular; an interval sums to \(e_i-e_{j+1}\). This transfers the formula to the directed-edge/root-polytope interpretation.

## Verification
The attached `verify.py` uses exact rational arithmetic to reconstruct every antipodal prefix/suffix pair, verify the apex/interior pairing identity for all applicable intervals, and calculate the section-coordinate determinant, for each \(2\le m\le16\). If SciPy is available, it also independently compares convex-hull volumes before and after deletion for all \(2\le m\le8\). An actual execution passed all exact identities and seven independently computed volume comparisons. Those bounded computations are supporting tests, not the universal proof; the latter is the symbolic dissection and determinant calculation above.

## Relationship to prior work
Numata, Takahashi and Tamaki (2022) develop face theory for general directed-edge polytopes, providing the natural root-polytope framework. Setiabrata (2020) characterizes faces of origin-adjoined positive-root polytopes. Hille (2015) studies their Catalan-volume and triangulation structures. These results give important background but do not directly give the exact crosspolytopal region removed on deleting the highest positive root or its power-of-two normalized volume. A related classification of the *one-skeleton* of the nonorigin positive-root polytope describes its edge adjacencies; adjacency alone does not determine the deleted pyramid or its lattice covolume. The asserted result is the geometric dissection and volume loss, not the pre-existing root-polytope construction or general face theory.

## Limitations
The theorem concerns a single distinguished longest interval, not arbitrary vertex deletions. It does not compute every face or Ehrhart polynomial of the remaining polytope. In particular no claims of previously unknown global volume formulas, independent certification, or exhaustive bibliographic uniqueness are made. Earlier literature under different terminology may describe an equivalent volume truncation; not every historical full text was accessible.

## References
- Y. Numata, Y. Takahashi and D. Tamaki, *Faces of Directed Edge Polytopes*, arXiv:2203.14521v1, first posted 2022-03-28, primary MSC2020 52B05. https://arxiv.org/pdf/2203.14521
- L. Setiabrata, *Faces of Root Polytopes*, arXiv:2001.05191v1, first posted 2020-01-15. https://arxiv.org/pdf/2001.05191
- L. Hille, *Tilting Modules over Path Algebra of Type A, Polytopes and Catalan Numbers*, arXiv:1505.06011v1, first posted 2015-05-22. https://arxiv.org/pdf/1505.06011
