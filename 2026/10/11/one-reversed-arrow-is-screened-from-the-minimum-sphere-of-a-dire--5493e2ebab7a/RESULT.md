# One reversed arrow is screened from the minimum sphere of a directed path simplex
## Finding
For integers \(m\ge3\) and \(1\le j\le m\), orient the path on \(m+1\) vertices by arrows \(i\to i+1\) except for the reversed arrow \(j+1\to j\). Its directed edge polytope is the simplex
\[
Q_{m,j}=\operatorname{conv}\{v_1,\ldots,v_m\}\subset\mathbb R^{m+1},\qquad
v_i=\begin{cases}e_i-e_{i+1},&i\ne j,\\e_{i+1}-e_i,&i=j.\end{cases}
\tag{1}
\]
Distances are inherited from ordinary Euclidean space and understood intrinsically to the affine hull of the simplex.

Set
\[
a=j-1,\qquad b=m-j,\qquad
S=a(a+1)(a+2)+b(b+1)(b+2),\qquad
\lambda=\frac{12}{S}.
\tag{2}
\]
The **unique minimum-enclosing ball** has squared radius
\[
\boxed{R_{m,j}^2=2-\lambda
=2-\frac{12}{(m+1)\bigl(m(m-1)-3(j-1)(m-j)\bigr)}.}
\tag{3}
\]
Its center is the following convex combination of all the nonreversed vertices:
\[
\boxed{c_{m,j}=\sum_{i=1}^{m}p_iv_i,}
\qquad
p_i=\begin{cases}
\frac{\lambda}{2}i(a+1-i),&1\le i\le a,\\
0,&i=j,\\
\frac{\lambda}{2}t(b+1-t),&i=j+t,\ 1\le t\le b.
\end{cases}
\tag{4}
\]
Here \(\sum_i p_i=1\), and \(p_i>0\) for every \(i\ne j\).

For every \(i\ne j\), the vertex \(v_i\) lies on the minimum sphere. The reversed-arrow vertex satisfies the exact gap
\[
\boxed{R_{m,j}^2-\|v_j-c_{m,j}\|^2
=\lambda(m-3).}
\tag{5}
\]
Thus, for \(m\ge4\), **exactly the \(m-1\) unreversed vertices are contact points**; the reversed vertex is strictly interior to the minimum sphere. Deleting that vertex has no effect on the enclosing ball. At the exceptional boundary \(m=3\), all three simplex vertices are contacts, even though its optimal convex-combination coefficient \(p_j\) vanishes.

At fixed path length, the squared radius depends on the flip position solely through
\[
(j-1)(m-j).
\]
It is smallest when \(j\) is a central edge, and largest when the flipped edge is an endpoint. Reversing any single arrow strictly reduces the radius relative to the fully consistently oriented path.

## Assumptions and scope
The directed edge polytope of an oriented graph with an arc \(u\to v\) is the convex hull of the directed incidence vectors \(e_u-e_v\). The opposite global sign convention gives an isometric reflection, so the radius statement does not depend on that convention.

A path has linearly independent edge incidence vectors. The \(m\) vertices in (1) are therefore linearly independent in the zero-sum hyperplane of \(\mathbb R^{m+1}\), and \(Q_{m,j}\) is an \((m-1)\)-simplex. This is the simplex family identified for arbitrarily oriented type-\(A\) Dynkin diagrams in the source's Example 5.2.

The theorem is metric, not purely combinatorial: all these simplices have identical face lattices, but their Euclidean minimum spheres depend sharply on the reversed-arrow position. The admissible range starts at \(m=3\), as the contact transition and formula are stated for that range.

## Proof
**Step 1: an enclosing-ball certificate.** Suppose finitely many points \(w_1,\ldots,w_m\) have common squared norm \(L\). Let \(p_i\ge0\) sum to one, put \(c=\sum_i p_iw_i\), and suppose
\[
\langle w_i,c\rangle\ge\|c\|^2\quad\text{for all }i,
\qquad
\langle w_i,c\rangle=\|c\|^2\quad\text{whenever }p_i>0.
\tag{6}
\]
Then \(\|w_i-c\|^2=L+\|c\|^2-2\langle w_i,c\rangle\le L-\|c\|^2\). For any competing center \(z\) in ambient Euclidean space, the exact weighted-average identity is
\[
\sum_i p_i\|w_i-z\|^2
=L-\|c\|^2+\|z-c\|^2.
\tag{7}
\]
The largest squared distance to the \(w_i\) is at least this average; hence it is strictly larger than \(L-\|c\|^2\) unless \(z=c\). This proves both minimality and uniqueness. Notice that no experimental optimization enters this argument.

**Step 2: the directed path Gram matrix.** Write \(s_i=1\) for \(i\ne j\) and \(s_j=-1\). Then \(v_i=s_i(e_i-e_{i+1})\), and the Gram matrix satisfies
\[
G_{ii}=2,\qquad G_{i,i+1}=G_{i+1,i}=-s_is_{i+1},\qquad G_{ik}=0\text{ if }|i-k|>1.
\tag{8}
\]
Inside the two consistently oriented blocks \(\{1,\ldots,a\}\) and \(\{j+1,\ldots,m\}\), this is the tridiagonal matrix with diagonal \(2\) and off-diagonal \(-1\). At the two possible links to the flipped edge its off-diagonal entries are instead \(+1\).

**Step 3: the exact nonnegative certificate.** For each integer \(L\ge1\), define
\[
q_u^{(L)}=\frac\lambda2u(L+1-u)\quad(1\le u\le L),
\qquad q_0^{(L)}=q_{L+1}^{(L)}=0.
\tag{9}
\]
A direct second-difference calculation gives
\[
2q_u^{(L)}-q_{u-1}^{(L)}-q_{u+1}^{(L)}=\lambda.
\tag{10}
\]
Also,
\[
\sum_{u=1}^{L}u(L+1-u)=\frac{L(L+1)(L+2)}6.
\tag{11}
\]
For the empty block \(L=0\), both formulas are interpreted as zero contributions. By (2), (4), and (11),
\[
\sum_{i=1}^{m}p_i
=\frac\lambda{12}\bigl(a(a+1)(a+2)+b(b+1)(b+2)\bigr)=1.
\tag{12}
\]
All nonzero weights are positive. Equations (8) and (10) imply
\[
(Gp)_i=\lambda\quad(i\ne j).
\tag{13}
\]
At the flipped position, the two adjacent coefficients contribute with the positive sign:
\[
(Gp)_j=p_{j-1}+p_{j+1}
=\frac\lambda2(a+b)
=\frac\lambda2(m-1),
\tag{14}
\]
where a coefficient beyond either path endpoint is defined as zero.

Since \(p_j=0\) and \(\sum_i p_i=1\), equations (13)--(14) yield
\[
\|c\|^2=p^{\mathsf T}Gp=\lambda.
\tag{15}
\]
Because \(m\ge3\), equations (13)--(15) show exactly the optimality conditions (6) with \(L=2\). By Step 1, \(c\) is the unique minimum-enclosing-ball center and the squared radius is \(2-\lambda\).

**Step 4: the complete contact spectrum.** For \(i\ne j\), equations (13) and (15) show \(\|v_i-c\|^2=2-\lambda\). For the reversed vertex, equations (14)--(15) give
\[
\|v_j-c\|^2
=2+\lambda-\lambda(m-1)
=2-\lambda(m-2),
\tag{16}
\]
so its deficit relative to the squared radius is \(\lambda(m-3)\). This is zero only at \(m=3\) and positive for all \(m\ge4\). For \(m\ge4\), the supported vertices constitute exactly the facet opposite \(v_j\), and deleting \(v_j\) preserves the same optimal ball by the same Step 1 certificate.

**Step 5: position and comparison laws.** The elementary identity
\[
a(a+1)(a+2)+b(b+1)(b+2)
=(m+1)\bigl(m(m-1)-3ab\bigr),
\tag{17}
\]
which follows from \(a+b=m-1\), proves the second form of (3). For fixed \(m\), larger \(ab\) decreases \(S\), hence increases \(\lambda\) and decreases \(R^2\). Its maximum occurs when \(a,b\) differ by at most one; its minimum zero occurs at an endpoint reversal.

For comparison, the consistently oriented path has Gram matrix with off-diagonals \(-1\) and all \(m\) positive barycentric weights
\[
\widetilde p_i=\frac{6i(m+1-i)}{m(m+1)(m+2)},\qquad
\widetilde\lambda=\frac{12}{m(m+1)(m+2)}.
\tag{18}
\]
Repeating Steps 1--3 gives its squared enclosing radius \(2-\widetilde\lambda\). With \(a+b=m-1\), the factor \(S/(m+1)=m(m-1)-3ab\) is strictly smaller than \(m(m+2)\). Therefore \(\lambda>\widetilde\lambda\), proving that any single reversal strictly reduces the radius.

## Verification
The proof covers all integers \(m\ge3\) and every possible flipped-arrow position. The exact role of every parameter and all equality cases are established in Steps 1--5.

The accompanying `verify.py` reconstructs all directed incidence vectors and Gram products in exact rational arithmetic for every \(3\le m\le25\) and every reversal position (322 instances). It checks weight normalization, sharp inner-product inequalities, all vertex distances, the reversed-vertex squared-distance deficit, and the fixed-length position law. For \(3\le m\le10\), an independent constrained nonlinear minimax solver tests the claimed minimum-enclosing center and squared radius for 52 instances. These finite experiments corroborate but do not prove the all-integer theorem.

## Relationship to prior work
Numata, Takahashi, and Tamaki develop faces of directed edge polytopes and explicitly prove the arbitrary-orientation type-\(A\) path family forms simplices (their Example 5.2). Their results concern face structure and do not give Euclidean optimal enclosing spheres or a flip-position/contact theorem.

Kálmán and Tóthmérész treat root polytopes of directed graphs and their Ehrhart and dissection geometry. The underlying directed-path realization overlaps, but their work does not give the Euclidean minimum sphere for a single reversed arrow.

An all-vertex circumsphere can be constructed for graded directed paths from a height function, but its existence does not determine the globally smallest ball. The present theorem instead determines the *strictly smaller minimum ball* and complete contact set in the one-reversal family. The consistently oriented type-\(A\) path leads to the different contact geometry computed in Step 5; neither statement implies the other without analyzing the changed signed Gram matrix.

The geometric mechanism is active-set screening: a single orientation defect changes two signs of adjacent Gram entries. The optimum deletes exactly the flipped vertex from its positive barycentric certificate, yet still encloses that vertex with an explicit strictly positive clearance once \(m\ge4\). The resulting radius is a cubic expression in the lengths of the two surviving arrow runs.

## Limitations
The formula is specific to paths with exactly one reversed arrow. Multiple reversals lead to a different active-set problem and are not classified here. The comparison with an all-forward path uses the same canonical Euclidean incidence-vector realization; affine equivalence of the simplices does not preserve these Euclidean radii.

The result treats minimum enclosing balls, not inscribed balls, John ellipsoids, or all lattice invariants. The general convex weighted-certificate lemma is standard; the asserted new content is the explicit all-position closed solution and exact contact deletion for this directed graph family. Equivalent formulas could exist under type-\(A\) root-system, oriented-simplex, or quadratic-optimization terminology beyond the targeted indexed searches.

## References
1. Yasuhide Numata, Yusuke Takahashi, and Dai Tamaki, *Faces of Directed Edge Polytopes*, arXiv:2203.14521v1, first publicly posted 2022-03-28, primary MSC 52B05; see Example 5.2 on arbitrary orientations of Dynkin paths.
2. Tamás Kálmán and Lilla Tóthmérész, *Root polytopes and Jaeger-type dissections for directed graphs*, arXiv:2105.00960v1 (2021); see the directed-root-polytope definitions and dissection setting.
