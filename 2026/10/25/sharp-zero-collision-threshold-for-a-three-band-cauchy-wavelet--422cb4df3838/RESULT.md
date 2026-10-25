# Sharp zero-collision threshold for a three-band Cauchy wavelet

## Finding

Let \(0<c<a<b\), and let \(f=\mathbf 1_E\) for the symmetric three-band set
\[
E=[-b,-a]\cup[-c,c]\cup[a,b].
\]
For \(\operatorname{Im}z>0\) consider the order-one analytic Cauchy-wavelet representative
\[
F_{a,b,c}(z)=\int_E\frac{dt}{(z-t)^2}.
\]
Its nonzero scalar multiple at \(z=x+iy\) is the continuous wavelet transform at position \(x\) and scale \(y>0\) for the Cauchy wavelet of Fourier multiplier proportional to \(\xi e^{-\xi}\mathbf1_{\xi>0}\). Hence its zeros and multiplicities are independent of that nonzero normalization.

Put \(r=a/b\), \(s=c/b\), and
\[
L=r^2+6r+1,\qquad
s_*(r)=\frac{2r(1-r)}{L+\sqrt{L^2+4r(1-r)^2}}.
\]
Then \(0<s_*(r)<r\), and \(F_{a,b,c}\) has **exactly two zeros in the open upper half-plane counted with analytic multiplicity**, with the following complete classification:

* For \(0<s<s_*(r)\), the two zeros are distinct, simple, and on the positive imaginary axis.
* At \(s=s_*(r)\), the two zeros coalesce into a single **double** zero on the positive imaginary axis.
* For \(s_*(r)<s<r\), the zeros are distinct, simple, and off the imaginary axis, of the form \(\pm x+iy\) with \(x,y>0\).

All the zero coordinates are algebraic, as explicitly determined in the proof. The collision is transverse: if \(r\in(0,1)\) is fixed and \(s\downarrow s_*(r)\) from above, the real-part displacement is a strictly positive constant times \(\sqrt{s-s_*(r)}\). In particular, for \(r=2/5\) the transition is exactly at \(s_*=1/15\), the double zero is \(z=i b\sqrt3/5\), and
\[
\frac{\operatorname{Re}z_+(s)}{b}
=\frac{\sqrt{91}}{10}\sqrt{s-\frac1{15}}+O\!\left(s-\frac1{15}\right).
\]
This collision is the first possible one among unions of equal-height disjoint interval bands: for either one band or two bands, the order-one Cauchy transform has respectively zero or one simple upper-half-plane zero.

## Assumptions and scope

The set \(E\) consists of exactly three nondegenerate, mutually disjoint closed intervals of equal indicator height, symmetric about the origin, with \(0<c<a<b<\infty\). The open upper half-plane is the zero-counting domain, and multiplicity is holomorphic multiplicity. No assertion is made for unequal heights, unequal outer bands, other Cauchy-wavelet orders, or limits where two intervals merge or disappear. The zero location is scaled by \(b\); \(r\) and \(s\) are dimensionless.

## Proof

**1. Endpoint integration and algebra.** The elementary identity
\[
\int_u^v(z-t)^{-2}dt=(z-v)^{-1}-(z-u)^{-1}
\]
provides, with \(\zeta=z/b\), \(w=\zeta^2\),
\[
bF_{a,b,c}(b\zeta)=2\left[\frac{(1-r)(w+r)}{(w-r^2)(w-1)}+\frac{s}{w-s^2}\right]
=\frac{2N_{r,s}(w)}{(w-r^2)(w-1)(w-s^2)},
\]
where \(N_{r,s}(w)=Aw^2+Bw+C\) and
\[
\begin{aligned}
A&=1-r+s,\\
B&=(1-r)(r-s^2)-s(r^2+1),\\
C&=rs\bigl(r-(1-r)s\bigr).
\end{aligned}
\]
We have \(A>0\) and \(C>0\): indeed, \(r-(1-r)s>r^2>0\) because \(s<r\). The six real endpoint poles are genuine when \(0<s<r<1\), so no numerator zero cancels a pole.

**2. Discriminant and unique threshold.** Direct expansion and factorization give
\[
\begin{aligned}
\Delta&=B^2-4AC\\
&=-(1-r)(r-s)(1+s)Q_r(s),\\
Q_r(s)&=(1-r)s^2+(r^2+6r+1)s-r(1-r).
\end{aligned}
\]
The function \(Q_r\) has strictly positive derivative for all \(s\ge0\), with \(Q_r(0)=-r(1-r)<0\) and \(Q_r(r)=8r^2>0\). Its unique root in \((0,r)\) is exactly the stated \(s_*(r)\). Consequently, \(\Delta>0\) below the threshold, \(\Delta=0\) at it, and \(\Delta<0\) above it. Furthermore \(B>0\) throughout \(0<s\le s_*\). To see this, \(B(r,0)=r(1-r)>0\); if \(B\) first vanished in that range, then \(\Delta=-4AC<0\), contradicting \(\Delta\ge0\).

**3. All upper-half-plane zeros.** Below the threshold the two roots of \(N\) are
\[
w_{\pm}=\frac{-B\pm\sqrt\Delta}{2A}<0.
\]
Thus the two upper zeros are \(z=ib\sqrt{(B+\sqrt\Delta)/(2A)}\) and \(z=ib\sqrt{(B-\sqrt\Delta)/(2A)}\). They are distinct and simple. At the threshold, \(N=A(w+B/(2A))^2\) and its negative double root corresponds to \(z=ib\sqrt{B/(2A)}\), a holomorphic zero of multiplicity two. Above the threshold the two \(w\)-roots are a nonreal conjugate pair; their four square roots contain precisely two in the upper half-plane, \(z=b(\pm x+iy)\) with \(x,y>0\), and all are simple, where
\[
x^2=\frac12\left(\sqrt{\frac CA}-\frac{B}{2A}\right),\qquad
y^2=\frac12\left(\sqrt{\frac CA}+\frac{B}{2A}\right).
\]
No other zeros exist because the numerator is quadratic in \(w\), and none of its roots lies at \(w=0\) or a denominator pole.

**4. Square-root opening.** Write \(s_c=s_*(r)\), \(A_c=A(r,s_c)\), \(B_c=B(r,s_c)\), \(y_c=\sqrt{B_c/(2A_c)}\), and
\[
H_r=(1-r)(r-s_c)(1+s_c)Q'_r(s_c)>0.
\]
Then \(\Delta(s)=-H_r(s-s_c)+O((s-s_c)^2)\). Expanding \(\sqrt{w}\) around \(w=-y_c^2\) shows
\[
x(s)=\frac{\sqrt{H_r}}{4A_cy_c}\sqrt{s-s_c}+O(s-s_c)
\]
on the upper off-axis branch. At \(r=2/5\), \(s_c=1/15\), \(A_c=2/3\), \(B_c=4/25\), \(y_c=\sqrt3/5\), and the squared prefactor equals \(91/100\), proving the stated example.

**5. Minimality in component count.** One interval \([u,v]\) produces \((v-u)/((z-u)(z-v))\), without finite zeros. For two disjoint intervals \([u,v]\) and \([h,k]\), with \(u<v<h<k\), the transform numerator is the quadratic
\[
P(z)=(v-u)(z-h)(z-k)+(k-h)(z-u)(z-v).
\]
Its discriminant is exactly \(-4(k-u)(u-v)(v-h)(k-h)<0\), so it has one simple upper and one simple lower zero, never a collision. Three bands therefore form the minimal equal-height indicator class in which upper zeros can collide.

## Verification

The included standalone `three_band_cauchy_verification.py` checks the general rational identity and discriminant factorization using exact symbolic algebra; it also checks the two-interval discriminant, the exactly solvable collision \((r,s)=(2/5,1/15)\), and the critical splitting constant. With 45-decimal-digit quadrature it independently evaluates the original integral at sample roots on both sides of the transition. Execute:

```bash
python three_band_cauchy_verification.py
```

These calculations are reproducibility checks; the global zero count and parameter ranges are proved above analytically rather than inferred from finite samples.

## Relationship to prior work

Mallat and Waldspurger (arXiv:1404.1183, first posted April 4, 2014), Section 2.2, develop analytic Cauchy wavelets and holomorphic transforms, while Section 6 examines how zeros affect reconstruction. Holighaus, Koliander, Průša, and Abreu (arXiv:1906.00738), Sections III and V-A, analyze phase-gradient behavior near wavelet zeros. These foundational results motivate studying the geometry of individual wavelet zeros, but neither supplies the equal-height three-band polynomial, its sharp threshold, or minimal-collision statement. General zero-location constraints for positive Cauchy transforms and previously analyzed discrete atomic or two-band profiles concern different source families or higher derivative orders, and do not by themselves imply this discriminant phase diagram.

## Limitations

The conclusion concerns exact noiseless uniform indicator signals; it does not establish numerical stability of inverse phase retrieval, robustness to perturbations in band heights, or a zero classification for arbitrary multiband signals. The originality comparison is bounded by the materials inspected; an equivalent formula in unindexed sources remains possible. Scientific review is not independent.

## References

1. S. Mallat and I. Waldspurger, *Phase retrieval for the Cauchy wavelet transform*, arXiv:1404.1183 (first public version April 4, 2014), Sections 2.2 and 6. https://arxiv.org/abs/1404.1183
2. N. Holighaus, G. Koliander, Z. Průša and L. D. Abreu, *Characterization of Analytic Wavelet Transforms and a New Phaseless Reconstruction Algorithm*, arXiv:1906.00738 (2019), Sections III and V-A. https://arxiv.org/abs/1906.00738
