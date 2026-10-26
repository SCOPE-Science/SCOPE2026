# Joint Gaussian–Poisson independence for bulk roots and rare long gaps in cyclic deposition

## Finding
For a uniformly random circular arrangement of \(K\) distinct priorities, let \(R_K\) be the number of strict cyclic local minima (roots), and let \(D_{i,K}\) count cyclically consecutive roots at distance \(i+1\). Put
\[
a_i=\frac{i2^{i+1}}{(i+1)(i+2)(i+4)i!},\qquad \lambda_K=Ka_{i(K)},\qquad S_K=\frac{R_K-K/3}{\sqrt{2K/45}}.
\]
For any integer sequence \(K\to\infty\), \(1\le i(K)\le K-4\), with \(\lambda_K\to\lambda\in(0,\infty)\),
\[
(S_K,D_{i(K),K})\ \Longrightarrow\ (Z,P_\lambda),\qquad Z\sim N(0,1),\quad P_\lambda\sim\operatorname{Poisson}(\lambda),\quad Z\perp P_\lambda.
\]
The genuinely joint assertion is asymptotic independence: the bulk Gaussian fluctuation and the rare, long-gap count retain no limiting dependence, even though both depend on the same random permutation.

There is also a finite-size mixed-test bound. Let \(\varepsilon_i=(2i+7)a_i+2(u_i+v_i)/a_i\), where \(u_i,v_i\) are the two neighboring joint-gap probabilities as in Matijasevick (Theorem 4.5). For \(K\ge2i+7\), any bounded Lipschitz real \(h\), and any set \(A\subseteq\mathbb Z_{\ge0}\),
\[
\begin{split}
&\left|\mathbb E[h(S_K)\mathbf 1_{\{D_{i,K}\in A\}}]-\mathbb Eh(S_K)\,\mathbb P\{P_{\lambda_K}\in A\}\right|\\
&\qquad\le \frac{2\lambda_K(i+6)}{\sqrt{2K/45}}\operatorname{Lip}(h)
+\lambda_K\varepsilon_i\Vert h\Vert_\infty,
\end{split}
\]
where \(P_{\lambda_K}\) denotes an independent Poisson variable of mean \(\lambda_K\). In the stated rare-gap regime the bound tends to zero.

## Assumptions and scope
The \(K\) priorities are independent with an arbitrary common continuous distribution; only their random relative order matters. Indices are read modulo \(K\). A root is a site whose priority is strictly smaller than the priorities at both adjacent sites. Consecutive roots are ordered around the cycle, including the wraparound. \(D_{i,K}\) counts their oriented cyclic gaps of precisely \(i+1\) lattice edges. The regime \(\lambda_K\to\lambda\in(0,\infty)\) necessarily has \(i(K)\to\infty\) and \(i(K)=(1+o(1))\log K/\log\log K\) by the explicit formula for \(a_i\). Hence \(K\ge2i(K)+7\) eventually. The result does not claim independence for fixed \(i\) or for gap counts with diverging mean.

## Proof
Write \(U_j\) for independent uniform priorities, \(\xi_j=\mathbf1\{U_j<\min(U_{j-1},U_{j+1})\}\), and \(Y_j\) for the indicator that \(j\) starts a gap of length \(g=i+1\) between consecutive roots. Then \(R_K=\sum_j\xi_j\) and \(D_{i,K}=\sum_j Y_j\). The indicator \(Y_j\) is measurable with respect to the priority block \(W_j=\{j-1,\ldots,j+i+2\}\) of length \(i+4\), and \(\mathbb EY_j=a_i\). Set \(N_j=\{k:d_K(k,j)\le i+3\}\) (size \(2i+7\) when \(K\ge2i+7\)). For \(k\notin N_j\), the windows of \(Y_j,Y_k\) are disjoint.

Let \(L_j=\{j-2,\ldots,j+i+3\}\) of cardinality \(i+6\), and define
\[
S_j=\frac1{\sqrt{2K/45}}\sum_{k\notin L_j}(\xi_k-1/3),\qquad D_j=\sum_{k\notin N_j}Y_k.
\]
The pair \((S_j,D_j)\) depends only on priorities outside \(W_j\), so is independent of \(Y_j\). Deterministically, \(|S_K-S_j|\le(i+6)/\sqrt{2K/45}\) and \(D_{i,K}-D_j=\sum_{k\in N_j}Y_k\).

Fix \(A\subseteq\mathbb Z_{\ge0}\), let \(g_A(k)=\mathbf1\{k\in A\}\), and take the bounded solution \(f\) of the Poisson Stein equation
\[
\lambda_K f(k+1)-k f(k)=g_A(k)-\mathbb E g_A(P_{\lambda_K}).
\]
Standard indicator-test Stein factors give \(\Vert f\Vert_\infty\le1\) and \(\Vert\Delta f\Vert_\infty\le1\), where \(\Delta f(k)=f(k+1)-f(k)\). Multiplying the equation by \(h(S_K)\), summing over \(Y_j\), and inserting the independent deleted pair \((S_j,D_j)\), the common term \(a_i\mathbb E[h(S_j)f(D_j+1)]\) cancels with \(\mathbb E[Y_jh(S_j)f(D_j+1)]\). Bounding the two errors from \(h(S_K)-h(S_j)\), and the changes of \(f\) due to neighboring \(Y\)-variables, yields
\[
\begin{split}
&\left|\mathbb E h(S_K)\bigl(g_A(D_{i,K})-\mathbb Eg_A(P_{\lambda_K})\bigr)\right|\\
&\le 2Ka_i\Vert f\Vert_\infty\operatorname{Lip}(h)\frac{i+6}{\sqrt{2K/45}}\\
&\quad+\Vert h\Vert_\infty\Vert\Delta f\Vert_\infty\left[K(2i+7)a_i^2+\sum_j\sum_{k\in N_j\setminus\{j\}}\mathbb E(Y_jY_k)\right].
\end{split}
\]
There are exactly four potentially co-occurring distinct offsets: \(\pm(i+1)\) and \(\pm(i+3)\). Their joint probabilities are \(u_i,v_i\) respectively (Matijasevick, Lemma 2.3 and Theorem 4.5). Consequently the double sum is \(2K(u_i+v_i)\). This proves the stated finite-size bound since \(Ka_i=\lambda_K\).

For completeness, \(\xi_j-1/3\) is a centered bounded 2-dependent stationary array with \(\operatorname{Var}R_K=2K/45\) for \(K\ge5\). Its fixed-order joint cumulants vanish for disconnected dependency graphs. The number of connected \(r\)-tuples is \(O_r(K)\), so the normalized cumulants of order \(r\ge3\) are \(O_r(K^{1-r/2})\). The variance is exactly one; the method of moments gives \(S_K\Rightarrow N(0,1)\). The cited original sources also prove this classical root-count CLT.

The formula for \(a_i\) implies \(i(K)=o(\sqrt K)\) and \(i(K)\to\infty\). Matijasevick's exact neighboring probabilities give \(u_i\sim(i/4)a_i^2\), \(v_i\sim a_i^2\), hence \(\varepsilon_i\sim(5/2)ia_i\to0\). The mixed-test bound therefore tends to zero. For bounded Lipschitz \(h\) and each integer \(k\), taking \(A=\{k\}\) gives
\[\mathbb E[h(S_K)\mathbf1\{D_{i(K),K}=k\}]\to\mathbb E[h(Z)]\mathbb P(P_\lambda=k).\]
The Poisson marginal is tight, so summing over bounded-support tests and taking tails establishes joint weak convergence with independence.

## Verification
The finite permutation verifier `verify.py` exhaustively enumerates all \(7!+8!=45{,}360\) arrangements, checking the root mean, root variance, gap-count expectation for every \(1\le i\le K-4\), and the deterministic cyclic gap conservation identities. It passes. These are checks of definitions and exact finite moments, not substitutes for the infinite proof. The substantive independence assertion follows analytically from the cancellation and the published local overlap probabilities.

## Relationship to prior work
Matijasevick (2026), arXiv:2610.21094v1, proves the Gaussian root-count limit and, separately, a marginal Poisson approximation for the growing single-gap count with explicit \(\varepsilon_i\). Its Theorems A–D and Sections 6–7 do not assert their joint independence or the mixed-test inequality. Mansour, Rastegar and Roitershtein (2019), arXiv:1903.12548v2, provide earlier root-count and fixed-length gap results, not this growing-gap joint law. General mixed Poisson–Gaussian theory exists (e.g. Bourguin and Peccati, 2012, arXiv:1209.3098), but that paper concerns Poisson-space functionals and does not directly verify these cyclic priority-pattern hypotheses. The contribution is the explicit model-specific joint limit and quantitative bound.

## Limitations
The result is asymptotic and concerns the specific natural rare-gap scaling; it does not determine a process of all rare gaps, their spatial positions, or finite-size optimal constants. Broad unlocated joint limit theorems for growing permutation patterns may imply similar independence after separate checking. The review does not constitute independent validation or an assertion of publication priority.

## References
1. M. Matijasevick, *Gaps between roots in ballistic deposition on a strip: linear variance, Gaussian limits and a Poisson regime*, arXiv:2610.21094v1 (first publicly posted 2026-10-15), https://arxiv.org/html/2610.21094v1 .
2. T. Mansour, R. Rastegar and A. Roitershtein, *On ballistic deposition process on a strip*, arXiv:1903.12548v2 (2019), https://arxiv.org/html/1903.12548v2 .
3. S. Bourguin and G. Peccati, *Portmanteau inequalities on the Poisson space: mixed regimes and multidimensional clustering*, arXiv:1209.3098 (2012), https://arxiv.org/abs/1209.3098 .
