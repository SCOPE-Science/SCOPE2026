# A Gaussian log-oversampling window for two-plateau randomly pivoted Cholesky

## Finding

Let \(r=r_n\to\infty\) with \(r=o(n)\), let \(m=n-r\), and fix \(\lambda>0\). Apply exact sequential residual-diagonal-proportional randomly pivoted Cholesky to \(A=\operatorname{diag}(\lambda n I_r,I_m)\), for \(n\) large enough that \(\lambda n>1\). Let \(L\) be the number of unit-weight coordinates selected before the last weight-\(\lambda n\) coordinate. With \(H_r=\sum_{h=1}^r h^{-1}\), put
\[
\mu_n=\frac{m}{\lambda n}H_r.
\]
Then \(\mu_n\sim\lambda^{-1}\log r\), and
\[
\frac{L-\mu_n}{\sqrt{\mu_n}}\Rightarrow N(0,1).
\]
For any fixed \(0<\varepsilon<\lambda\) and \(x\in\mathbb R\), let \(s_n=\lfloor\mu_n+x\sqrt{\mu_n}\rfloor\) and \(k_n=r+s_n\). If \(\widehat A^{(k_n)}\) is the resulting approximant, then
\[
\Pr\{\operatorname{tr}(A-\widehat A^{(k_n)})\le (1+\varepsilon)m\}\longrightarrow\Phi(x),
\]
where \(\Phi\) is the standard normal distribution function. The rank-\(r\) spectral truncation has residual trace \(m\). Thus the logarithmic oversampling threshold has a window of order \(\sqrt{\log r}\) around the specified centering. For feasible deterministic oversampling sequences with normalized offsets tending to \(+\infty\) or \(-\infty\), the success probabilities tend respectively to one or zero.

## Assumptions and scope

Each pivot is sampled from the current unselected residual diagonal, not in an iid batch. Calculations use exact arithmetic; selecting one diagonal coordinate removes it without altering the others. In the theorem, \(\lambda\) and \(\varepsilon\) are fixed, and the stated growth and tolerance assumptions are essential to the argument. In particular, the statement does not cover \(\varepsilon=\lambda\). The centering is \(\mu_n\) itself, not a replacement by its leading equivalent \(\lambda^{-1}\log r\) at the precision of the window.

## Proof

**1. Diagonal pivoting and exponential clocks.** For the general finite setup \(1\le r<n\), \(m=n-r\), and \(a>1\), the diagonal updates give sampling without replacement with weights \(a\) and \(1\). Assign each of the \(r\) heavy coordinates an independent rate-\(a\) exponential clock and each of the \(m\) light coordinates an independent rate-one clock. The minimum has selection probabilities proportional to these rates, and memorylessness repeats the rule after each selection. If \(T\) is the maximum of the heavy clocks, then \(L\mid T\sim\operatorname{Bin}(m,1-e^{-T})\). By rescaling, \(Y_r=aT\) is the maximum of \(r\) rate-one exponential variables; its independent spacings have rates \(r,r-1,\ldots,1\). Thus \(\mathbb E Y_r=H_r\) and \(\operatorname{Var}Y_r=\sum_{h=1}^r h^{-2}\le\pi^2/6\).

**2. Gaussian window.** Now take \(a=\lambda n\) and the growing-rank regime of the finding. Put \(p_n=1-e^{-Y_r/(\lambda n)}\). The variance bound gives \(Y_r=H_r+O_{\Pr}(1)\), and expansion at zero gives
\[
mp_n=\frac{m}{\lambda n}Y_r+O_{\Pr}((\log r)^2/n)=\mu_n+O_{\Pr}(1),\qquad p_n\xrightarrow{\Pr}0.
\]
In particular \(mp_n/\mu_n\xrightarrow{\Pr}1\) and \(\mu_n\to\infty\). For fixed real \(t\), write \(u=t/\sqrt{\mu_n}\). The logarithm of the conditional characteristic function of \((L-mp_n)/\sqrt{\mu_n}\) is
\[
-iump_n+m\log(1+p_n(e^{iu}-1))
=-\frac{u^2}{2}mp_n(1-p_n)+O(mp_n|u|^3),
\]
using the logarithm near one. It converges in probability to \(-t^2/2\). The conditional characteristic functions are bounded by one in modulus, so their expectations converge to \(e^{-t^2/2}\). The random centering differs from \(\mu_n\) by \(o_{\Pr}(\sqrt{\mu_n})\); the stated weak convergence follows. The largest heavy clock contributes bounded fluctuations to the conditional mean in count units, whereas the light-clock count contributes the growing Gaussian fluctuations.

**3. Relative-trace success.** After \(k=r+s\) pivots, let \(h\) be the number of heavy coordinates remaining. There are \(m-s-h\) light coordinates remaining, so the residual trace is \(m-s+(a-1)h\). At \(s=s_n\) we eventually have \(0\le s\le m\) and \(a-1>\varepsilon m+s\), since \(s=O(\log r)\) and \(\varepsilon<\lambda\). Trace success is then equivalent to \(h=0\); the last heavy coordinate is selected at pivot \(r+L\), so \(h=0\) at this step is exactly \(L\le s_n\). The Gaussian limit and continuity give \(\Phi(x)\). The residual trace decreases as pivots are added, so comparison with each fixed normalized offset gives the asserted zero and one limits for offsets diverging with either sign.

## Finite-law context and fixed-rank comparison

The finite capture-count distribution is a re-expression of the Wallenius biased-urn law, not a separate originality claim. In the notation of the finite setup in Proof §1, let \(X_k\) count heavy items among the first \(k\) draws. Then \(\Pr(L\le\ell)=\Pr(X_{r+\ell}=r)\). This is precisely the all-heavy endpoint of the fixed-draw Wallenius probability (Fog, §2, equations (1)–(6)); differencing adjacent draw counts gives the mass of \(L\), with the full-sample endpoint interpreted as certain capture.

Equivalently, the conditional binomial representation and the clock spacings give \(M_j=\mathbb E e^{-jT}=\prod_{h=1}^r ah/(ah+j)\) for \(j\ge0\). Consequently, for \(z\in[0,1]\),
\[
\mathbb E z^L=\sum_{j=0}^m\binom mj z^{m-j}(1-z)^j M_j,
\qquad
\Pr(L=\ell)=\binom m\ell\sum_{j=0}^\ell(-1)^j\binom\ell j M_{m-\ell+j},
\qquad \mathbb E L=m(1-M_1).
\]
These identities follow by expanding the conditional generating function \((z+(1-z)e^{-T})^m\) and conditional mass \(\binom m\ell(1-e^{-T})^\ell e^{-(m-\ell)T}\). In contrast to the growing-rank window, for fixed \(r\) and \(a=\lambda n\) the conditional binomial tends to Poisson with parameter \(Y_r/\lambda\). Mixing and using the independent spacings yields the limiting generating function \(\prod_{h=1}^r \lambda h/(\lambda h+1-z)\), that of a sum of independent geometric failure counts. This is included as a comparison of regimes, not as a separate originality claim.

## Verification

The unchanged standard-library `verify.py` checks the finite probability formula against a separate rational finite-state recursion and checks moments and sample centering values. Those checks do not establish the growing-rank limit, which follows from the proof above.

## Relationship to prior work and limitations

The pivot rule is that of Chen, Epperly, Tropp and Webber (equation (2.6)). Their Appendix C.4 studies two-level diagonal matrices for a different sampling law, the fixed-cardinality determinantal point process. The classical Wallenius law already treats the sequential weighted finite sample and hence determines the finite capture distribution. Epperly studies the cost of capturing all large coordinates on a two-level diagonal example in a different high-to-low weight regime and gives general expected and high-probability trace bounds. Divan and Gilles give general convergence bounds. The contribution here is the explicit critical Gaussian scale and success curve at fixed \(a/n=\lambda\) in the stated growing-rank regime. This does not assert absolute literature priority.

The proof does not cover dense kernels, other spectral ratios, approximate or block pivoting, floating-point error, or wall-clock cost.

## References

1. A. Fog, *Calculation Methods for Wallenius' Noncentral Hypergeometric Distribution*, Communications in Statistics – Simulation and Computation 37 (2008), 258–273. [Author copy](https://www.agner.org/random/theory/nchyp1.pdf), §2.
2. Y. Chen, E. N. Epperly, J. A. Tropp, and R. J. Webber, *Randomly pivoted Cholesky: Practical approximation of a kernel matrix with few entry evaluations*, [arXiv:2207.06503v6](https://arxiv.org/abs/2207.06503v6).
3. E. N. W. Epperly, *A new analysis of the randomly pivoted Cholesky algorithm*, [arXiv:2608.20633v1](https://arxiv.org/abs/2608.20633v1).
4. R. Divan and M. A. Gilles, *Convergence rates of randomly pivoted methods for low-rank approximation*, [arXiv:2609.06287v1](https://arxiv.org/abs/2609.06287v1).
