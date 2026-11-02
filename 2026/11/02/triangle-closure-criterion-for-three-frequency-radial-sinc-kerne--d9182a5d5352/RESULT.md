# Triangle closure criterion for three-frequency radial sinc kernels

## Finding

For every triple of positive real numbers \(a,b,c\), put
\[
F_{a,b,c}(r)=\operatorname{sinc}(ar)\operatorname{sinc}(br)\operatorname{sinc}(cr),\qquad
\operatorname{sinc}(u)=\begin{cases}\sin u/u,&u\ne0,\\1,&u=0.\end{cases}
\]
Write \(\Phi_d\) for the continuous normalized radial functions whose stationary kernels \(F(\|x-y\|)\) are positive semidefinite on every finite subset of \(\mathbb R^d\). Then
\[
\boxed{\ F_{a,b,c}\in\Phi_d\ \Longleftrightarrow\
\begin{cases}d\le5,&\max(a,b,c)\le(a+b+c)/2,\\
d\le3,&\max(a,b,c)>(a+b+c)/2.\end{cases}}
\]
Every admitted kernel is strictly positive definite for any finite set of pairwise distinct sites. In particular, degenerate length triangles (equality in the triangle inequality) also attain dimension five.

More explicitly, let \(L=|a-b|\), \(U=a+b\), and define
\[
h(r)=\left[\min(U,r+c)-\max(L,|r-c|)\right]_+,\qquad r\ge0,
\]
where \([z]_+=\max(z,0)\). The three-dimensional radial spectral probability is
\[
\nu_3(dr)=\frac{r h(r)}{4abc}\,dr.
\]
In the triangle regime, the five-dimensional radial spectral probability has the **nonnegative explicit density**
\[
\boxed{\ \nu_5(dr)=\frac{r\bigl(h(r)-r h'(r)\bigr)}{12abc}\,dr\ },
\]
with the derivative taken almost everywhere (the expression is piecewise continuous). Its support avoids an open neighborhood of the radial origin and has positive density on some nonempty open interval.

## Assumptions and scope

All lengths \(a,b,c\) are strictly positive, all dimensions \(d\) are positive integers, and the normalization of the Fourier characteristic function is \(\widehat\mu(x)=\int e^{i x\cdot\xi}\,\mu(d\xi)\). The measure \(\nu_d\) denotes the law of \(\|\xi\|\) when \(\mu\) is the unique rotation-invariant spectral probability on \(\mathbb R^d\). In the formula for \(\nu_5\), values of \(h'\) at finitely many breakpoints do not affect the measure. At \(r=0\) all expressions are interpreted by continuity or by their measure densities almost everywhere.

## Proof

**1. The three-dimensional Fourier law.** Let \(V_a,V_b,V_c\) be independent, uniformly distributed oriented vectors on the spheres of radii \(a,b,c\) in \(\mathbb R^3\). Each has characteristic function \(\operatorname{sinc}(a\|x\|)\), and their sum has characteristic function \(F_{a,b,c}(\|x\|)\). The length \(T=\|V_a+V_b\|\) has density
\[
\frac{t}{2ab}\mathbf1_{[L,U]}(t).
\]
Conditional on \(T=t\), the final length \(R=\|V_a+V_b+V_c\|\) has density \(r/(2tc)\) for \(|t-c|\le r\le t+c\). Multiplying and integrating out \(t\) yields
\[
\frac{r}{4abc}\operatorname{length}\bigl([L,U]\cap[|r-c|,r+c]\bigr)
=\frac{r h(r)}{4abc},
\]
which proves the claimed unique radial spectral law \(\nu_3\). Its density is positive on a nonempty open radial interval, so \(F_{a,b,c}\in\Phi_3\), strictly.

**2. A dimension-raising identity.** A uniform point on a sphere of radius \(s>0\) in \(\mathbb R^5\), projected onto the first three coordinates, has projected radius density \(3r^2/s^3\) on \(0<r<s\). Thus a radial five-dimensional probability \(\nu_5\) restricts to the three-dimensional radial law
\[
\nu_3(dr)=3r^2\left(\int_{(r,\infty)}s^{-3}\nu_5(ds)\right)dr.\tag{1}
\]
Similarly, in every codimension-one radial projection, a nonconstant rotationally invariant spectral probability projects to a radial law having positive mass in \((0,\varepsilon)\) for every \(\varepsilon>0\). Indeed, the projection of a nonzero-radius sphere has positive density in every sufficiently small ball about the origin; mixing such spheres preserves this property. The special possibility of a point mass at the origin cannot explain a nonconstant characteristic function.

**3. The triangle regime.** By permuting the lengths if necessary, the triangle condition is equivalent to \(L\le c\le U\). The auxiliary function
\[
q(r)=\min(U,r+c)-\max(L,|r-c|)
\]
is concave: the first term is the minimum of two affine functions and the second is the negative of the maximum of convex functions. We have \(q(0)=q(U+c)=0\); moreover \(q(r)>0\) for all \(0<r<U+c\) by concavity and its positive slope at the origin (one-sided slope \(2\) in the strict triangle case and \(1\) at equality). Hence \(h=q\) on \([0,U+c]\), vanishing outside. For \(0<r<s<U+c\), concavity with \(h(0)=0\) gives \(h(r)/r\ge h(s)/s\). Outside that interval \(h(s)/s=0\), so the ratio is nonincreasing everywhere it is defined. Consequently \(h-rh'\ge0\) almost everywhere.

Set \(R=U+c\) and define the nonnegative measure \(\nu_5\) by the stated density. Since \(h(R)=0\) and \(h\) is continuous and piecewise affine, integration by parts gives for every \(0<r<R\)
\[
\begin{aligned}
3r^2\int_r^R\frac{\nu_5(ds)}{s^3}
&=\frac{r^2}{4abc}\int_r^R\frac{h(s)-sh'(s)}{s^2}\,ds\\
&=\frac{r^2}{4abc}\left[-\frac{h(s)}s\right]_{r}^{R}
=\frac{rh(r)}{4abc}.
\end{aligned}
\]
The same identity holds for \(r\ge R\), both sides then vanishing. Equation (1) therefore identifies the three-dimensional projection of \(\nu_5\) with the already normalized \(\nu_3\). Tonelli's theorem applied to (1) shows \(\nu_5\) also has mass one. It defines a five-dimensional radial positive-definite extension of the same function by the uniqueness of characteristic functions restricted to \(\mathbb R^3\); hence \(F_{a,b,c}\in\Phi_5\).

The piecewise-affine function \(h\) is exactly proportional to \(r\) for every sufficiently small positive \(r\). Thus \(h-rh'=0\) in some interval \((0,\varepsilon)\), while the support of \(\nu_5\) contains a nonempty interval on which its density is positive. This also proves strict positive definiteness in dimension five.

**4. Optimality.** When the triangle condition fails, writing \(\delta=2\max(a,b,c)-(a+b+c)>0\), the three-dimensional spectral law \(\nu_3\) is supported on \([\delta,a+b+c]\) and therefore has no mass in \((0,\delta)\). The codimension-one projection property from Step 2 rules out a nonconstant radial positive-definite extension to dimension four. Thus dimension three is optimal.

When the triangle condition holds, the five-dimensional measure \(\nu_5\) is nonzero and has no mass in a neighborhood of zero. The same projection property rules out dimension six, making dimension five optimal. The nesting \(\Phi_{d+1}\subset\Phi_d\) rules out all higher dimensions in each case.

Finally, if a spectral measure on \(\mathbb R^d\) has positive Lebesgue density on some open set, its Fourier kernel is strictly positive definite on distinct sites: equality of a finite Gram quadratic form forces a finite exponential polynomial to vanish on that open set, hence everywhere, and the independence of exponentials at distinct frequencies forces every coefficient to vanish. The measures above have this property in dimensions three and five respectively; restriction to lower dimensions preserves strictness. This completes the proof.

## Verification

Run `python3 triple_sinc_checker.py` with Python 3, using only its standard library. The checker constructs exact rational piecewise-affine branches of \(h\) for 14 sample triples (strict, equality, and failing triangle), tests density signs and the spectral gap, and verifies exact normalization and the first seven even moments of both three- and five-dimensional Fourier radius laws against the Taylor coefficients of the triple-sinc product. These are reproducible finite tests of the critical formulas, **not** proof of the theorem for all positive real triples. The general result is supplied by concavity and the radial-projection identities above.

## Relationship to prior work

Golinskii, Malamud, and Oridoroga (arXiv:1502.07179, initially public February 25, 2015) prove general radial Schoenberg-dimension transition formulas in their Theorem 3.1 and classify products of **two** Schoenberg kernels with unequal radii in Theorem 4.1, as well as squares in Theorem 4.3. Their results explain the general dimension-raising mechanism, but those inspected statements do not supply the arbitrary **three-radius** sharp triangle classification or its explicit annular five-dimensional spectral law. In particular, the old unequal two-factor obstruction does not imply the three-factor answer: the third factor can restore dimension-five positivity when its length closes a triangle.

The classical positive spherical product-formula viewpoint also occurs in Rösler (arXiv:math/0210137, initial posting October 9, 2002), whose focus is Dunkl kernels and general positivity of radial product formulas rather than this Euclidean three-radius dimension frontier. For equal lengths, the dimension-five property of the third sinc power is compatible with known one-parameter power calculations and is not claimed to be new by itself. The contribution here is the sharp classification **uniform in every positive length triple**, including fully unequal triples and degenerate triangles.

## Limitations

This theorem concerns exactly three positive frequencies and the Euclidean radial notion of positive definiteness; it neither classifies arbitrary products of four or more different sinc factors nor supplies quantitative lower Gram eigenvalue bounds. General radial extension criteria and special equal-scale cases are earlier mathematics. While the specific triangle classification was not found in the bounded comparisons, an equivalent specialization in older Bessel-product or radial random-flight literature remains possible. No independent mathematical validation is asserted.

## References

1. L. Golinskii, M. Malamud, L. Oridoroga, *Radial positive definite functions and Schoenberg matrices with negative eigenvalues*, arXiv:1502.07179, first submitted 2015-02-25. https://arxiv.org/abs/1502.07179
2. L. Golinskii, M. Malamud, L. Oridoroga, *Schoenberg matrices of radial positive definite functions and Riesz sequences in \(L^2(\mathbb R^n)\)*, arXiv:1403.2234, first submitted 2014-03-10. https://arxiv.org/abs/1403.2234
3. M. Rösler, *A positive radial product formula for the Dunkl kernel*, arXiv:math/0210137, first submitted 2002-10-09. https://arxiv.org/abs/math/0210137
