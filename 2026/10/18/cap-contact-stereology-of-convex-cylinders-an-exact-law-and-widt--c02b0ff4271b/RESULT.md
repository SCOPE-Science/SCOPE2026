# Cap-contact stereology of convex cylinders: an exact law and width-distribution recovery

## Finding

Let \(K\subset\mathbb R^2\) be any compact convex body with nonempty interior. For \(h>0\), set \(C_h=K\times[-h,h]\subset\mathbb R^3\). An unoriented affine plane is sampled using the rotation- and translation-invariant plane measure, conditioned on meeting \(C_h\). Apart from null-probability tangencies, let \(N_h\in\{0,1,2\}\) count the two planar end faces \(K\times\{-h,h\}\) whose relative interiors meet that plane.

For a horizontal unit vector \(e_\phi=(\cos\phi,\sin\phi)\), let \(w(\phi)=\max_{x\in K}x\cdot e_\phi-\min_{x\in K}x\cdot e_\phi\) and denote circular averaging by \(\langle f\rangle=(2\pi)^{-1}\int_0^{2\pi}f(\phi)\,d\phi\). Set
\[
\mu=\langle w\rangle=\frac{\operatorname{per}(K)}{\pi},\qquad
G_h=\left\langle\frac{w}{2}\arctan\frac{w}{2h}\right\rangle,\qquad Z_h=h+\frac{\pi\mu}{4}.
\]
The **entire three-type random-plane law** is
\[
\Pr(N_h=2)=\frac{G_h}{Z_h},\qquad
\Pr(N_h=0)=\frac{h-\pi\mu/4+G_h}{Z_h},\qquad
\Pr(N_h=1)=\frac{\pi\mu/2-2G_h}{Z_h}.
\]
In particular, the shape-independent difference is
\[
\Pr(N_h=0)-\Pr(N_h=2)=\frac{h-\pi\mu/4}{h+\pi\mu/4}.
\]
For fixed \(h\) and fixed planar perimeter (equivalently fixed \(\mu\)), **constant-width convex bodies are exactly the minimizers of both the zero-cap and two-cap probabilities, and exactly the maximizers of the one-cap probability**. This equality class includes nondisks.

More strongly, knowledge of the single scalar function \(h\mapsto \Pr(N_h=2)\) for all \(h>0\) determines *exactly the probability distribution* of the directional width \(w(\Phi)\), with \(\Phi\) uniform on \([0,2\pi)\). It does not necessarily determine \(K\), even when \(K\) is smooth, strictly convex and centrally symmetric.

## Assumptions and scope

The invariant plane sampling convention means that the measure of planes with unit normal in \(d\sigma(u)\) and signed offset in \(dt\) is proportional to \(d\sigma(u)\,dt\); the pair \((u,t)\) and \((-u,-t)\) represent the same plane. Conditioning on meeting \(C_h\) makes this a finite probability measure. The normal is **not** uniformly distributed after this conditioning: directions are weighted by the directional width of \(C_h\). Planes parallel to an end face, and planes touching a face only on its boundary, form null events; any convention for those cases gives the same law. No origin symmetry, smoothness, strict convexity or special planar shape is assumed in the main theorem.

The two end faces are counted as two distinct faces. The events \(N_h=0\) and \(N_h=2\) describe contacts with planar end faces, not whether the section is circular, elliptical, polygonal or contained entirely in the lateral surface. In particular, for nonsmooth \(K\), a zero-end-face section need not be an ellipse.

## Proof

**1. Affine-plane offset intervals.** Fix a unit plane normal \(u=(s e_\phi,c)\), taking \(c\ge0\), \(s=\sqrt{1-c^2}\). For uniform spherical normals, \(c\) is uniform on \([0,1]\) and \(\phi\) is uniform on \([0,2\pi)\). Write \(m(\phi)=\min_{x\in K}x\cdot e_\phi\) and \(M(\phi)=\max_{x\in K}x\cdot e_\phi\), so \(w=M-m>0\). The plane \(u\cdot(x,z)=t\) meets the top face precisely when
\[
t\in I_+=[s m+hc,\,s M+hc],
\]
and the bottom face precisely when \(t\in I_-=[s m-hc,\,s M-hc]\). The full cylinder is met for \(t\) in the interval from \(s m-hc\) to \(s M+hc\), of length \(L=ws+2hc\). Thus the two-end-face, zero-end-face, and exactly-one-end-face sets of offsets have lengths, respectively,
\[
\ell_2=(ws-2hc)_+,\qquad
\ell_0=(2hc-ws)_+,\qquad
\ell_1=L-\ell_2-\ell_0=2\min(ws,2hc).
\]
These statements follow directly by intersecting two intervals of equal length \(ws\) whose centers are separated by \(2hc\). Translation of \(K\) moves both intervals equally and does not affect the lengths.

**2. Integrate over plane normals.** Fix a width value \(w>0\) and put \(c_*=w/\sqrt{w^2+4h^2}\). The two-cap offsets occur for \(0\le c<c_*\) and the zero-cap offsets for \(c_*<c\le1\). Elementary integration gives
\[
\int_0^1 \ell_2\,dc
=\int_0^{c_*}\bigl(w\sqrt{1-c^2}-2hc\bigr)\,dc
=\frac w2\arctan\frac{w}{2h}=:g_h(w),
\]
\[
\int_0^1\ell_0\,dc
=\int_{c_*}^1\bigl(2hc-w\sqrt{1-c^2}\bigr)\,dc
=h-\frac{\pi w}{4}+g_h(w),
\]
\[
\int_0^1 L\,dc=h+\frac{\pi w}{4}.
\]
Averaging these formulas over \(\phi\) and dividing by the averaged length \(Z_h\) proves the three probabilities and the universal difference. Cauchy's planar perimeter formula \(\operatorname{per}(K)=\int_0^\pi w(\phi)\,d\phi\) gives \(\mu=\operatorname{per}(K)/\pi\). Every type has strictly positive measure, because \(w\) is positive and continuous and the inequalities defining all three offset possibilities hold on suitable nonempty open sets of normals and offsets.

**3. Sharp fixed-perimeter extremizers.** For \(w>0\), direct differentiation yields
\[
g_h''(w)=\frac{8h^3}{(w^2+4h^2)^2}>0.
\]
Consequently \(G_h=\langle g_h(w)\rangle\ge g_h(\mu)\) by strict Jensen convexity, with equality exactly when \(w(\phi)\equiv\mu\), because widths are continuous. For fixed \(h,\mu\), the two-cap and zero-cap probabilities are both strictly increasing affine functions of \(G_h\), whereas the one-cap probability is a strictly decreasing affine function. This gives all sharp inequalities and the complete equality classification. An equivalent exact deficit formula for either minimum is \(\bigl(G_h-g_h(\mu)\bigr)/Z_h\), while the one-cap maximum deficit is twice that quantity.

**4. Recovery of the unlabelled directional-width distribution.** Write \(B(h)=\Pr(N_h=2)\) and \(W=w(\Phi)\), where \(\Phi\) is uniform on the circle. Since every convex body has \(0<\min w\le\max w<\infty\), uniformly as \(h\downarrow0\),
\[
G_h=\frac{\pi\mu}{4}-h+O(h^3),\qquad
1-B(h)=\frac{8h}{\pi\mu}+O(h^2).
\]
Thus the observed function alone determines \(\mu\) from \(\mu=8/(\pi\lim_{h\downarrow0}(1-B(h))/h)\). Consequently it determines \(G_h=B(h)(h+\pi\mu/4)\) at every \(h>0\). For \(2h>\max w\), the uniformly convergent arctangent power series gives
\[
G_h=\sum_{m=1}^{\infty}\frac{(-1)^{m-1}\mathbb E[W^{2m}]}{(2m-1)2^{2m}h^{2m-1}}.
\]
Successively subtracting known terms of this large-height expansion determines every positive even moment \(\mathbb E[W^{2m}]\). The law of \(W^2\) is a probability measure on a compact positive interval, so equality of its moments (and total mass) determines it uniquely by polynomial approximation. The positive square-root map then determines the law of \(W\). Conversely, the displayed contact formulas plainly depend only on that law. Hence two bases have identical full cap-contact profiles for all heights if and only if their unlabelled width distributions agree.

**5. The sharp non-identifiability boundary.** Define two planar support functions \(p_2(\phi)=1+(1/30)\cos(2\phi)\) and \(p_4(\phi)=1+(1/30)\cos(4\phi)\). For either \(j=2\) or \(j=4\), the planar radius of curvature is \(p_j+p_j''=1+(1-j^2)\cos(j\phi)/30\ge1/2\). Thus each function defines a smooth strictly convex centrally symmetric body. Its width is \(w_j(\phi)=2+(1/15)\cos(j\phi)\). The random variables \(\cos(2\Phi)\) and \(\cos(4\Phi)\) have the same law, so the two bodies have identical cap-contact profiles for every height. Yet the standard support-function area formula gives
\[
\operatorname{area}(K_j)=\frac12\int_0^{2\pi}(p_j^2-(p_j')^2)\,d\phi
=\pi\left(1+\frac{1-j^2}{1800}\right),
\]
so their areas are \(599\pi/600\) and \(119\pi/120\), respectively. They therefore cannot be congruent. Their unequal areas establish that even the entire contact profile need not determine base area.

## Verification

The accompanying standalone program `verify.py` calculates the formulas for disks, rectangles, ellipses and two smooth support-function examples, compares them to direct two-dimensional normal-and-offset integration and weighted Monte Carlo sampling, checks strict constant-width inequalities, confirms the two noncongruent equimeasurable support functions, and checks the first large-height moment coefficients. Its successful execution reports `CAP_CONTACT_VERIFICATION_OK`. These checks provide independent finite corroboration; the all-body identity, sharp equality case, and inverse statement are proved by the calculations above rather than by finite sampling.

## Relationship to prior work

Invariant affine-plane sampling and mean-width integration belong to classical integral geometry, for example Santaló's *Integral Geometry and Geometric Probability*. Oakeshott and Edwards (1992) and McGarrity, Sietsma and Jongbloed (2015 online preprint of earlier journal work) study cylinder stereology and inverse sampling, but the examined material concerns cylinder-shape/orientation inference from observed sections, not the present arbitrary-convex-base count of end-face contacts. Kim, Yaskin and Zvavitch (2015 preprint) study unlabeled section and projection distributions, including non-uniqueness phenomena. Those general equidistribution ideas are acknowledged: the claim here is the explicit *cap-contact transform*, its inversion using the height parameter, and its sharp constant-width extremizers, not the pre-existing concept of an unlabeled width distribution or Cauchy's perimeter identity. Public records for a random-cylinder shadow area–perimeter covariance address projected metrics rather than end-face contact events. No exact implication deriving the displayed transform or its rigidity from inspected results was identified; this is evidence-limited, not a proof of historical priority.

## Limitations

Historical-priority confirmation is incomplete. In particular, only an abstract of Oakeshott and Edwards (1992) was accessible; its complete text should be compared independently for possible related end-face calculations. Sources discussing general integral geometry could contain a known equivalent formula not indexed by terminology. The recovery result concerns the **distribution** of the directional width, not its alignment with individual directions, the base's area, or the base itself. The theorem does not cover oblique cylinders, arbitrary sampling of central planes, or non-invariant section-sampling conventions. No independent mathematical audit has been performed.

## References

1. L. A. Santaló, *Integral Geometry and Geometric Probability*, Cambridge University Press; online edition dated 28 January 2010, https://doi.org/10.1017/CBO9780511617331.
2. R. B. S. Oakeshott and S. F. Edwards, “On the stereology of ellipsoids and cylinders,” *Physica A* 189 (1992), 208–233, https://doi.org/10.1016/0378-4371(92)90135-D. Full text not inspected.
3. K. S. McGarrity, J. Sietsma and G. Jongbloed, “Nonparametric inference in a stereological model with oriented cylinders applied to dual phase steel,” arXiv:1503.01305, first online 4 March 2015, https://arxiv.org/abs/1503.01305.
4. J. Kim, V. Yaskin and A. Zvavitch, “Distribution functions of sections and projections of convex bodies,” arXiv:1512.07289, first online 22 December 2015, https://arxiv.org/abs/1512.07289.
