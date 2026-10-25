# Quadratic Fourier-zero loss under rounding the regular dodecagon

## Finding
Let \(P\) be the regular dodecagon of area \(\pi\), centered at the origin; \(B\) is the unit Euclidean disk. The area-normalized outer parallel body is
\[K_t=\sqrt{\pi/\operatorname{area}(P+tB)}\,(P+tB),\qquad t>0.\]
For a centrally symmetric convex body \(K\) write
\[\widehat{1_K}(\xi)=\int_K\cos(\xi\cdot x)\,dx,\quad
\kappa(K)=\inf\{\|\xi\|_2:\widehat{1_K}(\xi)=0\}.\]
Then for sufficiently small \(t>0\),
\[\kappa(K_t)\le\kappa(P)-\eta t^2+O(t^3)<\kappa(P),\]
where the **positive, explicitly computable** coefficient satisfies
\[0.00014158574849<\eta<0.00014158574850.\]
Thus rounding the proposed planar Fourier-zero extremizer by a small Euclidean disk strictly lowers the invariant after area renormalization. The statement is one-sided: no assertion is made that the displayed coefficient is the full quadratic expansion of \(\kappa(K_t)\).

## Assumptions and scope
The Fourier convention has no factor of \(2\pi\) in the exponential. Rotate \(P\) so that the first coordinate vector is a facet-normal direction. Put \(n=12\),
\[R=\sqrt{\pi/3},\quad r=R\cos(\pi/12),\quad \ell=2R\sin(\pi/12),\quad c=\tan(\pi/12)-\pi/12.\]
Thus \(R\) is the circumradius, \(r\) is the inradius, \(\ell\) is the side length, and \(c>0\). In the following formulas \(k=\kappa(P)\), whose nearest-zero directions are precisely the facet normals by Theorem 1.7 of Gómez-Serrano–Levitin–Platt–Polterovich (2026). In particular \(k\) is the first positive root of \(F(\rho)=\widehat{1_P}(\rho,0)\). The source's result proves the direction selection; its proof does not involve any outer-parallel-body perturbation.

## Proof
**1. Exact polygon transform.** Applying the divergence theorem with the vector field \((\sin(\rho x_1)/\rho,0)\), and grouping the twelve facets by their normal azimuths, gives
\[F(\rho)=\frac{2\ell}{\rho}\left[\sin(\rho r)+\sqrt3\sin\left(\frac{\sqrt3\rho r}{2}\right)\operatorname{sinc}\left(\frac{\rho\ell}{4}\right)+\sin\left(\frac{\rho r}{2}\right)\operatorname{sinc}\left(\frac{\sqrt3\rho\ell}{4}\right)\right],\]
where \(\operatorname{sinc}(x)=\sin(x)/x\). This expression and its elementary derivative give the exact value \(F'(k)\). The independently interval-checked root and derivative are \(3.83171224396364<k<3.83171224396366\) and \(F'(k)<0\).

**2. Geometric second-order wedge loss.** The scaled polygon \(Q_t=(1+t/r)P\) contains \(P+tB\): the support of \(P\) is at least \(r\) in every direction, so \((1+t/r)h_P\ge h_P+t\). The two bodies share all offset supporting facet lines. Their difference consists, for sufficiently small \(t\), of congruent disjoint vertex caps. At each vertex the cap area is exactly \(ct^2\): one removes a circular sector of exterior angle \(\pi/6\) from the intersection of the two adjacent offset half-planes, leaving \((\tan(\pi/12)-\pi/12)t^2\). Alternatively, the total \(12ct^2\) follows from Steiner's area formula and the polygon's tangential geometry; locality and congruence then give the cap value. The cap diameter is \(O(t)\). Hence for each \(\rho\) in a fixed neighborhood of \(k\),
\[\widehat{1_{P+tB}}(\rho,0)=\widehat{1_{Q_t}}(\rho,0)-ct^2\sum_{v\in\operatorname{Vert}(P)}\cos(\rho v_1)+O(t^3),\]
with a locally uniform error. The shifted cap locations differ from \(v\) by \(O(t)\), accounting for the error.

**3. Perturbed zero in the fixed facet-normal direction.** Set \(q_t=k/(1+t/r)\). Scaling shows \(\widehat{1_{Q_t}}(q_t,0)=0\), and \(\partial_\rho\widehat{1_{Q_t}}(q_t,0)=(1+t/r)^3 F'(k)\ne0\). The implicit function theorem gives a nearby real zero \(\rho_t\) of \(\widehat{1_{P+tB}}(\rho,0)\), and the previous cap formula yields
\[\rho_t=q_t+ct^2\frac{\sum_v\cos(kv_1)}{F'(k)}+O(t^3).\]
We do **not** assume that this is the globally nearest Fourier zero: by definition it provides the upper bound \(\kappa(P+tB)\le\rho_t\).

**4. Area normalization and coefficient.** Since \(P\) has area \(\pi\) and perimeter \(12\ell=2\pi/r\), Steiner's formula gives
\[\operatorname{area}(P+tB)=\pi+12\ell t+\pi t^2=\pi(1+t/r)^2-12ct^2.\]
Multiplying the fixed-direction root by \(\sqrt{\operatorname{area}(P+tB)/\pi}\), as required by Fourier scaling, gives
\[\kappa(K_t)\le k+ct^2\left[\frac{\sum_v\cos(kv_1)}{F'(k)}-\frac{6k}{\pi}\right]+O(t^3).\]
Define \(\eta\) as the negative of this coefficient. With vertex azimuths \((2j+1)\pi/12\),
\[\sum_v\cos(kv_1)=4\sum_{j=0}^{2}\cos\left(kR\cos\frac{(2j+1)\pi}{12}\right).\]
The standalone checker brackets the first positive root using opposite signs of \(F\) and interval-evaluates the exact derivative and coefficient. It gives \(-0.00014158574850<-\eta<-0.00014158574849\), proving \(\eta>0\). Therefore the strict reduction follows for all sufficiently small positive \(t\).

## Verification
Run \(\texttt{python verify.py}\) after installing \(\texttt{mpmath}\). The script uses 40-decimal-place interval arithmetic (not pointwise floating approximations) and tests the brackets \(F(3.83171224396364)>0\), \(F(3.83171224396366)<0\), \(F'(k)<0\), and the strict negative coefficient enclosure throughout this interval. The exact analytic cap argument and implicit-function analysis prove the order of the remainder; the computation checks the sign, not the remainder. An approximate value is \(\eta\approx0.00014158574849\).

## Relationship to prior work
Gómez-Serrano, Levitin, Platt and Polterovich prove that the regular dodecagon outperforms the disk for \(\kappa\), that it is the best among all regular even-sided polygons, and that its first Fourier-zero directions lie along facet normals (their Theorems 1.5 and 1.7). They pose its unrestricted maximizing property as Open Problem 1.6. The present statement establishes a previously unquantified **rounding-stability direction** of that candidate; it does not settle the global maximizing problem. Results on affine images and large-side-count asymptotics concern mathematically different deformations and do not imply the rounded-body coefficient.

## Limitations
The strict reduction is local in the rounding radius; it does not prove maximality under other perturbations. The computed coefficient is an upper-bound coefficient obtained from one direction, and is not asserted to be the exact coefficient of the global distance-to-zero functional. Source-dependent identification of the nearest-zero directions is invoked only at the undeformed polygon. Numerical verification relies on the interval arithmetic implementation of mpmath and must not be confused with independent review.

## References
1. J. Gómez-Serrano, M. Levitin, D. Platt and I. Polterovich, *An isoperimetric problem for Fourier zeros of centrally symmetric convex bodies*, arXiv:2609.10517v1, first posted 2026-09-09, Theorems 1.5, 1.7 and Open Problem 1.6. https://arxiv.org/html/2609.10517v1
2. Steiner's classical parallel-body formula for planar convex bodies (used for the area identity); the relevant polygonal specialization is also derived above.
