# Drift-aligned Gaussian innovations sharpen two-level Ornstein–Uhlenbeck Euler coupling

## Finding

For an Ornstein–Uhlenbeck equation simulated with two Euler–Maruyama resolutions, the usual coarse Brownian increment is not the lowest-variance coarse innovation among **independent-block, marginally correct couplings**. A normalized, drift-weighted combination of the two fine Gaussian innovations is the unique variance minimizer in this class. It has an exact strict advantage at every finite grid size and, in the fixed-horizon small-step limit, can reduce the variance of the linear-observable level correction by a factor greater than three.

More precisely, let \(\lambda>0\), \(\sigma\ne0\), \(m\ge1\) an integer, and \(0<h<1/(2\lambda)\). Set \(a=1-\lambda h\), \(b=1-2\lambda h\), and \(T=2mh\). For the explicit Euler–Maruyama fine and coarse approximations to
\[
  dX_t=-\lambda X_t\,dt+\sigma\,dW_t,\qquad X_0=x_0\in\mathbb R,
\]
write their terminal difference as \(D=X^{(h)}_T-X^{(2h)}_T\). For independent standard normal pairs \((\xi_{j,1},\xi_{j,2})\), use either the shared-Brownian coarse innovation
\[
 \zeta_j^{\rm B}=\frac{\xi_{j,1}+\xi_{j,2}}{\sqrt2},
\]
or the drift-aligned innovation
\[
 \zeta_j^*=\frac{a\xi_{j,1}+\xi_{j,2}}{\sqrt{1+a^2}}.
\]
Both choices produce exactly the prescribed Euler–Maruyama marginal law on *each* time grid. Denoting their correction variances by \(V_{\rm B}\) and \(V_*\),
\[
 V_* =\sigma^2h\sum_{k=0}^{m-1}
 \left(a^{2k}\sqrt{1+a^2}-\sqrt2\,b^k\right)^2,
\]
\[
 V_{\rm B}=\sigma^2h\sum_{k=0}^{m-1}
 \left[(a^{2k+1}-b^k)^2+(a^{2k}-b^k)^2\right],
\]
and their **exact positive gap** is
\[
 \boxed{V_{\rm B}-V_*=2\sigma^2h\left(\sqrt{2(1+a^2)}-(1+a)\right)
 \frac{1-(a^2b)^m}{1-a^2b}>0.}
\]
Among couplings whose time blocks are independent, in which each coarse innovation has the \(N(0,1)\) law and can depend arbitrarily on its own fine Gaussian pair but on no other block, \(\zeta_j^*\) is the unique (up to null sets) minimizer of \(\operatorname{Var}(D)\).

As \(h\downarrow0\) with \(T=2mh\) fixed and \(U=\lambda T\),
\[
 \frac{V_*}{h^2}\longrightarrow
 \frac{\sigma^2\lambda}{16}\left[1-e^{-2U}(1-2U+2U^2)\right],
\]
\[
 \frac{V_{\rm B}}{h^2}\longrightarrow
 \frac{\sigma^2\lambda}{16}\left[3-e^{-2U}(3-2U+2U^2)\right].
\]
The limiting ratio \(V_{\rm B}/V_*\) is exactly three at \(U=1\), **strictly greater than three** for \(U>1\), and approaches three from above as \(U\to\infty\).

## Assumptions and scope

The spatial dimension is one; the drift is exactly linear and stable, the diffusion is additive, and \(x_0\) is deterministic. We compare the **variance**, rather than the uncentered second moment, of a single MLMC correction for the identity observable. The fine and coarse Euler–Maruyama schemes use \(2m\) and \(m\) steps, respectively. The coupling class allows the coarse innovations to be generated from their corresponding fine two-normal blocks without additional random draws or cross-block dependence; unlike shared-Brownian coupling it does not require both numerical paths to approximate the same realized Brownian trajectory. No claim of global optimality over cross-block or noncausal couplings is made.

## Proof

**1. Correct time-grid marginals.** Two fine steps aggregate to
\[
 Y_{j+1}=a^2Y_j+\sigma\sqrt h\,(a\xi_{j,1}+\xi_{j,2}),
\]
whereas the coarse recursion is
\[
 Z_{j+1}=bZ_j+\sigma\sqrt{2h}\,\zeta_j.
\]
Each displayed candidate \(\zeta_j\) is standard normal, and independent fine blocks induce independent coarse innovations. Thus the coarse recursion retains exactly the distribution of Euler–Maruyama with step \(2h\); the fine recursion is unchanged. Their expected terminal values are \(a^{2m}x_0\) and \(b^m x_0\), independent of the coupling.

**2. Exact correction variances.** Unroll both recursions for \(m\) coarse blocks. With \(k\) indexing blocks backward from the terminal time, the centered difference is a sum of independent block contributions
\[
 \sigma\sqrt h\left[a^{2k}(a\xi_{j,1}+\xi_{j,2})-\sqrt2\,b^k\zeta_j\right].
\]
For shared Brownian increments, this is a sum of two independent normal components with the coefficients displayed in \(V_{\rm B}\). For the aligned innovation the entire random block is a scalar multiple of \(a\xi_{j,1}+\xi_{j,2}\), with norm \(\sqrt{1+a^2}\), giving \(V_*\). Subtracting their expanded squares yields
\[
 V_{\rm B}-V_*=2\sigma^2h\left[\sqrt{2(1+a^2)}-(1+a)\right]
 \sum_{k=0}^{m-1}(a^2b)^k.
\]
Since \(1/2<a<1\), \(0<b<1\), and
\[
 2(1+a^2)-(1+a)^2=(1-a)^2>0,
\]
all factors are strictly positive, and summing the geometric series gives the announced formula.

**3. Sharp block-local optimality.** Fix a block and let \(S=a\xi_1+\xi_2\). For any coarse normal \(\zeta\), regardless of possible nonlinear dependence on \((\xi_1,\xi_2)\), the Cauchy–Schwarz inequality gives
\[
 \operatorname{Cov}(S,\zeta)\le\sqrt{\operatorname{Var}(S)}\sqrt{\operatorname{Var}(\zeta)}=\sqrt{1+a^2}.
\]
Equality holds exactly when \(\zeta=S/\sqrt{1+a^2}\) almost surely. The coefficient multiplying this covariance in each terminal block variance is \(-2\sqrt2\,\sigma^2h\,a^{2k}b^k<0\), so maximizing every such covariance uniquely minimizes the complete correction variance within independent-block couplings. The aligned construction attains equality simultaneously in every block.

**4. Fixed-horizon limit and threefold frontier.** Let \(t_k=2kh\) and \(U=\lambda T\). Uniformly for \(0\le t_k\le T\),
\[
 a^{2k}-b^k=e^{-\lambda t_k}\frac{\lambda^2t_k}{2}h+O(h^2),
\qquad \sqrt{1+a^2}=\sqrt2\left(1-\frac{\lambda h}{2}+O(h^2)\right).
\]
The aligned summand therefore has leading squared size \(\sigma^2h^3\lambda^2 e^{-2\lambda t_k}(1-\lambda t_k)^2/2\). Riemann summation over mesh width \(2h\) gives
\[
 \lim_{h\to0}\frac{V_*}{h^2} =\frac{\sigma^2\lambda^2}{4}\int_0^T e^{-2\lambda t}(1-\lambda t)^2dt,
\]
which evaluates to the first asserted limit. Expanding the exact variance gap, or using the same Riemann-sum argument, gives
\[
 \lim_{h\to0}\frac{V_{\rm B}-V_*}{h^2}
 =\frac{\sigma^2\lambda}{8}(1-e^{-2U}),
\]
and thus the second limit. Its numerator minus three times the first limit's bracket equals \(4U(U-1)e^{-2U}\), proving the stated threefold sign classification. The first bracket is positive for all \(U>0\) because its equivalent defining integral has a nonzero nonnegative integrand.

## Verification

The standalone file `verify.py` checks 127 exact rational block-count identities, including the positivity and exact geometric gap, and additional numerical equalities and fixed-horizon asymptotic constants. At \(\lambda=\sigma=1\), \(h=14/31\), \(m=1\), the values are exactly
\[
 V_{\rm B}=\frac{2744}{29791},\qquad V_*=\frac{1008}{29791},\qquad
 \frac{V_*}{V_{\rm B}}=\frac{18}{49}.
\]
Run `python verify.py` with Python 3; no third-party dependencies are needed. The universal statements are proved analytically above, not inferred from these finite checks.

## Relationship to prior work

Multilevel Monte Carlo ordinarily couples fine and coarse Euler noise by summing fine Brownian increments, as in Giles's analysis and in Jourdain–Kebaier's same-Brownian-path error bounds for additive-noise Euler schemes. Chada–Hoel–Jasra–Zouraris analyze strong pairwise coupling for **exponential Euler** discretizations of reaction–diffusion SPDEs, where an exact semigroup-compatible noise combination can make the *linear* fine and coarse solutions pathwise agree. Here both marginals are instead the different **explicit Euler** schemes: the new observation is the sharply optimal *normalized* two-fine-increment coarse innovation within a stated implementable coupling class, with an exact gain and explicit threefold small-step comparison. The method uses the classical Gaussian maximal-covariance principle; it does not claim invention of Gaussian optimal transport or MLMC.

## Limitations

The drift-aligned coarse sequence is not the coarse sequence of the same Brownian motion used for the fine path. The theorem covers the identity observable, a scalar stable linear SDE, independent coarse time blocks, and the strictly monotone step regime \(0<\lambda h<1/2\). It does not assert optimality for nonlinear payoffs, arbitrary nonlinear SDEs, multi-dimensional or cross-block transport couplings, nor an improved *asymptotic order* in step size; the improvement is an exact variance constant. Although the cited primary literature was compared for related exact couplings, an overlooked equivalent specialized derivation remains a priority risk.

## References

- N. K. Chada, H. Hoel, A. Jasra, and G. E. Zouraris, *Improved Efficiency of Multilevel Monte Carlo for Stochastic PDE through Strong Pairwise Coupling*, arXiv:2108.00794 (initial public submission 2 August 2021); Journal of Scientific Computing 93, 62 (2022), doi:10.1007/s10915-022-02031-2.
- B. Jourdain and A. Kebaier, *Non-asymptotic error bounds for the Multilevel Monte Carlo Euler method applied to SDEs with constant diffusion coefficient*, arXiv:1708.07064 (initial public submission 23 August 2017).
- M. B. Giles, *Multilevel Monte Carlo methods*, Acta Numerica 24 (2015), 259–328, doi:10.1017/S096249291500001X.
