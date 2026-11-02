# Complete degree spectrum of commuting-involution graphs in three-block unipotent groups

## Finding
Let \(q\) be an even prime power and \(s,t\ge2\). The commuting-involution graph of the three-block unipotent group of sizes \((s,t,1)\), with the identity excluded, has an explicitly determined degree multiset and exact number of edges, for every \(q,s,t\).

Put \(N_{s,t}(a;q)={s\brack a}_q{t\brack a}_q|\operatorname{GL}_a(\mathbb F_q)|\), the standard number of rank-\(a\) matrices of size \(s\times t\). Its vertices occur in two disjoint types:

* **Zero terminal vector:** For every \(0\le a\le\min(s,t)\), there are \(q^sN_{s,t}(a;q)-\mathbf1_{a=0}\) vertices of degree
\[
d_a=q^s\left[q^{st}+(q^{t-a}-1)q^{s(t-1)}\right]-2.
\]
* **Nonzero terminal vector:** There are \(q^s(q^t-1)q^{s(t-1)}\) vertices of the common degree
\[
d_*=q^s\left[q^{1+s(t-1)}+(q^t-q)q^{s(t-2)}\right]-2.
\]

The multiplicities are added whenever two numerical degrees coincide. In particular the exact vertex count \(I-1\) and edge count \(E\) are
\[
I=q^s\left[q^{st}+(q^t-1)q^{s(t-1)}\right],\qquad E=\frac{C-3I+2}{2},
\]
where
\[
C=q^{2s}\left[q^{2st}+(q+1)(q^t-1)q^{2s(t-1)}+(q^t-1)(q^t-q)q^{s(2t-3)}\right].
\]

For \((s,t,q)=(2,2,2)\), the group has order \(256\); its commuting-involution graph has \(111\) vertices, \(3225\) edges, and exactly \(3,36,24,48\) vertices of degrees \(110,78,62,38\), respectively. This nonregularity beyond the central involutions is uniform in higher block sizes.

## Assumptions and scope
Over \(k=\mathbb F_q\), define \(U_{s,t}(q)\) to be the group of matrices
\[
u(X,y,z)=\begin{pmatrix}I_s&X&z\\0&I_t&y\\0&0&1\end{pmatrix},\quad X\in M_{s,t}(k),\quad y\in k^t,\quad z\in k^s.
\]
The group is the unipotent radical of the standard parabolic subgroup with block sizes \((s,t,1)\). The graph vertices are elements of order **exactly** two (not the identity); distinct vertices are adjacent if they commute. There are no loops. Characteristic two and \(s,t\ge2\) are assumed for the group-theoretic statement. The underlying matrix identities remain valid over odd-characteristic fields, but their square-zero solutions are then not involutions.

## Proof
Write \(u=1+N\) with the strictly upper-block part \(N\). Since the field has characteristic two,
\[
u^2=1\iff N^2=0\iff Xy=0.
\]
For \(u(X,y,z)\) and \(u(X',y',z')\), multiplication gives
\[
[u,u']=1\iff Xy'=X'y.
\]
Both properties are independent of central coordinates \(z,z'\). The number of involutions **including** the identity is therefore \(q^s\) times the number of pairs \((X,y)\) with \(Xy=0\). For \(y=0\), all \(q^{st}\) choices of \(X\) work; for each of the \(q^t-1\) nonzero \(y\), the condition imposes exactly one independent linear equation on each of the \(s\) rows, leaving \(q^{s(t-1)}\) matrices. This proves the formula for \(I\) and the type multiplicities.

Fix a square-zero pair \((X,0)\) of rank \(a\). A commuting involution \((X',y')\) must obey \(Xy'=0\) and \(X'y'=0\). There are \(q^{t-a}\) possible vectors \(y'\) in \(\ker X\). When \(y'=0\), any of the \(q^{st}\) matrices \(X'\) works; for every nonzero \(y'\in\ker X\), there are \(q^{s(t-1)}\) choices. Multiplying by \(q^s\) independent choices for \(z'\) yields \(d_a+2\) commuting involutions including the identity and the fixed element itself.

Now fix \((X,y)\) with \(y\ne0\) and \(Xy=0\). For each \(y'\) in the line \(ky\) (exactly \(q\) choices), the constraints \(X'y= Xy'=0\) and \(X'y'=0\) reduce to \(X'y=0\), giving \(q^{s(t-1)}\) matrices. For each of the \(q^t-q\) vectors \(y'\notin ky\), the two prescribed values \(X'y=Xy'\) and \(X'y'=0\) impose independent conditions on each row of \(X'\), giving \(q^{s(t-2)}\) matrices. The arbitrary central block multiplies the sum by \(q^s\), proving \(d_*+2\). Subtracting both the identity and the fixed vertex gives the claimed loopless degrees.

To count **ordered commuting pairs** among all involutions including identity, classify the ordered vectors \((y,y')\) by their span dimension. There is one zero pair; there are \((q+1)(q^t-1)\) ordered pairs spanning a line; and \((q^t-1)(q^t-q)\) pairs spanning a plane. For each row of \((X,X')\), the equations \(Xy=0\), \(X'y'=0\), \(Xy'=X'y\) have respectively \(0,2,3\) independent scalar constraints. Thus the numbers of choices for \((X,X')\) are respectively \(q^{2st}\), \(q^{s(2t-2)}\), and \(q^{s(2t-3)}\). Two independent central coordinates add a factor \(q^{2s}\), proving the displayed formula for \(C\).

Among these \(C\) ordered commuting involution pairs, the \(2I-1\) pairs incident with the identity are discarded. The \(I-1\) remaining diagonal pairs are also discarded. Each edge is represented by two ordered pairs, giving \(E=(C-3I+2)/2\). This completes the proof for every even prime power and every \(s,t\ge2\).

## Verification
The self-contained `verify.py` implements the group coordinates and checks all square-zero pairs and all commuting pairs directly, without using the asserted matrix-rank degree formulas to decide membership. Exhaustive configurations include \((s,t,q)=(2,2,2),(2,3,2),(2,2,3),(1,2,4)\); further small boundaries are included. It verifies all vertex degree formulas and the ordered-pair total. In particular \((2,2,2)\) gives \(I=112\) and \(C=6784\), hence \(E=3225\). The odd-field configurations test only the algebraic square-zero/commutativity identities, not the involution interpretation. Finite tests do not prove the unrestricted theorem, which follows from the linear-algebra argument above.

## Relationship to prior work
Evseev (arXiv:0801.3178, first posted 2008-01-21) studies parabolic conjugacy class enumeration. Goodwin and Röhrle (arXiv:0901.0667, first posted 2009-01-06; Pacific Journal of Mathematics 245 (2010), 47–56) establish polynomiality of numbers of conjugacy classes of unipotent radicals with flag length at most five and describe single-element centralizer structure. Those results concern conjugacy classes or centralizers of individual elements, not the degree distribution of the graph induced on **order-two elements**. This degree distribution counts the involutions *inside* each involution's centralizer and is not obtained from a single-element centralizer order alone. The elementary two-generated/extraspecial polar-graph boundary is not claimed as new; here \(s,t\ge2\) and the underlying commutator map has overlapping matrix-multiplication channels, not independent graphical edges.

## Limitations
Only the unipotent radicals with three blocks of sizes \((s,t,1)\) in characteristic two are covered. The result does not determine graph spectra, graph isomorphism classes, numbers of higher cliques, or analogous degrees when both exterior blocks have dimension greater than one. Publication priority remains subject to independent historical review, especially literature on incidence of involutions in parabolic unipotent radicals. No independent mathematical audit has been performed.

## References
1. A. Evseev, *Conjugacy classes in parabolic subgroups of general linear groups*, arXiv:0801.3178, first posted 2008-01-21, https://arxiv.org/abs/0801.3178.
2. S. M. Goodwin and G. Röhrle, *Counting conjugacy classes in the unipotent radical of parabolic subgroups of general linear groups*, arXiv:0901.0667, first posted 2009-01-06, https://arxiv.org/abs/0901.0667; *Pacific Journal of Mathematics* **245** (2010), 47–56, https://doi.org/10.2140/pjm.2010.245.47.
