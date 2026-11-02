# A universal collision-exponent moment law for random-node polynomial interpolation

## Finding

Fix any integer \(n\ge2\) and real \(\theta\ge0\). On \([0,1]^n\), sample distinct labeled nodes from the joint probability density
\[
 p_{n,\theta}(x)=Z_{n,\theta}^{-1}\prod_{1\le i<j\le n}|x_i-x_j|^{\theta},\quad
 Z_{n,\theta}=\int_{[0,1]^n}\prod_{i<j}|x_i-x_j|^{\theta}\,dx.
\]
Let \(\ell_i(t)=\prod_{j\ne i}(t-X_j)/(X_i-X_j)\) be the fundamental Lagrange polynomials, and let \(\Lambda=\max_{t\in[0,1]}\sum_{i=1}^n|\ell_i(t)|\). Then for every \(q>0\),
\[
 \mathbb E\Lambda^q<\infty\quad\Longleftrightarrow\quad q<\theta+1.
\]
In particular, mean-square worst-case nodal-noise amplification is finite exactly when \(\theta>1\), irrespective of \(n\). Independent uniform nodes (\(\theta=0\)) fail even to have finite mean amplification, whereas the polynomial projection determinantal ensemble (\(\theta=2\)) has finite quadratic amplification.

For \(n=2\), the complete tail is explicit. For every \(t\ge1\),
\[
 \Pr(\Lambda>t)=2\left(\frac{2}{1+t}\right)^{\theta+1}-t^{-(\theta+1)},
 \qquad \lim_{t\to\infty}t^{\theta+1}\Pr(\Lambda>t)=2^{\theta+2}-1.
\]
Consequently, when \(\theta>0\), \(\mathbb E\Lambda=1+3/\theta\); and when \(\theta>1\), \(\mathbb E\Lambda^2=(\theta^2+5\theta+8)/[\theta(\theta-1)]\).

There is a pointwise noise counterpart. Fix any \(f\in C^{n-1}([0,1])\), \(t_0\in[0,1]\) and \(\sigma>0\). Given the nodes, observe \(Y_i=f(X_i)+\varepsilon_i\), where the \(\varepsilon_i\) are independent \(N(0,\sigma^2)\) independent of the nodes. For the full degree-\(n-1\) noisy interpolant \(\widehat f(t)=\sum_iY_i\ell_i(t)\), every \(q>0\) satisfies
\[
 \mathbb E|\widehat f(t_0)-f(t_0)|^q<\infty
 \quad\Longleftrightarrow\quad q<\theta+1.
\]
The pointwise statement concerns unconditional error, averaging both the node design and observation noise; it is not a claim about least squares with oversampling or about deterministic nodes.

## Assumptions and scope

The normalizer \(Z_{n,\theta}\) is strictly positive and finite because the integrand is bounded by one and positive on the open set of pairwise distinct nodes. The law is exchangeable, absolutely continuous, and has no ties almost surely. The polynomial interpolant is defined exactly (no floating-point roundoff). The exponent \(\theta\) controls vanishing of the density at pair collisions, without endpoint weights. Finite dimensionality \(n\) is fixed throughout; no uniform-in-\(n\) bound on a finite moment is asserted. \(\Lambda\ge1\) identically, so the two-point tail starts at \(t=1\).

## Proof

**Finite moments.** For every \(t\in[0,1]\), \(|t-X_j|\le1\); hence
\[
 \Lambda\le\sum_{i=1}^n H_i,\qquad H_i=\prod_{j\ne i}|X_i-X_j|^{-1}.
\]
For positive \(q\), \((\sum_iH_i)^q\le n^{\max(q-1,0)}\sum_iH_i^q\). If \(q<\theta+1\), all factors \(|x_j-x_k|^\theta\) with \(j,k\ne i\) can be discarded in the expectation of \(H_i^q\) since they are at most one. Thus
\[
 \begin{aligned}
 \mathbb EH_i^q
 &\le Z_{n,\theta}^{-1}\int_0^1
  \left(\int_0^1|u-v|^{\theta-q}\,dv\right)^{n-1}du\\
 &\le Z_{n,\theta}^{-1}\left(\frac{2}{\theta-q+1}\right)^{n-1}<\infty.
 \end{aligned}
\]
This proves sufficiency for all \(n\ge2\).

**Divergence at the exact endpoint.** Fix \(t_0=0\), and choose two nodes \(X_1,X_2\) in a small common interval strictly inside \((0,1)\), with all remaining nodes confined to disjoint compact intervals away from that interval and from \(t_0\). The other pair separations are then uniformly bounded below, all numerator factors \(|t_0-X_j|\) are uniformly bounded below, and the joint density is bounded below by a positive constant times \(|X_1-X_2|^\theta\). Therefore, on this positive-volume region, \(|\ell_1(t_0)|\ge c/|X_1-X_2|\), with \(c>0\) depending only on the chosen intervals. Integrating the gap \(d=|X_1-X_2|\) over \((0,\epsilon)\) shows
\[
 \mathbb E\Lambda^q\ge c'\int_0^\epsilon d^{\theta-q}\,dd=\infty
 \qquad (q\ge\theta+1).
\]
The same construction works with any fixed \(t_0\): locate the colliding pair strictly away from \(t_0\). This proves necessity and will also be used for the pointwise noise claim.

**Two nodes: exact distribution.** Order the two node positions, denote their gap by \(d\in(0,1)\) and midpoint by \(u\in[d/2,1-d/2]\). The joint probability density in \((d,u)\) equals \(2d^\theta/Z_{2,\theta}\), where \(Z_{2,\theta}=2/[(\theta+1)(\theta+2)]\). The Lebesgue function is convex in the evaluation argument, so its maximum occurs at an endpoint and is
\[
 \Lambda=\frac{2\max\{u,1-u\}}{d}.
\]
For fixed \(t\ge1\), the total permitted midpoint length with \(\Lambda>t\) is \(1-d\) when \(0<d<1/t\), is \(2-(t+1)d\) when \(1/t\le d<2/(t+1)\), and vanishes for larger gaps. Direct integration therefore yields
\[
 \frac{2}{Z_{2,\theta}}\left[
 \int_0^{1/t}d^\theta(1-d)\,dd+
 \int_{1/t}^{2/(t+1)}d^\theta(2-(t+1)d)\,dd
 \right]
 =2\left(\frac{2}{t+1}\right)^{\theta+1}-t^{-(\theta+1)}.
\]
Asymptotics and the displayed first two moments follow by \(\mathbb E\Lambda^q=1+q\int_1^\infty t^{q-1}\Pr(\Lambda>t)\,dt\), where the integral is finite only in its stated domain.

**Gaussian observation noise at a fixed point.** The noiseless interpolant \(I_Xf(t)=\sum_if(X_i)\ell_i(t)\) remains bounded uniformly over all distinct configurations. Indeed, Newton interpolation with nodes in \([0,1]\) has divided-difference coefficients \(|f[X_1,\dots,X_{k+1}]|\le \|f^{(k)}\|_\infty/k!\) for \(0\le k\le n-1\), and every Newton basis product has absolute value at most one on \([0,1]\). Conditional on the nodes, the random perturbation \(N_X(t_0)=\sum_i\varepsilon_i\ell_i(t_0)\) is centered Gaussian with variance \(\sigma^2\sum_i\ell_i(t_0)^2\). Hence its absolute \(q\)-moment equals \(c_q\sigma^q(\sum_i\ell_i(t_0)^2)^{q/2}\), where \(c_q=\mathbb E|N(0,1)|^q\) is finite and positive. The upper bound \((\sum\ell_i(t_0)^2)^{1/2}\le\Lambda\) proves finiteness for \(q<\theta+1\). On the colliding-pair region located away from \(t_0\), \(|\ell_1(t_0)|\ge c/d\), proving divergence for \(q\ge\theta+1\). Adding the uniformly bounded deterministic interpolation offset \(I_Xf(t_0)-f(t_0)\) cannot change moment finiteness: apply the triangle inequality, or its \(q\)-power subadditive form for \(0<q\le1\). This completes the proof.

## Verification

Run `python3 verify.py` from the same directory. It independently evaluates the two-node survival law both as a closed expression and by numerical integration of the midpoint/gap density, checks symbolic moments for integer \(\theta=2,3,4\), tests elementary Lagrange identities on random configurations, and compares fixed-seed Monte Carlo frequencies to the exact tails. These finite checks are diagnostic only; the all-\(n\) moment theorem and divergence boundary are established by the analytic integrability proof above.

## Relationship to prior work

Belhadji, Bardenet and Chainais (2023, arXiv:2310.09437) develop finite-sample signal reconstruction with determinantal designs and mean-square approximation guarantees; their projection DPP corresponds to the \(\theta=2\) Vandermonde-squared sampling mechanism in the polynomial case. Their reconstruction theorems concern different estimators and approximation errors, and do not imply the stated all-\(n\) moment criterion for the random Lagrange Lebesgue constant or the exact two-node tail. Chkifa and Dolbeault (2023, arXiv:2306.07435) prove sampling and interpolation error bounds under a different dependent selection design, including relevant robustness discussion. Belhadji, Bardenet and Chainais (2020, arXiv:2002.09677) study kernel interpolation under continuous volume sampling and explicitly identify the analysis of its Lebesgue constant as a worthwhile open direction; the present constant-weight polynomial projection model is a specialization in spirit, not a claim about every continuous-volume-sampling kernel. Jantsch, Webster and Zhang (2016, arXiv:1606.07093) analyze deterministic weighted Leja Lebesgue constants on unbounded domains, not fixed-\(n\) random collision moments. The Lebesgue-function representation, Gaussian conditional variance formula, and Vandermonde density are established tools, not claimed as novel. A specialized previous result on random polynomial interpolation or inverse Vandermonde moments might cover some conclusions; complete priority verification remains open.

## Limitations

The distribution has constant base weight on the closed unit interval, a single global collision exponent \(\theta\ge0\), and a fixed number of nodes. Endpoint-singular Jacobi weights, multidimensional point processes, approximate interpolation, floating-point stability, adaptive regularization, and growth of the moment constants with \(n\) are not characterized. The result does not claim the same threshold for oversampled least squares or for every determinantal sampling algorithm. No independent audit or publication-priority certification has been carried out.

## References

1. A. Belhadji, R. Bardenet, P. Chainais, *Signal reconstruction using determinantal sampling*, arXiv:2310.09437, first publicly posted 2023-10-13. https://arxiv.org/abs/2310.09437
2. A. Chkifa, M. Dolbeault, *Randomized least-squares with minimal oversampling and interpolation in general spaces*, arXiv:2306.07435, first publicly posted 2023-06-12. https://arxiv.org/abs/2306.07435
3. A. Belhadji, R. Bardenet, P. Chainais, *Kernel interpolation with continuous volume sampling*, arXiv:2002.09677. https://arxiv.org/abs/2002.09677
4. P. Jantsch, C. G. Webster, G. Zhang, *On the Lebesgue constant of weighted Leja points for Lagrange interpolation on unbounded domains*, arXiv:1606.07093. https://arxiv.org/abs/1606.07093
