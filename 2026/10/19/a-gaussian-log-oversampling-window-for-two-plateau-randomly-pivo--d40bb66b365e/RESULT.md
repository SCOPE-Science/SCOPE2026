# A Gaussian log-oversampling window for two-plateau randomly pivoted Cholesky

## Finding

Let \(n\ge2\), \(1\le r<n\), and \(a>1\), and consider the positive-definite two-plateau matrix
\[
A_{n,r,a}=\operatorname{diag}(aI_r,I_{n-r}).
\]
Apply the exact, sequential **residual-diagonal-proportional** randomly pivoted Cholesky algorithm. Let \(L=L_{n,r,a}\) be the number of pivots from the \(n-r\) unit-weight coordinates **before the last** of the \(r\) weight-\(a\) coordinates is selected. Write \(m=n-r\).

**Exact finite distribution.** For every \(z\in[0,1]\),
\[
\boxed{\mathbb E[z^L]=\sum_{j=0}^{m}\binom mj z^{m-j}(1-z)^j\prod_{h=1}^r\frac{ah}{ah+j}.}
\]
In particular, for \(0\le\ell\le m\),
\[
\boxed{\Pr(L=\ell)=\binom m\ell\sum_{j=0}^{\ell}(-1)^j\binom\ell j\prod_{h=1}^r\frac{ah}{ah+m-\ell+j},}
\]
and
\[
\boxed{\mathbb E L=m\left(1-\prod_{h=1}^r\frac{ah}{ah+1}\right).}
\]
The alternating finite sum is an exact rational formula for integer \(a\); its positivity follows from the probabilistic construction in the proof.

**Two asymptotic regimes.** Fix \(\lambda>0\) and let \(a=\lambda n\) (so \(a>1\) eventually). For each fixed \(r\ge1\), as \(n\to\infty\),
\[
L_{n,r,\lambda n}\ \Rightarrow\ \sum_{h=1}^r G_h,
\quad
\Pr(G_h=j)=\frac{\lambda h}{1+\lambda h}\left(\frac1{1+\lambda h}\right)^j\quad(j=0,1,\ldots),
\]
where the \(G_h\) are independent.

If instead \(r=r_n\to\infty\) and \(r_n=o(n)\), let \(H_r=\sum_{h=1}^r h^{-1}\) and
\[
\mu_n=\frac{n-r_n}{\lambda n}H_{r_n}.
\]
Then \(\mu_n\sim(\log r_n)/\lambda\) and
\[
\boxed{\frac{L_{n,r_n,\lambda n}-\mu_n}{\sqrt{\mu_n}}\ \Rightarrow\ N(0,1).}
\]
The Gaussian, rather than Gumbel, window arises because the number of unit-weight pivots preceding the final dominant pivot has conditional binomial fluctuations of order \(\sqrt{\log r_n}\), whereas the centered maximum of the dominant exponential clocks fluctuates on order one.

**Sharp relative-trace stopping window.** Fix \(0<\varepsilon<\lambda\) and \(x\in\mathbb R\), and define
\[
s_n=\lfloor\mu_n+x\sqrt{\mu_n}\rfloor,\qquad k_n=r_n+s_n.
\]
For all sufficiently large \(n\), \(0\le s_n\le n-r_n\), and the randomized Cholesky approximant after \(k_n\) pivots satisfies
\[
\boxed{\Pr\left\{\operatorname{tr}(A_{n,r_n,\lambda n}-\widehat A^{(k_n)})\le(1+\varepsilon)(n-r_n)\right\}\ \longrightarrow\ \Phi(x),}
\]
where \(\Phi\) is the standard normal cumulative distribution function. The best rank-\(r_n\) approximation has residual trace exactly \(n-r_n\). Thus obtaining success probability tending to one or zero occurs on opposite sides of a sharp oversampling threshold \(\sim(\log r_n)/\lambda\), with window width \(\asymp\sqrt{\log r_n}\).

## Assumptions and scope

All matrices are real and computations use exact arithmetic. At each step, a pivot is sampled *sequentially* with probability proportional to the currently unselected residual diagonal, not in an iid batch from the original diagonal. A selected diagonal coordinate is removed by its one-column Cholesky update. The finite distribution holds for every finite \(n,r,a\) satisfying the first paragraph. The two limits use \(a=\lambda n\), fixed \(\lambda>0\), and either fixed \(r\) or growing \(r_n\to\infty\) with \(r_n=o(n)\). The trace-window statement additionally requires fixed \(0<\varepsilon<\lambda\); it does not cover the threshold equality \(\varepsilon=\lambda\).

## Proof

**1. Diagonal updates are size-biased sampling without replacement.** On a diagonal positive-definite matrix, selecting pivot \(i\) subtracts precisely the current diagonal entry at \(i\). All other diagonal entries remain unchanged. Thus the first \(r\) coordinates have selection weights \(a\), the other \(m\) have weights \(1\), and all selected coordinates subsequently have weight zero.

**2. Exponential-race representation and exact law.** Give every dominant coordinate an independent exponential clock of rate \(a\) and each unit-weight coordinate an independent exponential clock of rate one. Sorting all clocks gives exactly the same ordered pivot distribution: the next smallest exponential clock belongs to index \(i\) with probability equal to its rate divided by the sum of remaining rates, and the memoryless property iterates this identity. Let \(T\) be the largest of the \(r\) dominant clocks. Conditional on \(T=t\), the number \(L\) of unit-weight clocks less than \(t\) has the binomial distribution \(\operatorname{Bin}(m,1-e^{-t})\).

The spacings between successive ordered dominant clocks are independent exponentials of rates \(ar,a(r-1),\ldots,a\); equivalently,
\[
\mathbb E[e^{-jT}]=\prod_{h=1}^{r}\frac{ah}{ah+j}\qquad(j\ge0).
\]
Conditionally expanding \((z+(1-z)e^{-T})^m\) establishes the finite generating function. Similarly,
\[
\Pr(L=\ell)=\binom m\ell\mathbb E[(1-e^{-T})^\ell e^{-(m-\ell)T}],
\]
and binomial expansion gives the displayed finite mass formula. Differentiating the generating function at \(z=1\), or conditioning directly, proves the exact mean. The exact variance, if desired, follows from \(m_1=\mathbb E e^{-T}\), \(m_2=\mathbb E e^{-2T}\):
\[
\operatorname{Var}(L)=m(1-m_1)+m(m-1)(1-2m_1+m_2)-m^2(1-m_1)^2.
\]

**3. Fixed-rank Poisson-geometric limit.** Put \(a=\lambda n\). Let \(Y_r\) be the maximum of \(r\) independent unit-rate exponentials, so \(T=Y_r/(\lambda n)\). For fixed \(r\), conditional on \(Y_r\),
\[
\operatorname{Bin}\left(n-r,1-e^{-Y_r/(\lambda n)}\right)\ \Rightarrow\ \operatorname{Poisson}(Y_r/\lambda).
\]
Bounded convergence of conditional generating functions gives convergence after mixing over \(Y_r\). The limiting generating function is
\[
\mathbb E[e^{-(1-z)Y_r/\lambda}]
=\prod_{h=1}^r\frac{\lambda h}{\lambda h+1-z},
\]
which factors into generating functions of the independent geometric failure counts shown above. This also yields the fixed-\(r\) limiting mean \(H_r/\lambda\).

**4. Growing-rank central limit theorem.** Let \(r=r_n\to\infty\), \(r_n=o(n)\), and \(m=n-r_n\). Define \(Y_r\) as above. The maximum exponential has mean \(H_r\) and variance \(\sum_{h=1}^r h^{-2}\le\pi^2/6\), so \(Y_r-H_r=O_{\Pr}(1)\), while \(H_r\sim\log r\). Given \(Y_r\), write \(L\sim\operatorname{Bin}(m,p_n)\) with \(p_n=1-e^{-Y_r/(\lambda n)}\). Uniformly on events of probability tending to one on which \(Y_r=O(\log r)\),
\[
m p_n=\frac{m}{\lambda n}Y_r+O\left(\frac{(\log r)^2}{n}\right)
=\mu_n+O_{\Pr}(1)+o(1).
\]
Here \((\log r)^2/n\to0\) since \(r<n\) and \(r\to\infty\). Moreover \(p_n\to0\), \(m p_n/\mu_n\to1\), and \(\mu_n\to\infty\). The conditional binomial central limit theorem (or expansion of the conditional characteristic function) consequently yields \((L-mp_n)/\sqrt{\mu_n}\Rightarrow N(0,1)\). Since \((mp_n-\mu_n)/\sqrt{\mu_n}\to0\) in probability, Slutsky's theorem establishes the stated unconditional limit.

**5. Exact trace threshold.** Suppose \(k=r+s\) pivots have been taken, and \(h\) dominant coordinates remain unselected. Then precisely \(m-s-h\) unit-weight coordinates remain, and the residual trace is
\[
\operatorname{tr}(A-\widehat A^{(k)})=m-s+(a-1)h.
\]
For \(a>1\), the best rank-\(r\) spectral truncation has residual trace \(m\). If \(a-1>\varepsilon m+s\), the inequality \(m-s+(a-1)h\le(1+\varepsilon)m\) holds **if and only if** \(h=0\). With \(a=\lambda n\), fixed \(\varepsilon<\lambda\), \(r=o(n)\), and \(s=\lfloor\mu_n+x\sqrt{\mu_n}\rfloor=O(\log r)=o(n)\), this strict condition holds for all sufficiently large \(n\). The event \(h=0\) at step \(r+s\) is precisely \(L\le s\). Apply the central limit theorem at the continuity point \(x\) to obtain the asserted limit.

## Verification

`verify.py` contains an exact rational implementation of both the binomial-Laplace formula and an independent finite-state Markov recursion for sequential weighted pivoting. It checks all finite mass values, normalization, first two moments, and the critical-window mean centering on representative parameter arrays. Run with `python verify.py` using only Python's standard library. The finite calculations test formulas, not the universal limit theorems; those follow from Steps 1–5.

## Relationship to prior work

The residual-diagonal sampling algorithm is from Chen, Epperly, Tropp and Webber, *Randomly pivoted Cholesky: Practical approximation of a kernel matrix with few entry evaluations* (original 2022 preprint, arXiv:2207.06503; inspected v6). Its Appendix C.4 already features two-level diagonal spectra **for determinantal-point-process sampling**, a distinct fixed-cardinality distribution; the matrix family itself is not presented as new.

Epperly, *A new analysis of the randomly pivoted Cholesky algorithm* (arXiv:2608.20633v1, released August 21, 2026), gives general expected/high-probability trace-error bounds and motivates quantitatively sharp instance-dependent analyses. Divan and Gilles, *Convergence rates of randomly pivoted methods for low-rank approximation* (arXiv:2609.06287v1), give general spectral-decay bounds including approximate pivot distributions. Neither inspected result specifies the **exact finite capture-count law** or the **Gaussian logarithmic-oversampling success window** for the stated two-plateau RPCholesky family.

The exponential-race representation and conditional binomial/Poisson limits are classical probabilistic tools. The contribution claimed here is the exact RPCholesky-specific law and its nontrivial growing-rank trace-success transition, not invention of those tools, the diagonal test family, or general RPCholesky convergence bounds.

## Limitations

The result applies to a two-plateau diagonal matrix, not to arbitrary dense kernels or approximate/block pivoting. Its performance statement is about the event that the trace residual is within a fixed multiplicative tolerance of the best rank-\(r\) residual. The high modes scale as \(a=\lambda n\); a fixed spectral contrast can lead to different asymptotics. The threshold equality \(\varepsilon=\lambda\), other rank regimes, floating-point error, wall-clock cost, and general kernel accuracy are not determined. Classical sampling theory could contain differently phrased equivalent results; the literature search does not establish global uniqueness.

## References

1. E. N. W. Epperly, *A new analysis of the randomly pivoted Cholesky algorithm*, arXiv:2608.20633v1 (first public release 2026-08-21), https://arxiv.org/abs/2608.20633.
2. R. Divan and M. A. Gilles, *Convergence rates of randomly pivoted methods for low-rank approximation*, arXiv:2609.06287v1 (2026-09-05), https://arxiv.org/abs/2609.06287.
3. Y. Chen, E. N. Epperly, J. A. Tropp, and R. J. Webber, *Randomly pivoted Cholesky: Practical approximation of a kernel matrix with few entry evaluations*, arXiv:2207.06503v6 (original release 2022-07-13), https://arxiv.org/abs/2207.06503.
