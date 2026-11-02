# The sharp sparse-alphabet information law for random parking functions

## Finding

Let \(\Pi_n=(\Pi_n(1),\ldots,\Pi_n(n))\) be uniformly distributed over ordinary parking functions of size \(n\), and let \(U_n(1),\ldots,U_n(n)\) be independent uniform variables on \(\{1,\ldots,n\}\). Choose an *a priori deterministic* set \(E_n\subseteq\{1,\ldots,n\}\); at each of the first \(k_n\) coordinates, reveal the exact symbol if it belongs to \(E_n\), and otherwise reveal a single common censoring symbol \(\star\). Write \(\mathcal P_{n,k_n}^{E_n}\) and \(\mathcal Q_{n,k_n}^{E_n}\) for the laws of these two censored sequences. All logarithms are natural.

**Theorem (sharp alphabet-budget profile).** Fix \(\lambda\in(0,\infty)\), and take positive integers \(k_n\) with \(k_n\log n/n\to\lambda\). Suppose integers \(1\le M_n=o(n)\) satisfy \(\log M_n/\log n\to\alpha\in[0,1]\). Then

\[
\lim_{n\to\infty}\;\max_{E\subseteq\{1,\ldots,n\},\ |E|\le M_n}
 d_{\mathrm{TV}}(\mathcal P_{n,k_n}^{E},\mathcal Q_{n,k_n}^{E})
 =2\Phi\!\left(\sqrt{\lambda\alpha/\pi}\right)-1.
\]

For every \(n\), the deterministic *balanced boundary alphabet*
\[
E_n^*=\{1,\ldots,\lfloor M_n/2\rfloor\}\cup
\{n-\lceil M_n/2\rceil+1,\ldots,n\}
\]
attains this limiting optimum. In particular, an asymptotically vanishing fraction of available labels can preserve the *entire* uncensored critical testing profile: take \(M_n=\lfloor n/\log n\rfloor\), for which \(\alpha=1\). Conversely, any polynomial budget \(M_n=n^{\alpha+o(1)}=o(n)\) retains exactly the information fraction \(\alpha\) in the Gaussian limit.

A more general, non-optimization statement is also proved: if \(E_n\) has \(o(n)\) labels and its normalized marginal-bias energy
\[
 h=\lim_{n\to\infty}\frac{1}{\log n}\sum_{j\in E_n}g_n(j)^2\quad\text{exists},
 \qquad g_n(j)=n\Pr(\Pi_n(1)=j)-1,
\]
then the censored total variation tends to \(2\Phi(\sqrt{\lambda h}/2)-1\). Thus the testing limit depends on the selected alphabet only through one explicit logarithmic energy.

## Assumptions and scope

A parking function of size \(n\) is an integer sequence whose increasing rearrangement obeys \(a_{(i)}\le i\) for all \(1\le i\le n\). There are \((n+1)^{n-1}\) such sequences, each equally likely under \(\mathcal P\). Under \(\mathcal Q\), the \(n\) symbols are initially independent uniform variables; the two experiments are compared **only after censoring**. The alphabet \(E_n\) is selected before data are observed and is shared across coordinates. The theorem does not address adaptive, coordinate-dependent or arbitrary non-censoring observation maps. The budget may be bounded or increase, but must satisfy \(M_n=o(n)\). The limiting constant \(\lambda\) is strictly positive and finite.

## Proof

**1. Independent-marginal reduction.** Let \(\mu_n\) be the one-coordinate law of the uniform parking function, and put \(P_{n,k}=\mathcal L(\Pi_n(1),\ldots,\Pi_n(k))\). A known entropy-contraction lemma for exchangeable distributions with Lorentzian occupation polynomials states that
\[
D(P_{n,k}\Vert\mu_n^{\otimes k})\le
\frac{k(k-1)}{n(n-1)}D(P_{n,n}\Vert\mu_n^{\otimes n}).
\]
The parking occupation polynomial satisfies the hypothesis: the support of \(\prod_{i=1}^n(z_1+\cdots+z_i)\) is exactly the allowable parking occupation vectors, the product is Lorentzian, and the Lorentzian support-normalization theorem transfers this property to the polynomial with coefficients proportional to \(1/\prod_j a_j!\), which is the parking occupation probability polynomial. The entropy-contraction lemma follows from the strengthened delete-one entropy inequality of Lee and Seo: for an exchangeable Lorentzian length-\(r\) law, \(rH_{r-1}\ge(r-2)H_r+rH_1\); with \(D_r=rH_1-H_r\), this gives monotonicity of \(D_r/[r(r-1)]\). Finally,
\[
D(P_{n,n}\Vert\mu_n^{\otimes n})
=\log\frac{n^n}{(n+1)^{n-1}}-nD(\mu_n\Vert U_n)\le\log n.
\]
Pinsker's inequality and data processing under *every* deterministic censoring map yield, uniformly in \(E\),
\[
\big|d_{\mathrm{TV}}(\mathcal P_{n,k}^{E},\mathcal Q_{n,k}^{E})-
 d_{\mathrm{TV}}((\mu_n^{E})^{\otimes k},(U_n^{E})^{\otimes k})\big|
\le\sqrt{\frac{k(k-1)\log n}{2n(n-1)}}=o(1)
\]
when \(k\log n/n\to\lambda\). Here \(\mu_n^{E}\) and \(U_n^{E}\) are one-coordinate censored marginals. In particular, no independence approximation is asserted for \(k\) comparable to \(n\).

**2. Exact bias and the two endpoint tails.** The one-coordinate formula of Diaconis and Hicks, written using Borel probabilities \(q_i=e^{-i}i^{i-1}/i!\), gives
\[
g_n(1)=\frac{n-1}{n+1},\qquad
 g_n(i)-g_n(i+1)=\frac{q_iq_{n+1-i}}{q_{n+1}}>0\quad(1\le i<n).
\]
In particular \(\sum_jg_n(j)=0\), \(e^{-1}\le1+g_n(j)\le2\), and the reflection identity
\[
g_n(j)+g_n(n+2-j)=-\frac2{n+1}\quad(2\le j\le n)
\]
holds. Stirling's bounds, telescoping the displayed exact differences and the Borel tail estimate \(\sum_{i\ge j}q_i=\sqrt{2/\pi}\,j^{-1/2}+O(j^{-3/2})\) give uniformly for \(j\le(n+2)/2\)
\[
g_n(j)=\sqrt{2/\pi}\,j^{-1/2}
 +O(j^{-3/2}+\sqrt j/n).
\]
Consequently, with \(r_n(j)=\min(j,n+1-j)\),
\[
g_n(j)^2=\frac{2}{\pi r_n(j)}+O(r_n(j)^{-2}+n^{-1}),
\quad |g_n(j)|\le C r_n(j)^{-1/2},
\quad \sum_{j=1}^n|g_n(j)|^3\le C.
\]
These are uniform in \(n,j\); the finite special cases are absorbed in the constants. For any \(E\) containing \(m\) symbols, there are at most two symbols at every depth \(r_n(j)\). Rearranging the decreasing harmonic weights gives
\[
\sum_{j\in E}g_n(j)^2\le \frac4\pi\log(m+1)+O(1+m/n).
\]
For the balanced boundary set \(E_n^*\) of size \(m=o(n)\), summing the first approximately \(m/2\) depths at both ends gives
\[
\sum_{j\in E_n^*}g_n(j)^2=\frac4\pi\log(m+1)+O(1+m/n).
\]
Also \(|\sum_{j\in E}g_n(j)|\le C\sqrt m\), uniformly in the selected set.

**3. The exact effect of censoring.** Fix \(E\) of size \(m<n\). Under the censored uniform law, each observed label \(j\in E\) has mass \(1/n\) and the lumped symbol \(\star\) has mass \((n-m)/n\). Its one-coordinate likelihood ratio for the parking marginal is \(1+h_{n,E}\), with
\[
h_{n,E}(j)=g_n(j)\ (j\in E),\qquad
 h_{n,E}(\star)=-\frac{S_{n,E}}{n-m},\qquad
 S_{n,E}=\sum_{j\in E}g_n(j).
\]
The score has mean zero and exact second moment
\[
 I_{n,E}:=\mathbb E_{U_n^E}[h_{n,E}^2]
 =\frac1n\left(\sum_{j\in E}g_n(j)^2+\frac{S_{n,E}^2}{n-m}\right).
\]
For any \(m\le M_n=o(n)\), \(S_{n,E}^2/(n-m)=O(m/n)\) uniformly, and
\[
\mathbb E_{U_n^E}|h_{n,E}|^3
 \le C/n+C m^{3/2}/n^3.
\]
Moreover the exact likelihood ratios are uniformly bounded away from zero and infinity for large \(n\); this follows from the bound on \(1+g_n(j)\) and \(|S_{n,E}|/(n-m)\le C\sqrt m/(n-m)=o(1)\).

**4. Uniform Gaussian likelihood approximation.** For \(k_n\log n/n\to\lambda\), write \(L_{n,E}\) for the log likelihood of \((\mu_n^E)^{\otimes k_n}\) against \((U_n^E)^{\otimes k_n}\). For each fixed real \(t\), Taylor's theorem applied to \((1+h)^{it}\) on the above compact positive interval gives
\[
\mathbb E_{(U_n^E)^{\otimes k_n}} e^{itL_{n,E}}
=\left(1-\frac{t^2+it}{2}I_{n,E}
+O_t(n^{-1}+m^{3/2}n^{-3})\right)^{k_n}.
\]
The remainder multiplied by \(k_n\) goes to zero *uniformly over all admissible \(E\)*; also \(k_n I_{n,E}=O(1)\). Hence along any sequence of alphabets for which \(k_nI_{n,E_n}\to v\), Lévy's theorem yields
\[
L_{n,E_n}\Rightarrow N(-v/2,v),
\]
including \(v=0\). The bounded continuous function \(x\mapsto(1-e^x)_+\) converts this Gaussian likelihood limit to
\[
d_{\mathrm{TV}}((\mu_n^{E_n})^{\otimes k_n},(U_n^{E_n})^{\otimes k_n})
\longrightarrow 2\Phi(\sqrt v/2)-1.
\]
Since \(k_nI_{n,E_n}-(k_n/n)\sum_{j\in E_n}g_n(j)^2\to0\), the general energy law follows, with \(v=\lambda h\).

**5. Optimization, including nonconvergent selected sets.** Uniformly over all \(|E|\le M_n\), the preceding rearrangement shows
\[
\limsup k_nI_{n,E}\le 4\lambda\alpha/\pi.
\]
For any sequence of alleged better subsets, extract a subsequence along which their bounded information values converge. The Gaussian formula then forces its subsequential total-variation limit to be no greater than \(2\Phi(\sqrt{\lambda\alpha/\pi})-1\). This argument does not assume the maximizing subsets converge or that their scores converge. The balanced boundary subsets have matching information limit \(4\lambda\alpha/\pi\), so they attain the upper bound. This proves the theorem.

## Verification

The accompanying standalone Python 3 program `checker.py` exhaustively enumerates all parking functions for lengths \(2\) through \(6\), compares exact rational one-coordinate probabilities against the Borel-ratio recurrence, checks endpoint reflection and positivity, and verifies finite data processing and the exact censored chi-square identity for all tested small censoring sets. It also prints supplementary non-certifying numerical convergence of the balanced boundary energy. The verified program reported 209 passing exact assertions. The analytic argument, not these finite checks, establishes the asymptotic theorem.

## Relationship to prior work

Avital, Kontorovich, Vershynin and Zou (arXiv:2609.21049v1, first public September 17, 2026) study universal constant-factor total-variation formulas for products and hypothesis testing. Their general results do not provide an exact Gaussian constant or determine the optimal subset of observable labels of a parking-function law. The older one-coordinate parking laws of Diaconis and Hicks and the limited-coordinate approximation of Bellin provide foundational context. Lee and Seo (arXiv:2608.17920v1) prove the strengthened Lorentzian delete-one entropy inequality used here.

Kortchemski (arXiv:2610.40082v1, first posted October 29, 2026) subsequently established the uncensored parking-coordinate critical total-variation profile and the product-marginal approximation used as an input. That paper has been examined in full; its stated results do **not** optimize over sparse, value-revealing censoring alphabets. The present result depends substantively on the uncensored approximation and should not be claimed to supersede it. The October 29 paper was not used to establish the September 17 starting-publication date.

## Limitations

The theorem is restricted to a fixed positive finite critical sample-size constant, a single predetermined censoring alphabet shared by all observed positions, and sublinear alphabet budgets. It does not establish an optimal finite-\(n\) subset or extend to adaptive observation. The Gaussian limit is a theorem; the supplementary finite tests are not a substitute for the cited nonstandard entropy inequality. Broader statistical experiment-compression theory might already imply an equivalent formula, so historical originality remains provisional until independent literature audit. Independent proof validation has not been carried out.

## References

- A. Avital, A. Kontorovich, R. Vershynin, G. Zou. *Total Variation Distance between Product Distributions: an Analytic Proxy*. arXiv:2609.21049v1 (September 17, 2026). https://arxiv.org/abs/2609.21049
- I. Kortchemski. *A total variation threshold for the first coordinates of uniform parking functions via Lorentzian polynomials*. arXiv:2610.40082v1 (October 29, 2026). https://arxiv.org/html/2610.40082v1
- J. Lee and J. Seo. *Antiferromagnetic models are clique-minimizing*. arXiv:2608.17920v1 (August 18, 2026), Section 3. https://arxiv.org/html/2608.17920v1
- P. Diaconis and A. Hicks. *Probabilizing parking functions*. Advances in Applied Mathematics 89 (2017), 125–155. https://doi.org/10.1016/j.aam.2017.05.004
- E. Bellin. *Asymptotic behaviour of the first positions of uniform parking functions*. Journal of Applied Probability 60 (2023), 1201–1218; arXiv:2108.08661. https://arxiv.org/abs/2108.08661
- P. Brändén and J. Huh. *Lorentzian polynomials*. Annals of Mathematics 192 (2020), 821–891.
