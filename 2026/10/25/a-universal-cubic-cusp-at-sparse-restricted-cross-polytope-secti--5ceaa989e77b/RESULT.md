# A universal cubic cusp at sparse restricted cross-polytope sections

## Finding
For each integer \(n\ge3\), let
\[
B_1^n=\bigl\{x\in\mathbb R^n:\sum_{j=1}^{n}|x_j|\le1\bigr\},\qquad
M_n=\bigl\{a\in S^{n-1}:\sum_{j=1}^{n}a_j=0\bigr\},
\]
and let \(\Phi_n(a)\) be the \((n-1)\)-dimensional Euclidean volume of \(B_1^n\cap a^\perp\). Define the sparse normal and a unit collective tangent by
\[
p_n=\frac1{\sqrt2}(1,-1,0,\ldots,0),\qquad
r_n=\sqrt{\frac{n-2}{2n}},\qquad
h_n=\left(r_n,r_n,-\frac{2r_n}{n-2},\ldots,-\frac{2r_n}{n-2}\right).
\]
For the unit-speed spherical geodesic \(a_n(s)=p_n\cos s+h_n\sin s\), the **sharp two-sided asymptotic** is
\[
\boxed{\frac{\Phi_n(a_n(s))}{\Phi_n(p_n)}
 =1+\frac{n-8}{2n}s^2+C_n|s|^3+O_n(s^4),\qquad s\longrightarrow0,}
\]
where the strictly positive exact coefficient is
\[
\boxed{C_n=\frac{64(n-1)\,\Gamma(n-\tfrac12)}
{3\sqrt\pi\,n^{3/2}\sqrt{n-2}\,\Gamma(n)}.}
\]
In the critical dimension \(n=8\), the quadratic term vanishes and
\[
\boxed{\frac{\Phi_8(a_8(s))}{\Phi_8(p_8)}
=1+\frac{1001}{1024\sqrt3}|s|^3+O(s^4).}
\]
Thus the previously quadratically degenerate normal \(p_8\) is a **saddle**, not a local maximum: the displayed geodesic strictly raises the section volume for all sufficiently small nonzero \(s\), while a transverse geodesic strictly lowers it. Along the collective geodesic, section volume has two continuous derivatives but no third derivative at the origin. This is the missing local type at the exact second-variation threshold.

## Assumptions and scope
All dimensions \(n\ge3\) are fixed as \(s\to0\). The hyperplane is central and contains the barycenter of the positive facet of \(B_1^n\) because \(\sum a_j=0\). Both \(p_n\) and \(h_n\) lie in this constraint hyperplane, satisfy \(\|p_n\|_2=\|h_n\|_2=1\) and \(\langle p_n,h_n\rangle=0\). Hence \(a_n(s)\in M_n\) and \(s\) is spherical arclength. The error \(O_n(s^4)\) is two-sided and allows constants depending on \(n\). No global extremal assertion is made.

## Proof
The standard Fourier section formula, as used by Brazitikos and Pandis, is
\[
\Phi_n(a)=\frac{2^n}{\pi(n-1)!}I_n(a),\qquad
I_n(a)=\int_0^\infty\prod_{j=1}^n\frac{dt}{1+a_j^2t^2}.
\]
The positive prefactor cancels in the ratio. Put \(c=1/\sqrt2\), \(r=r_n\), \(z=-2r/(n-2)\), \(b=z^2=2/[n(n-2)]\), and \(m=n-2\). On the stated geodesic,
\[
I_n(a_n(s))=\int_0^\infty g(t,s)H(t,s)\,dt,
\]
where
\[
\begin{split}
g(t,s)&=\frac1{[1+(c\cos s+r\sin s)^2t^2]
[1+(-c\cos s+r\sin s)^2t^2]},\\
H(t,s)&=(1+b\sin^2s\,t^2)^{-m}.
\end{split}
\]
The two first denominator factors are exchanged by \(s\mapsto-s\), so \(g\) is even in \(s\). For sufficiently small \(|s|\), both first coordinate magnitudes are bounded away from zero. Consequently the ordinary Taylor expansion is uniform in \(t\ge0\), with an integrable remainder:
\[
 g(t,s)=g_0(t)+s^2g_2(t)+O_n\bigl(s^4(1+t^2)^{-2}\bigr),
\]
\[
 g_0(t)=\left(1+\frac{t^2}{2}\right)^{-2},\qquad
 g_2(t)=\frac{(2/n)t^2+((n-1)/n)t^4}{(1+t^2/2)^4}.
\]
Indeed, multiplying the two denominators gives
\[
 \left[1+(c^2\cos^2s+r^2\sin^2s)t^2\right]^2
 -4c^2r^2\cos^2s\sin^2s\,t^4;
\]
its coefficient of \(s^2\) is \(-2t^2/n-(n-1)t^4/n\), yielding the displayed \(g_2\).

Since \(|\sin^2s-s^2|=O(s^4)\), and \(\int_0^\infty t^2g_0(t)\,dt<\infty\), replacing \(H(t,s)\) by \(H_s(t)=(1+bs^2t^2)^{-m}\) changes its \(g_0\)-weighted integral by \(O_n(s^4)\). The same holds for the \(s^2g_2\) contribution because \(\int t^2|g_2(t)|dt<\infty\) and \(|H_s-1|\le mb s^2t^2\). Thus
\[
 I_n(a_n(s))=I_0+s^2I_2+E(s)+O_n(s^4),
\]
\[
\begin{split}
I_0&=\int_0^\infty g_0(t)dt=\frac{\pi\sqrt2}{4},\\
I_2&=\int_0^\infty[g_2(t)-mbt^2g_0(t)]dt,\\
E(s)&=\int_0^\infty g_0(t)
[(1+bs^2t^2)^{-m}-1+mbs^2t^2]dt.
\end{split}
\]
The quadratic coefficient simplifies, using \(mb=2/n\), to
\[
 I_2=\frac8n\int_0^\infty
\frac{t^4[2(n-3)-t^2]}{(t^2+2)^4}\,dt.
\]
The exact beta-moment identity
\[
 \int_0^\infty\frac{t^6}{(t^2+2)^4}dt
 =10\int_0^\infty\frac{t^4}{(t^2+2)^4}dt,
 \qquad\int_0^\infty\frac{t^4}{(t^2+2)^4}dt
 =\frac{\pi\sqrt2}{128}
\]
therefore gives \(I_2/I_0=(n-8)/(2n)\).

The cubic term comes from the large-\(t\) tail, so a formal fourth-order Taylor expansion under the integral would be invalid. Let
\[
F(u)=(1+bu^2)^{-m}-1+mbu^2\ge0.
\]
The inequality follows from convexity of \(x\mapsto(1+x)^{-m}\) on the nonnegative half-line. Moreover \(F(u)=O_n(u^4)\) near zero and \(F(u)=O_n(u^2)\) at infinity. Because \(g_0(t)=4/(t^2+2)^2\), changing variables \(u=|s|t\) gives
\[
E(s)=4|s|^3\int_0^\infty\frac{F(u)}{(u^2+2s^2)^2}\,du
=4J_m(b)|s|^3+O_n(s^4),
\]
where
\[
J_m(b)=\int_0^\infty\frac{(1+bu^2)^{-m}-1+mbu^2}{u^4}\,du.
\]
For the stated remainder, split the difference between \((u^2+2s^2)^{-2}\) and \(u^{-4}\) at \(u=|s|\), and use the two bounds for \(F\). The resulting difference is \(O_n(|s|)\) before multiplication by \(|s|^3\). In particular, \(J_m(b)\) is finite and strictly positive.

Twice integrating by parts, with vanishing boundary terms, evaluates this coefficient exactly:
\[
\begin{split}
J_m(b)&=\frac{2mb}{3}\int_0^\infty
\frac{1-(1+bu^2)^{-m-1}}{u^2}\,du\\
&=\frac{4m(m+1)b^2}{3}\int_0^\infty(1+bu^2)^{-m-2}\,du\\
&=\frac{2m(m+1)b^{3/2}\sqrt\pi}{3}
\frac{\Gamma(m+3/2)}{\Gamma(m+2)}.
\end{split}
\]
Dividing \(I_0+s^2I_2+4J_m(b)|s|^3+O_n(s^4)\) by \(I_0=\pi\sqrt2/4\), and substituting \(m=n-2\) and \(b=2/[n(n-2)]\), gives the announced \(C_n\). At \(n=8\), the gamma identities reduce this exactly to \(1001/(1024\sqrt3)>0\).

For the negative direction needed to establish the saddle, set
\[
v=(0,0,1,-1,0,\ldots,0)/\sqrt2\in T_{p_8}M_8.
\]
For \(p_8\cos s+v\sin s\), the integral becomes
\[
\int_0^\infty\frac{dt}{
(1+\tfrac12\cos^2s\,t^2)^2
(1+\tfrac12\sin^2s\,t^2)^2}.
\]
Its integrable quadratic Taylor coefficient is \(-t^4/[2(1+t^2/2)^3]\). Another beta integral yields the ratio \(1-3s^2/2+o(s^2)\), strictly below one for small nonzero \(s\). Combining both directions proves that \(p_8\) is a saddle. Differentiation of the original integral up to order two is locally dominated: derivatives of \(g\) decay as \(O_n((1+t^2)^{-2})\), while the first two derivatives of \(H\) are bounded by \(O_n(t)\) and \(O_n(t^2)\), respectively; after multiplication by \(g\), these are integrable. Thus the restricted volume profile is \(C^2\). The nonzero even term \(C_8|s|^3\) is incompatible with a third-order Taylor expansion having one cubic coefficient on both sides, so the profile is not \(C^3\) at zero.

## Verification
The accompanying standalone file `artifacts/verify_cusp.py` reconstructs the two beta moments and the closed critical coefficient symbolically using SymPy, then independently evaluates the original unexpanded Fourier integral with high-precision mpmath quadrature for six dimensions on two shrinking geodesic steps. It confirms positive cubic residuals and convergence to the analytic \(C_n\), including two-sided volume increase at \(n=8\). Run `python artifacts/verify_cusp.py` after installing packages specified in `artifacts/requirements.txt`; successful execution prints `VERIFY_OK`. Finite quadrature is a consistency check; the universal result is proved by the explicit integral analysis above.

## Relationship to prior work
Brazitikos and Pandis introduce the constrained cross-polytope problem, provide its Fourier-integral volume representation, establish the global minimum and formulate a conjecture for the global maximum. Their Section 5 does not give the third-order behavior at the sparse normal.

The independently published note *Exact local Hessian phase diagram for two conjectural cross-polytope section maximizers* computes the complete **quadratic** spectrum at \(p_n\), namely \(-3\) transversely and \((n-8)/n\) collectively. It explicitly leaves the critical dimension \(n=8\) unresolved beyond second order. Here the new \(C_n|s|^3\) term is strictly positive and resolves that case; a vanishing Hessian cannot determine its sign or magnitude. The present all-dimensional cubic coefficient also describes the first non-smooth correction in the natural collective direction.

Nayar and Tkocz establish log-concavity under coordinate dilations of a **fixed** cross-polytope section. Their geometric parameter is not the varying facet-barycenter normal considered here, so that theorem does not imply the cubic coefficient. These comparisons are about statements and parameter domains, not just titles.

## Limitations
Only the displayed geodesic receives an exact cubic expansion; no claim is made that this gives a complete multivariate third-order normal form. The global maximum among constrained normals remains an open problem. The result uses a fixed-dimensional \(s\to0\) limit, not a uniform large-dimension remainder estimate. Earlier work already gave the quadratic Hessian away from the exceptional dimension; those conclusions are not claimed as new. Unindexed historical treatments of local section-volume regularity may contain equivalent calculations.

## References
1. S. Brazitikos and C. Pandis, *Restricted Hyperplane Sections of the Cross-Polytope and the Simplex*, arXiv:2606.07163v1 (first posted 2026-06-05), especially Section 5, Theorem 5.1 and Conjecture 5.2; https://arxiv.org/abs/2606.07163.
2. *Exact local Hessian phase diagram for two conjectural cross-polytope section maximizers*, public research note (2026-10-04); https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-local-hessian-phase-diagram-for-two-conjectural-cross-poly--77988d83412a.
3. P. Nayar and T. Tkocz, *On a convexity property of sections of the cross-polytope*, Proceedings of the American Mathematical Society **148** (2020), 1271–1278, DOI:10.1090/proc/14777; https://arxiv.org/abs/1810.02038.
