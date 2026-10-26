# A bang–bang theorem for minimizing equilibrium disagreement under independent tie-strength bounds

## Finding

**Theorem (box-corner minimization and the one-peak law).** Let \(n\ge2\), let \(E\) be any finite collection of unordered pairs of distinct vertices, and let \(L_{\mathrm{fix}}\) be the weighted Laplacian of an arbitrary undirected graph on those vertices, with nonnegative weights. Each independently adjustable edge \(e\in E\) has nonnegative weight \(w_e\in[\ell_e,u_e]\), where \(0\le\ell_e\le u_e<\infty\). Let \(K=\operatorname{diag}(k_1,\ldots,k_n)\), with every \(k_i>0\), and fix innate opinions \(s\in\mathbb R^n\). Set

\[
L(w)=L_{\mathrm{fix}}+\sum_{e\in E} w_e b_e b_e^{\mathsf T},\quad
z(w)=(K+L(w))^{-1}Ks,\quad
D(w)=z(w)^{\mathsf T}L(w)z(w),
\]

where \(b_e\) has entries \(+1\) and \(-1\) at the two endpoints. Then there exists an exact global minimizer of \(D\) in which **every** adjustable weight is at one of its two permitted endpoints:

\[
\min_{\ell_e\le w_e\le u_e}D(w)
=\min_{w\in\prod_{e\in E}\{\ell_e,u_e\}}D(w).
\]

This is an existence result for an endpoint optimum; interior optima need not be excluded when a coordinate has zero equilibrium opinion contrast. No connectivity hypothesis is needed because all stubbornness coefficients are strictly positive. It applies to strictly positive lower bounds, so it does not merely prescribe deleting all connections.

More strongly, fix every adjustable edge except one with incidence vector \(b\) and varying strength \(t\ge0\). Write \(L(t)=L_0+tbb^{\mathsf T}\), \(B=K+L_0\), \(z_0=B^{-1}Ks\), \(h=B^{-1}b\), \(q=b^{\mathsf T}z_0\), \(r=b^{\mathsf T}h>0\), \(a=z_0^{\mathsf T}L_0h\), and \(c=h^{\mathsf T}Kh>0\). For \(\lambda(t)=t/(1+rt)\), the entire response is exactly

\[
\boxed{D(t)=D(0)+(q^2-2qa)\lambda(t)-q^2c\lambda(t)^2.}
\]

If \(q=0\), the disagreement does not change as this edge weight changes. If \(q\ne0\), the response is a strictly concave quadratic in the strictly increasing coordinate \(\lambda(t)\); consequently its only possible interior stationary point is a strict **maximum**, never a minimum. If \(0<q^2-2qa<2q^2c/r\), that unique maximum occurs at \(t_*=\lambda_* /(1-r\lambda_*)\), \(\lambda_*=(q^2-2qa)/(2q^2c)\). In the two other parameter regimes the response is monotone (allowing a horizontal endpoint tangent).

## Assumptions and scope

All graphs are finite, undirected, and have nonnegative symmetric edge weights. Each adjusted tie is independent of the others and subject only to its own closed interval constraint. The objective is **pure equilibrium edge disagreement**, including the weight of the changed tie, not opinion polarization, the sum of polarization and disagreement, disagreement with equilibrium opinions held fixed, or a graph cost with budget/degree constraints. Innate opinions are arbitrary real numbers (in particular they may lie in \([0,1]\)); all entries of \(K\) are strictly positive. Parallel fixed and adjustable contributions to an edge can be combined. The bounds must be finite to invoke the compact-box minimization conclusion.

## Proof

**Existence and response formula.** Since \(K\) is positive definite and every Laplacian is positive semidefinite, \(B=K+L_0\) is positive definite and the equilibrium \(z(t)\) exists uniquely. The rank-one inverse identity gives

\[
z(t)=z_0-q\lambda(t)h,\qquad b^{\mathsf T}z(t)=\frac{q}{1+rt}.
\]

The identity \(Bh=b\) implies \(h^{\mathsf T}L_0h=b^{\mathsf T}h-h^{\mathsf T}Kh=r-c\). Expanding \(D(t)=z(t)^{\mathsf T}L_0z(t)+t(b^{\mathsf T}z(t))^2\) and using \(t/(1+rt)^2=\lambda-r\lambda^2\) yields

\[
D(t)=D(0)-2qa\lambda+q^2(r-c)\lambda^2+q^2(\lambda-r\lambda^2)
=D(0)+(q^2-2qa)\lambda-q^2c\lambda^2.
\]

Here \(r=b^{\mathsf T}B^{-1}b>0\), \(h\ne0\), and \(c=h^{\mathsf T}Kh>0\). Also \(\lambda'(t)=(1+rt)^{-2}>0\). Thus when \(q\ne0\), \(D\) is strictly concave as a function of the increasing reparameterization \(\lambda\), so the minimum over any closed interval \([\ell,u]\subset[0,\infty)\) is at \(\ell\) or \(u\). Its derivative with respect to \(\lambda\) is \(q^2-2qa-2q^2c\lambda\), which gives the exact maximum classification. When \(q=0\), both \(z(t)\) and \(D(t)\) are constant.

**From one tie to the whole network.** A global minimizer \(w^*\) exists by continuity and compactness. With all weights except the first held fixed, the one-tie result permits replacing that first coordinate by one of its endpoints without increasing \(D\). Next hold that coordinate fixed and replace the second, then the third, and so on. After finitely many replacements we obtain a vector of endpoints with objective no greater than \(D(w^*)\); global optimality forces equality. No property of one coordinate's response beyond the stated endpoint-minimum property is required, and no independence of equilibrium opinions is assumed.

**Nontrivial example.** Consider the three-vertex path with adjustable ties \((1,2)\), \((2,3)\), diagonal stubbornness \(K=I\), innate opinions \(s=(0,0,1)^{\mathsf T}\), and permitted weight range \([1/4,3]\) on each tie. The four corner disagreements, ordered as \((w_{12},w_{23})=(1/4,1/4),(1/4,3),(3,1/4),(3,3)\), are exactly

\[
\frac{148}{1225},\qquad\frac{16}{169},\qquad\frac{199}{1521},\qquad\frac{87}{800}.
\]

Thus the unique optimum is the **mixed** corner \((1/4,3)\), not either uniform endpoint design. For two isolated vertices with innate opinions \((0,1)\) and a single adjustable tie of strength \(t\), the complete response is \(D(t)=t/(1+2t)^2\), attaining a strict interior maximum at \(t=1/2\). Hence a monotonic-decrease assertion would be false even in the smallest model.

## Verification

Run `python verify.py` using Python's standard library; it uses exact rational Gaussian elimination. It independently computes equilibria and disagreement, tests the rank-one expression for 84 parameter configurations at six tie strengths, checks interior values against endpoint minima, and tests a three-edge box against its eight corners. It reproduces the four exact rational values in the three-vertex example and the two-vertex counterexample. The run recorded 1,105 successful exact-fraction assertions. These finite checks corroborate, but do not replace, the fully quantified algebraic proof above.

## Relationship to prior work

Musco, Musco, and Tsourakakis (2017) introduced graph optimization for the **sum** of equilibrium polarization and disagreement, proving that combined objective convex in edge weights; this does not imply any endpoint-minimum property for the individual disagreement summand. Chitra and Musco (2019/2020) optimize edge disagreement **with expressed opinions held fixed at each network-administrator update**, subject to degree and total-change constraints; the present target instead recomputes the FJ equilibrium for each proposed weight vector under independent box constraints. Yi and Patterson (2019) establish generalized-stubbornness formulas for disagreement and convexity of a **weighted polarization-plus-disagreement index**; their theorem does not treat the one-edge pure-disagreement response or the all-box-corners conclusion. Rácz and Rigobon (2022) analyze **polarization** under edge perturbation and derive a rank-one update; polarization is not the same functional as equilibrium edge disagreement. Xu and collaborators (2022) give generalized-stubbornness formulas and perturbation/computation results, but their perturbations change stubbornness rather than deriving the box-corner optimum of pure edge disagreement. Cinus, Gionis, and Bonchi (2023) study feed rebalancing for a polarization/disagreement optimization problem with coupled feasible constraints and a different objective. The exact special-case theorem here follows from these common FJ preliminaries plus the explicit cancellation \(h^{\mathsf T}L_0h=r-c\); none of the inspected relevant statements directly supplies the box-corner result.

## Limitations

The corner guarantee is not asserted under total-weight budgets, fixed node degrees, coupling constraints, penalties for reweighting, directed or antagonistic ties, zero stubbornness coefficients, or a combined polarization–disagreement objective. The result reduces a continuous box problem to at most \(2^{|E|}\) discrete candidates; it does not establish an efficient polynomial-time way to select the best corner. Search-based originality checks are incomplete and cannot establish publication priority or exclude a general theorem that subsumes this one. No independent scientific audit has been performed.

## References

1. C. Musco, C. Musco, C. E. Tsourakakis, *Minimizing Polarization and Disagreement in Social Networks*, arXiv:1712.09948, first posted 2017-12-28. https://arxiv.org/abs/1712.09948
2. U. Chitra and C. Musco, *Understanding Filter Bubbles and Polarization in Social Networks*, arXiv:1906.08772, first posted 2019-06-20. https://arxiv.org/abs/1906.08772
3. Y. Yi and S. Patterson, *Disagreement and Polarization in Two-Party Social Networks*, arXiv:1911.11338, first posted 2019-11-26. https://arxiv.org/abs/1911.11338
4. M. Z. Rácz and D. E. Rigobon, *Towards Consensus: Reducing Polarization by Perturbing Social Networks*, arXiv:2206.08996, first posted 2022-06-17. https://arxiv.org/abs/2206.08996
5. W. Xu et al., *Effects of Stubbornness on Opinion Dynamics*, arXiv:2208.04160, first posted 2022-08-08. https://arxiv.org/abs/2208.04160
6. F. Cinus, A. Gionis, F. Bonchi, *Rebalancing Social Feed to Minimize Polarization and Disagreement*, arXiv:2308.14486, first posted 2023-08-28. https://arxiv.org/abs/2308.14486
