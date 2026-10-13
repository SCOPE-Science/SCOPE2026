# A parity-dependent covariance crossover in Ewens permutations

## Finding
Let \(n\ge2\) and \(\theta>0\). Sample a permutation \(\Pi\) of \(\{1,\ldots,n\}\) with probability proportional to \(\theta^{K}\), where \(K\) is its number of cycles. For \(1\le j\le n\), let \(A_j\) count its cycles of length \(j\), and put
\[
E=\sum_{\substack{1\le j\le n\\j\text{ even}}}j A_j,
\]
the number of labels lying in even-length cycles. Write \(c_n(\theta)=\operatorname{Cov}_{\theta}(K,E)\).

**Theorem.** If \(n\) is even, then \(c_n(\theta)<0\) for every \(\theta>0\). If \(n\ge3\) is odd, there exists a **unique** \(\theta_n>1\) such that
\[
 c_n(\theta)>0\quad(0<\theta<\theta_n),\qquad
 c_n(\theta_n)=0,\qquad
 c_n(\theta)<0\quad(\theta>\theta_n).
\]
Along odd integers \(n\to\infty\), the crossover has a sharp logarithmic boundary layer:
\[
(\theta_n-1)\log n-\log\log n\longrightarrow0.
\]
In particular, \(\theta_n\to1\) from above.
More exactly, for every \(n\ge2\) and \(\theta>0\),
\[
 \mathbb E_\theta E=n(n-1)\int_0^1 y^{\theta}(2y-1)^{n-2}\,dy,
 \qquad
 c_n(\theta)=\theta n(n-1)\int_0^1 y^{\theta}\log y\,(2y-1)^{n-2}\,dy.
\]
For \(n=3\), the unique crossover is \(\theta_3=\sqrt2\).

## Assumptions and scope
The sample space is the finite symmetric group, with
\[
\mathbb P_{\theta}(\Pi=\pi)=\frac{\theta^{K(\pi)}}{(\theta)^{\overline n}},\qquad
(\theta)^{\overline n}=\prod_{i=0}^{n-1}(\theta+i).
\]
Cycle lengths refer to the disjoint-cycle decomposition; the weights are constant per cycle, not per element. The parameter varies over all positive real numbers. The number of cycles and the total **mass** of even cycles are distinct statistics: \(E\) is not the count of even cycles. All inequalities are strict on the stated open ranges. At \(n=2\) only the negative regime exists; at \(n=1\) the mass is identically zero and that degenerate case is excluded.

## Proof
**1. Tagged cycle and a beta mixture.** By exchangeability, \(\mathbb E_\theta E/n\) is the probability that label \(1\) lies in an even-length cycle. Denote the length of its cycle by \(L\). The Ewens cycle enumeration identity gives
\[
 \mathbb E_\theta A_j=\frac\theta j\frac{n!}{(n-j)!}
 \frac{\Gamma(n-j+\theta)}{\Gamma(n+\theta)}
\]
and consequently
\[
 \mathbb P_\theta(L=j)=\theta\frac{(n-1)!}{(n-j)!}
 \frac{\Gamma(n-j+\theta)}{\Gamma(n+\theta)}.
\]
Equivalently, with \(V\) beta distributed with parameters \((1,\theta)\), conditional on \(V\), the variable \(L-1\) is binomial with \(n-1\) trials and success probability \(V\). To check this, integrate the binomial probability against the density \(\theta(1-v)^{\theta-1}\) using the beta-function identity.

The odd-part formula for a binomial random variable gives
\[
\mathbb P_\theta(L\text{ even})
=\frac12\left[1-\theta\int_0^1y^{\theta-1}(2y-1)^{n-1}\,dy\right],
\]
where \(y=1-v\). Integrating by parts, whose boundary terms vanish for \(\theta>0\), yields
\[
 e_n(\theta):=\mathbb E_\theta E=n(n-1)\int_0^1 y^\theta(2y-1)^{n-2}\,dy. \tag{1}
\]
The finite exponential-family identity
\[
 \frac{d}{d\theta}\mathbb E_\theta T
 =\frac1\theta\operatorname{Cov}_\theta(K,T)
\]
holds for every statistic \(T\) independent of \(\theta\): differentiate its finite weighted sum and the normalizing factor. Differentiating (1) under the integral sign gives the stated covariance identity.

**2. Even orders.** For even \(n\), the integer \(n-2\) is even and \((2y-1)^{n-2}\ge0\) for all \(y\), with strict positivity except possibly at one point. Since \(\log y<0\) on \((0,1)\), the covariance integral is strictly negative.

**3. Odd orders and uniqueness.** Let \(n\ge3\) be odd, so \(m=n-2\) is a positive odd integer. Define
\[
 L_m(\theta)=\int_0^{1/2}(-\log y)y^\theta(1-2y)^m\,dy,
 \qquad
 R_m(\theta)=\int_{1/2}^{1}(-\log y)y^\theta(2y-1)^m\,dy.
\]
Both are positive and finite for \(\theta\ge0\). The sign of \(c_n(\theta)\) is the sign of \(L_m(\theta)-R_m(\theta)\). Differentiating logarithms yields
\[
 \frac{d}{d\theta}\log\frac{L_m(\theta)}{R_m(\theta)}
 =\mathbb E_{L,\theta}[\log Y]-\mathbb E_{R,\theta}[\log Y]<0,
\]
where the first expectation uses a normalized density on \((0,1/2)\) and the second on \((1/2,1)\). The inequality is strict because the two supports are strictly ordered. Also \(L_m(\theta)/R_m(\theta)\to0\) as \(\theta\to\infty\): the numerator is at most a constant times \((1/2)^\theta\), while integrating the denominator over \([3/4,7/8]\) supplies a positive constant times \((3/4)^\theta\).

At \(\theta=1\), reflect the right integral by \(y\mapsto1-y\). Then
\[
 L_m(1)-R_m(1)
 =\int_0^{1/2}(1-2y)^m h(y)\,dy,
 \quad h(y)=(1-y)\log(1-y)-y\log y.
\]
The continuous function \(h\) vanishes at both endpoints of \([0,1/2]\), and
\[
 h''(y)=-\frac1y+\frac1{1-y}<0\qquad(0<y<1/2).
\]
Strict concavity gives \(h(y)>0\) in the interior. Therefore \(L_m(1)>R_m(1)\). Their strictly decreasing ratio crosses \(1\) precisely once at some \(\theta_n>1\), proving the complete sign classification.

**4. Limit of the crossover.** Fix \(\theta>0\) and let \(m\to\infty\) through odd integers. In \(L_m\), the change of variables \(x=2my\) and dominated convergence (using \((1-x/m)^m\le e^{-x}\)) give
\[
 L_m(\theta)\sim
 \frac{\Gamma(\theta+1)\log m}{(2m)^{\theta+1}}.
\]
In \(R_m\), put \(x=2m(1-y)\). Since \(-\log(1-u)\sim u\) as \(u\downarrow0\), the same endpoint estimate gives
\[
 R_m(\theta)\sim\frac{1}{4m^2}.
\]
The estimates can be made rigorous uniformly for \(\theta\) in any compact interval of positive parameters, by splitting each rescaled integral into a bounded interval and its exponentially dominated tail; expansions of \((1-x/m)^m\) around \(e^{-x}\) give an error \(O(1/m)\) after integration. Their ratio therefore obeys
\[
\frac{L_m(\theta)}{R_m(\theta)}
 \sim 2^{1-\theta}\Gamma(\theta+1)m^{1-\theta}\log m.
\]
For every fixed \(\theta>1\) this tends to zero, whereas at \(\theta=1\) it tends to infinity. Since the ratio is decreasing and \(\theta_n>1\), every fixed \(\theta>1\) eventually exceeds \(\theta_n\). This first proves \(\theta_n\to1\). Using the same endpoint estimates uniformly on \([1,2]\), the logarithm of the exact crossing equation \(L_m(\theta_n)=R_m(\theta_n)\) gives
\[
0=(1-\theta_n)\log m+\log\log m+(1-\theta_n)\log2+\log\Gamma(\theta_n+1)+o(1).
\]
The last two non-error terms tend to zero because \(\theta_n\to1\), yielding \((\theta_n-1)\log m-\log\log m\to0\). Since \(m=n-2\), this is equivalent to the theorem’s announced rate.

Finally, (1) at \(n=3\) gives \(e_3(\theta)=6\theta/[(\theta+1)(\theta+2)]\). Its derivative has the sign of \(2-\theta^2\), giving \(\theta_3=\sqrt2\).

## Verification
The standalone `verify.py` reconstructs the weighted permutation measure by exhaustive enumeration for \(2\le n\le8\) at four rational parameter values. It checks \(\mathbb E E\) and \(\operatorname{Cov}(K,E)\) against two independently evaluated exact formulas: the finite cycle-length sum and the integrated polynomial expression. It additionally checks the sign regime at rational parameters for a wider range of orders and the explicit \(n=3\) crossover. Run with `python3 verify.py` (Python standard library only). These finite tests corroborate the proof; they are not used as evidence of infinite uniqueness or convergence.

## Relationship to prior work
The Ewens sampling formula and size-biased cycle statistics are classical. Lugo [1, Lemma 1.2 and Proposition 2.4] gives the expected count of cycles of each fixed length under weighted permutations, and studies cycle structures with all lengths even or odd. These are distinct from allowing all cycles while counting the **elements** contained in even cycles. The exact expectation in (1) can be recovered by summing those established fixed-length expectations. The new assertion isolated here is the strict full-parameter covariance sign classification, uniqueness of the odd-order crossing, and convergence of its location; these require the sign-regular integral comparison, not just the marginal cycle formula. Maples–Nikeghbali–Zeindler [2] analyze normal limits for total cycle count in generalized Ewens measures, not the present parity-weighted mixed covariance.

## Limitations
No assertion is made about the full joint distribution of \((K,E)\), stochastic monotonicity, nonlinear prediction, an exact closed form for \(\theta_n\) at arbitrary odd \(n\), or a second-order expansion of \(\theta_n\) beyond the displayed logarithmic scale. The expectation formula alone is a consequence of established cycle enumeration; historical priority is claimed only for the covariance-sign and crossover classification, subject to independent literature review. The proof is mathematical, and the bundled finite checks provide reproducible corroboration without independent certification.

## References
[1] Michael Lugo, *Profiles of permutations*, arXiv:0907.5351v1 (first posted 2009-07-30), sections 1–3; Electronic Journal of Combinatorics 16 (2009), R99. https://arxiv.org/html/0907.5351v1

[2] Kenneth Maples, Ashkan Nikeghbali, and Dirk Zeindler, *On the number of cycles in a random permutation*, arXiv:1203.4132v1 (first posted 2012-03-19), sections 1 and 3; Electronic Communications in Probability 17 (2012), no. 20. https://arxiv.org/html/1203.4132v1
