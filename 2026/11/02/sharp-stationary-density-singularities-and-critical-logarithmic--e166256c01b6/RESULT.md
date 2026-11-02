# Sharp stationary-density singularities and critical logarithmic scaling in an asymmetric Pelikan map

## Finding
Consider independent random iteration on \([0,1)\), choosing \(T_-(x)=x/4\) with probability \(p\) and \(T_+(x)=2x\pmod 1\) with probability \(q=1-p\). For every \(0<p<1/3\), the unique stationary probability absolutely continuous with respect to Lebesgue measure is the law of \(X=2^{-K}U\), where \(U\) is uniform on \([0,1)\), independent of the nonnegative integer \(K\), and
\[
\mathbb E[z^K]=\frac{1-3p}{q-pz-pz^2}.
\]
Its density is exactly \(h_p(x)=\sum_{k\ge0}2^k\pi_k\mathbf1_{(0,2^{-k})}(x)\), where \(\pi_k=\Pr(K=k)\). Put
\[
\rho=\frac{p+\sqrt{p^2+4pq}}{2q},\qquad \sigma=\frac{p-\sqrt{p^2+4pq}}{2q},\qquad\pi_k=\frac{1-3p}{q}\frac{\rho^{k+1}-\sigma^{k+1}}{\rho-\sigma}.
\]
The following density-regularity transition is sharp.

For \(0<p<1/7\), \(h_p\) is bounded and its essential limit as \(x\downarrow0\) equals \((1-3p)/(1-7p)\). For \(p=1/7\), \(h_p(x)=\frac25\log_2(1/x)+O(1)\). For \(1/7<p<1/3\), write \(\alpha_p=\log_2(2\rho)\in(0,1)\). Then
\[
\lim_{x\downarrow0}\frac{\log h_p(x)}{\log(1/x)}=\alpha_p,
\qquad h_p\in L^r([0,1])\iff r\alpha_p<1\quad(r\ge1).
\]
In the first two regimes the density belongs to every finite \(L^r\). Finally, under the stationary distribution,
\[
(1-3p)\log_2(1/X)\ \xrightarrow[p\uparrow1/3]{\mathrm{law}}\ \operatorname{Exp}(1).
\]
This last statement identifies the full critical concentration scale, not merely weak convergence to the endpoint atom.

## Assumptions and scope
The state space is \([0,1)\) with its Borel sigma-algebra, and the map chosen at each step is independent of the past. Probabilities satisfy \(0<p<1/3\), \(q=1-p\). Densities and identities involving intervals are understood Lebesgue-almost everywhere; the unique-stationary assertion is restricted to absolutely continuous stationary probabilities. The endpoint point mass \(\delta_0\) is also stationary, so uniqueness among all stationary probabilities is not asserted. \(\operatorname{Exp}(1)\) denotes the mean-one exponential distribution. No assertion is made at or above \(p=1/3\).

## Proof
**Binary-prefix conjugacy.** With the nonterminating binary convention away from the countable dyadic set, \(x/4\) prepends two zero bits while \(2x\pmod1\) deletes the first bit. Therefore the family of probability measures \(\nu_k=\mathrm{Law}(2^{-k}U)\) is invariant under the random transition on indices \(k\ge0\): contraction sends \(k\mapsto k+2\), expansion sends \(k\mapsto\max(k-1,0)\). For \(k=0\), doubling maps the uniform law back to the uniform law. This is an irreducible aperiodic reflected random walk with increments \(+2\) and \(-1\). Its drift outside the boundary is \(3p-1<0\); the elementary Foster drift criterion, or the explicit invariant law below, proves positive recurrence.

**Exact stationary weights.** The stationary generating function \(\Pi(z)=\sum_{k\ge0}\pi_kz^k\) obeys
\[
\Pi(z)=pz^2\Pi(z)+q\bigl((\Pi(z)-\pi_0)/z+\pi_0\bigr).
\]
Thus \(\Pi(z)=q\pi_0/(q-pz-pz^2)\). Imposing \(\Pi(1)=1\) gives \(\pi_0=(1-3p)/q\) and the stated generating function. Since its coefficients satisfy the nonnegative stationary Markov-chain balance equations and sum to one, this is the unique index stationary law. Partial fractions yield the displayed \(\rho,\sigma\) formula. Mixing the laws \(\nu_k\) with these weights produces the stated stationary density.

**Uniqueness within absolutely continuous measures.** Fix any initially absolutely continuous distribution. Given the sequence of random map choices through time \(n\), the output has the binary form \(2^{-K_n}T_+^{J_n}(X_0)\) where \(K_0=J_0=0\), \(K_n\) follows the reflected walk above, and \(J_n=E_n-2C_n+K_n\), with \(E_n,C_n\) the numbers of expanding and contracting selections. In particular \(J_n/n\ge(E_n-2C_n)/n\to1-3p>0\) almost surely. Iteration of the doubling map is exact for Lebesgue measure: for every absolutely continuous initial law, the laws of \(T_+^j(X_0)\) converge in total variation to uniform as \(j\to\infty\), by approximation of its density by dyadic step functions. The conditional distributions indexed by \(K_n,J_n\) consequently approach \(\nu_{K_n}\) in total variation. The reflected walk converges in distribution (indeed total variation) to \(\pi\) by irreducible aperiodic positive recurrence. Thus every absolutely continuous initial law converges in total variation to \(\sum_k\pi_k\nu_k\), proving its uniqueness among absolutely continuous stationary probabilities.

**Endpoint density and integrability.** On the dyadic annulus \([2^{-(N+1)},2^{-N})\), the density takes the constant value \(H_N=\sum_{k=0}^N2^k\pi_k\). The roots satisfy \(0<\rho<1\), \(-\rho<\sigma<0\), and \(2\rho\lessgtr1\) exactly when \(p\lessgtr1/7\). In the subcritical case \(H_N\uparrow\Pi(2)=(1-3p)/(1-7p)\). At equality, the positive-root coefficient of \(\pi_k\) is \(2/5\), while the negative-root contribution to \(H_N\) stays bounded; hence \(H_N=(2/5)(N+1)+O(1)\), yielding the logarithmic result. Above equality, direct geometric summation gives
\[
\frac{H_N}{(2\rho)^N}\longrightarrow\frac{(1-3p)\rho}{q(\rho-\sigma)}\frac{2\rho}{2\rho-1}>0.
\]
Since \(N=\log_2(1/x)+O(1)\) on the annulus, the logarithmic exponent follows. Moreover \(\int_0^1h_p(x)^r\,dx=\sum_{N\ge0}2^{-(N+1)}H_N^r\); convergence is equivalent to \(r\log_2(2\rho)<1\), including strict exclusion at equality.

**Critical scaling.** Write \(\varepsilon=1-3p\downarrow0\). The Laplace transform of \(\varepsilon K\) is
\[
\mathbb E[e^{-t\varepsilon K}]=\frac{\varepsilon}{q-pe^{-t\varepsilon}-pe^{-2t\varepsilon}}\longrightarrow\frac1{1+t}\qquad(t\ge0).
\]
Thus \(\varepsilon K\) converges to a mean-one exponential. Since \(\log_2(1/X)=K+\log_2(1/U)\), with \(U\) independent uniform and \(\varepsilon\log_2(1/U)\to0\) in probability, Slutsky's theorem gives the final claim.

## Verification
The standalone script `CHECK.py` verifies exact-rational finite coefficient balance for four selected probabilities, normalization at the generating-function level, and rational finite dyadic-annulus formulas. These are consistency tests; all infinite-time and endpoint statements are proved analytically above.

## Relationship to prior work
Kalle and Maggioni (2018), *Invariant densities for random systems of the interval* (arXiv:1805.11430), provide a general constructive approach for piecewise-affine systems expanding on average, including random beta transformations; their named examples do not give this asymmetric dyadic single-contraction model's sharp boundedness transition or critical logarithmic scaling. Suzuki (2023), *Absolutely continuous invariant measures for random dynamical systems of beta-transformations* (arXiv:2303.17521), provides stationary-density series under conditions including an inverse-slope average bound. For this model that bound holds only for \(p<1/7\), whereas the present exact law covers all \(p<1/3\). Yan and coauthors (2023), *Transition to anomalous dynamics in a simple random map* (arXiv:2308.09269), analyze the symmetric Pelikan setting with slopes \(2\) and \(1/2\); the present asymmetric two-zero prefix case has a different queue and different thresholds. General methods for random affine interval maps may imply portions of the explicit expression, so publication priority beyond the sources inspected is not certified.

## Limitations
The model uses precisely contraction \(1/4\) and doubling, independent identical selection and Lebesgue-almost-everywhere assertions. It does not characterize all stationary measures, convergence rates for arbitrary initial laws, or the critical case \(p=1/3\). The full density exhibits dyadic log-periodic modulation above the boundedness threshold, so a simple unmodulated asymptotic constant times a power of \(x\) is not asserted. The checker is finite and does not constitute an independent audit.

## References
- C. Kalle and M. Maggioni, *Invariant densities for random systems of the interval*, arXiv:1805.11430 (first posted 2018-05-29), https://arxiv.org/abs/1805.11430.
- S. Suzuki, *Absolutely continuous invariant measures for random dynamical systems of beta-transformations*, arXiv:2303.17521 (first posted 2023-03-30), https://arxiv.org/abs/2303.17521.
- J. Yan et al., *Transition to anomalous dynamics in a simple random map*, arXiv:2308.09269 (first posted 2023-08-18), https://arxiv.org/abs/2308.09269.
