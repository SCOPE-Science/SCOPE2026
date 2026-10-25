# Exact cut-locus Hessian jump energy on flat two-tori

## Finding

Let \(\Lambda\subset\mathbb R^2\) be a full-rank lattice and equip \(T_\Lambda=\mathbb R^2/\Lambda\) with its quotient Euclidean metric. Fix a point \(p\), write \(d_p(x)=d(p,x)\), and at \(\mathcal H^1\)-almost every regular point of the cut locus define
\[
j(q)=\left|\nabla d_p^+(q)-\nabla d_p^-(q)\right|.
\]
The cut-locus jump energy is
\[
J_2(T_\Lambda)=\int_{\operatorname{Cut}(p)}j(q)^2\,d\mathcal H^1(q).
\]
Let \(V\) be the Voronoi cell of the origin in the universal cover. Let \(\mathcal R_+\) contain one vector from each pair \(\{v,-v\}\) of Voronoi-relevant lattice vectors, and let \(F_v\) be the facet of \(V\) equidistant from the lattice points \(0\) and \(v\), with length \(\ell_v=\mathcal H^1(F_v)\). Then
\[
\boxed{J_2(T_\Lambda)=4\sum_{v\in\mathcal R_+}|v|\arctan\!\left(\frac{\ell_v}{|v|}\right).}
\]
For the rectangular torus
\[
T_{a,b}=\mathbb R^2/(2a\mathbb Z\times2b\mathbb Z),\qquad a,b>0,
\]
this reduces to
\[
J_2(T_{a,b})=8a\arctan\!\left(\frac ba\right)+8b\arctan\!\left(\frac ab\right).
\]
Among rectangular flat tori with fixed area \(A=4ab\), the unique maximizer is the square torus \(a=b\), and the maximum is \(2\pi\sqrt A\).

## Assumptions and scope

The result concerns two-dimensional flat tori and the scalar density of the singular part of the distributional Hessian of a point-distance function. It does not use the absolutely continuous Hessian away from the cut locus. Points where three or more minimizing geodesics meet are lower-dimensional strata and have zero \(\mathcal H^1\)-measure, so their pointwise jump values do not affect \(J_2\). The square-maximization statement is restricted to rectangular tori of fixed area; it does not assert an optimizer among all lattice shapes or in higher dimensions.

## Proof

At a regular point of the Voronoi facet \(F_v\), the two closest lifts of \(p\) are \(0\) and \(v\). The point \(x\in F_v\) satisfies \(|x|=|x-v|\), and the two one-sided gradients of the distance are \(x/|x|\) and \((x-v)/|x-v|\). Therefore
\[
j(x)=\frac{|v|}{|x|}.
\]
The reflection \(x\mapsto v-x\) preserves \(F_v\), so the facet is centered at \(v/2\). With \(e\) a unit vector perpendicular to \(v\), parameterize it as \(x=v/2+te\), where \(-\ell_v/2\le t\le\ell_v/2\). Then \(|x|^2=|v|^2/4+t^2\), and hence
\[
\begin{aligned}
\int_{F_v}j^2\,d\mathcal H^1
&=\int_{-\ell_v/2}^{\ell_v/2}\frac{|v|^2}{|v|^2/4+t^2}\,dt\\
&=4|v|\arctan\!\left(\frac{\ell_v}{|v|}\right).
\end{aligned}
\]
Opposite facets \(F_v\) and \(F_{-v}\) are identified in the quotient torus, so one representative from each opposite pair is counted. Intersections of facets have zero \(\mathcal H^1\)-measure. Summing the facet integrals proves the general formula.

For the rectangular lattice, the two relevant vectors can be chosen as \((2a,0)\) and \((0,2b)\), with corresponding facet lengths \(2b\) and \(2a\). Substitution gives
\[
J_2(T_{a,b})=8a\arctan(b/a)+8b\arctan(a/b).
\]
Now fix \(A=4ab\), put \(r=b/a>0\), and define
\[
h(r)=\frac{\arctan r}{\sqrt r}+\sqrt r\,\arctan(1/r).
\]
Then \(J_2=4\sqrt A\,h(r)\), and \(h(1/r)=h(r)\). Direct differentiation yields
\[
h'(r)=\frac{r\arctan(1/r)-\arctan r}{2r^{3/2}}+\frac{1-r}{\sqrt r(1+r^2)}.
\]
For \(r>1\), set \(q(r)=r\arctan(1/r)-\arctan r\). We have \(q(1)=0\) and
\[
q'(r)=\arctan(1/r)-\frac{r+1}{1+r^2}<\frac1r-\frac{r+1}{1+r^2}<0,
\]
where the last inequality follows from \(r>1\). Thus \(q(r)<0\) for \(r>1\), and both terms in the displayed formula for \(h'(r)\) are negative. Hence \(h\) is strictly decreasing on \((1,\infty)\). Its symmetry under \(r\mapsto1/r\) proves that its unique maximum is at \(r=1\). Since \(h(1)=\pi/2\), the maximum is \(J_2=2\pi\sqrt A\).

## Verification

The facet integral is evaluated exactly, with no numerical approximation. The derivative sign establishes a strict global maximum over the full rectangular aspect-ratio range, rather than only a local extremum. The claim is limited to the stated two-dimensional flat and rectangular settings.

## Relationship to prior work

Mantegazza, Mascellani, and Uraltsev give the general singular-measure formula for the distributional Hessian of a Riemannian distance function. Zhou gives a facetwise distributional-Hessian formula for radial distance kernels on flat tori and studies distance-energy extremizers. Those works supply the local jump-density framework, but the inspected statements do not give the squared cut-locus jump integral above or its fixed-area rectangular maximizer. The contribution here is the explicit global aggregation and the sharp shape comparison; the local jump formula itself is not claimed as new.

## Limitations

No optimization over nonrectangular lattice shapes is asserted. No higher-dimensional analogue, stability estimate near the square, or downstream PDE theorem is proved. The relevance to weak geometric analysis is as a natural exact measure of the concentration of the singular Hessian density on a cut locus; applications to discretization or stability would require separate work.

## References

1. C. Mantegazza, G. Mascellani, and G. Uraltsev, “On the Distributional Hessian of the Distance Function,” arXiv:1303.1421 (first submitted 2013-03-06); *Pacific Journal of Mathematics* 270 (2014), 151–166. DOI: 10.2140/pjm.2014.270.151.
2. Y. Zhou, “Distance Energies and Negative Type of Flat Tori,” arXiv:2609.05622 (first submitted 2026-09-04), especially §3.1 and Theorem 3.3.
