# Antipodal balance uniquely optimizes three-mode Fourier observability from two equal arcs

## Finding

For every \(0<a<\pi/2\), observing an unknown three-mode trigonometric polynomial on two disjoint arcs of equal angular width \(2a\) is most stable, in the least-singular-value sense, when the two arc centers are antipodal. The optimizing relative placement is unique, modulo a common rotation, and has least **squared** singular value
\[
L(a)=\frac{2a-\sin(2a)}{\pi}.
\]
The complete squared singular spectrum at this placement, in increasing order, is
\[
\left\{\frac{2a-\sin(2a)}{\pi},\ \frac{2a}{\pi},\ \frac{2a+\sin(2a)}{\pi}\right\}.
\]
Consequently, the optimally placed measurement has sharp worst-case inverse amplification
\[
\|R^\dagger\|=\left(\frac{\pi}{2a-\sin(2a)}\right)^{1/2}.
\]
The result includes an exact positive global deficit and the leading quadratic penalty for shifting the arc centers away from antipodal alignment.

## Assumptions and scope

Let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) have Haar probability measure \(dt/(2\pi)\). Define the complex Hilbert space
\[
V=\operatorname{span}_{\mathbb C}\{e^{-it},1,e^{it}\}
\]
with its inherited \(L^2(\mathbb T)\) norm, so the displayed monomials are an orthonormal basis. Fix \(0<a<\pi/2\) and take two closed arcs of angular length \(2a\) whose interiors are disjoint; coincident endpoints have measure zero. After a global rotation and possibly exchanging the arcs, their centers lie at \(-\theta,\theta\), where \(a\le\theta\le\pi-a\). Write \(E_{a,\theta}\) for their union, and let
\[
R_{a,\theta}:V\longrightarrow L^2(E_{a,\theta},dt/(2\pi))
\]
be restriction. The codomain uses the **unconditional** ambient probability measure, without renormalization by arc area. Let \(G_{a,\theta}=R_{a,\theta}^{*}R_{a,\theta}\).

Define
\[
t=\frac{2a}{\pi},\quad c=\frac{2\sin a}{\pi},\quad
d=\frac{\sin(2a)}{\pi}=c\cos a,\quad
u=\cos\theta,\quad v=d(2u^2-1),\quad H=\sqrt{v^2+8c^2u^2}.
\]
Here \(c>d>0\) and \(-d\le v\le d\). All eigenvalues below are nonnegative and, for \(a>0\), strictly positive.

## Proof

**Exact Gram matrix.** Integration on the two arcs gives the Fourier coefficient
\[
\int_{E_{a,\theta}}e^{ikt}\frac{dt}{2\pi}
=\begin{cases}
2a/\pi,&k=0,\\
\bigl(2\sin(ka)/(k\pi)\bigr)\cos(k\theta),&k\ne0.
\end{cases}
\]
For the frequency ordering \((-1,0,1)\), symmetry makes the Gram matrix real symmetric:
\[
G_{a,\theta}=
\begin{pmatrix}
t&cu&v\\
cu&t&cu\\
v&cu&t
\end{pmatrix}.
\]
The antisymmetric vector \((1,0,-1)\) is an eigenvector of eigenvalue \(t-v\). On the symmetric two-dimensional subspace, the eigenvalues are
\[
t+\frac{v-H}{2},\qquad t+\frac{v+H}{2}.
\]

**Identification of the least eigenvalue.** Always
\[
\lambda_{\min}(G_{a,\theta})=t+\frac{v-H}{2}.
\]
Indeed, when \(v\le0\), the latter does not exceed \(t-v\). When \(v>0\), write \(x=|u|\). Since \(2x^2-1\le x\) on \(0\le x\le1\) and \(c>d>0\), we have \(|cu|\ge v\), hence \(H^2=v^2+8c^2u^2\ge9v^2\). Therefore \(H\ge3v\), so the claimed eigenvalue is no larger than \(t-v\). This also verifies the eigenvalue branch globally, including crossings.

**Global optimum and an exact stability identity.** The least eigenvalue at \(u=0\) is \(t-d\). At any allowed \(u\),
\[
\begin{aligned}
(t-d)-\lambda_{\min}(G_{a,\theta})
&=\frac{H-v-2d}{2}\\
&=\frac{4u^2(c^2-d^2)}{H+v+2d}.
\end{aligned}
\]
The rationalization is valid because \(v+2d=d(1+2u^2)>0\), so the denominator is positive. Since \(c^2-d^2=c^2\sin^2a>0\), the deficit is nonnegative and zero exactly when \(u=0\). As \(a\le\theta\le\pi-a\), this holds only at \(\theta=\pi/2\). Consequently antipodal arc centers are the unique optimal relative configuration, and \(L(a)=t-d=(2a-\sin(2a))/\pi\).

**Complete optimal spectrum and reconstruction norm.** At the antipodal configuration, \(u=0\) and \(v=-d\). The three eigenvalues are \(t-d,t,t+d\), strictly positive because \(0<\sin(2a)<2a\). The restriction is injective, and the Moore--Penrose left inverse on its range has sharp operator norm \((t-d)^{-1/2}\).

**Sharp local penalty.** Put \(\varepsilon=\theta-\pi/2\). Then \(u^2=\varepsilon^2+O(\varepsilon^4)\), \(H+v+2d=2d+O(\varepsilon^2)\), and the exact deficit yields
\[
L(a)-\lambda_{\min}(G_{a,\theta})
=\frac{2(c^2-d^2)}{d}\varepsilon^2+O_a(\varepsilon^4)
=\frac{4\sin^3a}{\pi\cos a}\varepsilon^2+O_a(\varepsilon^4).
\]
The coefficient is positive and is attained in the limit as \(\varepsilon\to0\), so it is the optimal local quadratic coefficient. Finally Taylor's theorem gives
\[
L(a)=\frac{4a^3}{3\pi}+O(a^5),\qquad
\|R^\dagger_{a,\pi/2}\|=\sqrt{\frac{3\pi}{4}}\,a^{-3/2}(1+O(a^2))
\]
as \(a\downarrow0\). These asymptotics do not require an unproved limiting interchange.

## Verification

The proof is exact for every real \(0<a<\pi/2\); finite numerical tests are supplementary only. The standalone `checker.py` evaluates the explicit matrix and its characteristic polynomial by independent finite formulas for sample widths and separations, confirms the global inequality, the rationalized deficit, and the small-angle quadratic curvature, and checks all equality cases on the sample grid. It uses only Python's standard library. Those finite tests neither establish the all-parameter inequality nor certify completeness of the literature; both must be evaluated separately.

## Relationship to prior work

Simons and Wang (2011, arXiv first public 2010-07-29) formulate spatiospectral concentration problems for prescribed spatial windows, including one-dimensional multiple-interval masks; their general integral-operator setup motivates the fixed-band restriction operator here. Wu (2002) derives eigenvalue formulas for symmetric first-order trigonometric regression designs, and studies E-optimal designs when observations are restricted to one connected partial cycle. The present result fixes two **equal-length continuous exposure windows**, varies their relative displacement, proves the **unique** global optimal geometry, and quantifies its **exact** nonlinear loss. Lev (2011, arXiv first public 2011-01-20) studies infinite exponential Riesz bases on multiband sets, a different criterion from the finite three-dimensional least singular value optimized over window placement. The matrix eigenvalue decomposition itself is elementary and not claimed to be new. The contribution is the constrained global geometric optimizer and sharp quantitative deficit.

## Limitations

The theorem optimizes the least singular value, not the Gram determinant, trace, largest eigenvalue, or condition number. It does not address unequal-length arcs, unequal observation densities, arbitrary measurable observation sets, more than two arcs, or Fourier degree two and higher. No originality claim is based on lack of a matching title or on absence from a finite database: a broader unlocated result in experimental design or multiband spectral concentration could imply this special case. All statements rely on two equal arcs, unweighted Haar restriction, and exactly the displayed three Fourier modes.

## References

1. F. J. Simons and D. V. Wang, *Spatiospectral concentration in the Cartesian plane*, arXiv:1007.5226 (first publicly posted 2010-07-29), https://arxiv.org/abs/1007.5226.
2. H. Wu, *Optimal designs for first-order trigonometric regression on a partial cycle*, Statistica Sinica **12** (2002), 917–930, https://www3.stat.sinica.edu.tw/statistica/oldpdf/A12n314.pdf.
3. N. Lev, *Riesz bases of exponentials on multiband spectra*, arXiv:1101.3894 (first publicly posted 2011-01-20), https://arxiv.org/abs/1101.3894.
