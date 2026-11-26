# Likelihood-ratio monotonicity of singleton coupons at collection completion

## Finding

Let \(q\ge2\) coupon types be sampled independently and uniformly. Let \(T\) be the discrete draw count at first complete collection and \(S\) the number of types seen exactly once by that draw. The conditional law of \(S\) given \(T=u\) is no larger in monotone likelihood-ratio order than the conditional law given \(T=t\) whenever \(q\le t<u\). In cross-product form, if \(p_{t,s}=\Pr(T=t,S=s)\), then for \(s<r\),
\[
p_{t,s}p_{u,r}\le p_{t,r}p_{u,s}.
\]
This includes zero-probability cells and implies ordinary stochastic ordering. The contribution concerns this discrete conditional order. The joint mass is due to Myers and Wilf [1]. The uniform identity \(\operatorname{Cov}(T,S)=q(H_q^{(2)}-H_q)\) is already recorded in [2]; it is included below with a derivation for context, not as a novelty claim.

## Proof of the order

**Stopping prefixes.** Conditional on \(T=t\) and the identity of the final type, the first \(\ell=t-1\) draws are uniform among words onto the other \(m=q-1\) types. Their singleton count is \(J=S-1\). Let \(F(z)=e^z-1-z=\sum_{a\ge2}z^a/a!\). The number of such words with \(j\) singleton types is
\[
C_{\ell,j}=\binom mj\ell!\,[z^\ell]z^jF(z)^{m-j}.
\]
Indeed the singleton types each contribute one occurrence, and all others contribute at least two. Multiplying rows by the positive factor \(q^{1-t}\) gives the joint mass [1], so the minor signs may be proved directly for \(C\).

**Log-concave coefficients.** The coefficients of \(F\) are nonnegative, with consecutive support and nonincreasing successive ratios on that support. Such sequences convolve to sequences with the same properties: their lower-triangular Toeplitz matrices have nonnegative order-two minors (use decreasing successive ratios on positive cells and interval support at zeros), and Cauchy–Binet on finite truncations preserves the minor signs under multiplication. Fix \(0\le j\le m-2\), and write \(u_b=[z^b]z^jF(z)^{m-j-1}\), setting coefficients below the support to zero. This sequence is log-concave with consecutive support unbounded to the right. For positive cells in both columns,
\[
\frac{C_{\ell,j+1}}{C_{\ell,j}}
=\frac{m-j}{j+1}\left(\sum_{a\ge2}\frac{1}{a!}\frac{u_{\ell-a}}{u_{\ell-1}}\right)^{-1}.
\]
For each \(a\ge2\), the lagged ratio \(u_{\ell-a}/u_{\ell-1}\) is nondecreasing in \(\ell\) wherever its denominator is positive: on positive indices it is a product of \(a-1\) consecutive ratios of the form \(u_b/u_{b+1}\), and entries before the numerator support are zero. Consequently the adjacent-column ratio of \(C\) is nonincreasing with \(\ell\) wherever both cells are positive.

**All minors and boundary cells.** At \(\ell=m\), only \(j=m\) is supported. At \(\ell>m\), the support is \(\max(0,2m-\ell)\le j\le m-1\), since the minimum number of draws with \(j\) singleton types is \(2m-j\), and any excess can go to a nonsingleton type. For \(\ell<\ell'\) and \(j<j'\), a zero left product makes \(C_{\ell,j}C_{\ell',j'}\le C_{\ell,j'}C_{\ell',j}\) automatic. Otherwise \(\ell>m\), \(j'\le m-1\) and the lower support boundary is nonincreasing, so both rows are positive throughout columns \(j,\dots,j'\). Multiply the adjacent-column ratio inequalities over those columns. This also covers \(m=1\), for which no minor has a positive left product. Shifting the columns to \(S=J+1\) and multiplying by row factors preserve the inequalities.

## Previously recorded covariance identity

Write \(H_q=\sum_{j=1}^q j^{-1}\) and \(H_q^{(2)}=\sum_{j=1}^q j^{-2}\). With \(v=z/q\), the probability generating function of \(T\) is \(G_q(z)=q!v^q\prod_{h=1}^{q-1}(1-hv)^{-1}\), by the independent geometric waiting times for new types. For one specified type, being last contributes \(G_q(z)/q\) to its singleton-weighted generating function. If another type is last, delete the specified singleton from the word before the last coupon. The remaining word is onto the \(k=q-2\) other types. These onto words have ordinary generating function \(k!B_k(v)\), with \(B_k(v)=v^k\prod_{h=1}^k(1-hv)^{-1}\): order the first appearances and insert arbitrary words on the types already seen. A word of length \(b\) allows \(b+1\) singleton insertion positions before the final coupon. Summing over the \(q-1\) choices of final type and then summing over specified singleton types gives
\[
\mathbb E[z^TS]=G_q(z)+q!v^2B_k(v)(1+D\log B_k(v)),\qquad D=v\frac{d}{dv}.
\]
For \(v=1/q\), the factor \(q!v^2B_k(v)\) is \(1/q\), \(D\log B_k(v)=q(H_q-1)-1\), and \(D^2\log B_k(v)=q^2(H_q^{(2)}-1)-q(H_q-1)\), by differentiating the product. Hence \(\mathbb E[S]=H_q\) and \(\mathbb E[TS]=q(H_q^2-H_q+H_q^{(2)})\). Subtracting \(\mathbb E[T]\mathbb E[S]\), with \(\mathbb E[T]=qH_q\), gives the identity in [2], strictly negative for \(q\ge2\).

## Verification and scope

The supplied `verify.py` checks the known joint mass against a direct occupancy recursion, the reverse minors exactly for \(2\le q\le9\) and \(q\le t<u\le55\), and direct word counts for \(q\le4\), \(t\le8\). It also checks the covariance numerically by truncating the moment sums. These finite checks are corroboration, not substitutes for the analytic argument. No discrete nonuniform order is asserted. A likelihood-ratio comparison given an auxiliary continuous Poissonized cover time [3] is on a different conditioning variable; smoothing a discrete kernel does not in general let one infer the original minors from the smoothed minors.

## References

1. A. N. Myers and H. S. Wilf, *Some New Aspects of the Coupon-Collector's Problem*, 2003, §4, joint-mass equation (44) in the [PDF](https://arxiv.org/pdf/math/0304229).
2. [*Universal negative cover-time–singleton covariance for unequal coupons*](https://github.com/Resultary/2026/blob/main/2026/10/12/SCOPE-universal-negative-cover-time-singleton-covariance-for-unequal-c--095ece1fb7b6/RESULT.md), uniform specialization.
3. [*Strict likelihood-ratio decay of singleton abundance at nonuniform coupon collection*](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-strict-likelihood-ratio-decay-of-singleton-abundance-at-nonunifo--261de08382e0/RESULT.md), continuous Poissonized completion-time result.
