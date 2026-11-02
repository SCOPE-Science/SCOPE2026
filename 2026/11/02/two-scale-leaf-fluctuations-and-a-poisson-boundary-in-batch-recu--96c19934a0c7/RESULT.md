# Two-scale leaf fluctuations and a Poisson boundary in batch-recursive trees

## Finding

Consider the random rooted tree which begins with one vertex, and at each of \(n\) successive rounds chooses one existing vertex uniformly and attaches \(m\) new leaf children to it. A birth cohort comprises the \(m\) vertices created in one round. Write \(L_n\) for the number of leaf vertices and \(C_n\) for the number of birth cohorts all of whose vertices remain leaves. In each row of the model, \(m\) is a fixed positive integer; it may depend on the final number \(n\) when a triangular limit is explicitly invoked.

The exact expectations, valid for every \(m,n\ge1\), are
\[
\mathbb E L_n=\frac{m(mn+1)}{m+1},\qquad
\mathbb E C_n=\frac n2+\frac{n}{2(m(n-1)+1)}.
\]

For every fixed \(m\ge1\), as \(n\to\infty\),
\[
\frac1{\sqrt n}\begin{pmatrix}L_n-\mathbb E L_n\\C_n-\mathbb E C_n\end{pmatrix}
\Longrightarrow N_2(0,\Sigma_m),\qquad
\Sigma_m=
\begin{pmatrix}
\frac{m^2}{(m+1)^2(m+2)}&\frac{m}{2(m+1)(2m+1)}\\
\frac{m}{2(m+1)(2m+1)}&\frac1{12}
\end{pmatrix}.
\]
The limiting correlation is \(\sqrt{3(m+2)}/(2m+1)\). When \(m=1\), the limit is singular because \(L_n=C_n\), as required by the definition.

If instead \(m=m_n\to\infty\) with \(m_n=o(n)\), then
\[
\left(\frac{L_n-\mathbb E L_n}{\sqrt{n/m_n}},
\frac{C_n-\mathbb E C_n}{\sqrt n}\right)
\Longrightarrow N(0,1)\otimes N(0,1/12).
\]
In particular, the two differently scaled fluctuations become independent, even though leaf and intact-cohort counts are positively correlated at every nontrivial finite size.

Define \(R_n=L_n-((m-1)n+1)\), the number of rounds after the first whose selected vertex already had children. For any \(m,n\ge1\),
\[
 d_{\mathrm{TV}}\left(\mathcal L(R_n),\operatorname{Pois}\!\left(\frac{n-1}{m+1}\right)\right)
 \le \frac{2n}{m(m+1)}+\frac{n}{m^2}.
\]
Thus when \(m_n/n\to c\in(0,\infty)\), \(R_n\Longrightarrow\operatorname{Pois}(1/c)\), with convergence in total variation; when \(m_n/n\to\infty\), \(R_n\to0\) in probability. This supplies a sharp Gaussian-to-Poisson crossover for the fluctuations of the leaf count. In both growing-\(m\) regimes, \((C_n-\mathbb E C_n)/\sqrt n\Longrightarrow N(0,1/12)\).

## Assumptions and scope

All recruiting choices are conditionally uniform over the current \(mt+1\) vertices at round \(t\), and no vertices or edges are ever removed. Distinct new vertices are individually recognizable, but their common birth round is retained as a cohort label. A cohort is counted by \(C_t\) only when every one of its \(m\) vertices has never itself recruited a later batch; its parent may have recruited other batches. Thus intact birth cohorts are not necessarily fringe-star subtrees. The first growth round is deterministic, leaving \(L_1=m\) and \(C_1=1\). \(m\) is constant within each run of \(n\) rounds. The Gaussian and Poisson limit regimes are as stated and no assertion about a uniform local limit theorem is made.

## Proof

**1. Exact two-coordinate dynamics.** At the end of round \(t\ge1\), put \(N_t=mt+1\). Let \(I_t\) indicate that the next recruiter is a leaf and \(J_t\) that it is a vertex belonging to an entirely intact birth cohort. Then \(J_t\le I_t\), and with \(\mathcal F_t\) the past,
\[
 p_t=\Pr(I_t=1\mid\mathcal F_t)=\frac{L_t}{N_t},\qquad
 q_t=\Pr(J_t=1\mid\mathcal F_t)=\frac{mC_t}{N_t}.
\]
All \(m\) newcomers are leaves; selecting a leaf destroys that leaf, and selecting a vertex in an intact cohort destroys precisely that cohort's intact status. Therefore
\[
L_{t+1}=L_t+m-I_t,\qquad C_{t+1}=C_t+1-J_t.
\]
The three exact transition probabilities are \(q_t\), \(p_t-q_t\), \(1-p_t\), corresponding respectively to increments \((m-1,0)\), \((m-1,1)\), and \((m,1)\). They sum to one and close the two-dimensional Markov state space. Taking expectations solves to the stated formulas, which also satisfy the initial values.

**2. Martingale decomposition and second moments.** Center both coordinates, \(X_t=L_t-\mathbb E L_t\), \(Y_t=C_t-\mathbb E C_t\), and define bounded centered increments \(\xi_t=p_t-I_t\) and \(\eta_t=q_t-J_t\). Then
\[
 X_{t+1}=\left(1-\frac1{N_t}\right)X_t+\xi_t,\qquad
 Y_{t+1}=\left(1-\frac m{N_t}\right)Y_t+\eta_t.
\]
The conditional increment covariance is
\[
\Gamma_t=\begin{pmatrix}p_t(1-p_t)&q_t(1-p_t)\\q_t(1-p_t)&q_t(1-q_t)\end{pmatrix},
\]
because \(I_tJ_t=J_t\). Let \(V^L_t=\operatorname{Var}(L_t)\), \(V^C_t=\operatorname{Var}(C_t)\), and \(K_t=\operatorname{Cov}(L_t,C_t)\). Writing \(\bar p_t=\mathbb E p_t=m/(m+1)\) and \(\bar q_t=\mathbb E q_t\), the law of total covariance gives the **exact** recurrences
\[
\begin{aligned}
V^L_{t+1}&=(1-2/N_t)V^L_t+\bar p_t(1-\bar p_t),\\
V^C_{t+1}&=(1-2m/N_t)V^C_t+\bar q_t(1-\bar q_t),\\
K_{t+1}&=(1-(m+1)/N_t)K_t+\bar q_t(1-\bar p_t).
\end{aligned}
\]
All three start from zero at \(t=1\). The coefficients of the covariance recurrence are nonnegative, and its forcing is positive, so \(K_t>0\) for \(t\ge2\). These recurrences show \(V^L_t\le tm/(m+1)^2\) and \(V^C_t\le t/4\) (for \(t\ge2\)); for the latter the coefficient at \(t=1\) can be negative, but the initial variance is zero, and all subsequent coefficients are nonnegative. Consequently \(p_t-\bar p_t\to0\) and \(q_t-1/2\to0\) in mean square as \(t\to\infty\), uniformly over integer \(m\ge1\): indeed, \(\operatorname{Var}(p_t)\le 1/[m(m+1)^2t]\), \(\operatorname{Var}(q_t)\le1/(4t)\), while
\[
\bar q_t-\tfrac12=\frac{m-1}{2(mt+1)(m(t-1)+1)}.
\]

**3. Fixed-\(m\) bivariate Gaussian law.** Iterating the centered recurrences gives martingale sums with deterministic weights
\[
w^L_{n,t}=\prod_{u=t+1}^{n-1}\left(1-\frac1{mu+1}\right),\qquad
w^C_{n,t}=\frac{mt+1}{m(n-1)+1},\quad 1\le t<n.
\]
For fixed \(m\), \(w^L_{n,\lfloor nx\rfloor}\to x^{1/m}\) and \(w^C_{n,\lfloor nx\rfloor}\to x\) for \(x\in(0,1)\). The covariance matrix \(\Gamma_t\) converges in probability, uniformly outside an initial \(o(n)\) interval, to
\[
\Gamma_{\infty,m}=\begin{pmatrix}
\frac m{(m+1)^2}&\frac1{2(m+1)}\\
\frac1{2(m+1)}&\frac14
\end{pmatrix}.
\]
Bounded increments yield the martingale-array Lindeberg condition. The predictable quadratic variation of the weighted, \(n^{-1/2}\)-normalized sum converges, entrywise, to \(\Gamma_{\infty,m}\) multiplied by integrals \(\int_0^1x^{2/m}\,dx=m/(m+2)\), \(\int_0^1x^{1+1/m}\,dx=m/(2m+1)\), and \(\int_0^1x^2\,dx=1/3\). Multivariate martingale convergence, including the singular \(m=1\) case by Cramér–Wold, gives exactly \(\Sigma_m\). Its displayed correlation follows by simplification.

**4. Growing-\(m\) Gaussian law.** Let \(m=m_n\to\infty\) and \(m=o(n)\). The first weight satisfies
\[
1-w^L_{n,t}\le \sum_{u=t+1}^{n-1}\frac1{mu+1}\le \frac{1+\log(n/t)}m,
\]
so it tends to one in averaged squares, while \(w^C_{n,\lfloor nx\rfloor}\to x\). The normalized martingale increment magnitudes are at most \(\sqrt{m/n}\) and \(1/\sqrt n\), which both vanish. The predictable quadratic variations converge respectively to \(1\) and \(1/12\): multiply the leaf conditional variance by \(m\), using \(m\bar p_t(1-\bar p_t)=m^2/(m+1)^2\to1\) and the uniform \(L^2\) concentration above. The normalized off-diagonal predictable variation vanishes, because \(\mathbb E[q_t(1-p_t)]\le\mathbb E(1-p_t)=1/(m+1)\), and its prefactor is only \(\sqrt m\). The multivariate martingale-array theorem therefore gives independent Gaussian limits. The same cohort argument works for every sequence \(m_n\to\infty\), without requiring \(m=o(n)\).

**5. Poisson crossover.** Put \(R_t=L_t-((m-1)t+1)\). It starts at \(R_1=0\), and exactly
\[
\Pr(R_{t+1}=R_t+1\mid R_t)=\frac{t-R_t}{mt+1},
\qquad \mathbb E R_n=\frac{n-1}{m+1}.
\]
Use independent uniforms to construct its successive Bernoulli increments together with independent \(B'_t\sim\operatorname{Bernoulli}(t/(mt+1))\), always taking the actual increment below \(B'_t\). Set \(S_n=\sum_{t=1}^{n-1}B'_t\). This coupling gives
\[
\Pr(R_n\ne S_n)\le\mathbb E(S_n-R_n)
=\sum_{t=1}^{n-1}\frac{\mathbb E R_t}{mt+1}
\le\frac n{m(m+1)}.
\]
Le Cam's independent-indicator inequality yields \(d_{\mathrm{TV}}(\mathcal L(S_n),\operatorname{Pois}(\mathbb E S_n))\le\sum_t(t/(mt+1))^2\le n/m^2\). The Poisson-mean distance is at most \(\mathbb E S_n-\mathbb E R_n\le n/[m(m+1)]\). Combining these three bounds proves the stated finite-size total-variation estimate. For \(m/n\to c\in(0,\infty)\), the mean \((n-1)/(m+1)\to1/c\) and the bound tends to zero. For \(m/n\to\infty\), Markov's inequality and the exact mean give the degenerate limit. This finishes all assertions.

## Verification

The independent Python 3 standard-library checker `CHECK.py` exhaustively evolves the exact rational law of \((L_n,C_n)\) for \(m=1,\ldots,6\) and \(n=1,\ldots,9\), cross-checks it against separately computed moment recurrences and both exact expectation formulas, and verifies finite covariance nonnegativity. It also checks limiting variance and correlation formulas at six fixed batch sizes, numerically tests three growing-batch covariance regimes, and compares exact finite Poisson-crossover probabilities against their coupling bound. The checker completed 1,955 assertions. Run `python3 CHECK.py`. These computations support finite algebra and numerical consistency; the infinite Gaussian and Poisson laws are proved in the preceding argument, not deduced from finite tests.

## Relationship to prior work

Bhutani, Kalpathy, Lesny, Mahmoud, and Neininger's 2026 paper introduces exactly this simultaneous-recruitment tree and analyzes depth, height, Wiener index, and total path length, but does not establish the joint law of leaves and intact birth cohorts. Desmarais and Holmgren's 2020 degree-count central limit theorem and the 2014 block-tree leaf theorem by Gopaladesikan, Mahmoud, and Ward cover related fixed-building-block degree or leaf marginals; they do not yield the intact birth-cohort count or the growing-batch Poisson transition as stated. The 2023 paper on \(m\)-ary hooking networks uses an outdegree-capacity parameter rather than the number of simultaneously introduced children; its theorem does not settle the present question. The 2017 general fringe-subtree CLT concerns subtree isomorphism counts in other random-tree models; an intact birth cohort here is not a fringe subtree because its parent may have other children. Existing general martingale central limit methods are used, not claimed as novel.

## Limitations

This is a result for uniformly chosen recruiters and deterministic equal-sized batches. It does not treat preferential recruitment, randomized batch sizes, a varying batch size *within* a single tree, joint Poisson/Gaussian coupling in the critical \(m\asymp n\) window, or sharper convergence rates for the Gaussian laws. Known fixed-block leaf central limit theorems overlap the leaf *marginal*; the combined cohort observable and triangular crossover are the contribution assessed here. The comparison with all historical general urn and fringe-tree theorems is not exhaustive, and independent mathematical and priority audits remain to be performed.

## References

1. K. Bhutani, R. Kalpathy, F. Lesny, H. Mahmoud, R. Neininger, *Distances in \(m\)-ary recursive trees*, arXiv:2609.33636 (first public 2026-09-27), https://arxiv.org/abs/2609.33636.
2. P. Desmarais and C. Holmgren, *Normal limit laws for vertex degrees in randomly grown hooking networks and bipolar networks*, Electronic Journal of Combinatorics (2020), https://doi.org/10.37236/9139.
3. M. Gopaladesikan, H. Mahmoud, M. D. Ward, *Building random trees from blocks*, Probability in the Engineering and Informational Sciences 28 (2014), 67–81, https://doi.org/10.1017/S0269964813000338.
4. K. Bhutani, R. Kalpathy, H. Mahmoud, *Degrees in random \(m\)-ary hooking networks*, arXiv:2308.03857, https://arxiv.org/abs/2308.03857.
5. C. Holmgren, S. Janson, M. Sileikis, *Multivariate normal limit laws for the numbers of fringe subtrees in \(m\)-ary search trees and preferential attachment trees*, arXiv:1603.08125, https://arxiv.org/abs/1603.08125.
