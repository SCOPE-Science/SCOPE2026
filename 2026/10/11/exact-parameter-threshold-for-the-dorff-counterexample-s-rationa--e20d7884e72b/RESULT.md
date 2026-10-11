# Exact parameter threshold for the Dorff counterexample’s rational witness

## Finding

Fix
\[
a=-\frac{10}{11}.
\]
For each
\[
0\le b<\frac1{43},
\]
set
\[
\Gamma_b(z)=z\frac{B_a(z)}{B_b(z)},
\qquad
B_r(z)=\frac{z-r}{1-rz},
\qquad |z|=1.
\]
Let \(U_b\) be the Poisson extension of \(\Gamma_b\), and perform the same real-affine normalization as in the recent Wang--Zhong construction. This gives a normalized convex harmonic mapping
\[
f_b\in\mathcal K_H^0
\]
whose image is an ellipse. Let
\[
F_b=f_b\widetilde *f_b
\]
be its harmonic self-convolution, and fix the rational witness
\[
x_0=-\frac{99}{100}.
\]

There is a unique
\[
\beta_*=0.0221846017351797023657\ldots
\]
in
\[
\left(0,\frac1{43}\right)
\]
such that
\[
J_{F_b}(x_0)
\begin{cases}
>0,&0\le b<\beta_*,\\
=0,&b=\beta_*,\\
<0,&\beta_*<b<1/43.
\end{cases}
\]

The source choice
\[
b=\frac1{44}
\]
lies strictly in the negative-Jacobian regime. More strongly, every
\[
b\in\left[\beta_*,\frac1{43}\right)
\]
produces a normalized convex harmonic ellipse mapping whose self-convolution is not locally univalent.

The threshold \(\beta_*\) is the unique zero in \((0,1/43)\) of
\[
\begin{aligned}
H(b)={}&111370457788920000b^{18}+200452967192016000b^{17}
+26384856553020119b^{16}\\
&-231322373255930660b^{15}-1432813729830625538b^{14}
-1953607940142274680b^{13}\\
&+1786614907376070838b^{12}+3981191613894394680b^{11}
-20746361469003038b^{10}\\
&-2248981109067364100b^9-338035249181596081b^8
+429279211367288760b^7\\
&-106176808553072400b^6-207727750712076000b^5
-32519528199900000b^4\\
&+17388937112400000b^3-6420414924000000b^2
+1010930760000000b-19448100000000.
\end{aligned}
\]
An exact rational bracket is
\[
0.02218460173517970<\beta_*<0.02218460173517971.
\]

## Assumptions and scope

The harmonic convolution, the class \(\mathcal K_H^0\), and the real-affine normalization are those used in arXiv:2609.11556v1. Only the second real Blaschke parameter is varied; the first parameter remains
\[
a=-10/11.
\]

The statement classifies the sign at the specific witness
\[
x_0=-99/100.
\]
It does not assert that \(\beta_*\) is the global first parameter at which the self-convolution loses local univalence somewhere in the disk.

The positive parameter interval
\[
0\le b<1/43
\]
is not an arbitrary truncation. It is exactly the interval on which the same degree-one circle map remains orientation-preserving before the angular derivative first degenerates at \(z=1\).

## Proof

For real \(b\), the angular derivative of the boundary map is
\[
1+\frac{1-a^2}{1-2ax+a^2}-\frac{1-b^2}{1-2bx+b^2},
\qquad x=\cos t.
\]
With \(a=-10/11\), after clearing denominators its numerator is
\[
N_b(x)=-440b^2x-463b^2+440bx^2+484bx-21.
\]
The remaining denominator has negative sign on \([-1,1]\) for \(0\le b<1\). For each \(b\ge0\), \(N_b\) is convex in \(x\), hence its maximum on \([-1,1]\) occurs at an endpoint. Those endpoint values are
\[
N_b(-1)=-(b+1)(23b+21)<0
\]
and
\[
N_b(1)=-21(b-1)(43b-1).
\]
Thus the angular derivative is strictly positive exactly for
\[
0\le b<1/43
\]
along this positive parameter ray; at \(b=1/43\) it vanishes at \(x=1\). Since the boundary map has degree one, it is a circle diffeomorphism throughout the open range, so the Radó--Kneser--Choquet theorem gives a harmonic disk diffeomorphism \(U_b\).

A partial-fraction expansion valid for variable \(b\) gives
\[
c_1(b)=\frac{-121b^2-110b+21}{11(10b+11)},
\]
\[
c_2(b)=-\frac{21(11b+10)}{121(10b+11)},
\]
and
\[
c_{-1}(b)=\frac{b(1-b^2)(11b+10)}{10b+11}.
\]
Moreover, for every \(n\ge2\),
\[
c_n=c_2a^{n-2},
\qquad
c_{-n}=c_{-1}b^{n-1}.
\]
The affine normalization determinant
\[
\Delta(b)=c_1(b)^2-c_{-1}(b)^2
\]
factors as
\[
\Delta(b)=
-\frac{E_1(b)E_2(b)}{121(10b+11)^2},
\]
where
\[
E_1(b)=121b^4+110b^3-21
\]
and
\[
E_2(b)=121b^4+110b^3-242b^2-220b+21.
\]
Exact sign certification gives
\[
E_1<0<E_2
\]
on \([0,1/43]\), hence \(\Delta>0\). The normalized maps \(f_b\) are therefore well-defined orientation-preserving affine images of \(U_b\), and their images are ellipses.

The normalized analytic and co-analytic coefficients retain the source's two-geometric-tail form. Summing their squared tails using
\[
S_r(z)=\frac{z(2-rz)}{(1-rz)^2}
\]
produces rational formulas for the two derivatives of \(F_b\). At \(x_0=-99/100\), exact elimination yields
\[
J_{F_b}(x_0)=
\frac{-14641K(b)H(b)}{1600000000(9b-10)^2(99b^2+100)^4E_1(b)^3E_2(b)^3},
\]
with
\[
\begin{aligned}
K(b)={}&963160000b^8+1751200000b^7-174164414761b^6
-333078645020b^5\\
&-123932051900b^4+34669404000b^3+17157210000b^2
+17509800000b-441000000.
\end{aligned}
\]
and \(H\) as displayed in the Finding.

On \([0,1/43]\), exact Bernstein-form certificates give
\[
K(b)<0,
\qquad
H'(b)>0,
\qquad
E_1(b)<0<E_2(b).
\]
The other denominator factors are strictly positive after their displayed even powers. Since
\[
H(0)=-19448100000000<0
\]
and
\[
H(1/43)>0,
\]
there is exactly one root \(\beta_*\in(0,1/43)\). The denominator of the Jacobian is negative on this interval, so
\[
\operatorname{sgn}J_{F_b}(x_0)=\operatorname{sgn}(K(b)H(b)).
\]
Because \(K<0\), the announced sign trichotomy follows.

At \(b=\beta_*\), Lewy's theorem already rules out local univalence because the Jacobian vanishes at \(x_0\). For \(b>\beta_*\), one has
\[
J_{F_b}(x_0)<0,
\qquad
J_{F_b}(0)=1,
\]
so continuity gives an interior zero of the Jacobian. Thus every \(b\in[\beta_*,1/43)\) is a counterexample parameter.

## Verification

The source's full primary preprint was inspected at the circle-homeomorphism argument, Fourier coefficients, affine normalization, two-geometric-tail formulas, rational self-convolution derivatives, and the Jacobian computation at \(-99/100\). The primary source fixes \(b=1/44\); its remark notes qualitative openness of the angular-derivative condition but does not give the exact one-parameter Jacobian threshold above.

The accompanying checker uses only exact rational arithmetic. It converts the relevant univariate polynomials to Bernstein form on \([0,1/43]\). The convex-hull property of the Bernstein basis certifies \(K<0\), \(H'>0\), \(E_1<0<E_2\) on the whole continuum interval, not merely at sampled points. It also verifies opposite signs of \(H\) at the two rational decimal endpoints enclosing \(\beta_*\).

The earlier fixed-parameter refinement locating the unique real-axis fold of the \(b=1/44\) example was also compared. That result varies the spatial point with \(b\) fixed; the present result varies \(b\) and gives the exact sign threshold at the source's fixed rational witness. Neither implication contains the other.

## Relationship to prior work

Wang and Zhong construct the single parameter pair
\[
a=-10/11,
\qquad
b=1/44,
\]
prove that its normalized harmonic disk map has elliptical image, and certify a negative Jacobian of the self-convolution at \(x_0=-99/100\). They also observe that strict positivity of the boundary angular derivative is an open condition in the two real parameters. The present result turns that qualitative robustness observation into an exact one-parameter phase boundary for the same rational witness.

A prior refinement of the same source proves that, at the fixed source value \(b=1/44\), the Jacobian has exactly one zero on the real diameter. That spatial classification does not determine how the source's witness behaves as the Blaschke parameter varies.

Muir's 2024 work develops finite-Blaschke-product methods for convolutions involving half-plane and strip mappings. Those families and their local-univalence criteria are structurally different from the bounded ellipse self-convolution here and do not imply the displayed degree-eighteen threshold.

## Limitations

The number \(\beta_*\) is the exact threshold for the fixed witness \(x_0=-99/100\), not a proved global onset threshold for loss of local univalence somewhere in the disk.

Only the one-parameter ray with \(a=-10/11\) and \(b\ge0\) is classified. A full two-parameter stability region would require a genuinely two-dimensional sign analysis.

The interval stops at \(b=1/43\) because the boundary map ceases to have strictly positive angular derivative there. No statement is made about alternative constructions beyond that geometric boundary.

## References

1. Z.-G. Wang and D. Zhong, *A counterexample to an open problem of Dorff*, arXiv:2609.11556v1, 2026.
2. M. Dorff, *Convolutions of planar harmonic convex mappings*, Complex Variables Theory and Application 45 (2001), 263--271.
3. S. Muir, *Blaschke Products and Convolutions with a Slanted Generalized Half-Plane Harmonic Mapping*, Complex Analysis and Operator Theory 18 (2024), article 74, DOI: 10.1007/s11785-024-01508-2.
