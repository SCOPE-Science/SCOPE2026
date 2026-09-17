# Exact Sylvester--Gallai dimension of \(K_{2,n}\)

## Statement

Let \(\operatorname{SGdim}(G)\) denote the Sylvester--Gallai dimension of a graph \(G\): the maximum affine dimension of a configuration of distinct real points indexed by \(V(G)\) such that every line determined by an edge contains at least one further point of the configuration.

**Theorem.** For every integer \(n\ge 1\),
\[
\boxed{\operatorname{SGdim}(K_{2,n})=1+\left\lfloor\frac n4\right\rfloor.}
\]

Thus the asymptotic order \(\Theta(n)\) known for this complete-bipartite family has exact leading constant \(1/4\), together with the exact lower-order term.

A slightly more informative form of the upper bound is the following. In any special-line realization of \(K_{2,n}\), let \(x,y\) be the two vertices in the part of size \(2\), let \(L=xy\), and let \(B^\ast\) be the vertices of the other part whose points do not lie on \(L\). If \(c\) is the number of connected components of the incidence graph defined below, then
\[
\operatorname{affdim}(P)\le c+1,\qquad 4c\le |B^\ast|.
\]

## Proof

Write the bipartition of \(K_{2,n}\) as
\[
\{x,y\}\sqcup B,\qquad |B|=n,
\]
and consider an arbitrary special-line realization by distinct points. We use the same letters for vertices and their points.

Let \(L=xy\), and put
\[
B^\ast=\{b\in B:b\notin L\}.
\]

### 1. An auxiliary bipartite incidence graph

For each \(b\in B^\ast\), let
\[
X_b=xb,\qquad Y_b=yb.
\]
Let \(\mathcal X\) be the set of distinct lines \(X_b\), and let \(\mathcal Y\) be the set of distinct lines \(Y_b\). Define a bipartite graph \(Q\) with parts \(\mathcal X,\mathcal Y\) by assigning to every \(b\in B^\ast\) the edge
\[
X_bY_b.
\]

This graph is simple. Indeed, for \(b\notin L\), the lines \(X_b\) and \(Y_b\) are distinct. If two distinct points \(b,b'\) gave the same pair \((X_b,Y_b)\), both would lie in the intersection of the same two distinct lines, which is impossible.

Moreover,
\[
\delta(Q)\ge 2.
\]
To see this, take \(X_b\in\mathcal X\). Since \(xb\) is an edge of \(K_{2,n}\), its line is special and contains a third configuration point. This point cannot be \(y\), because \(b\notin L\), and it cannot be a member of \(B\setminus B^\ast\), because \(X_b\) meets \(L\) only at \(x\). Hence it is another point \(b'\in B^\ast\) on the same line through \(x\), giving a second edge of \(Q\) incident with \(X_b\). The argument for vertices of \(\mathcal Y\) is identical.

Every connected component of a finite simple bipartite graph of minimum degree at least \(2\) contains a cycle, and every such cycle has length at least \(4\). Therefore every component of \(Q\) has at least four edges. If \(Q\) has \(c\) connected components, then
\[
4c\le |E(Q)|=|B^\ast|.
\tag{1}
\]

### 2. Each incidence component lies in one page

Fix a connected component \(C\) of \(Q\), choose any edge corresponding to \(b\in B^\ast\), and set
\[
\Pi_C=\operatorname{aff}\{x,y,b\}.
\]
Because \(b\notin L\), this is an affine plane containing \(L\).

If two edges of \(Q\), corresponding to \(b,b'\in B^\ast\), are adjacent in \(Q\), then either \(X_b=X_{b'}\) or \(Y_b=Y_{b'}\). In the first case \(b'\in xb\subseteq\Pi_C\); in the second \(b'\in yb\subseteq\Pi_C\). Following a path in the connected component shows that every point corresponding to an edge of \(C\) lies in the same plane \(\Pi_C\).

Consequently the whole realization lies in
\[
L\cup \Pi_1\cup\cdots\cup\Pi_c,
\]
where every \(\Pi_i\) contains the common line \(L\). After translating one point of \(L\) to the origin, the direction space of \(L\) has dimension \(1\), and each plane \(\Pi_i\) can add at most one further independent direction modulo \(L\). Hence
\[
\operatorname{affdim}(P)\le c+1.
\tag{2}
\]
Combining (1) and (2),
\[
\operatorname{affdim}(P)
\le 1+\left\lfloor\frac{|B^\ast|}{4}\right\rfloor
\le 1+\left\lfloor\frac n4\right\rfloor.
\tag{3}
\]

This proves the upper bound.

### 3. Sharp construction

Write
\[
n=4q+r,\qquad 0\le r<4.
\]
Work in \(\mathbb R^{q+1}\) with basis \(e_0,e_1,\ldots,e_q\), and place
\[
x=0,\qquad y=e_0.
\]
For each \(j=1,\ldots,q\), in the plane spanned by \(e_0,e_j\), place four vertices of \(B\) at
\[
\frac12e_0+\frac12e_j,\qquad
\frac23e_0+\frac23e_j,\qquad
\frac13e_0+\frac23e_j,\qquad
\frac12e_0+e_j.
\tag{4}
\]

In coordinates \((t,s)\) on this plane, these are the four intersections of the two lines through \(x=(0,0)\)
\[
s=t,\qquad s=2t
\]
with the two lines through \(y=(1,0)\)
\[
s=1-t,\qquad s=2(1-t).
\]
Thus each of the four points has another configuration point on its line to \(x\), and another configuration point on its line to \(y\). Every edge from \(x\) or \(y\) to these four vertices therefore lies on a special line.

Place the remaining \(r\) vertices of \(B\) at arbitrary distinct unused points of the line \(L=xy\). Their incident edges are special because \(x\), \(y\), and each such point are collinear.

The resulting configuration is a special-line realization of \(K_{2,n}\). It affinely spans all of \(\mathbb R^{q+1}\): \(e_0=y-x\), and from the first point in (4),
\[
e_j=2\left(\frac12e_0+\frac12e_j\right)-e_0.
\]
Therefore
\[
\operatorname{SGdim}(K_{2,n})\ge q+1
=1+\left\lfloor\frac n4\right\rfloor.
\]
Together with (3), this proves the theorem. \(\square\)

## Context and comparison with prior work

Dvir introduced the graph parameter \(\operatorname{SGdim}\) in 2026. The paper's Observation 2.5 specifically treats complete bipartite graphs: for \(K_{m,s}\) with \(m\ge s\), it records a lower bound \(\Omega(m/s)\) from the book construction and an asymptotically matching upper bound from the quantitative Sylvester--Gallai theorem. The paper does not state an exact value for \(K_{2,n}\) or \(K_{n,2}\).

The theorem above specializes to the fixed-side case \(s=2\) and replaces those asymptotic bounds by an exact formula for every \(n\). Its upper-bound mechanism is different from the general quantitative rank bound: it converts the special-line witnesses into a simple bipartite incidence graph of minimum degree two. The four-edge minimum for each incidence component is exactly what produces the factor \(1/4\), while each component can contribute at most one affine dimension beyond the common spine.

## Sanity checks

- \(1\le n\le 3\): the formula gives \(1\). Indeed, any off-spine vertex would create a component of \(Q\) with at least four edges, impossible, so all points are collinear.
- \(n=4\): the four-point page in (4) gives dimension \(2\), and the upper bound gives \(2\).
- Adding one, two, or three vertices on the spine does not increase dimension, explaining the floor term.

## Limitations

The result determines only the family \(K_{2,n}\); it does not give an exact formula for general \(K_{s,n}\) with \(s\ge3\), nor does it classify all dimension-maximizing realizations.

Originality is asserted only to the best of our knowledge. The full HTML text of the 2026 source introducing \(\operatorname{SGdim}\) was inspected, including its complete-bipartite observation. Targeted searches for the exact formula and equivalent \(K_{n,2}\)/complete-bipartite formulations found no separate prior statement. Because the parameter is very recent, residual risk remains from very recent or poorly indexed follow-up work.

No independent validation is asserted.

## References

1. Zeev Dvir, *The Sylvester--Gallai dimension of graphs*, arXiv:2608.15967v1 (2026), especially Definition 1.1, Theorem 1.2, and Observation 2.5. https://arxiv.org/abs/2608.15967
