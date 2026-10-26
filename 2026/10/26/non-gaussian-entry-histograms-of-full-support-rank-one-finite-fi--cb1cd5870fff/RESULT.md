# Non-Gaussian entry histograms of full-support rank-one finite-field matrices

## Finding

Fix a finite field \(\mathbb F_q\) and let \(H=\mathbb F_q^\times\), with \(d=q-1\). For positive integers \(m,n\), choose \(M\) uniformly from the \(m\)-by-\(n\) matrices over \(\mathbb F_q\) of rank exactly one **and with no zero entries**. Equivalently, choose uniformly among rank-one matrices having no zero row or column. For \(a\in H\), let
\[
N_a(M)=|\{(i,j):M_{ij}=a\}|,
\qquad
Z_{m,n}(a)=\frac{N_a(M)-mn/d}{\sqrt{mn}}.
\]
The histogram coordinates satisfy the exact, finite-size identities
\[
\mathbb E N_a=\frac{mn}{d},\qquad
\operatorname{Cov}(N_a,N_b)
=mn\left(\frac{\mathbf1_{a=b}}d-\frac1{d^2}\right).
\]
In fact, **any two distinct entries of \(M\) are independent**, even when they lie in the same row or column. Nevertheless, for fixed \(q\) and *every* joint limit \(m,n\to\infty\), the vector \((Z_{m,n}(a))_{a\in H}\) has a generally non-Gaussian limit \(Z=(Z_a)_{a\in H}\), with the following complete joint characteristic function: for every real vector \((t_a)_{a\in H}\),
\[
\boxed{\quad
\mathbb E\exp\!\left(i\sum_{a\in H}t_aZ_a\right)
=\prod_{\substack{\chi\in\widehat H\\\chi\ne1}}
\left(1+\frac1{d^2}\left|\sum_{a\in H}t_a\chi(a)\right|^2\right)^{-1/2}.
\quad}
\]
Every nontrivial multiplicative character occurs once, including both members of a nonreal conjugate pair. For \(d\ge2\), each individual coordinate has characteristic function and cumulants
\[
\mathbb E e^{itZ_a}=(1+t^2/d^2)^{-(d-1)/2},\qquad
\operatorname{Var}(Z_a)=\frac{d-1}{d^2},\qquad
\kappa_4(Z_a)=\frac{6(d-1)}{d^4}>0.
\]
Thus **no coordinate has a Gaussian limit** when \(q\ge3\). For \(q=3\), a coordinate has the distribution of one half the product of two independent standard normal variables. For \(q=4\), every coordinate has the exact limiting Laplace density
\[
\boxed{\quad f(z)=\frac32e^{-3|z|}\quad(z\in\mathbb R).\quad}
\]
For \(q=2\), the ensemble contains only the all-ones matrix and the centered histogram is identically zero.

An exact finite-histogram formula accompanies the limit. If nonnegative integers \((\nu_a)_{a\in H}\) sum to \(mn\), then
\[
\Pr((N_a)_{a\in H}=(\nu_a)_{a\in H})
=\frac1{d^{m+n}}
\sum_{\substack{r_x,c_y\ge0,\ \sum_xr_x=m,\ \sum_yc_y=n\\
\sum_xr_xc_{ax^{-1}}=\nu_a\ \forall a\in H}}
\frac{m!\,n!}{\prod_{x\in H}r_x!\prod_{y\in H}c_y!}.
\]
No asymptotic balance condition between \(m\) and \(n\) is required.

## Assumptions and scope

The field size \(q\) is a fixed prime power, \(m,n\ge1\), and both dimensions must diverge for the joint limiting statement. Conditioning on no zero entries is essential and is distinct from unconditional fixed-rank sampling. Among *all* rank-one \(m\)-by-\(n\) matrices, the conditioning event has exact probability
\[
\frac{d^{m+n}}{(q^m-1)(q^n-1)}.
\]
This event becomes exponentially rare at fixed \(q\), but it is the natural full-support stratum of the rank-one determinantal variety. All entries lie in \(H\); therefore the zero-entry count is identically zero. The proof in fact requires only a finite abelian multiplicative label group, but the stated matrix result concerns finite fields.

## Proof

**1. Uniform factorization and support.** Any nonzero rank-one matrix is an outer product \(uv^{\mathsf T}\) with nonzero vectors \(u,v\). It has no zero entries precisely when every coordinate of both factors belongs to \(H\). Any such matrix has exactly \(d\) factorizations with \(u\in H^m\), \(v\in H^n\), because its factors are unique up to the action \((u,v)\mapsto(cu,c^{-1}v)\) for \(c\in H\). Hence independent uniform \(u\in H^m\) and \(v\in H^n\) produce the stipulated uniform matrix law. There are exactly \(d^{m+n-1}\) distinct matrices in the full-support stratum. The standard total number of rank-one matrices is \((q^m-1)(q^n-1)/d\), proving the conditioning probability.

For any two distinct cells, their values \(u_iv_j\) and \(u_kv_\ell\) are independent and uniform on \(H\). When the row and column indices are both different this is immediate from independent factors; when one index coincides, condition on the shared factor and use uniformity and independence of the remaining two factors. Summing the resulting cellwise covariances proves the exact mean and covariance above.

**2. Complete finite formula and cancellation.** Let \(R_x=|\{i:u_i=x\}|\), \(C_y=|\{j:v_j=y\}|\). Independently, \((R_x)_{x\in H}\) and \((C_y)_{y\in H}\) are uniform-category multinomial vectors with sample sizes \(m\) and \(n\). Every cell with value \(a\) arises from a pair \((x,a x^{-1})\), so
\[
N_a=\sum_{x\in H}R_x C_{ax^{-1}}.
\]
Multinomial counting gives the displayed finite-histogram sum. Since \(\sum_x(R_x-m/d)=0\) and \(\sum_y(C_y-n/d)=0\) exactly, expanding this identity cancels both linear terms:
\[
\boxed{\quad
N_a-\frac{mn}{d}
=\sum_{x\in H}(R_x-m/d)(C_{ax^{-1}}-n/d).
\quad}
\]
This exact degeneracy is responsible for the non-Gaussian limit despite pairwise independence of the entries.

**3. Joint limit.** Put \(U_{m,x}=(R_x-m/d)/\sqrt m\) and \(V_{n,y}=(C_y-n/d)/\sqrt n\). The multivariate multinomial central limit theorem and independence of the two factor samples give
\[
(U_m,V_n)\ \xrightarrow{\mathrm d}\ (U,V),
\qquad U\perp V,
\qquad U,V\sim N_d(0,d^{-1}P),
\quad P=I_d-d^{-1}\mathbf1\mathbf1^{\mathsf T}.
\]
Consequently, by the exact identity and the continuous mapping theorem, jointly for all \(a\in H\),
\[
Z_{m,n}(a)\xrightarrow{\mathrm d}
Z_a:=\sum_{x\in H}U_x V_{ax^{-1}}.
\]
This reasoning does not restrict the ratio of the diverging dimensions.

**4. Characteristic function and diagonalization.** For real parameters \(t_a\), let \(B_t\) be the real \(d\)-by-\(d\) matrix with entries \((B_t)_{x,y}=t_{xy}\). Then \(\sum_a t_aZ_a=U^{\mathsf T}B_tV\). Writing independent standard real Gaussian vectors \(G,K\) in \(\mathbb R^d\) gives \(U=d^{-1/2}PG\), \(V=d^{-1/2}PK\). Gaussian integration, first in \(K\), then in \(G\), yields
\[
\mathbb E e^{iU^{\mathsf T}B_tV}
=\det_{\mathbf1^\perp}\!\left(I_{\mathbf1^\perp}
+d^{-2}(PB_tP)(PB_tP)^{\mathsf T}\right)^{-1/2}.
\]
For each multiplicative character \(\chi\) regarded as a complex vector indexed by \(H\),
\[
(B_t\chi)(x)=\chi(x)^{-1}\sum_{a\in H}t_a\chi(a).
\]
The constant character spans \(\mathbf1\) and is removed by \(P\). The nontrivial characters form an orthogonal basis of the complexified centered subspace. Therefore the squared singular values of \(PB_tP\) there are precisely \(\left|\sum_a t_a\chi(a)\right|^2\), one per nontrivial character, proving the joint characteristic function. Complex-conjugate characters supply the correct multiplicities for the determinant of a real operator.

**5. Marginals and non-Gaussianity.** If only one parameter \(t_a=t\) is nonzero, then \(\left|\sum_b t_b\chi(b)\right|=|t|\) for every character. Hence \(\phi_{Z_a}(t)=(1+t^2/d^2)^{-(d-1)/2}\). Equivalently, for independent standard real normals \(G_j,K_j\),
\[
Z_a\ \stackrel{\mathrm d}=\ \frac1d\sum_{j=1}^{d-1}G_jK_j.
\]
Expanding \(\log\phi_{Z_a}\) at zero gives \(\operatorname{Var}(Z_a)=(d-1)/d^2\) and fourth cumulant \(6(d-1)/d^4\). At \(d=2\) this is a scaled product-normal distribution; at \(d=3\) the characteristic function is \((1+t^2/9)^{-1}\), the Fourier transform of the stated Laplace density. At \(d=1\) the sum is empty and identically zero. This completes the proof.

## Verification

The standalone standard-library script `checker.py` enumerates every full-support rank-one matrix by fixing its gauge, over cyclic label groups of sizes \(d=1,2,3,4,5\) for \((m,n)=(2,2),(2,3),(3,3)\). It checks that there are exactly \(d^{m+n-1}\) distinct matrices, checks the mean/covariance identities as exact rational equalities, and checks pairwise independence for all six pairs of cells in the upper-left two-by-two rectangle. Its separate real determinant-versus-discrete-Fourier calculation checks the limiting joint characteristic-function diagonalization numerically for cyclic groups through order six, without Monte Carlo. The cyclic-group test at \(d=5\) is an extension of the group calculation, **not** an assertion that a field of order six exists. The output is in `checker_output.txt`; the success line is `ALL_FULL_SUPPORT_RANK_ONE_CHECKS_PASSED cases=15 matrices=5629 Fourier_cases=6`. These checks are finite consistency tests, not substitutes for the multivariate limit proof.

## Relationship to prior work

Migler, Morrison and Ogle (2006) determine the total nonzero weight distribution for rank-one finite-field matrices; on the full-support stratum this weight is deterministically \(mn\), so their weight statistic does not distinguish the values of the nonzero entries. Sanna (2023, arXiv:2307.14172, Theorem 1.1) proves a Gaussian limit for the count of entries in a specified value-set under **unconditional** fixed-rank sampling. Its Lemma 5.4 includes an exact bilinear Fourier decomposition: this is a substantial antecedent mechanism, and the present result does not claim to originate that decomposition. Chan and Xiong (2024, arXiv:2409.10412) extend that unconditional Gaussian theorem to certain growing-rank regimes. Here a different, exponentially rare but intrinsic conditional ensemble removes the leading mask fluctuation, and the claimed additional conclusions are the full non-Gaussian joint law, explicit character-product characteristic function, pairwise independence, and the Laplace/product-normal specializations. An equivalent conditional derivation embedded in other published analyses remains possible.

## Limitations

This result concerns rank one and no zero entries, at fixed field order with both dimensions diverging; it does not address higher ranks, unrestricted rank-one entry histograms, growing field order, or a quantitative convergence rate. The marginal distribution is not independent across labels: \(\sum_{a\in H}Z_a=0\) almost surely. The exact finite covariance does **not** imply a Gaussian limit. The argument uses the classical multinomial CLT and finite-group Fourier orthogonality. The source comparisons do not establish exhaustive historical priority.

## References

1. T. Migler, K. E. Morrison and M. Ogle, *How Much Does a Matrix of Rank k Weigh?*, Mathematics Magazine 79 (2006), 262–271. Open author copy: https://aimath.org/~morrison/Research/Weight-Rank.pdf .
2. C. Sanna, *On the distribution of the entries of a fixed-rank random matrix over a finite field*, arXiv:2307.14172v1, first released 2023-07-26. https://arxiv.org/html/2307.14172v1 .
3. C. H. Chan and M. Xiong, *The central limit theorem for entries of random matrices with specific rank over finite fields*, arXiv:2409.10412v1, first released 2024-09-16. https://arxiv.org/abs/2409.10412 .
