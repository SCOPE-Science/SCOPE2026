# A universal sharp nonlinear spectral rate for cyclic induced Aluthge means

## Finding

Fix an integer \(m\geq 2\) and a normalized Kubo–Ando operator mean whose representing function \(f:(0,\infty)\to(0,\infty)\) is operator monotone, satisfies \(f(1)=1\), and has \(\lambda=f'(1)\in(0,1)\). Write its scalar restriction as \(h(a,b)=a f(b/a)\) for positive \(a,b\). On \(\ell^2(\mathbb Z)\), let \(Ue_j=e_{j+1}\), and let \(T=U\operatorname{diag}(w_j)\) be any strictly positive \(m\)-periodic bilateral weighted shift. Its induced Aluthge iterates are the operators \(T^{[k]}=U\operatorname{diag}(w^{[k]}_j)\), where

\[
w^{[0]}_j=w_j,\qquad w^{[k+1]}_j=h(w^{[k]}_{j+1},w^{[k]}_j).
\]

They converge in operator norm to \(cU\) for some \(c>0\). Define

\[
\rho_m(\lambda)=\sqrt{1-4\lambda(1-\lambda)\sin^2(\pi/m)}.
\]

If \(\rho_m(\lambda)>0\), then for every initial positive weight profile there is a finite \(C\) such that

\[
\|T^{[k]}-cU\|\leq C\rho_m(\lambda)^k\qquad(k\geq0).
\]

The exponent is **sharp for every such operator mean**: there exist nonconstant positive initial profiles arbitrarily close to the constant profile with

\[
\lim_{k\to\infty}\|T^{[k]}-cU\|^{1/k}=\rho_m(\lambda).
\]

In the sole degenerate case \(m=2\) and \(\lambda=1/2\), convergence is supergeometric: the \(k\)-th root of the norm error has limit zero for every initial profile. The sharp worst-case rate among means is uniquely minimized by their first derivative \(\lambda=1/2\), with minimum \(\cos(\pi/m)\) (zero for \(m=2\)). Thus the **optimal asymptotic speed depends only on the first derivative of the representing function**, even though the limiting scalar generally depends on the entire mean.

## Assumptions and scope

The Hilbert space is complex \(\ell^2(\mathbb Z)\), the weights are real and strictly positive, and their period divides \(m\). The operator mean is any normalized, nontrivial Kubo–Ando mean with \(0<f'(1)<1\); symmetry of the mean is not assumed. The statement concerns fixed finite period \(m\) and convergence of the infinite-dimensional bilateral operator in operator norm. Constants are allowed to depend on the mean, the period, and the initial weights; no uniform-in-period bound is asserted. The quantity \(\rho_m(\lambda)\) is the *worst-case* exponential factor, not necessarily the factor of a particular profile with missing slow Fourier modes.

## Proof

**Operator reduction and consensus.** Since all weights are strictly positive and periodic, \(T=U|T|\) is a polar decomposition with unitary \(U\), and the induced mean is \(U h(U^*|T|U,|T|)\). The diagonal entries give the asserted scalar recurrence. A nontrivial Kubo–Ando mean with derivative strictly between zero and one is continuous, strictly increasing in each scalar argument, homogeneous of degree one, and strictly internal: \(\min(a,b)<h(a,b)<\max(a,b)\) when \(a\neq b\). This follows, for example, from the weighted harmonic and arithmetic mean bounds associated with \(f'(1)\).

Let \(a_k\) and \(b_k\) be the smallest and largest weights at step \(k\). Monotonicity and internality imply that \(a_k\) increases and \(b_k\) decreases. After \(m-1\) steps, each coordinate depends strictly increasingly on all \(m\) original coordinates. Therefore the diameter of any nonconstant profile strictly decreases after \(m-1\) steps. All profiles remain in the compact positive box between the initial extrema. If the diameters converged to a positive limit, take an accumulation point: continuity and the strict \((m-1)\)-step decrease at this nonconstant limit point would contradict convergence of the diameters. Hence the diameter tends to zero and the nested extrema converge to a common positive \(c\). In particular \(\|T^{[k]}-cU\|=\max_j|w_j^{[k]}-c|\to0\).

**The linearized cyclic spectrum.** Put \(y^{[k]}_j=\log w_j^{[k]}\), let \(\mathbf1=(1,\ldots,1)\), and write \(y^{[k]}=t_k\mathbf1+z_k\), with \(t_k\) the arithmetic average of the logarithms and \(z_k\perp\mathbf1\). The log-mean map is translation equivariant. Its Jacobian at any constant profile is

\[
B=\lambda I+(1-\lambda)S,\qquad (Sz)_j=z_{j+1\pmod m}.
\]

Operator monotonicity makes \(f\) real analytic on the positive half-line. Thus, near consensus, the centered recurrence and the scalar drift satisfy

\[
z_{k+1}=Bz_k+R(z_k),\quad \|R(z)\|_2\leq K\|z\|_2^2,\qquad |t_{k+1}-t_k|\leq K\|z_k\|_2^2.
\]

The discrete Fourier vectors diagonalize \(B\), with eigenvalues \(\lambda+(1-\lambda)e^{2\pi i r/m}\). On the zero-mean subspace,

\[
\|B\|=\max_{1\leq r<m}|\lambda+(1-\lambda)e^{2\pi i r/m}|=\rho_m(\lambda)<1.
\]

The maximum occurs at \(r=1\) and \(r=m-1\). The only zero maximum is \(m=2,\lambda=1/2\).

**Exact uniform exponential envelope.** Suppose \(\rho=\rho_m(\lambda)>0\). By the established consensus, eventually the quadratic remainder estimate holds and, for sufficiently small \(\eta>0\),

\[
\|z_{k+1}\|_2\leq(\rho+\eta)\|z_k\|_2,\qquad (\rho+\eta)^2<\rho.
\]

Consequently \(\|z_k\|_2=O((\rho+\eta)^k)\). Variation of constants in \(z_{k+1}=Bz_k+R(z_k)\) then yields

\[
\|z_k\|_2\leq O(\rho^k)+\sum_{j<k}\rho^{k-1-j}O((\rho+\eta)^{2j})=O(\rho^k).
\]

Here and below a fixed finite index shift is absorbed into the implied constants. Since \(t_k\to\log c\), the scalar drift estimate gives \(|t_k-\log c|=O(\rho^{2k})\). Finally exponentiation is locally Lipschitz, proving the asserted operator-norm bound.

**Sharpness.** Let \(E\) be the real invariant Fourier subspace spanned by frequencies \(1\) and \(m-1\) (one dimension when \(m=2\)), and fix a real \(v\in E\) of Euclidean norm one. Start at \(w_j=\exp(\varepsilon v_j)\) with any sufficiently small nonzero \(\varepsilon\). A quadratic variation-of-constants bootstrap gives \(\|z_k\|_2\leq2|\varepsilon|\rho^k\): if this is valid through step \(k-1\), the remainder contributes at most \(4K\varepsilon^2\rho^{k-1}/(1-\rho)\), and smallness of \(\varepsilon\) closes the estimate. Let \(P_E\) be orthogonal projection onto \(E\). Since \(B|_E\) is \(\rho\) times a real orthogonal map, the sequence

\[
a_k=(B|_E)^{-k}P_Ez_k
\]

is Cauchy, because the sum of successive increments is at most \(O(\varepsilon^2)\), using the quadratic remainder and \(\sum_{j\ge0}\rho^j<\infty\). Its limit satisfies \(a_\infty=\varepsilon v+O(\varepsilon^2)\neq0\). Hence \(\|P_Ez_k\|_2=\rho^k(\|a_\infty\|_2+o(1))\). This lower bound and the preceding upper bound give the sharp operator-norm root limit, because the logarithm and exponential are uniformly locally bi-Lipschitz near \(c\).

**Degenerate endpoint and optimization.** When \(m=2\) and \(\lambda=1/2\), the centered Jacobian is zero. For all sufficiently large \(k\), \(\|z_{k+1}\|_2\leq K\|z_k\|_2^2\), so the centered error tends to zero faster than any geometric sequence. The scalar drift tail is bounded by a constant times \(\|z_k\|_2^2\), and the same holds for the full operator error. Finally, \(\lambda(1-\lambda)\) has its unique maximum at \(\lambda=1/2\); this uniquely minimizes the attained worst-case factor and gives \(\sqrt{1-\sin^2(\pi/m)}=\cos(\pi/m)\).

## Verification

The accompanying standalone `CHECK.py` replays the scalar iterations for weighted arithmetic, geometric, and harmonic Kubo–Ando means and a nonsymmetric convex combination with derivative \(1/2\). It verifies the cyclic Fourier spectral radius, min/max invariance, monotone contraction of the range, and the Jacobian linearization on deterministic finite test instances. The successful run reported 54,076 checks. These tests are finite diagnostics; the above argument establishes the infinite-iteration and operator-norm assertions.

## Relationship to prior work

Osaka and Yamazaki (2024, arXiv:2409.03338, first submitted September 5, 2024) establish qualitative convergence of induced Aluthge iterations for invertible centered matrices and provide the cyclic operator-mean reduction. Their Theorem 4.4 gives consensus but not this universal sharp nonlinear rate or small-perturbation lower witnesses. Yamazaki (2019, arXiv:1912.08452, §5) gives the general scalar perspective recurrence and exact arithmetic and harmonic specializations, including binomial formulas. Rion (2011, *Dense orbits of the Aluthge transform*, pp. 51–52) gives an exact binomial-weight formula for iterated ordinary Aluthge shifts. Thus the geometric-mean specialization of the scalar update is already explicit in earlier work; novelty is **not** claimed for that recurrence or its elementary finite Fourier diagonalization. The asserted quantitative extension concerns all Kubo–Ando means, including nonlinear nonsymmetric scalar means, and proves that every mean shares a rate determined only by its derivative at one. Pálfia and Petz (2014) investigate a different multivariate operator-mean symmetrization and establish convergence of that iteration; their algorithm and rate statements do not give the present nearest-neighbor induced-Aluthge worst-case factor. Antezana, Pujals and Stojanoff (2011, §6.1) obtain exponential estimates for some finite-matrix Aluthge iterates whose factors depend on matrix spectra; these do not state a sharp derivative-only rate across all Kubo–Ando means. These comparisons cannot establish uniqueness of the present formulation.

## Limitations

The theorem concerns strictly positive periodic scalar weights; it does not establish a uniform rate for arbitrary nonperiodic sequences, noncommuting operator-valued weights, or time-varying means. The asymptotic factor is sharp as a supremum across initial data; individual weights can converge faster. It does not identify the nonlinear limit \(c\) for every operator mean. Near-constant sharpness witnesses are local, not a classification of all exceptional initial profiles. The literature comparison cannot rule out every equivalent formulation in nonlinear consensus or matrix-mean dynamics.

## References

- H. Osaka and T. Yamazaki, *Limit of iteration of the induced Aluthge transformations of centered operators*, arXiv:2409.03338, version 1 submitted 2024-09-05; Theorems 2.3 and 4.4. https://arxiv.org/abs/2409.03338
- T. Yamazaki, *The induced Aluthge transformations*, Linear Algebra Appl. 628 (2021), 1–28, DOI:10.1016/j.laa.2021.06.014.
- K. Rion, *Dense orbits of the Aluthge transform*, thesis, Bowling Green State University (2011), §3.2, especially pp. 51–52. https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=bgsu1300722238
- M. Pálfia and D. Petz, *Weighted multivariable operator means of positive definite operators*, Linear Algebra Appl. 463 (2014), 134–153, DOI:10.1016/j.laa.2014.08.025.
- M. Pálfia, *A multivariable extension of two-variable matrix means*, SIAM J. Matrix Anal. Appl. 32 (2011), 385–393, DOI:10.1137/100797230.
- J. Antezana, E. Pujals and D. Stojanoff, *The iterated Aluthge transforms of a matrix converge*, Advances in Mathematics 226 (2011), 1591–1620, §6.1–6.2, DOI:10.1016/j.aim.2010.08.037.
- T. Yamazaki, *A generalization of the Aluthge transformation in the viewpoint of operator means*, arXiv:1912.08452v3 (2020), original version submitted 2019-12-18, especially §5. https://arxiv.org/abs/1912.08452
