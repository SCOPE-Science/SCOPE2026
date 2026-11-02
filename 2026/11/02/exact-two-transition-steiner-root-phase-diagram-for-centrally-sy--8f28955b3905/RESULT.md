# Exact two-transition Steiner-root phase diagram for centrally symmetric circular bicones

## Finding
Let \(D_R=\{(u,v,0):u^2+v^2\le R^2\}\subset\mathbb R^3\), and for \(R,h>0\) let
\[
K_{R,h}=\operatorname{conv}\left(D_R\cup\{(0,0,h),(0,0,-h)\}\right).
\]
This is a solid, centrally symmetric right circular **bicone** (two congruent cones joined along the equatorial disk). Put \(x=h/R\) and define
\[
a(x)=x+\arctan(1/x),\qquad
b(x)=\sqrt{1+x^2},\qquad
q(x)=\sqrt{a(x)^2-2b(x)}.
\]
The expression under the last square root is strictly positive for all \(x>0\). Introduce the two transition functions
\[
\Phi_\pm(x)=a(x)^3-3a(x)b(x)+2x\pm q(x)^3.
\]
**Both transition functions are strictly increasing, with one zero each.** Let \(x_2\) denote the unique positive root of \(\Phi_+\), and \(x_1\) the unique positive root of \(\Phi_-\). Exact rational certificates give
\[
\frac12<x_2<\frac35<\frac{23}{20}<x_1<\frac65,
\]
and supplemental numerical approximations are
\[
x_2=0.569760013853177\ldots,\qquad x_1=1.189944916110692\ldots.
\]
For the ordinary three-dimensional Euclidean Steiner polynomial \(f_{K_{R,h}}(t)=\operatorname{Vol}_3(K_{R,h}+t\mathbb B_3)\), considered as a polynomial over the complex numbers, the root-type classification is exact:

* If \(0<x<x_2\), there is one simple negative real root and a nonreal conjugate pair.
* If \(x=x_2\), there is a negative double root at \(t=-R(a+q)/2\) and one distinct negative simple root.
* If \(x_2<x<x_1\), all three roots are distinct, negative, and real.
* If \(x=x_1\), there is a negative double root at \(t=-R(a-q)/2\) and one distinct negative simple root.
* If \(x>x_1\), there is one simple negative real root and a nonreal conjugate pair.

Thus axial stretching of a **centrally symmetric** family exhibits the exact reentrant pattern complex--real--complex, with two and only two sharp transition aspects.

## Assumptions and scope
All bodies are nondegenerate: \(R>0\) and \(h>0\). The disk belongs to the solid convex hull, not to the external surface. Distances and parallel offsets are Euclidean, and \(\mathbb B_3\) denotes the unit ball. The ordinary Steiner polynomial is
\[
f_K(t)=V(K)+S(K)t+M(K)t^2+\frac{4\pi}{3}t^3,
\]
where \(V\) is volume, \(S\) surface area, and \(M=2\pi\bar w\), with \(\bar w\) the rotationally averaged width. Roots are counted with multiplicities, and repeated roots at the transition values are ordinary double roots.

## Proof
**1. Exact Steiner coefficients.** By elementary cone geometry,
\[
V(K_{R,h})=\frac{2\pi}{3}R^2h,\qquad
S(K_{R,h})=2\pi R\sqrt{R^2+h^2}.
\]
For a unit vector with absolute axial cosine \(u\in[0,1]\), central symmetry and the support function give the directional width
\[
w(u)=2\max\{R\sqrt{1-u^2},hu\}.
\]
The absolute axial cosine is uniform on \([0,1]\). The switch occurs at \(u_0=(1+x^2)^{-1/2}\), and direct integration yields
\[
\bar w=2R\left(\int_0^{u_0}\!\sqrt{1-u^2}\,du+\int_{u_0}^{1}\!xu\,du\right)
=R\bigl[x+\arctan(1/x)\bigr]=Ra(x).
\]
Hence \(M(K_{R,h})=2\pi Ra(x)\). On setting \(z=t/R\), the exact normalized polynomial is
\[
\boxed{\ \frac{f_{K_{R,h}}(Rz)}{2\pi R^3}
=F_x(z)=\frac23z^3+a(x)z^2+b(x)z+\frac{x}{3}.\ }
\]

**2. Two distinct negative stationary points.** The three-dimensional Minkowski inequality \(M(K)^2\ge4\pi S(K)\) has equality only for a Euclidean ball. No nondegenerate bicone is a ball. Substituting the coefficients therefore gives \(a^2>2b\), so \(q>0\), and \(q<a\). The derivative of the normalized polynomial factors as
\[
F_x'(z)=2z^2+2az+b=2(z-z_-)(z-z_+),
\quad z_-=\frac{-a-q}{2}<z_+=\frac{-a+q}{2}<0.
\]
Substitution at these two critical points yields the exact identities
\[
6F_x(z_-)=\Phi_+(x),\qquad 6F_x(z_+)=\Phi_-(x).
\]
The first critical point is a strict local maximum, the second a strict local minimum. Since \(F_x(-\infty)=-\infty\), \(F_x(0)=x/3>0\), and all coefficients are positive, the two critical values determine exactly which of the stated negative-real, double-real, and conjugate-pair alternatives occurs. In particular, \(q>0\) excludes triple roots.

**3. Strict monotonicity of the transition functions.** Set \(v=x/b(x)\). Straight differentiation gives
\[
a'=v^2,\qquad b'=v,\qquad q'=\frac{v(av-1)}{q}.
\]
Algebra using \(q^2=a^2-2b\) simplifies the two derivatives to the positive-square identities
\[
\boxed{\ \Phi_\pm'(x)=\frac12+\frac32\left[v(x)\bigl(a(x)\pm q(x)\bigr)-1\right]^2>0.\ }
\]
These identities prove strict increase, rather than relying on numerical plots or sampled signs.

**4. Existence, ordering, and uniqueness of transitions.** As \(x\to0^+\), put \(p=\pi/2\) and \(q_0=\sqrt{p^2-2}\). Then
\[
\lim_{x\to0^+}\Phi_\pm(x)=p(p^2-3)\pm q_0^3.
\]
Because \(2<p^2<8/3<3\), the common first term is negative. Furthermore,
\[
p^2(p^2-3)^2-(p^2-2)^3=8-3p^2>0,
\]
so even \(\Phi_+(0^+)<0\). The derivative identities imply \(\Phi_\pm'(x)>1/2\) at every \(x>0\); hence both functions eventually become positive and have exactly one positive zero. Since
\[
\Phi_+(x)-\Phi_-(x)=2q(x)^3>0,
\]
the zero of \(\Phi_+\) strictly precedes the zero of \(\Phi_-\).

Finally, exact rational interval arithmetic using Machin's identity for \(\pi\), alternating arctangent series, and integer-square-root bounds verifies
\[
\Phi_+(1/2)<0<\Phi_+(3/5),
\qquad
\Phi_-(23/20)<0<\Phi_-(6/5).
\]
This proves the displayed strict rational brackets. The unique zeros, critical-value identities, and cubic shape complete the classification.

## Verification
The included `verify_bicone.py` is a standalone Python 3 verifier. Its exact-rational interval arithmetic checks all four strict transition signs and the limiting sign, with \(\pi\) bounded by the alternating Machin-arctangent formula. Square-root intervals are validated with integer-square comparisons. If SymPy is present, additional independent symbolic checks verify the cubic discriminant, both perfect-square derivative identities, and both critical-value identities. All these checks were executed from the packaged code and passed. The analytical argument proves strict monotonicity for every real \(x>0\); finite sign checks alone would not do so.

## Relationship to prior work
The ordinary Steiner polynomial and its root-location inequalities are classical. Henk and Hernández Cifre (2007/2008) analyze root bounds and geometric consequences for convex bodies, without this bicone root-type diagram. Hernández Cifre and Saorín (2007) establish the general three-dimensional Type 1/Type 2/root-real classification; the original full article was not accessible for this review, although bibliographic and abstract material was inspected. Later cone work treats *single right circular cones* with a planar base face and develops a separate two-transition diagram. The bicone is centrally symmetric, has no exterior planar base face, has a different Steiner polynomial, and the two transition values and monotonicity identities above do not follow by substitution into that single-cone theorem. Related circular-cylinder, tall-pyramid, and prism classifications also concern different solids. The exact bicone statement is not asserted to resolve general real-rootedness for centrally symmetric convex bodies.

## Limitations
The theorem covers only symmetric right circular bicones. It does not classify asymmetric, tilted, elliptical, or higher-dimensional double cones. The critical aspect ratios are rigorously specified as unique zeros of explicit smooth functions, not by an elementary closed form; the decimal approximations are supplementary. The most relevant 2007 three-dimensional root-classification paper was not fully accessible, and earlier unindexed computations could affect historical priority.

## References
1. M. Henk and M. A. Hernández Cifre, *Notes on the roots of Steiner polynomials*, arXiv:math/0703373 (initial public submission 13 March 2007); *Rev. Mat. Iberoam.* **24** (2008), 631–644, DOI: 10.4171/RMI/550.
2. M. A. Hernández Cifre and E. Saorín, *On the roots of the Steiner polynomial of a 3-dimensional convex body*, *Advances in Geometry* **7** (2007), 275–294, DOI: 10.1515/advgeom.2007.016.
3. E. Saorín Gómez, *On inner parallel bodies. From the Steiner polynomial to Poincaré inequality*, doctoral thesis, Universidad de Murcia (2008), relevant single-cone examples.
4. *Complete two-transition Steiner-root phase diagram for right circular cones*, public research record (2026), corresponding single-cone theorem.
