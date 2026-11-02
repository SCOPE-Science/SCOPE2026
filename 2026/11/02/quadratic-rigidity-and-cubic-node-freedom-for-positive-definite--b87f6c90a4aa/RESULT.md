# Quadratic rigidity and cubic node freedom for positive-definite Bernstein interpolation on the circle

## Finding
For the degree-\(n\) Bernstein sampling operator on \([0,\pi]\) with endpoint-fixed, ordered nodes \(0=x_0\le x_1\le\cdots\le x_n=\pi\), define
\[
(T_{\boldsymbol x}f)(\pi u)=\sum_{j=0}^{n}\binom nj u^j(1-u)^{n-j}f(x_j),\qquad 0\le u\le1.
\]
The operator preserves the cone of continuous functions defining positive-semidefinite isotropic kernels on the circle precisely as follows at the first two degrees with interior nodes:

* At degree \(n=2\), the unique admissible interior node is \(x_1=\pi/2\).
* At degree \(n=3\), the admissible pairs are exactly \(x_1=a\), \(x_2=\pi-a\), where \(0\le a\le\pi/2\).

Thus the quadratic sampling grid is rigid, but the cubic operator admits an entire one-parameter family of nonuniform positivity-preserving sampling grids. In both degrees, the single positive-definite test function \(f(t)=\cos t\) already forces these necessary conditions.

## Assumptions and scope
An isotropic function \(f\in C([0,\pi],\mathbb R)\) is positive definite on the circle when the kernel \((\theta,\varphi)\mapsto f(d_{\mathbb S^1}(\theta,\varphi))\) is positive semidefinite on every finite set. Equivalently, the even periodic continuation has a uniformly absolutely convergent expansion
\[
f(t)=b_0/2+\sum_{m=1}^{\infty}b_m\cos(mt),\qquad b_m\ge0,\quad\sum_{m\ge0}b_m<\infty.
\]
All endpoints and collisions are allowed in the node ordering; repeated interpolation nodes are permitted. Positivity means positive *semidefiniteness*, not strict definiteness. The output is a polynomial on \([0,\pi]\), interpreted through its even periodic continuation.

## Proof
**Cosine coefficient identity.** Put \(P(u)=(T_{\boldsymbol x}\cos(m\cdot))(\pi u)\) and define the output cosine coefficient, for \(k\ge0\), by
\[
C_k(P)=2\int_0^1P(u)\cos(k\pi u)\,du.
\]
For \(k\ge1\), two integrations by parts, followed by the same operation on \(P''\), give, for every polynomial of degree at most three,
\[
C_k(P)=\frac{2((-1)^kP'(1)-P'(0))}{(\pi k)^2}-\frac{2((-1)^kP'''(1)-P'''(0))}{(\pi k)^4},
\]
where \(P'''=0\) at degree at most two. Also \(C_0(P)=\tfrac{2}{n+1}\sum_{j=0}^{n}\cos(mx_j)\), by integrating each Bernstein basis polynomial. By the positive cosine-series representation, preserving the cone is equivalent to \(C_k(P)\ge0\) for every integer \(m\ge0\), \(k\ge0\).

**Necessity at degree two.** Let the nodes be \((0,a,\pi)\) and put \(c=\cos a\). For the input \(f(t)=\cos t\), the samples are \((1,c,-1)\). Direct calculation yields
\[
C_0=\frac{2c}{3},\qquad C_{2h}=-\frac{8c}{(2\pi h)^2}\quad(h\ge1).
\]
Nonnegativity of both forces \(c=0\), hence \(a=\pi/2\).

**Necessity at degree three.** Write the nodes as \((0,a,b,\pi)\) and put \(c_1=\cos a\), \(c_2=\cos b\). The same input gives
\[
C_0=\frac{c_1+c_2}{2},\qquad C_{2h}=-\frac{6(c_1+c_2)}{(2\pi h)^2}+O(h^{-4})\quad(h\to\infty).
\]
If all coefficients are nonnegative, the zeroth coefficient forces \(c_1+c_2\ge0\), while the even high-frequency tail forces \(c_1+c_2\le0\). Thus \(\cos a+\cos b=0\). Strict monotonicity of cosine on \([0,\pi]\) gives \(b=\pi-a\), and ordering yields \(0\le a\le\pi/2\).

**Sufficiency at degree two.** For \(a=\pi/2\), every odd input frequency has sample values \((1,0,-1)\), and hence \(P(u)=1-2u\). Its zeroth and positive even coefficients vanish, and each positive odd coefficient equals \(8/(\pi k)^2>0\). For even input frequency, put \(c=\cos(m\pi/2)\in\{-1,1\}\); then
\[
P(u)=1+2(c-1)u(1-u).
\]
Its zeroth coefficient is \(2(2+c)/3>0\), its positive odd coefficients vanish, and its positive even coefficients are \(8(1-c)/(\pi k)^2\ge0\). The constant input is preserved.

**Sufficiency at degree three.** Fix \(0\le a\le\pi/2\) and the symmetric grid \((0,a,\pi-a,\pi)\). For an even input frequency \(m\), let \(c=\cos(ma)\in[-1,1]\). The samples are \((1,c,c,1)\), so
\[
P(u)=1+3(c-1)u(1-u).
\]
Here \(C_0=1+c\ge0\), all positive odd coefficients vanish, and the positive even coefficients equal \(12(1-c)/(\pi k)^2\ge0\).

For odd input frequency \(m\), the samples are \((1,c,-c,-1)\), with the same bound \(-1\le c\le1\). The resulting polynomial is
\[
P(u)=1+3(c-1)u+(3-9c)u^2+(6c-2)u^3.
\]
Antisymmetry around \(u=1/2\) makes \(C_0\) and all positive even coefficients zero. For every positive odd integer \(k\), the identity above reduces to
\[
C_k(P)=\frac{12}{(\pi k)^4}\left[(1-c)(\pi k)^2+4(3c-1)\right].
\]
For \(k=1\), the bracket is increasing in \(c\), since \(12-\pi^2>0\); its minimum, at \(c=-1\), is \(2\pi^2-16>0\). For odd \(k\ge3\), the bracket is decreasing in \(c\), since \((\pi k)^2>12\); its minimum, at \(c=1\), is \(8>0\). Thus all coefficients are nonnegative for every cosine input frequency. Uniform convergence and positivity of the input coefficients extend preservation from the cosine generators to the full cone. This proves both classifications.

## Verification
The analytic coefficient identity can be verified by repeated integration by parts. The displayed formulas can alternatively be verified by expanding the Bernstein polynomials in powers of \(u\). The supplementary standalone Python 3 script `CHECK.py` independently constructs those polynomials from node samples and checks coefficient identities, nonnegativity, and nonsymmetric-node obstructions over a finite grid of angles and modes. Its executed run passed 35,102 checks. These finite comparisons supplement but do not replace the proof for all nodes and Fourier modes.

## Relationship to prior work
Otten, Nguyen and Watts proved that the **uniform** degree-\(n\) Bernstein operator, sampled at \(j\pi/n\), preserves circle positive definiteness for all integers \(n\ge1\) [1]. The present statement classifies **all ordered endpoint-fixed sampling grids** in degrees two and three. In degree three the previously treated uniform grid corresponds only to \(a=\pi/3\), whereas every \(a\in[0,\pi/2]\) is permitted. The classification and its necessity statement do not follow from the uniform-grid theorem alone. Generalized Bernstein-operator studies such as [2] concern different shape/reproduction properties, not this Fourier coefficient cone.

## Limitations
No classification is asserted for degrees \(n\ge4\), arbitrary non-Bernstein polynomial bases, higher-dimensional spheres, or strict positive definiteness. The cubic family contains nonuniform nodes, but it is not claimed to exhaust every possible cone-preserving approximation operator outside the specified Bernstein basis and endpoint conditions. The literature-overlap search is not an independence or priority certificate.

## References
[1] M. Otten, N. Nguyen, T. Watts, *Preservation of Positive-Definiteness by Bernstein Operators on the Circle*, arXiv:2608.04836 (first public 2026-08-05), https://arxiv.org/abs/2608.04836.

[2] J. M. Aldaz, O. Kounchev, H. Render, *Shape Preserving Properties of Generalized Bernstein Operators on Extended Chebyshev Spaces*, arXiv:0805.1614 (2008), https://arxiv.org/abs/0805.1614.
