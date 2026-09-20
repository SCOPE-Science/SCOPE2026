# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The ellipse identity is an exact Plancherel computation. For \(E=x_0+AD\), the change of variables \(\zeta=A^T\xi\) makes the Fourier-energy density radial. The same-sign quadrant condition becomes
\[
(r_1\cdot\zeta)(r_2\cdot\zeta)>0,
\]
where \(r_1,r_2\) are the rows of \(A^{-T}\). If their angle is \(\alpha\), the angular same-sign fraction is exactly \(1-\alpha/\pi\). Multiplication by the squared defect multiplier \(4\) gives the stated formula. For the diagonal eccentric ellipse, direct computation gives
\[
\cos\alpha=(\varepsilon^2-1)/(\varepsilon^2+1),
\]
hence \(\alpha=\pi-2\arctan\varepsilon\).

The truncated-strip asymptotic follows from the source paper's exact bad-quadrant integral. The tail
\[
A(t)=\int_t^\infty \sin^2(p)p^{-2}\,dp
\]
satisfies \(A(t)=1/(2t)+O(t^{-2})\). The range \(1<t<1/\varepsilon\) therefore contributes
\[
(\varepsilon^2/2)\log(1/\varepsilon)+O(\varepsilon^2),
\]
while the two complementary ranges are \(O(\varepsilon^2)\). Tracking the source normalization, the two orthogonal bad quadrants, the multiplier factor \(4\), and \(|V_\varepsilon|=4\varepsilon\) yields
\[
\frac{\|(\mathbf H-I)\chi_{V_\varepsilon}\|_2^2}{\|\chi_{V_\varepsilon}\|_2^2}
=
\frac4{\pi^2}\varepsilon\log(1/\varepsilon)+O(\varepsilon).
\]
Boundary axes have Fourier measure zero and do not affect either computation.

Adversarial checks included both eigenvalue signs, the orientation of the rotated coordinates, the quadrant identity
\[
\xi_1\xi_2=(\eta_v^2-\eta_u^2)/2,
\]
and the affine Fourier Jacobian. No hidden smoothness assumption is used beyond the explicit ellipse geometry.

## Originality

**PASS, to the best of our knowledge.**

The full text of arXiv:2609.15155v1 was inspected at its main quasi-eigenvector construction. It gives the truncated-strip Fourier formula and proves only an upper estimate of order
\[
\sqrt{\varepsilon|\log\varepsilon|};
\]
it explicitly contrasts the logarithm with the dyadic model. Searches within that paper found no ellipse construction, strictly convex quasi-eigenvector family, exact all-ellipse defect formula, or matching lower/asymptotic statement for the strip.

External searches were performed for exact and synonymous formulations involving double/product Hilbert transforms, ellipses, characteristic functions, smooth or strictly convex approximate eigenvectors, quadrant Fourier mass, anisotropic ellipses, and sharp truncated-strip asymptotics. No source stating either the all-ellipse formula or the sharp strip asymptotic was found.

The current SCOPE archive was searched by the source identifier, double-Hilbert terminology, quasi-eigenvector terminology, ellipses, and truncated strips; no overlapping accepted record was found.

A potentially nearby older item, S. Patel, *Double Hilbert transform in R2*, Acta Sci. Math. (Szeged) 77 (2011), 503–511, DOI 10.1007/BF03643931, was not available in full text from the inspected repository. Its accessible abstract states a different problem: \(L^p\) boundedness of polynomial-surface double Hilbert transforms. The abstract and bibliographic metadata were inspected; nothing there suggests indicator quasi-eigenvectors or ellipse Fourier leakage. It is therefore a low, not material, originality risk. No inaccessible source was identified as plausibly containing the present claim.

Residual risk remains because arXiv:2609.15155 is very recent and the ellipse calculation is short once the quadrant multiplier is viewed through affine radial Fourier energy; an unindexed concurrent observation or folklore remark is possible.

## Value

**PASS.**

The result changes the quantitative interpretation of the new bounded-indicator quasi-eigenvector phenomenon. The recent continuous construction exhibits a logarithmic loss and is explicitly compared with a log-free dyadic model. The new exact ellipse family shows that the continuous operator itself also admits log-free bounded, smooth, strictly convex indicator quasi-eigenvectors. At the same time, the matching strip asymptotic proves that the logarithm in the published construction is genuine for that geometry rather than merely an artifact of a loose estimate.

The all-ellipse formula is scale-free and exact, and it identifies a simple geometric parameter—the angle between the rows of the inverse-transpose affine map—that completely determines the two \(L^2\) eigen-defects for affine disks.

## Limitations

No claim is made that ellipses optimize the defect under a fixed eccentricity or any other geometric constraint, nor that \(\sqrt\varepsilon\) is a universal optimal rate. The analysis is restricted to \(L^2(\mathbb R^2)\) for the standard double Hilbert transform. It does not provide a sharp quantitative consequence for product-BMO commutators. The strip lower asymptotic applies only to the specific truncated strip used in arXiv:2609.15155v1.

## Sources inspected

- E. Abakumov, K. Domelevo, S. Petermichl, A. Poltoratski, *Invariant sets of the double Hilbert transform*, arXiv:2609.15155v1.
- S. Patel, *Double Hilbert transform in R2*, Acta Sci. Math. (Szeged) 77 (2011), 503–511, DOI 10.1007/BF03643931: abstract and bibliographic metadata inspected; full text not inspected.
- C. Fefferman, *Estimates for a double Hilbert transform*, Studia Math. 44 (1972), 1–15, as background for the classical operator.
