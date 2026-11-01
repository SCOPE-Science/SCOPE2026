# Sharp half-order stability from two great-circle Fourier modes

## Finding

Let \(\sigma\) denote probability area measure on \(S^2\), and let \(dg\) denote probability Haar measure on \(SO(3)\). Put \(u(\theta)=(\cos\theta,\sin\theta,0)\). For \(f\in L^2(S^2,d\sigma)\) and \(m\in\{2,3\}\), the measurable, almost-everywhere-defined equatorial Fourier observation is
\[
c_m(g;f)=\frac{1}{2\pi}\int_0^{2\pi}f(gu(\theta))e^{-im\theta}\,d\theta.
\]
Define \(E(f)=\int_{SO(3)}(|c_2(g;f)|^2+|c_3(g;f)|^2)\,dg\). Let \(f_\ell=\Pi_\ell f\) be the orthogonal degree-\(\ell\) spherical-harmonic component, and define the half-order shape distance
\[
D(f)^2=\sum_{\ell=2}^{\infty}\frac{\|f_\ell\|_{L^2(\sigma)}^2}{\ell+1}.
\]
For integers \(k\ge1\), set \(a_k=4^{-k}\binom{2k}{k}\),
\[
\lambda_{2k}=\frac{2k(2k+1)}{(2k-1)(2k+2)}a_k^2,
\qquad
\lambda_{2k+1}=\frac{2k(2k+1)(2k+3)}{(2k-1)(2k+2)(2k+4)}a_k^2.
\]
**Theorem.** For every complex-valued \(f\in L^2(S^2,d\sigma)\),
\[
\boxed{E(f)=\sum_{k\ge1}\lambda_{2k}\|f_{2k}\|_2^2+\sum_{k\ge1}\lambda_{2k+1}\|f_{2k+1}\|_2^2\ \ge\ \frac2\pi D(f)^2.}
\]
Equality in the inequality holds exactly when \(f=f_0+f_1\) almost everywhere. The constant \(2/\pi\) is sharp but is not attained by any \(f\) having a nonzero spherical-harmonic component of degree at least two.

The exponent is also sharp: there is no positive constant that bounds \(E(f)\) below by the squared spherical Sobolev distance \(\sum_{\ell\ge2}(1+\ell(\ell+1))^s\|f_\ell\|_2^2\) for any \(s>-1/2\), even for support functions of smooth strictly convex bodies arbitrarily close to balls.

**Geometric consequence.** If \(h_K\) is the support function of a full-dimensional convex body \(K\subset\mathbb R^3\), then \(h_K\) restricted to the normal circle of any plane is exactly the support function of that plane's orthogonal projection of \(K\). The observation \(E(h_K)\) is invariant under translations of \(K\), and its sharp lower bound controls the half-order distance from \(h_K\) to its degree-zero-and-one part, which is the support function of a translated Euclidean ball. In particular, \(E(h_K)=0\) if and only if \(K\) is a Euclidean ball up to translation.

## Assumptions and scope

All integrals are normalized as above, with **one positive Fourier order** for each of orders \(2\) and \(3\), not a sum over both signed orders. These conventions determine the sharp constant. The function may be complex and merely square integrable: a representative need not restrict pointwise to every fixed circle, but Fubini's theorem defines its restriction and the coefficients for almost every rotated circle. Convex-body applications concern continuous real support functions and hence have no such qualification. The degree-one term \(a\cdot u\) represents translation and the degree-zero term \(r\) the radius of a Euclidean ball. The theorem concerns the sphere in dimension three only.

## Proof

**1. Bounded observations.** Invariance of Haar measure and Jensen's inequality give
\[
\int_{SO(3)}|c_m(g;f)|^2\,dg\le\int_{SO(3)}\frac{1}{2\pi}\int_0^{2\pi}|f(gu(\theta))|^2\,d\theta\,dg=\|f\|_2^2.
\]
Thus each measurement extends continuously to all \(L^2(S^2)\), and it suffices to compute on finite harmonic sums.

**2. Exact spectral diagonalization.** Fix an orthonormal spherical-harmonic basis in normalized spherical measure. On the reference equator, the basis harmonic of degree \(\ell\) and azimuthal order \(m\) has Fourier coefficient
\[
b_{\ell m}=\sqrt{(2\ell+1)\frac{(\ell-m)!}{(\ell+m)!}}\,P_\ell^m(0).
\]
The coefficient vanishes when \(m>\ell\) or \(\ell-m\) is odd. Schur orthogonality of the irreducible \(SO(3)\)-harmonic representations, including orthogonality between different degrees, yields
\[
\int_{SO(3)}|c_m(g;f)|^2\,dg
=\sum_{\substack{\ell\ge m\\\ell\equiv m\pmod2}}
\frac{(\ell-m)!}{(\ell+m)!}|P_\ell^m(0)|^2\|f_\ell\|_2^2.
\]
Only order \(2\) occurs at even degrees, and only order \(3\) occurs at odd degrees at least three; both vanish on degrees zero and one. The normalization follows from integrating the squared Wigner matrix entries to \(1/(2\ell+1)\), canceling the factor \(2\ell+1\) in \(|b_{\ell m}|^2\).

**3. Closed coefficients.** Legendre's differential equation implies \(P_{2k}(0)=(-1)^ka_k\) and
\[
|P_{2k}^{2}(0)|=2k(2k+1)a_k.
\]
For odd degree, \(|P_{2k+1}'(0)|=(2k+1)a_k\); differentiating Legendre's equation at zero gives
\[
|P_{2k+1}^{3}(0)|=2k(2k+3)(2k+1)a_k.
\]
Substitution into the factorial prefactors in the preceding identity gives the two displayed rational formulas for \(\lambda_{2k}\) and \(\lambda_{2k+1}\), with no limits or approximations.

**4. Sharp Wallis bound.** Put \(W_k=(2k+1)a_k^2\). The central binomial recurrence gives the exact identity
\[
\frac{W_{k+1}}{W_k}=1-\frac1{(2k+2)^2}<1,
\qquad \lim_{k\to\infty}W_k=\frac2\pi.
\]
The limit is Wallis's classical product (or follows from the central binomial asymptotic). Further,
\[
(2k+1)\lambda_{2k}=W_k\left(1+\frac{2}{(2k-1)(2k+2)}\right)>W_k,
\]
\[
(2k+2)\lambda_{2k+1}=W_k\left(1+\frac{4}{(2k-1)(2k+4)}\right)>W_k.
\]
Hence \((\ell+1)\lambda_\ell>2/\pi\) for every \(\ell\ge2\). The inequality and its equality characterization follow by summing nonnegative terms. Conversely, \((\ell+1)\lambda_\ell\to2/\pi\) along both parities, so no larger constant is possible.

**5. Convex support functions and optimal loss.** Given a real spherical harmonic \(Y_\ell\) of any degree \(\ell\ge2\), the support perturbation \(h(u)=1+\varepsilon Y_\ell(u)\) defines a smooth strictly convex body for sufficiently small nonzero \(\varepsilon\), because \(\nabla^2_{S^2}h+h\operatorname{Id}\) remains positive definite. For this body, \(E(h)/D(h)^2=(\ell+1)\lambda_\ell\). Sending \(\ell\to\infty\) proves sharpness within the convex-body class, including even-degree centrally symmetric perturbations. The ratio of \(E(h)\) to a proposed squared \(H^s\) distance is of order \(\ell^{-1-2s}\), tending to zero whenever \(s>-1/2\). Thus the half-order loss cannot improve uniformly without additional regularity restrictions. Finally, every translation contributes only a degree-one harmonic, so does not change the observations or the shape distance.

## Verification

The standalone standard-library program `check_spectral_recovery.py` independently expands \(P_\ell(r\cos\theta)\) as a polynomial, extracts its azimuthal Fourier coefficient, integrates its square over uniformly random circle inclinations by **exact rational moments**, and compares it with the associated-Legendre and closed-eigenvalue formulas. It verifies all \(2\le\ell\le22\) and orders \(2,3\), including the parity zeros. For \(1\le k\le500\) it also checks the exact rational Wallis recurrence and the strict rational comparison \((\ell+1)\lambda_\ell>W_k\) for both parities. It completed with `SPECTRAL_CHECK_OK: 1042 exact/finite checks; ell<=22 and k<=500`.

The finite checker confirms normalizations and algebra but does **not** certify the infinite harmonic decomposition, Wallis limit, or universal convexity claim; those follow from the preceding proof. The verification program has no nonstandard dependencies.

## Relationship to prior work

Myroshnychenko, Ryabogin and Saroglou (2026), Theorem 1.4, prove the **qualitative** statement that if the great-circle Fourier modes \(2\) and \(3\) vanish for every circle, a continuous function is constant plus linear. Their proof uses irreducible spherical harmonics, and supplies the natural motivating inverse problem. That zero-kernel conclusion is established prior work and is not claimed as new. The present result evaluates the entire squared observation operator and obtains the sharp, nonattained constant and optimal negative half-order stability under approximate—not necessarily vanishing—observations.

Hielscher, Potts and Quellmalz (2017) derive a singular-value decomposition for great-circle **arc-integral** tomography, where the spectrum involves sums across many azimuthal orders. Their associated-Legendre and Wigner-harmonic framework is directly relevant and supplies established machinery. The single-circle-order amplitudes used here are accessible from that machinery; the specifically selected joint orders \(2,3\), their sharp \(2/\pi\) weighted recovery inequality, optimal loss, and convex-body interpretation are the present targeted assertions rather than a claim of inventing the general harmonic transform. Kiderlen (2004) supplies stability for different averaged Minkowski-sums-of-projections data, not these two circle Fourier observations.

## Limitations

The result controls a negative half-order spherical-harmonic norm, not the ordinary Hausdorff distance, and it does not claim a universal \(L^2\) or stronger-Sobolev inverse estimate. The explicit best constant uses probability measures on both the sphere and the rotation group and one positive Fourier order for each degree. The proof is dimension-specific; no higher-dimensional sharp coefficient is asserted. Earlier SVD techniques make independent historical priority for portions of the spectral calculation uncertain. Independent mathematical audit has not been performed.

## References

- S. Myroshnychenko, D. Ryabogin and C. Saroglou, *On convex bodies with rotationally symmetric planar projections*, first public arXiv submission 2026-09-23, arXiv:2609.27192, Theorems 1.2–1.4 and §§4–5. https://arxiv.org/abs/2609.27192
- R. Hielscher, D. Potts and M. Quellmalz, *An SVD in Spherical Surface Wave Tomography*, arXiv:1706.05284 (2017), §3 and Theorem 3.3. https://arxiv.org/abs/1706.05284
- M. Kiderlen, *Determination of a convex body from Minkowski sums of its projections*, Journal of the London Mathematical Society 70 (2004), 529–544, DOI:10.1112/S0024610704005551. https://doi.org/10.1112/S0024610704005551
