# An almost-sure Gumbel-mixture law for widths of random symmetric edge polytopes

## Finding
For each fixed \(p\in(0,1]\) and integer \(n\ge3\), let \(G_n\) be an Erdős–Rényi graph on \(\{1,\ldots,n\}\), each edge present independently with probability \(p\). Define the canonical Euclidean symmetric edge polytope
\[
P_{G_n}=\operatorname{conv}\{\pm(e_i-e_j):\{i,j\}\in E(G_n)\}\subset H_n,\quad H_n=\{x\in\mathbb R^n:\sum_i x_i=0\}.
\]
For an empty edge set adopt the harmless convention \(P_G=\{0\}\). Let \(U_n\) be uniform on the unit sphere of \(H_n\), and let \(w_P(u)=\max_{x\in P}\langle u,x\rangle-\min_{x\in P}\langle u,x\rangle\). Write \(\Phi\) for the standard normal CDF and set \(b_n=\Phi^{-1}(1-1/n)>0\).

Let \(E_1,E_2,\ldots\) be independent unit-rate exponential variables, \(S_k=E_1+\cdots+E_k\), and set
\[
A_p=\sum_{k=1}^{\infty}\frac{p(1-p)^{k-1}}{S_k},\qquad
M_p=H+\log A_p,
\]
where \(H\) is an independent standard Gumbel with CDF \(\exp(-e^{-t})\). At \(p=1\), the sum means \(A_1=1/S_1\). It is almost surely positive and finite, since \(p/S_1\le A_p\le1/S_1\).

**Theorem (quenched spherical-width limit).** For any joint construction of the sequence \((G_n)\) having these Erdős–Rényi marginals, almost surely with respect to the graphs,
\[
\mathcal L\!\left(\left.b_n\left[\frac{\sqrt{n-1}}{2}w_{P_{G_n}}(U_n)-2b_n\right]\right|G_n\right)
\ \Longrightarrow\ \mathcal L(M_p).
\]
In particular, this is also the joint (graph-and-direction) weak limit. The limit has explicit CDF and sharp right tail
\[
F_p(t)=\Pr(M_p\le t)=\mathbb E\exp(-e^{-t}A_p),\qquad
\Pr(M_p>t)\sim p\,t e^{-t}\quad(t\to+\infty).
\]
At \(p=1\), \(M_1\) is the sum of two independent standard Gumbels. For \(0<p<1\), the limiting law is a genuine (non-degenerate) Gumbel location mixture. For every deterministic graph \(G\) on \(n\ge2\) vertices,
\[
\Pr_{U}\big\{w_{P_G}(U)=w_{P_{K_n}}(U)\big\}
=\frac{|E(G)|}{\binom n2}.
\]
Thus for \(G_n\), this coincidence probability tends to \(p\) almost surely, even though the first-order widths of the two polytopes agree.

## Assumptions and scope
The geometry is Euclidean in the specific standard zero-sum embedding, not a general lattice-equivalent embedding. Graph randomness and spherical-direction randomness are independent. The parameter \(p\) is fixed in \((0,1]\) as \(n\to\infty\). The limiting probability statement is *quenched*: for almost every graph sequence, the distribution over directions converges to the same nonrandom distribution. The result remains meaningful on the negligible event that a sampled graph is disconnected because the width is always measured in \(H_n\). No statements are made for \(p=0\), \(p\) varying with \(n\), higher-order moments of finite-dimensional widths, or adaptive directions.

## Proof
**1. Gaussian support representation.** For a deterministic graph \(G\), symmetry of the root set yields
\[
w_{P_G}(u)=2\max_{\{i,j\}\in E(G)}|u_i-u_j|.
\]
Let \(g_1,\ldots,g_n\) be independent \(N(0,1)\), \(\bar g=n^{-1}\sum g_i\), and \(R_n=\|g-\bar g\mathbf1\|\). Then \(U_n=(g-\bar g\mathbf1)/R_n\) is uniform on the sphere of \(H_n\), and with \(D_G(g)=\max_{\{i,j\}\in E(G)}|g_i-g_j|\) (zero if no edges),
\[
\frac{R_n}{2}w_{P_G}(U_n)=D_G(g).
\]
Further, \(R_n/\sqrt{n-1}=1+O_{\Pr}(n^{-1/2})\) and \(D_G(g)\le\max_i g_i-\min_i g_i=O_{\Pr}(b_n)\), uniformly in the graph. Since \(b_n^2=O(\log n)\), uniformly over all graphs,
\[
b_n\left|\frac{\sqrt{n-1}}{2}w_{P_G}(U_n)-D_G(g)\right|=o_{\Pr}(1).
\]
It is therefore enough to prove the claimed conditional limit for \(b_n(D_G(g)-2b_n)\).

**2. Two Gaussian extreme processes.** The classical normal-tail estimate gives
\[
n\Pr\{g_1>b_n+t/b_n\}\longrightarrow e^{-t},\qquad
b_n^2=2\log n-\log\log n-\log(4\pi)+o(1).
\]
Hence the upper points \(b_n(g_i-b_n)\) and lower points \(b_n(-g_i-b_n)\) converge jointly, on compact sets of their respective upper tails, to independent Poisson point processes on \(\mathbb R\), each with intensity \(e^{-x}\,dx\). A single Gaussian coordinate cannot belong to both extreme tails for large \(n\). For every fixed finite number of extremal upper and lower labels, the graph edges between them are independently Bernoulli \(p\), independent of those Gaussian labels. These finite marked point configurations therefore converge jointly.

To justify discarding the remaining points, fix a threshold \(t\) and an error tolerance. Tightness of the two largest normalized extreme points allows choosing \(B\) such that, except on an event of arbitrarily small probability, both maxima are at most \(B\). Choose \(K>B-t\). A candidate pair whose normalized upper or negative-lower coordinate is below \(-K\) cannot have sum greater than \(t\). Hence the event \(\{b_n(D_G(g)-2b_n)>t\}\) is, up to arbitrarily small error, determined by a finite region of the marked extreme processes. Its limit is the event that some retained cross-edge connects points with upper and lower coordinates summing above \(t\). Denote the resulting maximum by \(M_p^*\). This also proves tightness; the limiting CDF is continuous by the computation below.

**3. Explicit Poisson transform.** Apply \(x\mapsto e^{-x}\) to the upper and lower Poisson processes. Both become independent homogeneous rate-one Poisson processes on \((0,\infty)\). Let the upper points in increasing order be \(S_1<S_2<\cdots\), and write \(z=e^{-t}\). A cross-pair with transformed coordinates \(s,v\) beats \(t\) exactly when \(sv<z\). Given all upper points, a lower point \(v\) produces no retained qualifying edge with probability \((1-p)^{N(z/v)}\), where \(N(a)=\#\{k:S_k<a\}\). Independence of edge marks between distinct lower points and Poisson thinning give
\[
\Pr(M_p^*\le t\mid(S_k))
=\exp\!\left(-\int_0^\infty\bigl[1-(1-p)^{N(z/v)}\bigr]dv\right).
\]
Since \(1-(1-p)^{N(a)}=\sum_{k:S_k<a}p(1-p)^{k-1}\), Tonelli's theorem and \(\int_{S_k}^\infty a^{-2}da=S_k^{-1}\) imply that the exponent's integral is
\[
z\int_0^\infty\frac{1-(1-p)^{N(a)}}{a^2}\,da
=z\sum_{k\ge1}\frac{p(1-p)^{k-1}}{S_k}=zA_p.
\]
Thus \(\Pr(M_p^*\le t)=\mathbb E e^{-e^{-t}A_p}\), identical to the conditional CDF of \(H+\log A_p\). Its continuity identifies \(M_p^*\) with \(M_p\) and proves the joint graph/direction weak limit. The bound \(p/S_1\le A_p\le1/S_1\) proves finiteness and logarithmic integrability.

**4. Almost-sure quenched upgrade.** For fixed \(t\), put \(c_n=2b_n+t/b_n\), and define \(f_n(G)=\Pr_g\{D_G(g)\le c_n\}\). Replacing any one graph edge can change this CDF by at most
\[
q_n(t)=\Pr\{|g_1-g_2|>c_n\}
=2\left[1-\Phi\!\left(\frac{c_n}{\sqrt2}\right)\right]
=O_t\!\left(\frac{\sqrt{\log n}}{n^2}\right),
\]
by the displayed Gaussian quantile expansion and the Mills estimate. There are \(\binom n2\) independent edge indicators. The bounded-differences inequality consequently yields, for every \(\varepsilon>0\),
\[
\Pr_G\{|f_n(G_n)-\mathbb E f_n(G_n)|>\varepsilon\}
\le2\exp\!\left(-c_{t,\varepsilon}\frac{n^2}{\log n}\right)
\]
for sufficiently large \(n\), with a positive constant \(c_{t,\varepsilon}\). This is summable. Borel–Cantelli at every rational threshold, together with continuity of \(F_p\), gives almost-sure weak convergence of the direction-conditional Gaussian-support law. The graph-uniform radial estimate in Step 1 transfers the conclusion to spherical widths.

**5. Exact coincidence probability.** For a Gaussian direction, the maximum over all pairs is the unique gap between the coordinates of its largest and smallest components. The two labels are a uniformly random unordered pair among \(\binom n2\), independently of any fixed graph. Equality of its width with the complete-graph width holds precisely when this pair is an edge. The exact probability is therefore the edge density. For \(G_n\), Hoeffding's inequality for \(\binom n2\) Bernoulli edge indicators gives almost-sure convergence of the edge density to \(p\).

**6. Sharp upper tail.** Split \(A_p=p/S_1+B_p\), where \(B_p\ge0\) and
\[
\mathbb E B_p
=\sum_{k\ge2}p(1-p)^{k-1}\mathbb E(1/S_k)
=\sum_{j\ge1}\frac{p(1-p)^j}{j}
=-p\log p<\infty,
\]
interpreted as zero for \(p=1\). For \(z\downarrow0\), positivity gives
\[
0\le \mathbb E(1-e^{-zA_p})-\mathbb E(1-e^{-zp/S_1})\le z\mathbb E B_p.
\]
Because \(S_1\) has the unit exponential law, splitting its integral at \(zp\) and at \(1\) yields
\[
\mathbb E(1-e^{-zp/S_1})=zp\log(1/(zp))+O_p(z).
\]
With \(z=e^{-t}\), this proves \(1-F_p(t)\sim pte^{-t}\).

## Verification
A standalone program `checker.py` uses independent finite and probabilistic representations. It exhaustively checks the support-width identity and complete-graph equality probability for all \(2^{10}=1024\) graphs on five labeled vertices and all \(5!=120\) orderings. It compares finite Gaussian/independent-edge maxima in dimension \(3000\), the weighted-arrival-time mixture, and an independently marked two-process Poisson construction; it separately checks the \(p=1\) sum-of-two-Gumbels specialization. The archived program's output was `EXACT_COMBINATORIAL_PASS 1024 120` and `FINITE_LIMIT_DIAGNOSTICS_PASS 3000 1400`. These finite and Monte Carlo checks are diagnostic; the proof of the infinite limit is the analytic argument above.

## Relationship to prior work
Chen, Davis and Korchevskaia (2021) develop the facet/face-subgraph correspondence for symmetric edge polytopes. Braun, Bruegge and Kahle (first circulated 2022) analyze facets of these polytopes for Erdős–Rényi and other graph ensembles; in particular their threshold concerns facet-supporting bipartitions, not random-direction widths. Donzelmann, Juhnke, Rednoß and Thäle (2026) derive central limit theorems for **counts of edges** of random symmetric edge polytopes and their triangulations, which do not imply directional-width laws. The present theorem instead gives a full second-order directional-width law, with an explicit random shift and almost-sure graph-quenched self-averaging. The standard Gaussian extreme-value point-process limit is used as background, not claimed as new.

## Limitations
The result only treats fixed edge probability and the standard Euclidean embedding. It does not derive an asymptotic theorem for \(p\to0\) or make finite-sample Kolmogorov-rate claims. Almost-sure quenched convergence is with respect to the randomness of the graph sequence, not an assertion about every deterministic graph with edge density near \(p\). The analytical proof does not depend on finite Monte Carlo confirmation. A specialized previously unindexed extreme-value treatment of Gaussian-labeled graphs could overlap with the marked-point-process reduction; that bibliographic possibility remains open. Independent validation has not been performed.

## References
1. T. Chen, R. Davis and E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315 (first public version 2021-07-26), https://arxiv.org/abs/2107.12315.
2. B. Braun, K. Bruegge and M. Kahle, *Facets of Random Symmetric Edge Polytopes, Degree Sequences, and Clustering*, arXiv:2204.07239 (first public version 2022-04-14), https://arxiv.org/html/2204.07239v4.
3. T. Donzelmann, M. Juhnke, B. Rednoß and C. Thäle, *Central limit theorems for high dimensional lattice polytopes: symmetric edge polytopes*, arXiv:2603.10650 (first public version 2026-03-11), https://arxiv.org/html/2603.10650v1.
