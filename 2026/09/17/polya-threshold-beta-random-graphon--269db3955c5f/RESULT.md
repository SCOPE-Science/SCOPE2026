# Beta-random graphon limits and two-scale edge fluctuations for Polya threshold graphs

## Statement

Consider the classical two-color Polya threshold graph of Yu, Alajaji and Gharesifard. The urn initially contains \(R>0\) red and \(B>0\) black mass and, after each draw, reinforces the drawn color by \(\Delta>0\). Write

\[
\rho=\frac{R}{R+B},\qquad
\delta=\frac{\Delta}{R+B},\qquad
a=\frac{\rho}{\delta}=\frac{R}{\Delta},\qquad
b=\frac{1-\rho}{\delta}=\frac{B}{\Delta}.
\]

Let \(Z_t\in\{0,1\}\) be the red-draw indicator. At time \(t\), \(Z_t=1\) creates a universal vertex and \(Z_t=0\) creates an isolated vertex. Let \(G_n^\circ\) be the simple graph obtained from the paper's graph by deleting self-loops.

Define
\[
\Theta=\lim_{n\to\infty}\frac1n\sum_{t=1}^n Z_t.
\]
The classical Polya law gives
\[
\Theta\sim {\rm Beta}(a,b).
\]

### Theorem 1: random graphon limit

Almost surely,
\[
G_n^\circ\longrightarrow \Gamma_{\mu_\Theta}
\]
in the dense graph-limit topology, where, for \(0<p<1\), \(\mu_p\) is the probability law on \([0,1]\) with density
\[
f_p(x)=
\begin{cases}
(1-p)/p,&0<x<p,\\[2mm]
p/(1-p),&p<x<1.
\end{cases}
\]

Equivalently, conditional on \(\Theta=p\), the limit is exactly the deterministic random-addition threshold limit \(\Gamma_{\mu_p}\) identified by Diaconis, Holmes and Janson.

The limiting edge density is
\[
t(K_2,\Gamma_{\mu_\Theta})=\Theta.
\]
Since \(\Theta\) is nondegenerate for \(R,B,\Delta>0\), the Polya threshold graph has no deterministic graph-limit limit in probability. Its macroscopic randomness survives in a one-dimensional Beta environment.

### Theorem 2: all fixed subgraph densities

Let \(H\) be any finite simple graph with \(h\) vertices. For an ordering \(\pi\) of \(V(H)\), let
\[
A_H(\pi)=\#\{v\in V(H): v\text{ has at least one neighbor preceding }v\text{ in }\pi\}.
\]
Define
\[
P_H(p)=\frac1{h!}\sum_{\pi} p^{A_H(\pi)}.
\]
Then almost surely
\[
t(H,G_n^\circ)\longrightarrow P_H(\Theta).
\]

In particular, for every \(r\ge2\),
\[
t(K_r,G_n^\circ)\longrightarrow \Theta^{r-1}.
\]
The expected number \(N_r(n)\) of \(r\)-cliques satisfies the exact finite-\(n\) identity
\[
\mathbb E N_r(n)
=
\binom nr
\frac{(a)^{\overline{r-1}}}{(a+b)^{\overline{r-1}}},
\]
where \(x^{\overline m}=x(x+1)\cdots(x+m-1)\).

For the three-vertex path \(P_3\),
\[
t(P_3,G_n^\circ)\longrightarrow \frac{\Theta+2\Theta^2}{3},
\]
whereas
\[
t(K_3,G_n^\circ)\longrightarrow \Theta^2.
\]
Hence the usual global transitivity coefficient converges almost surely to
\[
\frac{3\Theta}{1+2\Theta}.
\]

### Theorem 3: exact edge variance and two fluctuation scales

Let \(E_n=e(G_n^\circ)\), and set
\[
W_n=\binom n2,\qquad
Q_n=\sum_{j=1}^{n-1}j^2=\frac{(n-1)n(2n-1)}6.
\]
Then
\[
E_n=\sum_{t=2}^n (t-1)Z_t,
\]
and exactly
\[
\mathbb E E_n=\rho W_n,
\]
\[
\operatorname{Var}(E_n)
=
\frac{\rho(1-\rho)}{1+\delta}
\left(\delta W_n^2+Q_n\right).
\]
Consequently,
\[
\frac{E_n}{W_n}\longrightarrow\Theta
\qquad\text{almost surely},
\]
and
\[
\operatorname{Var}\!\left(\frac{E_n}{W_n}\right)
\longrightarrow
\frac{\rho(1-\rho)\delta}{1+\delta}>0.
\]

Around the random environment there is a smaller Gaussian scale. Jointly,
\[
\left(
\Theta,\,
\frac{E_n-\Theta W_n}
{\sqrt{\Theta(1-\Theta)Q_n}}
\right)
\Longrightarrow
(\Theta,Z),
\]
where \(Z\sim N(0,1)\) is independent of \(\Theta\). Equivalently, the convergence is stable with respect to \(\sigma(\Theta)\).

By contrast, deterministic centering leaves the order-\(n^2\) environmental fluctuation:
\[
\frac{E_n-\rho W_n}{W_n}\longrightarrow\Theta-\rho
\qquad\text{almost surely}.
\]

Thus reinforcement creates two asymptotic scales: a nonvanishing Beta fluctuation at graph-density scale and conditional Gaussian fluctuations of order \(n^{3/2}\) around that random environment.

## Proof

### 1. Beta mixing representation

The joint law in Eq. (3) of Yu, Alajaji and Gharesifard assigns to a binary string with \(k\) ones the probability
\[
\frac{\Gamma(a+b)\Gamma(a+k)\Gamma(b+n-k)}
{\Gamma(a)\Gamma(b)\Gamma(a+b+n)}.
\]
But
\[
\int_0^1 p^k(1-p)^{n-k}
\frac{p^{a-1}(1-p)^{b-1}}{B(a,b)}\,dp
\]
is exactly the same quantity. Hence there is a de Finetti variable
\(\Theta\sim{\rm Beta}(a,b)\) such that, conditional on \(\Theta=p\), the variables \(Z_1,Z_2,\ldots\) are iid Bernoulli\((p)\). The almost-sure sample-average limit in the source paper is this same \(\Theta\).

### 2. Graph-limit identification

Deleting self-loops removes the only effect of \(Z_1\). Conditional on \(\Theta=p\), the variables \(Z_2,\ldots,Z_n\) are iid Bernoulli\((p)\), so \(G_n^\circ\) is exactly the random threshold graph obtained by sequentially adding each new vertex as dominant with probability \(p\) and isolated with probability \(1-p\).

Theorem 6.5 of Diaconis, Holmes and Janson proves that this fixed-\(p\) model converges almost surely to \(\Gamma_{\mu_p}\), with the density \(f_p\) displayed above. Applying that theorem conditionally for every \(p\in(0,1)\), then integrating over the Beta law, gives
\[
G_n^\circ\to\Gamma_{\mu_\Theta}
\quad\text{almost surely}.
\]

The mean of \(\mu_p\) is
\[
\frac{1-p}{p}\int_0^p x\,dx+
\frac{p}{1-p}\int_p^1x\,dx=p,
\]
so the limiting edge density is \(p\). Therefore the random limit determines \(\Theta\), and a deterministic graph-limit limit is impossible because the Beta law is nondegenerate.

### 3. Subgraph polynomial

Condition on \(\Theta=p\). For an injective placement of the vertices of \(H\) into the birth order, the induced ordering \(\pi\) is uniform over the \(h!\) orders. An edge of \(H\) is present precisely when its later endpoint was added as dominant. Thus all edges of \(H\) are present exactly when every vertex counted by \(A_H(\pi)\) is dominant, an event of probability \(p^{A_H(\pi)}\).

Averaging over orders gives \(P_H(p)\). Collisions in ordinary homomorphism density have proportion \(O(1/n)\), so the same limit holds for \(t(H,G_n^\circ)\). For \(K_r\), every vertex except the first in the order is counted, yielding \(p^{r-1}\).

For a fixed \(r\)-set of vertices, the clique condition is again that all but its earliest vertex are dominant. Therefore, conditional on \(\Theta=p\), its clique probability is \(p^{r-1}\). Averaging over the Beta law gives
\[
\mathbb E[\Theta^{r-1}]
=
\frac{(a)^{\overline{r-1}}}{(a+b)^{\overline{r-1}}},
\]
which proves the exact clique expectation.

For \(P_3\), four of the six vertex orders require two dominant vertices and two orders require one, so
\[
P_{P_3}(p)=\frac{2p^2+p}{3}.
\]
Together with \(P_{K_3}(p)=p^2\), this gives the transitivity limit.

### 4. Edge moments and stable central limit theorem

Conditional on \(\Theta\),
\[
\mathbb E(E_n\mid\Theta)=\Theta W_n,\qquad
\operatorname{Var}(E_n\mid\Theta)=\Theta(1-\Theta)Q_n.
\]
For \(\Theta\sim{\rm Beta}(a,b)\),
\[
\operatorname{Var}(\Theta)=
\frac{\rho(1-\rho)\delta}{1+\delta},
\qquad
\mathbb E[\Theta(1-\Theta)]
=
\frac{\rho(1-\rho)}{1+\delta}.
\]
The law of total variance gives the stated exact formula.

Conditional on \(\Theta=p\in(0,1)\), \(E_n/W_n\) is a weighted average of iid Bernoulli\((p)\) variables with maximal normalized weight tending to zero, hence it converges almost surely to \(p\).

For the central limit theorem, conditional on \(\Theta=p\), consider
\[
\frac{\sum_{j=1}^{n-1}j(Z_{j+1}-p)}
{\sqrt{p(1-p)Q_n}}.
\]
The summands are independent and centered, and
\[
\frac{\max_{1\le j\le n-1}j}{\sqrt{Q_n}}\to0.
\]
Therefore the Lindeberg condition holds and the conditional law converges to \(N(0,1)\). For any bounded measurable \(g(\Theta)\), dominated convergence applied to conditional expectations gives joint convergence to an independent standard normal, which is the stated stable convergence.

Finally,
\[
\frac{E_n-\rho W_n}{W_n}
=
\frac{E_n-\Theta W_n}{W_n}+(\Theta-\rho),
\]
and the first term tends to zero almost surely, proving the deterministic-centering limit.

## Context and significance

Yu, Alajaji and Gharesifard introduced the Polya threshold graph in 2026 and derived exact one-vertex degree distributions, decay centrality, Laplacian structure, and consensus results. Their searchable full text cites the classical threshold-limit paper but does not state a graphon limit, global edge-density limit, clique-density limit, or central limit theorem for the reinforced model.

Diaconis, Holmes and Janson proved the graph-limit theorem for independent random vertex additions with a fixed probability \(p\). The result here identifies the reinforced model as a Beta mixture of that fixed-\(p\) family. This changes the qualitative asymptotics: the fixed-\(p\) model has a deterministic graph limit, while Polya reinforcement leaves a nondegenerate random graphon whose entire macroscopic environment is encoded by \(\Theta\).

The subgraph polynomial \(P_H\) makes this random limit directly observable through any fixed motif. The edge-count formula then separates the persistent environmental variance from the smaller conditional Gaussian noise.

## Limitations

- The result concerns the classical two-color constant-reinforcement Polya urn. It does not cover the finite-memory extension considered later in the source paper.
- The graph-limit statement is for the simple graph obtained by deleting self-loops. The deleted loops are only \(O(n)\), so they do not affect dense graph limits or the normalized edge asymptotics.
- No rate in cut distance is proved, and no functional central limit theorem for the whole graphon or degree empirical process is claimed.
- The stable central limit theorem concerns the global edge count; analogous joint fluctuation theorems for multiple motifs are not established here.
- Originality is to the best of our knowledge. General exchangeability and graph-limit theory supplies ingredients broad enough to imply parts of the argument, so the claimed contribution is the explicit Polya-threshold identification, the random-limit formula, motif consequences, and the two-scale edge fluctuation theorem, not a new general graph-limit representation theorem.

## References

1. J. Yu, F. Alajaji, B. Gharesifard, "Polya Thresholds Graphs", arXiv:2603.18452 (2026). https://arxiv.org/abs/2603.18452
2. P. Diaconis, S. Holmes, S. Janson, "Threshold Graph Limits and Random Threshold Graphs", Internet Mathematics 5(3), 267-320 (2008). https://doi.org/10.1080/15427951.2008.10129166
3. P. Diaconis, S. Janson, "Graph limits and exchangeable random graphs", Rendiconti di Matematica 28, 33-61 (2008). https://arxiv.org/abs/0712.2749
