# The cubic hub-allocation threshold for multi-leader coherence on \(K_{2,q}\)

## Finding

Consider the unit-conductance complete bipartite graph \(K_{2,q}\), consisting of two hubs adjacent to the same \(q\) peripheral vertices. Choose exactly \(k\) noise-free grounded leaders to minimize the grounded-Laplacian inverse trace
\[
J(S)=\operatorname{tr}\bigl(L_{V\setminus S,V\setminus S}^{-1}\bigr).
\]
For all integers \(k\ge4\) and \(q\ge k\), define
\[
P_k(q)=q^3+(1-2k)q^2+(-k^2+k-2)q+2k(k-1).
\]
There is a unique real \(\tau_k>k\) satisfying \(P_k(\tau_k)=0\), with \(2k<\tau_k<3k\). Let \(h\) be the number of selected hubs. **All and only** minimizers have
\[
h=\begin{cases}
0,&q<\tau_k,\\
0\text{ or }1,&q=\tau_k,\\
1,&q>\tau_k.
\end{cases}
\]
Every choice of the required number of peripheral leaders is a minimizer; no leader set with both hubs is optimal. If instead \(k=q+1\ge4\), all and only minimizers have exactly one hub and all \(q\) peripherals grounded. The threshold has the asymptotic expansion
\[
\tau_k=(1+\sqrt2)k-\tfrac32+O(k^{-1})\qquad(k\to\infty).
\]
In particular, on \(K_{2,8}\) the unique optimal two-leader set comprises both hubs, whereas every optimal four-leader set comprises four peripheral vertices and no hubs. Optimal leader sets therefore need not contain any optimal lower-budget leader set, even on this highly symmetric network.

## Assumptions and scope

Every original edge has conductance one. Leaders are perfectly grounded and receive no noise. The unnormalized combinatorial Laplacian is used. For nonempty leader sets \(S\), the follower principal submatrix \(L_{FF}\) is positive definite; when every vertex is grounded, the objective is zero by the empty-trace convention, but that trivial case is excluded. The main threshold classification assumes \(k\ge4\), \(q\ge k\); the boundary \(k=q+1\ge4\) is stated separately. The two-leader example is an additional exact comparison, not a claim about all two-leader configurations on arbitrary graphs. Total stationary follower variance for independent unit-intensity additive state noise is \(J(S)/2\).

## Proof

Write \(h\in\{0,1,2\}\) for the number of hubs that are leaders, \(\alpha=2-h\) for remaining hub followers and \(\beta=q-k+h\) for remaining peripheral followers. Feasibility means \(0\le\beta\le q\). After ordering followers, the grounded matrix is
\[
M_{\alpha,\beta}=\begin{pmatrix}
qI_\alpha&-\mathbf1_\alpha\mathbf1_\beta^\top\\
-\mathbf1_\beta\mathbf1_\alpha^\top&2I_\beta
\end{pmatrix}.
\]
When both follower classes are nonempty, vectors summing to zero within each class give eigenvalues \(q\) with multiplicity \(\alpha-1\) and \(2\) with multiplicity \(\beta-1\). The remaining two-dimensional block in the normalized class-constant basis is
\[
\begin{pmatrix}q&-\sqrt{\alpha\beta}\\-\sqrt{\alpha\beta}&2\end{pmatrix},
\]
whose determinant is \(2q-\alpha\beta>0\). Its inverse has trace \((q+2)/(2q-\alpha\beta)\). If either follower class is empty, direct inspection of the diagonal grounded matrix gives the same expression after cancellation. Consequently, without any assumptions on the particular vertices selected within a class,
\[
\boxed{J_h=\frac{\alpha-1}{q}+\frac{\beta-1}{2}+\frac{q+2}{2q-\alpha\beta}.}
\]
For \(4\le k\le q\) all three hub counts are feasible and this identity specializes to
\[
\begin{aligned}
J_0&=\frac1q+\frac{q-k-1}{2}+\frac{q+2}{2k},\\
J_1&=\frac{q-k}{2}+\frac{q+2}{q+k-1},\\
J_2&=\frac{q-k+2}{2}.
\end{aligned}
\]
Exact subtraction yields
\[
J_1-J_2=\frac{3-k}{q+k-1}<0,
\qquad
J_0-J_1=\frac{P_k(q)}{2kq(q+k-1)}.
\]
Thus two hubs are always strictly dominated. The sign of \(P_k(q)\) selects exactly the stated leader classes; class symmetry describes every labeled minimizer and all possible ties. For \(k=q+1\), \(h=0\) is infeasible and the same strict comparison shows that \(h=1\) alone is optimal.

To establish the threshold, compute
\[
P_k(k)=-2k(k^2-2k+2)<0,\quad
P_k(2k)=-2k(k-3)(k-1)<0,\quad
P_k(3k)=2k(3k^2+7k-4)>0.
\]
Moreover \(P_k''(q)=6q+2-4k>0\) for all \(q\ge k\). Strict convexity and these signs imply exactly one root on \([k,\infty)\), between \(2k\) and \(3k\), with the signs as claimed. Setting \(s=1+\sqrt2\), the leading term of \(k^{-3}P_k(sk)\) vanishes. Direct polynomial expansion gives
\[
P_k(sk-\tfrac32)=\frac{(14\sqrt2-50)k+15}{8}=O(k),
\]
while \(P_k'(q)=(4+2\sqrt2)k^2+O(k)\) near \(q=sk-3/2\). The intermediate value theorem, strict convexity and these derivative bounds therefore yield \(\tau_k=sk-3/2+O(k^{-1})\).

Finally, for \(q=8\) and two leaders, \(J_2=4\), \(J_1=37/9\) and \(J_0=41/8\), so the two hubs are the unique optimum. With four leaders on that same graph, \(J_0=23/8\), \(J_1=32/11\), and \(J_2=3\), so every four-leader optimum consists only of peripherals. This proves the stated non-nesting witness.

## Verification

The standalone program `verify.py` uses exact rational Gaussian elimination on the actual grounded Laplacian, independently of the spectral derivation. It compared 258 class-representative grounded inversions with the closed expression, checked every one of 1,474 leader subsets for all \(4\le q\le8\), \(4\le k\le q+1\), and compared all optimizer classes for \(4\le q\le15\). It also checked the signs of the cubic over many integer parameter pairs and the two exact examples. The record is in `verification.log`. These finite checks support, but do not substitute for, the complete symbolic proof.

## Relationship to prior work

Fitch and Leonard (arXiv:1407.1569, first posted July 7, 2014) express noisy-consensus leader performance through joint centrality and derive explicit path and cycle leader-placement results. Their general framework allows objective evaluation, but their analyzed special families do not give this complete bipartite hub-allocation threshold for arbitrary \(k\ge4\). Patterson, McGlohon and Dyagilev (arXiv:1412.6595, December 20, 2014) give exact polynomial-time algorithms for weighted paths and cycles, not the biclique allocation solved here. An existing exact-three-leader biclique classification covers \(k=3\), which is excluded here; an all-budget classification for \(K_{m,m+1}\) only intersects the present \(K_{2,q}\) family at \(q=3\), outside the threshold domain. The new result is an all-budget (\(k\ge4\)) phase law on the unbounded two-hub family and an exact non-nesting witness; it does not claim discovery of the general leader-selection objective or of non-nesting on arbitrary graphs.

## Limitations

The theorem is restricted to unit-conductance \(K_{2,q}\), perfect grounding, independent additive state noise, and the inverse-grounded-Laplacian trace. It does not classify arbitrary \(K_{p,q}\), heterogeneous edge weights, finite-strength leaders, or other control objectives. The threshold is the unique real root of a cubic; a nonintegral root simply means no integer-size tie. Searches and material inspection do not guarantee absolute publication priority, and an equivalent specialized result could still exist. No independent mathematical audit has been performed.

## References

1. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569 (initial posting July 7, 2014), https://arxiv.org/abs/1407.1569.
2. S. Patterson, N. McGlohon and K. Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595 (initial posting December 20, 2014), https://arxiv.org/abs/1412.6595.
