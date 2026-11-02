# A Gaussian logarithmic speedup for non-backtracking cover on balanced complete bipartite graphs

## Finding

There is an explicit coupling of a simple random walk and a non-backtracking random walk, both started at a prescribed vertex of the balanced complete bipartite graph \(K_{n,n}\), under which the cover-time saving has Gaussian fluctuations on a scale much smaller than the cover times themselves.

For each integer \(n\ge2\), let \(T_n^{\mathrm S}\) and \(T_n^{\mathrm N}\) be the respective vertex cover times (number of traversed edges, with the start counted as visited). In the **parity-stream compression coupling** specified below, \(T_n^{\mathrm N}\le T_n^{\mathrm S}\) almost surely and, as \(n\to\infty\),

\[
\left(
\frac{T_n^{\mathrm N}}{2n}-\log n,\quad
\frac{T_n^{\mathrm S}-T_n^{\mathrm N}-2\log n}{2\sqrt{\log n}}
\right)
\Longrightarrow (G+\log 2,Z),
\]

where \(G\) has the standard Gumbel law \(\Pr(G\le x)=\exp(-e^{-x})\), \(Z\) is standard normal, and \(G,Z\) are **independent**. The intrinsic mean difference (which does not depend on coupling) has the sharper expansion

\[
\mathbb E T_n^{\mathrm S}-\mathbb E T_n^{\mathrm N}
=2\log n+2\gamma+2\log 2+o(1),
\]

where \(\gamma\) is Euler's constant. Thus suppressing immediate backtracking preserves the macroscopic Gumbel fluctuations while producing a logarithmic expected saving with asymptotically independent square-root-logarithmic fluctuations under a natural joint construction.

There is also an exact finite-size law. Define, for integer \(j\ge0\),

\[
F_n(j)=\sum_{k=0}^{n-1}(-1)^k\binom{n-1}{k}
\left(\frac{n-1-k}{n-1}\right)^j,\qquad
H_n(j)=\sum_{k=0}^{n-1}(-1)^k\binom{n-1}{k}
\left(\frac{n-k}{n}\right)^j,
\]

and set both functions to zero for negative arguments (with \(0^0=1\) in the finite sums). Then for each integer \(t\ge0\),

\[
\Pr(T_n^{\mathrm N}\le t)
=F_n(\lfloor t/2\rfloor)F_n(\lfloor(t-1)/2\rfloor),
\qquad
\Pr(T_n^{\mathrm S}\le t)
=H_n(\lfloor t/2\rfloor)H_n(\lfloor(t-1)/2\rfloor).
\]

These identities concern the marginal laws; the Gaussian saving law additionally requires the coupling below.

## Assumptions and scope

The graph is the simple undirected \(K_{n,n}\) with two disjoint labeled vertex parts \(A\) and \(B\), each of cardinality \(n\ge2\). Time is discrete. In the simple walk, every step is uniform among the current vertex's \(n\) neighbors. In the non-backtracking walk, the first step is uniform; thereafter the vertex visited exactly one step earlier is excluded from the candidate neighbors, and the next neighbor is uniform among the remaining \(n-1\). Both walks start at a fixed \(a_*\in A\), and cover includes every vertex of both parts.

For their joint construction, take two independent streams: \(A_0=a_*\), followed by iid uniform \(A_1,A_2,\ldots\in A\), and iid uniform \(B_0,B_1,\ldots\in B\), independent of the first stream. Alternately display \(A_0,B_0,A_1,B_1,\ldots\) to obtain the simple walk. Compress **each parity stream separately** by removing repetitions of its immediately preceding symbol, and then interleave the two compressed streams, beginning with the retained \(A_0\) and \(B_0\). The compressed interleaving has exactly the non-backtracking walk law. This is coordinate-wise run-length compression, not a claim about physically deleting two-edge segments from an existing trajectory. The saving's distribution is explicitly coupling-dependent.

## Proof

**1. Independent parity streams and exact finite laws.** On a complete bipartite graph, the simple walk's even-time vertices are \(A_0,A_1,\ldots\), and its odd-time vertices are \(B_0,B_1,\ldots\); the two streams are independent. Removing successive repeats in each yields an independent uniform walk on the loopless complete graph on \(n\) labels: from any label, its next retained label is uniform on the other \(n-1\), and the number of discarded repeats is independent of that next label. Interleaving them forbids revisiting the vertex from two graph steps earlier, exactly the non-backtracking rule.

Let \(K_A,K_B\) be the numbers of transitions required for the two compressed streams to cover their respective parts, counting their first label as time zero. They are iid with the same law \(K_n\), where

\[
K_n\ \overset d=\ \sum_{k=1}^{n-1}\operatorname{Geom}\left(\frac{k}{n-1}\right).
\]

The geometrics are independent and supported on positive integers. Indeed, with \(k\) labels still unseen, the next compressed transition hits a new label with probability \(k/(n-1)\), independent of which visited label is current. The probability of avoiding a prescribed set of \(k\) labels other than the starting label for \(j\) transitions is \(((n-1-k)/(n-1))^j\); inclusion–exclusion gives \(F_n(j)=\Pr(K_n\le j)\). The iid-stream analogue gives \(H_n\). The interleaving completes part \(A\) at time \(2K_A\) and part \(B\) at time \(2K_B+1\), proving the two exact cover-time formulas.

**2. Conditional repeat-count law.** Before each new retained label, the original iid stream samples its current label repeatedly with probability \(1/n\) per attempt, until it chooses a different label with success probability \(p_n=(n-1)/n\). These repeat counts are independent of the retained-label chain. Let \(R_A,R_B\) be the respective total discarded counts up to coverage, and let \(N_A=K_A+R_A\), \(N_B=K_B+R_B\). Conditional on \(K_i=k\),

\[
\Pr(R_i=r\mid K_i=k)=\binom{k+r-1}{r}
\left(\frac{n-1}{n}\right)^k\left(\frac1n\right)^r,
\quad r\ge0.
\]

The two pairs \((K_A,R_A)\), \((K_B,R_B)\) are independent, and

\[
T_n^{\mathrm N}=\max\{2K_A,2K_B+1\},\qquad
T_n^{\mathrm S}=\max\{2(K_A+R_A),2(K_B+R_B)+1\}.
\]

In particular \(T_n^{\mathrm S}\ge T_n^{\mathrm N}\) pathwise. This conditional negative-binomial identity, not merely a marginal coupon-collector limit, is the crucial input to the fine-scale law.

**3. Gumbel scale and choice of the last part.** For \(K_n\), let \(U_{n,j}\) be the number of labels other than the starting label not yet seen after \(j\) compressed steps. Its factorial moments are

\[
\mathbb E[(U_{n,j})_k]=(n-1)_k
\left(1-\frac{k}{n-1}\right)^j.
\]

At \(j=\lfloor(n-1)(\log(n-1)+x)\rfloor\), each fixed factorial moment tends to \(e^{-kx}\), so \(U_{n,j}\) converges to \(\operatorname{Poisson}(e^{-x})\). Hence \(K_n/(n-1)-\log(n-1)\Rightarrow G\). Independence gives

\[
\frac{\max(K_A,K_B)}n-\log n\Longrightarrow G+\log2.
\]

For the expectation, right tails of the centered variable are at most a constant times \(e^{-x}\) by the union bound. For left tails, the unseen-label indicators are pairwise nonpositively correlated since \(1-2/(n-1)\le(1-1/(n-1))^2\), so \(\operatorname{Var}(U_{n,j})\le\mathbb E U_{n,j}\), and the zero-count probability is at most \(1/\mathbb E U_{n,j}\). These supply integrable exponential tails on both sides and thus uniform integrability. Therefore

\[
\frac{\mathbb E\max(K_A,K_B)}{n-1}
=\log n+\gamma+\log2+o(1).
\]

**4. No switching of the last part.** Each \(K_n\) includes an independent terminal \(\operatorname{Geom}(1/(n-1))\), so \(\sup_j\Pr(K_n=j)\le1/(n-1)\). Consequently, for every deterministic \(L\ge0\),

\[
\Pr(|K_A-K_B|\le L)\le\frac{2\lfloor L\rfloor+1}{n-1}.
\]

Also \(\mathbb E(R_A+R_B)^2=O((\log n)^2)\) by the conditional negative-binomial moments and the exact geometric-stage representation. If \(R_A+R_B+1<|K_A-K_B|\), the same part wins the two maxima. Let \(R_*\) refer to the repetitions in the part winning the compressed maximum (ties are resolved by its extra odd-time step). The discrepancy between \((T_n^{\mathrm S}-T_n^{\mathrm N})/2\) and \(R_*\) is nonnegative and at most \(R_A+R_B+1\), vanishing off the possible-switching event. Truncate \(R_A+R_B\) at \(L=(\log n)^3\). The expected discrepancy is at most \(O(L^2/n)+O((\log n)^2/L)=o(1)\). Thus

\[
\mathbb E(T_n^{\mathrm S}-T_n^{\mathrm N})
=\frac{2\mathbb E\max(K_A,K_B)}{n-1}+o(1),
\]

which, with Step 3, proves the mean expansion. The same switching estimate gives an \(o_{\Pr}(1)\) error on the Gaussian scale.

**5. Gaussian saving and asymptotic independence.** Given \(K_A,K_B\), the selected \(R_*\) is a sum of \(K_*:=\max(K_A,K_B)\) independent geometric-failure variables, each with mean \(1/(n-1)\) and variance \(n/(n-1)^2\). Since \(K_*/(n\log n)\to1\) in probability,

\[
\frac{K_* /(n-1)-\log n}{\sqrt{\log n}}\to0,
\qquad
\frac{nK_* /(n-1)^2}{\log n}\to1
\]

in probability. The geometric-failure summands have uniformly negligible third absolute moments at this triangular-array scale, giving the conditional central limit theorem

\[
\frac{R_*-\log n}{\sqrt{\log n}}\Longrightarrow N(0,1).
\]

Because their conditional characteristic functions converge in probability to the deterministic standard-normal characteristic function, this convergence is *joint* with, and asymptotically independent of, every bounded function of \((K_A,K_B)\), including the centered maximum's Gumbel limit. Step 4 transfers it to the pathwise saving. The extra odd-time unit changes neither limit.

## Verification

The self-contained file `check.py` can be run with Python 3 using `python check.py`; it uses standard-library modules only. It reconstructs both walks by an independent rational Markov-chain dynamic program on the actual \(2n\)-vertex graphs for \(2\le n\le5\), checks the finite cover CDF identities through 12 steps, compares independent geometric convolutions to inclusion–exclusion through size 13, and performs seeded coupling diagnostics for \(n=40,120,400\). It passed 8,764 assertions. Finite checks are not substituted for Steps 3–5, which prove the infinite limiting claims.

## Relationship to prior work

Matsuo, Kawagishi, and Ohsaki (first public online version November 7, 2022) study mean first-passage and mean cover times for non-backtracking walks on random regular and configuration-model networks. Their work motivates exact comparisons but does not give the two-walk coupling, finite bipartite cover distribution, independent Gaussian saving, or constant-order mean difference above. Aldous and Fill's coverage examples give the one-stream iid and loopless-complete-graph coupon-collector Gumbel laws; those ingredients are explicitly used here and are not claimed as new. Alon, Benjamini, Lubetzky, and Sodin study non-backtracking mixing on regular expanders, a different observable and graph class. Existing separate calculations for other bipartite walk protocols and non-backtracking cycle bouquets do not imply this coupled, two-scale cover-time comparison.

The novelty asserted is the **specific coupled logarithmic Gaussian speedup and its independence from the macroscopic Gumbel cover time**, together with the exact interleaved two-stream law. A comprehensive historical-priority proof is not claimed.

## Limitations

The result assumes balanced complete bipartite graphs, uniform transitions, one prescribed starting vertex, and this specific coordinate-wise compression coupling. Although the expectation difference is intrinsic, the distribution of a difference of cover times is not defined without coupling; another coupling need not have the stated Gaussian saving law. No theorem is asserted for general irregular networks, arbitrary different part sizes, mixing times, or edge-cover times. Historical-priority assessment is subject to possible unindexed work and independently authored comparisons.

## References

1. R. Matsuo, T. Kawagishi, and H. Ohsaki, *On the mean first passage time and mean cover time of a non-backtracking random walk on graphs*, IEICE Communications Express 12 (2023), 42–47, first public November 7, 2022. DOI: https://doi.org/10.1587/comex.2022XBL0146. Accessible full text: https://www.jstage.jst.go.jp/article/comex/12/1/12_2022XBL0146/_pdf.
2. D. Aldous and J. Fill, *Reversible Markov Chains and Random Walks on Graphs*, Chapter 6, Section 6.2 (1994), https://www.stat.berkeley.edu/users/aldous/RWG/Book_Ralph/Ch6.S2.html.
3. N. Alon, I. Benjamini, E. Lubetzky, and S. Sodin, *Non-backtracking random walks mix faster*, Communications in Contemporary Mathematics 9 (2007), 585–603, DOI: https://doi.org/10.1142/S0219199707002551.
4. V. Falgas-Ravry, J. Larsson, and K. Markström, *Speed and concentration of the covering time for structured coupon collectors*, Advances in Applied Probability 52 (2020), 433–462, DOI: https://doi.org/10.1017/apr.2020.5.
