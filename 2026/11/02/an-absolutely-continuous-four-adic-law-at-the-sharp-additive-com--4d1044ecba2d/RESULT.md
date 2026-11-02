# An absolutely continuous four-adic law at the sharp additive-complement threshold

## Finding
Let \(A\) be the nonnegative integers with only digits \(0,1\) in base four, put \(B=2A\), and write \(A(x)=\#\{a\in A:a\le x\}\), \(B(x)=\#\{b\in B:b\le x\}\). For every integer \(k\ge1\), choose \(N_k\) uniformly from the integers in \([4^k,4^{k+1})\), and put
\[
R_k=\frac{A(N_k)B(N_k)}{N_k}.
\]
There is a nondegenerate, absolutely continuous probability measure \(\mu\), supported exactly on \([1,3/2]\), for which \(R_k\) converges in law to \(\mu\). In fact, for every real Lipschitz function \(g\) with Lipschitz constant \(L\),
\[
\left|\mathbb E[g(R_k)]-\int g(y)\,d\mu(y)\right|
\le L\bigl(4\cdot2^{-k}+2\cdot4^{-k}\bigr).
\]

Here is an explicit density, including all its Cantor-scale fluctuations. For every integer \(j\ge1\) and every binary word \(w=(\varepsilon_1,\ldots,\varepsilon_{j-1})\), set
\[
\begin{aligned}
s_w&=\sum_{i=1}^{j-1}\varepsilon_i4^{-i},
&c_w&=\sum_{i=1}^{j-1}\varepsilon_i2^{-i}+2^{-j},\\
a_w&=s_w+4^{-j}/3,
&b_w&=s_w+4^{-j},\\
\ell_w&=\frac{1+c_w}{1+b_w},
&u_w&=\frac{1+c_w}{1+a_w}.
\end{aligned}
\]
Then an exact density of \(\mu\), for almost every \(y\in\mathbb R\), is
\[
\boxed{
 f(y)=\frac{\mathbf1_{(1,3/2)}(y)}{y^2}
 \left(2+\sum_{j=1}^{\infty}\ \sum_{w\in\{0,1\}^{j-1}}
 (1+c_w)\mathbf1_{(\ell_w,u_w)}(y)\right).
}
\]
The baseline density \(2/y^2\) has mass exactly \(2/3\). The gap-indexed correction has mass exactly \(1/3\), and the first gap alone adds \(3/(2y^2)\) for \(6/5<y<18/13\). Thus the critical \(3/2\) threshold is approached with a full interval of nonzero limiting frequencies, not only along specially chosen subsequences.

## Assumptions and scope
The digit sets contain zero and have unique complement representations: every nonnegative integer is uniquely \(a+b\) with \(a\in A\), \(b\in B\). The probability refers to a *complete four-adic block* \([4^k,4^{k+1})\), with a uniformly random integer in that block; no assertion of a global natural-density distribution over arbitrary cutoffs is made. For clarity, the strict indicator intervals in the density formula can be assigned arbitrary boundary values, because the limiting law has no atoms.

Let \(Z=\sum_{i\ge1}\xi_i4^{-i}\), where the \(\xi_i\) are independent fair bits, and let \(F(u)=\Pr(Z\le u)\), extended by \(0\) below zero and by \(1\) above \(1/3\). Its support \(K\subset[0,1/3]\) has Lebesgue measure zero. Put \(\phi(u)=(1+F(u))/(1+u)\) for \(0\le u\le1/3\). An equivalent integral description, useful for reproducibility, is
\[
\int g\,d\mu
=2\int_1^{3/2}\frac{g(y)}{y^2}\,dy
 +\int_0^{1/3}g(\phi(u))\,du.
\]
In particular, these two terms have respective masses \(2/3\) and \(1/3\).

## Proof
**1. Exact block counts.** Let \(Z_k=\sum_{i=1}^k\xi_i4^{-i}\) and \(F_k(u)=\Pr(Z_k\le u)\). The \(2^k\) lower-digit words correspond bijectively to the elements of \(A\) below \(4^k\). For \(4^k\le n<4^{k+1}\), writing \(t=n/4^k\), direct counting of the current leading-digit block and the completed earlier blocks gives the *exact* identities
\[
\frac{A(n)}{2^k}=1+F_k(t-1),\qquad
\frac{B(n)}{2^k}=1+F_k((t-2)/2).
\]
Indeed, the new \(A\)-block begins at \(4^k\), and the new \(B\)-block begins at \(2\cdot4^k\); each has \(2^k\) lower-digit words.

**2. Uniform Cantor approximation.** Couple \(Z_k\) to \(Z\) by using the same first \(k\) digits. Then \(0\le Z-Z_k\le4^{-k}/3\). Distinct \(Z_k\) values are at least \(4^{-k}\) apart, so for every real \(u\), at most one value of \(Z_k\) can satisfy \(u-4^{-k}/3<Z_k\le u\). Consequently,
\[
0\le F_k(u)-F(u)\le2^{-k}\quad\text{uniformly in }u.
\]
Define the continuous profile
\[
\rho(t)=\frac{(1+F(t-1))(1+F((t-2)/2))}{t},\qquad1\le t\le4.
\]
The exact counts imply \(\sup_{4^k\le n<4^{k+1}}|A(n)B(n)/n-\rho(n/4^k)|\le4\cdot2^{-k}\).

**3. Quantitative limit.** The numerator of \(\rho\) is nondecreasing from \(1\) to \(4\); multiplication by \(1/t\) shows that \(\rho\) has total variation at most \(3+4(1-1/4)=6\). Therefore \(g\circ\rho\) has variation at most \(6L\), and its complete left Riemann sum over the mesh \(4^{-k}\) differs from \(\int_1^4g(\rho(t))\,dt\) by at most \(6L4^{-k}\). Divide by the interval length \(3\), combine with the uniform profile estimate, and obtain the displayed explicit Lipschitz bound with \(\mu=\rho_\#(dt/3|_{[1,4]})\).

**4. Two copies of each phase.** The profile has four consecutive forms:
\[
\rho(t)=\begin{cases}
\phi(t-1),&1\le t\le4/3,\\
2/t,&4/3\le t\le2,\\
\phi(t/2-1),&2\le t\le8/3,\\
4/t,&8/3\le t\le4.
\end{cases}
\]
Changing variables separately in these intervals yields
\[
\frac13\int_1^4g(\rho(t))\,dt
=\int_0^{1/3}g(\phi(u))\,du+2\int_1^{3/2}g(y)y^{-2}\,dy.
\]
The first and third intervals have the same \(\phi\)-profile but lengths in ratio \(1:2\); the two rational branches have the same image distribution.

**5. Range and density.** For \(u=\sum\varepsilon_i4^{-i}\in K\), the Cantor staircase satisfies \(F(u)=\sum\varepsilon_i2^{-i}\). All coefficients in
\[
F(u)-\tfrac32u=\sum_{i\ge1}\varepsilon_i(2^{-i}-\tfrac32\,4^{-i})
\]
are positive and their full sum is \(1/2\). Hence \(F(u)\le1/2+3u/2\); also \(F(u)\ge u\). Both inequalities extend to gaps of \(K\) by monotonicity or by using their endpoints. Thus \(1\le\phi(u)\le3/2\), with equality at the appropriate endpoints. The rational branches cover every value between \(1\) and \(3/2\), proving exact support and strict positivity of the baseline density on its interior.

At level \(j\), the deleted gaps of \(K\) are precisely \((a_w,b_w)\), indexed by the binary words \(w\) of length \(j-1\). On each such gap, \(F(u)=c_w\) and \(\phi(u)=(1+c_w)/(1+u)\), a smooth strictly decreasing bijection onto \((\ell_w,u_w)\). Its pushforward of Lebesgue measure has density \((1+c_w)y^{-2}\) on that image. The complement of the union of these gaps is \(K\), of measure zero (the total stage-\(j\) interval length is \(2^{-j}/3\)). Therefore their pushforwards exhaust the \(\phi\)-part with no singular remainder. Summing the gap densities and adding the rational-branch contribution proves the exact displayed density. All terms are nonnegative; monotone convergence justifies the sum. Each gap contributes mass \(b_w-a_w=2\cdot4^{-j}/3\), so the complete correction has mass \(\sum_{j\ge1}2^{j-1}(2\cdot4^{-j}/3)=1/3\). The first gap has \((a,b,c)=(1/12,1/4,1/2)\), producing the stated extra term on \((6/5,18/13)\). This also proves absence of atoms.

## Verification
The accompanying standalone \(VERIFY.py\) checks exact digit counts against independently constructed sorted digit sets over seven complete four-adic blocks, uses exact rational arithmetic for the Cantor profile and finite-stage bounds, verifies unique complement representations over finite intervals, and checks twelve finite gap-mass identities. Its successful run reports `VERIFY_OK blocks=7 exact_ratio_cells=65532 cylinder_bounds=65532 unique_sum_checks=1360 gap_masses=12 absolutely_continuous_formula=algebraic finite_only=YES`.

These finite checks do not establish weak convergence, absolute continuity, or the infinite density series by themselves; those conclusions follow from the preceding uniform coupling, bounded-variation estimate, and Cantor-gap decomposition. Run with `python3 VERIFY.py` without external packages.

## Relationship to prior work
Zihan Zhang, *A sharp bound for additive complements* (arXiv:2610.29963v1, October 21, 2026), proves the optimal \(3/2\) upper-limit threshold and reproduces this specific base-four digit construction in Section 6. Its result concerns the sharp limsup and bounded excess, not the limiting distribution of counting-function products on full four-adic blocks. F. Y. Ma, *A note on additive complements* (arXiv:2205.04128, May 2022), studies extremal limsup values for digit-block complement families; its reported statements and relevant construction arguments are likewise concerned with extrema rather than the explicit absolutely continuous block law. The base-four construction itself and the fact that its product limsup is \(3/2\) are **not claimed as new**. The contribution here is the complete block-distribution law, explicit rate, full-support absolutely continuous density, and Cantor-gap correction of precise mass \(1/3\).

## Limitations
The law is tied to a uniform integer sampled within one full multiplicative scale \([4^k,4^{k+1})\). It does not assert the same distribution under uniform sampling from all integers up to an arbitrary moving cutoff, or for arbitrary exact additive complements. The density series is an almost-everywhere identity and need not converge pointwise at every \(y\). No independent external audit or exhaustive publication-priority certification has been performed; an equivalent unindexed analysis of this particular digit construction is a residual bibliographic risk.

## References
1. Z. Zhang, *A sharp bound for additive complements*, arXiv:2610.29963v1 (first posted October 21, 2026), https://arxiv.org/abs/2610.29963.
2. F. Y. Ma, *A note on additive complements*, arXiv:2205.04128v1 (May 2022), https://arxiv.org/abs/2205.04128.
3. Y. G. Chen and J. H. Fang, *On additive complements. II*, Proceedings of the American Mathematical Society **139** (2011), 881–883 (historical origin of the sharp digit-complement extremal construction as cited by Zhang).
