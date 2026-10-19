# Sharp edge recovery versus hidden consensus in adaptive-confidence averaging

## Finding

**Theorem (complete network with exactly one initially unreceptive pair).** For every integer \(n\geq3\), in the synchronous adaptive-confidence Hegselmann–Krause model of Li, Luo, and Porter [1], suppose the underlying graph is \(K_n\), every dyadic confidence bound initially equals \(c_0\in(0,1)\), and \(\gamma\in(0,1]\), \(\delta\in[0,1)\). Suppose initial opinions lie in \([0,1]\), every pair except \(\{1,n\}\) is receptive, and that one pair is not: writing \(d=|x_n(0)-x_1(0)|\),
\[
  |x_i(0)-x_j(0)|<c_0\quad(\{i,j\}\ne\{1,n\}),\qquad d\geq c_0.
\]
Set \(\rho=(n-1)\delta\). Then all the other pairs remain receptive forever. Moreover:

1. If \(\rho\leq1\), the pair \(\{1,n\}\) is never receptive at any finite time. All opinions nevertheless converge to the *same* limit,
\[
 L=\frac{(n-1)[x_1(0)+x_n(0)]+n\sum_{j=2}^{n-1}x_j(0)}{n^2-2},
\]
while its confidence tends to zero. Until infinity the effective graph stays \(K_n\) minus that edge. The endpoint disagreement obeys exactly \( |x_n(t)-x_1(t)|=d/(n-1)^t\), so the endpoint decay factor is sharp.
2. If \(\rho>1\), the absent edge first becomes receptive at the *exact* integer time
\[
 T=1+\left\lfloor\frac{\log(d/c_0)}{\log\rho}\right\rfloor.
\]
The effective graph becomes complete at \(T\), and the opinions become exactly equal after the update \(T\to T+1\), not earlier. In particular, the sharp confidence-decay boundary for repairing the absent tie is \(\delta_c=1/(n-1)\), independent of \(\gamma\) and of the intermediate opinions subject to the stated receptive-edge hypotheses.

The finite-time consensus value can also be computed without simulating the dynamics. Put
\[
 e_0=\tfrac12[x_1(0)+x_n(0)],\quad
 m_0=\frac{\sum_{j=2}^{n-1}x_j(0)}{n-2},\quad
 \lambda=-\frac{n-2}{n(n-1)}.
\]
In case 2 it is exactly
\[
 L+\frac{2(n-2)}{n(n^2-2)}\lambda^{T}(e_0-m_0).
\]
For \(d>c_0\), the recovery time diverges as \(\delta\downarrow\delta_c\), although the limiting consensus opinion tends to \(L\).

## Assumptions and scope

Time is integer \(t\geq0\). Let \(I_i(t)=\{i\}\cup\{j\ne i:|x_i(t)-x_j(t)|<c_{ij}(t)\}\). The original model uses the simultaneous updates
\[
 x_i(t+1)=\frac{1}{|I_i(t)|}\sum_{j\in I_i(t)}x_j(t),\qquad
 c_{ij}(t+1)=\begin{cases}
 c_{ij}(t)+\gamma[1-c_{ij}(t)]&\text{if }|x_i(t)-x_j(t)|<c_{ij}(t),\\
 \delta c_{ij}(t)&\text{otherwise}.
 \end{cases}
\]
Strict inequality matters, including at the critical boundary and at first recovery. The result is deterministic and applies to the stated open family of configurations with \(d>c_0\), as well as its \(d=c_0\) boundary. It is not a claim about arbitrary initial configurations, other network topologies, or asynchronous updates.

## Proof

Call \(a=1\) and \(b=n\) the two endpoints, and let \(M_t\) be the largest opinion difference on an edge other than \(\{a,b\}\). By assumption \(M_0<c_0\). While the endpoint pair is unreceptive, the other pairs form a complete graph with only this edge removed. Put \(S_t=\sum_i x_i(t)\). The averaging update then has the exact form
\[
 x_a(t+1)=\frac{S_t-x_b(t)}{n-1},\quad
 x_b(t+1)=\frac{S_t-x_a(t)}{n-1},\quad
 x_j(t+1)=\frac{S_t}{n}\quad (2\leq j\leq n-1).
\]
Consequently \(x_b(t+1)-x_a(t+1)=[x_b(t)-x_a(t)]/(n-1)\). For every intermediary \(j\),
\[
 |x_a(t+1)-x_j(t+1)|
 =\frac{|\sum_{k\ne b}(x_k(t)-x_b(t))|}{n(n-1)}.
\]
All summands except the one indexed by \(a\) have absolute value at most \(M_t\). The exceptional summand has absolute value at most \(2M_t\) by the triangle inequality through any intermediary (which exists because \(n\geq3\)). Thus this difference is at most \(M_t/(n-1)\). Interchanging \(a,b\) yields the analogous inequality at the other endpoint; all intermediary opinions become equal after each update. Therefore
\[
 M_{t+1}\leq\frac{M_t}{n-1}<c_0.
\]
Every receptive confidence bound is nondecreasing and initially equals \(c_0\), so none of the other pairs can ever stop being receptive. This closes the induction as long as the endpoint edge remains absent.

During this missing-edge regime, the endpoint difference and confidence are respectively \(d/(n-1)^t\) and \(c_0\delta^t\). Hence the edge is absent precisely while \(\rho^t\leq d/c_0\). If \(\rho\leq1\), this holds for all finite \(t\); if \(\rho>1\), it holds exactly for \(0\leq t<T\), with the displayed strict-inequality formula for \(T\). At time \(T\) all edges are receptive; at the subsequent synchronous update each agent averages all \(n\) opinions, producing exact consensus. Thereafter all opinion differences vanish and all confidence bounds are positive, so full receptiveness persists.

In the permanently missing case, the fixed averaging matrix is the self-looped random walk on \(K_n\) minus \(\{a,b\}\), with row-normalizing degrees \(n-1\) at the endpoints and \(n\) elsewhere. Its stationary weighted mean is \(L\), which is conserved. Since \(M_t\leq M_0/(n-1)^t\), the full opinion diameter is at most \(2M_t\) via a mediator, hence tends to zero. This plus conservation of \(L\) proves convergence to the stated common limit, without a numerical spectral assumption. The nonzero endpoint difference has the exact factor \((n-1)^{-t}\).

Finally, while the edge is absent, let \(e_t\) be the mean endpoint opinion and \(m_t\) the mean intermediary opinion. The same update gives
\[
 e_{t+1}=\frac{e_t+(n-2)m_t}{n-1},\qquad
 m_{t+1}=\frac{2e_t+(n-2)m_t}{n},\qquad
 e_{t+1}-m_{t+1}=\lambda(e_t-m_t).
\]
Writing \(\mu_t=n^{-1}\sum_i x_i(t)\), direct elimination from the invariant \(L\) gives
\[
 \mu_t=L+\frac{2(n-2)}{n(n^2-2)}(e_t-m_t).
\]
Since full consensus at time \(T+1\) equals \(\mu_T\), the stated formula follows. For \(d>c_0\), \(\log(d/c_0)>0\) and \(\log\rho\downarrow0\) as \(\delta\downarrow1/(n-1)\) from above, so \(T\to\infty\); the \(|\lambda|<1\) correction then vanishes. This completes the proof.

## Verification

The standalone standard-library program `verify.py` performs 720 exact-rational full model trajectories for \(3\leq n\leq12\), testing both sides of the sharp boundary, equality, a range of intermediate opinions, and confidence-increase parameters. It checks the active graph, exact endpoint decay, missing-edge confidence, invariant weighted mean, finite recovery time, and exact final consensus; all tests passed. The script also checks a four-agent example: \(c_0=1/2\), initial opinions \((0,1/4,1/3,3/5)\), with permanent nonreceptiveness at \(\delta=1/3\) and first recovery at \(t=1\) for \(\delta=1/2\). These finite tests are supporting checks, not a substitute for the proof for arbitrary \(n\).

## Relationship to prior work

Li, Luo, and Porter [1, §§2–3, 5–6 and appendices] define these exact dynamics, prove eventual constancy of the effective graph and zero-or-one confidence limits, and report numerical examples in which convergent opinions retain unreceptive edges. Their discussion specifically leaves determination of parameter effects and mediator nodes as further questions. Those qualitative theorems do not determine the sharp \(1/(n-1)\) recovery boundary, exact first recovery time, or the consensus-value formula for this complete-network family. The 2025 journal article [2] is the journal version of [1], not an independent earlier source. The bridge-to-consensus study [3] treats network-mediated consensus in bounded-confidence models, without this multiplicative confidence-update mechanism. The adaptive-rewiring paper [4] uses a distinct network evolution rule. No assertion of priority beyond the searched sources is made.

## Limitations

The theorem assumes exactly one initially missing receptive edge of the complete underlying graph; it does not classify simultaneous multiple missing edges or arbitrary histories. It is exact for the specified synchronous, strict-confidence model and not for stochastic Deffuant–Weisbuch dynamics. The result is a mathematical property of an idealized opinion process, not empirical evidence about interpersonal trust. Unindexed literature or a more specialized analytical example could still affect originality; independent expert review has not been performed.

## References

[1] G. J. Li, J. Luo, and M. A. Porter, *Bounded-Confidence Models of Opinion Dynamics with Adaptive Confidence Bounds*, arXiv:2303.07563, first submitted 14 March 2023; version 3, 27 July 2024. https://arxiv.org/html/2303.07563v3

[2] G. J. Li, J. Luo, and M. A. Porter, *Bounded-Confidence Models of Opinion Dynamics with Adaptive Confidence Bounds*, SIAM Journal on Applied Dynamical Systems 24 (2025), 994–1041, DOI:10.1137/23M1558951.

[3] H. Schawe, S. Fontaine, and L. Hernández, *The bridges to consensus: Network effects in a bounded confidence opinion dynamics model*, arXiv:2102.10910, 2021.

[4] N. Kan et al., *adaptive bounded-confidence model of opinion dynamics on networks*, Journal of Complex Networks, DOI:10.1093/comnet/cnac055, 2023.
