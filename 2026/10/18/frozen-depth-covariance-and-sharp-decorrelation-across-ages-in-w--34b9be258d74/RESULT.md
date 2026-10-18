# Frozen depth covariance and sharp decorrelation across ages in weighted recursive trees

## Finding

Fix arbitrary deterministic positive vertex weights \(w_1,w_2,\ldots\) and a label \(i\geq 3\). In the corresponding rooted weighted recursive tree, write \(D_m\) for the depth of vertex \(m\), \(W_k=\sum_{r=1}^{k}w_r\), and \(p_k=w_k/W_k\). Let \(X=D_i\), \(Y=D_{i+1}\). For **every** \(j\geq i+1\), there is a sum \(S_{i,j}=\sum_{k=i+1}^{j-1}B_k\) of mutually independent Bernoulli variables with \(\Pr(B_k=1)=p_k\), independent of \((X,Y)\), such that

\[
(D_i,D_j)\ \stackrel{d}{=}\ (X,Y+S_{i,j}). \tag{1}
\]

The empty sum for \(j=i+1\) is zero. In particular, the covariance is **strictly positive and exactly independent of the younger label**:

\[
\operatorname{Cov}(D_i,D_j)=C_i:=p_i v_i+\sum_{k=2}^{i-1}p_k^2v_k>0,\quad j>i, \tag{2}
\]

where \(v_k=\mathbb E[(D_{K_k}-A_{k-1}/W_{k-1})^2]\), \(K_k\) is the independently sampled parent of vertex \(k\), and \(A_m=\sum_{r\leq m}w_rD_r\). Each \(C_i\) is finite and depends only on the first \(i\) weights.

Define the distance from independent depths by

\[
\Delta_{i,j}=d_{\mathrm{TV}}\bigl(\mathcal L(D_i,D_j),\mathcal L(D_i)\otimes\mathcal L(D_j)\bigr),\qquad
V_{i,j}=\sum_{k=i+1}^{j-1}p_k(1-p_k),\tag{3}
\]

with the total-variation convention \(d_{\mathrm{TV}}(P,Q)=\sup_E|P(E)-Q(E)|\). For **every** deterministic positive weight sequence such that \(V_{i,j}\to\infty\),

\[
0<\frac{C_i}{(i-1)\sqrt{2\pi}}
\leq\liminf_{j\to\infty}\sqrt{V_{i,j}}\,\Delta_{i,j}
\leq\limsup_{j\to\infty}\sqrt{V_{i,j}}\,\Delta_{i,j}
\leq\frac{\sqrt\pi}{2\sqrt2}\,\mathbb E|Y-Y'|<\infty, \tag{4}
\]

where \(Y'\) is an independent copy of \(Y\). Thus the total-variation distance has the **sharp order** \(\Theta_i(V_{i,j}^{-1/2})\), even though the covariance stays equal to the nonzero constant \(C_i\).

For the natural power weights \(w_k=k^\alpha\), \(\alpha\in\mathbb R\), this produces a complete dependence phase diagram:

\[
\begin{array}{lll}
\alpha>-1:&\Delta_{i,j}=\Theta_i((\log j)^{-1/2}),\\
\alpha=-1:&\Delta_{i,j}=\Theta_i((\log\log j)^{-1/2}),\\
\alpha<-1:&\Delta_{i,j}\longrightarrow\Delta_{i,\infty}>0.
\end{array} \tag{5}
\]

In the last case, \(\Delta_{i,\infty}\) is precisely the distance between the joint and product laws of \((X,Y+S_{i,\infty})\), with \(S_{i,\infty}=\sum_{k=i+1}^{\infty}B_k<\infty\) almost surely, independent of \((X,Y)\). Equation (5) makes clear that nonvanishing covariance does not prevent asymptotic total-variation independence when the depth noise diverges.

## Assumptions and scope

Vertex 1 is the root, with \(D_1=0\). At each insertion \(m\geq2\), independently of earlier insertions, the new parent \(K_m\in\{1,\ldots,m-1\}\) is chosen with \(\Pr(K_m=r)=w_r/W_{m-1}\), and \(D_m=1+D_{K_m}\). All weights are deterministic, strictly positive and finite. There is no need for a regular-variation or summability assumption in (1)--(2). The two-label comparison always fixes the earlier label \(i\ge3\) and sends \(j\to\infty\). Constants in rate notation may depend on \(i\) and initial weights. For the unspecialized weight sequence, (4) requires variance divergence; when variance stays bounded, (4) is not claimed.

The statement concerns unconditional distributions of **depths of two labeled vertices**, not graph distance, degree, height, the tree profile or the global total path length.

## Proof

**1. Joint-depth convolution.** For formal \(u,z\) put \(F_{i,m}(u,z)=\mathbb E[u^{D_i}z^{D_m}]\), with the first label \(i\) fixed. For any \(m>i\), the choice \(K_m\) is independent of the tree on the previous vertices, so

\[
F_{i,m}(u,z)=\frac{z}{W_{m-1}}\sum_{r<m}w_rF_{i,r}(u,z).
\]

Set \(H_{i,m}(u,z)=\sum_{r\le m}w_rF_{i,r}(u,z)\). Then for \(m>i\),

\[
H_{i,m}=H_{i,m-1}\left(1+\frac{w_m z}{W_{m-1}}\right),\qquad
\frac{F_{i,m+1}}{F_{i,m}}=\frac{W_{m-1}+w_m z}{W_m}=1-p_m+p_m z.
\]

This is a polynomial identity (no division by an actual vanishing value). Iterating from \(m=i+1\) gives

\[
F_{i,j}(u,z)=F_{i,i+1}(u,z)\prod_{k=i+1}^{j-1}(1-p_k+p_kz).
\]

This is exactly the generating function of the independent Bernoulli convolution in (1). A one-vertex version of this recurrence is classical; the extension with a retained earlier-depth marker and the quantitative dependence consequences are the content under study.

**2. Frozen covariance and its strict sign.** Let \(\mathcal F_m\) be the sigma-field of the first \(m\) parent choices, define \(M_m=A_m/W_m\) and \(\xi_m=D_{K_m}-M_{m-1}\). Then \(\mathbb E[\xi_m\mid\mathcal F_{m-1}]=0\). Directly from weighted averaging,

\[
M_m-\mathbb EM_m=\sum_{k=2}^{m}p_k\xi_k,
\qquad
D_i-\mathbb ED_i=\sum_{k=2}^{i-1}p_k\xi_k+\xi_i.
\]

Also, \(\mathbb E[D_{i+1}\mid\mathcal F_i]=1+M_i\), hence by orthogonality of martingale differences,

\[
\operatorname{Cov}(D_i,D_{i+1})
=\operatorname{Cov}(D_i,M_i)
=\sum_{k=2}^{i-1}p_k^2\mathbb E\xi_k^2+p_i\mathbb E\xi_i^2=C_i.
\]

For \(i\ge3\), the parent of \(i\) has positive conditional probability to be vertex 1 or vertex 2, whose depths are respectively zero and one. Thus \(v_i=\mathbb E\xi_i^2>0\). Finally (1) makes \(S_{i,j}\) independent of \((D_i,D_{i+1})\), proving (2) for all \(j>i\).

**3. A universal total-variation upper bound.** Let \(q(a)=\Pr(S_{i,j}=a)\). Because \(q\) is a convolution of Bernoulli mass functions, it is log-concave and unimodal. For each integer \(h\), telescoping along shifts gives \(d_{\mathrm{TV}}(S_{i,j},S_{i,j}+h)\le |h|\max_a q(a)\). Couple the fixed-depth first coordinates and use an independent copy \(Y'\) of \(Y\); convexity of total variation yields

\[
\Delta_{i,j}\le\mathbb E|Y-Y'|\max_a q(a).
\]

The Bernoulli characteristic function satisfies

\[
\left|\mathbb E\exp(itS_{i,j})\right|
\le\exp\{-2V_{i,j}\sin^2(t/2)\}.
\]

Fourier inversion and \(\sin(|t|/2)\ge |t|/\pi\), for \(|t|\le\pi\), give

\[
\max_a q(a)\le\frac{1}{2\pi}\int_{-\pi}^{\pi}e^{-2V_{i,j}t^2/\pi^2}\,dt
\le \frac{\sqrt\pi}{2\sqrt{2V_{i,j}}}.
\]

This proves the upper bound in (4).

**4. A matching local-limit lower bound.** Suppose \(V=V_{i,j}\to\infty\), write \(S=S_{i,j}\), \(t_j=\lfloor\mathbb ES\rfloor\). A local central limit theorem holds uniformly for any *fixed finite* set of integers \(r\):

\[
\sqrt V\Pr(S=t_j-r)\longrightarrow\frac{1}{\sqrt{2\pi}}.
\]

For completeness, write the centered characteristic function at \(u/\sqrt V\). Its logarithm is \(-u^2/2+O(|u|^3/\sqrt V)\) on fixed compact \(u\)-sets, since the summed third absolute Bernoulli moments are at most \(V\). The previous Fourier bound provides the integrable majorant \(\exp(-2u^2/\pi^2)\) under the substitution \(u=t\sqrt V\). Fourier inversion and dominated convergence give the displayed local limit, including the bounded shifts \(r\).

Put \(g(X)=X/(i-1)\in[0,1]\). Since \(0\le Y\le i\), uniformly over the finitely many values of \((X,Y)\),

\[
\Pr(S+Y\le t_j\mid X,Y)
=\Pr(S\le t_j)-\frac{Y}{\sqrt{2\pi V}}+o(V^{-1/2}).
\]

Taking covariance with \(g(X)\), the difference between the joint expectation of the bounded test \(g(X)\mathbf1_{\{D_j\le t_j\}}\) and its expectation under the product of marginals is

\[
-\frac{\operatorname{Cov}(X,Y)}{(i-1)\sqrt{2\pi V}}+o(V^{-1/2}).
\]

Because a \([0,1]\)-valued test has expectation discrepancy at most total variation and \(\operatorname{Cov}(X,Y)=C_i>0\), this proves the lower bound in (4). No finite enumeration is used to establish a rate.

**5. Power weights and the phase boundary.** For \(w_k=k^\alpha\), elementary power-sum estimates give \(p_k\sim (\alpha+1)/k\) when \(\alpha>-1\), \(p_k=1/(kH_k)\) when \(\alpha=-1\), and \(p_k\sim k^\alpha/\zeta(-\alpha)\) when \(\alpha<-1\). In the first two cases, \(\sum p_k^2<\infty\); hence \(V_{i,j}\sim(\alpha+1)\log j\), or \(V_{i,j}\sim\log\log j\), respectively. Equation (4) yields the first two regimes in (5).

When \(\alpha<-1\), \(\sum_kp_k<\infty\), so the independent Bernoulli sum \(S_{i,j}\) converges almost surely to a finite integer-valued \(S_{i,\infty}\). In this canonical Bernoulli coupling, the probability that \(S_{i,j}\ne S_{i,\infty}\) is at most \(\sum_{k\ge j}p_k\to0\); thus the joint laws and their products converge in total variation. The limit has covariance \(C_i>0\), since \(S_{i,\infty}\) is independent of \((X,Y)\) and has finite second moment (indeed, finite exponential moments). Therefore the limiting joint law is not a product and \(\Delta_{i,\infty}>0\). This proves (5).

## Verification

The accompanying standalone `verify_depth_dependence.py` uses exact `fractions.Fraction` arithmetic to enumerate all parent choices for 7-vertex weighted recursive trees with four heterogeneous weight sequences. For every earlier label \(i\in\{3,4,5,6\}\) and every permitted younger label \(j>i\), it independently computes the bivariate depth law, recomputes the Bernoulli-convolution law, checks equality, verifies covariance is frozen across \(j\), and checks normalization: 120 assertions all passed. This exact finite enumeration checks examples, not the infinite theorem. The Fourier argument, local limit and summable-coupling proof establish the infinite assertions.

To reproduce from the package directory, run `python3 verify_depth_dependence.py` (standard Python library only).

## Relationship to prior work

Gałązka and Wdowicka (2026, arXiv:2610.00614v1) study the *same deterministic-weight recursive tree*. Their Proposition 2.1 (attributed to Mailler and Uribe Bravo, Curien and Haas, and others) gives the known **one-vertex** Bernoulli convolution, and their Section 5 gives the martingale innovations used here. Their Theorem 6 and subsequent sections treat **global total-path-length** fluctuations, not a tagged-pair bivariate factorization, frozen covariance or the sharp \(\Theta(V^{-1/2})\) two-label total-variation dependence rate.

Lodewijks (2023, arXiv:2204.09032) treats joint label/depth properties in the **uniform** recursive tree, notably regimes with all marked labels diverging. The present fixed-old-label, moving-young-label theorem also covers arbitrary positive deterministic attachment weights and includes the summable-weight nondecoupling boundary. Generic smoothing of a bounded signal by a divergent Poisson-binomial sum is a known probabilistic mechanism, but the exact joint-depth factorization and its strict nonzero frozen covariance identify the process-specific signal and give both matching bounds.

The title, exact quantities and implications were compared against relevant accessible full-text studies, older joint-depth results and semantically related mathematical research records. That comparison is not a proof of absolute novelty: earlier work on ancestral indicators or abstract translated Poisson-binomial kernels might implicitly imply parts of the result. The established one-vertex depth law, martingale decomposition, local CLT and general smoothing inequality are **not** claimed independently new.

## Limitations

The result is for two *labeled vertex depths*, with \(i\ge3\) fixed, and does not claim a uniform estimate as \(i\) grows with \(j\). The asymptotic upper and lower constants need not coincide; an exact asymptotic prefactor for total variation is not proved. For arbitrary deterministic weights with bounded \(V_{i,j}\), the theorem does not classify every possible limit; only the specified power-weight family is classified. It does not concern conditional independence given the evolving tree, ancestor relations, the whole tree profile, directed distances, or joint laws of many labels. The findings have undergone an internal mathematical review but no independent audit.

## References

1. Marek Gałązka and Hanna Wdowicka, *Total Path Length in Power-Weight Recursive Trees: Martingale Limits and Global Fluctuations*, arXiv:2610.00614v1 (first submitted 2026-09-30), Sections 2, 5--8; https://arxiv.org/html/2610.00614v1.
2. Bas Lodewijks, *On joint properties of vertices with a given degree or label in the random recursive tree*, arXiv:2204.09032 (2022 preprint; later revision 2023), especially joint depth and label results; https://arxiv.org/abs/2204.09032.
3. Camille Mailler and Gerónimo Uribe Bravo (2019), prior weighted-tree ancestral-indicator/depth representation, Corollary 8 (as cited in Reference 1).
4. Nicolas Curien and Bénédicte Haas (2017), weighted ancestral-indicator coupling, equation (2.2) (as cited in Reference 1).
5. Hendrik Hiesmayr and Ümit Işlak (2020), weighted recursive graph literature (as cited in Reference 1).
