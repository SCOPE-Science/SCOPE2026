# A lattice Poisson law for the height of bridges with linearly many returns

## Finding
Let \(S_0=0,S_1,\ldots,S_{2n}\) be a simple symmetric random walk conditioned on \(S_{2n}=0\). Define
\[
K_n=\#\{j:1\le j\le n,\ S_{2j}=0\},\qquad M_n=\max_{0\le j\le 2n}|S_j|.
\]
The \(K_n\) intervals between successive visits to zero are complete excursions. For an integer \(h\ge2\), let \(Z_{n,h}\) be the number of these excursions whose absolute height is at least \(h\).

**Poisson law at the return-conditioned height window.** For every sequence of integers \(k_n\in\{1,\ldots,n\}\) such that \(k_n/n\to\rho\in(0,1)\), and every sequence of integers \(h_n\to\infty\) such that
\[
k_n(1-k_n/n)^{h_n}\longrightarrow\tau\in[0,\infty),
\]
we have, conditional on \(K_n=k_n\),
\[
Z_{n,h_n}\ \xrightarrow{d}\ \operatorname{Poisson}\!\left(\frac{\rho\tau}{1-\rho}\right).
\]
In particular,
\[
\Pr(M_n<h_n\mid K_n=k_n)\longrightarrow
\exp\!\left(-\frac{\rho\tau}{1-\rho}\right).
\]
The integer constraint on \(h_n\) matters: the centered maximum has lattice oscillations, so an unrestricted continuous Gumbel limit is **not** claimed.

**Logarithmic height law.** For every such sequence \(k_n\),
\[
\frac{M_n}{\log n}\ \xrightarrow{\Pr(\cdot\mid K_n=k_n)}\ \frac{1}{-\log(1-\rho)}.
\]
The ordinary bridge has a square-root height scale, so conditioning on linearly many returns changes the scale to logarithmic.

**Exact finite-size statement.** Put \(C_0(z)=1\) and, for integers \(j\ge1\), define \(C_j(z)=1/(1-zC_{j-1}(z))\); also write \(C(z)=(1-\sqrt{1-4z})/(2z)\). For all integers \(n\ge1\), \(1\le k\le n\), and \(h\ge2\),
\[
\Pr(M_n<h\mid K_n=k)=
\frac{[z^{n-k}]\,C_{h-2}(z)^k}{[z^{n-k}]\,C(z)^k},
\qquad
[z^{n-k}]C(z)^k=\frac{k}{2n-k}\binom{2n-k}{n-k}.
\]
This identity includes boundary cases such as \(k=n\), when all excursions have height one.

## Assumptions and scope
All increments take values \(\pm1\) independently with probability \(1/2\). Conditioning first on the bridge and then on \(K_n=k\) gives the uniform distribution on bridges with exactly \(k\) nonempty excursions. Time is \(2n\), so an excursion of duration \(2\ell\) has semilength \(\ell\). The asymptotic statements require a *fixed interior* limit \(\rho\in(0,1)\). No uniformity is claimed when the return fraction approaches either endpoint.

## Proof
**1. Exact excursion decomposition.** A primitive signed excursion of semilength \(\ell\ge1\) is an up-excursion or its reflection, and has \(2\operatorname{Cat}_{\ell-1}\) realizations, where \(\operatorname{Cat}_j=\binom{2j}{j}/(j+1)\). Its semilength generating function is
\[
E(z)=2zC(z)=1-\sqrt{1-4z}.
\]
The generating function for primitive signed excursions whose absolute height is strictly below \(h\) is \(E_{<h}(z)=2zC_{h-2}(z)\): after the first upward step, the interior Dyck path must remain at height at most \(h-2\). Concatenation of exactly \(k\) excursions gives \([z^n]E(z)^k\), and restricting every height gives \([z^n]E_{<h}(z)^k\). Cancelling the common factor \((2z)^k\) proves the exact finite-size formula. Marking an excursion of height at least \(h\) with \(s\) gives the exact probability-generating function
\[
\mathbb E[s^{Z_{n,h}}\mid K_n=k]=
\frac{[z^n]\{E_{<h}(z)+s(E(z)-E_{<h}(z))\}^{k}}{[z^n]E(z)^k}
\quad (0\le s\le1).
\]

**2. An exact geometric height tail under exponential tilting.** Fix \(z\in(0,1/4)\) and put \(q=\sqrt{1-4z}\), \(\lambda=(1-q)/(1+q)\). The fractional-linear recurrence \(C_j=(1-zC_{j-1})^{-1}\) has fixed points \(2/(1+q)\) and \(2/(1-q)\). Tracking their cross-ratio from \(C_0=1\) gives, for every \(h\ge2\),
\[
E(z)-E_{<h}(z)=\frac{2q\lambda^h}{1-\lambda^h}.
\]
Under the probability measure on individual signed excursions that assigns weight \(z^\ell/E(z)\) to each excursion of semilength \(\ell\), the height \(H\) therefore has the *exact* tail
\[
\Pr_z(H\ge h)=\frac{2q}{1-q}\frac{\lambda^h}{1-\lambda^h}.
\]

**3. Select the tilt matching the observed number of returns.** Write \(\rho_n=k_n/n\), and choose
\[
z_n=\frac{1-\rho_n}{(2-\rho_n)^2},\quad
q_n=\frac{\rho_n}{2-\rho_n},\quad
\lambda_n=1-\rho_n.
\]
For the individual semilength \(L\) under this tilt,
\[
\mathbb E_{z_n}L=\frac{z_n E'(z_n)}{E(z_n)}=\frac{n}{k_n},
\qquad
\operatorname{Var}_{z_n}(L)=\frac{(1-\rho_n)(2-\rho_n)}{\rho_n^3}.
\]
The exact height tail specializes to
\[
p_n:=\Pr_{z_n}(H\ge h_n)=
\frac{\rho_n}{1-\rho_n}\frac{\lambda_n^{h_n}}{1-\lambda_n^{h_n}}.
\]
Under the claimed window hypothesis, \(p_n=O(1/k_n)\), and \(k_np_n\to\rho\tau/(1-\rho)\).

**4. Conditioning on the total semilength does not disturb the extreme-value window.** Let \(F_{n,s}(z)=E_{<h_n}(z)+s(E(z)-E_{<h_n}(z))\), \(0\le s\le1\). By weighting excursion lengths by \(z_n^\ell/F_{n,s}(z_n)\), obtain independent integer-valued \(L^{(n,s)}_1,\ldots,L^{(n,s)}_{k_n}\). The coefficient identity, valid exactly for every \(n\), is
\[
\frac{[z^n]F_{n,s}(z)^{k_n}}{[z^n]E(z)^{k_n}}=
\left(\frac{F_{n,s}(z_n)}{E(z_n)}\right)^{k_n}
\frac{\Pr(\sum_iL_i^{(n,s)}=n)}{\Pr(\sum_iL_i^{(n,1)}=n)}.
\]
The fractional-linear formula from step 2, differentiated at \(z_n\), shows that the mean of \(L^{(n,s)}\) differs from \(n/k_n\) by \(O(h_n\lambda_n^{h_n})\), uniformly in \(s\in[0,1]\); the variance differs from the positive value in step 3 by \(O(h_n^2\lambda_n^{h_n})\). Since the window condition implies \(h_n\lambda_n^{h_n}=O((\log n)/n)\), the sum's mean differs from \(n\) by \(O(\log n)=o(\sqrt n)\). (If \(h_n\) exceeds a constant multiple of \(\log n\), exponential decay makes the same bound stronger.) All tilted length laws have exponential moments uniformly in \(n\) and \(s\), since \(z_n\) remains in a compact subinterval of \((0,1/4)\). For all large \(n\), their probabilities at lengths one and two are uniformly positive, ensuring aperiodicity. Fourier inversion with a third-order characteristic-function expansion near zero and uniform strict contraction away from zero thus gives the triangular-array lattice local central limit theorem
\[
\Pr(\sum_iL_i^{(n,s)}=n)=
\frac{1+o(1)}{\sqrt{2\pi k_n\sigma_\rho^2}},\quad
\sigma_\rho^2=\frac{(1-\rho)(2-\rho)}{\rho^3},
\]
uniformly in \(s\in[0,1]\). Consequently the final probability ratio in the coefficient identity tends to one.

**5. The limiting laws.** At \(z_n\), \(F_{n,s}/E=1-(1-s)p_n\). Therefore
\[
\mathbb E[s^{Z_{n,h_n}}\mid K_n=k_n]
=\{1-(1-s)p_n\}^{k_n}(1+o(1))
\longrightarrow
\exp\!\left(-\frac{\rho\tau}{1-\rho}(1-s)\right).
\]
This is the probability-generating function of the asserted Poisson law. Putting \(s=0\) gives the maximum-height probability. To obtain the logarithmic scale, take heights slightly above and below \(\log k_n/[-\log\lambda_n]\). The upper choice gives \(k_n\lambda_n^{h_n}\to0\). For the lower choice take a small fractional deficit \(\delta\in(0,1/2)\); then \(k_n\lambda_n^{h_n}=\Theta(k_n^\delta)\) and the tilted total-length mean shift is still \(O(k_n^\delta\log k_n)=o(\sqrt{k_n})\). The same local central limit estimate gives \(\Pr(M_n<h_n\mid K_n=k_n)\le\exp(-c k_n^\delta)(1+o(1))\to0\). Monotonicity in height yields the stated convergence in conditional probability.

## Verification
The accompanying standalone file `verify.py` reconstructs the restricted Dyck-series coefficients and enumerates all bridges of lengths up to 16. It checks the exact return-count and joint return/maximum-height formulas, and checks the rational tilted-tail identity without floating-point arithmetic. It passed 320 exact assertions. As a separate numerical illustration, the conditional probabilities for \((n,k,h)=(100,50,7),(200,100,8),(400,200,9)\) are approximately \(0.688015\), \(0.688796\), and \(0.686914\), while their lattice-window asymptotic approximations are each \(0.676634\). These finite comparisons are illustrations, not the proof of convergence.

## Relationship to prior work
Csáki and Hu, *Lengths and heights of random walk excursions* (published December 31, 2002, DOI below), derive distributions of ranked excursion lengths and heights in the unconditioned walk/bridge setting, and square-root-scale limits. The present statement is conditional on a *linear* number of returns, a different rare-event ensemble with logarithmic height and a conditional Poisson extreme law. Drube, *Raised \(k\)-Dyck paths* (2022), develops return-count and bounded-height enumeration frameworks; its inspected statements do not give the linear-return conditional maximum asymptotic. The classical exponential tilting and local-limit tools used here are not claimed as new. Priority remains subject to independent historical review, including possible general conditioned-composition theorems.

## Limitations
Only the interior linear-return regime is covered. Neither a continuous nonlattice Gumbel limit nor universality beyond simple symmetric steps is asserted. The exact enumerations are finite checks and do not replace the analytic proof. The historical literature comparison cannot establish uniqueness or external certification.

## References
1. Endre Csáki and Yueyun Hu, *Lengths and heights of random walk excursions*, Discrete Mathematics and Theoretical Computer Science, proceedings AC (2003), 45–52. Publisher first-publication record: December 31, 2002. DOI: 10.46298/dmtcs.3337. Full text: https://dmtcs.episciences.org/articles/3337/download .
2. Paul Drube, *Raised \(k\)-Dyck paths*, arXiv:2206.01194, first posted June 2, 2022. Full text: https://arxiv.org/abs/2206.01194 .
