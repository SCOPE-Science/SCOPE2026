# Exact Fourier-defect identity and sharp stability for threefold projection symmetry

## Finding

Let \(d\sigma\) be probability area measure on \(S^2\), let \(dR\) be probability Haar measure on \(SO(3)\), and let \(f:S^2\to\mathbb R\) be continuous. Write its spherical-harmonic expansion as \(f=\sum_{\ell\ge0}H_\ell\), with \(H_\ell\) of degree \(\ell\). For \(R\in SO(3)\), define

\[
\widehat f_R(k)=\frac1{2\pi}\int_0^{2\pi}f\bigl(R(\cos\theta,\sin\theta,0)\bigr)e^{-ik\theta}\,d\theta.
\]

For every integer \(k\ge0\), the exact identity is

\[
\mathcal E_k(f):=\int_{SO(3)}|\widehat f_R(k)|^2\,dR
=\sum_{\substack{\ell\ge k\\\ell\equiv k\pmod 2}}\gamma_{\ell,k}\|H_\ell\|_2^2,
\qquad
\gamma_{\ell,k}=\frac{\binom{\ell+k}{(\ell+k)/2}\binom{\ell-k}{(\ell-k)/2}}{2^{2\ell}}.
\]

The binomial entries are integers because the sum is restricted to \(\ell\equiv k\pmod 2\). In particular,

\[
\mathcal E_2(f)+\mathcal E_5(f)
=\sum_{\substack{\ell\ge2\\\ell\text{ even}}}\gamma_{\ell,2}\|H_\ell\|_2^2
+\sum_{\substack{\ell\ge5\\\ell\text{ odd}}}\gamma_{\ell,5}\|H_\ell\|_2^2.
\]

Thus there are absolute constants \(0<c<C<\infty\) such that

\[
c\|f-H_0-H_1-H_3\|_{H^{-1/2}(S^2)}^2
\le \mathcal E_2(f)+\mathcal E_5(f)
\le C\|f-H_0-H_1-H_3\|_{H^{-1/2}(S^2)}^2.
\]

The exponent is sharp: no uniform lower bound of this kind holds with \(H^{-s}\) replacing \(H^{-1/2}\) for any \(s<1/2\).

For a convex body \(K\subset\mathbb R^3\), the support function of its planar projection onto \(P\) is the restriction of \(h_K\) to \(P\cap S^2\). Translation changes only Fourier modes \(\pm1\), so the mode-two and mode-five energies are translation-invariant measurements of projection asymmetry. Their joint vanishing is equivalent to \(h_K=H_0+H_1+H_3\); each great-circle restriction then contains only modes \(0,\pm1,\pm3\), and each planar projection is threefold rotationally symmetric after a translation.

## Assumptions and scope

All norms \(\|H_\ell\|_2\) use probability area measure on \(S^2\). The Sobolev scale is normalized by \(\|g\|_{H^{-s}(S^2)}^2=\sum_{\ell\ge0}(1+\ell(\ell+1))^{-s}\|H_\ell(g)\|_2^2\) for \(s\ge0\). The Haar measure on \(SO(3)\) is normalized to total mass one. The theorem is stated for continuous functions so the circle integrals are pointwise defined; the spectral identity extends by boundedness to the corresponding \(L^2\) measurement operator. The geometric interpretation concerns support functions of convex bodies in \(\mathbb R^3\). No uniform or Hausdorff-distance estimate is asserted.

## Proof

Choose complex spherical harmonics \(Y_{\ell m}\), orthonormal for \(d\sigma\), and expand \(H_\ell=\sum_{m=-\ell}^{\ell}a_mY_{\ell m}\). On the equator, the \(k\)-th Fourier coefficient of \(Y_{\ell m}\) vanishes unless \(m=k\) and \(\ell-k\) is even. For the nonzero case, the normalized associated-Legendre formula gives an equatorial coefficient \(c_{\ell k}\) with

\[
|c_{\ell k}|^2=(2\ell+1)\frac{(\ell-k)!}{(\ell+k)!}
\left(\frac{(\ell+k-1)!!}{(\ell-k)!!}\right)^2.
\]

Equivalently, \(|c_{\ell k}|^2/(2\ell+1)=\gamma_{\ell,k}\), with \(\gamma_{\ell,k}\) as above. Rotating \(H_\ell\) acts by the irreducible degree-\(\ell\) representation of \(SO(3)\). Schur orthogonality gives

\[
\int_{SO(3)}|\widehat{(H_\ell)}_R(k)|^2\,dR
=\gamma_{\ell,k}\sum_{m=-\ell}^{\ell}|a_m|^2.
\]

The same orthogonality makes cross terms between distinct degrees vanish. Summing over \(\ell\) proves the exact identity, first for finite harmonic sums and then for continuous \(f\) by continuity of the operator \(T_kf(R)=\widehat f_R(k)\). Indeed, Jensen's inequality and Haar invariance give \(\int_{SO(3)}|T_kf(R)|^2\,dR\le\int_{S^2}|f(u)|^2\,d\sigma(u)\), so \(T_k:L^2(S^2)\to L^2(SO(3))\) is a contraction.

For fixed \(k\) and matching parity, the central-binomial asymptotic gives

\[
\gamma_{\ell,k}\sim\frac{2}{\pi\ell}\qquad(\ell\to\infty).
\]

The mode \(k=2\) detects every even degree \(\ell\ge2\), and the mode \(k=5\) detects every odd degree \(\ell\ge5\). These are exactly the degrees outside \(\{0,1,3\}\). Since \((1+\ell(\ell+1))^{-1/2}\asymp(1+\ell)^{-1}\), the displayed two-sided \(H^{-1/2}\) estimate follows: each relevant coefficient is positive, and its ratio to the Sobolev weight tends to \(2/\pi\), leaving only finitely many positive ratios to check. For sharpness, take a unit \(L^2\)-norm harmonic of even degree \(\ell\to\infty\). Its mode-two energy is asymptotic to \(2/(\pi\ell)\), while its squared \(H^{-s}\) norm is asymptotic to \(\ell^{-2s}\). Their ratio tends to zero whenever \(s<1/2\), ruling out a uniform lower bound in any stronger such norm.

For support functions, \(h_{K|P}=h_K|_{P\cap S^2}\). A translation adds a linear function on the circle, which has only modes \(\pm1\). Hence the mode-two and mode-five coefficients are translation-invariant. If both energies vanish, the exact identity forces every harmonic component outside degrees \(0,1,3\) to vanish. A degree-three spherical harmonic restricts to any great circle with frequencies only \(1\) and \(3\), so after removing the degree-one translation each projected support function is threefold rotationally invariant. Conversely, threefold rotational symmetry up to translation eliminates circle frequencies two and five, so both energies vanish.

## Verification

The coefficient formula gives \(\gamma_{2,2}=3/8\), \(\gamma_{4,2}=5/32\), and \(\gamma_{5,5}=63/256\). These values follow directly from the binomial expression and provide low-degree normalization checks. The large-degree asymptotic follows from \(\binom{2m}{m}/4^m\sim(\pi m)^{-1/2}\). The proof is analytic and does not rely on finite enumeration or numerical experiments. The optimality test uses a single normalized harmonic in each even degree tending to infinity.

## Relationship to prior work

Myroshnychenko, Ryabogin, and Saroglou prove qualitative rigidity for convex bodies whose planar projections have rotational symmetry of order at least four, and construct non-spherical constant-width examples in the threefold case. Their harmonic analysis includes the fact that a nonzero degree-\(\ell\) spherical harmonic exhibits every parity-compatible Fourier frequency on some great circle. The present claim does not claim novelty for the qualitative zero-set classification that follows from that lemma. It adds the exact Haar-averaged mode-energy identity, its central-binomial weights, the two-sided \(H^{-1/2}\) stability estimate, and the optimality of that Sobolev exponent.

## Limitations

The estimate controls a negative Sobolev norm, not the uniform norm, Hausdorff distance, or curvature. Additional regularity assumptions would be needed to infer a stronger geometric metric. The proof is for \(S^2\), corresponding to bodies in \(\mathbb R^3\); higher-dimensional analogues require a separate normalization and representation calculation. The qualitative source result is used as motivation and as a comparison point, not as evidence that the quantitative identity was previously published.

## References

- S. Myroshnychenko, D. Ryabogin, and C. Saroglou, “On convex bodies with rotationally symmetric planar projections,” arXiv:2609.27192, first submitted 23 September 2026. https://arxiv.org/abs/2609.27192
