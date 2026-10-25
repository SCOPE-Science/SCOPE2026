# Distance statistics detect the half-twist of a flat Möbius band

## Finding

Fix any circumference \(C>0\) and strip width \(H>0\). Let \(\mathcal C_{C,H}\) be the flat cylinder obtained from \([0,C]\times[-H/2,H/2]\) by identifying \((0,y)\sim(C,y)\), and let \(\mathcal M_{C,H}\) be the flat Möbius band obtained instead by identifying \((0,y)\sim(C,-y)\). Both have the intrinsic length metric, area \(CH\), and total boundary length \(2C\). For two independent area-uniform points, write \(F_{\mathcal C}(r)\) and \(F_{\mathcal M}(r)\) for the intrinsic-distance cumulative distribution functions.

**Theorem (exact onset, strict comparison, and inverse classification).** For every \(C,H>0\):

1. \(F_{\mathcal M}(r)=F_{\mathcal C}(r)\) for all \(0\le r\le C/2\); for every \(C/2<r<\sqrt{C^2/4+H^2}\), the inequality \(F_{\mathcal M}(r)>F_{\mathcal C}(r)\) is strict; and both functions equal one for \(r\ge\sqrt{C^2/4+H^2}\). Thus the Möbius distance is stochastically no larger, with a precisely located strict region.
2. As \(\varepsilon\downarrow0\),
   \[
   F_{\mathcal M}(C/2+\varepsilon)-F_{\mathcal C}(C/2+\varepsilon)
    =\frac{8}{3H\sqrt C}\,\varepsilon^{3/2}+O_{C,H}(\varepsilon^2).
   \]
   The coefficient is positive for all nondegenerate widths and has no aspect-ratio exception.
3. For \(0\le r\le\min\{C/2,H\}\), both distributions obey the same exact local law
   \[
   F(r)=\frac{\pi r^2}{CH}-\frac{4r^3}{3CH^2}.
   \]
   In particular, these two coefficients uniquely determine \(C\) and \(H\). The *full* distance distribution consequently determines the isometry class among all flat rectangular cylinders and Möbius bands of this form, including their orientability.

The following integral formulas give the full distributions for every \(r\ge0\). Define
\[
G_H(t)=\begin{cases}0,&t\le0,\\2t/H-t^2/H^2,&0<t<H,\\1,&t\ge H.\end{cases}
\]
Then
\[
F_{\mathcal C}(r)=\frac2C\int_0^{C/2}G_H\!\left(\sqrt{(r^2-a^2)_+}\right)\,da.
\]
For \(a\in[0,C/2]\), set \(b=C-a\). If \(r\ge b\), define \(u=\sqrt{r^2-a^2}\), \(v=\sqrt{r^2-b^2}\), and \(q=\min\{v,(H-u)_+\}\); otherwise put \(q=0\) and the integrand below equal to zero. With \((x)_+=\max\{x,0\}\),
\[
 F_{\mathcal M}(r)-F_{\mathcal C}(r)
 =\frac{2}{CH^2}\int_{\max\{0,C-r\}}^{C/2}
 \left[2(H-u)q-q^2\right]da
 \quad(r>C/2),
\]
and the difference is zero for \(r\le C/2\). The integral is nonnegative; where \(u\ge H\), its integrand vanishes by the definition of \(q\).

## Assumptions and scope

The metrics are those of the **abstract flat quotient surfaces**, not the ambient Euclidean distance between points of a physical embedding. Neither an isometric smooth embedding in three-space nor an elastic equilibrium is assumed. Boundary points have area measure zero; including them in the compact length spaces does not change the sampling law. The words ``circumference'' and ``width'' refer to the rectangle's length in the quotient direction and the transverse interval length, respectively; the Möbius boundary is one connected curve of length \(2C\), whereas the cylinder has two boundary curves of length \(C\) each. All assertions include every \(C,H>0\), with no thin-strip approximation.

## Proof

**1. Quotient metric and a common coupling.** The universal covering strip is \(\mathbb R\times[-H/2,H/2]\). Its deck generator is \(T(s,y)=(s+C,y)\) in the cylindrical case, and \(T(s,y)=(s+C,-y)\) in the Möbius case. Because the strip is Euclidean and convex, the intrinsic distance between quotient points equals the least Euclidean distance between any representatives related by deck transformations. For independent uniform points, let \(a\in[0,C/2]\) be the shorter circular separation between their horizontal coordinates. This random variable is uniform with density \(2/C\) and independent of their transverse coordinates.

In the Möbius case, the closest horizontal image and the closest image of the opposite deck parity have respective horizontal displacements \(a\) and \(b=C-a\). All other images of either parity have no smaller horizontal displacement and exactly the same transverse displacement as the corresponding nearest image, so none can improve the distance. If the first nearest image is an odd reflection, reflect the second transverse coordinate; since it is uniform on the centered interval, this measure-preserving change does not affect the joint law. Hence there exist independent \(Y_1,Y_2\sim\operatorname{Unif}[-H/2,H/2]\), independent of \(a\), such that the *joint* distance laws admit the coupling
\[
D_{\mathcal C}=\sqrt{a^2+(Y_2-Y_1)^2},\qquad
D_{\mathcal M}=\min\!\left\{D_{\mathcal C},\sqrt{(C-a)^2+(Y_2+Y_1)^2}\right\}.
\]
This immediately gives \(D_{\mathcal M}\le D_{\mathcal C}\) pointwise in this coupling.

**2. Sharp strict region.** Since \(C-a\ge C/2\), the extra Möbius route cannot have length below \(C/2\). Thus both distribution functions agree through that threshold. The cylinder's maximum distance is \(R=\sqrt{C^2/4+H^2}\). To show strictness for any fixed \(r\in(C/2,R)\), choose \(a=C/2\), \(Y_1=H/2\), and \(Y_2=-H/2\). The competing Möbius route has length \(C/2<r\), whereas \(D_{\mathcal C}=R>r\). Strict inequalities persist in a positive-measure neighborhood of these parameter values (using slightly interior coordinates). Therefore \(\Pr(D_{\mathcal M}\le r<D_{\mathcal C})>0\) at every such \(r\). Beyond \(R\) both distribution functions are one.

**3. Exact difference integral.** Write \(V=Y_1+Y_2\) and \(W=Y_2-Y_1\). Their joint density equals \(1/(2H^2)\) on the diamond \(|V|+|W|\le H\) and zero elsewhere. Fix \(a\le C/2\). The event contributing to \(F_{\mathcal M}(r)-F_{\mathcal C}(r)\) is precisely
\[
 (C-a)^2+V^2\le r^2<a^2+W^2.
\]
If \(r<C-a\) it is empty. Otherwise put \(u=\sqrt{r^2-a^2}\) and \(v=\sqrt{r^2-(C-a)^2}\). Integrating the diamond density over \(|V|\le v\) and \(|W|>u\) gives
\[
\frac1{H^2}\int_{-q}^{q}(H-u-|V|)\,dV
=\frac{2(H-u)q-q^2}{H^2},\qquad q=\min\{v,(H-u)_+\}.
\]
Integrating against the density \(2/C\) of \(a\) proves the stated one-dimensional integral without a truncation or asymptotic assumption.

**4. Exact onset coefficient.** Put \(r=C/2+\varepsilon\) and \(a=C/2-t\), where \(0\le t\le\varepsilon\) is the only contributing range for small \(\varepsilon>0\). Uniformly on this interval,
\[
 v=\sqrt{C(\varepsilon-t)+O(\varepsilon^2)},\qquad
 u=O_{C}(\sqrt\varepsilon).
\]
For sufficiently small \(\varepsilon\) (depending on fixed \(C,H\)), one has \(q=v\). The exact difference integral becomes
\[
\frac{2}{CH^2}\int_0^\varepsilon\left(2(H-u)v-v^2\right)dt
=\frac4{CH}\int_0^\varepsilon\sqrt{C(\varepsilon-t)}\,dt
  +O_{C,H}(\varepsilon^2).
\]
The elementary integral equals \(2\sqrt C\,\varepsilon^{3/2}/3\). This proves the \(3/2\) exponent, the explicit coefficient, and the claimed remainder.

**5. Common local law and reconstruction.** The random variable \(W\) has triangular density \((H-|w|)/H^2\) on \([-H,H]\). Consequently, when \(r\le\min(C/2,H)\), the cylinder distance event describes an untruncated disk in the local \((a,w)\) coordinates, with radial integration
\[
 F_{\mathcal C}(r)
 =\frac1C\int_{-r}^r\frac{2H\sqrt{r^2-x^2}-(r^2-x^2)}{H^2}\,dx
 =\frac{\pi r^2}{CH}-\frac{4r^3}{3CH^2}.
\]
The Möbius law is the same in this region by step 2. If \(A>0\) and \(B<0\) are the quadratic and cubic coefficients of the observed short-distance expansion, then
\[
 H=-\frac{4A}{3\pi B},\qquad C=\frac{\pi}{AH}.
\]
Thus both geometric parameters are reconstructed solely from the distance distribution. Holding these recovered parameters fixed, the cylinder and Möbius distributions are different by step 2, so the same distribution cannot come from both topologies. This completes the inverse classification.

## Verification

The standalone `verify.py` in this package evaluates the exact integral with adaptive quadrature, compares it against independent direct sampling of the quotient metrics, tests the exact local polynomial, and checks convergence of the rescaled excess near \(C/2\) for several aspect ratios. Its numerical checks are supplementary; the above analytical argument, not any finite simulation, establishes the quantified conclusions. The script prints the actual tested parameters, numerical errors, and the theoretical onset constants.

## Relationship to prior work

A flat Möbius band as a rectangular strip with a half-twist, and its developable/isometric realizations, are classical. Starostin and van der Heijden (2007) analyze the *extrinsic equilibrium shape* of an inextensible Möbius strip; Sabitov (2007) studies its *isometric immersion and embedding*. Neither the extrinsic equilibrium problem nor existence of an immersion implies an intrinsic two-point distance distribution. Standard random-distance formulas for Euclidean domains (for example, Zhuang and Pan, 2011, on rhombuses) concern ambient straight-line distances in a single planar domain and not competing deck-parity geodesics on a quotient. The present theorem instead compares the complete intrinsic two-point laws of the twisted and untwisted rectangular interval bundles, determines their first point of disagreement, and supplies the exact half-integer onset coefficient. No prior claim of uniqueness across arbitrary compact surfaces is made.

## Limitations

The theorem concerns only these two *rectangular, locally Euclidean, constant-width* quotient families, with uniform area sampling and shortest intrinsic distance. It does not treat arbitrary nonflat physical Möbius embeddings, variable-width ribbons, weighted sampling, nonuniform curvature, or all topological surface types. The originality assessment is based on accessible literature and mathematical implication checks; earlier equivalent formulas in less accessible specialized sources remain possible. The claim is not an independent certification or an exhaustive statement about the history of Möbius-band geometry.

## References

- E. L. Starostin and G. H. M. van der Heijden, *The shape of a Möbius strip*, Nature Materials **6** (2007), 563–567; DOI: 10.1038/nmat1929. First published 2007-07-15. Investigates elastic/developable shape, not random intrinsic distances.
- I. Kh. Sabitov, *Isometric immersions and embeddings of a flat Möbius strip in Euclidean spaces*, Izvestiya: Mathematics **71** (2007), 1049–1078; DOI: 10.1070/IM2007v071n05ABEH002376. Concerns the geometric realization of flat bands.
- Y. Zhuang and J. Pan, *Random Distances Associated with Rhombuses*, arXiv:1106.1257 (first posted 2011-06-07). Euclidean-domain distance distributions rather than quotient-surface distances.
- *Straight lines in curved spaces: geodesics*, Tangente, published 2016-04-25, https://tangente-mag.com/en/articles/straight-lines-in-curved-spaces-geodesics. Expository description of unfolding and shortest paths.
