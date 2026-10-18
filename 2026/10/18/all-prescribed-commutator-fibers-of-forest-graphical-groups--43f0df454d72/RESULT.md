# All prescribed commutator fibers of forest graphical groups

## Finding
Let \(T=(V,E)\) be any finite simple forest (possibly disconnected, including isolated vertices), and let \(q\) be a prime power. Put \(n=|V|\), \(m=|E|\). The graphical group \(G_T(\mathbb F_q)\) is defined explicitly below. For a central edge-coordinate target \(w=(w_e)\), define \(E_+(w)=\{e\in E:w_e\ne0\}\), \(r=|E_+(w)|\), and \(V_+(w)=\bigcup_{e\in E_+(w)}e\). For any vertex set \(U\subseteq V\), write \(c(U)\) for the number of connected components in \(T[U]\), counting isolated vertices and taking \(c(\varnothing)=0\).

**Theorem (complete prescribed-target fibers).** The number of ordered pairs \((g,h)\in G_T(\mathbb F_q)^2\) satisfying \([g,h]=(0,w)\) is exactly
\[
\boxed{\mathcal N_T(w)=q^{2m+r}\sum_{Z\subseteq V\setminus V_+(w)}(q+1)^{c(V\setminus Z)}(q-1)^{|V\setminus Z|-r}.}
\]
Every target in the derived subgroup is a single commutator. Targets outside that subgroup are not commutators. The count depends only on which edge coordinates of \(w\) are nonzero, not on their actual values. A two-state leaf-to-root recurrence computes each complete fiber using linearly many additions and multiplications in the vertex count. All statements hold in characteristic two and over nonprime finite fields.

For the first nonstar path on four vertices, over \(\mathbb F_2\), the **Lie bracket** fibers in edge order along the path are \(76,36,24,24,36,12,24,24\) for targets \((0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1)\), respectively. Their sum is \(256\). The corresponding group commutator fibers are each multiplied by \(2^6=64\). Thus all nonzero targets are attained but their fiber sizes are not constant.

## Assumptions and scope
Order the vertices arbitrarily. Write elements as \((x,z)\in\mathbb F_q^V\times\mathbb F_q^E\), and define
\[
(x,z)(y,t)=\left(x+y,\ z+t+\bigl(x_i y_j\bigr)_{\{i,j\}\in E,\ i<j}\right).
\]
The bilinear cocycle makes this a group of nilpotency class at most two and order \(q^{n+m}\). Using the convention \([g,h]=g^{-1}h^{-1}gh\), direct multiplication gives
\[
[(x,z),(y,t)]=\left(0,\bigl(x_i y_j-x_j y_i\bigr)_{\{i,j\}\in E,\ i<j}\right).
\]
All edge coordinates generate the derived subgroup when \(E\ne\varnothing\): for any edge, the corresponding two vertex basis vectors give its unit bracket. Therefore the derived subgroup is precisely \(\{0\}\times\mathbb F_q^E\); it is trivial for an edgeless forest. An associated graph Lie algebra has this same displayed bracket on its vertex space, with an independent central edge space. Bracket fibers on pairs of vertex vectors differ from group fibers by the factor \(q^{2m}\), which counts the freely chosen central coordinates of each input.

## Proof
Associate to every ordered pair of vertex vectors \((x,y)\) the vertex labels \(a_i=(x_i,y_i)\in\mathbb F_q^2\). The bracket constraint on an edge \(\{i,j\}\), \(i<j\), is \(\det(a_i,a_j)=w_{ij}\). In particular, endpoints of an edge with nonzero target must have nonzero labels. Fix the set of zero-labeled vertices \(Z\); its admissibility is exactly \(Z\subseteq V\setminus V_+(w)\). Put \(U=V\setminus Z\). Every vertex of \(U\) has a nonzero label, hence a projective direction in \(\mathbb P^1(\mathbb F_q)\), which has \(q+1\) points.

On a surviving edge with zero target, the two projective directions must agree. On a surviving edge with nonzero target, the directions must differ. Since \(T[U]\) is a forest, contracting all zero-target edges produces another forest, with \(c(U)\) components and exactly \(r\) positive-target edges. On each component choose the first projective direction in \(q+1\) ways. Across every positive-target edge there are exactly \(q\) choices for a direction distinct from its parent direction. Thus there are precisely \((q+1)^{c(U)}q^r\) allowed systems of projective directions.

Choose a nonzero representative of each projective direction and write \(a_i=\lambda_i\widehat a_i\), where \(\lambda_i\in\mathbb F_q^\times\). Every positive-target edge imposes one nonzero equation \(\lambda_i\lambda_j\det(\widehat a_i,\widehat a_j)=w_{ij}\). These \(r\) independent constraints lie on a forest, so choose one free nonzero scalar on each component of the positive-target-edge graph and propagate the others uniquely. They leave precisely \((q-1)^{|U|-r}\) scalar assignments. Edges whose target is zero impose no additional scalar condition. Therefore the number of vertex-vector pairs with this zero set is \((q+1)^{c(U)}q^r(q-1)^{|U|-r}\). Sum over admissible \(Z\) and multiply by \(q^{2m}\) unrestricted input-center choices. This proves the boxed expression.

The choice \(Z=\varnothing\) contributes strictly positively, since \(q\ge2\), so every central target is attained. Noncentral elements cannot be commutators by the displayed formula. This proves single-commutator surjectivity and the stated width, including the trivial-derived-group boundary case.

**Linear-time recurrence.** Root each component of \(T\). At a leaf set \(A_v=B_v=1\), where \(A_v\) counts satisfying assignments in its descendant subtree conditional on the vertex vector being zero, and \(B_v\) counts those conditional on one prescribed nonzero vertex vector. For each child \(u\) of \(v\), put
\[
\begin{array}{c|cc}
&\text{factor for }A_v&\text{factor for }B_v\\\hline
w_{vu}=0&A_u+(q^2-1)B_u&A_u+(q-1)B_u\\
w_{vu}\ne0&0&qB_u.
\end{array}
\]
Then \(A_v\) (respectively \(B_v\)) is the product of its corresponding child factors. At a root \(s\), the component count is \(A_s+(q^2-1)B_s\). Multiply these counts over root components and multiply by \(q^{2m}\). The factors follow from elementary determinant equations: with a zero parent, every child vector is allowed exactly when its edge target vanishes; with a fixed nonzero parent, a zero determinant has \(q\) child solutions, and each prescribed nonzero determinant also has \(q\) solutions. The recurrence has one constant-size update per vertex/edge, giving \(O(n)\) arithmetic operations (without asserting bit complexity independent of coefficient size).

## Verification
The standalone Python 3 checker `check_forest_commutators.py` computes independent direct commutator counts by enumeration of all ordered pairs of vertex vectors and compares every fiber with the boxed zero-set formula. It checks all labeled forests of orders one through four over \(\mathbb F_2\) and \(\mathbb F_3\), additional paths and stars over \(\mathbb F_4\), a path over \(\mathbb F_5\), and two forests of order five over \(\mathbb F_2\): \(101\) entire graph-field configurations. The \(\mathbb F_4\) implementation uses polynomial arithmetic modulo \(X^2+X+1\). Its success marker is `ALL_FOREST_FIBER_CHECKS_PASSED 101`. Exhaustive checking of finitely many small examples is not an infinite-family proof; the preceding argument proves the general statement.

## Relationship to prior work
Rossmann's *Enumerating conjugacy classes of graphical groups over finite fields* (arXiv:2107.05564) develops these graphical groups and studies their conjugacy and character-enumeration invariants, including general rank formulae for commuting pairs. Those results already encompass aggregate zero-target information, but the material inspected does not give a uniform explicit **all-central-target** forest formula or this specialized linear-time evaluation. Levy's *Enumerating fibres of commutator words over p-groups* (arXiv:1602.04093), Theorem 2.1, provides a general representation-theoretic expression for commutator fibers of finite class-two groups under its hypotheses; this is broader abstract coverage and can in principle evaluate individual odd-characteristic instances, but its inspected statement does not supply the present forest support-only count and recurrence. Naik's arXiv:1805.00091 addresses possible numbers of distinct nontrivial commutator-fiber sizes for other group families. Cocke and Ho's arXiv:1807.07111 investigates general structural questions about word-map distributions. The distinct contribution claimed here is the explicit **complete prescribed nonzero-target distribution** on arbitrary forests, including nonstars and all finite-field characteristics; not general graphical-group theory, the zero-target aggregate, or known formulas for complete bipartite cases.

## Limitations
The formula is restricted to forests. Cycles may introduce global direction and scalar compatibility constraints and are not covered. All fibers are for one commutator, not products of several commutators. The exact formula does not establish historical uniqueness against every unindexed work; equivalent all-target forest formulas in older class-two-group or graph-matrix literature remain a priority risk. The group presentation and proof apply to any finite field, but the attached exhaustive computations are small-field corroboration only. No independent mathematical audit has been performed.

## References
1. T. Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, arXiv:2107.05564 (2021), https://arxiv.org/abs/2107.05564; DOI: 10.1112/blms.12665.
2. M. Levy, *Enumerating fibres of commutator words over p-groups*, arXiv:1602.04093 (2016), https://arxiv.org/abs/1602.04093.
3. T. K. Naik, *On the probability distribution associated to commutator word map in finite groups II*, arXiv:1805.00091 (2018), https://arxiv.org/abs/1805.00091.
4. W. Cocke and M.-C. Ho, *The Probability Distribution of Word Maps on Finite Groups*, arXiv:1807.07111 (2018), https://arxiv.org/abs/1807.07111.
