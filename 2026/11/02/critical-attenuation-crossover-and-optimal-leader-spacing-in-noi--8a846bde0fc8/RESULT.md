# Critical attenuation crossover and optimal leader spacing in noisy directed rings

## Finding
For a one-way directed ring of \(n\ge2\) vertices with exactly \(1\le k\le n\) noise-free pinned leaders, independent unit-intensity Brownian disturbances at followers, and predecessor-feedback gain \(0<\rho\le1\), all minimum-total-variance leader configurations have **exactly** the most balanced cyclic gaps: the numbers of followers between consecutive leaders differ by at most one. This is an exhaustive classification, including ties.

Put \(N=n-k\), \(a=\lfloor N/k\rfloor\), \(r=N-ka\), and \(C_j=\binom{2j}{j}4^{-j}\). Define
\[
\Phi_\rho(\ell)=\frac12\sum_{j=0}^{\ell-1}(\ell-j)C_j\rho^{2j},\qquad \Phi_\rho(0)=0.
\]
Then the exact optimum is
\[
J^*_{n,k}(\rho)=(k-r)\Phi_\rho(a)+r\Phi_\rho(a+1),
\]
and the number of distinct optimal \(k\)-subsets of labelled ring vertices is \(\frac nk\binom{k}{r}\). At the critical gain \(\rho=1\),
\[
\Phi_1(\ell)=\frac{\ell(2\ell+1)}3\frac{\binom{2\ell}{\ell}}{4^\ell}.
\]

There is a sharp attenuation-size crossover. For fixed \(k\), if \(\rho_n\in(0,1]\) satisfies \(n(1-\rho_n)\longrightarrow c\in[0,\infty)\), then
\[
\lim_{n\to\infty}\frac{J^*_{n,k}(\rho_n)}{n^{3/2}}
=F_k(c):=\frac{k}{2\sqrt\pi}\int_0^{1/k}
\left(\frac1k-u\right)u^{-1/2}e^{-2cu}\,du.
\]
The crossover is positive and strictly decreasing in \(c\), with
\[
F_k(0)=\frac{2}{3\sqrt{\pi k}},\qquad
F_k(c)\sim\frac1{2\sqrt{2c}}\quad(c\to\infty).
\]
Conversely, if \(\rho_n\to1\) and \(n(1-\rho_n)\to\infty\), then
\[
J^*_{n,k}(\rho_n)\sim\frac{n}{2\sqrt{1-\rho_n^2}}.
\]
For a fixed \(0<\rho<1\), this becomes \(J^*_{n,k}(\rho)=\frac{n}{2\sqrt{1-\rho^2}}+O_{k,\rho}(1)\). Hence a fixed number of leaders changes the leading \(n^{3/2}\) cost at criticality, while fixed attenuation gives leading linear cost independent of that fixed budget.

## Assumptions and scope
Index the labelled vertices cyclically. Each follower \(i\notin S\) obeys the Itô stochastic differential equation
\[
dX_i(t)=\bigl(-X_i(t)+\rho X_{i-1}(t)\bigr)\,dt+dW_i(t),
\]
where \(i-1\) is its sole predecessor, indices are cyclic, and independent standard Brownian motions \(W_i\) drive the followers. A pinned leader has \(X_s(t)\equiv0\). The quantity optimized is the sum of stationary follower variances, \(J_{n,k}(S;\rho)=\sum_{i\notin S}\lim_{t\to\infty}\mathbb E[X_i(t)^2]\); centered initial conditions are not required because the follower dynamics are Hurwitz. We optimize over exactly \(k\) pinned vertices, not variable gains, heterogeneous disturbance intensities, or weighted/undirected edges. A predecessor gain \(\rho<1\) is local attenuation; it is not claimed to be a conservative, leak-free consensus Laplacian. At \(\rho=0\) all placements tie, so strict optimal-set classification is explicitly restricted to \(\rho>0\).

## Proof
Choose a pinned vertex as a cyclic starting point. Deleting the pinned coordinates decomposes the follower system into \(k\) directed path blocks of lengths \(\ell_1,\ldots,\ell_k\), allowing zero lengths, with \(\sum_j\ell_j=n-k\). A length-\(\ell\) block has drift matrix \(-I+\rho T\), where \(T\) is the strictly lower one-step shift; its eigenvalues are all \(-1\), so its stationary covariance exists uniquely.

Because \(T^\ell=0\), the impulse response from noise at position \(p\) to follower position \(i\ge p\) is \(e^{-t}(\rho t)^{i-p}/(i-p)!\). Integration of its squared magnitude over positive time yields \(\frac12\binom{2h}{h}4^{-h}\rho^{2h}\) for offset \(h=i-p\). Summing over all source positions and then over all followers proves
\[
J_{n,k}(S;\rho)=\sum_{j=1}^k\Phi_\rho(\ell_j).
\]
Writing \(\Delta\Phi(\ell)=\Phi(\ell+1)-\Phi(\ell)\) gives
\[
\Delta\Phi_\rho(\ell)=\frac12\sum_{h=0}^{\ell}C_h\rho^{2h},\quad
\Delta\Phi_\rho(\ell+1)-\Delta\Phi_\rho(\ell)
=\frac12 C_{\ell+1}\rho^{2\ell+2}>0.
\]
Thus if two gap lengths differ by at least two, shortening the longer one and lengthening the shorter one strictly decreases the cost. Repeating establishes both existence and exclusivity of the balanced gap vectors. Their objective gives the exact displayed formula. Every labelled leader set is counted \(k\) times by selecting its distinguished starting leader, while there are \(n\binom{k}{r}\) pairs consisting of a starting vertex and a choice of which \(r\) of the \(k\) gaps have length \(a+1\). Hence the optimizer count is \(\frac nk\binom{k}{r}\), an integer.

For the critical closed form, use \(C_{\ell+1}/C_\ell=(2\ell+1)/(2\ell+2)\). The identity \(\sum_{j=0}^{\ell-1}C_j=2\ell C_\ell\), together with summation by parts, yields \(\Phi_1(\ell)=\ell(2\ell+1)C_\ell/3\).

Fix \(k\) and suppose \(n(1-\rho_n)\to c<\infty\). For each balanced gap \(\ell_n/n\to 1/k\). The central-binomial asymptotic \(C_h\sim (\pi h)^{-1/2}\) and \(\rho_n^{2\lfloor un\rfloor}\to e^{-2cu}\) turn the normalized exact sum into the displayed integral. To justify the integrable singularity at zero, bound \(C_h\le K(h+1)^{-1/2}\), split the sum into \(h\le\delta n\) and \(h>\delta n\), bound the first contribution uniformly by \(O(\sqrt\delta)\), then pass to the Riemann-integral limit and let \(\delta\downarrow0\). The same argument includes \(c=0\). Elementary integration gives \(F_k(0)=2/(3\sqrt{\pi k})\); dominated differentiation makes \(F_k\) strictly decreasing, and the change of variables \(v=2cu\) gives its large-\(c\) asymptotic.

For the strongly attenuated near-critical regime, set \(z=\rho_n^2<1\). The generating functions
\[
\sum_{h\ge0}C_h z^h=(1-z)^{-1/2},\qquad
\sum_{h\ge0}hC_h z^h=\frac{z}{2(1-z)^{3/2}}
\]
imply, for every nonnegative integer \(\ell\),
\[
0\le\frac{\ell}{2\sqrt{1-z}}-\Phi_{\sqrt z}(\ell)
\le\frac{z}{4(1-z)^{3/2}}.
\]
Summing over \(k\) balanced gaps yields \(J^*_{n,k}(\rho_n)=(n-k)/(2\sqrt{1-z})+O(k(1-z)^{-3/2})\). When \(n(1-\rho_n)\to\infty\), its remainder is little-oh of its main term. For a fixed subcritical \(\rho\), the remainder is bounded independently of \(n\), proving the final assertion.

## Verification
A standalone exact-rational checker, `verify_directed_ring.py`, reconstructs stationary covariance blocks directly from their Lyapunov equations. It verifies the exact cost formula, positive second differences, the critical-gain closed form, and exhaustively compares all leader subsets on small rings. It additionally checks the critical-window Riemann-integral limit numerically. The checker reports 33 exact Lyapunov blocks, 6105 enumerated leader sets, 1365 balancing-optimal sets, and 16 numerical crossover tests. These finite tests corroborate but do not replace the infinite-family proof given above.

## Relationship to prior work
Lin, Fardad, and Jovanović (2012) compute the variance-growth behavior of singly rooted unidirectional paths; Fu Lin (2016) gives their exact central-binomial covariance and \(\sqrt{\ell}\) pointwise growth. The \(\rho=1\) single-path formula here is therefore **not claimed as new**. Patterson, McGlohon, and Dyagilev (2014) optimize leader selection on **undirected** paths and rings, where a symmetric grounded inverse determines variance. Here, by contrast, the nonnormal directed Lyapunov covariance is optimized for all \(k\) on a ring and for every attenuated gain; the coupled \(n(1-\rho_n)\) critical window provides a uniform crossover law. No inspected source establishes the combination of strict directed-gap optimization and this attenuation-size scaling law.

## Limitations
This theorem concerns a homogeneous one-way ring with perfectly pinned states and independent unit Brownian disturbances. Heterogeneous gains, correlated noise, uncertain leaders, bidirectional feedback, and optimization of feedback gain rather than pinned vertices are outside scope. The \(\rho=0\) degeneracy is excluded from the strict classifier. Publication priority is not independently certified; specialized prior work could contain an equivalent multi-leader or attenuation law. Computer checks do not establish the asymptotic theorem independently.

## References
1. F. Lin, M. Fardad, and M. R. Jovanović, *Performance of leader-follower networks in directed trees and lattices*, IEEE CDC (2012), pp. 734–739. DOI: 10.1109/CDC.2012.6425879. Open full text: https://ecs.syr.edu/faculty/fardad/Papers/LinFarJov12d.pdf
2. F. Lin, *Performance of leader-follower multi-agent systems in directed networks*, arXiv:1606.02269 (first posted 2016-06-07). Open full text: https://arxiv.org/html/1606.02269v2
3. S. Patterson, N. McGlohon, and K. Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595 (first posted 2014-12-20). Open full text: https://arxiv.org/pdf/1412.6595
