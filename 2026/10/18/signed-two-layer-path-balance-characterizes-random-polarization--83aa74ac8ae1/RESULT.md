# Signed two-layer path balance characterizes random polarization in reinforced Bernoulli networks

## Finding
Let \(B,W\) be nonnegative row-stochastic matrices of order \(n\ge2\), with \(P=BW\) irreducible. Let \(q_j\in[0,1]\) and \(s_j=2q_j-1\). Construct a directed **signed-path multigraph**: for every triple \((i,j,k)\) with \(B_{ij}W_{jk}>0\), add an edge \(i\to k\) labelled \(s_j\). Call the graph **balanced** when every occurring label is \(+1\) or \(-1\), and some \(h\in\{-1,1\}^n\) satisfies \(h_i=s_jh_k\) on every such edge. Equivalently, all occurring labels have modulus one and every directed closed walk (including parallel-edge distinctions) has positive sign product.

For any deterministic \(z_0\in(0,1)^n\), consider the process specified below. If the signed-path multigraph is not balanced, then \(z_t\to \frac12\mathbf1\) almost surely. If it is balanced, there exists a nonconstant random variable \(\xi\in[0,1]\) such that, almost surely, for every \(i\),
\[
 z_t(i)\longrightarrow \frac{1-h_i}{2}+h_i\xi.
\]
Let \(\pi\) be the unique stationary probability row vector of \(P\), let \(\alpha_j=\sum_i\pi_iB_{ij}\), and let \(p_j^0=q_j\sum_kW_{jk}z_0(k)+(1-q_j)(1-\sum_kW_{jk}z_0(k))\). Then
\[
\mathbb E\xi=\sum_i\pi_i\bigl[\tfrac12+h_i(z_0(i)-\tfrac12)\bigr],\qquad
\operatorname{Var}(\xi)\ge\sum_j\alpha_j^2p_j^0(1-p_j^0)>0.
\]
Thus balance is a necessary and sufficient, finite graph-theoretic condition for a genuinely random limit, rather than merely a singular drift matrix.

A striking example has \(n=4\), \(q=(1,1,0,0)\), and matrices
\[
W=\frac12\begin{pmatrix}1&1&0&0\\0&0&1&1\\1&1&0&0\\0&0&1&1\end{pmatrix},\qquad
B=\frac12\begin{pmatrix}1&0&0&1\\1&0&0&1\\0&1&1&0\\0&1&1&0\end{pmatrix}.
\]
Here \(BW=\mathbf1\mathbf1^{\mathsf T}/4\), so the unsigned two-layer interaction is strictly positive and mixes in one step, yet \(h=(1,1,-1,-1)\) is balanced and
\[
z_t\longrightarrow(\xi,\xi,1-\xi,1-\xi)\quad\text{a.s.}
\]
For \(z_0=\mathbf1/2\), the bound reads \(\operatorname{Var}(\xi)\ge1/16\). This is random anti-consensus despite a strictly positive primitive effective interaction matrix.

## Assumptions and scope
At each integer time \(t\ge0\), conditional on the past, independently across \(j\in\{1,\ldots,n\}\), sample \(I_{t+1}(j)\in\{0,1\}\) with
\[
\Pr(I_{t+1}(j)=1\mid\mathcal F_t)=q_j(Wz_t)_j+(1-q_j)(1-(Wz_t)_j).
\]
Define \(z_{t+1}=\frac{t}{t+1}z_t+\frac1{t+1}BI_{t+1}\). All entries remain in \([0,1]\). The theorem assumes \(P=BW\) irreducible; neither factor need be irreducible, primitive, symmetric, or a permutation. The sampling indicators must be conditionally independent. The initial vector is deterministic and strictly interior. The result does not assert a density or closed-form law for \(\xi\).

## Proof
**Step 1: Drift and the path-balance equivalence.** Put \(x_t=z_t-\frac12\mathbf1\). Since \(B\) and \(W\) are row-stochastic, with \(S=\operatorname{diag}(s_j)\) and \(R=BSW\), conditional expectation gives
\[
\mathbb E[x_{t+1}\mid\mathcal F_t]=x_t+\gamma_t(R-I)x_t,\qquad \gamma_t=(t+1)^{-1}.
\]
Every \(R\)-eigenvalue has modulus at most one, since \(|R|\le BW=P\) entrywise. We show \(1\) is an eigenvalue precisely under balance. If \(Ru=u\) for some nonzero complex vector, let \(M=\max_i|u_i|\) and choose a vertex attaining this maximum. The convexity chain
\[
M=|u_i|\le\sum_{j,k}B_{ij}W_{jk}|s_j||u_k|\le\sum_{j,k}B_{ij}W_{jk}M=M
\]
forces modulus-one labels and phase equality on every two-step path leaving that vertex. As \(P\) is irreducible, equality propagates to every vertex and every occurring triple: \(u_i=s_ju_k\), with all \(|u_i|=M\). Fixing a reference vertex, all coordinates are its common complex phase multiplied by real signs, yielding \(h\in\{\pm1\}^n\). Conversely, balance gives \(Rh=h\) directly. Directed-walk sign balance is equivalent by transporting \(h\) along paths from one root, using irreducibility to close any two paths by a return walk; inconsistency is then a negative signed closed walk. In particular, \(R-I\) is Hurwitz whenever balance fails, since no eigenvalue is \(1\) and all eigenvalues satisfy modulus at most one.

**Step 2: Almost-sure deterministic convergence when unbalanced.** Write \(\eta_{t+1}=B(I_{t+1}-\mathbb E[I_{t+1}\mid\mathcal F_t])\). These are bounded martingale differences. With \(A=R-I\) Hurwitz, the positive-definite matrix
\[
H=\int_0^\infty e^{A^{\mathsf T}u}e^{Au}\,du
\]
is finite and satisfies \(A^{\mathsf T}H+HA=-I\). For \(V_t=x_t^{\mathsf T}Hx_t\), the exact quadratic expansion and boundedness give a deterministic \(K<\infty\) such that
\[
\mathbb E[V_{t+1}\mid\mathcal F_t]\le V_t-\gamma_t\|x_t\|_2^2+K\gamma_t^2.
\]
Adding the summable tail \(K\sum_{u\ge t}\gamma_u^2\) makes a nonnegative supermartingale. Thus \(V_t\) converges almost surely and \(\sum_t\gamma_t\|x_t\|_2^2<\infty\). Since \(\sum_t\gamma_t=\infty\) and \(V_t\) is norm-equivalent to \(\|x_t\|_2^2\), its limit must be zero. Hence \(z_t\to\frac12\mathbf1\) almost surely.

**Step 3: Exact gauge transformation under balance.** Fix balanced \(h\) and define \(y_t(i)=\frac12+h_i(z_t(i)-\frac12)\). For every active observation vertex \(j\) (some \(B_{ij}>0\)), all its recipient indices have the same sign \(r_j=h_i\), and every \(k\) with \(W_{jk}>0\) satisfies \(h_k=r_js_j\). Define \(C_{t+1}(j)=I_{t+1}(j)\) when \(r_j=1\), and \(1-I_{t+1}(j)\) when \(r_j=-1\). Then
\[
\mathbb E[C_{t+1}(j)\mid\mathcal F_t]=(Wy_t)_j,
\qquad y_{t+1}=y_t+\gamma_t(BC_{t+1}-y_t).
\]
Inactive observations have zero columns in \(B\), and can be defined arbitrarily. Conditional independence is preserved by complementation. Consequently the gauged process is an ordinary **nonnegative** two-layer reinforced Bernoulli system, with mean drift \((P-I)y_t\).

**Step 4: Martingale consensus.** Irreducibility gives the unique strictly positive stationary \(\pi\), \(\pi P=\pi\), \(\sum_i\pi_i=1\). Therefore \(m_t=\pi y_t\) is a bounded martingale and converges almost surely and in \(L^2\) to \(\xi\in[0,1]\). Write \(v_t=y_t-m_t\mathbf1\), so \(\pi v_t=0\). On this invariant subspace, all eigenvalues of \(P-I\) have strictly negative real parts: the eigenvalue \(1\) of irreducible \(P\) is simple, and any other eigenvalue has real part less than one, even if \(P\) is periodic. The projected recursion has bounded martingale-difference noise. The Lyapunov/supermartingale argument of Step 2, restricted to this subspace, proves \(v_t\to0\) almost surely. Thus \(y_t\to\xi\mathbf1\) and the claimed inverse-gauge limit follows.

**Step 5: Strict nondegeneracy and numerical constant.** Write \(\alpha_j=\sum_i\pi_iB_{ij}\). Independence of the fresh Bernoulli indicators gives the conditional martingale-increment variance
\[
\operatorname{Var}(m_{t+1}-m_t\mid\mathcal F_t)
=\gamma_t^2\sum_j\alpha_j^2p_j(t)(1-p_j(t)),
\]
where \(p_j(t)=\Pr(I_{t+1}(j)=1\mid\mathcal F_t)\); complementation does not alter variance. Orthogonality of martingale increments and \(m_t\to\xi\) in \(L^2\) imply
\(\operatorname{Var}(\xi)\ge\operatorname{Var}(m_1-m_0)\), giving the claimed lower bound because \(\gamma_0=1\). Each \(p_j(0)\) lies strictly between zero and one, and \(\sum_j\alpha_j=1\), so the lower bound is strictly positive. In the displayed four-state example, direct multiplication yields \(P_{ik}=1/4\), \(R=\operatorname{diag}(h)P\operatorname{diag}(h)\), \(\pi_i=\alpha_j=1/4\), and \(p_j(0)=1/2\); hence \(\sum_j\alpha_j^2p_j(0)(1-p_j(0))=1/16\). This completes the proof.

## Verification
A standalone Python script `verify.py` checks the path-support criterion against exact rational ranks of \(I-B\operatorname{diag}(s)W\) for 1,367 reproducibly selected irreducible small networks with \(n\in\{2,3,4\}\), verifies gauge identities, and checks the four-state strict-positivity and \(1/16\) variance certificate exactly. These finite calculations check algebra and the example; the almost-sure claims follow from the preceding proof, not finite sampling.

## Relationship to prior work
Dahiya, Kaur and Sahasrabudhe (2026), Theorem 3.1, proves deterministic convergence when the full matrix drift is invertible; their graph-theoretic tests in Section 3.2 impose coincident interaction edges, while their Section 4 treats the random regime under additional partition assumptions. The present claim gives an **if and only if signed-path condition** for arbitrary distinct nonnegative row-stochastic sampling and reinforcement matrices when their product is irreducible, and proves nondegeneracy of the random alternative. Kaur and Sahasrabudhe (2025) classify one-network node-dependent urns, including signed cycle cases; that does not describe two-layer path signs with different sender and recipient patterns. Classical signed-matrix balance and ordinary stochastic approximation supply proof techniques, but do not by themselves state the stochastic dichotomy or the strictly positive primitive-mixing polarization example.

## Limitations
Irreducibility of the unsigned product is essential to this exact two-alternative formulation; reducible products can support multiple limiting martingales. The result concerns critical nonnegative row-stochastic reinforcement, conditionally independent Bernoulli observations, and deterministic strictly interior initial data. It makes no claim about general affine signed edge reinforcement, non-independent noise, convergence rates, limit densities, or independent external validation. The classification is not asserted to solve every case of the broader 2026 model.

## References
1. Y. Dahiya, G. Kaur and N. Sahasrabudhe, *Interacting Stochastic Systems with Agent-Based Sampling and Connection-Based Reinforcement*, arXiv:2610.13884 (first public October 9, 2026), Sections 2–4 and 7.
2. G. Kaur and N. Sahasrabudhe, *Interacting urns on directed networks with node-dependent sampling and reinforcement*, Journal of Applied Probability 62 (2025), 972–996, DOI:10.1017/jpr.2024.105, Sections 3 and 5.
3. P. Dai Pra, P.-Y. Louis and I. G. Minelli, *Synchronization via interacting reinforcement*, Journal of Applied Probability 51 (2014), 556–568, arXiv:1603.01849 (nonnegative mean-field synchronization).
