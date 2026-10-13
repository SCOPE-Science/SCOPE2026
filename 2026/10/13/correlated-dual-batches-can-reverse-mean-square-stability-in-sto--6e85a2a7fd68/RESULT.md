# Correlated dual batches can reverse mean-square stability in stochastic primal-dual hybrid gradient
## Finding
Consider stochastic primal-dual hybrid gradient (SPDHG) with two scalar dual blocks and identical per-block inclusion probabilities \(1/2\). Although these probabilities and the expected number of block updates are fixed, changing the joint selection law can reverse mean-square convergence on a strongly convex quadratic problem.

Set \(g(x)=x^2/20\), \(f_1(t)=f_2(t)=t^2/2\), \(A_1=A_2=1\), primal and dual step sizes \(\tau=\sigma_1=\sigma_2=1\), and extrapolation \(\theta=1\). At each iteration select a subset \(S\subseteq\{1,2\}\), independently across iterations, according to
\[
\Pr(S=\varnothing)=\Pr(S=\{1,2\})=q,\qquad
\Pr(S=\{1\})=\Pr(S=\{2\})=\tfrac12-q,
\qquad 0\le q\le\tfrac12.
\]
For every such law the marginal probability of selecting either individual block is \(1/2\), and \(\mathbb E|S|=1\). Nevertheless:

1. For every \(0\le q\le 1/100\), the entire primal-dual-extrapolation state converges to the unique saddle point \(0\) geometrically in mean square, from every finite initial state.
2. For every \(q\ge1/4\), with the legitimate initialization \(x_0=1\), \(y_{1,0}=y_{2,0}=0\), and \(\bar z_0=0\), and every integer \(k\ge1\),
\[
\mathbb E[x_k^2]\ge\left(\frac{25}{118}\right)^2(4q)^k.
\]
Thus mean-square convergence fails at \(q=1/4\) (independently included blocks) and exponential mean-square divergence holds for every \(q>1/4\); in particular fully synchronized empty/full selection \(q=1/2\) gives a lower bound proportional to \(2^k\).

This establishes an explicit, robust, fixed-marginal dependence obstruction. The statement does **not** claim that the interval between \(1/100\) and \(1/4\) is fully classified or that either endpoint is a sharp stability threshold.

## Assumptions and scope
All variables and computations are real and in exact arithmetic. The primal objective is
\[
F(x)=\sum_{i=1}^2 f_i(A_ix)+g(x)=\frac{21}{20}x^2,
\]
with unique minimizer \(0\) and unique dual saddle point \((0,0)\). The conjugates are \(f_i^*(y)=y^2/2\). The original dual-extrapolated SPDHG ordering updates the primal variable using the previous extrapolated dual vector, then the selected dual blocks, then the extrapolation. With \(\bar z_k=\bar y_{1,k}+\bar y_{2,k}\), the particular updates are
\[
\begin{aligned}
x_{k+1}&=\frac{10}{11}(x_k-\bar z_k),\\
\delta_{i,k}&=\begin{cases}(x_{k+1}-y_{i,k})/2,&i\in S_{k+1},\\0,&i\notin S_{k+1},\end{cases}\\
y_{i,k+1}&=y_{i,k}+\delta_{i,k},\\
\bar z_{k+1}&=y_{1,k}+y_{2,k}+3(\delta_{1,k}+\delta_{2,k}).
\end{aligned}
\]
Indeed the dual update is the proximal mapping of \(y^2/2\) at step size one, and the extrapolation coefficient for a selected block is \(1+\theta/p_i=3\). The initial extrapolation agrees with the unextrapolated initial dual variable. The probability law above includes correlated, independent, and serial block selection, always with independent sampling *across iterations*.

## Proof
Let \(v_k=(x_k,y_{1,k},y_{2,k},\bar z_k)^\mathsf T\). Put \(M_{ij}\) for the linear update when the two selection indicators equal \((i,j)\). Direct substitution gives
\[
M_{00}=\begin{pmatrix}
10/11&0&0&-10/11\\0&1&0&0\\0&0&1&0\\0&1&1&0
\end{pmatrix},\quad
M_{10}=\begin{pmatrix}
10/11&0&0&-10/11\\5/11&1/2&0&-5/11\\0&0&1&0\\15/11&-1/2&1&-15/11
\end{pmatrix},
\]
\[
M_{01}=\begin{pmatrix}
10/11&0&0&-10/11\\0&1&0&0\\5/11&0&1/2&-5/11\\15/11&1&-1/2&-15/11
\end{pmatrix},\quad
M_{11}=\begin{pmatrix}
10/11&0&0&-10/11\\5/11&1/2&0&-5/11\\5/11&0&1/2&-5/11\\30/11&-1/2&-1/2&-30/11
\end{pmatrix}.
\]
The first subscript denotes inclusion of block one, and the second inclusion of block two.

**Geometric convergence.** Define the rational symmetric matrix
\[
P=\frac1{933}\begin{pmatrix}
7233&620&620&-6300\\
620&13303&-7233&-620\\
620&-7233&13303&-620\\
-6300&-620&-620&7233
\end{pmatrix}.
\]
Its four leading principal minors are exactly
\[
\frac{2411}{311},\quad\frac{95836199}{870489},\quad
\frac{885830833360}{812166237},\quad
\frac{1655359932560}{812166237},
\]
so \(P\succ0\) by Sylvester's criterion. For every \(q\) define the deterministic second-moment Lyapunov slack
\[
H(q)=P-q(M_{00}^{\mathsf T}PM_{00}+M_{11}^{\mathsf T}PM_{11})
 -(\tfrac12-q)(M_{10}^{\mathsf T}PM_{10}+M_{01}^{\mathsf T}PM_{01}).
\]
Exact multiplication gives \(H(0)=I_4\). At \(q=1/100\), one obtains
\[
H(1/100)=\begin{pmatrix}
28607/37631&2256/17105&2256/17105&9024/37631\\
2256/17105&1&-1128/7775&-2256/17105\\
2256/17105&-1128/7775&1&-2256/17105\\
9024/37631&-2256/17105&-2256/17105&28607/37631
\end{pmatrix}.
\]
Its leading principal minors are
\[
\frac{28607}{37631},\quad\frac{217329889}{292581025},\quad
\frac{5152050361}{7314525625},\quad\frac{3143533561}{7314525625},
\]
all strictly positive. Because \(H(q)\) is affine in \(q\), the convexity of the positive-definite cone implies \(H(q)\succ0\) for every \(q\in[0,1/100]\). Independence across rounds then yields
\[
\mathbb E[v_{k+1}^{\mathsf T}Pv_{k+1}\mid v_k]
 =v_k^{\mathsf T}(P-H(q))v_k.
\]
The fixed positive-definite matrices \(P\) and \(H(q)\) furnish a contraction factor strictly below one, uniformly for this closed interval. Their norm equivalence implies geometric decay of \(\mathbb E\|v_k\|_2^2\).

**Failure under batching.** Start from \(v_0=(1,0,0,0)^\mathsf T\). On the event that \(S_1=\cdots=S_k=\{1,2\}\), write \(s=y_1+y_2\) and use the state \(w=(x,s,\bar z)^\mathsf T\). One full-batch step acts by
\[
B=\begin{pmatrix}
10/11&0&-10/11\\10/11&1/2&-10/11\\30/11&-1/2&-30/11
\end{pmatrix}.
\]
The characteristic polynomial has the distinct roots \(-2\), \(0\), and \(15/22\). More precisely, the corresponding eigenvectors can be chosen as \((5/16,1/4,1)^\mathsf T\), \((1,0,1)^\mathsf T\), and \((4,15,1)^\mathsf T\). The legitimate start decomposes exactly as
\[
w_0=-\frac{80}{59}\begin{pmatrix}5/16\\1/4\\1\end{pmatrix}
+\frac43\begin{pmatrix}1\\0\\1\end{pmatrix}
+\frac4{177}\begin{pmatrix}4\\15\\1\end{pmatrix}.
\]
Consequently, for every integer \(k\ge1\),
\[
x_k=-\frac{25}{59}(-2)^k+\frac{16}{177}\left(\frac{15}{22}\right)^k
\qquad\text{on the full-batch event}.
\]
The second term has magnitude at most \((25/118)2^k\), so \(|x_k|\ge(25/118)2^k\) on that event. Its probability is \(q^k\). Taking the nonnegative contribution of this single event to \(\mathbb E[x_k^2]\) proves the bound \((25/118)^2(4q)^k\). This proves both conclusions, without interpreting a finite simulation as an asymptotic proof.

## Verification
Run `python3 verify.py` with Python 3 and no third-party dependencies. The program reconstructs the four update matrices independently from the proximal recurrence; checks the exact rational \(P\), both Lyapunov slacks, and their leading principal minors; verifies a polynomial identity for the full-batch matrix; checks the exact trajectory formula; and compares 324 explicit rational one-step updates against their matrix representations. The finite loops are diagnostic. The proof of arbitrary-horizon convergence/divergence is the matrix-inequality and algebraic-event argument above, not the finite-loop count.

## Relationship to prior work
Chambolle, Ehrhardt, Richtárik, and Schönlieb introduced SPDHG with arbitrary i.i.d. subsets, probability-adjusted dual extrapolation, and expected-separable-overapproximation (ESO) *sufficient* conditions; their Algorithm 1 is used here. The two regimes here both use \(\tau\sigma_i\|A_i\|^2=1\) and \(p_i=1/2\), outside the source's usual sufficient condition \(v_i<p_i\), and no contradiction with its convergence theorem is claimed. Alacaoglu, Fercoq, and Cevher subsequently proved almost-sure and linear convergence under standard sufficient steps, principally with serial sampling. Gutierrez, Delplancke, and Ehrhardt extended arbitrary-sampling convergence under an operator-norm sufficient condition and compared practical sampling strategies. These findings do not by themselves determine the *opposite* mean-square outcomes of the two present laws at the stated common parameters. The specific fixed-marginal stability separation and its rational Lyapunov/path certificates are the proposed incremental result, not the algorithm or the general fact that sampling influences performance.

## Limitations
The statement concerns only two scalar dual blocks, exact quadratics, the original dual extrapolation at the specified constant steps, and i.i.d. selection across rounds. It does not supply a sharp threshold over the full interval \(1/100<q<1/4\), show almost-sure divergence, optimize work-normalized performance, or extend to nonlinear objectives or general MRI reconstruction. Because the chosen steps violate established sufficient bounds, the result should not be read as showing a failure of the published convergence theorems. An equivalent previously unindexed special-case counterexample could affect priority.

## References
1. A. Chambolle, M. J. Ehrhardt, P. Richtárik, and C.-B. Schönlieb, *Stochastic Primal-Dual Hybrid Gradient Algorithm with Arbitrary Sampling and Imaging Applications*, arXiv:1706.04957v1 (first posted 2017-06-15), SIAM J. Optim. 28 (2018), 2783–2808; DOI:10.1137/17M1134834. https://arxiv.org/abs/1706.04957 ; https://epubs.siam.org/doi/pdf/10.1137/17M1134834
2. A. Alacaoglu, O. Fercoq, and V. Cevher, *On the Convergence of Stochastic Primal-Dual Hybrid Gradient*, arXiv:1911.00799; SIAM J. Optim. 32 (2022), 1288–1318. https://arxiv.org/pdf/1911.00799
3. E. B. Gutierrez, C. Delplancke, and M. J. Ehrhardt, *On the convergence and sampling of randomized primal-dual algorithms and their application to parallel MRI reconstruction*, arXiv:2207.12291v1 (2022), subsequently published as *Randomized Primal-Dual Algorithm with Arbitrary Sampling*, J. Math. Imaging Vis. 67 (2025), article 25. https://arxiv.org/abs/2207.12291 ; https://link.springer.com/article/10.1007/s10851-025-01231-3
