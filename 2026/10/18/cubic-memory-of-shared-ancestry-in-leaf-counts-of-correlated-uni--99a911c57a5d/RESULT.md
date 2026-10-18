# Cubic memory of shared ancestry in leaf counts of correlated uniform-attachment trees

## Finding

Two random recursive trees are grown together for an initial segment and independently afterward. Their *unrooted degree-one leaf counts* retain a surprisingly sharp and quantifiable trace of the shared history.

For integers \(n\ge 4\) and \(2\le t\le n\), let \(L_n^{(1)}\) and \(L_n^{(2)}\) be the two final leaf counts, coupled as specified below. Both have mean \(\mu_n=n/2+1/(n-1)\) and variance \(v_n=n/12-1/(n-1)^2\). Their covariance and Pearson correlation are exactly
\[
\operatorname{Cov}(L_n^{(1)},L_n^{(2)})=
\begin{cases}
0,&2\le t\le 3,\\
\dfrac{t(t-1)^2-12}{12(n-1)^2},&4\le t\le n,
\end{cases}
\qquad
\operatorname{Corr}(L_n^{(1)},L_n^{(2)})=
\begin{cases}
0,&2\le t\le 3,\\
\dfrac{t(t-1)^2-12}{n(n-1)^2-12},&4\le t\le n.
\end{cases}
\]
The leaf counts are independent exactly when \(t\le3\). If \(t\ge4\), they are strictly positively correlated, and they satisfy **positive association across the pair**: for arbitrary nondecreasing functions \(f,g\) on the integer leaf-count range,
\[
\operatorname{Cov}(f(L_n^{(1)}),g(L_n^{(2)}))\ge0.
\]
For any sequence of common-history lengths \(t_n\) with \(t_n/n\to\alpha\in[0,1]\), the centered pair has the joint limit
\[
\frac{(L_n^{(1)}-\mu_n,L_n^{(2)}-\mu_n)}{\sqrt{n/12}}
\ \Longrightarrow\
\mathcal N_2\!\left(0,\begin{pmatrix}1&\alpha^3\\\alpha^3&1\end{pmatrix}\right).
\]
The Gaussian may be singular when \(\alpha=1\). Consequently the joint above-mean probability has the explicit limit
\[
\lim_{n\to\infty}\Pr\{L_n^{(1)}>\mu_n,\ L_n^{(2)}>\mu_n\}
=\frac14+\frac{\arcsin(\alpha^3)}{2\pi}.
\]
In particular, the limiting Pearson correlation is the **cube of the proportion of shared growth**.

## Assumptions and scope

Start with the fixed edge joining vertices \(1,2\). At each integer size \(m=2,3,\ldots,n-1\), the vertex \(m+1\) attaches to a uniformly random vertex of \(\{1,\ldots,m\}\), producing a random recursive (uniform-attachment) tree. The two trees make exactly the same attachments while their common size is at most \(t\), then independently sample all further attachments, conditional on the common tree at size \(t\). Here \(n\ge4\), \(t\in\{2,\ldots,n\}\). The scalar \(L_m\) counts vertices of **undirected degree exactly one**, including the root if it has degree one; it is not a count of vertices with zero offspring. All events and covariances are with respect to the described joint sampling law. The joint central limit assertion allows any deterministic sequence \(2\le t_n\le n\).

## Proof

**1. A closed leaf-count Markov chain.** At size \(m\ge2\) a new vertex is a leaf; the parent ceases to be a leaf precisely when it was already a leaf. Thus, conditional on \(L_m=k\),
\[
L_{m+1}=k+1-B_{m+1},\qquad
\Pr\{B_{m+1}=1\mid L_m=k\}=k/m.
\]
This transition depends on the tree only through its leaf count. Consequently \(\mathbb E[L_{m+1}\mid L_m]=1+(1-1/m)L_m\). Starting with \(L_2=2\), induction gives \(\mu_m=m/2+1/(m-1)\) for every \(m\ge2\). Write \(v_m=\operatorname{Var}(L_m)\). The law of total variance gives
\[
v_{m+1}=\left(1-\frac2m\right)v_m+\frac14-\frac1{m^2(m-1)^2}.
\]
Since \(L_3=2\) deterministically, \(v_3=0\). Direct substitution and induction yield \(v_m=m/12-1/(m-1)^2\) for all \(m\ge3\) (the exceptional initial variance is \(v_2=0\)). The variance is strictly positive when \(m\ge4\).

**2. Conditional regression and exact covariance.** Iterating the conditional-mean recursion, for every \(2\le t\le n\),
\[
\mathbb E[L_n\mid T_t]=\mathbb E[L_n\mid L_t]
=\frac n2+\frac{t-1}{n-1}\left(L_t-\frac t2\right).
\]
The future branches are conditionally independent given \(T_t\). By total covariance,
\[
\operatorname{Cov}(L_n^{(1)},L_n^{(2)})
=\operatorname{Var}\bigl(\mathbb E[L_n\mid T_t]\bigr)
=\left(\frac{t-1}{n-1}\right)^2v_t.
\]
Inserting \(v_2=v_3=0\) and the exact formula for \(v_t\) at \(t\ge4\) proves both displayed rational expressions. When \(t\le3\), the conditional distribution of \(L_n\) depends only on deterministic \(L_t\), so the two final counts are actually independent. For \(t\ge4\) the covariance is positive since \(v_t>0\), excluding independence. At \(t=n\) the two counts coincide, recovering correlation one.

**3. Positive association of the two counts.** Couple leaf-count chains starting from \(k\le\ell\) at common size \(m\) with identical independent uniform variables \(U\) by the update \(x\mapsto x+1-\mathbf1\{U\le x/m\}\). This map preserves the integer order, including the case \(\ell=k+1\). Therefore the conditional expectations \(h_f(k)=\mathbb E[f(L_n)\mid L_t=k]\) and \(h_g(k)\) are nondecreasing. Conditional independence reduces the desired covariance to \(\operatorname{Cov}(h_f(L_t),h_g(L_t))\). With an independent copy \(L_t'\), twice this covariance equals
\[
\mathbb E\big[(h_f(L_t)-h_f(L_t'))(h_g(L_t)-h_g(L_t'))\big]\ge0.
\]
No claim of joint association of all vertex-degree indicators is made.

**4. Bivariate central limit theorem.** Put \(W_m=L_m-\mu_m\), and let \(\xi_{m+1}=L_m/m-B_{m+1}\) be the bounded, conditionally mean-zero noise. Then
\[
W_{m+1}=\frac{m-1}{m}W_m+\xi_{m+1},\qquad
W_n=\sum_{m=3}^{n-1}\frac{m}{n-1}\xi_{m+1}
\]
because \(W_3=0\). Both coordinate martingale increments are identical before the common-history cutoff and conditionally independent after it. For every \(m\ge3\), the exact moments from Step 1 imply
\[
\mathbb E\left[\left(\frac{L_m}{m}-\frac12\right)^2\right]=\frac1{12m},
\qquad
\mathbb E\left[\frac{L_m}{m}\left(1-\frac{L_m}{m}\right)\right]=\frac14-\frac1{12m}.
\]
For any fixed linear combination of the two normalized sums, the predictable quadratic variation converges in probability to \(a^2+b^2+2ab\alpha^3\), because the diagonal conditional variance sums are asymptotic to \(n/12\), and the off-diagonal sum comes exclusively from the shared increments \(m<t_n\):
\[
\frac{12}{n(n-1)^2}\sum_{m=3}^{t_n-1}\frac{m^2}{4}
\longrightarrow\alpha^3.
\]
The difference between each quadratic-variation sum and its constant-\(1/4\) approximation tends to zero in \(L^1\), by the bound \(\mathbb E[(L_m/m-1/2)^2]=1/(12m)\); the bound is \(O(1/n)\) after normalization. The largest normalized martingale increment is \(O(n^{-1/2})\), so conditional Lindeberg holds. The martingale central limit theorem and Cramér--Wold give the asserted bivariate Gaussian limit, including zero-variance linear combinations at \(\alpha=1\).

**5. Quadrant probability.** The limiting Gaussian has continuous nondegenerate one-dimensional marginals, hence no mass on either coordinate axis. Weak convergence passes to the positive quadrant. The elementary bivariate-normal orthant identity \(\Pr(Z_1>0,Z_2>0)=1/4+\arcsin(\rho)/(2\pi)\), valid by continuity also at \(\rho=1\), proves the final formula.

## Verification

The self-contained `verify.py` uses rational arithmetic and no nonstandard dependencies. It exhaustively generates all uniform-attachment trees up to size eight and independently checks the Markov-chain leaf distributions. It then builds exact bivariate distributions for every \(2\le t\le n\le16\) and verifies the covariance, mean, variance, independence boundary, and all nondecreasing upper-tail indicator covariance inequalities. Large-parameter deterministic checks validate the correlation formula and its cubic limit. This finite verification supplements the analytical argument above; it cannot establish the infinite quantifiers or normal limit by itself.

## Relationship to prior work

Rácz and Sridhar [1] introduced the shared-growth-then-independent uniform-attachment coupling and studied detection and estimation of the common-history length using graph-level statistics (notably subtree and balancedness statistics). The present theorem evaluates the complete second-order dependence of the much simpler *unrooted leaf-count pair*, proves positive two-coordinate dependence, and identifies its cubic Gaussian memory law. The same shared-history model alone does not imply these formulas without the leaf-count transition and moment analysis.

Bäumler, Rácz, Ross and Sridhar [2] analyze a different coupling that correlates attachments throughout growth at a fixed per-step rate; their Appendix A contains a bivariate leaf-count Gaussian limit for **that different coupling**. It does not yield the present shared-prefix covariance formula, and [2] is later than the anchor source [1]. Marginal degree-count limit theory, including Janson [3], supports the plausibility of the univariate Gaussian scaling but does not establish the present two-tree law. Similar-looking second-moment formulas in the literature may be implicitly reducible to the present result; historical-priority assurance is not claimed.

## Limitations

The theorem concerns the particular deterministic two-vertex seed, the undirected degree-one count and a shared-prefix growth coupling, not preferential attachment or a coupling with correlated decisions at every time. The exact scalar independence boundary does not imply independence of the *trees*: graph structure can carry common ancestry undetected by leaf counts. A fixed positive shared-prefix length produces only \(O(n^{-3})\) leaf-count correlation; this does not imply that all tree-level detection tests lose power. The Gaussian limit describes macroscopic shared-history fractions, not a sharp total-variation detection threshold for sublinear \(t_n\). This work is self-reviewed and has not received an independent mathematical audit.

## References

[1] M. Z. Rácz and A. Sridhar, *Correlated randomly growing graphs*, arXiv:2004.13537v1, first submitted April 28, 2020. https://arxiv.org/abs/2004.13537

[2] J. Bäumler, M. Rácz, N. Ross and A. Sridhar, *Correlated uniform attachment trees*, arXiv:2606.02472v1, June 2026. https://arxiv.org/abs/2606.02472

[3] S. Janson, *Asymptotic degree distribution in random recursive trees*, Random Structures & Algorithms (2005), DOI: 10.1002/rsa.20046.
