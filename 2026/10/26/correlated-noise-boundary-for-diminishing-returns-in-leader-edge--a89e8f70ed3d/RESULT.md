# Correlated-noise boundary for diminishing returns in leader-edge polarization control

## Finding

Consider any finite connected weighted undirected social network with at least one fixed-opinion leader and \(n\ge2\) followers. All leaders have opinion zero. Followers obey continuous-time noisy DeGroot dynamics with a **fixed**, symmetric positive-semidefinite instantaneous noise covariance \(\Sigma\in\mathbb R^{n\times n}\). A candidate intervention adds a previously absent, positive-weight edge from a follower to a leader; the covariance does not change with the intervention. Let \(P(S)\) be the total stationary variance of follower opinions after adding candidate-edge set \(S\).

**Universal characterization.** For a fixed \(\Sigma\), the diminishing-returns inequality
\[
P(S)-P(S\cup\{e\})\ \ge\ P(T)-P(T\cup\{e\})
\]
for every admissible underlying connected weighted network, every candidate set, every \(S\subseteq T\), and every \(e\notin T\), holds **if and only if** every off-diagonal entry of \(\Sigma\) is nonnegative. Equivalently, stationary polarization is universally a decreasing supermodular set function of leader-edge additions precisely for entrywise-nonnegative noise covariance. In contrast, \(P\) is nonincreasing for **every** positive-semidefinite \(\Sigma\), even with negative correlations.

The characterization is sharp already with two followers and strictly positive-definite noise. With
\[
L=\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\qquad
\Sigma=\begin{pmatrix}1&-4/5\\-4/5&1\end{pmatrix},
\]
where the two proposed unit-weight leader edges independently add one to either diagonal of \(L\), the four stationary polarizations are
\[
P(\varnothing)=\frac25,\qquad
P(\{e_1\})=P(\{e_2\})=\frac{17}{50},\qquad
P(\{e_1,e_2\})=\frac{11}{40}.
\]
Consequently,
\[
P(\varnothing)+P(\{e_1,e_2\})-P(\{e_1\})-P(\{e_2\})=-\frac1{200}<0.
\]
The second added edge gives a larger, not smaller, variance reduction. The covariance has eigenvalues \(1/5\) and \(9/5\).

For a symmetric two-follower network with equal grounding \(s>0\), follower-to-follower weight \(c>0\), candidate leader-edge weight \(t>0\), and unit marginal variances with correlation \(-1\le\rho\le1\), the **exact** supermodularity gap has the sign of
\[
\rho-\rho_*(s,c,t),\qquad
\rho_*=-\frac{2c^2+2cs+ct}{2c^2+2cs+ct+s^2+st}.
\]
Thus \(\rho_*\in(-1,0)\) is the sharp two-follower correlation boundary; at \(s=c=t=1\) it is \(-5/7\).

## Assumptions and scope

Write \(F\) for the follower set and \(Z\ne\varnothing\) for the set of zero-opinion leaders. The weighted graph is finite, undirected, connected, and has positive weights on existing edges. The grounded follower Laplacian \(L\in\mathbb R^{n\times n}\) is the principal follower block of the full graph Laplacian. It is positive definite. Candidate edges are absent in the base graph, each joins one follower to one leader, and each has a specified positive weight \(w_e\). Multiple different candidate edges may reach the same follower. Define \(i(e)\) as the follower endpoint and
\[
A(S)=L+\sum_{e\in S}w_eE_{i(e)i(e)},\qquad E_{ii}=e_ie_i^{\mathsf T}.
\]
The follower opinion process is
\[
dX_t=-A(S)X_t\,dt+B\,dW_t,\qquad BB^{\mathsf T}=\Sigma\succeq0,
\]
with standard Brownian motion \(W\). The noise law is independent of \(S\); deterministic initial conditions have finite second moment. Stationary polarization means \(P(S)=\lim_{t\to\infty}\mathbb E\|X_t\|_2^2\), the sum of component variances, not their variance about the random population mean. The universal assertion quantifies over all such graphs and candidate sets on the given \(n\) follower labels.

## Proof

**Stationary trace identity.** Positive definiteness of \(A(S)\) gives a unique stationary covariance \(C(S)\), satisfying the Lyapunov equation
\[
A(S)C(S)+C(S)A(S)=\Sigma.
\]
Multiplying by \(A(S)^{-1}\), taking traces and using cyclicity yields
\[
P(S)=\operatorname{tr}C(S)=\frac12\operatorname{tr}\bigl(A(S)^{-1}\Sigma\bigr).
\]
This formula is valid for any symmetric positive-semidefinite covariance, including correlated or degenerate noise.

**All positive-semidefinite noise preserves monotonicity.** For nonnegative real added grounding strengths \(u=(u_1,\ldots,u_n)\), set \(A(u)=L+\operatorname{diag}(u)\) and \(G(u)=A(u)^{-1}\). Matrix differentiation gives
\[
\frac{\partial P}{\partial u_i}=-\frac12\bigl(G\Sigma G\bigr)_{ii}\le0,
\]
since \(G\Sigma G\) is positive semidefinite. Integrating along positive-coordinate increments proves \(P(T)\le P(S)\) whenever \(S\subseteq T\).

**Sufficiency for supermodularity.** A grounded Laplacian with positive weights is a nonsingular symmetric \(M\)-matrix. By the discrete maximum principle its inverse is entrywise nonnegative: \(G_{ij}\ge0\). A second differentiation gives the *exact mixed-sensitivity identity*
\[
\frac{\partial^2P}{\partial u_i\partial u_j}
=G_{ij}\bigl(G\Sigma G\bigr)_{ij}\quad(1\le i,j\le n).
\]
If \(\Sigma\) is entrywise nonnegative, then \(G\Sigma G\) is entrywise nonnegative as well. Thus every mixed derivative is nonnegative, including \(i=j\). Integrating these derivatives over two candidate-edge increments (and then summing over previously selected edges) gives nonnegative pairwise discrete differences. These differences are equivalent to the stated diminishing-returns supermodularity for all finite candidate sets.

**Necessity on the entire network class.** Suppose \(\Sigma_{ij}<0\) for distinct follower labels \(i,j\). Take two zero-opinion leaders \(z_0,z_1\), connect them, attach every follower to \(z_0\) with weight \(s>0\), and add a follower-follower edge of weight \(c>0\) between \(i,j\); no other follower-follower edges are needed. The two missing unit-weight candidate edges join \(z_1\) to \(i\) and to \(j\). This defines a connected, finite weighted network. Its grounded matrix before candidate additions is
\[
L_s=sI+c(e_i-e_j)(e_i-e_j)^{\mathsf T}.
\]
Uniformly for candidate increments \(u_i,u_j\in[0,1]\), a Neumann expansion as \(s\to\infty\) gives
\[
G_{ij}=\frac c{s^2}+O(s^{-3}),\qquad
(G\Sigma G)_{ij}=\frac{\Sigma_{ij}}{s^2}+O(s^{-3}).
\]
The mixed-sensitivity identity therefore equals \(c\Sigma_{ij}s^{-4}+O(s^{-5})<0\) throughout the unit square for all sufficiently large \(s\). Integrating over that square makes the discrete supermodularity gap strictly negative. Consequently **no** positive-semidefinite covariance with a negative off-diagonal can guarantee supermodularity over all connected weighted leader-follower networks. Together with sufficiency, this proves the characterization.

**Sharp two-follower boundary.** When
\[
L=\begin{pmatrix}s+c&-c\\-c&s+c\end{pmatrix},\qquad
\Sigma_\rho=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},
\]
and each candidate contributes \(t\) to its own diagonal, direct \(2\times2\) inversion gives the exact difference
\[
\begin{split}
\Delta&=P(\varnothing)+P(\{e_1,e_2\})-P(\{e_1\})-P(\{e_2\})\\[2pt]
&=\frac{ct^2\Bigl[(2c^2+2cs+ct)(1+\rho)+\rho s(s+t)\Bigr]}{s(2c+s)(s+t)(2c+s+t)(2cs+ct+s^2+st)}.
\end{split}
\]
Its denominator is strictly positive, giving the exact threshold and explicit rational example stated in the finding. No numerical approximation is required in the proof.

## Verification

Run `python verify.py` with Python 3; it uses only the standard library. The checker independently inverts rational matrices, tests the exact two-follower formula across rational parameter grids, verifies the positive-definite counterexample and all four polarizations, and tests monotonicity and the sufficient supermodularity condition on small, randomly generated weighted follower networks with rational positive-semidefinite covariances. The saved verifier passed **8,686 exact-rational assertions**. These finite checks are supplements to, not proofs of, the universal claims; the analytic proof above supplies the infinite quantifiers.

## Relationship to prior work

Xu and Zhang (2023, arXiv:2308.07008, Theorem 4.3) show supermodularity of grounded effective-resistance polarization for the independent unit-variance noise model, using the same type of leader-to-follower candidate edge. The present theorem takes their natural correlated-noise extension and characterizes exactly when the guarantee survives uniformly over networks, while distinguishing the universally preserved monotonicity. The original independent-noise result is not contradicted.

Clark, Bushnell and Poovendran (2012, arXiv:1208.0946) treat noisy linear networks and supermodular **leader selection** under independent link noise, not this fixed-leader, fixed-correlated-covariance edge-addition characterization. Summers, Shames, Lygeros and Dörfler (2014, arXiv:1411.4884) study coherence optimization via edge addition with independent node noise in an ungrounded consensus formulation. Mackin and Patterson (2017, arXiv:1712.08212) study selection of noise-corrupted **leader nodes** under an inverse-trace objective, also not the covariance-sign criterion for leader-edge additions. Matrix inverse-positivity and standard calculus are acknowledged proof ingredients, not claimed as new. No covering statement was located in the sources inspected; this is a bounded literature assessment, not proof of publication priority.

## Limitations

The criterion is **universal across the specified graph class**, not necessary for supermodularity on every single fixed graph: a negatively correlated covariance can still yield supermodularity on particular networks. The noise covariance is fixed while edges are added; state-dependent, edge-dependent, temporally colored, or nonstationary noise is not covered. The theorem concerns undirected positive-weight networks with fixed zero-opinion leaders and total stationary opinion variance; it does not characterize alternative polarization metrics, directed influence, adaptive leader opinions, or edge additions between two followers. The greedy performance implications use the usual assumptions and are not new algorithmic guarantees beyond the recovered supermodularity property. Publication priority remains provisional, and no independent scientific audit was performed.

## References

1. Wanyue Xu and Zhongzhi Zhang, *Minimizing Polarization in Noisy Leader-Follower Opinion Dynamics*, arXiv:2308.07008v1, first submitted 14 August 2023. https://arxiv.org/html/2308.07008v1
2. Andrew Clark, Linda Bushnell and Radha Poovendran, *A Supermodular Optimization Framework for Leader Selection under Link Noise in Linear Multi-Agent Systems*, arXiv:1208.0946v1, 2012. https://arxiv.org/html/1208.0946v1
3. Tyler Summers, Iman Shames, John Lygeros and Florian Dörfler, *Topology Design for Optimal Network Coherence*, arXiv:1411.4884v1, 2014. https://arxiv.org/html/1411.4884v1
4. Erika Mackin and Stacy Patterson, *Submodular Optimization for Consensus Networks with Noise-Corrupted Leaders*, arXiv:1712.08212, 2017. https://arxiv.org/abs/1712.08212
