# A quantitative affine-orbit region for the regular dodecagon Fourier-zero problem
## Finding
Let \(P_{12}\subset\mathbb{R}^2\) be the regular dodecagon of area \(\pi\), centred at the origin. For a bounded balanced set \(K\), write
\[
\kappa(K)=\operatorname{dist}\bigl(0,\mathcal{N}(K)\bigr),
\]
where \(\mathcal{N}(K)\) is the real zero set of the Fourier transform of \(\chi_K\).

Let \(A\in SL(2,\mathbb{R})\) and put \(s=\sigma_{\max}(A)\ge1\). Then
\[
\frac{\kappa(AP_{12})}{\kappa(P_{12})}
\le
\left(
 s^2\sin^2\!\frac{\pi}{12}+s^{-2}\cos^2\!\frac{\pi}{12}
\right)^{1/2}.
\]
Consequently, if
\[
1<s<2+\sqrt3,
\]
then
\[
\kappa(AP_{12})<\kappa(P_{12}).
\]
Since \(\det A=1\), the spectral condition number satisfies \(\operatorname{cond}_2(A)=s^2\). Thus the strict region is equivalently
\[
1<\operatorname{cond}_2(A)<7+4\sqrt3.
\]
If \(s=1\), then \(A\) is a rotation and equality holds.

The numerical cutoff is exact for the particular certificate that uses only the twelve nearest Fourier zeros of the regular dodecagon. If the minor singular axis is placed halfway between two adjacent midpoint directions, the displayed upper bound is attained by that finite set of witnesses; at \(s=2+\sqrt3\) it equals one. This last statement concerns the strength of the finite-witness argument, not the true value of \(\kappa(AP_{12})\) beyond the cutoff.

## Assumptions and scope
The motivating source, Gómez-Serrano, Levitin, Platt and Polterovich, arXiv:2609.10517v1, proves that among regular centrally symmetric polygons the regular dodecagon has the largest \(\kappa\), and asks whether it maximises \(\kappa\) among all convex balanced planar domains of area \(\pi\). It also proves that for \(P_{12}\) the complete set of minimising directions consists of the side-midpoint directions.

The result here treats a substantial but restricted family inside that open problem: determinant-one linear images of \(P_{12}\). It does not settle the full affine orbit for arbitrarily large anisotropy, and it does not address non-affine perturbations or arbitrary convex balanced domains.

## Proof
Set \(P=P_{12}\), \(\kappa_0=\kappa(P)\), and \(B=A^{-T}\). Because \(\det A=1\), a change of variables gives
\[
\widehat{\chi_{AP}}(\xi)=\widehat{\chi_P}(A^T\xi).
\]
Therefore
\[
\mathcal{N}(AP)=B\,\mathcal{N}(P).
\]

For the regular dodecagon, Theorem 1.7 of arXiv:2609.10517v1 states that the minimising directions are exactly the twelve side-midpoint directions. After choosing the orientation so that one midpoint direction is horizontal, these are
\[
e_j=\bigl(\cos(j\pi/6),\sin(j\pi/6)\bigr),\qquad j=0,\ldots,11,
\]
and
\[
\kappa_0 e_j\in\mathcal{N}(P)
\]
for every \(j\). Hence
\[
\kappa(AP)\le \kappa_0\min_j |Be_j|.
\]

The singular values of \(B=A^{-T}\) are \(s\) and \(s^{-1}\). Let \(v\) be a unit vector on the minor singular axis, corresponding to singular value \(s^{-1}\). The six unoriented lines determined by the twelve vectors \(e_j\) are spaced by \(\pi/6\), so at least one of them makes an angle \(\theta\) with \(v\) satisfying
\[
0\le\theta\le\frac{\pi}{12}.
\]
For the corresponding \(e_j\), resolving into the minor and major singular directions gives
\[
|Be_j|^2=s^{-2}\cos^2\theta+s^2\sin^2\theta.
\]
For \(s\ge1\), this expression is nondecreasing on \([0,\pi/2]\) as a function of \(\theta\). Thus
\[
\min_j|Be_j|^2
\le
s^{-2}\cos^2\!\frac{\pi}{12}+s^2\sin^2\!\frac{\pi}{12},
\]
which proves the displayed bound.

It remains to identify exactly when that right-hand side is less than one. Put \(q=s^2\) and \(\delta=\pi/12\). Then
\[
q\left(q\sin^2\delta+q^{-1}\cos^2\delta-1\right)
=
\sin^2\delta\,(q-1)\left(q-\cot^2\delta\right).
\]
Since
\[
\cot\frac{\pi}{12}=2+\sqrt3,
\qquad
\cot^2\frac{\pi}{12}=7+4\sqrt3,
\]
the factor is negative exactly for
\[
1<q<7+4\sqrt3,
\]
or equivalently \(1<s<2+\sqrt3\). This proves strict decrease throughout the claimed anisotropy range.

Finally, choose the minor singular axis exactly halfway between two adjacent midpoint lines. Then every midpoint line is at angular distance at least \(\pi/12\) from the minor axis, and the two nearest lines have distance exactly \(\pi/12\). Therefore the minimum of \(|Be_j|\) over these twelve source zeros is exactly the displayed factor. At \(s=2+\sqrt3\), its square is one by the factorisation above. Hence the cutoff is sharp for this twelve-zero witness argument.

## Verification
The proof uses only three ingredients: Fourier covariance under a determinant-one linear map; the source theorem identifying all nearest-zero directions of the regular dodecagon; and an exact two-dimensional singular-value calculation. The trigonometric cutoff is checked by the explicit factorisation
\[
\sin^2\delta\,(q-1)(q-\cot^2\delta),
\qquad \delta=\frac{\pi}{12}.
\]
No numerical approximation is used in the theorem or cutoff.

## Relationship to prior work
ArXiv:2609.10517v1 proves that the regular dodecagon beats the disk, is best among regular centrally symmetric polygons, and poses the global planar maximisation problem. Its Theorem 1.7 identifies the twelve side-midpoint directions as exactly the minimising directions for \(P_{12}\). The paper does not discuss affine or determinant-one linear images; full-text searches for “affine”, “linear transformation”, and “SL(2” return no occurrence.

Targeted searches for an affine-orbit theorem, the exact constants \(2+\sqrt3\) and \(7+4\sqrt3\), and equivalent singular-value formulations did not locate a prior statement of this quantitative region. A nearby recent result on the same source concerns an explicit zero-free strip for the higher-dimensional bipyramid construction; it does not address planar affine images of the dodecagon.

## Limitations
The theorem gives a sufficient region, not a full classification of the affine orbit. When \(s\ge2+\sqrt3\), the finite set of twelve nearest source zeros no longer forces strict decrease for every orientation. Other, farther zeros of \(P_{12}\) may still force \(\kappa(AP_{12})<\kappa(P_{12})\); this proof does not decide that question.

The cutoff is therefore sharp only for the stated twelve-nearest-zero witness method. It is not claimed to be a sharp boundary for the true functional on the affine orbit.

## References
1. J. Gómez-Serrano, M. Levitin, D. Platt, I. Polterovich, “An isoperimetric problem for Fourier zeros of centrally symmetric convex bodies,” arXiv:2609.10517v1, submitted 9 September 2026. In particular, Open Problem 1.6 and Theorem 1.7.
