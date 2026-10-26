# Rarest-taxon asymptotics for the covariance of observed richness and Shannon diversity

## Finding

Let \(s\ge2\) fixed, with a species-probability vector \(p=(p_1,\ldots,p_s)\), where every \(p_i>0\) and \(\sum_i p_i=1\). From \(n\ge1\) independent categorical draws let \(N_i\) count species \(i\), \(K_n=\sum_i\mathbf 1\{N_i>0\}\) be observed richness, and \(\widehat H_n=-\sum_i(N_i/n)\log(N_i/n)\) be plug-in Shannon entropy, with \(0\log0=0\) and natural logarithms.

For each \(i\), let \(p^{(-i)}\) denote the \((s-1)\)-component distribution formed by deleting species \(i\) and dividing the other probabilities by \(1-p_i\). Define \(M_n(r)=\mathbb E_r[\widehat H_n]\). For every \(n\ge1\), the **exact deletion identity** is

\[
\operatorname{Cov}_p(K_n,\widehat H_n)=\sum_{i=1}^s(1-p_i)^n\bigl(M_n(p)-M_n(p^{(-i)})\bigr).
\]

Let \(t=\min_i p_i\), with multiplicity \(m\), and let \(u>t\) be the next distinct probability, if one exists. Put \(q=p^{(-i)}\) for any \(i\) with \(p_i=t\), and

\[
\Delta=H(p)-H(q)=h(t)-tH(q)>0,\qquad h(t)=-t\log t-(1-t)\log(1-t),
\]
\[
B=\frac1t+t\sum_{j\ne i}\frac1{p_j}.
\]

(The displayed \(\Delta\) and \(B\) do not depend on the choice of a minimum-probability species.) As \(n\to\infty\),

\[
\boxed{\operatorname{Cov}(K_n,\widehat H_n)=m(1-t)^n\left[\Delta-\frac1{2n}-\frac{B}{12n^2}+O_p(n^{-3})\right]+O_p((1-u)^n).}
\]

When no \(u\) exists, the last term is absent. In particular, the covariance is strictly positive for all sufficiently large \(n\), and

\[
\lim_{n\to\infty}\frac{\operatorname{Cov}(K_n,\widehat H_n)}{(1-t)^n}=m\Delta>0.
\]

Thus the rarest species, not the most abundant, determine the exact exponential decay rate of this joint sampling uncertainty. The first relative correction \(-1/(2n)\) is independent of the species proportions; the second is explicit.

## Assumptions and scope

The result concerns one fixed finite community distribution with strictly positive probabilities, independent sampling with replacement, and the uncorrected plug-in Shannon entropy. Sample size \(n\) tends to infinity with \(s\) and \(p\) fixed. Multiple taxa may share the minimum probability. The claim is an identity and an asymptotic theorem; it does **not** assert positive covariance for every finite sample size, nor does it cover growing alphabets or sampling without replacement.

## Proof

**1. Exact deletion formula.** Let \(A_i=\mathbf1\{N_i=0\}\), so \(K_n=s-\sum_i A_i\). By linearity of covariance,
\[
\operatorname{Cov}(K_n,\widehat H_n)=-\sum_i\operatorname{Cov}(A_i,\widehat H_n).
\]
The probability of \(A_i=1\) is \((1-p_i)^n\). Conditional on that event, the \(n\) observations are independent with distribution \(p^{(-i)}\), so \(\mathbb E[\widehat H_n\mid A_i=1]=M_n(p^{(-i)})\). Therefore each negative covariance is \((1-p_i)^n[M_n(p)-M_n(p^{(-i)})]\). Summing proves the exact identity, with no approximation and no claim of independence among absence indicators.

For any probability vector \(r=(r_1,\ldots,r_d)\), \(M_n(r)\) can be reproduced from the binomial marginals without enumerating all categorical samples:
\[
M_n(r)=\log n-\frac1n\sum_{a=1}^{d}\sum_{k=1}^{n}{n\choose k}r_a^k(1-r_a)^{n-k}k\log k.
\]
The \(k=1\) summand vanishes. This is also an exact, computable finite-sample expression for the covariance.

**2. Entropy-bias expansion.** For any fixed strictly positive \(d\)-category distribution \(r\), a binomial Taylor expansion of \(f(x)=-x\log x\) at each \(r_a\) yields
\[
M_n(r)=H(r)-\frac{d-1}{2n}+\frac{1-\sum_a r_a^{-1}}{12n^2}+O_r(n^{-3}).
\]
Indeed, for \(X\sim\operatorname{Bin}(n,v)\), the central moments of \(X/n\) through order four are respectively \(0\), \(v(1-v)/n\), \(v(1-v)(1-2v)/n^2\), and \(3v^2(1-v)^2/n^2+O(n^{-3})\). The first four derivatives of \(f\) give a contribution \(-(1-v)/(2n)+(v-v^{-1})/(12n^2)\) beyond \(f(v)\). Expanding two derivatives further and using the fifth and sixth centered moments, both \(O(n^{-3})\), controls the remaining expectation on \(|X/n-v|\le v/2\); a standard binomial exponential-tail bound controls its complement. Summing over the fixed number \(d\) of categories gives the formula. For \(d=1\), both sides are zero exactly. This also agrees with the published finite-alphabet entropy-bias expansion cited below.

Subtracting the expansion for \(q=p^{(-i)}\) from that for \(p\) gives, for every fixed \(i\),
\[
M_n(p)-M_n(q)=H(p)-H(q)-\frac1{2n}-\frac1{12n^2}\left[\frac1{p_i}+p_i\sum_{j\ne i}\frac1{p_j}\right]+O_p(n^{-3}),
\]
because \(\sum_{j\ne i}1/q_j=(1-p_i)\sum_{j\ne i}1/p_j\). All constants can be chosen uniformly across the finite set of deleted distributions.

**3. Rarest-taxon dominance and strict sign.** The minimum probability \(t\) is at most \(1/s\). Normalizing the other \(s-1\) probabilities after deleting a minimum-probability taxon gives the Shannon chain-rule identity \(H(p)=h(t)+(1-t)H(q)\), so \(\Delta=h(t)-tH(q)\). Since \(H(q)\le\log(s-1)\) and
\[
\frac{h(t)}{t}>-\log t\ge\log s>\log(s-1),
\]
one has \(\Delta>0\). Every minimum-probability taxon has the same \(H(q)\) and \(B\), because only the value \(t\) matters. Its absence probability is \((1-t)^n\), while each other absence probability is at most \((1-u)^n\) when \(u\) exists. The exact deletion formula and the boundedness \(0\le M_n(r)\le\log s\) bound their collective contribution by \(O_p((1-u)^n)\). Inserting Step 2 for the \(m\) minima yields the boxed expansion. Its leading coefficient is strictly positive, completing the proof.

## Verification

Run `python verify.py` in the folder containing `certificate.json`. It recomputes the certificate and checks 180 coefficients of \(\log k\) **exactly over rational arithmetic**, comparing a direct multinomial enumeration of \(\operatorname{Cov}(K_n,\widehat H_n)\) with the independently computed conditional-deletion formula. Five rational species profiles and sample sizes two through nine are included. Numerical large-sample diagnostics for three profiles show the normalized covariance approaching \(\Delta\) and the scaled first-order difference approaching \(-1/2\). These are checks, not proofs of the asymptotic limit; the proof above handles all fixed positive distributions.

## Relationship to prior work

Shannon entropy and observed richness are standard but distinct ecological diversity summaries. De'ath (2012) models multinomial Shannon diversity in relation to ecological predictors. Gauthier and Derome (2021) explain how richness and evenness can diverge between ecological samples. Chen et al. (2018) record the established fixed-alphabet plug-in entropy bias expansion used and independently derived in Step 2. The present mathematical object is the **within-sample covariance of observed species count and plug-in Shannon entropy**, with its exact deletion identity and rarest-taxon exponential asymptotics. These statements are not asserted by the cited entropy-estimation or diversity-visualization results. An existing mathematical result on covariance of observed richness and unbiased Gini–Simpson diversity concerns a different index, whose algebra does not imply the Shannon asymptotic coefficient without further argument. Older general occupancy and entropy identities could potentially subsume the deletion step; that bibliographic risk remains.

## Limitations

The infinite-sample result requires a fixed positive finite alphabet. It does not determine the covariance sign at every finite \(n\), does not provide uncertainty bounds for estimated probabilities, and does not establish results under spatial clustering, non-iid field observations, or undetected species with exactly zero sampling probability. The exact deletion identity remains valid at \(n=1\), where both statistics are constant. Independent scholarly review and a broader search for equivalent results under occupancy/entropy terminology remain necessary.

## References

- De'ath, G. (2012), “The multinomial diversity model: linking Shannon diversity to multiple predictors,” *Ecology* 93, 2286–2296, doi:10.1890/11-2155.1. First public journal date 2012-10-01.
- Chen, C., Grabchak, M., Stewart, A., Zhang, J., and Zhang, Z. (2018), “Normal Laws for Two Entropy Estimators on Infinite Alphabets,” *Entropy* 20, 371, doi:10.3390/e20050371, especially equation (3).
- Gauthier, J., and Derome, N. (2021), “Evenness-Richness Scatter Plots,” *mSphere* 6, e01019-20, doi:10.1128/msphere.01019-20.
- Hausser, J., and Strimmer, K. (2009), “Entropy Inference and the James–Stein Estimator,” *JMLR* 10, 1469–1484, sections 2.1–2.2, https://www.jmlr.org/papers/volume10/hausser09a/hausser09a.pdf.
