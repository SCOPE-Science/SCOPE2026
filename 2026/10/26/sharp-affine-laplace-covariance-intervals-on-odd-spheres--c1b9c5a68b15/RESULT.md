# Sharp affine-Laplace covariance intervals on odd spheres

## Finding
Let \(m\geq1\) be an integer, let \(a>0\), and let \(\theta(x,y)=\arccos\langle x,y\rangle\in[0,\pi]\) be the geodesic distance between points of the unit sphere \(\mathbb S^{2m+1}\). For a real slope \(b\), consider
\[
K_{a,b}(x,y)=e^{-a\theta(x,y)}(1+b\theta(x,y)).
\]
Set
\[
E=e^{-\pi a},\qquad
L_m(a)=-\left(\frac1a-\frac{\pi E}{1-E}+2a\sum_{j=1}^{m}\frac1{a^2+4j^2}\right)^{-1},\qquad
U(a)=\frac{a(1-E)}{1-(1-\pi a)E}.
\]
Then, **for every integer \(m\ge1\) and every \(a>0\)**,
\[
\boxed{K_{a,b}\text{ is positive semidefinite on every finite subset of }\mathbb S^{2m+1}
\quad\Longleftrightarrow\quad L_m(a)\le b\le U(a).}
\]
Every admissible kernel is **strictly positive definite on pairwise distinct sites**, including both endpoints. At \(b=L_m(a)\), precisely the degree-zero Gegenbauer coefficient vanishes; at \(b=U(a)\), no finite-degree coefficient vanishes, although its even-degree spectral tail gains two decay powers. The upper threshold is independent of the dimension, while \(L_m(a)\) is strictly increasing in \(m\), with
\[
L_m(a)=-\frac2\pi-\frac{2a}{\pi^2m}+O_a(m^{-2})\quad(m\to\infty).
\]
Consequently this **one family** is positive definite on every sphere of every finite dimension exactly when
\[
\boxed{-\frac2\pi\le b\le U(a).}
\]
This universal lower boundary has a geometric witness: \(1-2\theta/\pi\) is the correlation of two random hemisphere signs.

## Assumptions and scope
All assertions concern the unit sphere with its intrinsic great-circle metric, real parameters \(a>0\), \(b\in\mathbb R\), and every finite point configuration. The primary dimension classification is for odd sphere dimensions \(2m+1\ge3\). The all-dimension corollary uses equatorial embeddings of even-dimensional spheres into higher odd-dimensional ones; it does not claim an individual sharp bound for every even dimension. The distance profile need not be pointwise nonnegative. Positive definiteness means the usual nonnegative quadratic form for complex coefficients on every finite site set.

The upper bound satisfies \(0<U(a)<a\). The lower bound is negative. At \(a=1\), for instance, \(U(1)=0.87573937173774\ldots\), whereas the respective lower bounds in dimensions three, five and seven are approximately \(-0.79484447857607\), \(-0.72687370762029\), and \(-0.69939418105429\).

## Proof
**1. An exact Gegenbauer transform in every odd dimension.** Set
\[
I_{m,n}(a)=\int_0^\pi e^{-a\theta}C_n^{(m)}(\cos\theta)\sin^{2m}\theta\,d\theta,
\qquad n=0,1,\ldots.
\]
For integers \(m\ge1\), \(n\ge0\), write \(p(\theta)=\sin^{2m}\theta C_n^{(m)}(\cos\theta)\). It is an even trigonometric polynomial with cosine frequencies only in \(\{n,n+2,\ldots,n+2m\}\): frequencies above \(n+2m\) are excluded by polynomial degree, and frequencies below \(n\) vanish by Gegenbauer orthogonality against \(\cos(k\theta)\), a polynomial of degree \(k<n\) in \(\cos\theta\). As \(p\) vanishes to order \(2m\) at the origin, its cosine coefficients \(c_j\) satisfy \(\sum_{j=0}^m c_j(n+2j)^{2r}=0\) for \(0\le r<m\). All frequencies have parity \(n\), and
\[
\int_0^\pi e^{-a\theta}\cos(k\theta)\,d\theta
=\frac{a[1-(-1)^k e^{-\pi a}]}{a^2+k^2}.
\]
After combining the \(m+1\) fractions over their common denominator, the moment cancellations leave a constant numerator. Its value is fixed by the large-\(a\) asymptotic \(I_{m,n}(a)\sim(2m)!C_n^{(m)}(1)a^{-2m-1}\), obtained from \(p(\theta)=C_n^{(m)}(1)\theta^{2m}+O(\theta^{2m+2})\). Thus the exact identity is
\[
\boxed{I_{m,n}(a)=(2m)!\binom{n+2m-1}{2m-1}
\frac{a[1-(-1)^nE]}{\prod_{j=0}^m[a^2+(n+2j)^2]}>0.}
\]
This argument treats \(n=0\) without an exceptional normalization: the factor with \(j=0\) is \(a^2\), which cancels one power of the numerator's \(a\). The positivity is strict for all \(a>0\).

**2. Affine correction as a logarithmic derivative.** Because \(\theta e^{-a\theta}=-\partial_a e^{-a\theta}\), differentiation under the integral yields the unnormalized Schoenberg coefficient
\[
I_{m,n}(a)-bI_{m,n}'(a)=I_{m,n}(a)[1-bR_{m,n}(a)],
\]
where
\[
R_{m,n}(a)=\frac1a+\frac{\pi(-1)^nE}{1-(-1)^nE}
-2a\sum_{j=0}^m\frac1{a^2+(n+2j)^2}.
\]
For fixed parity, \(R_{m,n}(a)\) is strictly increasing in \(n\). Its two parity limits are
\[
R_{m,\mathrm{even},\infty}=\frac1a+\frac{\pi E}{1-E},\qquad
R_{m,\mathrm{odd},\infty}=\frac1a-\frac{\pi E}{1+E},
\]
so the global supremum is the positive, unattained even limit. The degree-zero value is
\[
R_{m,0}=-\frac1a+\frac{\pi E}{1-E}
-2a\sum_{j=1}^m\frac1{a^2+4j^2}<0,
\]
using \(e^{\pi a}-1>\pi a\).

To verify that this degree-zero value is also the global minimum, it remains to compare it with the lowest odd value. Direct subtraction gives
\[
R_{m,1}-R_{m,0}
=2a\sum_{j=0}^m\left[\frac1{a^2+4j^2}-\frac1{a^2+(2j+1)^2}\right]
-\frac\pi{\sinh(\pi a)}.
\]
Each summand is positive. The first alone equals \(2/[a(a^2+1)]\), which exceeds \(\pi/\sinh(\pi a)\): indeed \(\sinh(\pi a)>(\pi/2)a(1+a^2)\) follows from the first two nonzero Taylor terms and \(\pi^2>3\). Hence \(R_{m,1}>R_{m,0}\); monotonicity within each parity proves
\[
\inf_{n\ge0}R_{m,n}=R_{m,0}<0<\sup_{n\ge0}R_{m,n}=\frac1a+\frac{\pi E}{1-E}.
\]
The supremum is approached only along even \(n\to\infty\).

**3. Exact interval, sharpness and strictness.** The Schoenberg theorem reduces positive definiteness to nonnegativity of all the coefficients in step 2. For \(b<0\), the tight inequality is the degree-zero condition \(b\ge1/R_{m,0}=L_m(a)\); for \(b>0\), it is the limiting even-frequency condition \(b\le1/R_{m,\mathrm{even},\infty}=U(a)\). These are also necessary: below the lower boundary the constant coefficient is negative, and above the upper boundary a sufficiently high even coefficient is negative. The endpoints are included. At the lower endpoint precisely degree zero has coefficient zero, whereas every \(n\ge1\) is positive; at the upper endpoint all coefficients are positive because the supremum is not attained. The standard strict Schoenberg criterion on a sphere of dimension at least two—infinitely many positive coefficients of each parity—therefore proves strict positive definiteness even at both endpoints.

At the upper endpoint and even \(n\), the remaining positive factor is exactly
\[
1-U(a)R_{m,n}(a)=2aU(a)\sum_{j=0}^m\frac1{a^2+(n+2j)^2}\sim\frac{2aU(a)(m+1)}{n^2},
\]
which explains the two additional powers of even-degree decay.

**4. Dimension walk and the universal limit.** The formula for \(R_{m,0}\) decreases strictly when \(m\) increases; since it is negative, its reciprocal \(L_m(a)\) increases strictly. The classical partial-fraction identity
\[
\sum_{j=1}^\infty\frac1{a^2+4j^2}
=\frac{\pi a\coth(\pi a/2)-2}{4a^2}
\]
yields \(R_{m,0}\downarrow-\pi/2\). Moreover,
\[
R_{m,0}+\frac\pi2
=2a\sum_{j=m+1}^\infty\frac1{a^2+4j^2}
=\frac{a}{2m}+O_a(m^{-2}),
\]
so reciprocal expansion gives \(L_m(a)=-2/\pi-2a/(\pi^2m)+O_a(m^{-2})\). Every even-dimensional sphere embeds equatorially into an odd-dimensional one, preserving geodesic distance. Consequently the intersection of all finite-dimensional positivity intervals is exactly \([-2/\pi,U(a)]\). As an independent geometric sufficiency check at its lower endpoint, for a standard rotationally invariant random vector \(G\),
\[
\mathbb E[\operatorname{sgn}\langle G,x\rangle\operatorname{sgn}\langle G,y\rangle]
=1-\frac{2\theta(x,y)}\pi;
\]
its product with \(e^{-a\theta}\) is positive definite by the Schur product theorem. This geometric observation is not used to infer the dimension-specific sharp bounds.

## Verification
The accompanying standalone script `verify_spherical_affine.py` uses high-precision numerical integration, symbolic Laurent-polynomial expansion, exact moment cancellations and finite sign tests. On the supplied execution it passed 105 independent integral comparisons (maximum absolute discrepancy below \(8.6\times10^{-50}\)), 35 exact finite-support/moment identities and 1,500 finite-degree sign checks. It additionally checks the first three odd-dimensional endpoint values above. The checker corroborates but cannot replace the all-degree analytic argument or prove novelty. `check_output.txt` records its actual output.

To reproduce, run `python verify_spherical_affine.py` with Python, SymPy and mpmath installed. The checker script and its output log are embedded alongside this report.

## Relationship to prior work
Schoenberg's coefficient criterion and its strict-positivity parity refinement supply the spectral framework. Beatson–zu Castell–Xu develop sufficient spherical Pólya criteria; Gneiting reviews spherical covariance families and proves that the standard geodesic Matérn correction with fixed slope is not admissible. Ziegel studies general convolution roots and smoothness. These sources do not give the free-slope affine-exponential interval on arbitrary odd spheres or the universal large-dimension threshold. The known one-dimensional circle formula already yields the same upper endpoint, but not the dimension-dependent odd-sphere lower endpoints or the high-dimensional limit: positivity on a circle alone does not imply positivity on a higher sphere. The 2026 preprint of Feng–Ge principally treats compactly supported Euclidean-to-sphere inheritance, not the present untruncated free-slope family. Literature comparison is bounded and an uncatalogued equivalent formula remains possible.

## Limitations
The individual exact interval is established for odd sphere dimensions at least three, not for every even dimension separately. The all-dimensional criterion is an intersection statement, not a complete classification of each even dimension. No sample-path regularity or statistical optimality theorem is asserted. Results are analytically proven but have not undergone an independent mathematical audit; the numerical checker is finite evidence only. The originality comparison is limited to the stated inspected primary sources, literature searches and available overlap records; missing or unindexed equivalent work remains possible.

## References
1. R. K. Beatson, W. zu Castell and Y. Xu, *A Pólya criterion for (strict) positive definiteness on the sphere*, arXiv:1110.2437, first posted 2011-10-11, especially the introduction, Theorems 1.1, 1.2, 1.3 and Section 2.
2. T. Gneiting, *Strictly and non-strictly positive definite functions on spheres*, arXiv:1111.7077, first posted 2011-11-30; see Sections 3 and 4 and the exponential and Matérn examples.
3. J. Ziegel, *Convolution roots and differentiability of isotropic positive definite functions on spheres*, arXiv:1201.5833, first posted 2012-01-27; see Theorems 1.1 and 1.2.
4. H. Feng and Y. Ge, *Isotropic Positive Definite Functions on Spheres*, arXiv:2604.11187, first posted 2026-04-13; see the compact-support and dimension-inheritance results for comparison only.
