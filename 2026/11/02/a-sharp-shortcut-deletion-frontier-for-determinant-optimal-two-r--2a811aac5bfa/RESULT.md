# A sharp shortcut-deletion frontier for determinant-optimal two-route networks

## Finding

Consider two distinct terminals connected by three internally vertex-disjoint routes: one route of \(a\ge2\) edges, one of \(b\ge2\) edges, and a direct shortcut edge. The original simple graph has \(n=a+b\) vertices and \(a+b+1\) edges. Each long-route edge is independently assigned a nonnegative conductance and has unit-conductance price \(p>0\) on the first route or \(q>0\) on the second. The shortcut has price \(r>0\). Expenditure is exactly \(B>0\). Optimize the weighted spanning-tree enumerator \(\mathcal T=\det L_{\mathrm{red}}\), equivalently a D-optimal reduced-Laplacian information determinant.

**Theorem (all lengths, prices and budgets).** The global maximizer exists and is unique, even when all individual edge conductances vary independently. The conductances are constant along each long route: \(x_*\) on the \(a\)-edge route, \(y_*\) on the \(b\)-edge route, and \(z_*\) on the shortcut.

Put \(A=a^2p\), \(C=b^2q\) and define
\[
 r_c=\frac{aC+bA-\sqrt{(aC+bA)^2-4(a+b-1)AC}}{2(a+b-1)}
     =\frac{2AC}{aC+bA+\sqrt{(aC+bA)^2-4(a+b-1)AC}}.
\]
The cutoff is the unique root in \(0<r_c<\min\{A,C\}\) of
\[
 G(r)=\frac1r-\frac{a-1}{A-r}-\frac{b-1}{C-r}=0.
\]
When \(0<r<r_c\), the optimal conductances are
\[
 x_*=\frac{Ba(a-1)}{(a+b-1)(A-r)},\qquad
 y_*=\frac{Bb(b-1)}{(a+b-1)(C-r)},\qquad
 z_*=\frac{B}{a+b-1}G(r)>0.
\]
When \(r\ge r_c\), the shortcut is absent, \(z_*=0\). Let \(t>0\) denote the unique positive root of
\[
 (b-1)p\,t^2+(ap-bq)t-(a-1)q=0.
\]
Then the unique optimum is
\[
 y_*=\frac{B}{apt+bq},\qquad x_*=t\,y_*,\qquad z_*=0.
\]
All long-route edges receive positive conductance in both regimes. In particular, the shortcut is deleted **if and only if** \(r\ge r_c\). The exactly maximized determinant in either regime is
\[
 \boxed{\mathcal T_* = x_*^{a-1} y_*^{b-1}(a y_*+b x_*+ab z_*).}
\]

For equal long-route prices \(p=q=s\), the cutoff simplifies to the structural formula
\[
 \boxed{r_c=\frac{ab}{a+b-1}\,s.}
\]
It grows with the two route lengths. There is a sharp continuous transition. Let
\[
 K=\frac1{r_c^2}+\frac{a-1}{(A-r_c)^2}+\frac{b-1}{(C-r_c)^2}>0.
\]
As \(r\uparrow r_c\), holding \(a,b,p,q,B\) fixed,
\[
 z_* =\frac{BK}{a+b-1}(r_c-r)+O((r_c-r)^2),\qquad
 \log\frac{\mathcal T_*(r)}{\mathcal T_*(r_c)}
 =\frac K2(r_c-r)^2+O((r_c-r)^3).
\]
For \(r\ge r_c\), the optimal value is independent of \(r\). Hence it meets the increasing-shortcut regime with quadratic contact.

## Assumptions and scope

All graphs are finite, simple, undirected, and described above; \(a,b\) are integers at least two. Nonnegative conductances are permitted, provided the positive-conductance support is connected. If the support is disconnected, \(\mathcal T=0\), so it cannot maximize against a positive feasible design. Each edge of the two long routes has its own decision variable, even though its price depends only on its route. The rooted Laplacian deletes any one fixed vertex; the determinant is independent of that choice. There is no holding probability, stochastic transition matrix, or resistance-minimization objective hidden in the claim.

## Proof

**1. Tree polynomial without a symmetry assumption.** Let the conductances along the first route be \(u_1,\ldots,u_a\) and those along the second be \(v_1,\ldots,v_b\). Write \(U=\prod_i u_i\), \(V=\prod_j v_j\), and let \(E_{a-1}(u)\) and \(E_{b-1}(v)\) be elementary symmetric polynomials of degrees one below the route lengths. A spanning tree deletes exactly two edges, on different routes. Thus the weighted Matrix–Tree Theorem gives the polynomial identity, valid including at zero weights,
\[
 \mathcal T=z E_{a-1}(u)E_{b-1}(v)
             +E_{a-1}(u)V+U E_{b-1}(v).
\]
The polynomial and the linear price constraint are independently invariant under every permutation of the \(u_i\) and every permutation of the \(v_j\). This algebraic invariance does not assume these permutations are graph automorphisms.

**2. Strict concavity and unrestricted uniqueness.** On the positive-determinant domain, \(\log\mathcal T=\log\det L_{\mathrm{red}}(w)\). The reduced Laplacian is affine in conductances, and its linear map is injective for every simple graph: off-diagonal entries determine each edge away from the deleted root, after which diagonal entries determine root-incident edges. Since \(\log\det\) is strictly concave on positive definite matrices, \(\log\mathcal T\) is strictly concave in the complete edge vector. A positive optimum exists on the compact nonnegative budget simplex because a fully positive feasible vector has \(\mathcal T>0\). Every permutation within either route preserves the objective and the constraint, so uniqueness forces equality of all optimal conductances within each route. Internal route conductances cannot be zero, because each has an internal vertex which would be disconnected if all its route edges were zero. Denote the common positive values by \(x,y\) and shortcut conductance by \(z\ge0\).

**3. Reduced determinant and first-order conditions.** The polynomial becomes
\[
 \mathcal T=x^{a-1}y^{b-1}(a y+b x+abz),\qquad apx+bqy+rz=B.
\]
Put \(H=a y+b x+abz\). In a positive-shortcut optimum, stationarity gives
\[
 \frac{a-1}{x}+\frac bH=\lambda ap,\quad
 \frac{b-1}{y}+\frac aH=\lambda bq,\quad
 \frac{ab}{H}=\lambda r.
\]
Euler homogeneity, since every spanning tree has \(a+b-1\) edges, gives \(\lambda=(a+b-1)/B\). Solving gives exactly the displayed interior formulas. Here \(z>0\) is equivalent to \(G(r)>0\), and denominators are positive for \(r<r_c\). Since \(G\) strictly decreases from \(+\infty\) to \(-\infty\) on \((0,\min\{A,C\})\), it has a unique zero there. Multiplication by \(r(A-r)(C-r)\) yields
\[
 (a+b-1)r^2-(aC+bA)r+AC=0,
\]
whose smaller root is the displayed \(r_c\). Strict concavity makes the feasible stationary interior solution globally optimal.

**4. Shortcut-free regime and the boundary.** If \(z=0\), write \(t=x/y>0\). Budget gives \(y=B/(apt+bq)\), and the determinant is proportional to \(t^{a-1}(a+bt)/(apt+bq)^{a+b-1}\). Its logarithmic derivative vanishes precisely at
\[
 (b-1)pt^2+(ap-bq)t-(a-1)q=0.
\]
The quadratic has exactly one positive root; strict concavity makes it the unique shortcut-free optimum. At \(r=r_c\), the interior formulas yield \(z=0\), solve the two shortcut-free stationarity equations, and make the shortcut's nonnegativity KKT inequality an equality. For larger \(r\), the same shortcut-free conductances still satisfy all long-route stationarity equations; the shortcut directional derivative \(ab/H-\lambda r\) is then strictly negative. Consequently, the shortcut-free design satisfies the global KKT conditions for all \(r\ge r_c\). The explicit formulas and complete support classification follow.

**5. Equal-price rule and transition order.** Substituting \(p=q=s\) into the threshold quadratic gives its smaller root \(ab s/(a+b-1)\). In the interior regime \(z_*=B G(r)/(a+b-1)\). Since \(G'(r_c)=-K\), Taylor's theorem yields the stated linear vanishing. Finally, the constrained envelope identity is
\[
 \frac{d}{dr}\log \mathcal T_*(r)=-\lambda z_*(r)=-G(r)
\]
for \(0<r<r_c\), while above the cutoff the value is constant. Integrating from \(r\) to \(r_c\) and expanding \(G\) gives the quadratic contact formula.

## Verification

Run the accompanying standalone \(\texttt{verify.py}\) with Python 3, NumPy, SciPy and SymPy. It constructs actual reduced Laplacians without using the tree-polynomial formula for its determinant computations, compares against the polynomial independently, checks budget feasibility and the cutoff, and tests against asymmetric feasible conductance vectors and numerical constrained optima.

The executed checker reported six exact symbolic/rational examples, 80 reduced-Laplacian determinant comparisons, 80 threshold/budget checks, 1,200 unrestricted asymmetric feasible comparisons, and 27 unconstrained-individual-edge numerical solver comparisons. These finite tests are supporting checks, not a proof of the all-length statement. The proof above supplies that statement.

**Exact example.** For \(a=2,b=3,p=q=B=1\), the shortcut threshold is \(r_c=3/2\). At shortcut price \(r=1\), the unique allocation is \(x_*=1/6\), \(y_*=3/16\), \(z_*=5/48\) and \(\mathcal T_*=9/1024\). At any \(r\ge3/2\), it becomes \(x_*=y_*=1/5\), \(z_*=0\), and \(\mathcal T_*=1/125\).

## Relationship to prior work

The weighted Matrix–Tree Theorem, log-determinant concavity, and the Karush–Kuhn–Tucker criterion are classical. Khosoussi and coauthors (first public preprint April 5, 2016) study weighted spanning-tree maximization under edge-selection and convex-relaxation constraints, including general D-optimal network motivations. Their model and techniques do not directly state the continuous linear-price, unrestricted individual-conductance solution for overlapping cycles. Existing cactus decompositions rely on edge-disjoint cycles; they do not determine the shortcut-deletion threshold on a theta graph with shared-cycle edges. The formulas here solve that specific finite-dimensional structured design problem explicitly and establish uniqueness and its near-threshold behavior. Priority beyond the inspected material remains subject to possible specialized prior work.

## Limitations

The prices are homogeneous *within* each of the two long routes. Arbitrary position-dependent prices are not classified. The shortest route is exactly one edge, and the other two have length at least two; the theorem does not classify general three-long-route theta networks or arbitrary bicyclic graphs. The result optimizes a spanning-tree information determinant, not the sum of effective resistances or a spectral gap. Numerical verification covers finite cases only. The finding has not undergone independent mathematical audit, and publication-priority searches are not exhaustive.

## References

1. K. Khosoussi, G. S. Sukhatme, S. Huang, and G. Dissanayake, *Maximizing the Weighted Number of Spanning Trees: Near-\(t\)-Optimal Graphs*, first posted April 5, 2016, arXiv:1604.01116, https://arxiv.org/abs/1604.01116. See the weighted Matrix–Tree setup and convex edge-selection sections.
2. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37–66, https://doi.org/10.1137/050645452. This is a related network-conductance convex design framework, but with a different objective.
3. Weighted Matrix–Tree Theorem and strict concavity of \(\log\det\) on positive definite matrices (classical background, with the weighted theorem restated in Reference 1).
