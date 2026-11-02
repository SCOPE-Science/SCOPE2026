# Exact cubic all-leader phase transition for second-order coherence on \(K_{m,m+1}\)

## Finding
For each integer \(m\ge2\) and leader budget \(1\le k\le m\), let \(G=K_{m,m+1}\) have unit edge conductances and let \(L\) be its combinatorial Laplacian. Choose exactly \(k\) distinct noise-free grounded leaders \(S\); let \(F=V(G)\setminus S\), and minimize the **second-order grounded coherence**
\[
J(S)=\operatorname{tr}(L_{FF}^{-2}).
\]
Here \(L_{FF}\) is the principal submatrix indexed by followers, *not* the follower-induced-subgraph Laplacian (the original follower degrees remain on its diagonal).

Put
\[
P_m(k)=(2m+1)k^3+2m(m+1)k-(2m+1)^3.
\]
Then **every global minimizer is monochromatic**: every chosen leader belongs to a single part. More precisely, if \(P_m(k)<0\), precisely all \(k\)-subsets of the part of size \(m\) minimize \(J\); if \(P_m(k)>0\), precisely all \(k\)-subsets of the part of size \(m+1\) minimize \(J\); and if \(P_m(k)=0\), precisely those two families tie. No mixed allocation is optimal, even at equality.

The polynomial \(P_m\) is strictly increasing for positive real arguments and has a unique positive root \(\tau_m\). The threshold has the asymptotic expansion
\[
\tau_m=4^{1/3}m^{2/3}-\frac{m^{1/3}}{3\,4^{1/3}}+O(1).
\]
Thus the favored side changes at a leader budget proportional to \(m^{2/3}\), a different structural scale from the first-order grounded coherence criterion.

## Assumptions and scope
The graph is finite, simple, connected, unweighted, undirected, and exactly complete bipartite with part sizes \(m\) and \(m+1\). The leaders are perfectly grounded and noiseless, have no stochastic follower states, and do not contribute to \(J\); the number of leaders is exactly \(k\). The theorem applies to *every* integer \(m\ge2\) and \(1\le k\le m\), with no additional assumptions. This is an optimization of the inverse **square**; its optimizer need not agree with that of \(\operatorname{tr}(L_{FF}^{-1})\).

## Proof
Label the two parts \(A\) and \(B\), with \(|A|=m\) and \(|B|=m+1\). Let \(a=|S\cap A|\), so \(0\le a\le k\), and define the follower counts
\[
u=m-a,\qquad v=m+1-k+a,\qquad N=2m+1.
\]
With the followers ordered by part, their grounded matrix is
\[
L_{FF}=\begin{pmatrix}(m+1)I_u&-\mathbf1_u\mathbf1_v^{\mathsf T}\\-\mathbf1_v\mathbf1_u^{\mathsf T}&mI_v\end{pmatrix}.
\]
The mean-zero subspaces within the two parts carry eigenvalues \(m+1\) and \(m\), with multiplicities \(u-1\) and \(v-1\), when both parts have followers. The two remaining constant-on-part modes have a \(2\)-by-\(2\) representative with trace \(N\) and determinant
\[
D(a)=m(m+1)-uv=mk+a(a-k+1)>0.
\]
For its eigenvalues \(\lambda_\pm\), the inverse-square sum is \((N^2-2D)/D^2\). Thus for every allowed count,
\[
J(a)=\frac{u-1}{(m+1)^2}+\frac{v-1}{m^2}+\frac{N^2-2D(a)}{D(a)^2}.\tag{1}
\]
At the possible degeneracy \(u=0\) (which requires \(k=m, a=m\)), the grounded matrix is simply \(mI_v\); formula (1) remains valid because the formal extra \(m+1\) mode cancels the negative-multiplicity term \(-1/(m+1)^2\). This directly verifies the boundary rather than relying on an inadmissible two-mode decomposition.

Define \(f(d)=N^2/d^2-2/d\). For \(0<d\le m(m+1)\),
\[
f'(d)=\frac{2(d-N^2)}{d^3}<0.
\]
For every mixed configuration \(1\le a\le k-1\),
\[
D(a)=mk-a(k-1-a)\le mk=D(0).
\]
Meanwhile the first two terms of (1), compared with the all-\(B\) configuration \(a=0\), rise strictly by
\[
a\left(\frac1{m^2}-\frac1{(m+1)^2}\right)>0.
\]
Monotonicity of \(f\) therefore proves the **strict** inequality \(J(a)>J(0)\) for every mixed count. Hence only the pure counts \(a=0\) and \(a=k\) can minimize.

For these two counts, \(D(0)=mk\) and \(D(k)=k(m+1)\). Substitution and rational simplification of (1) give
\[
J(k)-J(0)=\frac{(2m+1)k^3+2m(m+1)k-(2m+1)^3}{k^2m^2(m+1)^2}.\tag{2}
\]
The denominator is positive. The sign of (2) gives exactly the asserted classification, including its equality case and every minimizer within each symmetry class.

Finally, regarding \(k\) as a positive real variable, \(P_m(0)=-(2m+1)^3<0\), \(P_m(k)\to\infty\), and
\[
\frac{\partial P_m}{\partial k}=3(2m+1)k^2+2m(m+1)>0.
\]
There is therefore precisely one positive root \(\tau_m\). To determine its scale, substitute \(k=c m^{2/3}+d m^{1/3}\) into \(P_m(k)\). Cancellation of orders \(m^3\) and \(m^{8/3}\) requires \(c^3=4\) and \(6c^2d+2c=0\), hence \(c=4^{1/3}\) and \(d=-1/(3c)\). The next order also cancels, and the residual is \(O(m^2)\), while the positive derivative on an interval of constant width around the approximation is of order \(m^{7/3}\). The unique exact root consequently differs by \(O(m^{-1/3})\), in particular by \(O(1)\), completing the stated expansion.

## Verification
The accompanying standalone `verify.py` uses exact rational Gauss–Jordan inverses of the **actual grounded matrices**, independent of the spectral formula used in the proof. Running `python3 verify.py` prints `FINITE_CHECKS_OK spectral=154,optimizer_cases=35,subsets=399`. The checks comprise all leader-count orbits for \(2\le m\le8\), all admissible budgets in those instances, polynomial-sign comparisons, and exhaustive subset comparisons for smaller graphs. Direct exact inversion also covers the \(u=0\) boundary. An independent symbolic simplification confirms the pure-objective difference (2). No finite calculation is used as a substitute for the proof for arbitrary \(m\).

## Relationship to prior work
Fitch and Leonard (2014, arXiv:1407.1569) develop noisy-consensus leader selection and joint centrality for **first-order** grounded inverse-trace performance. Patterson, McGlohon and Dyagilev (2014, arXiv:1412.6595) optimize that same inverse-trace objective on **paths and cycles**, not a complete bipartite graph with inverse-square performance. Mackin and Patterson (2019, arXiv:1905.09156) derive an inverse-square trace criterion for second-order **finite-gain absolute-information** systems and study submodular greedy selection; their full text does not give an exact all-budget optimum for perfectly grounded \(K_{m,m+1}\). The present complete classification is not a mere numeric special case of those more general algorithmic frameworks, because their statements do not determine the minimizing sets or the cubic transition. It is nevertheless possible that specialized graph-family results not located in this comparison overlap this claim.

## Limitations
The placement theorem is proved only for unit-weight complete bipartite networks with part sizes differing by exactly one, perfectly grounded leaders, and \(1\le k\le m\). The expansion describes the *continuous* real root; admissible integer leader budgets are classified by the exact sign of \(P_m(k)\), including hypothetical ties. The general proof does not assert an extension to unequal edge weights, arbitrary bipartitions, finite leader-information gains, or alternative noise covariances. No independent mathematical audit has been performed, and a missed specialized precursor remains possible.

## References
1. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, first publicly posted 2014-07-07. https://arxiv.org/abs/1407.1569
2. S. Patterson, N. McGlohon and K. Dyagilev, *Efficient, Optimal \(k\)-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595, first publicly posted 2014-12-20. https://arxiv.org/abs/1412.6595
3. E. Mackin and S. Patterson, *Submodularity in Systems with Higher Order Consensus with Absolute Information*, arXiv:1905.09156, first publicly posted 2019-05-22. https://arxiv.org/abs/1905.09156
