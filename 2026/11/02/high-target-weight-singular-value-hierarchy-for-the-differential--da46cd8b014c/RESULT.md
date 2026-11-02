# High-target-weight singular-value hierarchy for the differential Hilbert operator

## Finding

Fix a real parameter \( -1<\alpha<0 \). On the normalized weighted Bergman spaces of the disk, consider the differential Hilbert operator
\[
\mathcal H_2 f(z)=\int_0^1\frac{f(t)}{(1-tz)^2}\,dt:
A^2_\alpha\longrightarrow A^2_\beta,
\qquad \beta>\alpha+2.
\]
Write \(s_1(\beta)\ge s_2(\beta)\ge\cdots>0\) for its singular values and
\[
w_m(\gamma)=\frac{\Gamma(\gamma+2)\,m!}{\Gamma(m+\gamma+2)},\quad
W_k(\beta)=\prod_{m=0}^{k-1}\sqrt{w_m(\beta)},\quad
F_k(\beta)=\frac{\prod_{j=1}^{k}s_j(\beta)}{W_k(\beta)}.
\]
For every fixed positive integer \(k\), the function \(F_k\) is **strictly decreasing and logarithmically convex** on \((\alpha+2,\infty)\). It has the exact positive limit
\[
\lim_{\beta\to\infty}F_k(\beta)
 =k!\sqrt{\det G_k(\alpha)}=:c_k(\alpha)>0,
\qquad
(G_k(\alpha))_{rs}=
\int_0^1\!\int_0^1\frac{x^r y^s}{(1-xy)^{\alpha+2}}\,dx\,dy,
\quad 0\le r,s<k.
\]
In particular, \(F_k(\beta)>c_k(\alpha)\) for every finite admissible \(\beta\), and this lower bound is optimal in the large-weight limit. With \(\det G_0(\alpha)=1\), every fixed-index singular value obeys the sharp asymptotic
\[
\boxed{\displaystyle
s_k(\beta)\sim k\sqrt{(k-1)!}
\sqrt{\frac{\det G_k(\alpha)}{\det G_{k-1}(\alpha)}}
\,\beta^{-(k-1)/2}}
\qquad(\beta\to\infty).
\]
Thus the constant mode survives at order one, while each successive approximation-number level loses another half-power of the target weight. For example, at \(\alpha=-1/2\), the norm tends to \(2\sqrt{\log 2}\).

## Assumptions and scope

The weighted Bergman monomial norm is \(\|z^m\|_{A^2_\gamma}^2=w_m(\gamma)\). The normalized monomials identify every space \(A^2_\gamma\) with \(\ell^2(\mathbb N_0)\); these identifications depend on \(\gamma\) and are included when comparing singular values. The source parameter is fixed in \((-1,0)\), the target parameter ranges over \(\beta>\alpha+2\), and the singular-value rank \(k\) is fixed before taking \(\beta\to\infty\). The theorem does not assert a uniform asymptotic when the rank also increases. The cited operator theorem supplies boundedness, compactness and trace-class membership in this domain.

## Proof

**1. Coefficient matrix and positive compound entries.** The normalized monomial matrix is
\[
B_{ij}(\beta)=\frac{i+1}{i+j+1}
\sqrt{\frac{w_i(\beta)}{w_j(\alpha)}}
\qquad(i,j\in\mathbb N_0).
\]
For any increasing \(k\)-tuples \(I=(i_1<\cdots<i_k)\) and \(J=(j_1<\cdots<j_k)\), its compound matrix \(C_k(\beta)=\bigwedge^k B(\beta)\) has coefficient
\[
(C_k(\beta))_{IJ}=
\left(\prod_{r=1}^k(i_r+1)\sqrt{w_{i_r}(\beta)}\right)
\left(\prod_{s=1}^k w_{j_s}(\alpha)^{-1/2}\right)
\det\left[\frac1{i_r+j_s+1}\right]_{r,s=1}^{k}.
\]
The classical Cauchy determinant formula gives
\[
\det\left[\frac1{i_r+j_s+1}\right]
=\frac{\prod_{r<t}(i_t-i_r)\prod_{s<t}(j_t-j_s)}
{\prod_{r,s}(i_r+j_s+1)}>0.
\]
Consequently every compound entry is strictly positive. All singular values are nonzero, since the matrix has nonzero minors of every order. The top singular-value product satisfies \(\|C_k(\beta)\|=\prod_{j=1}^k s_j(\beta)\).

**2. The normalized coefficient order.** Set \(I_0=(0,1,\ldots,k-1)\). After division by \(W_k(\beta)\), every compound entry is a positive \(\beta\)-independent constant times
\[
q_I(\beta)=\prod_{r=1}^{k}
\sqrt{\frac{w_{i_r}(\beta)}{w_{r-1}(\beta)}}.
\]
Because \(i_r\ge r-1\), each squared factor is \(1\) when \(i_r=r-1\), and otherwise equals
\[
\frac{w_{i_r}(\beta)}{w_{r-1}(\beta)}
=\prod_{h=r}^{i_r}\frac{h}{\beta+h+1}.
\]
These factors decrease strictly and have convex logarithms in \(\beta\). Hence every positive entry of \(C_k(\beta)/W_k(\beta)\) is decreasing and log-convex, with strict decrease in every row except \(I_0\). Since a matrix with nonnegative entries has the same norm after restricting the bilinear norm supremum to nonnegative unit vectors, entrywise order implies monotonicity. Compactness gives a nonnegative maximizing right vector at any fixed target weight; every row evaluates positively on that vector. The strictly decreasing off-minimal rows then make \(F_k\) strictly decreasing.

For any two admissible weights \(\beta_0,\beta_1\) and \(0<\theta<1\), entrywise log-convexity and Hölder's inequality for the positive bilinear sum give
\[
F_k((1-\theta)\beta_0+\theta\beta_1)
\le F_k(\beta_0)^{1-\theta}F_k(\beta_1)^\theta.
\]
The infinite sums are justified first on finite truncations and then by the bounded positive compound operators. This proves logarithmic convexity.

**3. Compactness identifies the exact limiting compound row.** Fix \(\beta_*>\alpha+2\). For \(\beta\ge\beta_*\), target monomial scaling yields
\[
\frac{C_k(\beta)}{W_k(\beta)}
=\frac{D_k(\beta)C_k(\beta_*)}{W_k(\beta_*)},
\]
where \(D_k(\beta)\) is diagonal on output \(k\)-tuples with multiplier \(q_I(\beta)/q_I(\beta_*)\). Each multiplier lies in \([0,1]\), equals \(1\) for \(I_0\), and tends to zero for all other \(I\). Thus \(D_k(\beta)\) converges strongly to the one-coordinate projection \(P_{I_0}\). The compactness of \(C_k(\beta_*)\), inherited from the source's compactness theorem, upgrades this to operator-norm convergence after right multiplication by \(C_k(\beta_*)\). Consequently,
\[
\lim_{\beta\to\infty} F_k(\beta)
=\frac{\|P_{I_0}C_k(\beta_*)\|}{W_k(\beta_*)}.
\]

**4. Exact Gram determinant.** The squared norm of the selected exterior row is, by Cauchy--Binet applied first to finite input truncations,
\[
\frac{\|P_{I_0}C_k(\beta_*)\|^2}{W_k(\beta_*)^2}
=(k!)^2\det\left[
\sum_{j=0}^{\infty}
\frac1{w_j(\alpha)(r+j+1)(s+j+1)}
\right]_{r,s=0}^{k-1}.
\]
Since \(1/w_j(\alpha)=(\alpha+2)_j/j!\), the binomial series and Tonelli's theorem identify this matrix with \(G_k(\alpha)\). Its entries are finite because the summand is \(O(j^{\alpha-1})\) and \(-1<\alpha<0\). It is positive definite: a vanishing quadratic form would imply \(\sum_{r=0}^{k-1}u_r/(r+j+1)=0\) for every nonnegative integer \(j\); a rational function with those infinitely many zeros has all coefficients zero. Hence \(c_k(\alpha)>0\). The strict decrease in Step 2 makes the finite-weight inequality strict.

**5. Individual singular values.** For each fixed \(m\), the gamma ratio gives \(w_m(\beta)\sim m!\,\beta^{-m}\). Since \(s_k(\beta)=(F_k(\beta)/F_{k-1}(\beta))\sqrt{w_{k-1}(\beta)}\), taking the positive limits yields the asserted sharp constant, with \(F_0\equiv1\). For \(k=1\), direct integration gives \(G_1(\alpha)=[\psi(1)-\psi(-\alpha)]/(\alpha+1)\); at \(\alpha=-1/2\) this equals \(4\log2\).

## Verification

The accompanying standard-library checker `check_spectral.py` performs exact rational checks of Cauchy-minor positivity, finite Cauchy--Binet Gram identities, binomial weight coefficients, and strict normalized row-weight monotonicity and midpoint log-convexity. On execution it returned `EXACT_BERG_SPECTRAL_OK 4240`. Finite checks corroborate the algebra but do not establish the infinite-rank spectral limits. Those follow from the compactness, strong-to-norm convergence, and Cauchy--Binet arguments above. A separate finite-section singular-value calculation also showed decreasing normalized spectral products for ranks one through four and target weights from two to two hundred; those finite numbers are not used to prove the theorem.

## Relationship to prior work

Li and Zhou determine the weighted Bergman coefficient matrix, boundedness/compactness, trace-class membership and a Gram representation of the operator norm. Their results do not provide fixed-rank singular-value asymptotics as the target weight tends to infinity, nor the present normalized exterior-product inequalities and exact finite Gram-determinant constants. Classical Cauchy total positivity, Cauchy--Binet and exterior-power norm identities are explicitly used as ingredients. Earlier work on generalized Hilbert operator Schatten membership and on exterior products of operators concerns different membership or approximation questions. The theorem does not claim newness for those classical ingredients or an independently certified publication priority.

## Limitations

The source weight is restricted to \(-1<\alpha<0\), and the target is in the compact range \(\beta>\alpha+2\). The asymptotics hold for each fixed singular index only. They do not yield the joint large-index/large-weight regime, a closed elementary evaluation of the higher Gram determinants, or results for arbitrary non-Hilbert Bergman exponents. The literature comparison is best-knowledge and does not exclude undiscovered equivalent formulations; no independent mathematical audit has been performed.

## References

1. S. Li and M. Zhou, *The Differential Hilbert Operator Between Weighted Bergman Spaces*, arXiv:2610.05672v1 (public October 5, 2026), especially Lemma 2.4, Theorem 3.1, Proposition 3.6, and Theorem 4.2.
2. H. Wulan, M. Zhou, and J.-F. Zhu, *Hilbert matrix norms on weighted Bergman spaces: even exponents and a counterexample to the beta formula*, arXiv:2607.23540v1 (2026), on the ordinary Hilbert matrix rather than the differential two-weight operator.
3. D. Chiotis, Z. A. Lykova, and N. J. Young, *Exterior products of operators and superoptimal analytic approximation*, Transactions of the London Mathematical Society (2021), DOI: 10.1112/tlm3.12035, for the classical exterior-power operator perspective.
