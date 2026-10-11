# Fourth-chord moment amplification and angular phase transition for parallelograms

## Finding

Let \(P\subset\mathbb R^2\) be any nondegenerate parallelogram. Let \(I,I'\) be independent area-uniform random points of \(P\), and \(S,S'\) independent arclength-uniform random points of \(\partial P\). Define the fourth-chord amplification
\[
\mathcal R_4(P)=\frac{\mathbb E\|S-S'\|_2^4}{\mathbb E\|I-I'\|_2^4}.
\]
Then the complete sharp range is
\[
\boxed{1<\mathcal R_4(P)\le \frac{61}{17}.}
\]
Equality on the right occurs **if and only if \(P\) is a square**. The lower value \(1\) is an unattained infimum, approached by rectangles whose side-length ratio tends to infinity.

There is also an exact angular phase transition. Write \(P=x_0+[-a,a]+[-b,b]\), where the nonparallel nonzero vectors \(a,b\) are the half-side generators, and put
\[
A=\|a\|_2,\qquad B=\|b\|_2,\qquad r=\frac{\max\{A,B\}}{\min\{A,B\}},\qquad c=\frac{|\langle a,b\rangle|}{AB}.
\]
Thus \(r\ge1\) and \(0\le c<1\). Let \(v_*>2\) be the unique zero on \((2,\infty)\) of
\[
4v^3+4v^2-21v-8=0,
\]
and put \(r_*=(v_*+\sqrt{v_*^2-4})/2\), numerically \(r_*\approx1.2363261915\). At fixed \(r\), the exact function \(\mathcal R_4\) is strictly decreasing in \(c^2\) when \(1\le r<r_*\), independent of \(c\) when \(r=r_*\), and strictly increasing in \(c^2\) when \(r>r_*\). In particular, an entire one-parameter family of distinct parallelogram angles has exactly the same fourth-chord amplification at the critical aspect ratio.

## Assumptions and scope

The area and arclength distributions are normalized probability measures; every pair is independent and sampled *with replacement*. This is the Euclidean norm, with no random-line or invariant-line chord convention. Parallel sides have lengths \(2A\) and \(2B\); nondegeneracy means \(|\langle a,b\rangle|<AB\). All statements are translation- and scale-invariant. The limiting collinear shape is not included as a parallelogram.

## Proof

Translation allows \(x_0=0\). Set \(z=\langle a,b\rangle\). For a centered random vector \(X\), with independent copy \(X'\) and covariance matrix \(\Sigma_X\), expansion of the fourth power and independence give
\[
\mathbb E\|X-X'\|_2^4=2\mathbb E\|X\|_2^4+2(\mathbb E\|X\|_2^2)^2+4\operatorname{tr}(\Sigma_X^2). \tag{1}
\]
For area-uniform sampling, \(I=Ua+Vb\), where \(U,V\) are independent uniform variables on \([-1,1]\). Using \(\mathbb EU^2=1/3\) and \(\mathbb EU^4=1/5\) in (1) yields
\[
M_I:=\mathbb E\|I-I'\|_2^4=\frac8{45}\bigl(6A^4+5A^2B^2+6B^4+10z^2\bigr). \tag{2}
\]

For boundary sampling, sides parallel to \(a\) have total probability \(A/(A+B)\). Conditional on such a side, the point is distributed as \(\sigma b+Ua\), with independent symmetric sign \(\sigma\); on the complementary sides, it is \(\sigma a+Ub\). Define
\[
p=\frac A{A+B},\quad q=\frac B{A+B},\quad
\alpha=\frac{A/3+B}{A+B},\quad \beta=\frac{A+B/3}{A+B}.
\]
Direct integration gives the exact boundary moments
\[
\begin{aligned}
m_2&:=\mathbb E\|S\|_2^2=\frac{(A+B)^2}{3},\\
m_4&:=\mathbb E\|S\|_2^4\\
&=p\left(B^4+\frac{2A^2B^2+4z^2}{3}+\frac{A^4}{5}\right)
 +q\left(A^4+\frac{2A^2B^2+4z^2}{3}+\frac{B^4}{5}\right),\\
\Sigma_S&=\alpha aa^{\mathsf T}+\beta bb^{\mathsf T}.
\end{aligned} \tag{3}
\]
Consequently
\[
M_S:=\mathbb E\|S-S'\|_2^4
=2m_4+2m_2^2+4\bigl(\alpha^2A^4+\beta^2B^4+2\alpha\beta z^2\bigr). \tag{4}
\]
Equations (2)--(4) are an explicit rational formula for \(\mathcal R_4=M_S/M_I\), valid for all admissible generators. By comparison, the quadratic chord-moment ratio is exactly \((A+B)^2/(A^2+B^2)\), so all rhombi attain its maximum \(2\) regardless of angle. The fourth-power law breaks this degeneracy. Subtraction factors as
\[
M_S-M_I=\frac{8}{45(A+B)^2}\left[
24A^5B+49A^4B^2+30A^3B^3+49A^2B^4+24AB^5
+(20A^2+60AB+20B^2)z^2\right]>0, \tag{5}
\]
which proves the strict lower bound. As \(A/B\to\infty\) with \(z=0\), equations (2)--(4) imply \(\mathcal R_4\to1\), giving its sharpness.

For the upper bound let \(\Delta=(61/17)M_I-M_S\). Interchange \(a,b\) if needed and write \(A=B(1+t)\) with \(t\ge0\), and \(z^2=A^2B^2c^2\), \(0\le c^2<1\). Since \(\Delta\) is affine in \(z^2\),
\[
\Delta=(1-c^2)\Delta_0+c^2\Delta_1,
\]
where exact substitution at \(z=0\) and at the algebraic endpoint \(z^2=A^2B^2\) gives
\[
\begin{aligned}
\Delta_0&=\frac{8B^4t^2}{765(t+2)^2}
 (264t^4+1704t^3+4211t^2+5014t+2507),\\
\Delta_1&=\frac{8B^4}{255}
 (88t^4+216t^3+221t^2+10t+5).
\end{aligned} \tag{6}
\]
Every displayed coefficient is positive. Thus \(\Delta\ge0\), and equality requires \(t=0\) and \(c=0\); these conditions say \(A=B\) and \(a\perp b\), precisely a square. The endpoint \(c^2=1\) is used only in the affine polynomial identity, not as an admissible geometric shape.

To prove the angular classification, differentiation of the exact rational formula gives
\[
\frac{\partial\mathcal R_4}{\partial(z^2)}=
\frac{128G(A,B)}{135(A+B)^2M_I^2},
\]
where
\[
G(A,B)=4A^6+4A^5B-9A^4B^2-9A^2B^4+4AB^5+4B^6.
\]
With \(r=A/B\ge1\) and \(v=r+r^{-1}\ge2\), this factors as
\[
G(A,B)=B^6r^3(4v^3+4v^2-21v-8). \tag{7}
\]
The cubic is \(-2\) at \(v=2\), and its derivative \(12v^2+8v-21\) is strictly positive for \(v\ge2\); hence it has a unique zero \(v_*>2\). The sign of (7) gives exactly the three angular regimes. This proves the whole stated theorem.

## Verification

The standalone file `verify.py` regenerates (2)--(6) and the angular derivative using exact symbolic arithmetic, checks the positivity certificates' coefficients, checks the square value, and verifies the elongated limit. Run `python verify.py` after installing the sole declared dependency in `requirements.txt`. Its successful output is `PARALLELOGRAM_FOURTH_CHORD_EXACT_OK`. The companion `independent_check.py` integrates the actual two-point sampling laws independently at one nonorthogonal rational parallelogram and checks both exact fourth moments. The proof of uniqueness of the cubic root and polynomial positivity is elementary and appears above; finite parameter checks are not used to infer any universal statement.

## Relationship to prior work

Tokmachev's 2026 convex-order theorem compares the arclength-uniform and area-uniform distributions when their centroids agree, yielding \(\mathbb E\|I-I'\|_2^p\le\mathbb E\|S-S'\|_2^p\) for all \(p\ge1\) in the planar case [1]. Parallelograms satisfy the centroid condition. That inequality supplies a lower comparison, but does not imply the exact **upper** ratio \(61/17\), its square equality case, or the angular phase transition for \(p=4\). The related 2026 arbitrary-planar-body theorem treats mean distance (power one), not the fourth-power upper comparison [2]. Earlier studies of random chord distributions for triangles and quadrilaterals use additional chord-selection conventions [3]; equivalence must not be presumed. A published exact squared-distance comparison for triangles is likewise a different exponent and body family [4].

## Limitations

The theorem is confined to Euclidean parallelograms, independent area- or arclength-uniform endpoint sampling, and fourth powers. It gives no optimal bound for all convex bodies and does not assert higher-power analogues. The close 2026 convex-order source was available only at abstract level in this comparison; possible unindexed examples or appendices leave residual priority risk. No independent audit of this finding has been carried out.

## References

[1] A. S. Tokmachev, *Inequalities for convex functions of random points inside and on the boundary of convex bodies*, arXiv:2607.08869v1, first posted 2026-07-09, https://arxiv.org/abs/2607.08869.

[2] M. Kukushkin, *The Zaporozhets--Tarasov Inequality for an Arbitrary Planar Convex Body*, arXiv:2608.14833, first posted 2026-08-14, https://arxiv.org/abs/2608.14833.

[3] J. Gates, *Recognition of triangles and quadrilaterals by chord length distribution*, Journal of Applied Probability 19 (1982), 873--879, https://doi.org/10.2307/3213843.

[4] *Exact second-moment boundary gap for arbitrary Euclidean triangles*, public mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-second-moment-boundary-gap-for-arbitrary-euclidean-triangl--d886b40f95a8.
