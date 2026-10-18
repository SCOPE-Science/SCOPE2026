# Gain-reentrant optimal leader placement on noisy star consensus networks

## Finding

**Theorem (exact finite-gain classification).** Let \(n\ge 3\), and consider the unweighted star \(K_{1,n-1}\) with hub vertex \(0\). Fix a leader budget \(1\le q\le n-1\), common feedback gain \(\kappa>0\), and a subset \(S\) of exactly \(q\) pinned vertices. The unit-noise stochastic consensus dynamics are
\[
 dX_t=-A_S X_t\,dt+dW_t,\qquad
 A_S=L+\kappa\operatorname{diag}(\mathbf 1_S),
\]
where \(L\) is the unit-conductance graph Laplacian and \(W_t\) is a standard \(n\)-dimensional Brownian motion. Their total stationary variance is
\[
 J(S)=\frac12\operatorname{tr}(A_S^{-1}).
\]
All such matrices are positive definite. Define \(J_C\) for a set consisting of the hub and \(q-1\) leaves, and \(J_L\) for a set consisting of \(q\) leaves without the hub. Then
\[
 \boxed{\displaystyle
 J_C-J_L=\frac{(1+\kappa)^2(2q-n)+\kappa q(q-1)}
 {2q(1+\kappa)(\kappa+q)}.}
\]
All configurations have one of these two values. Thus the exact global optimum is hub-inclusive precisely when
\[
 \boxed{\displaystyle n>2q+\frac{\kappa q(q-1)}{(1+\kappa)^2},}
\]
and is hub-excluding when this inequality is reversed; at equality both entire classes are optimal. In each strict regime every optimizer belongs to the preferred class.

For \(q=1\) and all \(n\ge3\), the hub is uniquely optimal. For \(q\ge2\), set \(B_q=q(q-1)/4\). The complete phase classification is:

- If \(n\le 2q\), every optimum excludes the hub for every finite positive gain.
- If \(n>2q+B_q\), every optimum includes the hub for every finite positive gain.
- If \(n=2q+B_q\), the hub-inclusive class is optimal at all gains, with an additional hub-excluding tie exactly at \(\kappa=1\).
- If \(2q<n<2q+B_q\), write \(\delta=(n-2q)/(q(q-1))\). Then \(0<\delta<1/4\), and the two reciprocal transition gains
\[
 \boxed{\displaystyle
 \kappa_{\pm}=\frac{1-2\delta\pm\sqrt{1-4\delta}}{2\delta},
 \qquad \kappa_-\kappa_+=1}
\]
partition the gains as follows: the hub-inclusive class is optimal for \(0<\kappa<\kappa_-\) and \(\kappa>\kappa_+\), the hub-excluding class for \(\kappa_-<\kappa<\kappa_+\), with ties at the endpoints.

The smallest possible reentrant example over all integer network sizes and leader budgets is \(n=7\), \(q=3\), with exact gains \(\kappa_{\pm}=2\pm\sqrt3\). At \(\kappa=1\),
\[
 J_C=\frac{31}{8},\qquad J_L=\frac{23}{6},\qquad J_C-J_L=\frac1{24}>0,
\]
so exactly the three-leaf sets are optimal; for sufficiently weak or strong positive feedback, precisely the sets containing the hub are optimal.

## Assumptions and scope

There are \(n\) scalar states, one hub, \(n-1\) mutually nonadjacent leaves, and unit edge conductances. Each of the exactly \(q\) leaders receives **identical finite positive** feedback \(\kappa\) toward a constant common reference. Every vertex—including a leader—is disturbed by independent unit-intensity Brownian noise. The objective is total steady-state nodewise variance and equals the squared stochastic \(H_2\) gain for identity disturbance input and identity state output. There are no costs for feedback gain, heterogeneous edge weights, or state/input normalization beyond those stated. For \(q=n\), all vertices are pinned and there is only one placement, so the statement intentionally treats \(q\le n-1\).

## Proof

**Existence of stationary variance.** For every real vector \(v\),
\[
 v^\mathsf T A_Sv=\sum_{i=1}^{n-1}(v_i-v_0)^2+\kappa\sum_{i\in S}v_i^2.
\]
Since the star is connected and \(S\ne\varnothing\), equality holds only for \(v=0\). Thus \(A_S\) is symmetric positive definite. The stationary covariance solves \(A_S\Sigma+\Sigma A_S=I\), giving uniquely \(\Sigma=A_S^{-1}/2\).

**A resolvent formula for the entire star.** Write \(m=n-1\), and suppose the hub indicator is \(c\in\{0,1\}\), so \(r=q-c\) leaves are pinned. Reorder the leaves and set
\[
 A_S=\begin{pmatrix}m+c\kappa&-\mathbf1^\mathsf T\\-\mathbf1&D\end{pmatrix},
 \qquad D=\operatorname{diag}(\underbrace{1+\kappa,\ldots,1+\kappa}_{r},
 \underbrace{1,\ldots,1}_{m-r}).
\]
Let
\[
 s_1=m-r+\frac r{1+\kappa},\qquad
 s_2=m-r+\frac r{(1+\kappa)^2},\qquad
 \tau=m+c\kappa-s_1.
\]
By the Schur-complement inverse formula,
\[
 \operatorname{tr}(A_S^{-1})=s_1+\frac{1+s_2}{\tau}.
\]
The positive complement \(\tau\) is \(\kappa(\kappa+q)/(1+\kappa)\) for \(c=1\), and \(q\kappa/(1+\kappa)\) for \(c=0\). Substituting \(r=q-1\) and \(r=q\), and simplifying the two rational expressions, gives precisely
\[
 2(J_C-J_L)=
 \frac{(1+\kappa)^2(2q-n)+\kappa q(q-1)}
 {q(1+\kappa)(\kappa+q)}.
\]
Leaf permutations act transitively on the sets in each class, and every eligible leader set is in exactly one class. Comparing this one difference consequently solves the unrestricted combinatorial placement problem.

**Gain phases and endpoint cases.** The denominator in the last display is strictly positive. Dividing the numerator by \((1+\kappa)^2\), its sign is that of
\[
 2q-n+q(q-1)f(\kappa),\qquad
 f(\kappa)=\frac{\kappa}{(1+\kappa)^2}.
\]
For \(\kappa>0\), \(f(\kappa)>0\), \(f(\kappa)\le1/4\), with equality only at \(\kappa=1\), and \(f(1/\kappa)=f(\kappa)\). These properties give all constant-class regimes and the isolated tangent tie. In the intermediate regime, the equation \(f(\kappa)=\delta\) is
\[
 \delta\kappa^2+(2\delta-1)\kappa+\delta=0.
\]
Its two real positive roots are \(\kappa_\pm\) as displayed, ordered \(0<\kappa_-<1<\kappa_+\), and their product is one. The strict signs between and outside them follow from the strict maximum of \(f\) at one. For \(q=1\) the numerator reduces to \((1+\kappa)^2(2-n)<0\), giving the unique hub optimum.

**First reentrant size.** Reentrance requires integers \(q\ge3\) and \(2q<n<2q+q(q-1)/4\). For \(q=2\), the open interval \((4,9/2)\) has no integer; for \(q\ge4\), \(n>2q\) forces \(n\ge9\). For \(q=3\), the open interval \((6,15/2)\) contains exactly \(n=7\). Its \(\delta=1/6\) gives \(\kappa_\pm=2\pm\sqrt3\), and the exact reported objective values follow from the resolvent formula.

## Verification

Run \(\texttt{python3 verify.py}\) with Python 3 and no third-party libraries. The checker constructs full rational pinned-Laplacian matrices, inverts them by exact Gauss–Jordan elimination, checks both orbit representatives and their analytical traces for every \(3\le n\le14\), \(1\le q\le n-1\), and the five rational gains \(1/10,1/3,1,3,10\). It verifies the exact difference formula and exhaustively checks all \(\binom73=35\) placements at gains \(1/10,1,10\), yielding 1,455 rational tests. The expected final diagnostic is \(\texttt{VERIFY\_OK}\). All universal statements are proven algebraically above; finite tests are regression checks only.

## Relationship to prior work

Lin, Fardad, and Jovanović [1] formulated exactly the same finite-feedback, noise-corrupted stochastic consensus objective for arbitrary connected graphs and developed convex relaxations and leader-selection algorithms, but did not give the above all-budget star classification or the gain-reentrant boundary. Fitch and Leonard [2] developed graph-centrality criteria for one or two noise-corrupted leaders and arbitrary numbers of noise-free leaders; their explicitly solved graph examples use cycles or paths, not the finite-gain \(q\ge3\) star problem. Patterson, Yi, and Zhang [3] derived resistance-distance expressions and solved several noise-free cases and the two-noise-corrupted-leader cycle case, not the present arbitrary-budget finite-gain star phases. Liu et al. [4] analyzed grounded Laplacian **smallest eigenvalues**, including a singly pinned star, rather than the trace-inverse finite-feedback objective; those spectral claims do not imply this gain-reentrant optimization. The direct contribution here is the closed-form hub-versus-leaf law and its reciprocal gain transition, not the general covariance identity, block inverse formula, or unweighted star spectrum.

## Limitations

The classification requires a simple unit-weight star, homogeneous leader gain, independently disturbed leaders and followers, exactly \(q\) leaders, and total *unweighted* steady-state variance. It does not cover optimal selection under heterogeneous gains, finite gain budgets, nonstar trees, noise-free followers, or alternative spectral design criteria. It establishes no physical cost or performance guarantee beyond the specified Gaussian linear dynamics and objective. Independent historical priority and mathematical validation have not been established; general formulations and potentially unindexed specializations of related work are residual originality risks.

## References

[1] F. Lin, M. Fardad, and M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450v1, first public 3 February 2013, https://arxiv.org/abs/1302.0450 . Relevant material: Secs. 2.1, 3, and 5.

[2] K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569v1, https://arxiv.org/abs/1407.1569 . Relevant material: Secs. IV and V.

[3] S. Patterson, Y. Yi, and Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873v1, https://arxiv.org/abs/1708.06873 . Relevant material: Secs. III and IV.

[4] H. Liu, X. Xu, J.-A. Lu, G. Chen, and Z. Zeng, *Optimizing Pinning Control of Complex Dynamical Networks Based on Spectral Properties of Grounded Laplacian Matrices*, arXiv:1804.10818v1, https://arxiv.org/abs/1804.10818 . Relevant material: Sec. III-C, Proposition 1.
