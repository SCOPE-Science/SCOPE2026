# Reentrant variance matching and accelerated Poisson approximation for band-pass neighbour thinning

## Finding
For fixed \(\tau>0\) and integer \(n>2\tau\), let \(X_n\) be a homogeneous Poisson process of intensity \(n\) on the circumference-one circle \(\mathbb T\). Put \(r_n=\tau/(2n)\). Independently for each original point, retain it with probability
\[
\frac1n\,\mathbf 1\{1\le N_{r_n}(x;X_n)\le3\},
\]
where \(N_{r_n}\) counts **other original points**, not retained points, within circular distance \(r_n\). Let \(Y_n\) count retained points, and set
\[
\alpha(\tau)=e^{-\tau}\left(\tau+\frac{\tau^2}{2}+\frac{\tau^3}{6}\right).
\]
Define
\[
\begin{aligned}
I(\tau)={}&\left(\frac{\tau^2}{2}+4\tau+9\right)e^{-\tau}\\
&+\left(\frac{\tau^6}{2304}+\frac{7\tau^5}{384}+\frac{17\tau^4}{64}+\frac{79\tau^3}{48}+\frac{35\tau^2}{8}+\frac{11\tau}{2}\right)e^{-3\tau/2}\\
&-\left(\frac{\tau^7}{36}+\frac{7\tau^6}{36}+\frac{11\tau^5}{12}+3\tau^4+8\tau^3+15\tau^2+18\tau+9\right)e^{-2\tau}.
\end{aligned}
\]
Then the following statements hold for every fixed \(\tau>0\):

1. The identities \(\mathbb E Y_n=\alpha(\tau)\) and \(\operatorname{Var}(Y_n)-\mathbb E Y_n=2I(\tau)/n\) are **exact** for every integer \(n>2\tau\).
2. Writing \(p_\alpha(k)=e^{-\alpha}\alpha^k/k!\) when \(k\ge0\), and zero otherwise, the signed count-law expansion is
\[
\sum_{k\ge0}\left|\mathbb P(Y_n=k)-p_{\alpha(\tau)}(k)-\frac{I(\tau)}n\big[p_{\alpha(\tau)}(k)-2p_{\alpha(\tau)}(k-1)+p_{\alpha(\tau)}(k-2)\big]\right|=O_\tau(n^{-2}).
\]
Consequently, if \(I(\tau)\ne0\), total variation from \(\operatorname{Poisson}(\alpha(\tau))\) is \(\Theta_\tau(n^{-1})\); if \(I(\tau)=0\), it is \(O_\tau(n^{-2})\).
3. Exact rational bounds on the exponential series establish \(I(2)>0\), \(I(3)<0\), and \(I(4)>0\). Hence there exist **at least two distinct critical values**, \(\tau_-\in(2,3)\) and \(\tau_+\in(3,4)\), where variance is exactly Poisson-matched for every sufficiently large \(n\), and the Poisson total-variation rate improves to \(O_\tau(n^{-2})\). No uniqueness or exact root formulas are claimed.

## Assumptions and scope
The distance is the geodesic distance on the unit circle, underlying points constitute a homogeneous Poisson process of mean count \(n\), and all retention uniforms are independent conditional on the **underlying** process. The critical-range parameter \(\tau\) is fixed as \(n\to\infty\). The inequality \(n>2\tau\) ensures that the two interaction neighborhoods do not wrap into anomalous self-overlap when evaluating separations of at most twice the interaction radius. Bounds hidden in \(O_\tau(\cdot)\) need not be uniform as \(\tau\) varies.

## Proof
**One- and two-point Palm calculations.** By the one-point Mecke identity, the number of original neighbors of a typical point is \(\operatorname{Poisson}(\tau)\). Its retention probability is \(\alpha(\tau)/n\), so \(\mathbb E Y_n=\alpha(\tau)\). Two Palm points separated by circular distance \(u/n\), with \(0\le u\le\tau\), have Poisson input in the overlap of their \(r_n\)-balls of mean \(\tau-u\) and independent input in each exclusive portion of mean \(u\). Each Palm point contributes one extra neighbor precisely when \(u\le\tau/2\). Let \(U\sim\operatorname{Poisson}(\tau-u)\) and \(V,W\sim\operatorname{Poisson}(u)\) be independent and define
\[
m(u;\tau)=\mathbb P\big(1\le U+V+b\le3,\ 1\le U+W+b\le3\big),\quad b=\mathbf1\{u\le\tau/2\}.
\]
For points separated by more than \(2r_n\), the Palm retention factors are independent and their product expectation is \(\alpha(\tau)^2\). By the second-order Mecke identity and integration over circular displacements,
\[
\operatorname{Var}(Y_n)-\mathbb E Y_n=\frac2n\int_0^\tau\big(m(u;\tau)-\alpha(\tau)^2\big)du.
\]
The two regions are finite Poisson sums. Explicitly, \(m(u;\tau)=e^{-\tau-u}Q_b(u,\tau)\), with
\[
Q_b(u,\tau)=\sum_{j=0}^{3-b}\frac{(\tau-u)^j}{j!}\left(\sum_{v=\max(0,1-b-j)}^{3-b-j}\frac{u^v}{v!}\right)^2.
\]
(The inner sum is zero when its upper limit is below its lower limit.) Integrating \(Q_1\) over \([0,\tau/2]\) and \(Q_0\) over \([\tau/2,\tau]\), then subtracting \(\tau\alpha(\tau)^2\), yields the displayed explicit exponential polynomial \(I(\tau)\), proving the two exact identities.

**Distributional correction, with a uniform remainder.** For any integer \(k\ge2\), consider the \(k\)-fold Mecke formula. Because the underlying intensity \(n^k\) cancels \(n^{-k}\) retention factors, \(\mathbb E(Y_n)_k\) is the integral over \(\mathbb T^k\) of the joint expected product of the band-pass marks. Form the graph connecting Palm points at circular separation at most \(2r_n=\tau/n\). If there are no graph edges, all neighborhoods are disjoint, so the integrand is \(\alpha^k\). If there is exactly one graph edge, its two-point factor is \(m(u;\tau)\) and the other \(k-2\) factors equal \(\alpha\). Configurations with at least two specified graph edges have total measure at most \(C_\tau k^4/n^2\), by a union bound over pairs of edges and conditional independence of fresh uniform points (whether or not edges share a vertex). On those configurations, the integrands and the corresponding one-edge approximations are bounded by one. Thus uniformly in every integer \(k\ge2\),
\[
\mathbb E(Y_n)_k=\alpha^k+\binom k2\frac{2I(\tau)}n\alpha^{k-2}+O_\tau(k^4/n^2).
\]
The same formula holds for \(k=0,1\) with zero remainder. As every factorial moment is at most one, the factorial-moment generating series is entire. Summing the uniformly bounded remainder with weights \(|z-1|^k/k!\) gives, uniformly on each fixed complex disc,
\[
\mathbb Ez^{Y_n}=e^{\alpha(z-1)}\left[1+\frac{I(\tau)}n(z-1)^2\right]+O_{\tau,R}(n^{-2}),\qquad |z|\le R.
\]
Take any \(R>1\). Cauchy's coefficient bound makes the sum of absolute coefficient errors \(O_\tau(n^{-2})\). This proves the claimed signed Poisson–Charlier formula. Since the coefficient sequence \(p_\alpha(k)-2p_\alpha(k-1)+p_\alpha(k-2)\) is nonzero and absolutely summable, its leading nonzero multiple yields the lower and upper \(\Theta(n^{-1})\) total-variation rate when \(I\ne0\).

**Two distinct tuning windows.** The exponential-polynomial formula for \(I\) is continuous on \((0,\infty)\). Using exact rational arithmetic, the companion verifier encloses every needed \(e^{-x}\) by reciprocals of truncated positive exponential series with an explicit geometric tail bound. It establishes the strict rational signs \(I(2)>0\), \(I(3)<0\), \(I(4)>0\); the intermediate value theorem produces at least one root in each of the disjoint intervals.

## Verification
Run the standalone Python 3 checker `verify_bandpass.py` without third-party dependencies. It reconstructs the exponential polynomial by exact polynomial/Palm integral algebra, verifies the polynomial coefficients, checks the rational exponential enclosures at \(\tau=2,3,4\), and checks the nonvanishing of the Poisson–Charlier second difference. Numeric values are illustrations only: \(I(2)\approx0.08304943\), \(I(3)\approx-0.00694674\), \(I(4)\approx0.04097500\). The infinite-order conclusion is proved by the factorial-moment and analytic-coefficient arguments above, not by numerical testing.

## Relationship to prior work
Hlyniana, *Neighbour-count dependent thinning of Poisson processes: correlation structure and Poisson approximation* (arXiv:2511.10083), provides the arbitrary-rule two-ball correlation formula and general connected-graph factorial-cumulant bounds. Those tools underlie, but do not themselves identify, two distinct finite-\(\tau\) sign reversals for the natural band-pass retention rule. Hlyniana, *A law of thin processes with neighbour-count thinning* (arXiv:2609.25733), establishes the first-order Poisson limit under critical spatial scaling. The focus here is the special rule's exact reentrant variance matching and the resulting cancellation of the leading distributional error. The general pair-correlation formula, Poisson limit, and generic factorial-cumulant methods are not claimed as new.

## Limitations
This theorem concerns one spatial dimension, homogeneous Poisson input, a particular band-pass rule, and a total retained **count**, not the full spatial retained process. It proves existence of at least two roots, not uniqueness or all-root classification. The \(O(n^{-2})\) improvement only concerns count total variation at fixed tuning \(\tau\); no claim about faster convergence of the full point process is made. Familiar Poisson factorial-moment identities and finite-range graph estimates do not confer independent validation of the result; independent audit has not been performed.

## References
1. K. Hlyniana, *Neighbour-count dependent thinning of Poisson processes: correlation structure and Poisson approximation*, arXiv:2511.10083 (first posted 2025-11-13), revised 2026-09-22. https://arxiv.org/abs/2511.10083
2. K. Hlyniana, *A law of thin processes with neighbour-count thinning*, arXiv:2609.25733 (first posted 2026-09-22). https://arxiv.org/abs/2609.25733
3. G. Last and M. Penrose, *Lectures on the Poisson Process*, Cambridge University Press, 2018, for Mecke's identity and Poisson Palm calculus.
