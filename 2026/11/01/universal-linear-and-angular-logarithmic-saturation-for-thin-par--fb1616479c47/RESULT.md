# Universal linear and angular logarithmic saturation for thin parallelograms

## Finding

Let \(0<\vartheta<\pi\), write \(c=\cos\vartheta\), \(h=\sin\vartheta>0\), and for \(0<\ell<1\) define the nondegenerate Euclidean parallelogram
\[
P_{\ell,\vartheta}=\{(s+\ell c t,\ell h t):0\le s,t\le1\}.
\]
Let \(M_{\mathrm{in}}(P)\) be the Euclidean distance expectation for two independent, area-uniform points of \(P\), and let \(M_{\partial}(P)\) be the same expectation for two independent, arclength-uniform boundary points. Put \(G_{\vartheta}(\ell)=M_{\partial}(P_{\ell,\vartheta})-M_{\mathrm{in}}(P_{\ell,\vartheta})\).

**Theorem.** For every fixed \(\vartheta\in(0,\pi)\), as \(\ell\downarrow0\),
\[
\boxed{\displaystyle
G_{\vartheta}(\ell)=\frac{\ell}{3}
+\ell^2\left[\frac{h^2}{3}\log\frac{2}{h\ell}
-\frac{55h^2}{72}-\frac{c^2}{6}\right]
+O_{\vartheta}\!\left(\ell^3\log\frac1\ell\right).}
\]
In particular, the linear coefficient is independent of the angle, whereas the next nonanalytic coefficient is precisely \(\sin^2\vartheta/3\):
\[
\lim_{\ell\downarrow0}\frac{G_{\vartheta}(\ell)}{\ell}=\frac13,
\qquad
\lim_{\ell\downarrow0}\frac{G_{\vartheta}(\ell)-\ell/3}{\ell^2\log(1/\ell)}=\frac{\sin^2\vartheta}{3}.
\]
Equivalently, the corresponding multiplicative sharpness ratio has the two exact limits
\[
\lim_{\ell\downarrow0}\frac{M_{\partial}/M_{\mathrm{in}}-1}{\ell}=1,
\qquad
\lim_{\ell\downarrow0}\frac{M_{\partial}/M_{\mathrm{in}}-1-\ell}{\ell^2\log(1/\ell)}=\sin^2\vartheta.
\]
The already known strict inequality \(M_{\partial}>M_{\mathrm{in}}\) is not part of the novelty assertion. The result quantifies its degeneration within the full fixed-angle parallelogram family.

## Assumptions and scope

Distance is ordinary Euclidean distance; measures are normalized Lebesgue area and normalized Euclidean arclength. Both sampled points in each pair are independent. The longer generating segment has length one, the shorter has length \(\ell\), and the angle is fixed in \((0,\pi)\) while \(\ell\to0\). A general long-side length \(L>0\) is restored by multiplying every distance and the displayed gap by \(L\), with \(\ell\) interpreted as the ratio of short to long side lengths. Constants implicit in remainders may depend on the fixed angle; there is no claim of uniformity as the angle tends to zero or \(\pi\).

## Proof

**1. A one-dimensional distance kernel.** Let \(T\) have density \((1-|t|)\mathbf1_{[-1,1]}(t)\), the law of the difference of two independent uniform variables on \([0,1]\). For \(a\in\mathbb R\) and \(b>0\) set
\[
F(a,b)=\int_{-1}^1(1-|t|)\sqrt{(t+a)^2+b^2}\,dt.
\]
For \(a=0\), direct integration gives
\[
F(0,b)=\sqrt{1+b^2}+b^2\operatorname{arsinh}(1/b)
-\frac23\bigl((1+b^2)^{3/2}-b^3\bigr).
\]
Consequently
\[
F(0,b)=\frac13+b^2\left(\log\frac2b-\frac12\right)+O(b^3).
\]
For fixed \(b>0\), differentiation under the integral yields
\[
\partial_a^2F(a,b)=\int_{-1}^1(1-|t|)\frac{b^2}{((t+a)^2+b^2)^{3/2}}\,dt.
\]
The kernel integrates to two over the entire real line. With \(w(t)=(1-|t|)_+\), the bound \(0\le1-w(t)\le|t|\) on \(\mathbb R\) implies
\[
0\le2-\partial_a^2F(a,b)
\le\int_{\mathbb R}(|u|+|a|)\frac{b^2}{(u^2+b^2)^{3/2}}\,du
=2(b+|a|).
\]
Since \(F\) is even in \(a\), integrate twice to obtain, uniformly when \(|a|+b\to0\),
\[
F(a,b)=\frac13+a^2+b^2\left(\log\frac2b-\frac12\right)
+O\bigl((|a|+b)^3\bigr).
\]
The displayed remainder is valid for all fixed ratios \(a/b\) and, by the explicit bound, remains integrable when the common scaling variable below tends to zero.

**2. Interior sampling.** Every area-uniform point has the representation \((S+\ell cR,\ell hR)\), where \(S,R\) are independent uniform variables on \([0,1]\). If \(Z=R-R'\) has the triangular density above, then by conditioning on \(Z\),
\[
M_{\mathrm{in}}=\mathbb E\,F(\ell cZ,\ell h|Z|).
\]
The triangular law satisfies \(\mathbb EZ^2=1/6\) and \(\mathbb E[Z^2\log(1/|Z|)]=7/72\). Substituting the kernel expansion gives
\[
M_{\mathrm{in}}=\frac13+\ell^2\left[\frac{c^2}{6}
+\frac{h^2}{6}\log\frac{2}{\ell h}+\frac{h^2}{72}\right]+O_{\vartheta}(\ell^3).
\]
All possible events \(Z=0\) have zero probability and introduce no singular mass.

**3. Boundary sampling.** Each of the two long edges has length one, and each of the two short edges has length \(\ell\). Thus a boundary point lies on a long edge with probability \(1/(1+\ell)\). Let \(H\), \(V\), and \(C\) be conditional mean distances for respectively two long-edge points, two short-edge points, and one point from each edge class. Counting same and opposite long edges gives
\[
H=\frac16+\frac12F(\ell c,\ell h)
=\frac13+\frac{\ell^2}{2}\left[c^2+h^2\left(\log\frac{2}{\ell h}-\frac12\right)\right]
+O_{\vartheta}(\ell^3).
\]
On the two short edges, a same-edge pair contributes \(\ell/6\) after the probability of that case is included; an opposite-edge pair contributes \(1/2+O_{\vartheta}(\ell^2)\). Therefore \(V=1/2+O_{\vartheta}(\ell)\). For cross-class pairs, a symmetry of the four choices of edges cancels the first-order tangential displacement. More explicitly, \(C\) is the average over \(x,r\in[0,1]\) of
\[
\frac12\left[\sqrt{(x+\ell cr)^2+(\ell hr)^2}
+\sqrt{(x-\ell cr)^2+(\ell hr)^2}\right].
\]
Split the \(x\)-integral at \(2\ell\). Below that threshold the contribution of the difference from \(x\) is \(O(\ell^2)\); above it the symmetrized Taylor remainder is bounded by \(O(\ell^2/x)\). Therefore \(C=1/2+O_{\vartheta}(\ell^2\log(1/\ell))\). The exact conditional mixture is
\[
M_{\partial}=\frac{H+2\ell C+\ell^2V}{(1+\ell)^2}.
\]
Expanding this quotient and using \(c^2+h^2=1\) cancels the otherwise apparent \(c^2\) term at second order:
\[
M_{\partial}=\frac13+\frac\ell3
+\ell^2h^2\left[\frac12\log\frac2{\ell h}-\frac34\right]
+O_{\vartheta}\!\left(\ell^3\log\frac1\ell\right).
\]
Subtracting the interior formula proves the boxed expansion.

**4. Sharpness and the ratio.** The coefficient \(1/3\) is an actual limit, not merely a bound, for every fixed permissible angle. Subtracting it exposes the exact positive logarithmic coefficient \(h^2/3\). Since \(M_{\mathrm{in}}=1/3+O_{\vartheta}(\ell^2\log(1/\ell))\), division gives both stated ratio limits. Taking the angle \(\pi/2\) specializes the theorem to the original thin-rectangle degeneration.

## Verification

The accompanying standalone `check.py` (dependency listed in `requirements.txt`) evaluates the independently normalized interior and long/short/cross boundary decompositions using high-precision quadrature and checks the predicted three-term asymptotic at four fixed angles and four small lengths per angle. It also checks the integral primitive against direct weighted integration, invariance under replacing \(\vartheta\) by \(\pi-\vartheta\), and the classical exact unit-square interior mean. An additional independently sampled 180000-pair test checks area and boundary normalization at a non-rectangular angle. All checks pass. The analytical argument, not the finite tests, establishes the theorem and its remainder.

## Relationship to prior work

The planar boundary-versus-interior distance inequality is established in the works of Shen (arXiv:2608.06470) and Kukushkin (arXiv:2608.14833). Both identify the degenerating thin-rectangle mechanism qualitatively. The displayed sources do not give its universal fixed-angle rate or the angular logarithmic correction. Lotnikov (arXiv:2608.14848) treats centrally symmetric bodies and related distance comparisons, not this three-term degeneration law. Classical line-picking work (including Sheng, 1985, and Agaronyan, 2012) gives formulas for interior distances of parallelograms or rectangles; those formulas are not represented as novel. The contribution asserted here is the specific coupled boundary-minus-interior asymptotic, with its universal leading constant, shear-dependent finite term, and angle-detecting logarithmic term.

## Limitations

This is a fixed-angle thin-body theorem, not an inequality uniform over all parallelogram shapes, not a stability theorem for arbitrary convex bodies, and not a new proof of the general Zaporozhets–Tarasov inequality. The error term is not claimed to have a globally optimal coefficient. Historical priority for equivalent boundary-distance asymptotics, especially within older line-picking literature, is not conclusively settled. No independent mathematical validation is claimed.

## References

1. E. Shen, *The Zaporozhets–Tarasov Conjecture on Mean Distances*, arXiv:2608.06470 (first posted 2026-08-06), Sections 1 and 5.
2. M. Kukushkin, *The Zaporozhets–Tarasov Inequality for an Arbitrary Planar Convex Body*, arXiv:2608.14833 (posted 2026-08-14), Section 2, Remark 1 and Section 6.
3. A. S. Lotnikov, *Mean distance between points inside and on the boundary of a convex body*, arXiv:2608.14848 (posted 2026-08-14).
4. T. Sheng, *The distance between two random points in plane regions*, *Advances in Applied Probability* **17** (1985), 748–773.
5. N. G. Agaronyan, *Mean distance between two points in a domain*, *Proceedings of the YSU A: Physical and Mathematical Sciences* **46** (2012), 3–8.
