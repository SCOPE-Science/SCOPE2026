# Zero contacts suppress quadratic energy in symmetric random-walk bridges

## Finding
Let \((S_t)_{t=0}^{2n}\) be uniformly sampled from all nearest-neighbor paths with \(S_0=S_{2n}=0\) and steps in \(\{-1,+1\}\), where \(n\ge2\). Define the interior zero-contact count and integrated discrete quadratic energy by
\[
R_n=\sum_{k=1}^{n-1}\mathbf1_{\{S_{2k}=0\}},\qquad
Q_n=\sum_{t=1}^{2n-1}S_t^2.
\]
Put \(b_n=4^n/\binom{2n}{n}\). Their exact finite-sample moments are
\[
\begin{aligned}
\mathbb ER_n&=b_n-2,
&\operatorname{Var}(R_n)&=4n+2-b_n-b_n^2,\\
\mathbb EQ_n&=\frac{n(2n+1)}3,
&\operatorname{Var}(Q_n)&=\frac{8n^2(n-1)(2n+1)}{45},\\
\operatorname{Cov}(R_n,Q_n)&=-\frac{n(n-1)}6\,b_n& &<0.
\end{aligned}
\]
In particular, the correlation has a nonzero universal limit:
\[
\lim_{n\to\infty}\operatorname{Corr}(R_n,Q_n)
=-\frac{\sqrt{5\pi}}{8\sqrt{4-\pi}}\approx-0.5347160729.
\]
More generally, prescribe any \(q\ge1\) distinct interior zero contacts \(S_{2k_1}=\cdots=S_{2k_q}=0\), where \(1\le k_1<\cdots<k_q\le n-1\). Write the positive semilengths of the resulting \(q+1\) segments as \(\ell_0=k_1\), \(\ell_j=k_{j+1}-k_j\), and \(\ell_q=n-k_q\). Conditioning on these contacts **without forbidding additional zero contacts**, one has the exact pinning-deficit identity
\[
\mathbb E[Q_n\mid S_{2k_1}=\cdots=S_{2k_q}=0]
=\frac13\sum_{j=0}^{q}\ell_j(2\ell_j+1)
=\mathbb EQ_n-\frac43\sum_{0\le i<j\le q}\ell_i\ell_j.
\]
The reduction is strictly positive whenever at least one interior contact is prescribed.

## Assumptions and scope
Each bridge is sampled uniformly from the \(\binom{2n}{n}\) step sequences containing exactly \(n\) upward and \(n\) downward steps. The statistic \(R_n\) counts zeros only at even times strictly between the endpoints; parity rules out zero at odd times. The energy \(Q_n\) sums squared unscaled positions at every interior integer time. It is neither the sum of absolute positions nor the square of the time-integrated position. The strict covariance inequality and correlation limit are asserted for every integer \(n\ge2\). The pinning identity holds for any nonempty set of eligible contact times, not for conditioning on **exactly** \(q\) returns.

## Proof
**1. Bridge energy and the pinning law.** Write \(N=2n\) and let \(\xi_1,\ldots,\xi_N\) be the exchangeable, balanced signs of the bridge. For each \(1\le t<N\), \(S_t=\sum_{j\le t}\xi_j\). Sampling without replacement gives
\[
\mathbb E S_t=0,\qquad \mathbb E S_t^2=\frac{t(N-t)}{N-1}.
\]
Consequently
\[
\mathbb E Q_n=\frac1{N-1}\sum_{t=1}^{N-1}t(N-t)
=\frac{N(N+1)}6=\frac{n(2n+1)}3.
\]
When zeros are prescribed, every intervening segment is, conditionally, an independent uniform bridge with the prescribed length. Its expected energy is \(\ell(2\ell+1)/3\); squared values at the segment endpoints are zero. Summing the segment expectations gives the first formula in the pinning identity, and \(n^2-\sum_j\ell_j^2=2\sum_{i<j}\ell_i\ell_j\) gives the second.

**2. Exact mixed covariance.** Let \(c_k=\binom{2k}{k}\). Cutting a bridge at its contact at \(2k\) shows
\[
 p_{n,k}:=\Pr(S_{2k}=0\mid S_{2n}=0)
 =\frac{c_k c_{n-k}}{c_n}.
\]
By the single-contact case of the pinning identity,
\[
 \mathbb E[Q_n\mid S_{2k}=0]-\mathbb E Q_n=-\frac43k(n-k).
\]
Since \(R_n\) is a sum of contact indicators,
\[
\operatorname{Cov}(R_n,Q_n)
=-\frac4{3c_n}\sum_{k=1}^{n-1}k(n-k)c_kc_{n-k}.
\]
Now \(B(z)=\sum_{k\ge0}c_kz^k=(1-4z)^{-1/2}\), and therefore
\[
\sum_{k=1}^{n-1}k(n-k)c_kc_{n-k}
=[z^n](zB'(z))^2
=4[z^{n-2}](1-4z)^{-3}
=\frac{n(n-1)}2\,4^{n-1}.
\]
Substitution proves the exact negative covariance for all \(n\ge2\).

**3. Moments of the contact count.** The return-point counting identities are
\[
\mathbb ER_n=\frac{[z^n]B(z)^2}{c_n}-2
=\frac{4^n}{c_n}-2=b_n-2
\]
and
\[
\mathbb E[R_n(R_n-1)]
=\frac{2[z^n](B(z)-1)^3}{c_n}
=4n+8-6b_n.
\]
For the second identity, the ordered pair of distinct interior returns determines three positive-length bridge segments. It follows that
\[
\operatorname{Var}(R_n)=\mathbb E[R_n(R_n-1)]+\mathbb ER_n-(\mathbb ER_n)^2
=4n+2-b_n-b_n^2.
\]

**4. Exact quadratic-energy variance.** Write \(w_{ij}=N-j\) for \(1\le i<j\le N\). Expanding each squared partial sum gives
\[
Q_n=\frac{N(N-1)}2+2\sum_{i<j}w_{ij}\xi_i\xi_j.
\]
For distinct indices, balance and exchangeability yield
\[
m_2=\mathbb E(\xi_i\xi_j)=-\frac1{N-1},\qquad
m_4=\mathbb E(\xi_i\xi_j\xi_k\xi_l)
=\frac3{(N-1)(N-3)}.
\]
The latter also follows by comparing the coefficient of \(z^4\) in \((1+z)^n(1-z)^n=(1-z^2)^n\) with \(\binom N4\).
Put \(W=\sum_{i<j}w_{ij}\), \(U=\sum_{i<j}w_{ij}^2\), and \(V=\sum_{e<f:\,e\cap f\ne\varnothing}w_ew_f\), with edges \(e,f\) being unordered pairs of positions. Elementary power sums give
\[
\begin{aligned}
W&=\frac{N(N-1)(N-2)}6,\\
U&=\frac{N(N-2)(N-1)^2}{12},\\
V&=\frac{N(N-3)(N-2)(N-1)(8N-7)}{120}.
\end{aligned}
\]
Pair products sharing one position have expectation \(m_2\); disjoint pairs have expectation \(m_4\). Partitioning the double sum into equal, incident, and disjoint pairs yields
\[
\operatorname{Var}(Q_n)=4\bigl[U(1-m_4)+2V(m_2-m_4)+W^2(m_4-m_2^2)\bigr]
=\frac{N^2(N-2)(N+1)}{45},
\]
which equals \(8n^2(n-1)(2n+1)/45\).

**5. Correlation limit.** By Stirling's formula,
\[
b_n=\frac{4^n}{\binom{2n}{n}}\sim\sqrt{\pi n}.
\]
Therefore \(\operatorname{Var}(R_n)\sim(4-\pi)n\), \(\operatorname{Var}(Q_n)\sim16n^4/45\), and \(\operatorname{Cov}(R_n,Q_n)\sim-\sqrt\pi\,n^{5/2}/6\). Division by the standard deviations gives the stated finite negative limit.

## Verification
Run `python3 verify_bridge_energy.py` with Python 3 and no third-party packages. The verifier enumerates all \(66{,}194\) bridges for \(2\le n\le9\) and compares the exact first moments, variances, covariance, and energies conditioned on each one or two prescribed contacts against independently accumulated rational moments. It also checks the central-binomial convolution for \(2\le n\le100\) and the polynomial pair-weight identities through even \(N=60\). The verifier completed with 346 exact-arithmetic assertions. None of the finite checks substitutes for the displayed all-size proof.

## Relationship to prior work
Pitman's study of Brownian-bridge local times (1998 technical report, 1999 publication) gives the Rayleigh marginal law of Brownian-bridge local time, a continuous analogue of the contact count; the present statement concerns an exact **discrete joint covariance** with squared-position energy and its finite-size variances. Csáki and Hu (2003) treat ranked excursion lengths and heights of simple symmetric walks, including bridges; their inspected exact-distribution and limit results do not state the joint squared-energy/contact moment. Knight (2000) studies moments of the **absolute-value area** of a reflected Brownian bridge conditional on local time, a close but different continuous functional. Only its abstract and introductory preview could be inspected, so possible deeper implications are an explicit priority risk. Exact statement-to-statement comparisons with existing findings about bridge peaks/returns and fixed-composition run/energy statistics identify different local observables; one does not immediately imply the present joint moment.

## Limitations
The theorem is for uniformly balanced nearest-neighbor bridges and unweighted quadratic energy. It does not assert stochastic ordering of the full conditional law, a formula for conditioning on **exactly** a prescribed number of returns, higher joint moments, or a multivariate invariance principle. The asymptotic correlation follows from explicit discrete moments alone. A qualified historical-priority risk persists for literature on joint Brownian bridge local time and quadratic additive functionals, particularly inaccessible full texts; this does not constitute a proof of uniqueness.

## References
1. J. Pitman, *The distribution of local times of a Brownian bridge*, University of California, Berkeley Technical Report 539 (November 3, 1998); *Séminaire de Probabilités* XXXIII (1999), 388–394. https://live-statistics.pantheon.berkeley.edu/sites/default/files/tech-reports/539.pdf
2. E. Csáki and Y. Hu, *Lengths and heights of random walk excursions*, *Discrete Mathematics and Theoretical Computer Science*, Proceedings AC (2003), 45–52, DOI: 10.46298/dmtcs.3337. https://dmtcs.episciences.org/en/articles/3337/download
3. F. B. Knight, *The moments of the area under reflected Brownian bridge conditional on its local time at zero*, *Journal of Applied Mathematics and Stochastic Analysis* 13 (2000), 99–124, DOI: 10.1155/S1048953300000137. Full document not inspected; abstract and accessible introduction preview considered.
