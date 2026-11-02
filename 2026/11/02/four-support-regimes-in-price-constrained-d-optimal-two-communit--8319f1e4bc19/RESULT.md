# Four support regimes in price-constrained D-optimal two-community complete networks

## Finding

Fix integers \(p,q\ge 2\), write \(N=p+q\), and partition the vertices of the complete graph \(K_N\) into two prescribed groups of sizes \(p\) and \(q\). Every individual nonnegative edge conductance may be chosen freely. Within the first group an edge costs \(P>0\) per conductance unit; within the second group it costs \(Q>0\); every cross-group edge costs one. The total expenditure is exactly \(B>0\). Maximize the weighted spanning-tree enumerator \(\mathcal T\), equivalently the determinant of any reduced weighted Laplacian.

There is a **unique** global maximizer, and it is constant on each of the three edge classes. Let \(a,b,c\) denote its respective within-first-group, within-second-group, and cross-group conductances; let \(\Lambda=(N-1)/B\). The following four cases form a disjoint and exhaustive classification, including all equalities on their stated boundaries.

**All three classes retained.** If
\[
qP+(q-1)Q<2q,\qquad (p-1)P+pQ<2p,
\]
put
\[
D=pq-\frac{q(p-1)P+p(q-1)Q}{2}.
\]
Then \(D>0\), and
\[
c=\frac{1}{\Lambda D},\qquad
 a=\frac{1}{p}\left(\frac{2}{\Lambda P}-qc\right)>0,\qquad
 b=\frac{1}{q}\left(\frac{2}{\Lambda Q}-pc\right)>0.
\]

**Only first-group internal edges removed.** If
\[
Q<\frac{2q}{N-1},\qquad P\ge 2-\frac{q-1}{q}Q,
\]
put \(E=q-(q-1)Q/2\). Then
\[
a=0,\qquad c=\frac{1}{\Lambda E},\qquad
b=\frac{1}{q}\left(\frac{2}{\Lambda Q}-pc\right)>0.
\]

**Only second-group internal edges removed.** If
\[
P<\frac{2p}{N-1},\qquad Q\ge 2-\frac{p-1}{p}P,
\]
put \(F=p-(p-1)P/2\). Then
\[
b=0,\qquad c=\frac{1}{\Lambda F},\qquad
 a=\frac{1}{p}\left(\frac{2}{\Lambda P}-qc\right)>0.
\]

**Both internal edge classes removed.** If
\[
P\ge\frac{2p}{N-1},\qquad Q\ge\frac{2q}{N-1},
\]
then
\[
a=b=0,\qquad c=\frac{B}{pq}.
\]
The optimal support is precisely \(K_{p,q}\). No cross-group edge is ever removed.

In every case the exact optimal objective is
\[
\boxed{\mathcal T_{\max}=c\,(pa+qc)^{p-1}(qb+pc)^{q-1}.}
\]

**Two-stage equal-price collapse.** If \(p<q\) and \(P=Q=t>0\), the internal edges of the smaller group vanish first, at \(t_1=2q/(2q-1)\), and the remaining internal edges vanish later, at \(t_2=2q/(p+q-1)>t_1\). For \(t<t_1\) both internal classes survive; for \(t_1\le t<t_2\) only the larger group's internal edges survive; for \(t\ge t_2\) the optimum is complete bipartite. If \(p=q\), both internal classes vanish simultaneously at \(t=2p/(2p-1)\). For \(p>q\), interchange group names.

## Assumptions and scope

All conductance variables are independently nonnegative; no upper bounds, degree constraints, or preselected sparsity are imposed. Prices are strictly positive and constant within each of the three designated classes. The graph has at least two vertices in each group, and all cross-group edges are available. All objective values refer to weighted spanning-tree sums, not to sums of electrical resistances or ordinary minimum-cost spanning trees. The budget is exhausted at every maximum because \(\mathcal T\) is strictly increasing in each conductance on a connected graph.

## Proof

Write \(L_g(w)\) for a reduced weighted Laplacian. By the weighted Matrix–Tree theorem, \(\mathcal T(w)=\det L_g(w)\). The feasible set \(\sum_e \rho_e w_e=B\) is compact. A strictly positive feasible allocation gives \(\det L_g>0\), whereas a disconnected allocation gives zero, so a connected maximizer exists.

**Global uniqueness, without imposing class symmetry.** On the cone of connected allocations, \(\log\det L_g\) is strictly concave in all individual edge weights. Indeed, the map \(w\mapsto L_g(w)\) is injective for a simple complete graph: its off-diagonal entries identify all non-ground-edge weights, and its diagonal entries then identify each ground-edge weight. For any nonzero weight perturbation \(v\), its Hessian quadratic form is
\[
-\operatorname{tr}\bigl[(L_g^{-1/2}\,\delta L_g(v)\,L_g^{-1/2})^2\bigr]<0.
\]
Thus two different connected allocations cannot both maximize the determinant. Permuting vertices within either group preserves prices and the objective, so uniqueness forces the unrestricted maximizer to give one conductance \(a\) to every first-group internal edge, \(b\) to every second-group internal edge, and \(c\) to every cross-group edge. Connectivity requires \(c>0\), since \(c=0\) disconnects the prescribed groups.

**Exact spectral reduction.** The Laplacian acts by the scalar \(U=pa+qc\) on the \((p-1)\)-dimensional first-group contrast subspace and by \(V=qb+pc\) on the \((q-1)\)-dimensional second-group contrast subspace. Its remaining nonzero eigenvalue is \(Nc\). Matrix–Tree therefore gives
\[
\mathcal T=cU^{p-1}V^{q-1},\qquad
B=\binom p2 Pa+\binom q2 Qb+pqc.
\]
The objective is homogeneous of degree \(N-1\). At a maximum the budget multiplier is \(\Lambda=(N-1)/B\), by Euler's identity, including at boundary maxima.

**Exact optimality conditions.** Divide the logarithmic objective derivative in each class by that class's cost coefficient. The resulting marginal returns per unit expenditure are
\[
r_a=\frac{2}{PU},\qquad r_b=\frac{2}{QV},\qquad
r_c=\frac{1/c+q(p-1)/U+p(q-1)/V}{pq}.
\]
The necessary and sufficient concave-program optimality conditions are \(r_c=\Lambda\); \(r_a=\Lambda\) when \(a>0\) and \(r_a\le\Lambda\) when \(a=0\); and the analogous conditions for \(b\). Sufficiency follows from concavity, and uniqueness from strict concavity.

If \(a,b>0\), the equalities give \(U=2/(\Lambda P)\), \(V=2/(\Lambda Q)\), and \(c=1/(\Lambda D)\). The conditions \(a,b>0\) simplify exactly to the two strict linear inequalities in the first case. If \(a=0<b\), then \(U=qc\) and \(V=2/(\Lambda Q)\); the cross-edge equality gives \(c=1/(\Lambda E)\). The requirements \(b>0\) and \(r_a\le\Lambda\) become, respectively, \(Q<2q/(N-1)\) and \(P\ge 2-(q-1)Q/q\). The case \(b=0<a\) is symmetric. Finally, if \(a=b=0\), budget and cross-edge stationarity give \(c=B/(pq)\), while both inactive inequalities reduce to \(P\ge2p/(N-1)\) and \(Q\ge2q/(N-1)\). These mutually disjoint conditions cover the full positive price quadrant, either by direct comparison of their linear boundaries or because every maximizer must occupy exactly one of these four support patterns. Hence all formulas and support statements hold globally.

For equal prices, substituting \(P=Q=t\) into those conditions gives the stated two-stage or simultaneous-collapse thresholds. When \(p<q\), \(2q/(2q-1)<2q/(p+q-1)\) strictly because \(p<q\).

## Verification

Run `python3 verify_two_block.py` with NumPy and SciPy installed. The deterministic verifier evaluates **1,225** direct reduced-Laplacian determinants against the three-eigenspace factorization, **1,225** budget and Karush–Kuhn–Tucker condition sets, **1,800** unrestricted asymmetric feasible-perturbation comparisons, and **30** independent numerical optimizations over all individual edges. All these tests passed when this package was prepared. They corroborate the proof; they do not constitute an exhaustive proof over infinite parameter ranges.

As an exact transition example, with \(p=2\), \(q=5\) and equal internal prices \(P=Q=t\), the first deletion occurs at \(t=10/9\), and the entire internal support disappears at \(t=5/3\). At \(t=6/5\), with \(B=1\), the exact optimum is \(a=0\), \(b=7/234\), \(c=5/78\); its expenditure is exactly \(1\).

## Relationship to prior work

The weighted Matrix–Tree theorem and general D-optimality of Laplacian determinants are classical. Bailey and Cameron (2011) describe the spanning-tree interpretation of optimal pairwise block designs, but address designs with fixed experimental combinatorial constraints rather than the present positive class-price continuum. Harman, Bachratá and Filová (2014) give procedures for exact D-efficient designs under resource constraints, including pairwise block designs, but do not establish these three-price support cutoffs. Khosoussi, Sukhatme, Huang and Dissanayake (arXiv 2016) formulate edge-selection problems and log-determinant convex relaxations, without this unrestricted, three-class continuous-budget analytic phase diagram. The general optimization framework is not claimed as new. The contribution assessed here is the explicit unrestricted optimizer, its complete support-region classification, and its sharp unequal-group two-stage collapse.

## Limitations

The result assumes precisely two vertex groups, independent conductance allocation, class-constant prices, a complete set of potential edges, and a linear global budget. It is not a theorem for arbitrary stochastic-block networks, integer edge selections, arbitrary edgewise prices, bounded conductances, or objectives other than weighted spanning-tree determinant. The analysis is exact; numerical verification is finite. No independent mathematical audit has been performed. An unlocated specialized prior solution of the identical priced problem would affect any publication-priority claim.

## References

1. R. A. Bailey and P. J. Cameron, *Using graphs to find the best block designs*, arXiv:1111.3768 (first posted 16 November 2011), https://arxiv.org/abs/1111.3768.
2. R. Harman, A. Bachratá and L. Filová, *Heuristic construction of exact experimental designs under multiple resource constraints*, arXiv:1402.7263 (2014), https://arxiv.org/abs/1402.7263.
3. K. Khosoussi, G. S. Sukhatme, S. Huang and G. Dissanayake, *Maximizing the Weighted Number of Spanning Trees: Near-\(t\)-Optimal Graphs*, arXiv:1604.01116 (first posted 5 April 2016), https://arxiv.org/abs/1604.01116.
