# Three fluctuation regimes for uniform empirical averages on a geometric alphabet

## Finding

Fix \(0<\rho<1\), let \(p_j=(1-\rho)\rho^{j-1}\) for integers \(j\ge1\), and sample independent \(X_1,\ldots,X_n\) with \(\Pr(X_i=j)=p_j\). Let \(N_{n,j}=\#\{i\le n:X_i=j\}\). For fixed \(1<q<\infty\), put \(r=q/(q-1)\) and define the uniform empirical expectation error
\[
\Delta_{n,q}=\sup_{\sum_{j\ge1}p_j|f(j)|^q\le1}\left|\frac1n\sum_{i=1}^nf(X_i)-\sum_{j\ge1}p_jf(j)\right|.
\]
The supremum is over real functions, with the same value for complex functions. By weighted \(L^q\) duality,
\[
\Delta_{n,q}^r=\sum_{j\ge1}p_j\left|\frac{N_{n,j}}{np_j}-1\right|^r.
\tag{1}
\]
There are three different fluctuation regimes, all at fixed \(\rho\) and fixed \(q\).

**Gaussian sequence regime \(q>2\) (\(1<r<2\)).** Let \((G_j)_{j\ge1}\) be a centered jointly Gaussian sequence with
\[\operatorname{Cov}(G_i,G_j)=p_i\mathbf1_{\{i=j\}}-p_ip_j.\]
Then the Gaussian series is finite almost surely and
\[
\sqrt n\,\Delta_{n,q}\ \Longrightarrow\
\left(\sum_{j\ge1}p_j^{1-r}|G_j|^r\right)^{1/r}.
\tag{2}
\]

**Critical regime \(q=2\) (\(r=2\)).** The discrepancy has a logarithmic enhancement with an exact coefficient:
\[
\frac{n\Delta_{n,2}^{2}}{\log n}\ \xrightarrow{\Pr}\ \frac1{|\log\rho|}.
\tag{3}
\]
In particular \(\sqrt{n/\log n}\,\Delta_{n,2}\xrightarrow{\Pr}|\log\rho|^{-1/2}\).

**Rare-coordinate regime \(1<q<2\) (\(r>2\)).** Put
\[
K_n=1+\left\lfloor\log_{1/\rho}(n(1-\rho))\right\rfloor,
\qquad\tau_n=np_{K_n}\in[1,\rho^{-1}).
\]
Along any subsequence for which \(\tau_n\to\tau\in[1,\rho^{-1}]\), take independent \(P_k\sim\operatorname{Pois}(\tau\rho^k)\), \(k\in\mathbb Z\). Then
\[
n^{1/r}\Delta_{n,q}\ \Longrightarrow\
\left(\sum_{k\in\mathbb Z}
\frac{|P_k-\tau\rho^k|^r}{(\tau\rho^k)^{r-1}}\right)^{1/r}.
\tag{4}
\]
The series on the right is finite almost surely, is nonconstant, and has infinite \(r\)-th moment. Its distribution is unchanged by replacing \(\tau\) by \(\tau/\rho\), since this only reindexes \(k\). The theorem does not assert that different interior phases must give different laws.

For every \(n\ge1\), the random variable \(\Delta_{n,q}\) is almost surely finite. Nevertheless,
\[\mathbb E\Delta_{n,q}^r=\infty\qquad\text{whenever }1<q\le2.\tag{5}\]
Thus the critical and rare-coordinate conclusions are convergence statements, not convergence of the corresponding \(r\)-th moments.

## Assumptions and scope

The alphabet is countably infinite, with exactly geometric masses \(p_j=(1-\rho)\rho^{j-1}\). The observations are independent and identically distributed. There are no auxiliary observations, Poissonization assumptions, truncation of the empirical measure, or asymptotics in \(q\) or \(\rho\). Statement (4) concerns every convergent subsequence of the log-lattice phase \(\tau_n\), including the identified equivalent endpoints. Formula (1) is the exact operator norm of the difference between empirical and true expectation as functionals on weighted \(L^q\).

## Proof

**Duality and finiteness.** Define the density \(h_n(j)=N_{n,j}/(np_j)-1\). Hölder duality between \(L^q(p)\) and \(L^r(p)\) gives (1). On any sample, at most \(n\) coordinates are observed. Their \(p_j\)'s are positive, while on the unobserved coordinates \(h_n=-1\). Consequently \(h_n\in L^r(p)\) and the supremum is finite. The exact alternative identity
\[
n\Delta_{n,q}^r=\sum_{j\ge1}\frac{|N_{n,j}-np_j|^r}{(np_j)^{r-1}}
\tag{6}
\]
is particularly useful for \(r\ge2\).

**Gaussian sequence regime.** For any fixed integer \(J\), the multinomial central limit theorem gives
\[\big((N_{n,j}-np_j)/\sqrt n\big)_{1\le j\le J}
\Longrightarrow(G_j)_{1\le j\le J}.\]
For \(1<r<2\), concavity of the \(r/2\)-power and the binomial variance estimate imply
\[
\mathbb E|N_{n,j}-np_j|^r\le(np_j)^{r/2}.
\]
The expected \(r\)-th power of the \(\sqrt n\)-scaled discrepancy from coordinates \(j>J\) is therefore at most
\[
\sum_{j>J}p_j^{1-r/2}\longrightarrow0.
\]
The same bound for the limiting Gaussian coordinates follows from their individual variances \(p_j(1-p_j)\). This proves absolute convergence of the nonnegative limiting series and, by finite-dimensional convergence followed by truncation, (2).

**Critical regime.** For this paragraph put \(\mu_j=np_j\), \(K=K_n\), \(L=\lfloor\sqrt K\rfloor\), and \(J=K-L\). Since \(K\sim(\log n)/|\log\rho|\), we have \(L\to\infty\), \(L/K\to0\), and \(\mu_J\ge \rho^{-L}\) up to a fixed multiplicative constant. Define
\[
Q_J=\sum_{j\le J}\frac{(N_{n,j}-\mu_j)^2}{\mu_j}.
\]
Every summand has exact mean \(1-p_j\), so \(\mathbb E Q_J=J-\sum_{j\le J}p_j=J+O(1)\).
To bound the variance without falsely assuming independent multinomial counts, let
\[
f_J(x,y)=\sum_{j\le J}
\frac{(\mathbf1_{\{x=j\}}-p_j)(\mathbf1_{\{y=j\}}-p_j)}{p_j}.
\]
Then \(Q_J=n^{-1}\sum_{a,b=1}^n f_J(X_a,X_b)\). For independent \(X,Y\),
\[\mathbb E[f_J(X,Y)\mid X]=0,\qquad
\mathbb E f_J(X,Y)^2\le J+1.\]
The off-diagonal unordered terms are thus pairwise uncorrelated except when identical, contributing \(O(J)\) to \(\operatorname{Var}Q_J\). The diagonal terms are independent; directly expanding \(f_J(X,X)\) gives
\[
\operatorname{Var}\left(n^{-1}\sum_{a=1}^nf_J(X_a,X_a)\right)
\le\frac{C}{n}\left(1+\sum_{j\le J}p_j^{-1}\right)
=O(1+\rho^L).
\]
Furthermore, diagonal and off-diagonal parts are uncorrelated by degeneracy. Hence \(\operatorname{Var}Q_J=O(J)\), and \(Q_J/K\to1\) in probability.
The neighboring band \(J<j\le K+L\) has at most \(2L\) terms, each with mean at most one; Markov's inequality shows its sum divided by \(K\) tends to zero in probability. For the far tail \(j>K+L\), a union bound gives
\[\Pr(\exists i:X_i>K+L)\le n\sum_{j>K+L}p_j=O(\rho^L).\]
On the complement every tail count is zero, so its contribution to \(n\Delta_{n,2}^2\) is \(\sum_{j>K+L}\mu_j=O(\rho^L)\). Combining core, band, and tail proves (3).

**Rare-coordinate regime.** For every fixed integer \(k\), the expected count at coordinate \(K_n+k\) is exactly
\[\mu_{K_n+k}=np_{K_n+k}=\tau_n\rho^k.\]
Under \(\tau_n\to\tau\), the multinomial law of any finite number of these counts converges to independent Poisson variables of respective means \(\tau\rho^k\), because their cell probabilities are \(O(1/n)\). Equation (6) therefore converges for every finite window \(|k|\le M\).

It remains to control both infinite tails uniformly. For fixed \(r>2\), a standard centered binomial moment inequality (obtainable by expansion of independent centered Bernoulli summands or Rosenthal's inequality) gives, with a constant depending only on \(r\),
\[\mathbb E|N_{n,j}-\mu_j|^r
\le C_r(\mu_j^{r/2}+\mu_j).\]
Consequently the mean contribution to (6) from \(j<K_n-M\), where \(\mu_j\ge c\rho^{-M}\), is bounded by
\[
C_r\sum_{j<K_n-M}(\mu_j^{1-r/2}+\mu_j^{2-r})
\le C_{r,\rho}\big(\rho^{M(r/2-1)}+\rho^{M(r-2)}\big).
\]
For \(j>K_n+M\), the probability any observation occupies that tail is at most
\[n\sum_{j>K_n+M}p_j\le C_\rho\rho^M.\]
When no observation does, the contribution to (6) equals \(\sum_{j>K_n+M}\mu_j\le C_\rho\rho^M\). These bounds vanish as \(M\to\infty\), and analogous bounds hold for independent Poisson coordinates. Window convergence plus these tail estimates gives (4). The same bounds yield almost-sure finiteness of the Poisson series. At any coordinate its summand changes with the Poisson count, proving a nondegenerate distribution by independence. For \(k\to+\infty\), write \(\mu=\tau\rho^k\to0\); then
\[
\mathbb E\frac{|\operatorname{Pois}(\mu)-\mu|^r}{\mu^{r-1}}
\ge\Pr(\operatorname{Pois}(\mu)=1)\frac{(1-\mu)^r}{\mu^{r-1}}
\sim\mu^{2-r}\to\infty.
\]
Thus the limiting nonnegative series has infinite mean and its \(r\)-th root has infinite \(r\)-th moment. Replacing \(\tau\) by \(\tau/\rho\) replaces \(\tau\rho^k\) by \(\tau\rho^{k-1}\), proving endpoint equivalence by reindexing.

**Infinite moments at finite sample size.** For \(r=2\), \(\mathbb E[(N_{n,j}-np_j)^2/(np_j)]=1-p_j\), so \(\mathbb E[n\Delta_{n,2}^2]=\sum_j(1-p_j)=\infty\) by Tonelli. For \(r>2\), as \(j\to\infty\), \(\Pr(N_{n,j}=1)\sim np_j=\mu_j\) at fixed \(n\), hence the expected single-coordinate summand of (6) is bounded below by a positive multiple of \(\mu_j^{2-r}\), which diverges. Tonelli again yields (5). This completes the proof.

## Verification

The companion standalone file `checker.py` verifies 1,478 exact-rational/finite assertions, including finite count-vector dual-norm identities and the exact binomial second-moment identity. Its fixed-seed simulations provide finite-sample illustrations at two sizes for the critical and rare-coordinate regimes. Recorded output is included as `checker-output.txt`. These checks are diagnostics, not proofs of the infinite limits. The analytical truncation and covariance arguments above establish (2)--(5).

## Relationship to prior work

Bartel and Morgan, first publicly available October 21, 2026, prove a qualitative simultaneous strong law on countable probability spaces: the full \(L^q(p)\) class has almost-sure simultaneous convergence exactly under a specified mass-summability criterion. Geometric probabilities satisfy their criterion for all \(q>1\). Their theorem does not give the fluctuation-scale empirical operator norm analyzed here. Garza and Wang derive functional central limit theorems for linear occupancy-count statistics in a polynomial-tail Karlin model, whereas the present statistic is a nonlinear dual-norm sum over geometric cells. Iksanov and Kotelnikova study iterated-logarithm laws for numbers of boxes with a fixed occupancy count, not the discrepancy of empirical and true expectations in \(L^q\). These are substantive differences of statements, not proofs of historical priority. Broad general empirical-process theorems remain a possible source of implicit coverage and should be assessed independently.

## Limitations

The theorem requires exactly geometric masses, an infinite alphabet, independent identically distributed observations, and a fixed exponent \(q\in(1,\infty)\). It does not provide quantitative convergence rates, almost-sure sharp constants, uniformity as \(q\to2\), or a classification of whether all interior log-lattice phases give distinct laws. For \(q\le2\) the stated normalizations concern convergence in probability or distribution despite infinite \(r\)-th moments at each finite sample size.

## References

1. A. Bartel and A. Morgan, *On the notion of reasonable functions in Cohen–Lenstra type heuristics*, arXiv:2610.29880v1 (first public October 21, 2026), https://arxiv.org/html/2610.29880v1 .
2. J. Garza and Y. Wang, *A functional central limit theorem for weighted occupancy processes of Karlin model*, arXiv:2412.02160v1 (first public December 3, 2024), https://arxiv.org/html/2412.02160v1 .
3. A. Iksanov and V. Kotelnikova, *A law of the iterated logarithm for small counts in Karlin’s occupancy scheme*, Modern Stochastics: Theory and Applications 11 (2024), 217–245, https://doi.org/10.15559/24-VMSTA248 .
