# Exact vertex-convexification threshold of every convex quadrilateral

## Finding

Let \(Q\subset\mathbb R^2\) be a nondegenerate convex quadrilateral, with four-element vertex set \(V(Q)\). Let its diagonals intersect, and let \(p,q\in(0,1]\) be the shorter-to-longer division ratios on the respective diagonals. For the vertex-convexification index
\[
 c_V(Q):=\inf\{\lambda>0:V(Q)+\lambda Q=(1+\lambda)Q\},
\]
we prove the **complete affine-invariant formula**
\[
\boxed{c_V(Q)=1+\frac{1-pq}{1+\max\{p,q\}}.}
\]
In particular the displayed Minkowski identity holds if and only if \(\lambda\ge c_V(Q)\). Consequently \(1\le c_V(Q)<2\), with equality at the lower endpoint precisely for parallelograms. The attained range over all nondegenerate convex quadrilaterals is exactly \([1,2)\).

## Assumptions and scope

The quadrilateral must have four distinct extreme vertices and nonempty interior; its diagonals then cross strictly inside. The shorter-to-longer ratios are strictly positive and at most one. All sets are closed and Minkowski addition is literal set addition. This is a statement about the four vertices combined with the entire convex quadrilateral, not repeated vertex-only averaging or a Euclidean covering radius. The index and the ratios are invariant under invertible affine transformations.

## Proof

**Affine normalization.** Translate the diagonal intersection to the origin and choose each positive coordinate endpoint to be the longer diagonal half. Independent affine scaling of the diagonal directions sends the vertices to
\[
Q_{p,q}=\operatorname{conv}\{(-p,0),(1,0),(0,-q),(0,1)\},\qquad 0<p,q\le1.
\]
Interchanging the coordinates allows \(p\le q\). Put
\[
 a_r(t)=\begin{cases}t,&t\ge0,\\-t/r,&t\le0.\end{cases}
\]
The Minkowski functional of the normalized body is \(a_p(x)+a_q(y)\), and
\[
Q_{p,q}=\{(x,y):a_p(x)+a_q(y)\le1\}.
\]

**Reduction to a rectangle.** Fix \(\lambda\ge1\) and put \(R=[-p,1]\times[-q,1]\). For \(z=(x,y)\in(1+\lambda)Q_{p,q}\) outside \(R\), at least one of \(x\ge1\), \(x\le-p\), \(y\ge1\), \(y\le-q\) holds. Choose the corresponding vertex \(v\) of the quadrilateral. The appropriate one-dimensional gauge component satisfies \(a_r(t-v_i)=a_r(t)-1\), so
\[
 a_p(x-v_x)+a_q(y-v_y)=a_p(x)+a_q(y)-1\le\lambda.
\]
Thus every point outside \(R\) already belongs to \(V(Q_{p,q})+\lambda Q_{p,q}\).

Within \(R\), define the two tent functions
\[
 m_p(x)=\min\{x+p,(1-x)/p\},\qquad m_q(y)=\min\{y+q,(1-y)/q\}.
\]
The minimum translated gauge over all four vertices is exactly
\[
 F(x,y)=\min\{m_p(x)+a_q(y),\ a_p(x)+m_q(y)\}.
\]
Therefore every point of \(R\) is covered once \(\lambda\ge\max_R F\). Conversely any maximizer \(z_*\in R\cap 2Q_{p,q}\) with \(F(z_*)=\max_R F>\lambda\ge1\) is a point in \((1+\lambda)Q_{p,q}\) missed by all four vertex translates.

**Exact four-quadrant maximum.** We compute the maximum on \(R\), assuming \(p\le q\).

In the southwest quadrant write \(x=-pu,y=-qv\), with \(0\le u,v\le1\). The two arguments of the minimum become \(p(1-u)+v\) and \(u+q(1-v)\). Their sum is at most two, hence \(F\le1\).

In the northwest quadrant \(x=-pu\), \(y\in[0,1]\). If \(p(1-u)+y\le1\), the desired estimate \(F\le1\) is immediate. Otherwise \(y>1-p(1-u)\ge1-q\), whence \(m_q(y)=(1-y)/q<p(1-u)/q\le1-u\). Then the second argument, \(u+m_q(y)\), is less than one. So again \(F\le1\).

In the southeast quadrant \(x\in[0,1]\), \(y=-qv\), where \(0\le v\le1\). The two affine-in-\(v\) quantities are \(m_p(x)+v\) and \(x+q(1-v)\). Their intersection occurs at
\[
 v_*(x)=\frac{x+q-m_p(x)}{1+q}\in[0,1],
\]
using \(p\le q\). Thus the maximum over \(v\) equals
\[
 \frac{q m_p(x)+x+q}{1+q}.
\]
It increases until \(x=1-p\) and then is nonincreasing; its maximum is
\[
 1+\frac{q-p}{1+q}.
\]

In the northeast quadrant, \(x,y\in[0,1]\). Holding \(x\) fixed, below \(y=1-q\) both arguments of \(F\) increase with \(y\). On \([1-q,1]\) the first increases and the second decreases, and their intersection lies in that interval at
\[
 y_*(x)=\frac{q x+1-q m_p(x)}{1+q}.
\]
The maximal value over \(y\) is therefore \(m_p(x)+y_*(x)\). For \(0\le x\le1-p\) this increases with slope one; for \(1-p\le x\le1\) its slope is \((pq-1)/(p(1+q))\le0\). Its maximum is attained at \(x=1-p\), with value
\[
 1+\frac{1-pq}{1+q}.
\]
This dominates the southeast maximum since \(1-pq-(q-p)=(1-q)(1+p)\ge0\). Hence
\[
 \max_R F=1+\frac{1-pq}{1+q}.
\]
The exhibited maximizer \(z_*=(1-p,(1-pq)/(1+q))\) belongs to \(R\cap2Q_{p,q}\), since its gauge is \(1-p+(1-pq)/(1+q)\le2\). It proves the lower bound for every \(1\le\lambda<c_V(Q)\), and the preceding rectangle reduction proves coverage for every \(\lambda\ge c_V(Q)\).

**No value below one.** For \(\lambda<1\), take the relative interior of any edge of \((1+\lambda)Q\). Only the two vertices lying on the corresponding supporting edge of \(Q\) can contribute points from their translated copies of \(\lambda Q\) on that exposed edge. These copies cover intervals of lengths \(\lambda\) times the edge length starting at opposite ends of an edge of length \(1+\lambda\) times that edge length. Since \(2\lambda<1+\lambda\), a nonempty central subinterval remains uncovered. Thus \(c_V(Q)\ge1\), completing the threshold proof.

**Equality and range.** Because \(0<p,q\le1\), the index equals one only if \(pq=1\), that is, \(p=q=1\), equivalent to the diagonal bisection property of parallelograms. All four-vertex bodies have index less than two. Taking \(p=q=t\in(0,1]\) gives \(c_V(Q)=2-t\), realizing every value in \([1,2)\).

## Verification

The accompanying standalone `verify.py` performs an independent finite **exact rational** test. It partitions the normalized rectangle at all gauge breakpoints, computes the two affine expressions on each cell, checks all cell corners and their equality-line intersections with cell edges, and compares the exact maximum to the theorem's formula for all \(36\) pairs drawn from \(\{1,1/2,1/3,1/5,2/3,3/4\}\). Run `python verify.py`; the output is `PASS: 36 affine-shape pairs checked using exact rational polyhedral subdivision.` These finite tests corroborate but do not replace the all-parameter analytic argument above.

## Relationship to prior work

Meyer (2026) develops general necessary and sufficient criteria for eventual convexification of compact sets under Minkowski addition, including the planar case, but does not provide the above exact two-diagonal-ratio threshold. Artstein-Avidan, Falah and Slomka (2024) develop vertex-generated-polytope theory and associated general covering bounds, but not this two-parameter classification. The general Schneider nonconvexity framework, its relation to vertex-generated polytopes, and the general lower bound \(1\) are background rather than new claims. The exact all-quadrilateral formula, equality characterization and range are the present result.

## Limitations

The assertion is confined to planar nondegenerate convex quadrilaterals and the vertex-plus-dilated-same-body sum. It makes no claims about higher-dimensional polytopes, other finite point sets or other convexifiers. Although the two most relevant full-text studies were checked, older unindexed calculations could conceivably contain equivalent formulas; independent historical-priority assessment has not been performed. The rational checks are finite and are not claimed as a proof of the universal statement.

## References

1. Mark Meyer, *Finite convexification by Minkowski summation* (2026), arXiv:2610.26744v1, first submitted 2026-10-19, https://arxiv.org/html/2610.26744v1.
2. Shiri Artstein-Avidan, Tomer Falah and Boaz A. Slomka, *Vertex generated polytopes* (2024), arXiv:2407.20604v1, https://arxiv.org/html/2407.20604v1.
