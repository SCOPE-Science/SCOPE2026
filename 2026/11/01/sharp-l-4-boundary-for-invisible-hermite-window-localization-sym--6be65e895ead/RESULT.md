# Sharp \(L^4\) boundary for invisible Hermite-window localization symbols

## Finding

Let \(\mathcal F^2_{(k)}\) be the one-complex-variable true-polyanalytic Gaussian Fock space of order \(k\ge1\), using the standard normalization \(d\mu(z)=\pi^{-1}e^{-|z|^2}\,dA(z)\). For \(a\in L^\infty(\mathbb C)\), let \(T_{a,(k)}=P_{(k)}M_a\vert_{\mathcal F^2_{(k)}}\) denote Toeplitz localization. Lebesgue \(L^p\)-norms below are with respect to **unweighted planar area** \(dA\).

**Sharp injectivity threshold.** For every integer \(k\ge2\) and every \(1\le p\le4\),
\[
T_{a,(k)}=0,\quad a\in L^\infty(\mathbb C)\cap L^p(\mathbb C,dA)
\quad\Longrightarrow\quad a=0\ \text{a.e.}
\]
For every \(p>4\) and every \(k\ge2\), this implication fails: there exists a nonzero real-valued, smooth, bounded \(a\in L^p(\mathbb C,dA)\) with \(T_{a,(k)}=0\). At \(k=1\), quantization is injective on all of \(L^\infty\), independent of \(p\).

For an explicit witness at any \(k\ge2\), let \(\lambda>0\) be any zero of the ordinary Laguerre polynomial \(L_{k-1}\). Set
\[
a_\lambda(z)=J_0(2\sqrt\lambda\,|z|).
\]
Then \(T_{a_\lambda,(k)}=0\), and
\[
a_\lambda\in L^p(\mathbb C,dA)\quad\Longleftrightarrow\quad p>4
\qquad(1\le p<\infty).
\]
The sharp critical divergence has coefficient
\[
\int_{|z|\le R}|a_\lambda(z)|^4\,dA(z)
=\frac{3}{4\pi\lambda}\log R+O_\lambda(1)
\qquad(R\to\infty).
\]

## Assumptions and scope

The true-polyanalytic Fock projector and Toeplitz operators use the normalization of Fulsche--Hagger, *Quantum harmonic analysis for polyanalytic Fock spaces*, Section 3. There the symplectic form is \(\sigma(\xi,z)=2\operatorname{Im}(\xi\overline z)\). The Fourier transform \(\mathcal F_\sigma\) has this phase, and the ordinary Laplacian \(\Delta\) acts in its Fourier variables by multiplication with \(-4|\xi|^2\).

We only quantify over integer \(k\ge1\), real \(1\le p<\infty\), and bounded symbols additionally in unweighted \(L^p\). No assertion is made for arbitrary unbounded symbols whose Toeplitz compressions are not defined. The usual ordinary Laguerre polynomial is \(L_n(t)=\sum_{j=0}^{n}\binom nj(-t)^j/j!\).

## Proof

**1. Precise null-frequency reduction.** Proposition 3.2, Corollary 3.3 and Theorem 3.4 of Fulsche--Hagger give the Fourier--Weyl multiplier relation, valid for bounded symbols as tempered distributions:
\[
\mathcal F_W(\pi T_{a,(k)})(\xi)
=\exp(-|\xi|^2/2)L_{k-1}(|\xi|^2)
\,\mathcal F_\sigma a(\xi).
\]
The overall nonzero normalization does not affect vanishing. If \(T_{a,(k)}=0\), the distribution \(\mathcal F_\sigma a\) is supported on the finite disjoint union \(\bigcup_{j=1}^{k-1}\{\xi:|\xi|=\sqrt{\lambda_j}\}\), where \(\lambda_j\) are the positive simple roots of \(L_{k-1}\). For \(k=1\), this union is empty, so \(a=0\).

**2. Isolate each characteristic circle without losing integrability.** For \(k\ge2\), choose smooth compactly supported cutoffs \(\chi_j\) with disjoint annular supports, equal to one near the respective characteristic circles. They can be chosen so that \(\sum_j\chi_j=1\) near the entire Fourier support. Define \(u_j=\mathcal F_\sigma^{-1}(\chi_j\mathcal F_\sigma a)\). Because the inverse transform of \(\chi_j\) is a Schwartz convolution kernel, Young's inequality gives \(u_j\in L^p\) whenever \(a\in L^p\), including \(p=1\). Moreover \(a=\sum_j u_j\) in tempered distributions, and, since each localized Fourier distribution is supported on just one circle,
\[
(\Delta+4\lambda_j)u_j=0
\]
in the distributional sense. The characteristic roots are simple, so multiplying the original equation by the local reciprocal of the other Laguerre factors justifies this last relation even for distributions with possible transverse derivatives. Elliptic regularity makes every \(u_j\) smooth on the whole plane.

**3. An \(L^p\) obstruction for entire Helmholtz waves.** Suppose \(u\in L^p(\mathbb R^2)\), \(1\le p\le4\), satisfies \((\Delta+\kappa^2)u=0\) for some \(\kappa>0\). Its angular Fourier coefficients
\[
u_m(r)=\frac{1}{2\pi}\int_0^{2\pi}u(re^{i\theta})e^{-im\theta}\,d\theta
\]
solve the radial Bessel equation. Smoothness at the origin excludes the singular \(Y_{|m|}\) branch, giving \(u_m(r)=c_mJ_{|m|}(\kappa r)\) for each integer \(m\). Jensen's inequality implies
\[
2\pi\int_0^\infty |u_m(r)|^p r\,dr\le\|u\|_{L^p(\mathbb R^2)}^p.
\]
For each fixed order \(\nu\), the classical large-argument asymptotic
\[
J_\nu(\kappa r)=\sqrt{\frac{2}{\pi\kappa r}}
\left(\cos(\kappa r-\nu\pi/2-\pi/4)+O(r^{-1})\right)
\]
shows \(\int_1^\infty|J_\nu(\kappa r)|^pr\,dr=\infty\) for every \(p\le4\): restrict to a fixed positive fraction of each oscillation where the cosine modulus is bounded below. Therefore every \(c_m=0\). Completeness of angular Fourier series yields \(u=0\). Apply this to all \(u_j\) to deduce \(a=0\).

**4. Construction past the boundary and exact endpoint growth.** For a positive Laguerre root \(\lambda\), the plane-wave identity in Fulsche--Hagger Theorem 3.4 gives
\[
T_{\exp(i\sigma(\xi,\cdot)),(k)}=0
\quad\text{for every}\quad |\xi|=\sqrt\lambda.
\]
Average this bounded family over the circle. Since Toeplitz quantization is weak-* continuous, the average is still annihilated. The standard angular-integral representation of \(J_0\) identifies this average with \(a_\lambda(z)=J_0(2\sqrt\lambda|z|)\). It is nonzero since \(a_\lambda(0)=1\), smooth and bounded by one. Its large-radius asymptotic is of order \(|z|^{-1/2}\), and the oscillatory lower bound in Step 3 proves that its \(L^p\) membership is exactly \(p>4\).

At the endpoint, insert \(J_0(\kappa r)^4=4(\pi^2\kappa^2r^2)^{-1}\cos^4(\kappa r-\pi/4)+O(r^{-3})\), with \(\kappa=2\sqrt\lambda\), into \(2\pi\int_0^RrJ_0(\kappa r)^4dr\). The mean of \(\cos^4\) over one period is \(3/8\); its zero-mean periodic remainder has a bounded \(\int_1^R(\cdot)\,dr/r\). Thus the coefficient of \(\log R\) is \(3/(\pi\kappa^2)=3/(4\pi\lambda)\), as claimed.

## Verification

A standalone checker, `check_threshold.py`, evaluates roots and simplicity of Laguerre polynomials for degrees 1--11, checks the normalized angular Bessel identity at six radii, and tests the explicit \(L^4\) logarithmic slope on three independent annuli. It passed **153 deterministic assertions**. These finite numerical tests do not certify the all-degree or all-exponent theorem; its proof is Steps 1--4 above. Reproduce with `python check_threshold.py` with SciPy and NumPy installed.

## Relationship to prior work

The essential Fourier--Weyl multiplier identity, noninjectivity for unrestricted bounded symbols and characterization of null frequencies are **prior results**, specifically Fulsche--Hagger (2023 preprint; 2024 journal), Theorem 3.4. Their Proposition 3.8 proves injectivity on \(L^1\), but does not state an \(L^p\) threshold. The present conclusion supplies the precise critical value \(p=4\), the nonzero bounded \(L^p\) null symbols on the other side, and the endpoint logarithmic divergence. The proof uses classical Bessel asymptotics and two-dimensional Helmholtz separation; these are not claimed as new.

Keller--Luef (2019) develops polyanalytic Toeplitz symbolic calculus, including Hermite/Laguerre expansions, but does not provide the bounded-symbol \(L^p\) kernel phase transition in its symbol calculus statements. The cited 2022 work of Hagger discusses compactness/Fredholm phenomena rather than this sharp integrability obstruction. These comparisons do not constitute an exhaustive historical-priority guarantee.

## Limitations

The theorem is restricted to one complex dimension, the standard Gaussian normalization and **bounded** symbols; all \(L^p\) spaces here use unweighted plane area. It does not characterize every \(L^p\) null symbol for \(p>4\) or establish stable inverse estimates. A broader result might follow from general Helmholtz Fourier-restriction uniqueness theorems; independently verifying global historical priority remains open. The accompanying numerical checks are finite corroboration, not proof of the infinite statement. Independent mathematical verification has not been performed.

## References

1. R. Fulsche and R. Hagger, *Quantum harmonic analysis for polyanalytic Fock spaces*, arXiv:2308.11292 (first submitted 2023-08-22), especially Proposition 3.2, Theorem 3.4 and Proposition 3.8; https://arxiv.org/html/2308.11292v2 .
2. J. Keller and F. Luef, *Polyanalytic Toeplitz operators: isomorphisms, symbolic calculus and approximation of Weyl operators*, arXiv:1905.07741 (first submitted 2019-05-19); https://arxiv.org/html/1905.07741v2 .
3. R. Hagger, *Toeplitz and related operators on polyanalytic Fock spaces*, arXiv:2201.10230 (first submitted 2022-01-25); https://arxiv.org/abs/2201.10230 .
4. Classical Bessel asymptotics and the Jacobi--Anger integral representation: standard special-function identities, used explicitly in the proof.
