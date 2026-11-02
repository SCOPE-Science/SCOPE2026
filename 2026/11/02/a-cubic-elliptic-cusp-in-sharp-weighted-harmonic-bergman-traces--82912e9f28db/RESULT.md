# A cubic elliptic cusp in sharp weighted harmonic Bergman traces

## Finding
Let \(\alpha>-1\). For \(0<r<1\) and real \(\varepsilon\) sufficiently small, let \(C_{r,\varepsilon}\) be the ellipse
\[
z(\theta)=r(e^{i\theta}+\varepsilon e^{-i\theta}),\quad 0\le\theta<2\pi.
\]
Let \(\mathcal H_\alpha\) be the complex harmonic functions in the unit disk with squared Hilbert norm
\[
\|f\|_\alpha^2=\frac{\alpha+1}{\pi}\int_{|z|<1}|f(z)|^2(1-|z|^2)^\alpha\,dA(z).
\]
Define the optimal *squared* trace constant
\[
\mathcal K_\alpha(r,\varepsilon)
=\sup_{f\in\mathcal H_\alpha\setminus\{0\}}
\frac{\int_{C_{r,\varepsilon}}|f(z)|^2(1-|z|^2)^{\alpha+1}\,|dz|}{\|f\|_\alpha^2}.
\]
Put \(s=r^2\). For every fixed \(\alpha>-1\) and
\[
\frac1{\alpha+2}<s<\frac2{\alpha+3},
\]
the unperturbed sharp constant is
\[
K_0=\mathcal K_\alpha(r,0)=2\pi r(1-s)^{\alpha+1}(\alpha+2)s,
\]
and the sharp first-order ellipticity response is
\[
\boxed{\frac{\mathcal K_\alpha(r,\varepsilon)}{K_0}
=1+\frac{|3-(2\alpha+5)s|}{2(1-s)}|\varepsilon|+O_{\alpha,s}(\varepsilon^2).}
\]
There is exactly one radius in this first-harmonic regime where the linear cusp disappears:
\[
\boxed{s_*=\frac3{2\alpha+5}.}
\]
At this radius the full sharp quadratic response is
\[
\boxed{\frac{\mathcal K_\alpha(\sqrt{s_*},\varepsilon)}{K_0}
=1+\frac{(\alpha-2)(2\alpha+5)}{4(\alpha+1)(5\alpha+14)}\varepsilon^2
+O_\alpha(|\varepsilon|^3).}
\]
At the distinguished weight and radius \(\alpha=2\), \(r=1/\sqrt3\), the quadratic response also vanishes; the first nonzero correction is the **sharp cubic cusp**
\[
\boxed{\mathcal K_2(1/\sqrt3,\varepsilon)
=\frac{64\pi}{81\sqrt3}\left(1+\frac9{16}|\varepsilon|^3+O(\varepsilon^4)\right).}
\]
All remainders concern real \(\varepsilon\to0\) with \(\alpha,s\) fixed and with the entire ellipse inside the disk. These are expansions of the actual optimum over all complex harmonic functions, not of a restricted polynomial test family.

## Assumptions and scope
Area measure \(dA\) is ordinary Euclidean area, and the arc integral uses Euclidean length. The constant is the norm squared of the restriction operator from \(\mathcal H_\alpha\) into the weighted \(L^2\) space on the ellipse. The parameter \(\varepsilon\) may have either sign; replacing it by its negative rotates the ellipse through \(\pi/2\), leaving the optimum unchanged. The chosen radius interval is open; no uniform remainder at its endpoints is asserted. The weight \(\alpha\) is arbitrary real above \(-1\), not restricted to integers.

## Proof
**1. Circle spectral gap.** Define \(\beta=\alpha+1\), \(R=1-s\), and \((v)_n=v(v+1)\cdots(v+n-1)\), with \((v)_0=1\). Angular orthogonality and a beta integral give the harmonic orthonormal basis
\[
e_0=1,\qquad e_n^+(z)=\sqrt{\frac{(\alpha+2)_n}{n!}}z^n,\qquad
e_n^-(z)=\sqrt{\frac{(\alpha+2)_n}{n!}}\overline z^{\,n}\quad(n\ge1).
\]
The self-adjoint trace form for \(\varepsilon=0\) is diagonal in this basis, with eigenvalues
\[
d_n=2\pi rR^\beta s^n\frac{(\alpha+2)_n}{n!},\qquad
\frac{d_{n+1}}{d_n}=s\frac{n+\alpha+2}{n+1}.
\]
The ratios decrease strictly with \(n\) and eventually fall below one. Hence \(d_1\) is strictly greater than every other distinct eigenvalue exactly in the displayed open interval. It has multiplicity two, with eigenspace \(E=\operatorname{span}\{e_1^+,e_1^-\}\).

**2. Analytic compact family and first variation.** The ellipse remains in a fixed compact subdisk for sufficiently small \(|\varepsilon|\). Cauchy estimates for the analytic and anti-analytic components make the trace form a real-analytic family of compact self-adjoint operators in operator norm. Thus the isolated two-dimensional spectral cluster near \(d_1\) admits ordinary analytic finite-dimensional perturbation reductions; all other modes remain separated by a gap. With \(u=e^{i\theta}\), \(c=\cos2\theta\), and
\[
L=1+\frac{2\beta s}{R},
\]
the ellipse geometry gives, uniformly in \(\theta\),
\[
\frac{(1-|z(\theta)|^2)^\beta|z'(\theta)|}{rR^\beta}
=1-L\varepsilon c+O(\varepsilon^2).
\]
Moreover \(z(\theta)^2/s=u^2+2\varepsilon+\varepsilon^2u^{-2}\). Fourier averaging produces, on \(E\),
\[
P T'(0)P=d_1\begin{pmatrix}0&2-L/2\\2-L/2&0\end{pmatrix}.
\]
Its largest first-order eigenvalue for signed \(\varepsilon\) is \(d_1|2-L/2|\,|\varepsilon|\). The explicit formula follows from \(2-L/2=[3-(2\alpha+5)s]/[2R]\). The unique zero is \(s_*\), and it lies strictly between the stated interval endpoints because \(\alpha+1>0\).

**3. Exact quadratic coefficient at the cancellation radius.** The normalized arc-weight factor through order two equals
\[
1-L\varepsilon c+\varepsilon^2(D_0+D_2c^2)+O(\varepsilon^3),
\]
where
\[
D_0=\frac12-\frac{\beta s}{R},\qquad
D_2=-\frac12+\frac{2\beta s}{R}+\frac{2\beta(\beta-1)s^2}{R^2}.
\]
At \(s=s_*\), \(L=4\). The direct second-order coefficient on each basis vector in \(E\), divided by \(d_1\), is
\[
q_{\rm direct}=\frac14-\frac{2\beta s}{R}+\frac{\beta(\beta-1)s^2}{R^2}.
\]
Fourier selection allows a first-order coupling from \(e_1^+\) only to \(e_3^+\) outside \(E\), and from \(e_1^-\) only to \(e_3^-\). The two first-order coupling moduli equal \(d_1\sqrt{x}\), where
\[
x=\frac{s^2(\beta+2)(\beta+3)}6=\frac{d_3}{d_1}<1.
\]
The off-diagonal second-order effective entry on \(E\) is zero by the Fourier selection rule. The second-order spectral shift, divided by \(d_1\), is therefore
\[
q_{\rm direct}+\frac{x}{1-x}
=\frac{(\beta-3)(2\beta+3)}{4\beta(5\beta+9)}.
\]
Substituting \(\beta=\alpha+1\) proves the universal quadratic formula. In particular, the quadratic term vanishes if and only if \(\alpha=2\).

**4. Exact cubic splitting at the doubly exceptional point.** Set \(\beta=3\), \(s=1/3\); then \(L=4\), \(x=5/9\). Write the normalized arc-weight factor as \(1+\varepsilon W_1+\varepsilon^2W_2+\varepsilon^3W_3+O(\varepsilon^4)\). Direct expansion gives
\[
W_1=-4c,\quad W_2=-1+\frac{11}{2}c^2,\quad
W_3=\frac72c-3c^3.
\]
The coefficient of \(\varepsilon^3\) in the \((e_1^+,e_1^-)\) matrix entry is \((17/8)d_1\). The coefficient of \(\varepsilon^2\) connecting \(e_3^+\) to \(e_1^-\) is \((-5/8)d_1\sqrt{x}\), with the conjugate-reflected coupling likewise. Consequently the two second-plus-first-order indirect paths contribute
\[
2\frac{d_1\sqrt{x}\,[-(5/8)d_1\sqrt{x}]}{d_1-d_3}
=-\frac{25}{16}d_1.
\]
Three successive first-order couplings through the orthogonal complement cannot connect the opposite first harmonics: every nonzero first-order step changes the angular index by exactly two, and the only first-order edge from \(e_1^+\) into the complement goes to \(e_3^+\), while the only such edge into \(e_1^-\) comes from \(e_3^-\). Diagonal cubic terms vanish by parity, and the first- and second-order reduced matrices are zero. The effective cubic matrix is thus
\[
\frac9{16}d_1\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
Its eigenvalues are \(\pm(9/16)d_1\varepsilon^3+O(\varepsilon^4)\). Taking the maximum gives the claimed \(|\varepsilon|^3\) cusp; \(d_1=64\pi/(81\sqrt3)\). Compact analytic perturbation justifies the remainders for the actual infinite-dimensional optimum.

## Verification
Run the standalone standard-library script `python3 checker.py`. It expands the ellipse arc Jacobian and radial weight as rational bivariate Taylor–Laurent series, and verifies 70 exact rational coefficient, cancellation, and coupling identities for nine rational weights including the doubly exceptional one. Separate finite-section numerical quadrature checks were used for consistency, but neither type of finite computation establishes the infinite-dimensional statement; the compact spectral-gap argument in the proof does.

## Relationship to prior work
Halder and Kumar's July 15, 2026 preprint proves the general weighted harmonic Bergman Gabriel inequality for convex curves and an explicit circle inequality. Those estimates ensure boundedness but do not give the optimal constant under a noncircular shape perturbation. A subsequent exact circular trace staircase determines the diagonal sharp constants at concentric circles; its circular computation explains the unperturbed twofold first-harmonic multiplicity but does not determine shape derivatives. The present result computes the actual elliptic perturbation through the first nonvanishing order, including the exceptional cubic splitting.

## Limitations
Only centered ellipses generated by the displayed area-preserving-to-first-order affine deformation are treated. The radius is required to be in the open first-harmonic spectral regime; endpoint eigenvalue collisions and other Fourier regimes are not classified. Error constants depend on fixed weight and radius. Exact higher-order coefficients away from the displayed exceptional case are not determined, and the result does not claim a general sharp norm for arbitrary convex curves or finite elliptic eccentricity. Same-source and historical overlap checks cannot prove mathematical uniqueness.

## References
1. H. Halder and R. Kumar, *Gabriel's and Frazer's problems for weighted Bergman spaces and their applications*, arXiv:2607.13543v1, first publicly submitted 2026-07-15. Theorems 1.1–1.3 and proofs in Section 3.
2. T. Kato, *Perturbation Theory for Linear Operators*, Springer, chapters on isolated eigenvalues of analytic compact operator families (standard perturbative machinery; no assertion of originality for this tool).
