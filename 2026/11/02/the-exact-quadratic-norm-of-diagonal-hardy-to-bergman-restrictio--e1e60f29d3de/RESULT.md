# The exact quadratic norm of diagonal Hardy-to-Bergman restriction

## Finding

Let \(D F(z)=F(z,z)\) be the diagonal restriction from the bidisc to the unit disc. With normalized boundary and area measures, restrict \(D\) to the complex vector space \(\mathcal H_2\) of homogeneous quadratic polynomials
\[
F(z_1,z_2)=a z_1^2+b z_1z_2+c z_2^2,\qquad a,b,c\in\mathbb C.
\]
The exact restricted norm from \(H^1(\mathbb D^2)\) to \(A^1(\mathbb D)\) is
\[
\boxed{\|D|_{\mathcal H_2}\|=\frac{\pi}{4\tau}=1.062662646\ldots},
\qquad \tau=\cos\tau,\quad 0<\tau<\frac\pi2.
\]
One extremizer is
\[
F_*(z_1,z_2)=\frac{z_1^2+2\sin\tau\,z_1z_2+z_2^2}{2(1+\sin\tau)}.
\]
This strictly exceeds the ratio \(\pi/3\) furnished by a homogeneous linear test. No assertion about the unrestricted \(H^1\)-to-\(A^1\) norm is made.

## Assumptions and scope

The Hardy norm of a polynomial is its integral of absolute value against normalized Haar measure on \(\mathbb T^2\): \(\|F\|_{H^1}=\int_{\mathbb T^2}|F|\,dm_2\). The Bergman norm is \(\|g\|_{A^1}=\pi^{-1}\int_{|z|<1}|g(z)|\,dA(z)\). The claim covers all complex coefficient triples, including zero coefficients. The operator norm is the supremum over nonzero members of \(\mathcal H_2\).

## Proof

**Reduction.** Write \(P(w)=a+bw+cw^2\). Factoring out the first unimodular coordinate on \(\mathbb T^2\) shows
\[
\|F\|_{H^1}=\int_{\mathbb T}|P(w)|\,dm(w),\qquad
\|DF\|_{A^1}=\tfrac12|P(1)|.
\]
If \(P(1)=0\), its ratio is zero. Otherwise multiply by a scalar so that \(P(1)=1\). We must minimize the boundary \(L^1\) norm under this normalization.

**Symmetrization.** Complex coefficient conjugation \(P(z)\mapsto\overline{P(\bar z)}\) and polynomial reversal \(P(z)\mapsto z^2P(1/z)\) both preserve \(P(1)=1\) and preserve its \(L^1(\mathbb T)\) norm (after the first conjugation the coefficients are real). Convexity of the \(L^1\) norm permits successive averaging. Hence a global minimizer can be taken of the form
\[
P_u(z)=u+(1-2u)z+u z^2,\qquad u\in\mathbb R.
\]
On the circle its modulus is \(|1-2u+2u\cos\theta|=|1-4u\sin^2(\theta/2)|\). Therefore
\[
G(u)=\|P_u\|_1=\frac1{2\pi}\int_0^{2\pi}|1-4u\sin^2(\theta/2)|\,d\theta
\]
is convex on the entire real line. It decreases strictly for \(u\le1/4\); since it grows as \(u\to+\infty\), the global minimum lies above \(1/4\). To locate it, parameterize \(u=1/[2(1+v)]\), for \(0<v<1\) (thus \(1/4<u<1/2\)). Direct integration across the two zeros of \(\cos\theta+v\) yields
\[
G\left(\frac1{2(1+v)}\right)
=\frac{2}{\pi}\frac{\sqrt{1-v^2}+v\arcsin v}{1+v}.
\]
Its derivative with respect to \(v\) has the sign of
\[
\arcsin v-\sqrt{1-v^2}.
\]
This is strictly increasing from \(-1\) to \(\pi/2\), so it vanishes exactly at \(v_*=\sin\tau\), where \(\tau\in(0,\pi/2)\) uniquely solves \(\tau=\cos\tau\). This is a stationary point of the globally convex \(G(u)\), hence a global minimizer even among \(u\) outside the displayed parameter interval. At this point, \(\sqrt{1-v_*^2}=\arcsin v_*=\tau\), so
\[
\min_{P(1)=1}\|P\|_1=G\left(\frac1{2(1+\sin\tau)}\right)=\frac{2\tau}{\pi}.
\]
Combining this with \(\|DF\|_{A^1}=1/2\) proves the exact norm and the stated extremizer.

**Strict improvement over the linear test.** The scalar equation gives \(\tau<3/4\), since \(\cos(3/4)<3/4\) and \(t-\cos t\) strictly increases. Thus \(\pi/(4\tau)>\pi/3\). For the linear test \(F=z_1+z_2\), direct integration gives \(\|DF\|_{A^1}/\|F\|_{H^1}=\pi/3\).

## Verification

Reproduction requires only the scalar root equation and elementary circular integrals. The accompanying standard-library program checks the root, the exact analytic norm formula against midpoint boundary quadrature, the improvement over \(\pi/3\), and sample coefficient inequalities. Its finite tests do not establish the theorem: convex symmetrization and the exact one-variable minimum above do.

## Relationship to prior work

Brevig, Gómez-Serrano, Ortega-Cerdà and Seip proved contractivity of the unrestricted diagonal restriction for \(p\ge2\) and provided the noncontractive linear test for \(0<p<2\); their October 2026 text does not calculate this sharp degree-two restricted norm. General Nikolskii inequalities give order estimates for trigonometric-polynomial evaluation, but order bounds do not imply the transcendental exact finite-degree constant here. Arestov's 1980 paper addresses a best constant relative to the geometric-mean norm (the endpoint denoted \(L^0\)), not this \(L^1\) evaluation norm. The 2020 Lorentz–Zygmund inequalities of Doktorski likewise do not identify this finite-section constant. This claim is equivalent to the sharp \(L^\infty/L^1\) ratio for complex trigonometric polynomials of degree at most one; equivalent classical coverage in less indexed literature remains a genuine originality risk.

## Limitations

This is an exact finite-dimensional restriction result, not a determination of the full operator norm on \(H^1(\mathbb D^2)\), nor a statement for other exponents or higher-degree sections. Numerical quadrature and finite random tests do not prove any universal inequality. A specialized older exact trigonometric-polynomial inequality might subsume this claim despite the comparison searches described in the scientific review.

## References

- O. F. Brevig, J. Gómez-Serrano, J. Ortega-Cerdà and K. Seip, *Contractivity of Rudin's diagonal restriction operator for \(H^p\) of the polydisc*, arXiv:2610.16227v1, first posted 2026-10-12. https://arxiv.org/html/2610.16227v1
- V. V. Arestov, *Inequality of different metrics for trigonometric polynomials*, Mathematical Notes 27 (1980), 265–269. https://www.mathnet.ru/eng/mzm6503
- L. R. Ya. Doktorski, *Nikol'skii-Type Inequalities for Trigonometric Polynomials for Lorentz–Zygmund Spaces*, Journal of Function Spaces (2020), 6853723. https://doi.org/10.1155/2020/6853723
