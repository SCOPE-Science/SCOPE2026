# Exact scalar \(L_2\) metric-cotype lifting constant on even discrete tori
## Finding
For every integer \(n\ge 1\) and every even integer \(m\ge 2\), put
\[
G_{m,n}=(\mathbb Z/(2m\mathbb Z))^n,
\]
and define
\[
D_{\mathrm{long}}F(x,j)=F(x+me_j)-F(x),\qquad
D_{\mathrm{sgn}}F(x,\varepsilon)=F(x+\varepsilon)-F(x),
\]
where \(j\in\{1,\ldots,n\}\) and \(\varepsilon\in\{-1,1\}^n\). With normalized counting measure on all finite sets, the exact real-scalar quadratic difference constant is
\[
C_{2,\mathbb R}(n,m)=\sqrt{\frac{2}{1-\cos(\pi/m)^n}}.
\]
By quotient duality, the same formula is the optimal adjoint lifting constant:
\[
\Lambda_{2,\mathbb R}(n,m)=C_{2,\mathbb R}(n,m).
\]
Equivalently, the least constant \(L_{n,m}\) for which every scalar datum \(g\) admits \(h\) satisfying
\[
D_{\mathrm{sgn}}^*h=\frac{\sqrt n}{m}D_{\mathrm{long}}^*g,
\qquad \|h\|_2\le L_{n,m}\|g\|_2,
\]
is
\[
L_{n,m}=\sqrt{\frac{2n}{m^2\bigl(1-\cos(\pi/m)^n\bigr)}}.
\]
If \(n\to\infty\) and even integers \(m=m_n\) obey \(m_n/\sqrt n\to\alpha\in(0,\infty)\), then
\[
L_{n,m_n}\longrightarrow
\frac{\sqrt2}{\alpha\sqrt{1-\exp(-\pi^2/(2\alpha^2))}}.
\]
At the same normalization, the optimal regular norm of a single scalar linear lifting is \(\sqrt n\). Hence the datum-dependent scalar lifting problem has an explicit bounded sharp-scale profile while every regular linear realization has an unbounded \(\sqrt n\) cost.

## Assumptions and scope
The statement concerns real scalar-valued functions, the exponent \(p=2\), integers \(n\ge1\), and even integers \(m\ge2\). The group, increment operators, normalized counting measures, and normalization \(\sqrt n/m\) are exactly those used in Wang's finite-torus divergence-lifting framework. No assertion is made here for odd \(m\), Banach-valued targets, or exponents other than \(2\).

## Proof
Complexify first and write the characters of \(G_{m,n}\) as
\[
\chi_k(x)=\exp\!\left(\frac{\pi i}{m}\,k\cdot x\right),
\qquad k\in(\mathbb Z/(2m\mathbb Z))^n.
\]
Let \(r(k)\) be the number of coordinates \(k_j\) that are odd. For one character, normalized Parseval computation gives
\[
\|D_{\mathrm{long}}\chi_k\|_2^2
 =\frac1n\sum_{j=1}^n|\exp(\pi i k_j)-1|^2
 =\frac{4r(k)}n,
\]
whereas averaging over independent signs gives
\[
\|D_{\mathrm{sgn}}\chi_k\|_2^2
 =2\left(1-\prod_{j=1}^n\cos\!\left(\frac{\pi k_j}{m}\right)\right).
\]
The two quadratic forms are simultaneously diagonal in the Fourier basis, so the squared optimal ratio is the maximum, over frequencies with nonzero sign energy, of
\[
\frac{2r(k)}{n\left(1-\prod_{j=1}^n\cos(\pi k_j/m)\right)}.
\]
Set \(c=\cos(\pi/m)\). If \(m=2\), then \(c=0\), every odd-coordinate cosine vanishes, and the displayed ratio is at most \(2\), with equality when all \(n\) coordinates are odd. Assume now \(m>2\), so \(0<c<1\). For every odd residue \(a\) modulo \(2m\),
\[
\left|\cos\!\left(\frac{\pi a}{m}\right)\right|\le c.
\]
If the cosine product is nonpositive, the ratio is at most \(2r(k)/n\le2\), which cannot exceed the value obtained below. If the product is positive, then it is at most \(c^{r(k)}\), and therefore the ratio is at most
\[
\frac{2r(k)}{n(1-c^{r(k)})}.
\]
For \(0<c<1\), the function \(x\mapsto x/(1-c^x)\) is increasing on \((0,\infty)\): writing \(c=\exp(-t)\) with \(t>0\), its derivative is positive because \(\exp(tx)>1+tx\). Thus the last expression is at most
\[
\frac{2}{1-c^n}.
\]
Equality is attained at the frequency \(k=(1,\ldots,1)\). The real two-dimensional span of \(\operatorname{Re}\chi_k\) and \(\operatorname{Im}\chi_k\) has the same quotient of the two quadratic forms, so the complex optimum is already attained by a real scalar function. This proves
\[
C_{2,\mathbb R}(n,m)^2=\frac{2}{1-c^n}.
\]
Wang's quotient-duality theorem identifies the adjoint lifting constant with the difference constant, proving the second equality. Multiplying the long-difference operator by \(\sqrt n/m\) gives the formula for \(L_{n,m}\).

Finally,
\[
\log\cos(\pi/m)=-\frac{\pi^2}{2m^2}+O(m^{-4}),
\]
so if \(m/\sqrt n\to\alpha\), then
\[
\cos(\pi/m)^n\to\exp\!\left(-\frac{\pi^2}{2\alpha^2}\right),
\]
which yields the stated limit. Wang's exact regular-factorization theorem gives regular norm \(\sqrt n\) for the normalized scalar adjoint equation when \(p=q=2\).

## Verification
The Fourier multipliers were derived directly from the definitions and checked symbolically. A finite enumeration for small \(n\) and even \(m\) was used only as a sanity check and was not used in the proof. Boundary cases \(n=1\) and \(m=2\) were checked separately in the argument. The real-scalar attainment follows from the invariant real span of an extremizing character and its conjugate. The asymptotic uses only the standard Taylor expansion of \(\log\cos z\) at \(0\).

## Relationship to prior work
Wang defines the difference constant and proves that it equals the corresponding optimal nonlinear adjoint lifting constant. The same paper computes the optimal regular factorization norm exactly: for even \(m\), the unnormalized regular norm is \(m\), and after the metric-cotype normalization with \(p=q=2\) the least regular norm is \(\sqrt n\). It also supplies a uniform Banach-valued nonlinear upper bound at sharp scales. The exact scalar \(L_2\) difference constant above is not stated there; the paper's introduction and proofs do not give this Fourier formula or its sharp-scale scalar limit profile. Mendel and Naor introduced the discrete-torus metric-cotype framework and its relation to Rademacher cotype; the present calculation is an exact finite scalar constant for the sign-increment formulation rather than a new metric-cotype equivalence theorem.

## Limitations
The result is restricted to the scalar Hilbert exponent and even \(m\). It does not determine exact constants for non-Hilbertian exponents or Banach-valued targets. An equivalent Fourier/Poincaré computation may exist in older discrete-torus harmonic-analysis literature under different terminology; targeted searches did not locate such a statement. The comparison with regular liftings concerns the regular norm, not the ordinary operator norm of every possible linear lifting.

## References
1. Yue Wang, “Divergence Liftings and Regular Factorizations for Metric Cotype,” arXiv:2609.32589v1, 2026. See Theorem 1.1, Theorem 1.3, and Corollary 1.4.
2. Manor Mendel and Assaf Naor, “Metric cotype,” Annals of Mathematics 168 (2008), 247–298, doi:10.4007/annals.2008.168.247.
