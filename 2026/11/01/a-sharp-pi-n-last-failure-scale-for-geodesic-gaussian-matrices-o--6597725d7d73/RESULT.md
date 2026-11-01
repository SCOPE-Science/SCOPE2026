# A sharp \(\pi/n\) last-failure scale for geodesic Gaussian matrices on finite cycles

## Finding
For every integer \(n\ge3\), let \(C_n=\mathbb Z/n\mathbb Z\) with graph distance
\[
d_n(a,b)=\min\{|a-b|,n-|a-b|\},
\]
where \(|a-b|\) is the representative difference in \(\{0,1,\ldots,n-1\}\). Define the real symmetric \(n\)-by-\(n\) matrix
\[
K_n(t)_{ab}=\exp\bigl(-t\,d_n(a,b)^2\bigr),\qquad t>0.
\]
Define the last-indefiniteness scale, without assuming that the positive-definite parameter set is an interval, by
\[
\tau_n=\sup\bigl(\{t>0:K_n(t)\text{ has a negative eigenvalue}\}\cup\{0\}\bigr).
\]
Then \(\tau_n\) is finite for each \(n\), and
\[
\boxed{\lim_{n\to\infty} n\tau_n=\pi.}
\]
More precisely, for every \(0<\varepsilon<\pi\), there is an integer \(N_\varepsilon\) such that, for all \(n\ge N_\varepsilon\):

* \(K_n(t)\) is **strictly positive definite simultaneously for every** \(t\ge(\pi+\varepsilon)/n\);
* \(K_n((\pi-\varepsilon)/n)\) has a strictly negative eigenvalue.

This implies the sharp leading threshold in physical unit-circle coordinates. For points at angles \(2\pi a/n\), write the arc-distance Gaussian as \(\exp(-\lambda\,\delta(a,b)^2)\), with \(\delta=2\pi d_n/n\). The last-indefiniteness parameter in that convention is asymptotic to \(n/(4\pi)\).

## Assumptions and scope
All matrices are over \(\mathbb R\), and positive definite means a strictly positive quadratic form on all nonzero real vectors. The parameter \(t\) is positive and unnormalized by the circumference. There is no claim of uniqueness of a finite-\(n\) crossing, no claim about monotonicity in \(t\), and no claim about the sign at \(t=\tau_n\). The limit concerns all integers \(n\to\infty\), without restricting parity or congruence classes.

## Proof
**1. Exact Fourier decomposition.** Since \(K_n(t)\) is circulant, all of its eigenvalues are real and have the form
\[
L_{n,j}(t)=\sum_{r=0}^{n-1}e^{-t\min(r,n-r)^2}\cos\left(\frac{2\pi jr}{n}\right),\quad 0\le j<n.
\]
For a real \(\theta\), put
\[
\Theta_t(\theta)=\sum_{r\in\mathbb Z}e^{-tr^2}e^{ir\theta}
=\sqrt{\frac\pi t}\sum_{k\in\mathbb Z}\exp\left(-\frac{(\theta+2\pi k)^2}{4t}\right).
\]
The second equality is the Gaussian Poisson-summation formula. On \(\theta\in[-\pi,\pi]\), all terms are positive, giving
\[
\Theta_t(\theta)\ge \sqrt{\frac\pi t}\,e^{-\pi^2/(4t)}.\tag{1}
\]
Writing \(\theta_j=2\pi j/n\), the difference \(\Theta_t(\theta_j)-L_{n,j}(t)\) consists of omitted Gaussian lattice terms. For odd \(n\), the finite frequency sum uses the representatives \(-\lfloor n/2\rfloor,\ldots,\lfloor n/2\rfloor\). For even \(n\), it uses \(-n/2+1,\ldots,n/2\). In either case every omitted integer has magnitude at least \(n/2\). Consecutive terms beyond that magnitude have ratio at most \(e^{-tn}\). Consequently
\[
\bigl|\Theta_t(\theta_j)-L_{n,j}(t)\bigr|
\le \frac{2e^{-tn^2/4}}{1-e^{-tn}}.\tag{2}
\]

**2. Uniform positivity above the constant \(\pi\).** Fix \(a>\pi\). For \(a/n\le t\le1\), (1)--(2) show that the ratio of the absolute truncation error to the positive theta value is at most
\[
\frac{2\sqrt{t/\pi}}{1-e^{-a}}
\exp\left(\frac{\pi^2}{4t}-\frac{tn^2}{4}\right)
\le \frac{2}{\sqrt\pi(1-e^{-a})}
\exp\left[-\frac{a^2-\pi^2}{4a}\,n\right].\tag{3}
\]
Here \(t\mapsto\pi^2/(4t)-tn^2/4\) is strictly decreasing. The right side tends to zero, uniformly across all Fourier indices and all \(t\in[a/n,1]\). Every eigenvalue is therefore strictly positive for sufficiently large \(n\). For \(t\ge1\), the absolute sum of the off-diagonal entries in any row is bounded by
\[
2\sum_{r\ge1}e^{-tr^2}\le\frac{2e^{-t}}{1-e^{-3t}}\le\frac{2e^{-1}}{1-e^{-3}}<1.
\]
Strict diagonal dominance of the symmetric matrix proves positivity in the remaining range. Thus **all** \(t\ge a/n\) are admissible for sufficiently large \(n\).

**3. A negative Fourier mode below the constant \(\pi\): even orders.** Fix \(c\in(0,\pi)\), and set \(t=c/n\). Suppose \(n=2m\). If \(m\) is even, take \(j=m\) and \(\eta=0\); if \(m\) is odd, take \(j=m-1\) and \(\eta=1\). In both cases \(j\) is even and \(\theta_j=\pi-2\pi\eta/n\). The omitted term at \(-m\) and the two tails give the **exact** identity
\[
\Theta_t(\theta_j)-L_{n,j}(t)
=e^{-tm^2}\left[1+2\sum_{q=1}^\infty(-1)^q
 e^{-t(2mq+q^2)}\cos\left(\frac{2\pi\eta q}{n}\right)\right].\tag{4}
\]
By dominated convergence, the bracket tends to
\[
1+2\sum_{q\ge1}(-e^{-c})^q
=\frac{1-e^{-c}}{1+e^{-c}}>0.\tag{5}
\]
On the other hand, the Poisson representation, with \(\theta_j=\pi+O(1/n)\), gives
\[
\Theta_{c/n}(\theta_j)
=O_c\left(\sqrt n\,e^{-\pi^2 n/(4c)}\right).\tag{6}
\]
The positive difference in (4) has order \(e^{-cn/4}\), and \(\pi^2/(4c)>c/4\). Thus \(L_{n,j}(c/n)<0\) for all sufficiently large even \(n\).

**4. A negative Fourier mode below \(\pi\): odd orders.** Suppose \(n=2m+1\). Choose \(b=1\) if \(m\) is even and \(b=3\) if \(m\) is odd; take \(j=(n-b)/2\). For large \(n\) this is an admissible Fourier index, with \(\theta_j=\pi-b\pi/n\). Put \(r_0=(n+1)/2\). The exact omitted-tail identity is
\[
\Theta_t(\theta_j)-L_{n,j}(t)
=2e^{-t r_0^2}\sum_{q=0}^\infty (-1)^q
 e^{-t(2r_0q+q^2)}
 \sin\left(\frac{b\pi(q+1/2)}n\right).\tag{7}
\]
At \(t=c/n\), dominated convergence applies after multiplication by \(n e^{tr_0^2}/(2b\pi)\), because \(n|\sin(b\pi(q+1/2)/n)|/(b\pi)\le q+1/2\) and the Gaussian ratios are bounded by \(e^{-cq}\). The resulting series is
\[
\sum_{q=0}^\infty(-1)^q(q+1/2)e^{-cq}
=\frac{1-e^{-c}}{2(1+e^{-c})^2}>0.\tag{8}
\]
Hence the positive difference in (7) is asymptotic to
\[
\frac{b\pi}{n}\frac{1-e^{-c}}{(1+e^{-c})^2}
\exp\left(-\frac{c(n+1)^2}{4n}\right),\tag{9}
\]
whereas the theta term still satisfies (6). The exponential gap \(\pi^2/(4c)>c/4\) dominates the extra factor \(1/n\), so \(L_{n,j}(c/n)<0\) for all sufficiently large odd \(n\).

**5. The sharp limit.** For any \(0<\varepsilon<\pi\), part 2 with \(a=\pi+\varepsilon\) forces \(\tau_n\le(\pi+\varepsilon)/n\) eventually. Parts 3--4 with \(c=\pi-\varepsilon\) force \(\tau_n\ge(\pi-\varepsilon)/n\) eventually. Squeezing proves \(n\tau_n\to\pi\). All \(\tau_n\) are finite because diagonal dominance holds for \(t\ge1\). Finally, \(t=(4\pi^2/n^2)\lambda\) establishes the physical-circle scaling stated above.

## Verification
The accompanying Python program `check_cycle_gaussian.py` uses 100-digit arithmetic to compute the relevant cyclic Fourier eigenvalues, their theta/truncation comparison, and the uniform-positive error bound. It passed for \(n=40,41,42,43,80,81,82,83,120,121,122,123\) at both \(t=(\pi-0.5)/n\) and \(t=(\pi+0.5)/n\), covering every residue modulo four. The calculated negative eigenvalues are extremely small in larger instances, so ordinary double precision is not an appropriate sign certificate. The checker also compares independent finite Fourier expressions at smaller orders. These finite tests are corroboration; the quantified asymptotic assertion is proved by (1)--(9).

## Relationship to prior work
Feragen, Lauze, and Hauberg [1] established restrictions on geodesic Gaussian kernels being positive definite for every bandwidth, but did not derive a finite-grid asymptotic cutoff. Feragen and Hauberg [2] explicitly discussed nontrivial finite-sample positive-definite bandwidth ranges. Da Costa, Mostajeran, and Ortega [3] used evenly spaced circle samples and partial-theta estimates to show that no fixed Gaussian scale is positive definite on the entire geodesic circle. Their fixed-scale obstruction does not determine the simultaneous high-bandwidth positive region or the sharp constant in a growing sample-size threshold. Wood [4] studied covariance functions truncated onto a continuous circle; its bibliographic abstract does not establish a finite-grid cutoff. The present result quantifies the deterministic last-failure scale across **every** sample size, including odd orders. The Poisson identity and Fourier diagonalization are standard tools, not new claims.

## Limitations
The theorem gives only the first-order asymptotic cutoff, not a finite-\(n\) exact root formula or a correction term. It does not establish that the positive-definite set is connected for any fixed \(n\). The scope is equally spaced samples and squared intrinsic arc distance; irregular sampling and other powered distances are not covered. Novelty checks were bounded by accessible literature and search records, and an equivalent formula in less accessible historical covariance literature remains possible. No independent mathematical audit has been performed.

## References
1. A. Feragen, F. Lauze, and S. Hauberg, *Geodesic Exponential Kernels: When Curvature and Linearity Conflict*, arXiv:1411.0296v1 (first posted 2014-11-02), https://arxiv.org/abs/1411.0296.
2. A. Feragen and S. Hauberg, *Open Problem: Kernel methods on manifolds and metric spaces. What is the probability of a positive definite geodesic exponential kernel?*, Proceedings of Machine Learning Research 49 (2016), pp. 1647–1650, https://proceedings.mlr.press/v49/feragen16.html.
3. N. Da Costa, C. Mostajeran, and J.-P. Ortega, *The Gaussian kernel on the circle and spaces that admit isometric embeddings of the circle*, arXiv:2302.10623v1 (2023), https://arxiv.org/abs/2302.10623.
4. A. T. A. Wood, *When is a truncated covariance function on the line a covariance function on the circle?*, Statistics & Probability Letters 24 (1995), pp. 157–164, DOI:10.1016/0167-7152(94)00162-2.
