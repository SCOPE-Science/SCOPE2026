# Widom–Rowlinson partition functions as 1-type polynomials of the generic diameter-3 metric space

## Finding

Let \(\mathbb U_3\) be the Fraïssé limit of the class of all finite metric spaces whose nonzero distances lie in \(\{1,2,3\}\). Equivalently, this is the unrestricted generic integer metric structure of diameter three. For a finite parameter set \(A\subseteq\mathbb U_3\), a nonalgebraic one-point extension is described by a Katětov function
\[
f:A\longrightarrow\{1,2,3\}
\]
satisfying, for every \(a,b\in A\),
\[
|f(a)-f(b)|\le d(a,b)\le f(a)+f(b).
\]
For distances in \(\{1,2,3\}\), these constraints have the particularly simple form
\[
\begin{array}{c|c}
d(a,b)&\text{forbidden values of }(f(a),f(b))\\ \hline
1&\{1,3\}\text{ in either order}\\
2&\text{none}\\
3&(1,1).
\end{array}
\]

Now let \(G=(V,E)\) be any finite simple graph and form the metric parameter subspace \(A_G\) on \(V\) by
\[
d_G(u,v)=\begin{cases}1,&uv\in E,\\2,&uv\notin E,\end{cases}\qquad u\ne v.
\]
This is always a metric, because every nonzero distance is either \(1\) or \(2\). Define the weighted nonalgebraic 1-type polynomial
\[
\Theta_{A_G}(x,y,z)
 =\sum_{p\in S_1(A_G)\setminus S_1^{\rm alg}(A_G)}
 x^{n_1(p)}y^{n_2(p)}z^{n_3(p)},
\]
where \(n_i(p)\) is the number of parameters at distance \(i\) from a realization of \(p\). Then
\[
\boxed{
\Theta_{A_G}(x,y,z)
 =\sum_{Z\subseteq V} y^{|Z|}
   \prod_{C\in\pi_0(G-Z)}\bigl(x^{|C|}+z^{|C|}\bigr).
}
\]
Here \(\pi_0(G-Z)\) denotes the connected components of the induced graph on \(V\setminus Z\).

At unit weights this becomes
\[
\boxed{
N(A_G):=|S_1(A_G)\setminus S_1^{\rm alg}(A_G)|
 =\sum_{Z\subseteq V}2^{c(G-Z)}
 =\operatorname{hom}(G,P_3^{\circ}),
}
\]
where \(P_3^{\circ}\) is the three-vertex path with a loop at every vertex. This is exactly the two-particle Widom–Rowlinson partition function: the middle state is vacancy and the two endpoint states are the two particle species, which may not occupy adjacent vertices simultaneously. Consequently
\[
|S_1(A_G)|=|V|+\operatorname{hom}(G,P_3^{\circ}).
\]

The bridge immediately imports an exact complexity classification. Dyer and Greenhill proved that the Widom–Rowlinson partition function is #P-complete, and that hardness persists for graphs of maximum degree three. Therefore exact finite-parameter nonalgebraic 1-type counting for \(\mathbb U_3\) is #P-complete under polynomial-time reductions already on parameter spaces using only distances \(1\) and \(2\), even when the distance-1 graph has maximum degree three. The total 1-type count is equally hard, since it differs by the explicitly known additive term \(|A|\).

There is also a sharp extremal envelope on this graph-metric slice. For every \(n\)-vertex \(G\),
\[
\boxed{2^{n+1}-1\le N(A_G)\le 3^n.}
\]
For \(n\ge2\), equality on the left occurs exactly for \(G=K_n\), and equality on the right exactly for the edgeless graph. Thus among \(n\)-point \(\{1,2\}\)-metric parameter spaces, the all-distance-1 space uniquely minimizes the number of nonalgebraic 1-types and the all-distance-2 space uniquely maximizes it.

## Proof

For a one-point extension \(x\) of a finite metric space \(A\), putting \(f(a)=d(x,a)\), the triangle inequalities for the triangle \(x,a,b\) are exactly
\[
|f(a)-f(b)|\le d(a,b)\le f(a)+f(b).
\]
When all values lie in \(\{1,2,3\}\), inspect the three possible values of \(d(a,b)\). If \(d=1\), the right inequality is automatic and the left fails only for the pair \(1,3\). If \(d=2\), both inequalities are automatic. If \(d=3\), the left inequality is automatic and the right fails only for \((1,1)\). This proves the local table.

On \(A_G\) there are no distance-3 parameter pairs. Hence a map \(f:V\to\{1,2,3\}\) is admissible exactly when no graph edge has endpoint values \(1\) and \(3\). Equivalently, \(f\) is a homomorphism to the fully looped path \(P_3^{\circ}\). Because \(\mathbb U_3\) is universal and ultrahomogeneous, each admissible one-point extension is realized and determines exactly one nonalgebraic complete 1-type over \(A_G\).

To derive the polynomial, fix the set
\[
Z=f^{-1}(2).
\]
On \(G-Z\), only states \(1\) and \(3\) remain. Since an edge may not join the two different states, every connected component of \(G-Z\) must be monochromatic. A component \(C\) therefore contributes either \(x^{|C|}\) or \(z^{|C|}\), independently of the other components, while the vacancy set contributes \(y^{|Z|}\). Summing over \(Z\subseteq V\) gives the displayed factorization. Setting \(x=y=z=1\) gives \(\sum_Z2^{c(G-Z)}\).

For the upper extremum, deleting all edges removes constraints, so the edgeless graph has all \(3^n\) assignments. If \(G\) contains an edge \(uv\), the assignment \(f(u)=1,f(v)=3\), with all other values \(2\), is excluded, so the inequality is strict. For the lower extremum, adding edges only removes assignments. In \(K_n\), an admissible assignment cannot use both species \(1\) and \(3\), so the count is
\[
2^n+2^n-1=2^{n+1}-1,
\]
where the all-2 assignment is subtracted once. If \(G\ne K_n\), choose a nonedge \(uv\); assigning \(u\mapsto1\), \(v\mapsto3\), and every other vertex to \(2\) is valid for \(G\) but not for \(K_n\), giving strict inequality.

For complexity, the map \(G\mapsto A_G\) is polynomial-time. The above bijection gives
\[
N(A_G)=\operatorname{hom}(G,P_3^{\circ}).
\]
Dyer and Greenhill's fixed-target homomorphism dichotomy places this target on the #P-complete side, and their bounded-degree result explicitly includes the Widom–Rowlinson model at maximum degree three. Membership in #P is immediate by nondeterministically guessing the distance vector \(f\) and checking the triangle inequalities in polynomial time.

## Relationship to prior work

Amato, Cherlin, and Macpherson classify the countable metrically homogeneous graphs of diameter three. Their paper's manuscript is dated November 2019, its accepted version was deposited publicly on 2020-02-19, and the manuscript lists Primary MSC 03C10. The unrestricted \(\{1,2,3\}\)-metric Fraïssé class is the generic diameter-three case with no additional forbidden triangles. This supplies the eligible foundations anchor, but the paper does not enumerate finite-parameter 1-types or connect them to a statistical-mechanics partition function.

Dyer and Greenhill treat the graph-homomorphism formulation of the Widom–Rowlinson model and prove the relevant #P-completeness, including maximum degree three. That complexity theorem is prior and is imported rather than reproved. Their 2004 corrigendum closes a gap in one proof in the original paper; the published dichotomy and the Widom–Rowlinson hardness statement remain the prior complexity input used here.

The retained contribution is the exact model-theoretic identification of the finite-parameter 1-type polynomial with the weighted Widom–Rowlinson partition function on the \(\{1,2\}\)-metric slice, the connected-component factorization, and the sharp complete/edgeless extremal envelope. Targeted published-finding corpus and web searches for Katětov functions, Urysohn/generic diameter-three metrics, finite-parameter 1-types, and Widom–Rowlinson formulations did not locate this bridge. The current ledger's closest related item is the Henson-graph 1-type/#P result, which instead identifies admissible neighborhoods with clique-free subsets and the independence polynomial; it does not imply the present metric/Katětov/Widom–Rowlinson formula.

## Verification

The bundled `artifacts/verify.py` directly enumerates all three-valued distance vectors over every labeled graph-metric through five vertices and checks the Katětov inequalities pair by pair. It independently evaluates the connected-component formula and compares the full multivariate coefficient dictionaries. At six vertices it checks all \(2^{15}=32768\) labeled graphs at scalar level. It also verifies the unique complete/edgeless extrema and the path specialization
\[
1,3,7,17,41,99,239,577,1393
\]
through eight vertices. The verifier terminates with `VERIFY_OK`.

This is same-model verification. No independent audit has been performed.
