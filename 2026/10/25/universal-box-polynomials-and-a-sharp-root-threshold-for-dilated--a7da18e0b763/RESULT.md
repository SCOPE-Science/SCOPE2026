# Universal box polynomials and a sharp root threshold for dilated empty tetrahedra

## Finding
Let \(S\subset\mathbb R^3\) be **any empty lattice tetrahedron** with normalized volume \(m=6\operatorname{vol}_3(S)\ge2\): its only lattice points are its four vertices. For every integer \(r\ge1\), define \(a=a_{m,r}\), \(b=b_{m,r}\) by
\[
a=\frac{mr(r^2-1)}6-(r-1)^2,\qquad
b=\frac{mr(2r^2+1)}3-2r^2+2r-1.
\]
Then the local Ehrhart (box) polynomial of the dilate \(rS\) is
\[
\boxed{\ell^*(rS;z)=az+bz^2+az^3.}
\]
This entire polynomial depends only on \(m\) and \(r\), not on the shape or lattice-equivalence class of \(S\). At \(r=1\), it is \((m-1)z^2\). At every \(r\ge2\), both gamma coefficients in
\[
\boxed{\ell^*(rS;z)=a z(1+z)^2+
\left(\frac{mr(r^2+2)}3-2r+1\right)z^2}
\]
are **strictly positive**. Consequently the roots of the box polynomial are simple: one is zero, while the other two are strictly negative.

The ordinary Ehrhart numerator has three simple negative roots for every \(r\ge2\), and it has nonreal roots at \(r=1\). At the sharp borderline,
\[
\boxed{\ell^*(2S;z)=(m-1)z+(6m-5)z^2+(m-1)z^3,}
\]
\[
\boxed{h^*(2S;z)=(1+6z+z^2)(1+(m-1)z).}
\]
Thus \(r=2\) is the smallest positive integer dilation with **simultaneously simple real roots** for the ordinary numerator and box polynomial throughout this entire nonunimodular family.

## Assumptions and scope
A lattice tetrahedron is *empty* if it has no lattice points except its vertices; this includes the boundary. The normalized volume is a positive integer. Here \(m\ge2\) excludes unimodular tetrahedra, for which the local polynomial has different onset behavior. All dilations \(r\) are about the origin; lattice translation does not change either polynomial.

For any simplex \(T=\operatorname{conv}(w_0,w_1,w_2,w_3)\) with integer vertices, the **local box polynomial** is the finite lattice-point enumerator
\[
\ell^*(T;z)=\sum_{u\in\Pi_T^\circ\cap\mathbb Z^4} z^{u_4},\quad
\Pi_T^\circ=\left\{\sum_{i=0}^3\lambda_i(w_i,1):0<\lambda_i<1\right\}.
\]
The ordinary numerator is defined by
\[
\sum_{t\ge0}|tT\cap\mathbb Z^3|z^t=\frac{h^*(T;z)}{(1-z)^4}.
\]
Throughout, real-rootedness of \(h^*\) refers to all its nonzero polynomial roots, and **simple** means no repeated root. The box polynomial is allowed its intrinsic zero root.

## Proof
**1. Universal Ehrhart polynomial.** Since an empty tetrahedron has exactly four lattice points, the coefficient of \(z\) in its ordinary Ehrhart numerator is zero. Ehrhart reciprocity makes its top-degree coefficient zero as well. The constant coefficient is one, and the sum of all coefficients equals normalized volume \(m\). Therefore
\[
h^*(S;z)=1+(m-1)z^2.
\]
Equivalently, for every nonnegative integer \(t\),
\[
L_S(t)=\binom{t+3}{3}+(m-1)\binom{t+1}{3}
=\frac m6t^3+t^2+\frac{12-m}{6}t+1.
\]
For any integer \(r\ge1\), \(L_{rS}(t)=L_S(rt)\). The exact numerator coefficient extraction
\[
[z^j]h^*(rS;z)=\sum_{i=0}^j(-1)^{j-i}\binom4{j-i}L_S(ri),\quad 0\le j\le3,
\]
gives
\[
\begin{split}
h^*(rS;z)={}&1+\left[\frac{mr(r^2-1)}6+(r-1)(r+3)\right]z\\
&+\left[\frac{mr(2r^2+1)}3-4r+3\right]z^2\\
&+\left[\frac{mr(r^2-1)}6-(r-1)^2\right]z^3.
\end{split}
\]
This establishes shape-independence of the ordinary numerator without assuming all empty tetrahedra are unimodularly equivalent.

**2. Open-box inclusion-exclusion.** The closed, half-open, and open fundamental parallelepiped enumerators give, by assigning each integral representative to the unique relative interior of a face, the Boolean-face identity
\[
\ell^*(T;z)=\sum_{F\text{ face of }T}(-1)^{3-\dim F}h^*(F;z),
\]
with \(h^*(\varnothing;z)=1\), for a three-dimensional simplex \(T\). Every facet of an empty lattice tetrahedron is unimodular in its induced plane lattice: each facet has exactly its three vertices as lattice points, so Pick's theorem gives normalized facet area one. Every edge is primitive for the same reason. Consequently, after scaling by \(r\), all four facets are lattice-equivalent to \(r\Delta_2\), and all six edges to \(r\Delta_1\). Their Ehrhart numerators are
\[
h^*(r\Delta_2;z)=1+\frac{(r-1)(r+4)}2z+\frac{(r-1)(r-2)}2z^2,\qquad
h^*(r\Delta_1;z)=1+(r-1)z.
\]
In the Boolean-face identity, four vertices contribute \(1\) each, and the empty face contributes another \(1\) with opposite parity. Hence
\[
\ell^*(rS;z)=h^*(rS;z)-4h^*(r\Delta_2;z)
+6h^*(r\Delta_1;z)-4+1.
\]
Substitution and collection of the three nonzero coefficients yields exactly \(az+bz^2+az^3\) as stated. For \(r=1\), the result reduces to \((m-1)z^2\).

**3. Sharp gamma-positivity and box roots.** For \(m\ge2\) and \(r\ge2\),
\[
a\ge\frac{(r-1)(r^2-2r+3)}3>0,
\]
and
\[
c:=b-2a=\frac{mr(r^2+2)}3-2r+1
\ge\frac{2r^3-2r+3}{3}>0.
\]
Thus \(\ell^*(rS;z)=z[az^2+(2a+c)z+a]\), whose quadratic discriminant is \(c(4a+c)>0\). Both quadratic roots are strictly negative because all three coefficients are positive. Neither is zero, so together with the single factor \(z\) these are three **distinct real** roots. The expression \(az(1+z)^2+cz^2\) is the strict gamma-positive expansion. At \(r=1\), zero has multiplicity two instead, proving the onset is sharp for the local polynomial.

**4. Ordinary numerator roots.** Direct substitution at \(r=2\) gives
\[
h^*(2S;z)=(1+6z+z^2)(1+(m-1)z).
\]
The quadratic roots are \(-3\pm2\sqrt2\); the third is the rational number \(-1/(m-1)\). These are all negative and pairwise different for every integer \(m\ge2\). For all \(r\ge3\), Jochemko's Veronese real-root theorem applies to the initial numerator of degree \(2\), and guarantees three distinct negative roots. At \(r=1\), \(h^*(S;z)=1+(m-1)z^2\), with nonreal roots. This proves the sharp simultaneous threshold.

## Verification
A dependency-free Python checker (`verify.py`) independently enumerates lattice points in dilated tetrahedra of the form \(\operatorname{conv}(0,e_1,e_2,(1,p,m))\), with \(2\le m\le10\), \(1\le p<m\), and \(\gcd(p,m)=1\), for \(1\le r\le4\). It computes ordinary numerators by integer-point interpolation and computes local box coefficients by directly enumerating *strictly positive and less-than-one* barycentric coordinates, without using the inclusion-exclusion identity. It also verifies the two borderline formulas for \(2\le m\le100\). Command: `python3 verify.py`.

The executed checker returned: `EXACT_OK parameter_cases=124 empty_tetra_shapes=31 box_points=19368 hstar_interpolation=True`. These finite checks support the formulas but do not establish them for all parameters; the argument above does.

## Relationship to prior work
Nill (2026) proves that sufficiently large lattice width forces real-rooted local box and ordinary Ehrhart numerators, but does not give a sharp dimension-three threshold for dilates of empty tetrahedra. The present theorem resolves that threshold in this specific family, without asserting a general width bound for other lattice simplices. Jochemko (2018) proves real-rootedness of ordinary Ehrhart numerators at dilation at least their numerator degree and simplicity for dilation exceeding that degree. Our borderline ordinary factorization is consistent with this theorem but establishes simplicity at dilation two for this special **integer-volume** family. The explicit box polynomial and its strict gamma-positive classification are additional claims not contained in the cited Veronese theorem.

Bajo–Braun–Codenotti–Hofscheier–Vindas-Meléndez study local box polynomials of one-row Hermite-normal-form simplices and their asymptotic distributions. Their formulas may be used for many particular simplices, but their inspected classifications do not state the all-empty-tetrahedra, all-dilation formula or the sharp two-dilation root onset. The classical Reeve Ehrhart numerator, recalled for example by Liu–Tao–Xin (2026), is an input-level special case rather than the present local dilation classification.

## Limitations
The theorem is restricted to dimension three, **empty** tetrahedra of normalized volume at least two, and integer dilations. It does not determine the optimal lattice-width threshold among arbitrary three-dimensional simplices, and it does not claim that all empty tetrahedra have the same lattice shape. The proof of ordinary strict real-rootedness for \(r\ge3\) uses the cited Veronese theorem; the local polynomial is proved directly. Although targeted literature and database comparisons found no already-published equivalent all-parameter classification, historical priority is not guaranteed, especially under older HNF and local-box terminology. The accompanying finite checker is not an independent audit.

## References
1. Benjamin Nill, *Lattice polytopes of large width have real-rooted Ehrhart \(h^*\)-polynomials*, arXiv:2608.03635v1 (first public 2026-08-04), Theorems 1.1 and 1.2. https://arxiv.org/abs/2608.03635
2. Katharina Jochemko, *On the real-rootedness of the Veronese construction for rational formal power series*, arXiv:1602.09139, 2018 journal version, Theorem 1.1 and Corollary 4.4. https://arxiv.org/abs/1602.09139
3. E. Bajo, B. Braun, G. Codenotti, J. Hofscheier and A. R. Vindas-Meléndez, *Local \(h^*\)-polynomials for one-row Hermite normal form simplices*, arXiv:2309.01186v4. https://arxiv.org/abs/2309.01186
4. S. Liu, Q. Tao and X. Xin, *Explicit Construction of Polytopes whose Ehrhart Polynomials Realize any Given Sign Pattern*, arXiv:2605.23544v2, introductory Reeve tetrahedron example. https://arxiv.org/abs/2605.23544
