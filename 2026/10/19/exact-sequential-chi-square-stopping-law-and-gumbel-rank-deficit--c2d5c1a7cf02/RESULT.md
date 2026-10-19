# Exact sequential chi-square stopping law and Gumbel rank deficit for Gaussian block QB

## Finding

Consider the fresh-Gaussian Frobenius error test in a block randomized QB range finder, applied to a flat-spectrum matrix. Although every test is an unbiased squared-error estimate, repeated independent inspections create an extreme-value stopping effect. The exact finite stopping law is a product of chi-square upper-survival probabilities, and, for any fixed block width, the shortfall from the smallest tolerance-satisfying rank has a nondegenerate Gumbel limit.

**Theorem.** Fix a positive integer \(b\) and \(\gamma\in(0,1)\). Let \(n\to\infty\) through multiples of \(b\), set
\[
 q_n=b\left\lfloor\frac{\gamma n}{b}\right\rfloor,\qquad A_n=I_n,\qquad \tau_n=\sqrt{q_n}.
\]
For sufficiently large \(n\), \(0<q_n<n\). At each inspection, independently sample \(\Omega\in\mathbb R^{n\times b}\) with independent \(N(0,1/b)\) entries. With the current orthonormal column basis \(Q\), form \(Y=(I-QQ^{\mathsf T})\Omega\). If \(\|Y\|_F\le\tau_n\), stop *without* adding this block. Otherwise append an orthonormal basis for \(Y\), maintaining exact orthogonality. Let \(T_n\) be the total number of appended columns at the first successful inspection and \(M_n=n-T_n\). A hypothetical inspection at residual rank zero stops with certainty.

For every finite \(n\) and every grid value \(m\in\{0,b,2b,\ldots,n\}\), define
\[
 p_m=\Pr\{\chi^2_{bm}\le bq_n\}\quad(m>0),\qquad p_0=1.
\]
Then the **complete finite distribution**, including the endpoint, is
\[
 \boxed{\Pr\{M_n=m\}=p_m\prod_{\substack{\ell\in\{m+b,m+2b,\ldots,n\}}}(1-p_\ell).}
\]
In particular, the probability of stopping without actually meeting the Frobenius tolerance is exactly
\[
 \boxed{\Pr\{\|I_n-QQ^{\mathsf T}\|_F>\tau_n\}
  =1-\prod_{m=q_n+b,q_n+2b,\ldots,n}(1-p_m).}
\]
The product is one when its index set is empty.

For sufficiently large \(q_n\), let \(\beta_n>0\) be the unique positive solution of
\[
 \boxed{\beta_n^2+4\log\beta_n=\log\frac{q_n}{\pi b^3}.}
\]
Then \(\beta_n\to\infty\), and, with \(G\) a standard Gumbel random variable,
\[
 \boxed{\beta_n\left[\sqrt{\frac{b}{2q_n}}(M_n-q_n)-\beta_n\right]
 \xrightarrow{d}G,\quad \Pr\{G\le x\}=\exp(-e^{-x}).}
\]
Consequently,
\[
 \boxed{\frac{(n-q_n)-T_n}{\sqrt{2q_n\log(q_n)/b}}\xrightarrow{P}1,
 \qquad \Pr\{M_n>q_n\}\longrightarrow1.}
\]
The more precise centering satisfies \(\beta_n^2=\log q_n-2\log\log q_n-\log(\pi b^3)+o(1)\).

If a final procedure only deletes columns from the **last accepted block**, let \(K_n\) denote its final rank. Then \(0\le T_n-K_n\le b\) (apart from the vacuous first-test stop, where both ranks are zero). Therefore the same Gumbel limit and normalized rank deficit hold with \(n-K_n\) replacing \(M_n\), and the final projection fails the stated tolerance with probability tending to one. The exact finite distribution above concerns the *pre-pruning* stopping rank, not the pruned rank.

## Assumptions and scope

All matrices, Gaussian draws, QR computations, and stopping decisions are over the reals in exact arithmetic. The tolerance is a prescribed *absolute* Frobenius tolerance, not the source paper's optional estimated-relative-norm criterion. The matrix is exactly \(I_n\). The Gaussian block width \(b\) remains fixed as \(n\) grows; the target fraction \(\gamma\) is fixed strictly between zero and one. Blocks are independent across inspections. Every unsuccessful test adds precisely \(b\) directions until residual rank zero. The theorem analyzes the raw sequential test and, asymptotically, a last-block-only pruning operation; it does not analyze other error indicators or a growing block size.

For \(A_n=I_n\), any orthonormal \(k\)-column basis has true squared Frobenius residual \(n-k\), so the smallest attainable block-grid rank meeting \(\tau_n\) is exactly \(n-q_n\). The matrix has a completely flat singular spectrum. This is a stability benchmark, not a claim that a flat full-rank matrix is highly compressible.

## Proof

**1. Projector invariant and independent test statistics.** Suppose \(k=jb\) columns have been accepted. Since \(A=I_n\) and the accepted columns are orthonormal, the residual is the orthogonal projection \(P=I_n-QQ^{\mathsf T}\) of rank \(m=n-jb\). The next Gaussian block is independent of the past. Rotational invariance of its columns yields, conditional on *every* possible preceding history with this rank,
\[
 b\|P\Omega\|_F^2\overset{d}=\chi^2_{bm}.
\]
This conditional law depends only on \(m\), not on the previous basis orientation or stopping failures. It follows by conditional expectation induction that the success indicators at successive possible ranks are independent Bernoulli variables with probabilities \(p_m\). If a test fails and \(m\ge b\), \(P\Omega\) has rank \(b\) almost surely; its orthonormalization adds exactly \(b\) columns. The terminal rank-zero test succeeds surely. Thus success first at residual rank \(m\) has probability \(p_m\) times every earlier failure probability, proving the finite formula. Since \(\|P\|_F^2=m\), the stated exact false-acceptance formula follows by excluding successes at \(m>q_n\).

**2. Uniform moderate-deviation estimate.** Temporarily write \(q=q_n\) and hold \(b\) fixed. Set \(s_q=\sqrt{b/(2q)}\), and let \(\Phi\) and \(\phi\) be the standard normal distribution and density. For every fixed \(C>0\), Stirling's formula applied to the chi-square density shows, uniformly for \(m=q+j\) and \(0\le j\le C\sqrt{q\log q}\), that
\[
 p_{q+j}=(1+o(1))\,\bar\Phi(s_q j),\qquad\bar\Phi=1-\Phi.
\]
Here is the needed quantitative justification. With \(d=bm\) and \(Z=(\chi^2_d-d)/\sqrt{2d}\), the gamma density and Stirling's formula give
\[
 \log\frac{f_Z(z)}{\phi(z)}=O\!\left(\frac{1+|z|^3}{\sqrt d}\right)
 \quad\text{uniformly for }|z|\le D\sqrt{\log d},
\]
for each fixed \(D\). Integrating the local density estimate over the negative tail down to \(-D\sqrt{\log d}\), then using the exponential chi-square lower-tail Chernoff bound for the discarded remainder, gives relative convergence uniformly for \(|z|=O(\sqrt{\log d})\), provided \(D\) is chosen larger than the constant in that range. The actual standardized lower-tail location is
\[
 \frac{bm-bq}{\sqrt{2bm}}=s_qj+O\!\left(\frac{\log q}{\sqrt q}\right),
\]
whose change in normal log-tail is \(o(1)\) on the stated range. The same Chernoff bound shows that the **total** contribution of \(j>C\sqrt{q\log q}\) is \(o(1)\) if \(C\) is chosen sufficiently large: the tail at the lower endpoint is \(q^{-bC^2/4+o(1)}\), and at most \(n/b=O(q)\) ranks are inspected because \(q/n\to\gamma>0\). This both justifies truncation and rules out an early-stop mass outside the moderate-deviation region.

**3. Hazard-sum asymptotics.** Since \(\beta_q^2+4\log\beta_q=\log(q/(\pi b^3))\), one has \(\beta_q\sim\sqrt{\log q}\) and
\[
 \frac{\sqrt{2q}}{b^{3/2}}\frac{\phi(\beta_q)}{\beta_q^2}=1.
\]
For fixed \(x\in\mathbb R\), choose the first grid point above
\[
 t_q(x)=q+s_q^{-1}(\beta_q+x/\beta_q).
\]
The standardized grid mesh is \(b s_q=b^{3/2}/\sqrt{2q}\). Monotone-sum comparison, the moderate-deviation estimate, and the far-tail bound yield
\[
 \sum_{\substack{m\in b\mathbb Z\\m>t_q(x),\,m\le n}}p_m
 =(1+o(1))\frac{\sqrt{2q}}{b^{3/2}}
 \int_{\beta_q+x/\beta_q}^{\infty}\bar\Phi(u)\,du.
\]
The omitted endpoint rectangle is bounded by the first summand, which tends to zero. Integration by parts and Mills' ratio give
\[
 \int_z^\infty\bar\Phi(u)\,du=\phi(z)-z\bar\Phi(z)
 \sim\frac{\phi(z)}{z^2}\quad(z\to\infty).
\]
Writing \(z=\beta_q+x/\beta_q\) gives \(\phi(z)/\phi(\beta_q)\to e^{-x}\) and \(z^2/\beta_q^2\to1\), hence the sum of success probabilities tends to \(e^{-x}\). Their maximum tends to zero, since \(\bar\Phi(\beta_q+x/\beta_q)=O(\beta_q/\sqrt q)\), so also \(\sum p_m^2=o(1)\).

**4. First-success product and limiting law.** The event \(M_n\le t_q(x)\) is precisely the event of **no success** at any tested grid rank strictly exceeding \(t_q(x)\). By step 1 its probability is the product of \(1-p_m\) across those ranks. Expanding \(\log(1-p_m)=-p_m+O(p_m^2)\), step 3 gives
\[
 \Pr\{M_n\le t_q(x)\}\longrightarrow\exp(-e^{-x}),
\]
which is the claimed Gumbel limit. Since the centered Gumbel variable is tight and \(\beta_q\sim\sqrt{\log q}\), \((M_n-q)/\sqrt{2q\log q/b}\to1\) in probability. Hence \(M_n>q\) with probability approaching one. Finally, last-block pruning changes rank by at most \(b\), which changes the normalized Gumbel argument by at most \(b\beta_q s_q=o(1)\). Slutsky's theorem transfers both asymptotics to the final pruned rank. No independence of pruning and stopping is required.

## Verification

Run `python verify.py` with NumPy and SciPy. It independently implements the exact finite product probabilities and a direct simulation of successive chi-square tests, uses actual small-matrix orthonormal QR updates to check the projector invariant, and compares finite-dimensional chi-square product CDFs with the stated Gumbel limit. A fixed seed makes the numerical experiment reproducible. The script performs **784 asserted finite/numerical checks** in the supplied run. These are corroboration; the asymptotic statement depends on the proof above.

For the unpruned process with \(n=1024\) and \(q=800\), the exact probability of stopping above the target residual dimension equals approximately \(0.8765204061\) for \(b=4\), \(0.4190568078\) for \(b=8\), and \(0.0565607743\) for \(b=16\). These are distinct finite-dimensional risks despite the common limiting probability one for every **fixed** \(b\). Numerical convergence to the Gumbel law is slow at moderate \(q\), consistent with the logarithmic centering and Mills-ratio corrections.

## Relationship to prior work

Smith, Do, and Chen (arXiv:2607.06758v1, publicly released 2026-07-07) introduced the relevant matrix-free Frobenius QB test: Algorithm 2, lines corresponding to its normalized fresh Gaussian block, residual sketch, and early stopping before orthonormalization. Their text supplies the algorithm and unbiasedness of the individual squared residual estimate, but the inspected Section 3 and related results do not derive the exact flat-spectrum sequential stopping distribution, Gumbel fluctuations, or sharp fixed-block calibration.

Gorman et al. (arXiv:1810.04125, precursor of SIAM J. Sci. Comput. 2019) considered matrix-free adaptive HSS sampling. Its Sections 2.4–2.5 and Appendix A develop relative/absolute criteria and single-estimator Gaussian concentration bounds; the inspected material does not establish the present first-success extreme-value limit for the specific QB rule. Pearce et al. (arXiv:2310.09417) study adaptive randomized interpolative decompositions with LU pivoting; the inspected sections concern a different matrix factorization and error-estimation method. Liu and Qu (arXiv:2610.03321v1, 2026-10-02) establish information limits and simultaneous calibration of *reused* validation probes for nested approximation paths; their certification results do not imply this law for newly drawn, uncalibrated QB sketch blocks.

An earlier mathematical result (opaque identifier `88fc5e21-b8ad-4125-8a76-f940bc870968`) establishes a leading \(\sqrt{n\log n}\) false-acceptance rank deficit for the **unit-block relative-tolerance** version with an evolving stochastic input-norm estimate, including last-block pruning. That qualitative failure and leading one-block scale are not new here. The present result addresses a **fixed absolute** threshold, arbitrary fixed positive block width, an exact finite product distribution, and Gumbel-scale *second-order* fluctuations, none determined by that leading-order result. Other identified mathematical records concern different adaptive sketches or stopping statistics.

## Limitations

The asymptotic theorem does not apply when the block width grows with dimension or when the input has a non-flat singular spectrum. The exact finite stopping distribution is *before* source rank pruning; only the asymptotic law transfers automatically to the last-block-pruned rank. The stated absolute threshold is fixed externally rather than estimated from data. As the probability of a tolerance miss tends to one, the **relative size of the miss tends to zero**: the residual-dimension overshoot is of order \(\sqrt{n\log n}\), whereas the prescribed squared tolerance is of order \(n\). The result does not refute the empirical success reported on rapidly decaying spectra and gives no finite-precision claim. Searches cannot exclude all unindexed prior literature; independent expert validation has not been performed.

## References

1. A. I. Smith, E. Do, C. Chen, *Adaptive, Matrix-Free Low-Rank Approximation*, arXiv:2607.06758v1 (2026), https://arxiv.org/abs/2607.06758.
2. C. Gorman, G. Chávez, P. Ghysels, T. Mary, F.-H. Rouet, X. S. Li, *Matrix-free construction of HSS representation using adaptive randomized sampling*, arXiv:1810.04125 (2018), https://arxiv.org/abs/1810.04125; related journal article *Robust and Accurate Stopping Criteria for Adaptive Randomized Sampling in Matrix-Free Hierarchically Semiseparable Construction*, SIAM J. Sci. Comput. 41 (2019), doi:10.1137/18M1194961.
3. K. J. Pearce, C. Chen, Y. Dong, P.-G. Martinsson, *Adaptive Parallelizable Algorithms for Interpolative Decompositions via Partially Pivoted LU*, arXiv:2310.09417 (2023), https://arxiv.org/abs/2310.09417.
4. K. Liu, B. Qu, *Information Limits of Low-Rank Approximation Certification*, arXiv:2610.03321v1 (2026), https://arxiv.org/abs/2610.03321.
