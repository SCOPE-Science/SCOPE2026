# Conditional diameter law and sharp two-radius phase diagram for central cube sections

## Finding
Let \(Q=[-1,1]^3\), let \(U\) be uniform on \(S^2\), and let \(P_U=Q\cap U^\perp\). Let \(r(U)\) be its intrinsic Euclidean inradius and \(D(U)\) its Euclidean diameter. Write
\[
H=\sqrt{r(U)^2-1},\qquad Z=\sqrt{D(U)^2/4-2}.
\]
Their ranges are \(0\le H\le1/\sqrt2\) and \(0\le Z\le1\). The **complete conditional diameter law** is elementary. For \(0\le h<1/\sqrt2\), let
\[
\begin{aligned}
\alpha&=\arcsin h,\qquad \beta=\pi/4,\\
\gamma&=\begin{cases}
\arccos(h/\sqrt2)-\pi/4,&0\le h<1/\sqrt5,\\
\alpha,&1/\sqrt5\le h<1/\sqrt2,
\end{cases}\\
L_h(z)&=\arctan z-\arcsin\frac{h}{\sqrt{1+z^2}},\\
R_h(z)&=\arccos\frac{h}{\sqrt{1+z^2}}-\arctan z.
\end{aligned}
\]
With \([x]_+=\max\{0,x\}\), for \(0\le z\le1\),
\[
\boxed{\mathbb P\{Z\le z\mid H=h\}=\frac{[\min\{\gamma,L_h(z)\}-\alpha]_+ +[\beta-\max\{\gamma,R_h(z)\}]_+}{\beta-\alpha}.}
\]
This is a continuous regular conditional distribution for interior \(h\), with the endpoint \(h=0\) defined by continuity. At \(h=1/\sqrt2\) the section is a regular hexagon and \(Z=0\) deterministically. Outside \([0,1]\) the CDF is zero or one as appropriate. The marginal density of \(H\), with respect to ordinary Lebesgue measure, is
\[
\boxed{f_H(h)=\frac{12}{\pi}\frac{\pi/4-\arcsin h}{(1+h^2)^{3/2}}\quad(0<h<1/\sqrt2).}
\]
Together these formulas specify the complete joint law of \((r,D)\), not just either marginal.

The **sharp attainable support** has two transitions. Let \(h_0\) be the unique root in \((0,1/\sqrt5)\) of
\[
\frac{2h}{\sqrt{1-h^2}}+\sqrt2h=1
\qquad(h_0=0.285620483895568\ldots).
\]
For every fixed \(r=\sqrt{1+h^2}\), \(0\le h\le1/\sqrt2\), the possible values of \(Z\) form exactly \([\ell(h),u(h)]\), where
\[
\begin{aligned}
\ell(h)&=\begin{cases}
2h/\sqrt{1-h^2},&0\le h\le h_0,\\
1-\sqrt2h,&h_0\le h\le1/\sqrt2,
\end{cases}\\
u(h)&=\begin{cases}
1,&0\le h\le1/\sqrt5,\\
\sqrt{1-h^2}/h-1,&1/\sqrt5\le h\le1/\sqrt2.
\end{cases}
\end{aligned}
\]
Consequently the attainable diameters at fixed inradius are exactly \(2\sqrt{2+z^2}\) for \(\ell(h)\le z\le u(h)\); every endpoint is attained. Furthermore, where both the quadrilateral and hexagonal branches contribute to the conditional density (\(0<h<1/\sqrt5\), \(\max\{2h/\sqrt{1-h^2},1-\sqrt2h\}<z<1\)), an exact cancellation gives
\[
f_{Z\mid H=h}(z)=\frac{2}{(\pi/4-\arcsin h)(1+z^2)}.
\]

## Assumptions and scope
All distances and inradii are Euclidean in the intrinsic two-plane; \(U\) is a Haar-uniform unoriented plane normal, represented by a uniform spherical vector. The cube has half-edge length one. The diameter is the largest pairwise separation within the section, not the planar projection width. The inradius permits arbitrary disk centers; symmetry implies a largest disk can be centered at the origin. The theorem includes sections with vertex-through-plane degeneracies by continuity, but the probability of such directions is zero. The CDF conditional on \(H=h\) is the specific continuous regular version given by the displayed formula; pointwise conditional distributions at zero-probability values are otherwise not unique.

## Proof
**1. Exact inradius.** Let the ordered absolute coordinates of \(U\) be \(0\le a\le b\le c\), with \(a^2+b^2+c^2=1\). Within \(U^\perp\), the cube constraints are the six strips \(|\langle e_i,x\rangle|\le1\). An origin-centered Euclidean disk of radius \(s\) satisfies these constraints precisely when \(s\|\operatorname{proj}_{U^\perp}e_i\|\le1\) for each \(i\). Their largest projected norm is \(\sqrt{1-a^2}\), so \(r=(1-a^2)^{-1/2}\). Central symmetry gives an origin-centered disk from any optimal translated disk by averaging it with its negative. Hence \(H=a/\sqrt{b^2+c^2}\).

**2. Exact diameter.** Every section vertex is a cube-edge intersection and hence has two coordinates of absolute value one. With \(0\le a\le b\le c\), if \(c\ge a+b\), only the edges parallel to the largest-normal coordinate meet the plane generically, and the largest free-coordinate magnitude is \((a+b)/c\). If \(c\le a+b\), the possible free-coordinate magnitudes at vertices are \((c-b)/a\), \((c-a)/b\), and \((b-a)/c\) when the denominators are nonzero. The second dominates the others because
\[
\begin{aligned}
a(c-a)-b(c-b)&=(b-a)(a+b-c)\ge0,\\
c(c-a)-b(b-a)&=(c-b)(c+b-a)\ge0.
\end{aligned}
\]
Thus the maximum vertex squared norm is \(2+z^2\), with
\[
z=\begin{cases}(a+b)/c,&c\ge a+b,\\(c-a)/b,&c\le a+b.\end{cases}
\]
The central symmetry of the section makes its diameter exactly twice the maximum vertex norm. Degenerate cases follow by taking limits.

**3. Uniform conditional angle.** Set \(h=a/\sqrt{b^2+c^2}\), and define an angle \(\theta\) by
\[
(b,c)=\frac1{\sqrt{1+h^2}}(\sin\theta,\cos\theta),\qquad
 a=\frac h{\sqrt{1+h^2}}.
\]
The ordering \(a\le b\le c\) is exactly \(\alpha(h)=\arcsin h\le\theta\le\beta=\pi/4\) with \(0\le h\le1/\sqrt2\). On a spherical coordinate chart with first coordinate \(a\), the spherical area element is \(da\,d\theta=(1+h^2)^{-3/2}\,dh\,d\theta\). All \(48\) sign/order chambers have equal Haar weight, and one chamber has area \(\pi/12\). Thus the joint density on the displayed domain is \(12/(\pi(1+h^2)^{3/2})\), so \(\theta\) is uniform conditional on \(H=h\) and integrating its allowed interval yields the stated marginal density.

**4. Two monotone branches.** In these variables the section-vertex parameter is
\[
z(\theta)=\begin{cases}
(h+\sin\theta)/\cos\theta,&\cos\theta\ge h+\sin\theta,\\
(\cos\theta-h)/\sin\theta,&\cos\theta\le h+\sin\theta.
\end{cases}
\]
The first branch is strictly increasing in \(\theta\), since its derivative is \((1+h\sin\theta)/\cos^2\theta\). The second is strictly decreasing, since its derivative is \((h\cos\theta-1)/\sin^2\theta<0\). Their boundary solves \(\cos\theta-\sin\theta=h\), at \(\theta=\arccos(h/\sqrt2)-\pi/4\). This point belongs to the allowed angular interval precisely when \(h\le1/\sqrt5\); otherwise the second branch occupies the whole interval. This proves the formula for \(\gamma\).

**5. Invert the two branches.** For \(0\le z\le1\), the first-branch condition \((h+\sin\theta)/\cos\theta\le z\) is equivalent to \(\theta\le L_h(z)\), by solving \(\sin(\theta-\arctan z)\le-h/\sqrt{1+z^2}\) on the allowed angle range. The second-branch condition \((\cos\theta-h)/\sin\theta\le z\) is equivalent to \(\theta\ge R_h(z)\). Intersect the first with \([\alpha,\gamma]\), the second with \([\gamma,\beta]\), and divide the summed lengths by \(\beta-\alpha\) to obtain the exact conditional CDF. Differentiating the two inverse angles gives
\[
L_h'(z)=\frac{1+hz/\sqrt{1+z^2-h^2}}{1+z^2},\qquad
-R_h'(z)=\frac{1-hz/\sqrt{1+z^2-h^2}}{1+z^2}.
\]
Their sum is \(2/(1+z^2)\) whenever both inverse bounds lie strictly inside their branches, proving the density cancellation.

**6. Sharp support and extremizers.** The one-peaked \(z(\theta)\) has its minimum at an angular endpoint and its maximum at its branch meeting point, if that point exists, or at \(\theta=\alpha\) otherwise. At \(\theta=\alpha\) (equivalently \(a=b\)), its value is \(2h/\sqrt{1-h^2}\) for \(h\le1/\sqrt5\), and \(\sqrt{1-h^2}/h-1\) thereafter. At \(\theta=\beta\) (equivalently \(b=c\)), its value is \(1-\sqrt2h\). The meeting point gives \(z=1\). For \(0<h<1/\sqrt5\), the two endpoint values cross exactly once: the first increases strictly and the second decreases strictly, giving the stated unique \(h_0\). For \(h\ge1/\sqrt5\), the decreasing second branch gives the lower endpoint at \(b=c\) and upper at \(a=b\). Continuity of \(z(\theta)\) fills the entire interval between the sharp bounds. The cases \(h=0\) and \(h=1/\sqrt2\) follow by continuity and explicit axial/body-diagonal normals. This establishes both the support and equality directions. \(\square\)

## Verification
Run `python3 verify_radii.py` and `python3 verify_conditional.py` in the same directory as this document. The first program independently enumerates cube-edge intersections with exact rational arithmetic for \(893\) sorted integer triples, checks \(25{,}000\) additional normals, and probes sharp endpoints. The second independently evaluates conditional angular probabilities on \(176{,}000\) deterministic midpoint directions, checks the joint normalization by composite Simpson quadrature, and verifies the two-branch density cancellation. Both scripts use the Python standard library. The infinite statements follow from the explicit geometric proof above, not from finite tests.

## Relationship to prior work
Guédon, Litvak, Tatarko and Vritsiou (2026) investigate the random diameters of sections of general convex bodies, including probability bounds and examples. Their publicly accessible abstract does not state this cube-specific *joint* radius distribution; the full manuscript was not accessible for direct comparison. Lonke (1998/2000) derives expected face numbers of random sections of cubes rather than their joint metric invariants; the accessible author manuscript was read through its mathematical sections. The published 2026 result *Exact inradius law for random planar projections of the regular octahedron* gives, by polarity, the **marginal law of the diameter of a central cube section**, and explicitly contains the deterministic cube-section circumradius formula used in Step 2. That marginal is not a conditional distribution with the cube-section's own inradius: the new information here is the uniform-angle disintegration, the exact conditional law, and the sharp joint feasible domain. The published result *Exact Haar diameter law for central sections of the regular octahedron* concerns the *different* body/section statistic and does not imply this joint law. No uniqueness is inferred merely from a search partition, and historical formulas not indexed under these geometric aliases could still overlap.

## Limitations
The theorem is for Haar-random central sections of the three-dimensional Euclidean cube only; it does not describe arbitrary affine offsets, rectangular boxes, or higher dimensions. The conditional formula at exceptional probability-zero inradius values specifies one continuous version, and the pointwise endpoint \(h=1/\sqrt2\) is separately degenerate. The full 2026 motivating manuscript was unavailable, leaving residual priority risk; accessible statements do not establish an identical conditional joint result. No independent mathematical audit has been performed.

## References
1. O. Guédon, A. E. Litvak, K. Tatarko, and B.-H. Vritsiou, *On Random Diameters of Convex Bodies*, arXiv:2609.24131v1, first publicly posted September 21, 2026, https://arxiv.org/abs/2609.24131.
2. Y. Lonke, *On Random Sections of the Cube*, arXiv:math/9812123v1, first posted December 21, 1998; Discrete & Computational Geometry 23 (2000), 157–169. Author manuscript accessible at https://www.researchgate.net/publication/225671896_On_Random_Sections_of_the_Cube.
3. *Exact inradius law for random planar projections of the regular octahedron*, publicly indexed mathematical research result (2026); its full result and polar reduction were inspected.
4. *Exact Haar diameter law for central sections of the regular octahedron*, publicly indexed mathematical research result (2026); its full result was inspected.
