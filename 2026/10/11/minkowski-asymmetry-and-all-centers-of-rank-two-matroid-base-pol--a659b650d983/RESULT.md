# Minkowski asymmetry and all centers of rank-two matroid base polytopes

## Finding
Let \(M\) be a finite loopless rank-two matroid on a ground set \(E\). Its parallel classes \(C_1,\ldots,C_p\) form a partition with \(p\ge2\); put \(m_j=|C_j|\) and \(n=|E|\). Let \(P(M)\) be the convex hull of the indicator vectors of its bases. Define Minkowski asymmetry, intrinsically in the affine hull, by
\[
s(P)=\min_{c\in P}\inf\{s\ge1:-(P-c)\subseteq s(P-c)\}.
\]
If \(p\ge3\), then
\[
\boxed{s(P(M))=r=\max\left\{\max_jm_j,\frac{n-2}{2},\frac{2}{p-2}\right\}.}
\]
All minimizing centers are precisely
\[
\boxed{\mathcal M(P(M))=\left\{c:\sum_{e\in E}c_e=2,\quad (r+1)c_e\ge1\ (e\in E),\quad (r+1)c(C_j)\le r\ (1\le j\le p)\right\}.}
\]
Write \(q_j=r-m_j\), \(Z=2(r+1)-n\), \(U=pr-n=\sum_jq_j\), and \(H=\{j:q_j>0\}\). Then \(0\le Z\le U\), and the entire minimizing-center space has affine dimension
\[
\boxed{
\dim\operatorname{aff}\mathcal M(P(M))=
\begin{cases}
0,&Z=0,\\
\sum_{j\in H}(m_j-1),&Z=U>0,\\
\sum_{j\in H}m_j-1,&0<Z<U.
\end{cases}}
\]
Equivalently, its exact center polytope is given by \(c_e=(1+z_e)/(r+1)\), where \(z_e\ge0\), \(z(C_j)\le q_j\), and \(z(E)=Z\).

If \(p=2\), the matroid is the direct sum of two rank-one uniform matroids. In this case
\[
\boxed{s(P(M))=r=\max\{1,m_1-1,m_2-1\}.}
\]
Its complete center locus is \(c_e=(1+z_e)/(r+1)\), subject to \(z_e\ge0\) and \(z(C_j)=r+1-m_j\) for \(j=1,2\). Its affine dimension is
\[
\boxed{\sum_{j:\,m_j<r+1}(m_j-1).}
\]
This includes the point case \(m_1=m_2=1\), for which asymmetry is \(1\) by the stated convention.

## Assumptions and scope
Every matroid is finite and loopless, and has rank exactly two; no representability, simplicity, or connectedness assumption is imposed. A basis consists of two elements from distinct parallel classes. The ambient affine equation is \(x(E)=2\). All assertions are exact and apply to arbitrary positive integral class sizes. The classification is of ordinary Minkowski asymmetry, not Euclidean eccentricity or a John/Löwner ellipsoid.

## Proof
**Polytope description.** The exact halfspace representation is
\[
P(M)=\{x\in\mathbb R^E:x_e\ge0\ (e\in E),\ x(C_j)\le1\ (1\le j\le p),\ x(E)=2\}.
\]
Indeed, if \(a_j=x(C_j)\), then \(0\le a_j\le1\) and \(\sum_ja_j=2\), so \(a\) is a convex combination of indicator vectors of two-element subsets of \([p]\). Given a selected pair of classes, choose independently an element of each according to the normalized within-class coordinates of \(x\). Averaging the resulting basis indicators reproduces \(x\). Classes with zero total mass can be assigned arbitrary conditional distributions. Hence the displayed inequalities describe precisely the convex hull of bases.

**Exact containment criterion.** For any \(s\ge1\) and \(c\in P(M)\), the inclusion \(-(P(M)-c)\subseteq s(P(M)-c)\) is equivalent to
\[
(s+1)c-x\in sP(M)\quad\text{for every }x\in P(M).
\]
When \(p\ge3\), for every element \(e\) the maximum of \(x_e\) over \(P(M)\) is \(1\); for each parallel class \(C_j\), the minimum of \(x(C_j)\) is \(0\), because a basis can be chosen from two other classes. Applying the displayed polytope description to all transformed points therefore yields, necessarily and sufficiently,
\[
(s+1)c_e\ge1,\qquad(s+1)c(C_j)\le s,\qquad c(E)=2.
\]
These conditions already imply \(c\in P(M)\), so no additional feasibility condition is needed.

**Optimization.** Put \(w_e=(s+1)c_e\). For \(p\ge3\) the criterion asks for \(w_e\ge1\), \(w(C_j)\le s\), \(w(E)=2(s+1)\). The feasible total within class \(j\) is exactly the interval \([m_j,s]\). Such intervals admit a collective total \(2(s+1)\) if and only if
\[
m_j\le s\quad(1\le j\le p),\qquad n\le2(s+1)\le ps.
\]
Solving these inequalities subject to \(s\ge1\) gives the stated maximum. Replacing \(w\) by \(1+z\) gives the complete center polytope.

**Dimension.** If \(Z=0\), every nonnegative \(z_e\) vanishes. If \(0<Z<U\), only classes in \(H\) can vary. The point assigning to each element of class \(j\in H\) the positive value \(Zq_j/(Um_j)\) is strict in every varying coordinate and every positive class cap. Thus the only affine constraint on the \(\sum_{j\in H}m_j\) variable coordinates is their total sum, giving one less dimension. If \(Z=U>0\), all positive class caps are tight; each such class supports a full simplex of dimension \(m_j-1\), and distinct class factors vary independently. This proves all dimension branches.

**Two classes.** If \(p=2\), the class-sum constraints and \(x(E)=2\) force \(x(C_1)=x(C_2)=1\); hence \(P(M)\) is the product of two simplices. The transformed containment criterion reduces to \((s+1)c_e\ge1\) and \((s+1)c(C_j)=s+1\). Feasibility is equivalent to \(s+1\ge m_j\) for both classes, together with \(s\ge1\). Translation by \(1\) in every coordinate gives the stated product of scaled simplices, and any factor has dimension \(m_j-1\) precisely when \(r+1>m_j\).

## Verification
The included `verify.py` uses only Python's standard library and exact rational arithmetic. It exhaustively checks every ordered positive parallel-class size profile with total size from \(2\) through \(11\). For each profile it constructs all basis vertices, forms a center using the explicit feasible allocation, and checks that every reflected vertex remains in the polytope. It also checks the elementary lower-bound obstructions and dimension-case consistency. The verification prints 2036 profiles and 77808 transformed-vertex checks passing. An independent linear-programming comparison, using the full matroid rank inequalities rather than only the class representation, matched the formula on 247 ordered profiles through size \(8\). These are finite checks; the universal assertions follow from the proof above.

For example, \(U_{2,4}\) has asymmetry \(1\) and a unique center, whereas a connected rank-two matroid with parallel class sizes \((3,1,1)\) has asymmetry \(3\) and a one-dimensional segment of optimal centers. The nonconnected product with class sizes \((5,2)\) has asymmetry \(4\) and a one-dimensional center locus.

## Relationship to prior work
Ferroni, Jochemko, and Schröter provide the parallel-class hyperplane description of rank-two matroid base polytopes and determine their Ehrhart properties, not Minkowski asymmetry. Pineda-Villavicencio and Schröter study reconstruction from the basis-exchange graph, a distinct invariant. Den Hertog, Pauphilet, and Soali give a general robust linear-optimization formulation for Minkowski centers of arbitrary polyhedra; that formulation can computationally recover individual instances but does not state the three-obstruction formula, two-class exception, or full rank-two center-dimension classification here. The present proof is self-contained except for familiar matroid terminology.

## Limitations
The formula applies to loopless rank-two matroid base polytopes, not arbitrary-rank matroids. It determines intrinsic affine Minkowski asymmetry, not a Euclidean radius or volume. The finite verifier does not certify all matroids or establish bibliographic priority. Although the most pertinent inspected sources do not state the classification, an equivalent earlier specialization under alternate terminology cannot be excluded.

## References
1. L. Ferroni, K. Jochemko, B. Schröter, *Ehrhart polynomials of rank two matroids*, arXiv:2106.08183 (first posted 2021-06-15), §2.2 and Lemmas 2.6–2.7; https://arxiv.org/abs/2106.08183 .
2. G. Pineda-Villavicencio, B. Schröter, *Reconstructibility of matroid polytopes*, arXiv:2010.10227 (first posted 2020-10-20); https://arxiv.org/abs/2010.10227 .
3. D. den Hertog, J. Pauphilet, M. Y. Soali, *Minkowski Centers via Robust Optimization: Computation and Applications*, *Operations Research* 72 (2024), 2135–2152; preprint https://optimization-online.org/2022/01/8768/ , especially Proposition 4.
4. K. Jochemko, M. Ravichandran, *Generalized permutahedra: Minkowski linear functionals and Ehrhart positivity*, *Mathematika* 68 (2022), 217–236; https://doi.org/10.1112/mtk.12122 .
