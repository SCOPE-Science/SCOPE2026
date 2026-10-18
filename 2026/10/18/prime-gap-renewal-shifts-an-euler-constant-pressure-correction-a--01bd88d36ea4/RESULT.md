# Prime-gap renewal shifts: an Euler-constant pressure correction and a Poisson rare-marker limit

## Finding

Let \(\mathbb P\) be the positive prime integers. In the compact two-sided binary shift \(X_{\mathbb P}\), every pair of consecutive symbols \(1\) has exactly \(p\in\mathbb P\) intervening zeros. The all-zero configuration is included. Let \(\sigma\) be the shift and let \(\phi_t(x)=-t\mathbf1_{\{x_0=1\}}\), \(t\ge0\). All entropy and logarithm conventions here use natural units.

The pressure \(s=P(t)\) is the unique positive solution of
\[
e^{-t}\sum_{p\in\mathbb P} e^{-s(p+1)}=1.
\]
There is exactly one equilibrium state \(\mu_t\), a stationary renewal law whose successive prime gap labels are iid with \(q_t(p)=e^{-t-s(p+1)}\). Let \(\gamma=0.57721566\ldots\) be Euler's constant and \(L=\log(1/s)\). As \(t\to\infty\),
\[
P(t)=\frac{e^{-t}}{t+\log t-\gamma+o(1)},\qquad
\rho(t):=\mu_t[x_0=1]=P(t)\bigl(1+L^{-1}+O(L^{-2})\bigr).
\]
For any admissible prescribed marker density \(\rho>0\), write \(h_{\max}(\rho)=\sup\{h_\nu(\sigma):\nu\text{ invariant},\nu[x_0=1]=\rho\}\). As \(\rho\downarrow0\),
\[
h_{\max}(\rho)=\rho\left[\log(1/\rho)-\log\log(1/\rho)+1+o(1)\right].
\]
This gives an explicit \(\rho\log\log(1/\rho)\) entropy loss relative to binary sequences with unrestricted gap lengths at the same sparse marker density.

For the Palm gap length \(G_t=p+1\), sampled between consecutive markers, set \(s=P(t)\). For every fixed \(x>0\),
\[
\begin{split}
\Pr(sG_t\le x)={}&1-e^{-x}\\
&-\frac{\int_0^x e^{-u}\log u\,du+\gamma(1-e^{-x})}{L}
+O_x(L^{-2}).
\end{split}
\]
Thus \(sG_t\) converges to \(\mathrm{Exp}(1)\). Under the stationary equilibrium, the locally finite random counting measure \(N_t=\sum_{j:x_j=1}\delta_{s j}\) converges in distribution, in the vague topology, to the stationary Poisson point process on \(\mathbb R\) with rate one.

## Assumptions and scope

The word `prime' refers to the **permitted number of zeros between consecutive markers**, not gaps between consecutive prime numbers. The potential penalizes markers, \(t\ge0\). Every stated equilibrium uniqueness assertion concerns two-sided shift-invariant Borel probability measures. Statements involving \(t\to\infty\) fix the prime-gap shift while varying only the potential parameter. The constant in \(O_x(L^{-2})\) may depend on fixed \(x>0\); no error is asserted uniformly for \(x\to\infty\). For \(h_{\max}\), sufficiently small positive \(\rho\) is realized by a unique parameter \(t\ge0\). Weak convergence of counting measures concerns bounded continuous compactly supported test functions; no quantitative Poisson approximation rate is claimed.

## Proof

**1. Renewal variational principle and uniqueness.** Put \(\ell_p=p+1\). For \(s>0\), \(F(s)=\sum_{p\in\mathbb P}e^{-s\ell_p}\) is continuous and strictly decreasing from \(+\infty\) to zero. Therefore \(F(s)=e^t\) has a unique root \(s>0\), and \(q_t(p)=e^{-t-s\ell_p}\) is a probability mass function with finite mean \(m_t=\sum q_t(p)\ell_p\).

For an ergodic invariant measure \(\nu\) having positive marker frequency \(\rho\), induce the shift on the marker cross-section \(\{x_0=1\}\). Its return time is \(\ell_p\) with marginal \(r(p)\), satisfying \(\rho=(\sum r(p)\ell_p)^{-1}\) by Kac's formula. Abramov's entropy formula and the bound of process entropy by marginal entropy give \(h_\nu(\sigma)\le\rho H(r)\). Gibbs' inequality for \(q_t\) yields
\[
D(r\Vert q_t)=-H(r)+t+s\sum_p r(p)\ell_p\ge0.
\]
Consequently \(h_\nu(\sigma)-t\rho\le s\), with equality only when the induced gaps are independent and have marginal \(q_t\). The stationary renewal extension of iid \(q_t\)-gaps realizes equality. An invariant measure with zero marker frequency is concentrated on the all-zero configuration and has pressure contribution zero, strictly below \(s\). Ergodic decomposition extends the upper bound and uniqueness to all invariant probability measures. Thus \(P(t)=s\), and the equilibrium is unique.

**2. Prime Laplace expansion.** The classical effective prime number theorem \(\pi(y)=\operatorname{Li}(y)+O(ye^{-c\sqrt{\log y}})\), for sufficiently large \(y\), implies through partial summation and a split at polynomial powers of \(1/s\) that, for \(s\downarrow0\),
\[
\sum_{p\in\mathbb P}e^{-sp}
=\frac1s\left(\frac1L+\frac\gamma{L^2}+O(L^{-3})\right),\qquad L=\log(1/s).
\]
For clarity, the main integral after substituting \(u=sy\) is \(s^{-1}\int_{2s}^\infty e^{-u}(L+\log u)^{-1}\,du\), **not** an integral starting at zero (where that unexpanded integrand would have a singularity). Split at \(u=e^{-L/2}\) and \(u=e^{L/4}\). On the middle interval, expand \((L+\log u)^{-1}\) in inverse powers of \(L\); the lower and upper intervals contribute less than every term retained. The expansion coefficients are computed by the integrable logarithmic moments of \(e^{-u}\), in particular \(\int_0^\infty e^{-u}\log u\,du=-\gamma\). Error from the effective prime number theorem is smaller than every inverse power of \(L\) after rescaling. The same procedure permits differentiation and a fixed upper integration endpoint \(x\):
\[
\sum_{\substack{p\in\mathbb P\\sp\le x}}e^{-sp}
=\frac1s\left(\frac{1-e^{-x}}L-
\frac{\int_0^x e^{-u}\log u\,du}{L^2}+O_x(L^{-3})\right).
\]
The formal integration through \(u=0\) is legitimate after a cutoff; \(\int_0^x|\log u|\,du\) is finite and the discarded cutoff is superpolynomially small in \(1/L\).

**3. Pressure and marker density.** The normalization and the factor \(e^{-s}\) give
\[
e^t=F(s)=\frac1{sL}\left(1+\frac\gamma L+O(L^{-2})\right).
\]
Taking logarithms yields \(t=L-\log L+\gamma/L+O(L^{-2})\), hence \(L=t+\log t+o(1)\), while direct inversion gives \(e^{-t}/s=L-\gamma+O(1/L)\). Combining these expressions proves the pressure asymptotic, including the constant \(-\gamma\).

Implicit differentiation of \(e^{-t}F(P(t))=1\) gives \(-P'(t)=m_t^{-1}=\rho(t)\). Differentiating the prime Laplace expansion, or applying its first-moment analogue, gives \(m_t=s^{-1}(1-L^{-1}+O(L^{-2}))\), proving \(\rho(t)=s(1+L^{-1}+O(L^{-2}))\). Strict decrease of \(\rho(t)\) follows from \(\rho'(t)=-\rho(t)^3\operatorname{Var}_{q_t}(\ell_p)<0\), since \(q_t\) supports infinitely many distinct gaps.

**4. Constrained-entropy asymptotic.** For \(\rho=\rho(t)\), the equilibrium variational equality gives \(h_{\max}(\rho)=P(t)+t\rho\); a positive-density invariant measure with the same \(\rho\) cannot have higher entropy. Also \(\rho=s(1+O(L^{-1}))\), so \(L=\log(1/\rho)+O(L^{-1})\) and \(P(t)/\rho=1+O(L^{-1})\). Therefore
\[
\frac{h_{\max}(\rho)}\rho=t+\frac s\rho
=L-\log L+1+o(1),
\]
which is the claimed entropy law. For unrestricted binary sequences the sharp entropy at marker density \(\rho\) equals \(-\rho\log\rho-(1-\rho)\log(1-\rho)\), so the displayed deficit has the stated order.

**5. Refined gap law and Poisson limit.** Divide the fixed-upper-endpoint Laplace expansion in Step 2 by the complete prime sum. Replacing \(p\) by the return time \(p+1\) shifts the threshold and exponential weights by \(O(s)\), negligible compared with \(L^{-2}\). The result is
\[
\Pr(sG_t\le x)=1-e^{-x}-\frac{J(x)+\gamma(1-e^{-x})}{L}+O_x(L^{-2}),\quad
J(x)=\int_0^x e^{-u}\log u\,du.
\]
This proves convergence of the Palm return time to an exponential random variable. Its mean satisfies \(s\mathbb E G_t=s/\rho(t)\to1\); its second moment also converges by the exponentially decaying prime Laplace tails. To obtain the stationary point process, select the interval containing the origin with length-biased law \(\ell_pq_t(p)/m_t\), and place the origin uniformly among its \(\ell_p\) lattice positions. The joint scaled age and residual life therefore converge to the stationary size-biased exponential interval split uniformly at the origin, whose density is \(e^{-(a+r)}\) on \((a,r)\in(0,\infty)^2\). The ages to either side are independent rate-one exponentials. All other scaled return times are independent and converge jointly to rate-one exponentials. Finite-window tightness follows from \(\mathbb E N_t(I)\le |I|\rho(t)/s+O(1)\) for fixed bounded \(I\) (or directly from the stationary renewal construction). The limiting process therefore has independent exponential spacings both ways and is the stationary rate-one Poisson point process.

## Verification

The accompanying standalone `verify.py` enumerates primes to a fixed finite cutoff, solves the renewal pressure equation numerically at three specified penalties, checks normalization and the explicit Euler-constant pressure denominator, compares corrected Palm CDFs at nine finite choices of \((t,x)\), checks the leading renewal-mean relation, and independently enumerates finite prime-gap marker words against their composition recursion. It prints a `VERIFY_OK` status when every asserted finite test passes. Numerical comparisons are finite-range corroboration only: none of them establishes the prime number theorem, the infinite asymptotic, uniqueness of the equilibrium, or the Poisson convergence. Those statements follow from the mathematical arguments above.

## Relationship to prior work

Baker and Ghenciu (2014, arXiv:1411.7167) develop the \(S\)-gap symbolic framework and describe the classical entropy-root formula. The basic renewal partition identity and general thermodynamic methods are not claimed as novel. Ramirez and Somers (2025, arXiv:2501.08438) explicitly discuss non-syndetic sets including primes and give the unweighted entropy formula in a generalized \((S,w)\)-gap setting; they do not derive a low-marker asymptotic pressure, the Euler-constant correction, the sparse-density entropy envelope, or a Palm-to-Poisson limit. The arXiv:2010.14686 study establishes pressure computability for arbitrary continuous potentials on \(S\)-gap shifts, not these asymptotic evaluations. Classical effective prime number theory supplies the arithmetic input and is a known theorem, not a contribution here. Separately, published mathematical findings on geometric \(S\)-gap shifts establish different log-periodic behavior for exponentially sparse allowable gaps, and on square-gap shifts establish a theta-function low-activity expansion. Those are not implications for the prime-gap arithmetic scale because \(\#\{p\le y\}\sim y/\log y\), unlike their allowed-return counting laws.

The asserted contribution is the *combined, specifically prime-gap, quantitatively evaluated thermodynamic and renewal limit*: an explicit constant correction \(-\gamma\), a sharp \(\rho\log\log(1/\rho)\) entropy penalty, and the first logarithmic Palm-return correction leading to the Poisson scaling limit. A broad general renewal theorem combined with prime number theory could subsume portions of these results; no claim of absolute historical priority is made.

## Limitations

No claims are made for gap sets other than prime numbers, for arbitrary nonlocal potentials, for finite-\(t\) Poisson behavior, or for a convergence rate of stationary point processes. The first correction to the CDF is stated for fixed \(x>0\) only. The root identity, uniqueness and renewals are elementary consequences of standard inducing technology; they are included to precisely fix normalization and explain the new arithmetic asymptotics. Historical priority remains contingent on literature beyond accessible indexed sources; the available comparisons do not prove uniqueness of the finding.

## References

- S. Baker and A. E. Ghenciu, *Dynamical properties of S-gap shifts and other shift spaces*, arXiv:1411.7167, initially public November 26, 2014, https://arxiv.org/abs/1411.7167.
- C. Ramirez and A. Somers, *(S,w)-Gap Shifts and Their Entropy*, arXiv:2501.08438, https://arxiv.org/abs/2501.08438.
- *Computability of topological pressure on compact shift spaces beyond finite type*, arXiv:2010.14686, https://arxiv.org/abs/2010.14686.
- Classical prime number theorem with de la Vallée Poussin exponential error term, and the classical renewal/Abramov/Kac/relative-entropy formulas (standard results).
