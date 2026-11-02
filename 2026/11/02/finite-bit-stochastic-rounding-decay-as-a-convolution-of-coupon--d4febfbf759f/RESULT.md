# Finite-bit stochastic-rounding decay as a convolution of coupon collectors

## Finding
A fixed-point, decrement-rounded Euler solver for scalar decay can retain a strictly positive absorbing residual when its rounding decision uses fewer random bits than the state grid has fraction bits. For integers \(p,r\geq1\), write \(N=2^p\) and \(K=2^r\). In the exact discretization below, **zero is reached almost surely if and only if \(r\ge p\)**. If \(r<p\), the almost-sure limiting residual is exactly \(K^{-1}-N^{-1}>0\).

For \(r\le p\), put \(L=N/K=2^{p-r}\), and let \(\tau\) be the number of time steps until the residual first reaches \((L-1)/N\). If \(C_K\) is the number of independent, equiprobable draws needed to collect all \(K\) distinct coupons, and \(C_K^{(1)},\ldots,C_K^{(L)}\) are independent copies, then
\[
\boxed{\tau\ \stackrel{d}{=}\ \sum_{a=1}^{L}C_K^{(a)}-L+1.}
\]
Hence the full absorption-time law is a shifted \(L\)-fold coupon-collector convolution, with
\[
\boxed{\mathbb E\tau=1+N H_{K-1},\qquad
\operatorname{Var}(\tau)=NK H_{K-1}^{(2)}-N H_{K-1},}
\]
where \(H_m^{(s)}=\sum_{j=1}^m j^{-s}\). At and above the critical bit budget, the exact hitting time of zero has the ordinary coupon-collector law \(C_N\).

There is a second, two-parameter settling-time distinction. With a fixed bit deficit \(s=p-r\ge0\), \(L=2^s\) fixed, and \(K\to\infty\),
\[
\frac{\tau}{N}-\log K\ \Longrightarrow\ \frac1L\sum_{a=1}^LG_a,
\]
where the \(G_a\) are independent standard Gumbel variables with cumulative distribution \(\exp(-e^{-x})\). For \(L>1\) this is not a Gumbel distribution. When instead both \(L\) and \(K\) diverge, the same centered quantity converges in probability to Euler's constant \(\gamma\). Thus the number of missing random bits determines whether normalized settling-time fluctuations persist or self-average.

## Assumptions and scope
Solve \(u'=-u\), \(u(0)=1\), by an explicit Euler **decrement form** with fixed time step \(h=1/N\). Store the state as \(U_n=J_n/N\), \(J_0=N\), on the fixed-point grid \(\{0,1/N,\ldots,1\}\). At a state \(J_n=j\), compute the Euler decrement \(d_j=hU_n=j/N^2\) exactly, then stochastically round **the nonnegative decrement**, not the final state, to either \(0\) or \(1/N\). To decide the upper outcome, first truncate its fraction of a grid cell \(j/N\) downward to the \(r\)-random-bit grid \(\{0,1/K,\ldots,1\}\). A fresh independent uniform integer from \(\{0,\ldots,K-1\}\) is used at each step. Accordingly,
\[
J_{n+1}=J_n-B_n,\qquad
\Pr(B_n=1\mid J_n=j)=q_j=\frac{\lfloor Kj/N\rfloor}{K},
\]
for integers \(0\le j\le N\); conditional choices are independent given the current state. This is a specified **fixed-point probability-truncation model**; it is not IEEE floating-point arithmetic and is not the same as rounding \(U_n-hU_n\) in one operation. We assume exact evaluation of \(d_j\), no overflow, exact uniform random bits, and infinitely many independent rounding decisions when needed.

For \(r\le p\), the target absorption state is \(j_*=L-1\), \(L=N/K\); define \(\tau=\inf\{n\ge0:J_n=j_*\}\). For \(r\ge p\), define \(\tau_0=\inf\{n\ge0:J_n=0\}\). All assertions are exact in this model and for all positive integer \(p,r\); the limits explicitly prescribe how these integers tend to infinity.

## Proof
**1. Positive states and the exact bit threshold.** If \(r\le p\), then \(q_j=0\) for \(0\le j<L\), while \(q_j>0\) for \(j\ge L\). Starting at \(J_0=N\), the chain is nonincreasing and each visited state \(j\ge L\) is left almost surely after a geometric waiting time with parameter \(q_j>0\). It therefore visits \(N,N-1,\ldots,L\) in order and stops almost surely at \(L-1\). The stored limiting value is \((L-1)/N=1/K-1/N\); this is positive exactly for \(r<p\). If \(r\ge p\), then \(K/N\) is an integer and \(q_j=j/N\) for every integer \(j\). All \(j>0\) therefore have a strictly positive exit probability and the chain hits zero almost surely. This proves both directions of the bit threshold.

**2. Independent holding times.** Let \(G_j\) count the number of successive steps spent at state \(j\) (including its successful departure). The use of fresh independent decisions and the strong Markov property imply that the \(G_j\) are independent and \(G_j\sim\operatorname{Geom}(q_j)\) on \(\{1,2,\ldots\}\). For \(r\le p\), \(q_N=1\), and for each \(\ell=1,\ldots,K-1\), precisely the \(L\) integers
\[
\ell L,\ell L+1,\ldots,(\ell+1)L-1
\]
have common parameter \(\ell/K\). Thus \(\tau\) contains one deterministic waiting time and \(L\) independent geometric waiting times for every parameter \(\ell/K\), \(1\le\ell<K\).

**3. Coupon-collector identification.** A standard \(K\)-coupon collector visits \(K,K-1,\ldots,1\) unseen-coupon counts, spending an independent \(\operatorname{Geom}(\ell/K)\) number of draws when \(\ell\) coupons remain, including \(\operatorname{Geom}(1)\equiv1\). Hence one collector consists of one deterministic draw and one waiting time at each \(\ell/K\), \(1\le\ell<K\). Combining \(L\) independent collectors and discarding \(L-1\) of their deterministic draws leaves exactly the multiset of independent holding times of \(\tau\). This proves the claimed distributional identity. The probability-generating function follows, for \(0<z<1\), as
\[
\mathbb Ez^{\tau}=z^{1-L}\left[\prod_{\ell=1}^{K}
\frac{\ell z}{K-(K-\ell)z}\right]^L,
\]
with the endpoint at \(z=0\) defined by continuity.

**4. Exact moments.** On \(\{1,2,\ldots\}\), a geometric waiting time of parameter \(q\) has mean \(1/q\) and variance \((1-q)/q^2\). Summing the independent waiting times and using \(N=LK\) yields
\[
\mathbb E\tau=1+L\sum_{\ell=1}^{K-1}\frac K\ell
=1+NH_{K-1},
\]
\[
\operatorname{Var}(\tau)=L\sum_{\ell=1}^{K-1}
\left(\frac{K^2}{\ell^2}-\frac K\ell\right)
=NKH_{K-1}^{(2)}-NH_{K-1}.
\]
If \(r\ge p\), the parameters are exactly \(1,2/N,\ldots,1/N\), identifying \(\tau_0\stackrel d=C_N\).

**5. Limiting laws.** The classical coupon-collector theorem gives \(C_K/K-\log K\Longrightarrow G\), a standard Gumbel, and independent copies converge jointly. The exact convolution identity, \(N=LK\), and \((L-1)/N\to0\) prove the fixed-\(L\) limit. Its third standardized cumulant differs from that of one Gumbel by a factor \(L^{-1/2}\), so for \(L>1\) the sum-average is not Gumbel. For the joint limit \(L,K\to\infty\), the exact moments imply
\[
\mathbb E(\tau/N-\log K)=H_{K-1}+N^{-1}-\log K\to\gamma,
\]
\[
\operatorname{Var}(\tau/N)=\frac{H_{K-1}^{(2)}}L-\frac{H_{K-1}}N\to0,
\]
by boundedness of second-order harmonic sums. Chebyshev's inequality gives convergence in probability. No interchange of an unproved limit and infinite summation is used.

## Verification
The included standalone file `verify.py` uses only the Python standard library. Run `python verify.py`. It independently reconstructs the absorption-time probability mass from the finite-state Markov chain and from the shifted coupon-collector convolution using exact rational arithmetic and Stirling-number coupon probabilities. It checks all \(1\le r\le p\le4\) for finite horizons, the harmonic mean and variance formulas, the exact terminal plateaus, the fully unbiased probability identity at and above the bit threshold for \(1\le p\le6\), and the worked case. The run produced `PASS 70 rational identities and exact distributions across dyadic grids`. These are finite reproducibility checks; the proof above establishes the all-integer and asymptotic statements.

For \(p=4\), \(r=2\), the model has \(N=16\), \(K=4\), \(L=4\). It stops at \(U_\infty=3/16\), and
\[
\tau\stackrel d=\sum_{a=1}^4C_4^{(a)}-3,
\quad\mathbb E\tau=91/3,
\quad\operatorname{Var}(\tau)=520/9.
\]
When \(r=p=4\), the stopping state instead is exactly zero and the stopping time follows \(C_{16}\).

## Relationship to prior work
El Arar, Fasi, Filip, and Mikaitis introduce limited-precision stochastic rounding and prove its one-step bias properties (arXiv:2408.03069, Definitions 3–4 and Section 3). The fixed-point truncation rule here is its precisely specified grid analogue, but their results do not themselves identify the exact Euler absorption law. Fitzgibbon and Felix (arXiv:2504.20634, Sections II–IV) examine few-bit rounding biases and corrections, with a different application and without a finite-state absorption classification. The stochastic-rounding survey of Croci and coauthors (arXiv:2010.16225) discusses ideal rounding and mitigation of stagnation; that ideal unbiased premise fails for \(r<p\) here. General coupon-collector formulas, the Gumbel limit, and finite-state geometric holding times are classical and are not claimed as new. The contribution is the explicit precision-to-dynamics correspondence, sharp bit-budget barrier, full convolution law, and two-parameter settling-time classification for this concrete fixed-point scheme.

## Limitations
The specified model rounds the **decrement**, not the completed Euler update, and uses a uniform fixed-point grid. It is not a universal assertion about IEEE floating-point stochastic rounding, arbitrary time steps, adaptive solvers, rounded multiplication, or alternative few-bit rounding implementations. A different intermediate rounding rule (for example, unbiased correction or rounding to nearest) can eliminate or modify the plateau. The numerical experiment verifies only finite cases; no independent scientific audit is asserted. Literature comparisons cannot exclude an equivalent unpublished or less discoverable prior finite-state analysis.

## References
1. E.-M. El Arar, M. Fasi, S.-I. Filip, and M. Mikaitis, *Probabilistic error analysis of limited-precision stochastic rounding*, arXiv:2408.03069 (initial posting 2024-08-06), https://arxiv.org/abs/2408.03069.
2. A. Fitzgibbon and S. Felix, *On Stochastic Rounding with Few Random Bits*, arXiv:2504.20634 (2025), https://arxiv.org/abs/2504.20634.
3. M. Croci, M. Fasi, N. J. Higham, T. Mary, and M. Mikaitis, *Stochastic rounding: implementation, error analysis, and applications*, arXiv:2010.16225, https://arxiv.org/abs/2010.16225.
4. W. Feller, *An Introduction to Probability Theory and Its Applications*, Vol. I, coupon-collector discussion (classical reference).
5. A. S. Hathcock and S. H. Strogatz, *Asymptotic absorption-time distributions in birth-death processes*, arXiv:2103.08522, https://arxiv.org/abs/2103.08522 (general background on absorption laws, not the exact fixed-bit scheme).
