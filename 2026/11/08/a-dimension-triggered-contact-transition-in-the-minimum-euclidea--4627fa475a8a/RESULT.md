# A dimension-triggered contact transition in the minimum Euclidean sphere of sparse box-Cayley polytopes

## Finding

For integers \(d\ge3\) and \(\alpha,\beta\ge1\), put
\[
P_{d;\alpha,\beta}=\operatorname{conv}\!\left(
([0,\alpha]^d\times\{0\})\ \cup\
\bigcup_{j=1}^d([0,\beta e_j]\times\{e_j\})\right)
\subset\mathbb R_x^d\times\mathbb R_y^d.
\]
Here \(e_j\) is the \(j\)-th coordinate unit vector, and \([0,\beta e_j]\) is a line segment in the fiber coordinates. Every point is measured in the **specified standard Euclidean embedding** in \(\mathbb R^{2d}\).

Write \(\mathbf1=(1,\ldots,1)\). The unique center of the smallest enclosing Euclidean ball is \((c\mathbf1,t\mathbf1)\), with the following explicit data.

**When \(1\le\beta<\alpha\)**, let
\[
L_0=d\alpha^2+\frac1d,\qquad V_0=\frac{d-1}{d},\qquad
q_0=\frac{L_0-V_0}{2L_0}.
\]
Then
\[
c=\alpha q_0,\quad t=\frac{1-q_0}{d},\qquad
R^2=\frac{d(d\alpha^2+1)^2}{4(d^2\alpha^2+1)}.
\]
The only vertices on the enclosing sphere are \((\alpha\mathbf1,0)\) and the \(d\) vertices \((0,e_j)\). Thus all \(d\) vertices \((\beta e_j,e_j)\) are strictly inside: changing \(\beta\) within this regime does not change the optimal ball.

**When \(\beta\ge\alpha\)**, let
\[
L_1=\frac{(d\alpha-\beta)^2+1}{d},\quad
V_1=\frac{d-1}{d}(\beta^2+1),\quad
\Delta=d^2\alpha^2-2d\alpha\beta-(d-2)(\beta^2+1),
\]
and set
\[
q_1=\max\left\{0,\frac{L_1-V_1}{2L_1}\right\}.
\]
Then
\[
c=\alpha q_1+\frac\beta d(1-q_1),\quad
 t=\frac{1-q_1}{d},\quad
R^2=V_1+q_1^2L_1
=\begin{cases}
V_1,&\Delta\le0,\\
\displaystyle\frac{d(d\alpha^2-2\alpha\beta+\beta^2+1)^2}{4((d\alpha-\beta)^2+1)},&\Delta>0.
\end{cases}
\]
All \(d\) vertices \((\beta e_j,e_j)\) are contacts; the additional vertex \((\alpha\mathbf1,0)\) is a contact **if and only if** \(\Delta\ge0\). No other vertices contact the sphere.

In particular, for each pair of positive integers \(\beta>\alpha\), let
\[
d_+(\alpha,\beta)=\frac{2\alpha\beta+\beta^2+1+
\sqrt{(2\alpha\beta+\beta^2+1)^2-8\alpha^2(\beta^2+1)}}{2\alpha^2}>2.
\]
For integer \(d\ge3\), the all-\(\alpha\) cube vertex is strictly interior for \(d<d_+\), becomes a contact at \(d=d_+\) (when integral), and is a contact for \(d>d_+\). For example \((\alpha,\beta)=(1,2)\) gives \(d_+=(9+\sqrt{41})/2\), so the additional contact first appears at \(d=8\). At that dimension \((c,t,R^2)=(10/37,9/74,162/37)\).

## Assumptions and scope

The result concerns the smallest **enclosing** Euclidean ball, not the largest inscribed ball or the John ellipsoid. The box-Cayley realization, orthogonal indicator coordinates, and unscaled ambient Euclidean metric are part of the definition. Dimensions \(d\ge3\) and both integral parameters at least one are essential to the screening inequalities used in the proof; no assertion is made here about the entire positive-real parameter domain, or dimensions one and two. All stated contact counts refer to vertices of \(P_{d;\alpha,\beta}\), not to its uncountably many boundary points.

## Proof

**1. Vertex and symmetry reduction.** For each cube vertex \(u\in\{0,\alpha\}^d\), the point \((u,0)\) is a vertex. At each \(y=e_j\), the fiber is the segment with endpoints \((0,e_j)\) and \((\beta e_j,e_j)\), both vertices. Their convex hull is \(P_{d;\alpha,\beta}\). The barycentric coordinate \(y\) distinguishes the simplex fibers, so no endpoint is redundant. Since every minimum enclosing ball is unique and the polytope is invariant under simultaneous coordinate permutations, its center necessarily has the form \((c\mathbf1,t\mathbf1)\).

At such a center, the squared distance to a base cube vertex with \(s\) nonzero coordinates is
\[
s(\alpha-c)^2+(d-s)c^2+dt^2,
\]
which is **affine in \(s\)**. Thus the farthest cube vertex belongs to the two extremes \(O=(0,0)\) and \(A=(\alpha\mathbf1,0)\). At the top of each fiber the two possible squared distances are
\[
D_B=dc^2+dt^2+1-2t,
\qquad D_C=D_B+\beta^2-2\beta c.
\]
Furthermore \(D_B-D_O=1-2t\).

**2. An exact sphere lemma.** Let \(Q_1,\ldots,Q_d\) be points with mean \(b\), all satisfying \(\|Q_j-b\|^2=V>0\), and let \(A\) be an extra point with \(L=\|A-b\|^2>0\). Assume furthermore that \(\langle A-b,Q_j-b\rangle=0\) for every \(j\), as happens when the \(Q_j\) form one transitive permutation orbit and \(A\) is fixed by that symmetry. The minimum enclosing center of these points is
\[
z=b+q(A-b),\qquad q=\max\left\{0,\frac{L-V}{2L}\right\},
\]
with squared radius \(V+q^2L\). Indeed the average squared distance to the \(Q_j\) is \(V+\|z-b\|^2\), and the distance to \(A\) is \(\|z-A\|^2\). The perpendicular component of \(z-b\) increases both quantities, so this lower bound is minimized on that line. By the stated orthogonality hypothesis, the proposed center on the line is equidistant from every \(Q_j\), thus it attains the lower bound. Minimizing \(\max\{V+q^2L,(1-q)^2L\}\) gives the formula. For \(L>V\) the two terms balance, whereas for \(L\le V\) the mean \(b\) already minimizes the symmetric orbit radius. Equivalently, the proposed center lies in the convex hull of the contacting points, furnishing a global minimum-enclosing-ball certificate.

**3. The regime \(\beta<\alpha\).** Apply the lemma with \(Q_j=B_j=(0,e_j)\) and \(A=(\alpha\mathbf1,0)\). Their mean is \(b=(0,\mathbf1/d)\), squared spread \(V_0=(d-1)/d\), and \(L_0=d\alpha^2+1/d>V_0\). This yields the first formula, including \(q_0>0\). Since
\[
2c=\alpha\left(1-\frac{d-1}{d^2\alpha^2+1}\right)
>\alpha-1\ge\beta,
\]
we have \(D_C<D_B\). Also \(0<t<1/d<1/2\), so \(D_O<D_B\). By the affine-in-\(s\) cube-distance formula, every cube vertex other than \(A\) is strictly closer than \(A\) (indeed \(2c<\alpha\), giving strictly positive slope). The ball enclosing \(A\) and all \(B_j\) therefore contains every vertex, has exactly the stated contacts, and is minimal for the whole polytope.

**4. The regime \(\beta\ge\alpha\).** Apply the lemma to \(Q_j=C_j=(\beta e_j,e_j)\) and \(A\). The mean is \(b=(\beta\mathbf1/d,\mathbf1/d)\); its orbit spread is \(V_1\) and its squared separation from \(A\) is \(L_1\). This yields \(q_1,c,t,R\), and \(L_1-V_1=\Delta/d\). To prove that the unselected top vertices \(B_j\) are strictly interior, it suffices to show \(2c<\beta\). Since \(\alpha\le\beta\) and \(d\ge3\),
\[
|d\alpha-\beta|\le(d-1)\beta,
\quad L_1<\frac{(d-1)^2(\beta^2+1)}d=(d-1)V_1.
\]
Consequently \(q_1<(d-2)/(2(d-1))\); this also holds when \(q_1=0\). Hence
\[
c\le \beta\left(q_1+\frac{1-q_1}{d}\right)<\beta/2,
\]
so \(D_B<D_C\). We also have \(0<t\le1/d<1/2\), so \(D_O<D_B\). Moreover \(2c<\beta\) and \(\alpha\le\beta\) imply \(2c<\alpha\) is not automatic; this is unnecessary: every cube distance is at most \(\max\{D_O,D_A\}\), with \(D_O<R^2\) and \(D_A\le R^2\). If \(L_1>V_1\), the apex \(A\) is a contact; if \(L_1=V_1\), it remains a contact at \(q_1=0\); and if \(L_1<V_1\), it lies strictly inside. When \(A\) and \(O\) have equal distance, intermediate cube points can only contact at that radius, but \(O\) is strictly interior, so no additional contacts occur. This proves the complete vertex-contact classification.

**5. Sharp dimension threshold.** For fixed \(\beta>\alpha\), the sign of \(\Delta\) is the sign of
\[
\alpha^2d^2-(2\alpha\beta+\beta^2+1)d+2(\beta^2+1).
\]
At \(d=2\) it is \(4\alpha(\alpha-\beta)<0\), while it tends to \(+\infty\) as \(d\to\infty\). It therefore has exactly one real root greater than two, equal to \(d_+\), and its sign changes precisely as stated. The displayed numerical example follows by direct substitution. The uniqueness of each minimum enclosing center follows from strict convexity of the squared-norm term: if two distinct centers enclosed at the same radius, their midpoint would strictly reduce the maximum squared distance over the finite vertex set.

## Verification

Run `python3 check.py` with Python 3. The standard-library exact checker enumerates all \(2^d+2d\) vertices for dimensions \(3\le d\le10\) and parameters \(1\le\alpha,\beta\le7\), checking the stated center, containment, equality cases, and positive barycentric support. It reported 107,408 exact rational assertions, including 105,056 point-distance comparisons. With SciPy available, the independent SLSQP routine solves 66 unrestricted three-variable epigraph problems for the four vertex-orbit squared distances and checks the same answer. These finite checks only corroborate the symbolic proof above.

## Relationship to prior work

Ferroni's September 9, 2026 preprint introduces and studies Cayley sums of rectangular boxes, including the sparse matrix \([\alpha\mathbf1_d\mid\beta I_d]\), for Ehrhart theory. Its Cayley construction, integer decomposition, and related smoothness facts are prior work; the present theorem concerns Euclidean minimum-enclosing balls and their contacts instead. Standard Euclidean minimum-enclosing-ball convex-hull criteria are also classical and are used without a claim of priority. Earlier work on inscribed Euclidean balls of the same box-Cayley family concerns a different extremal quantity; an inball radius or its incenter locus does not imply an enclosing-ball contact transition. Searches among related geometric results did not identify an equivalent all-dimensional theorem for this sparse family, but this is not a proof of historical uniqueness.

## Limitations

The theorem treats only \(d\ge3\) and positive **integer** \(\alpha,\beta\), and fixes the canonical orthogonal coordinate embedding. A nonisometric affine re-embedding may change the minimum enclosing sphere. The vertex classification says nothing additional about nonvertex points of intersection between the polytope and the optimal sphere; strict convexity does imply that no nonvertex point can lie on that sphere. The result does not give the John or Löwner ellipsoids, the exact inradius outside the known saturation regime, or arbitrary matrix parameters. Historical priority remains subject to broader bibliographic and independent review.

## References

1. L. Ferroni, *Unimodality shenanigans in Ehrhart theory*, arXiv:2609.10513, first posted 2026-09-09. Primary definition and sparse matrix family.
2. M. Bădoiu and K. L. Clarkson, *Smaller core-sets for balls*, Proceedings of SODA (2003). General background on minimum-enclosing-ball geometry; no claimed overlap with the special family theorem.
