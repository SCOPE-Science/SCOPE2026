# All even-moment rigidity for quadratic spherical harmonics on the two-sphere

## Finding

Let \(\sigma\) denote probability-normalized area measure on \(S^2\). Every nonzero **real** degree-two spherical harmonic can be written uniquely as \(Y_A(\omega)=\omega^{\mathsf T}A\omega\), where \(A\) is a real symmetric, nonzero, traceless \(3\times3\) matrix. Put
\[
S=\operatorname{tr}(A^2)>0,\qquad T=\operatorname{tr}(A^3),\qquad \delta=\frac{6T^2}{S^3}.
\]
Then \(0\le\delta\le1\). For **every integer** \(m\ge1\), the normalized even moment has the exact positive-polynomial representation
\[
\boxed{\frac{\displaystyle\int_{S^2}|Y_A|^{2m}\,d\sigma}
{\left(\displaystyle\int_{S^2}|Y_A|^2\,d\sigma\right)^m}
=R_m(\delta)}
\]
where the rising factorial is \((a)_j=a(a+1)\cdots(a+j-1)\), with \((a)_0=1\), and
\[
\boxed{R_m(z)=\frac{15^m(2m)!}{(4m+1)!!}
\sum_{h=0}^{\lfloor m/3\rfloor}
\frac{(\tfrac12)_{m-h}}{(m-3h)!(2h)!}
\left(\frac{4z}{27}\right)^h.}
\]
Here \((4m+1)!!=1\cdot3\cdot5\cdots(4m+1)\). All coefficients of \(R_m\) are nonnegative, and its coefficient of \(z\) is strictly positive for every \(m\ge3\). Thus for every \(m\ge3\), \(R_m\) is strictly increasing on \([0,1]\), giving the **sharp two-sided bounds for real harmonics**
\[
\boxed{R_m(0)\le\frac{\|Y_A\|_{2m}^{2m}}{\|Y_A\|_2^{2m}}\le R_m(1).}
\]
The upper equality holds precisely for nonzero multiples of rotated zonal quadratics \(Y_A(\omega)=c((v\cdot\omega)^2-1/3)\), where \(c\in\mathbb R\setminus\{0\}\), \(v\in S^2\). The lower equality holds precisely when \(A\) has eigenvalues \((a,0,-a)\), where \(a\ne0\), equivalently when \(Y_A\) is, up to rotation, a nonzero multiple of \(\omega_1^2-\omega_2^2\).

For **complex** degree-two spherical harmonics \(F\), the upper bound remains sharp:
\[
\boxed{\|F\|_{2m}^{2m}\le R_m(1)\|F\|_2^{2m}\qquad(m\ge3).}
\]
Every nonzero complex equality case is \(F(\omega)=\gamma((v\cdot\omega)^2-1/3)\), with \(\gamma\in\mathbb C\setminus\{0\}\) and \(v\in S^2\). No corresponding two-sided complex bound is asserted.

The quartic case is degenerate: \(R_2(z)=15/7\) independently of biaxiality. **Degree six is the first even moment that distinguishes the shapes**:
\[
\boxed{R_3(\delta)=\frac{5625+1000\delta}{1001},\qquad
R_3(1)-R_3(\delta)=\frac{1000}{1001}(1-\delta).}
\]
In particular, the sharp real lower sixth-moment ratio is \(5625/1001\), the sharp real-and-complex upper ratio is \(6625/1001\), and the last equation is an exact global biaxiality deficit.

## Assumptions and scope

The sphere is \(S^2=\{\omega\in\mathbb R^3:\|\omega\|=1\}\), with \(\int_{S^2}1\,d\sigma=1\); every norm \(\|\cdot\|_p\) is taken with respect to \(\sigma\). All matrices encoding real harmonics are real symmetric, traceless and nonzero. Integer \(m\) ranges over all \(m\ge1\); the extremizer classifications and strict polynomial dependence refer to \(m\ge3\). No claim is made for non-even exponents, higher harmonic degree, or complex lower extremizers.

## Proof

**1. Gaussian-to-sphere reduction.** Let \(G\sim N(0,I_3)\). Write \(G=\rho\omega\) in polar form, where \(\omega\) is uniform on \(S^2\), independent of \(\rho\). For every integer \(m\ge0\), \(\mathbb E\rho^{4m}=(4m+1)!!\). Also, for traceless symmetric \(A\),
\[
\|Y_A\|_2^2=\frac{\mathbb E(G^{\mathsf T}AG)^2}{\mathbb E\rho^4}=\frac{2S}{15}.
\]

**2. The exact generating function.** For real \(t\) close to zero, diagonalizing \(A\) gives
\[
\begin{aligned}
\mathbb E\exp(tG^{\mathsf T}AG)
&=\det(I-2tA)^{-1/2}\\
&=\left(1-2St^2-\frac83Tt^3\right)^{-1/2}.
\end{aligned}
\]
Indeed, \(\operatorname{tr}A=0\) and \(\det A=T/3\) imply \(\det(I-2tA)=1-2St^2-(8/3)Tt^3\). In the binomial expansion of this generating function, contributions to \([t^{2m}]\) can contain exactly \(2h\) factors of \(t^3\), accompanied by \(m-3h\) factors of \(t^2\), for \(0\le h\le\lfloor m/3\rfloor\). Consequently,
\[
\mathbb E(G^{\mathsf T}AG)^{2m}
=(2m)!(2S)^m
\sum_{h=0}^{\lfloor m/3\rfloor}
\frac{(\tfrac12)_{m-h}}{(m-3h)!(2h)!}
\left(\frac{4\delta}{27}\right)^h.
\]
Dividing by \((4m+1)!!\), then by \((2S/15)^m\), proves the exact \(R_m\) formula. For \(m=1\) and \(m=2\), the sum has only \(h=0\); for \(m\ge3\), the term \(h=1\) is strictly positive and every further coefficient is nonnegative. Therefore \(R_m\) is strictly increasing on the whole interval \([0,1]\) for every \(m\ge3\).

**3. Exact feasible interval and real equality cases.** Write the real eigenvalues of \(A\) as \(\lambda_1,\lambda_2,\lambda_3\). Their characteristic polynomial is
\[
\lambda^3-\frac S2\lambda-\frac T3.
\]
Its discriminant is
\[
\prod_{i<j}(\lambda_i-\lambda_j)^2
=\frac{S^3}{2}-3T^2\ge0.
\]
Hence \(0\le\delta\le1\). Equality \(\delta=1\) forces a repeated eigenvalue, so trace zero forces the eigenvalue multiset \((2a,-a,-a)\) with \(a\ne0\), equivalent to a rotated zonal quadratic. Equality \(\delta=0\) forces \(T=3\det A=0\), yielding \((a,0,-a)\). Both shapes exist. Strict monotonicity therefore proves both sharp real inequalities and exhausts the real equality cases.

**4. Complex upper inequality and its rigidity.** Write any complex degree-two harmonic \(F=U+iV\) with real degree-two harmonics \(U,V\). Since \(m>1\), the triangle inequality in \(L^m\), together with the real upper bound, yields
\[
\begin{aligned}
\|F\|_{2m}^2
&=\|U^2+V^2\|_{L^m}
\le\|U^2\|_{L^m}+\|V^2\|_{L^m}\\
&=\|U\|_{2m}^2+\|V\|_{2m}^2
\le R_m(1)^{1/m}\bigl(\|U\|_2^2+\|V\|_2^2\bigr)\\
&=R_m(1)^{1/m}\|F\|_2^2.
\end{aligned}
\]
Raising to the power \(m\) proves the upper inequality. Equality requires every nonzero real component to be zonal and equality in the strict \(L^m\) triangle inequality. In particular \(U^2\) and \(V^2\) are proportional almost everywhere (unless a component vanishes). By continuity and quadratic homogeneity, \(U^2=cV^2\) as polynomials on \(\mathbb R^3\). Factorization in the real polynomial ring gives \(U=\pm\sqrt c\,V\). Thus \(F\) is a global complex scalar multiple of one real zonal harmonic. Conversely each such multiple attains equality.

**5. Sixth moment, quartic degeneracy, and stability.** Evaluating the finite polynomial at \(m=2\) gives \(R_2=15/7\); at \(m=3\) gives \(R_3(z)=(5625+1000z)/1001\). The displayed exact deficit and constants follow. Because \(\delta=1\) characterizes uniaxiality, the deficit vanishes exactly at the described real maximizing orbit.

## Verification

The standalone standard-library file `verify_even_moments.py` performs 291 exact rational assertions. It independently integrates even monomials on the sphere for five distinct real traceless diagonal matrices through the twentieth power, checks the normalized Legendre-zonal moments for the first thirteen even-moment orders, checks the coefficient polynomial and strict interior inequalities through order nineteen, tests several genuinely complex quadratics, and checks sharpness representatives for orders three through ten. `VERIFICATION_OUTPUT.txt` records a successful execution. These finite checks corroborate the formulas; the generating-function, discriminant, and Minkowski arguments above are the proofs for all indicated orders and all admissible harmonics.

## Relationship to prior work

The sharp degree-two \(L^4/L^2\) inequality and complex extremizer classification is previously established in the published record listed below as published-finding corpus `2026/9/20/SCOPE-sharp-l4-degree-two-spherical-harmonics--d4106097159f`. Its theorem concerns the fourth moment; on \(S^2\), every real degree-two harmonic is quartically extremal. The present statement starts from that exact degeneracy and determines every higher even moment, the first strict distinction at the sixth moment, both sharp real endpoints, and the complex upper equality class; these are not consequences of the fourth-moment statement. Kwon–Lee's 2017 projection bounds, Dai–Feng–Tikhonov's reverse Hölder estimates and Dai–Gorbachev–Tikhonov's 2019 lacunary Nikolskii bounds concern general/asymptotic degree dependence, not this finite-degree-two invariant polynomial or extremizers. Classical Gaussian quadratic-form moment expansions supply the proof mechanism but do not alone settle the extremal ordering or complex rigidity.

## Limitations

The results are established only on \(S^2\), for exactly degree-two harmonics and integer even powers. The complex result is an upper bound and equality classification only. No estimate for non-even exponents, noise stability in an external inverse problem, or higher harmonic degrees is inferred. Earlier invariant-theory and Gaussian-quadratic-form literature could contain equivalent higher-moment statements under different terminology; mathematical priority is not independently established.

## References

1. Yehyun Kwon and Sanghyuk Lee, “Sharp \(L^p\)–\(L^q\) estimates for the spherical harmonic projection,” arXiv:1709.09795, first posted 2017-09-28. https://arxiv.org/abs/1709.09795
2. Feng Dai, Dmitry Gorbachev and Sergey Tikhonov, “Nikolskii inequality for lacunary spherical polynomials,” arXiv:1905.00323, first posted 2019-05-01. https://arxiv.org/abs/1905.00323
3. Feng Dai, Han Feng and Sergey Tikhonov, “Reverse Hölder's inequality for spherical harmonics,” arXiv:1408.1877, first posted 2014-08-06. https://arxiv.org/abs/1408.1877
4. “Sharp L4/L2 norm and extremizers for degree-two spherical harmonics,” published-finding corpus mathematical record, 2026-09-20. https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-sharp-l4-degree-two-spherical-harmonics--d4106097159f
5. R. J. Stanton and A. Weinstein, “On the L4 norm of spherical harmonics,” *Mathematical Proceedings of the Cambridge Philosophical Society* **89** (1981), 343–358. https://doi.org/10.1017/S0305004100058229
