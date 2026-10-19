# An all-even-moment shape ordering for real degree-two spherical harmonics

## Finding

Let \(\mu\) be normalized surface measure on \(\mathbb S^2\) and let \(Y_A(\omega)=\omega^{\mathsf T}A\omega\) for a nonzero real symmetric traceless \(3\times3\) matrix \(A\). Put
\[
s_2=\operatorname{tr}(A^2)>0,\qquad
\nu(A)=\frac{\det(A)^2}{s_2^3}.
\]
For every integer \(m\ge1\), its normalized even moment is the explicitly positive-coefficient polynomial
\[
\frac{\int_{\mathbb S^2}|Y_A|^{2m}\,d\mu}
{\left(\int_{\mathbb S^2}|Y_A|^2\,d\mu\right)^m}
=\mathcal P_m(\nu(A)),
\]
where
\[
\mathcal P_m(u)=
\frac{(2m)!}{(4m+1)!!}\left(\frac{15}{2}\right)^m
\sum_{j=0}^{\lfloor m/3\rfloor}
\frac{(1/2)_{m-j}\,2^{m-3j}\,64^j}{(m-3j)!(2j)!}\,u^j.
\tag{1}
\]
Here \((a)_k=a(a+1)\cdots(a+k-1)\), with \((a)_0=1\), and \((2r+1)!!=1\cdot3\cdots(2r+1)\).

The shape invariant has the **sharp range**
\[
0\le\nu(A)\le\frac1{54}.
\tag{2}
\]
The first two normalized even-moment quotients, \(\mathcal P_1=1\) and \(\mathcal P_2=15/7\), do not distinguish real harmonic shapes. In contrast, **for every integer \(m\ge3\)** the polynomial \(\mathcal P_m\) is strictly increasing on the entire interval in (2). Consequently
\[
\boxed{\ \mathcal P_m(0)\le
\frac{\|Y_A\|_{L^{2m}(\mu)}^{2m}}
{\|Y_A\|_{L^2(\mu)}^{2m}}
\le\mathcal P_m(1/54).\ }
\tag{3}
\]
For \(m\ge3\), equality on the left holds precisely when the spectrum of \(A\) is \(\{t,0,-t\}\), for some \(t\ne0\). Equality on the right holds precisely when its spectrum is \(\{2t,-t,-t\}\), for some \(t\ne0\). These correspond, respectively, to real sectoral and zonal degree-two harmonics, up to nonzero scale and rotation. Both endpoints are attained.

In particular the sharp sixth-moment bounds are
\[
\boxed{\ \frac{5625}{1001}\le
\frac{\|Y_A\|_{L^6(\mu)}^{6}}{\|Y_A\|_{L^2(\mu)}^{6}}
\le\frac{6625}{1001}.\ }
\tag{4}
\]
Every intermediate value of \(\nu(A)\) and hence of the normalized moment ratio occurs. Thus degree two is the first real spherical-harmonic degree in which the even moments \(2m\ge6\) distinguish two noncongruent fixed-\(L^2\) shapes while the fourth moment does not.

## Assumptions and scope

All matrices are **real symmetric and traceless**. Every nonzero such matrix gives a real degree-two Laplace--Beltrami eigenfunction on \(\mathbb S^2\). The norm is with respect to **probability-normalized surface measure**, not unnormalized area. All exponent statements require an integer \(m\ge1\); sharp strict ordering and equality classification require \(m\ge3\). Rotations may be chosen in \(SO(3)\) because a permutation/sign adjustment of an eigenbasis can be made orientation-preserving. No sharp claim is made for complex-valued harmonics at exponents greater than four, for non-even exponents, or in other sphere dimensions.

## Proof

### 1. The Gaussian generating function

Write \(G=R\omega\), where \(G\) is a standard Gaussian vector in \(\mathbb R^3\), \(R=\|G\|_2\), and \(\omega\) is independent of \(R\) and distributed according to \(\mu\). Since \(\mathbb E R^{4m}=(4m+1)!!\),
\[
\mathbb E(\omega^{\mathsf T}A\omega)^{2m}
=\frac{\mathbb E(G^{\mathsf T}AG)^{2m}}{(4m+1)!!}.
\tag{5}
\]
Because \(A\) is real symmetric, diagonalization and the Gaussian square MGF give, for all \(t\) sufficiently close to zero,
\[
\mathbb E e^{tG^{\mathsf T}AG}
=\prod_{i=1}^3(1-2t\lambda_i)^{-1/2}
=\bigl(1-2s_2t^2-8\det(A)t^3\bigr)^{-1/2}.
\tag{6}
\]
The second identity uses \(\sum_i\lambda_i=0\), \(\sum_{i<j}\lambda_i\lambda_j=-s_2/2\), and \(\lambda_1\lambda_2\lambda_3=\det A\). Equation (6) holds analytically near zero (hence also coefficientwise as a formal series).

Expanding \((1-z)^{-1/2}=\sum_{k\ge0}(1/2)_k z^k/k!\), the coefficient of \(t^{2m}\) selects \(2j\) cubic factors and \(m-3j\) quadratic factors, for exactly \(0\le j\le\lfloor m/3\rfloor\). Therefore
\[
\mathbb E(\omega^{\mathsf T}A\omega)^{2m}
=\frac{(2m)!}{(4m+1)!!}
\sum_{j=0}^{\lfloor m/3\rfloor}
\frac{(1/2)_{m-j}}{(m-3j)!(2j)!}
(2s_2)^{m-3j}(8\det A)^{2j}.
\tag{7}
\]
The case \(m=1\) gives \(\int |Y_A|^2\,d\mu=2s_2/15\). Dividing (7) by \((2s_2/15)^m\) and grouping the matrix invariants into \(\nu(A)\) proves (1). This coefficient extraction is exact for **every** integer \(m\), not an experimentally inferred pattern.

### 2. Sharp admissible shape interval

The eigenvalues are real roots of
\[
z^3-\frac{s_2}{2}z-\det A=0.
\]
Its discriminant is
\[
\prod_{i<j}(\lambda_i-\lambda_j)^2
=\frac{s_2^3}{2}-27(\det A)^2
=\frac{s_2^3}{2}\bigl(1-54\nu(A)\bigr)\ge0.
\tag{8}
\]
Hence (2) holds. The left endpoint means \(\det A=0\), which together with zero trace and \(A\ne0\) forces the eigenvalues \(\{t,0,-t\}\). The right endpoint means vanishing discriminant, so two eigenvalues coincide; trace zero forces \(\{2t,-t,-t\}\). Continuous rotation-invariant paths in the unit-squared-trace eigenvalue circle connect these shapes, so all intermediate values are attained.

### 3. Strict all-even-moment ordering

Each summand coefficient of (1) is strictly positive for all allowed \(m,j\). For \(m=1,2\), only \(j=0\) appears; simplifying gives \(\mathcal P_1=1\) and \(\mathcal P_2=15/7\). For every \(m\ge3\), the term \(j=1\) appears with strictly positive coefficient. Consequently \(\mathcal P_m'(u)>0\) for every \(u\in[0,1/54]\), including both endpoints. Combine this observation with (8) for the sharp bounds and all equality cases (3).

At \(m=3\), exact rational simplification yields
\[
\mathcal P_3(u)=\frac{5625}{1001}+\frac{54000}{1001}u,
\]
so its values at \(0\) and \(1/54\) are exactly those in (4). This completes the proof.

## Verification

The standalone `checker.py` (Python standard library only) checks the normalized polynomial coefficients exactly through \(m=10\), and independently computes spherical moments by multinomial integration for seven traceless eigenvalue triples through \(m=9\). It also verifies both sharp sixth-moment configurations and the eigenvalue discriminant identity in 288 small-integer configurations. The 368 reported checks used exact rational arithmetic. The general mathematical assertions for all \(m\) follow from (5)--(8) and the positive-coefficient argument, **not** from finite enumeration.

Run `python3 checker.py`; the accompanying `checker_output.txt` records the expected output.

## Relationship to prior work

Speckbacher and Hrycak (arXiv:1909.01670, first posted September 4, 2019) analyze concentration of band-limited spherical harmonic expansions through large-sieve bounds, not these exact pure-degree-two moment-shape identities. Beiner and Verreault (arXiv:2209.00212, first posted September 1, 2022) study positive/negative \(L^p\)-mass asymmetry for sequences of high-degree zonal harmonics, a different quantification.

The published result **“Sharp L4/L2 norm and extremizers for degree-two spherical harmonics”** (published-finding corpus, September 20, 2026, identifier `SCOPE-sharp-l4-degree-two-spherical-harmonics--d4106097159f`) proves the full fourth-power sharp bound, including the fact that all **real** degree-two spherical harmonics on \(\mathbb S^2\) share the same fourth-moment ratio. That prior result **covers** the \(m=2\) case of the present formula, which is included here solely as a boundary comparison; it neither states nor implies the strict sixth-and-higher shape ordering (3) from the fourth-moment assertion. The new claims are (1) for every even order, (3) for all \(m\ge3\), and the sharp sixth-order interval and equality classification.

Older work on spherical harmonic norm growth and extremizers, including Stanton--Weinstein and Sogge, provides context but not the explicit determinant-resolved degree-two all-even moment statement in the portions checked.

## Limitations

The inequalities are for **real** degree-two harmonics on the 2-sphere and integral even powers only. They do not settle sharp sixth-moment norms for the full **complex** degree-two space, noninteger powers, higher harmonic degrees or higher-dimensional spheres. The literature comparison is a best-knowledge originality assessment rather than a universal proof of priority. Equivalent Gaussian quadratic-form moment formulas or invariant-theoretic expressions may exist in older literature. No separate independent mathematical audit has been performed.

## References

1. Michael Speckbacher and Tomasz Hrycak, “Concentration estimates for band-limited spherical harmonics expansions via the large sieve principle,” arXiv:1909.01670, first public version September 4, 2019, https://arxiv.org/abs/1909.01670 .
2. Gabriel Beiner and William Verreault, “Failure of \(L^p\) symmetry of zonal spherical harmonics,” arXiv:2209.00212, first public version September 1, 2022, https://arxiv.org/abs/2209.00212 .
3. “Sharp L4/L2 norm and extremizers for degree-two spherical harmonics,” published September 20, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/9/20/SCOPE-sharp-l4-degree-two-spherical-harmonics--d4106097159f/RESULT.md .
4. R. J. Stanton and A. Weinstein, “On the L4 norm of spherical harmonics,” Math. Proc. Cambridge Philos. Soc. 89 (1981), 343--358, https://doi.org/10.1017/S0305004100058229 .
5. C. D. Sogge, “Oscillatory integrals and spherical harmonics,” Duke Math. J. 53 (1986), 43--65, https://doi.org/10.1215/S0012-7094-86-05303-2 .
