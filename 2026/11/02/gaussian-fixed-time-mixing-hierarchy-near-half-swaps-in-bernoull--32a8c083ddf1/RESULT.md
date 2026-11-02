# Gaussian fixed-time mixing hierarchy near half swaps in Bernoulli–Laplace urns

## Finding

Let \(n\) run through even positive integers, and let \(k=k_n\in\{1,\ldots,n-1\}\) satisfy \(k/n\to1/2\). In the balanced Bernoulli–Laplace chain, each urn contains \(n\) balls, the combined stock contains \(n\) red and \(n\) white balls, and at each step an independent uniform \(k\)-subset of each urn is exchanged with the other. Write \(X_t\) for the number of red balls in the first urn. Its stationary distribution is
\[
\pi_n(j)=\frac{\binom{n}{j}^{2}}{\binom{2n}{n}},\qquad 0\le j\le n.
\]
Set \(\lambda_n=1-2k_n/n\), and let \(\Phi\) be the standard normal distribution function. For **each fixed integer** \(t\ge2\), the following approximation is uniform over all initial states \(x\in\{0,\ldots,n\}\):
\[
\boxed{\sup_{0\le x\le n}\left|\left\|P_n^t(x,\cdot)-\pi_n\right\|_{\mathrm{TV}}-\left[2\Phi\!\left(\frac{|\lambda_n|^t|x-n/2|}{\sqrt{n/2}}\right)-1\right]\right|\longrightarrow0.}
\]
Consequently the worst-start distance satisfies
\[
\boxed{d_n(t):=\max_x\|P_n^t(x,\cdot)-\pi_n\|_{\mathrm{TV}}=2\Phi\!\left(\frac{\sqrt n|\lambda_n|^t}{\sqrt2}\right)-1+o(1).}
\]
At one step, \(d_n(1)\to1\). Writing \(\delta_n=k_n-n/2=o(n)\), the sharp fixed-time transition window is \(|\delta_n|\asymp n^{1-1/(2t)}\): if \(\delta_n/n^{1-1/(2t)}\to c\in\mathbb R\), then
\[
\boxed{d_n(t)\longrightarrow 2\Phi\!\left(\frac{(2|c|)^t}{\sqrt2}\right)-1.}
\]
If the absolute ratio goes to zero the distance tends to zero, and if it diverges while \(\delta_n=o(n)\), the distance tends to one. In particular, for \(k_n=n/2\) the worst-case mixing time at every fixed accuracy \(\varepsilon\in(0,1)\) is **exactly two steps for all sufficiently large even** \(n\). More generally \(|k_n-n/2|=o(n^{3/4})\) also implies eventual two-step mixing, whereas the second-step window at the \(n^{3/4}\) scale has the displayed nondegenerate Gaussian profile.

## Assumptions and scope

All random choices in distinct steps and in the two urns are independent. The count process has finite state space \(\{0,1,\ldots,n\}\). The convergence \(k_n/n\to1/2\) is essential, and \(t\) is held fixed as \(n\to\infty\); this is not a growing-time cutoff assertion. Total variation is \(\|\mu-\nu\|_{\mathrm{TV}}=\frac12\sum_j|\mu(j)-\nu(j)|\). Define the discrete Gaussian \(G_{n,m}\) on \(\{0,\ldots,n\}\), for real \(m\), by
\[
G_{n,m}(j)=\frac{\exp[-4(j-m)^2/n]}{\sum_{h=0}^{n}\exp[-4(h-m)^2/n]}.
\]
The intermediate, stronger assertion proved below is
\[
\sup_{0\le x\le n}\bigl\|P_n^t(x,\cdot)-G_{n,m_{n,t}(x)}\bigr\|_{\mathrm{TV}}\to0,\qquad m_{n,t}(x)=\frac n2+\lambda_n^t\left(x-\frac n2\right),\quad t\ge2.
\]

## Proof

**1. Exact transition moments and stationarity.** Conditional on \(X_s=x\), the red balls selected from the first and second urns are independent variables
\[
U\sim\mathrm{Hyp}(n,x,k),\qquad V\sim\mathrm{Hyp}(n,n-x,k),\qquad X_{s+1}=x-U+V.
\]
Here \(\mathrm{Hyp}(N,K,\ell)\) is the number of distinguished balls in a uniform sample of size \(\ell\) from \(N\) balls, \(K\) distinguished. Direct hypergeometric moments yield
\[
\mathbb E[X_{s+1}\mid X_s=x]=\frac n2+\lambda_n\left(x-\frac n2\right),
\qquad \operatorname{Var}(X_{s+1}\mid X_s=x)=\frac{2k(n-k)x(n-x)}{n^2(n-1)}.
\]
The uniform distribution on labelled colour placements is invariant under independent uniform equal-size swaps, giving the hypergeometric stationary count law above. Iterating the conditional mean from a fixed \(X_0=x\) gives exactly \(\mathbb E_xX_s=m_{n,s}(x)\). The conditional variance is at most \(n^2/[8(n-1)]\), so the total-variance recursion gives, for every fixed \(s\),
\[
\sup_x\operatorname{Var}_x(X_s)\le \frac{n^2}{8(n-1)}\sum_{j=0}^{s-1}\lambda_n^{2j}=O_s(n).
\]
As \(\lambda_n\to0\), for every fixed \(s\ge1\), \(X_s/n\to1/2\) in probability **uniformly in the initial count**, by Chebyshev's inequality.

**2. Uniform one-step lattice local limit near the centre.** We establish the following lemma: along any triangular sequences of integers \(x_n,k_n\) with \(x_n/n\to1/2\) and \(k_n/n\to1/2\),
\[
\left\|P_n(x_n,\cdot)-G_{n,\,n/2+\lambda_n(x_n-n/2)}\right\|_{\mathrm{TV}}\to0.
\]
To see this without presuming a Gaussian approximation, use the exact mass function
\[
\Pr(\mathrm{Hyp}(n,K,\ell)=u)=\frac{\binom K u\binom{n-K}{\ell-u}}{\binom n\ell}.
\]
For \(K/n\to1/2\), \(\ell/n\to1/2\), its mean is \(\mu=\ell K/n\) and its variance is \(\sigma^2=\ell(n-\ell)K(n-K)/[n^2(n-1)]\sim n/16\). On every fixed central window \(|u-\mu|\le M\sqrt n\), Stirling's formula, uniformly for four factorial ratios bounded away from their endpoints, gives
\[
\sup_{|u-\mu|\le M\sqrt n}\left|\sqrt n\Pr(\mathrm{Hyp}(n,K,\ell)=u)-\frac4{\sqrt{2\pi}}\exp\!\left[-\frac{8(u-\mu)^2}{n}\right]\right|\to0.
\]
Indeed \(\log\binom ab=ah(b/a)-\tfrac12\log[2\pi a(b/a)(1-b/a)]+O(a^{-1})\), where \(h(p)=-p\log p-(1-p)\log(1-p)\); Taylor expansion about \(u=\mu\) cancels the linear term, the quadratic term tends to \(-8(u-\mu)^2/n\), and the cubic remainder is \(O_M(n^{-1/2})\). The constant comes from the prefactor and \(\sigma^2\sim n/16\). Hypergeometric variance bounds and Chebyshev's inequality control the complementary tails by \(O(M^{-2})\). First taking \(n\to\infty\), then \(M\to\infty\), proves total-variation approximation by the normalized discrete Gaussian with that mean and variance \(n/16\). Applying this independently to \(U\) and \(V\), the contraction of total variation under convolution, followed by a Gaussian Riemann-sum convolution, proves the lemma with total variance \(n/8\). These estimates hold for **every** such parameter sequence, which also supplies the requisite uniformity over a shrinking relative neighbourhood of the centre (otherwise select a violating sequence).

**3. Uniform discrete-normal approximation after two or more steps.** Fix \(t\ge2\). By Step 1, \(X_{t-1}/n\to1/2\) uniformly in the starting state. Step 2 therefore implies that the conditional law of \(X_t\), given \(X_{t-1}\), is within \(o(1)\) total variation (uniform in the starting state after averaging) of \(G_{n,\,n/2+\lambda_n(X_{t-1}-n/2)}\). The latter random centre differs from the deterministic centre \(m_{n,t}(x)\) by \(\lambda_n(X_{t-1}-\mathbb E_xX_{t-1})\). Step 1 bounds its expected absolute size by \(O_t(|\lambda_n|\sqrt n)=o(\sqrt n)\). Equal-variance discrete Gaussians whose centres differ by \(o(\sqrt n)\) in expected absolute value have total variation \(o(1)\): this follows from the normal shift bound \(C|a-b|/\sqrt n\) and the uniform lattice Riemann-sum error. The claimed uniform approximation to \(G_{n,m_{n,t}(x)}\) follows. Boundary truncation is negligible because both centres differ from \(n/2\) by \(o(n)\) uniformly in \(x\).

**4. Exact asymptotic total-variation profile.** The stationary hypergeometric mass
\[\pi_n(j)=\frac{\binom n j^2}{\binom{2n}n}\]
satisfies the same Stirling argument and variance \(n^2/[4(2n-1)]\sim n/8\), hence \(\|\pi_n-G_{n,n/2}\|_{\mathrm{TV}}\to0\). For two Gaussians of equal variance \(n/8\) and means differing by \(a\), the total variation is exactly \(2\Phi(|a|/\sqrt{n/2})-1\). The analogous identity for the discretizations has uniform \(o(1)\) error, even when \(|a|/\sqrt n\) diverges: the likelihood ratio crosses one at the midpoint of the means, so their total variation is a difference of two one-sided Gaussian distribution functions, each having uniform lattice-to-continuum error \(O(n^{-1/2})\). Applying the triangle inequality in both directions and using Step 3 proves the uniform formula in the Finding. Its right-hand side is increasing in \(|x-n/2|\), whose maximum is \(n/2\), giving \(d_n(t)\). Substituting \(|\lambda_n|=2|\delta_n|/n\) yields all three scaling regimes.

**5. One step and sharpness.** From \(X_0=0\), the only red balls are in the second urn, so \(X_1=k\) deterministically. Therefore \(d_n(1)\ge1-\pi_n(k)\). The largest stationary point mass is \(O(n^{-1/2})\) by the same Stirling estimate, and thus \(d_n(1)\to1\). When \(\delta_n=o(n^{3/4})\), the \(t=2\) formula gives \(d_n(2)\to0\); combined with \(d_n(1)\to1\), this yields eventual mixing time exactly two for every fixed accuracy in \((0,1)\).

## Verification

Run `python checker.py` (standard library only). It independently constructs the full transition matrix from two hypergeometric draws and checks normalization, reversibility against the stationary hypergeometric law, exact first and second conditional moments, and finite-step comparisons using rational arithmetic for even orders \(4,6,8,10,12\). Its larger-order calculations are numerical diagnostics only; the proof for all orders is the analytic local-limit argument above. The checker prints its actual assertion count and halved-swap two-step distance, and requires no downloaded data.

## Relationship to prior work

Griffin, Hall, Hebner, Herzog, Selyuzhitsky, Wong and Wright (arXiv:2308.08676v1, Section 4, Theorem 4.2) prove only an accuracy-dependent **bounded** mixing time, with lower bound two, in a critical generalization; their hypothesis requires \(|\lambda_1|=O(n^{-1/2})\), corresponding here to \(|k-n/2|=O(\sqrt n)\), and gives neither the fixed-step Gaussian profile nor the \(n^{1-1/(2t)}\) hierarchy. Alameda, Bang, Brennan, Herzog, Kritschgau and Sprangel (arXiv:2203.08647v1, Assumption 1 and Theorem 1.2) work with limiting exchange fractions strictly below one half and therefore do not cover this boundary. Nestoridi and White (arXiv:1606.01437v2, Section 4.1 and Theorem 5) handle the exact half-swap case spectrally but their displayed vanishing bound begins at **three** steps, whereas the present result proves two-step total-variation convergence and a larger varying-parameter hierarchy. Their exact eigenvalue framework is compatible with, but does not by itself state, the new local-Gaussian profile.

## Limitations

This result treats only the balanced two-colour, equal-urn, discrete-time Bernoulli–Laplace chain, with independent fixed-size swaps and \(k_n/n\to1/2\). It does not determine a uniform profile for times growing with \(n\), unequal urn sizes, non-hypergeometric exchange mechanisms, or the borderline mixing-time outcome when an accuracy threshold exactly equals the limiting critical profile. Numerical tests do not certify asymptotic claims. General spectral formulas or other unindexed earlier estimates might yield an equivalent theorem; the historical originality comparison is not an independent priority certification.

## References

1. T. Griffin, B. Hall, J. Hebner, D. Herzog, D. Selyuzhitsky, K. Wong, J. Wright, *Cutoff in the Bernoulli-Laplace Model With Unequal Colors and Urn Sizes*, arXiv:2308.08676v1, first posted 2023-08-16, https://arxiv.org/html/2308.08676v1 .
2. J. S. Alameda, C. Bang, Z. Brennan, D. P. Herzog, J. Kritschgau, E. Sprangel, *Cutoff in the Bernoulli-Laplace model with \(O(n)\) swaps*, arXiv:2203.08647v1, first posted 2022-03-16, https://arxiv.org/abs/2203.08647 .
3. E. Nestoridi, G. White, *Shuffling large decks of cards and the Bernoulli-Laplace urn model*, arXiv:1606.01437v2, https://arxiv.org/html/1606.01437v2 .
4. A. Eskenazis, E. Nestoridi, *Cutoff for the Bernoulli-Laplace urn model with \(o(n)\) swaps*, arXiv:1805.07803, https://arxiv.org/abs/1805.07803 .
