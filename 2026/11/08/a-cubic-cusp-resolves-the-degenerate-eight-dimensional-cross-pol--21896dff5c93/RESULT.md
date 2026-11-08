# A cubic cusp resolves the degenerate eight-dimensional cross-polytope section

## Finding
Let \(B_1^8=\{x\in\mathbb R^8:\sum_{j=1}^8|x_j|\le1\}\), let
\(M=\{a\in\mathbb R^8:\sum_j a_j=0,\ \|a\|_2=1\}\), and put
\(V(a)=\operatorname{vol}_7(B_1^8\cap a^\perp)\). The constraint on \(a\) means that the section contains the barycenter of the facet \(\operatorname{conv}\{e_1,\ldots,e_8\}\).

Write
\[
p=\frac1{\sqrt2}(1,-1,0,0,0,0,0,0),\quad
h=\left(\sqrt{\frac38},\sqrt{\frac38},-\frac1{\sqrt{24}},\ldots,-\frac1{\sqrt{24}}\right),\quad
k=\frac1{\sqrt2}(0,0,1,-1,0,0,0,0),
\]
where the last value in \(h\) is repeated six times. For \(-1<s<1\) define the two feasible great-circle parametrizations
\[
a_+(s)=\sqrt{1-s^2}\,p+sh,\qquad a_-(s)=\sqrt{1-s^2}\,p+sk.
\]
Then, as \(s\to0\),
\[
\boxed{\frac{V(a_+(s))}{V(p)}=1+\frac{1001\sqrt3}{3072}|s|^3+O(s^4)},\qquad
\boxed{\frac{V(a_-(s))}{V(p)}=1-\frac32s^2+o(s^2)}.
\]
In particular \(p\) is a **saddle**, neither a local maximum nor a local minimum, of the facet-barycenter restricted cross-polytope section-volume functional in dimension eight. Along the one-dimensional null-Hessian direction its first nonzero correction is a positive, nonanalytic cubic absolute-value term, not an ordinary quartic correction.

## Assumptions and scope
Everything concerns the Euclidean eight-dimensional unit \(\ell_1\) ball and normals with both unit Euclidean norm and coordinate sum zero. Both vectors \(h,k\) have unit norm and sum zero, and both are orthogonal to \(p\). Thus the two displayed paths remain in \(M\) for all \(|s|<1\). The statement is local at the sparse normal \(p\), and makes no assertion about a global maximizing normal.

## Proof
The standard cross-polytope section formula, recalled by Brazitikos--Pandis, is
\[
V(a)=\frac{2^8}{\pi7!}I(a),\qquad
I(a)=\int_0^\infty\prod_{j=1}^8\frac{du}{1+a_j^2u^2}.
\]
The positive proportionality constant cancels in ratios. At \(p\),
\[
A_0(u):=\prod_j(1+p_j^2u^2)^{-1}=(1+u^2/2)^{-2},\qquad
I(p)=\int_0^\infty A_0(u)\,du=\frac{\pi\sqrt2}{4}.
\]
For the collective path \(a_+\), its two initially nonzero coordinates satisfy
\[
a_{+,1}^2+a_{+,2}^2=1-\frac{s^2}{4},\qquad
a_{+,1}a_{+,2}=-\frac12+\frac78s^2,
\]
while the other six squared coordinates equal \(s^2/24\). Hence
\[
I(a_+(s))=\int_0^\infty A(s,u)B(s,u)\,du,
\]
\[
A(s,u)=\frac{1}{1+(1-s^2/4)u^2+(1/4-7s^2/8+49s^4/64)u^4},\quad
B(s,u)=(1+s^2u^2/24)^{-6}.
\]
For small \(|s|\), the denominator of \(A\) is uniformly comparable with \((1+u^2)^2\). Therefore its expansion in \(s^2\) is uniformly integrable:
\[
A(s,u)=A_0(u)+s^2 A_2(u)+R(s,u),\quad
A_2(u)=\frac{u^2/4+7u^4/8}{(1+u^2/2)^4},\quad
\int_0^\infty|R(s,u)|\,du=O(s^4).
\]
The bound \(|B(s,u)-1|\le s^2u^2/4\), together with the integrability of \(u^2A_2(u)\), gives
\[
I(a_+(s))-I(p)=s^2\int_0^\infty A_2(u)\,du
+\int_0^\infty A_0(u)(B(s,u)-1)\,du+O(s^4).
\]
The exact beta integrals
\[
\int_0^\infty A_2(u)\,du
=\frac14\int_0^\infty u^2A_0(u)\,du
=\frac{\pi\sqrt2}{8}
\]
show cancellation of the quadratic term. Consequently
\[
I(a_+(s))-I(p)=\int_0^\infty A_0(u)
\left[(1+s^2u^2/24)^{-6}-1+\frac{s^2u^2}{4}\right]du+O(s^4).
\]
Here the bracket is nonnegative and is \(O(s^4u^4)\) when \(|su|\) is bounded. Split the integral at \(u=1\) and use \(A_0(u)=4u^{-4}+O(u^{-6})\) on \(u\ge1\). The error from replacing \(A_0\) by \(4u^{-4}\) there, including the contribution from \(u<1\), is \(O(s^4)\). The substitution \(v=|s|u/\sqrt{24}\) therefore gives
\[
I(a_+(s))-I(p)=\frac{4|s|^3}{24^{3/2}}J+O(s^4),\quad
J=\int_0^\infty\frac{(1+v^2)^{-6}-1+6v^2}{v^4}\,dv.
\]
Twice integrating by parts (with vanishing boundary terms) yields
\[
J=4\int_0^\infty\frac{1-(1+v^2)^{-7}}{v^2}\,dv
=56\int_0^\infty(1+v^2)^{-8}\,dv
=\frac{3003\pi}{512}.
\]
Dividing by \(I(p)=\pi\sqrt2/4\) proves the positive cubic coefficient \(1001\sqrt3/3072\).

For the transverse path \(a_-\) the integral is instead
\[
I(a_-(s))=\int_0^\infty
(1+(1-s^2)u^2/2)^{-2}(1+s^2u^2/2)^{-2}\,du.
\]
The derivative with respect to \(s^2\) at zero is integrable and equals
\[
A_0(u)\left(\frac{u^2}{1+u^2/2}-u^2\right)
=-\frac{4u^4}{(u^2+2)^3}.
\]
Dominated convergence and another beta integral give
\[
\lim_{s\to0}\frac{I(a_-(s))-I(p)}{s^2}
=-\int_0^\infty\frac{4u^4}{(u^2+2)^3}\,du
=-\frac{3\pi\sqrt2}{8}.
\]
After normalization this is \(-3/2\). Thus arbitrarily close feasible normals have both larger and smaller section volumes than at \(p\), proving the saddle claim.

## Verification
Running \(\texttt{python verify_saddle.py}\) with SymPy and mpmath reproduces the exact beta integrals, tangent-vector constraints, cancellation of the collective quadratic term, the two exact coefficients, and supplementary high-precision evaluations at three positive perturbation parameters. Its successful terminal line is \(\texttt{SADDLE_EXACT_OK}\). The cubic term is proved by the displayed uniform integral estimates, not by finite sampling or extrapolation.

## Relationship to prior work
Brazitikos--Pandis introduced the facet-barycenter restricted section problem and their Conjecture 5.2 concerns the global maximizing normal. The previously published *Exact local Hessian phase diagram for two conjectural cross-polytope section maximizers* computes the spectrum at \(p_n\) and, in dimension eight, obtains a one-dimensional quadratic null direction, explicitly leaving its higher-order sign unresolved. A vanishing quadratic form cannot determine a local extremum. The present positive \(|s|^3\) correction resolves precisely that borderline case; it is not implied by the Hessian alone. Nayar--Tkocz's strong B-inequality concerns coordinate dilations of a fixed section and does not furnish the stated constrained-normal perturbation expansion.

## Limitations
This local saddle classification does not determine the global maximizing section, classify other critical normals, or assert anything about other dimensions. The integral representation and lower-order Hessian are known, not claimed as new. Independent validation and definitive historical-priority assessment remain outstanding.

## References
1. S. Brazitikos and C. Pandis, *Restricted Hyperplane Sections of the Cross-Polytope and the Simplex*, arXiv:2606.07163v1 (first posted 2026-06-05), Section 5 and Conjecture 5.2, https://arxiv.org/abs/2606.07163.
2. *Exact local Hessian phase diagram for two conjectural cross-polytope section maximizers*, published research record (2026-10-04), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-local-hessian-phase-diagram-for-two-conjectural-cross-poly--77988d83412a.
3. P. Nayar and T. Tkocz, *On a convexity property of sections of the cross-polytope*, Proc. Amer. Math. Soc. 148 (2020), 1271–1278, arXiv:1810.02038, DOI:10.1090/proc/14777.
