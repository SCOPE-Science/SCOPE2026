# Sharp phase optimization of pairwise entanglement in complete tripartite weighted graph states

## Finding
For each integer \(c\ge1\) and real edge phase \(\theta\), the state on the complete tripartite graph \(K_{1,1,c}\) is
\[
|\Psi_{c,\theta}\rangle=\prod_{\{i,j\}\in E(K_{1,1,c})}e^{-i\theta Z_i Z_j/2}|+\rangle^{\otimes(c+2)}.
\]
Let \(A,B\) be its two singleton vertices, and \(\rho_{AB}\) the two-qubit state after tracing the remaining \(c\) vertices. With negativity normalized as \(\mathcal N=(\|\rho_{AB}^{T_B}\|_1-1)/2\), put \(x=\cos^c\theta\) and \(y=\cos^c(2\theta)\). Then
\[
\mathcal N_c(\theta)=\frac{\sqrt{(1-y)^2+16x^2\sin^2\theta}-(1-y)}8.
\]
For finite \(c\), this is strictly positive exactly when \(\sin\theta\cos\theta\ne0\).

Let \(M_c=\max_{\theta\in\mathbb R}\mathcal N_c(\theta)\), and for each maximizing \(\theta_c\) let \(\vartheta_c=\operatorname{dist}(\theta_c,\pi\mathbb Z)\in[0,\pi/2]\). For every \(c\ge1\), \(0<M_c<1/(2c)\), and \(M_1=1/6\), attained at \(\sin^2\vartheta_1=1/3\). Moreover,
\[
M_c=\frac1{2c}-\frac{3^{2/3}}{4c^{5/3}}+o(c^{-5/3}),\qquad
c^{2/3}\vartheta_c\longrightarrow3^{1/6}.
\]
Thus the optimal phase shrinks at a different rate from the optimized entanglement itself.

## Assumptions and scope
The graph is precisely \(K_{1,1,c}\), including the direct edge between its singleton vertices and the \(2c\) edges to the third part. All Ising gates use the same real phase, in the normalization \(e^{-i\theta ZZ/2}\); all qubits start in \(|+\rangle\). The source's three Pauli axes, one per vertex part, can be mapped to \(Z\) by a tensor product of single-qubit unitaries, provided the initial single-site states are equatorial relative to their interaction axes. Hence the stated negativity is also a local-unitarily invariant specialization of the tripartite graph-state architecture in the cited source. There is no assertion for generic input states, nonuniform phases, or other tripartite graphs.

## Proof
**Partial trace and exact spectrum.** In the \(Z\)-basis, label the eigenvalues on \(A,B\) by \(s,t\in\{+1,-1\}\). Let \(S\) be the sum of \(c\) independent symmetric signs. The conditional phase from the remaining vertices is \(e^{-i\theta(s+t)S/2}\). Its character averages are \(\mathbb E[e^{i\theta S}]=x\) and \(\mathbb E[e^{2i\theta S}]=y\). The matrix entries of the reduced density operator are therefore
\[
\langle st|\rho_{AB}|s't'\rangle=\frac14 e^{-i\theta(st-s't')/2}\left[\cos\!\left(\frac\theta2(s+t-s'-t')\right)\right]^c.
\]
A diagonal two-qubit unitary removes the direct-edge phase before partial transposition, but is not local; instead retain that phase and diagonalize the actual partial transpose. Exchange symmetry splits it into two real two-dimensional invariant sectors after harmless basis rephasings. Their eigenvalues are
\[
\lambda^{(1)}_{\pm}=\frac{1-y\pm\sqrt{(1-y)^2+16x^2\sin^2\theta}}8,
\qquad
\lambda^{(2)}_{\pm}=\frac{3+y\pm\sqrt{(1-y)^2+16x^2\cos^2\theta}}8.
\]
The second pair is nonnegative: \(\mathbb E\cos^2(\theta S)=(1+y)/2\ge x^2\), so \(x^2\cos^2\theta\le(1+y)/2\), which is equivalent to \(\lambda^{(2)}_-\ge0\). Because \(1-y\ge0\), the first minus eigenvalue is negative exactly when \(x\sin\theta\ne0\). It is the only negative eigenvalue, proving the closed expression and the strict-positivity criterion.

**Finite-size upper bound.** By periodicity/reflection take \(0\le\theta\le\pi/2\), and let \(p=\sin^2\theta\), \(q=1-p\), \(A=1-(1-2p)^c\), \(v=pq^c\). Squaring the expression, and choosing its nonnegative root, gives the exact quadratic
\[
4\mathcal N_c^2+A\mathcal N_c=v.
\]
For \(0<p<1\), the odd-binomial identity yields
\[
\frac A2=\sum_{j\text{ odd}}\binom cj p^j q^{c-j}
=cpq^{c-1}(1+R_c),\quad
R_c=\sum_{\substack{j\ge3\\j\text{ odd}}}\frac{\binom cj}{c}\left(\frac pq\right)^{j-1}\ge0.
\]
Consequently \(\mathcal N_c<v/A=q/[2c(1+R_c)]<1/(2c)\); at the endpoints the negativity is zero. For \(c=1\), inserting \(\mathcal N=1/6\) into \(4\mathcal N^2+2p\mathcal N=p(1-p)\) yields the nonnegative difference \((p-1/3)^2\), proving its sharp maximum.

**Asymptotic expansion.** For \(\theta=zc^{-2/3}\), with \(z\) in any compact subset of \((0,\infty)\), binomial expansion uniformly gives
\[
p=z^2c^{-4/3}+O(c^{-8/3}),\quad
R_c=\frac{z^4}{6c^{2/3}}+O(c^{-4/3}),\quad
A=2z^2c^{-1/3}(1+o(1)).
\]
Set \(\mu=v/A=q/[2c(1+R_c)]\). From the exact quadratic, \(\mathcal N_c=\mu-4\mathcal N_c^2/A\); this identity and the displayed expansions imply, uniformly on such compact sets,
\[
\mathcal N_c(zc^{-2/3})=\frac1{2c}-c^{-5/3}\left(\frac{z^4}{12}+\frac1{2z^2}\right)+o(c^{-5/3}).
\]
The function \(F(z)=z^4/12+1/(2z^2)\) has its unique global minimum at \(z^6=3\), with value \(3^{2/3}/4\).

**No escaping maximizer.** Taking this trial value proves \(D_c:=1/(2c)-M_c=O(c^{-5/3})\). At a maximizing \(p_c\), \(M_c\le q_c/[2c(1+R_c)]\), so \(p_c\to0\) and \(R_c\to0\). The first term of \(R_c\) for \(c\ge3\) is \((c-1)(c-2)p_c^2/(6q_c^2)\). Since \(D_c\ge (p_c+R_c)/[2c(1+R_c)]\), it follows \(R_c=O(c^{-2/3})\), hence \(p_c=O(c^{-4/3})\). On the other hand, \(A_c\le2cp_c\), \(M_c\sim1/(2c)\), and \(D_c\ge\mu_c-M_c=4M_c^2/A_c\) force \(p_c\ge\mathrm{const}\,c^{-4/3}\). Thus the rescaled maximizing phase remains in a compact subset of \((0,\infty)\), where the uniform expansion and uniqueness of the minimizer force \(c^{2/3}\vartheta_c\to3^{1/6}\), and determine the claimed maximum expansion. These steps include all global maximizers, not merely locally selected critical points.

## Verification
Run `python verify.py` with Python 3 and NumPy 1.24 or later. The standalone program computes full state vectors and partial transposes for \(1\le c\le7\) at ten phases each; compares all four eigenvalues and the negativity formula; tests the odd-binomial identity for \(1\le c\le40\); checks the strict finite upper-bound numerically away from exact zeros; verifies the \(c=1\) optimum; and samples large-size maximizers after rescaling. It prints `VERIFY_OK 8211 checks`. This finite replay supports but is not the proof for arbitrary \(c\) or the asymptotic theorem.

## Relationship to prior work
Gnatenko [1] introduces general weighted tripartite graph states, derives single-qubit-versus-rest entanglement distances and two-point correlators including common-neighbor contributions. The full text and its triangle example do not state the two-terminal partial-transpose spectrum, global optimal negativity, or the fractional scaling laws above. Hein and collaborators [2] give general weighted graph-state reduced-state machinery: the partial trace itself is not claimed as new, and indeed this theorem specializes that framework. The substantive additional result is a closed partial-transpose entanglement law for this tripartite family together with a *global*, sharply corrected optimization and optimizer localization. Literature and database comparison did not locate an equivalent optimized asymptotic; implicit or unindexed prior coverage remains possible.

## Limitations
This is a two-terminal bipartite-negativity theorem for one specifically normalized and uniformly weighted family. It does not calculate genuine multipartite entanglement, arbitrary multipartite reductions, robustness to phase disorder, or an asymptotic theorem for different couplings. The supplied finite tests are not an infinite proof. No independent audit has been performed.

## References
[1] Kh. P. Gnatenko, “Entanglement of multi-qubit quantum graph states and studies structural properties of tripartite graphs with quantum computing,” arXiv:2604.27829, first publicly posted 30 April 2026. https://arxiv.org/abs/2604.27829 ; full paper https://arxiv.org/pdf/2604.27829 .

[2] M. Hein, W. Dür, J. Eisert, R. Raussendorf, M. Van den Nest, and H. J. Briegel, “Entanglement in Graph States and its Applications,” arXiv:quant-ph/0602096 (2006), Section 9.2 on weighted graph states and their reduced states. https://arxiv.org/abs/quant-ph/0602096 .
