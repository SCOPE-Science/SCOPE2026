# Convex collision association and two-threshold frequency dependence in multinomial occupancy

## Finding

Let \(X_1,\ldots,X_n\) be independent draws from a strictly positive probability vector \((p_1,\ldots,p_m)\), with \(n,m\ge2\). Write \(N_i=\#\{a:X_a=i\}\), let \(T=\sum_i\binom{N_i}{2}\) be the number of colliding sample pairs, and put \(W_f=\sum_i f(N_i)\) for a real function \(f\) on \(\{0,\ldots,n\}\).

**Theorem (convex collision association).** If \(f\) is discretely convex (\(\Delta^2 f(k)\ge0\) for all \(0\le k\le n-2\)), then \(\operatorname{Cov}(T,W_f)\ge0\). Equality holds **exactly when** \(f\) is affine on \(\{0,\ldots,n\}\); every nonaffine convex score gives strict positivity. The statement is finite-sample and allows arbitrarily unequal category probabilities.

**Theorem (complete uniform frequency sign law).** In the uniform model \(p_i=1/m\), write \(F_r=\#\{i:N_i=r\}\), \(0\le r\le n\), and \(b_k(j)=\binom kj m^{-j}(1-m^{-1})^{k-j}\) for \(0\le j\le k\) and \(0\) otherwise. Then
\[
\operatorname{Cov}(T,F_r)=\binom n2\frac{m-1}{m^2}\bigl[b_{n-2}(r)-2b_{n-2}(r-1)+b_{n-2}(r-2)\bigr].
\]
At \(r=0\), covariance is positive. At \(r=1\) its exact sign is \(\operatorname{sgn}(n-2m)\) and it vanishes **if and only if** \(n=2m\). For every \(2\le r\le n\), covariance has the sign (including zero) of
\[
P_{n,m}(r)=m^2r^2-m(2n+m-2)r+n(n-1).
\]
Thus the frequency covariance is positive for \(r<r_-\) or \(r>r_+\), negative for \(r_-<r<r_+\), and zero at the roots whenever these are admissible integers at least two, where
\[
r_{\pm}=\frac{2n+m-2\pm\sqrt{(m-2)^2+4n(m-1)}}{2m}.
\]
These cases together give a complete exact sign classification for every feasible frequency count.

## Assumptions and scope

The alphabet is finite of size \(m\ge2\), all \(p_i>0\), \(\sum_i p_i=1\), and \(n\ge2\). A collision counts unordered pairs of equal observations, including all \(\binom{k}{2}\) pairs in an occupancy cell of size \(k\). The discrete differences are \(\Delta f(k)=f(k+1)-f(k)\) and \(\Delta^2 f(k)=f(k+2)-2f(k+1)+f(k)\). There is no claim of stochastic domination or nonnegative covariance for arbitrary nonconvex scores. Binomial probability terms outside their natural range are defined to be zero.

## Proof

Fix the first two observations, and write \(H=\mathbf1\{X_1=X_2\}\). Let \(B_i\) be the number of occurrences of letter \(i\) among the remaining \(n-2\) observations. For each \(i\), \(B_i\sim\operatorname{Bin}(n-2,p_i)\). Put \(G_i=\mathbb E[\Delta f(B_i)]\), \(J_i=\mathbb E[\Delta^2 f(B_i)]\), and \(s_2=\sum_i p_i^2\). Writing \(W_0=\sum_i f(B_i)\), inserting two letters in different cells \(i,j\) adds \(\Delta f(B_i)+\Delta f(B_j)\); inserting both in cell \(i\) adds \(2\Delta f(B_i)+\Delta^2 f(B_i)\). Independence of the two inserted draws from \(\boldsymbol B\) therefore gives the **exact identity for every real score**:
\[
\operatorname{Cov}(T,W_f)=\binom n2\left[(1-s_2)\sum_i p_i^2 J_i+2\sum_i p_i(p_i-s_2)G_i\right].\tag{1}
\]
Indeed exchangeability gives \(\operatorname{Cov}(T,W_f)=\binom n2\operatorname{Cov}(H,W_f)\); direct substitution of the two conditional additions yields (1). This derivation requires no independence among the \(B_i\).

If \(f\) is discretely convex, every \(J_i\ge0\). The function \(g(t)=\mathbb E[\Delta f(\operatorname{Bin}(n-2,t))]\) is nondecreasing in \(t\in[0,1]\), because a common-uniform-variable coupling orders the binomials and \(\Delta f\) is nondecreasing. Hence
\[
\sum_i p_i(p_i-s_2)G_i=\operatorname{Cov}_{I\sim p}(p_I,g(p_I))
=\frac12\sum_{i,j}p_ip_j(p_i-p_j)(g(p_i)-g(p_j))\ge0.
\]
Also \(1-s_2>0\). If \(f\) is not affine, at least one of \(\Delta^2 f(0),\ldots,\Delta^2 f(n-2)\) is positive. Since all \(0<p_i<1\), every binomial \(B_i\) assigns positive probability to every integer from \(0\) through \(n-2\), so every \(J_i>0\) and the first term of (1) is strictly positive. If \(f\) is affine, \(W_f\) is constant because \(\sum_iN_i=n\), and the covariance vanishes.

For uniform probabilities, all \(G_i\) agree and the last sum in (1) vanishes. Substituting \(f(k)=\mathbf1\{k=r\}\) gives the binomial second-difference formula in the finding. At \(r=0\) only \(b_{n-2}(0)\) survives. At \(r=1\), the difference reduces to
\[
\operatorname{Cov}(T,F_1)=\binom n2\frac{n-2m}{m^2}(1-1/m)^{n-2}.
\]
For \(2\le r\le n\), \(b_{n-2}(r-2)>0\). Dividing the second difference by this factor and multiplying by the positive quantity \(r(r-1)(m-1)^2\) gives
\[
r(r-1)(m-1)^2-2r(n-r)(m-1)+(n-r)(n-r-1)=P_{n,m}(r).
\]
The discriminant of this upward quadratic in \(r\) is \(m^2((m-2)^2+4n(m-1))>0\); the quadratic formula gives the stated roots and sign regions. This completes both statements for every integer \(n,m\) in scope.

## Verification

The standalone `verify.py` implements independent exact multinomial occupancy enumeration using rational arithmetic, and a separate computation of the two-draw identity. It checks all five probability profiles in the source, \(2\le n\le9\), every convex hinge \(f(k)=\max(0,k-j)\), every frequency indicator \(f(k)=\mathbf1\{k=r\}\), affine equality, and all uniform sign/boundary cases. Running `python verify.py` produced: `PASS: 520 exact-rational occupancy distribution and covariance checks; 180 strict convex hinges; exact boundary identities verified.` The finite checks are corroboration only; the preceding proof establishes the all-parameter result.

## Relationship to prior work

The literature studies collision-pair counts and frequency-of-frequency spectra separately and together, especially in asymptotic regimes. Eaton, Godbole and Sinclair (2008) work with the identical collision variable and occupancy frequency variables, but their Theorems 1–3 provide Poisson approximation bounds, not the finite-sample sign classification or convex-score association of this finding. Hitczenko and Wormald (2023) study asymptotic multivariate normality of frequency counts with bounded cell capacities; these assumptions and conclusions do not imply the present finite, possibly nonuniform, collision-covariance inequality. Zhu (2021) studies attainable laws for the total number of distinct observed values rather than the present pair-collision/convex-occupancy covariance. Classical binomial moments can calculate each covariance, but the *all-convex-scores strict sign* and exact two-root phase classification require the stated additional comparison.

## Limitations

This is an exact finite iid categorical theorem, not a theorem for dependent allocations, empty/zero-probability categories retained in the support, or general convex functions of the whole occupancy vector. The frequency sign law assumes uniform probabilities. Its relation to older general occupancy moment identities remains a historical-priority risk; the checked works provide close ingredients but do not explicitly state this combined result. No independent mathematical review or comprehensive historical-priority certification has been performed.

## References

1. J. Eaton, A. Godbole, and B. Sinclair, *Competition between Discrete Random Variables, with Applications to Occupancy Problems*, arXiv:0806.1007, first posted 5 June 2008, Sections 1–2, Theorems 1–3. https://arxiv.org/abs/0806.1007
2. P. Hitczenko and N. Wormald, *Multivariate asymptotic normality determined by high moments*, arXiv:2312.04246v1, first posted 7 December 2023, Sections 1 and 4. https://arxiv.org/abs/2312.04246
3. T. Zhu, *The distribution of the number of distinct values in a finite exchangeable sequence*, arXiv:2103.07518v1, first posted 12 March 2021, Sections 1–2 and 4–5. https://arxiv.org/abs/2103.07518
