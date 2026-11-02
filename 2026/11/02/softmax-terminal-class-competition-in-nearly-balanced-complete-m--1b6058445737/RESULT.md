# Softmax terminal-class competition in nearly balanced complete multipartite walks

## Finding
Fix an integer \(k\ge3\). Let \(G_n=K_{m_{1,n},\ldots,m_{k,n}}\) be a complete \(k\)-partite graph, and run simple random walk from any specified vertex. Write \(\tau_{i,n}\) for the first time by which **every** vertex in part \(i\) has been visited, \(T_n=\max_i\tau_{i,n}\), and \(J_n\) for the part containing the last first-visited vertex. Assume, with fixed real numbers \(\theta_1,\ldots,\theta_k\), that
\[
m_{i,n}=n+\frac{\theta_i n}{\log n}+o\!\left(\frac n{\log n}\right).
\]
Set \(\Theta=\sum_i\theta_i\) and \(A=(k-2)\Theta/[k(k-1)]\). Let \(G_1,\ldots,G_k\) be independent standard Gumbel random variables (distribution function \(\exp(-e^{-x})\)). Then
\[
\left(\frac{\tau_{i,n}-kn(\log n+A)}{kn}\right)_{i=1}^k
\ \Longrightarrow\ \left(G_i+\frac{\theta_i}{k-1}\right)_{i=1}^k.
\]
In particular, for every real \(x\),
\[
\Pr\{T_n\le kn(\log n+A+x)\}\longrightarrow
\exp\left(-e^{-x}\sum_{i=1}^k e^{\theta_i/(k-1)}\right),
\qquad
\Pr\{J_n=i\}\longrightarrow
\frac{e^{\theta_i/(k-1)}}{\sum_{j=1}^k e^{\theta_j/(k-1)}}.
\]
Thus an imbalance of order \(n/\log n\), although negligible as a proportion of a part, changes the limiting location of the last discovered vertex. The factor \(1/(k-1)\) in the softmax is a nonbipartite slowdown of part-size sensitivity.

More generally, suppose all \(m_{i,n}/n\to1\) and one part \(i_*\) satisfies \((m_{i_*,n}-m_{j,n})\log n/n\to+\infty\) for every \(j\ne i_*\). Then \(\Pr\{J_n=i_*\}\to1\). This gives the one-sided dominance beyond the critical \(n/\log n\) window.

## Assumptions and scope
Time is the number of walk moves after the initial specified vertex at time zero. All edges between distinct parts are present and no edges within a part are present. The number \(k\ge3\) of parts is fixed while \(n\to\infty\); part sizes are positive integers. The starting vertex is arbitrary, and may vary with \(n\). No laziness, vertex weights, or growth of \(k\) is assumed. The last newly visited part is unique because a step visits at most one new vertex.

## Proof
Write \(m_i=m_{i,n}\), \(N=\sum_i m_i\), and \(S=\sum_i m_i(N-m_i)=N^2-\sum_i m_i^2\). A walk move from part \(i\) first chooses its next part \(j\ne i\) with probability \(P(i,j)=m_j/(N-m_i)\), then chooses uniformly among the \(m_j\) vertices in that part. This constructs a class Markov chain independently of \(k\) infinite streams of independent, uniformly distributed within-class coupon labels. Its stationary law is exactly
\[
\pi_i=\frac{m_i(N-m_i)}S,
\]
since \(\pi_iP(i,j)=m_im_j/S=\pi_jP(j,i)\).

For \(k\ge3\) and \(m_i/n\to1\), all off-diagonal entries of \(P\) are bounded below by a constant independent of \(n\). Every entry of \(P^2\) is therefore bounded below by a positive constant: for distinct endpoints choose an intermediate third part; for equal endpoints choose any other part. Consequently the class chain satisfies a uniform two-step Doeblin contraction. If \(V_i(t)\) counts visits to part \(i\) among moves \(1,\ldots,t\), uniformly in the starting class,
\[
\mathbb EV_i(t)=t\pi_i+O(1),\quad
\operatorname{Var}(V_i(t))=O(t).
\]
Indeed, geometric contraction bounds the initial transient in the mean and makes the covariance sum of the visit indicators summable. For deterministic \(t=O(n\log n)\), Chebyshev's inequality gives
\[
V_i(t)=t\pi_i+o_p(n),
\]
simultaneously for every fixed finite selection of parts and deterministic times.

Let \(C_m\) be the number of independent uniform draws from \(m\) coupons needed to see every coupon. The streams give \(k\) independent completion counts \(C_{m_i}\). At the starting part one vertex was already seen at time zero. Coupling against an ordinary coupon stream changes that part's completion count only when the fixed initial vertex would have been the last distinct coupon in the ordinary stream, an event of probability \(1/m_i\). Thus, up to a probability \(O(1/n)\), every event \(\{\tau_{i,n}\le t_i\}\) agrees simultaneously with \(\{C_{m_i}\le V_i(t_i)\}\), for any specified deterministic \(t_i\).

The elementary coupon-collector Gumbel limit is
\[
\Pr\{C_m\le m\log m+my\}\longrightarrow\exp(-e^{-y}).
\]
For completeness, the number of unseen coupons after \(\lfloor m\log m+my\rfloor\) draws has \(r\)-th factorial moment \((m)_r(1-r/m)^{\lfloor m\log m+my\rfloor}\to e^{-ry}\), for every fixed nonnegative integer \(r\). Hence the missing count tends to \(\operatorname{Poisson}(e^{-y})\), proving the displayed formula.

The expansions under the critical-window assumptions are
\[
\pi_i=\frac1k\left[1+\frac{k-2}{k-1}\left(\theta_i-\frac\Theta k\right)\frac1{\log n}+o\!\left(\frac1{\log n}\right)\right],
\qquad
m_i\log m_i=n\log n+\theta_i n+o(n).
\]
For any fixed real \(x_i\), put \(t_i=\lfloor kn(\log n+A+x_i)\rfloor\). It follows that
\[
\frac{\pi_i t_i-m_i\log m_i}{m_i}\longrightarrow x_i-\frac{\theta_i}{k-1}.
\]
Combining class-visit concentration with the independent coupon streams, squeeze each local random clock between deterministic clocks separated by \(\varepsilon n\), then send \(\varepsilon\downarrow0\). The joint cumulative distribution is therefore
\[
\Pr\{\tau_{i,n}\le t_i\ \text{for all }i\}\longrightarrow
\prod_i\exp\left(-e^{-x_i+\theta_i/(k-1)}\right).
\]
This proves the joint convergence, including asymptotic independence of the shifted Gumbel coordinates. The continuous maximum mapping proves the cover-time law. The shifted Gumbels have no ties, so the argmax mapping also applies. Writing \(G_i=-\log E_i\) for independent rate-one exponentials \(E_i\) shows that their shifted argmax is the minimum among independent exponentials with rates \(e^{\theta_i/(k-1)}\), proving the softmax probabilities.

Finally, under the broader imbalance assumptions, the same coupon and class-clock bounds yield
\[
\tau_{i,n}=b_i+O_p(n),\qquad b_i=\frac{S}{N-m_i}\log m_i.
\]
For fixed \(N\), the function \(g(x)=\log x/(N-x)\) has positive derivative
\[
g'(x)=\frac{(N-x)/x+\log x}{(N-x)^2}.
\]
Uniformly for \(x/n\to1\), we have \(Sg'(x)\sim k\log n/(k-1)\). The mean-value theorem now gives
\[
b_{i_*}-b_j\sim\frac{k}{k-1}(m_{i_*}-m_j)\log n\gg n.
\]
The tight \(O_p(n)\) remainder cannot reverse these inequalities, proving unique-part dominance.

## Verification
The accompanying standalone standard-library program `check.py` computes exact absorbing Markov-chain last-part probabilities for small multipartite graphs, checks the stationary distribution algebraically with rational arithmetic, verifies critical-window clock expansions numerically, and performs reproducible walk simulations. Its finite checks and simulations are not substitutes for the limiting argument above. The exact finite values for a walk starting in the first part include \((0,1/2,1/2)\) on \(K_{1,1,1}\) and \((23/105,41/105,41/105)\) on \(K_{2,2,2}\).

## Relationship to prior work
Tishby, Biham and Katzav (first posted October 26, 2021) studied cover-time distributions and Gumbel behavior in random regular graphs. Buchanan, Horn and Rombach (first posted September 16, 2022) studied which directed graphs have uniform last-new-vertex probabilities; their theorem is not a multipartite asymptotic probability formula. Chang and Xu (2015) studied hitting times and symmetry for complete multipartite walks, according to the available published abstract; full text could not be inspected. A previously recorded complete-bipartite analysis proves a two-part logistic imbalance window. It does not imply the result here for \(k\ge3\): the class chain is no longer deterministic alternation and the softmax sensitivity is attenuated by \(1/(k-1)\). General hitting-time formulas or regular-graph cover-time marginals do not alone supply the joint, part-labeled completion law proved here.

## Limitations
Only the fixed-\(k\), nearly equal part-size regime is addressed; heterogeneous macroscopic part proportions, growing \(k\), lazy dynamics, directed graphs, and finite-\(n\) convergence rates are not covered. The finite-state checks do not establish the infinite limit. Historical priority is provisional, especially because the full 2015 Chang–Xu paper was inaccessible during review. No independent mathematical validation has been performed.

## References
- I. Tishby, O. Biham, E. Katzav, *Analytical results for the distribution of cover times of random walks on random regular graphs*, arXiv:2110.13592 (first posted October 26, 2021). https://arxiv.org/abs/2110.13592
- C. Buchanan, P. Horn, P. Rombach, *On the Last New Vertex Visited by a Random Walk in a Directed Graph*, arXiv:2209.08079 (first posted September 16, 2022). https://arxiv.org/abs/2209.08079
- X. Chang, H. Xu, *Random walks on complete multipartite graphs*, Pure and Applied Mathematics Quarterly 11 (2015), 393–402, doi:10.4310/PAMQ.2015.v11.n3.a1. https://doi.org/10.4310/PAMQ.2015.v11.n3.a1
- N. Rivera, T. Sauerwald, J. Sylvester, *Multiple Random Walks on Graphs: Mixing Few to Cover Many*, ICALP 2021, DOI:10.4230/LIPIcs.ICALP.2021.107. https://doi.org/10.4230/LIPIcs.ICALP.2021.107
