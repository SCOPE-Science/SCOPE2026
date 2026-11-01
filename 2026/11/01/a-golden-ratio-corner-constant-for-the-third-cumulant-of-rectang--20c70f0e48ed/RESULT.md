# A golden-ratio corner constant for the third cumulant of rectangular Fock localization

## Finding
Let \(\mathcal F^2\) be the analytic Bargmann--Fock space on \(\mathbb C\) with squared norm \(\|f\|^2=\pi^{-1}\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z)\). Write \(P\) for its orthogonal projection and \(T_E=P\mathbf 1_E|_{\mathcal F^2}\). Fix arbitrary real \(a,b>0\); for \(R>0\) let \(E_R=[0,aR]+i[0,bR]\).

**Theorem.** There is a constant \(c_{a,b}>0\) such that, as \(R\to\infty\),
\[
\operatorname{Tr}(T_{E_R}-3T_{E_R}^{2}+2T_{E_R}^{3})
=\frac{3}{2\pi^2}\left(\sqrt5-1-\log\frac{1+\sqrt5}{2}\right)
+O_{a,b}(e^{-c_{a,b}R^2}).
\]
The displayed positive constant is approximately \(0.11472437826741094\), and is independent of the rectangle's aspect ratio. Equivalently, it is the limiting third cumulant of the number of particles of the **infinite** complex Ginibre determinantal process inside \(E_R\), when its intensity is \(1/\pi\).

## Assumptions and scope
All rectangle edges are parallel to two perpendicular axes; \(a,b\) are held fixed and strictly positive. The Fock normalization is essential: its unweighted, unitarily equivalent projection kernel on \(L^2(dA)\) is
\[
K(z,w)=\pi^{-1}\exp\big(z\overline w-(|z|^2+|w|^2)/2\big).
\]
The characteristic-function localization \(T_{E_R}\) is a positive trace-class contraction. The cubic polynomial \(h(t)=t-3t^2+2t^3=t(1-t)(1-2t)\) defines the third Bernoulli cumulant on its spectrum. The statement concerns the trace of this *single* operator and does not require a finite-dimensional cutoff.

## Proof
**1. Exact trace integrals.** Write \(A=aR\), \(B=bR\). The diagonal kernel gives \(\operatorname{Tr}T_E=AB/\pi\). Cyclic kernel multiplication and the differences of points give
\[
\operatorname{Tr}T_E^2=\pi^{-2}\int_{\mathbb R^2}e^{-x^2-y^2}(A-|x|)_+(B-|y|)_+\,dx\,dy,
\]
where \(t_+=\max(t,0)\). Thus, extending each integral to the whole line and controlling the Gaussian tails,
\[
\operatorname{Tr}T_E^2=\frac{AB}{\pi}-\frac{A+B}{\pi^{3/2}}+\frac1{\pi^2}+O_{a,b}(e^{-cR^2}). \tag{1}
\]
For the third trace, set the three integration points to \(z,z+u,z+v\), with \(u=x+iy\) and \(v=s+it\). The cyclic Bargmann kernel phase is exactly \(\exp(-|u|^2-|v|^2+u\overline v)\). The intersection of three translated rectangles has area
\[
(A-\Delta(x,s))_+(B-\Delta(y,t))_+,
\quad \Delta(p,q)=\max(0,p,q)-\min(0,p,q)=\tfrac12(|p|+|q|+|p-q|).
\]
Consequently,
\[
\operatorname{Tr}T_E^3=\pi^{-3}\int_{\mathbb R^4}e^{-|u|^2-|v|^2+u\overline v}
(A-\Delta(x,s))_+(B-\Delta(y,t))_+\,dx\,ds\,dy\,dt. \tag{2}
\]
The real part of the exponent in (2) is at most \(-(|u|^2+|v|^2)/2\). Removing the two positive-part cutoffs changes (2) by \(O_{a,b}(e^{-cR^2})\), since any discrepancy forces \(\Delta(x,s)>A\) or \(\Delta(y,t)>B\), hence at least one Gaussian variable to have modulus of order \(R\). All polynomial factors are harmless after slightly reducing \(c>0\).

**2. A four-dimensional complex Gaussian computation.** Order the real coordinates as \((x,s,y,t)\). The quadratic exponent has matrix
\[
M=\begin{pmatrix}
1&-1/2&0&i/2\\
-1/2&1&-i/2&0\\
0&-i/2&1&-1/2\\
i/2&0&-1/2&1
\end{pmatrix}.
\]
Direct elimination gives \(\det M=1\) and its formal covariance \(C=M^{-1}/2\):
\[
C=\tfrac12\begin{pmatrix}
1&1/2&0&-i/2\\
1/2&1&i/2&0\\
0&i/2&1&1/2\\
-i/2&0&1/2&1
\end{pmatrix}.
\]
The normalized integral of the exponential in (2) is \(\pi^2\). Every member of \(X=(x,s,x-s)\) and \(Y=(y,t,y-t)\) has variance \(1/2\), and their normalized cross-correlation matrix is
\[
\rho_{jk}=2\operatorname{Cov}(X_j,Y_k)=
\begin{pmatrix}0&-i/2&i/2\\i/2&0&i/2\\-i/2&-i/2&0\end{pmatrix}. \tag{3}
\]
All covariances here are *complex Gaussian integration identities*, not a claim that a complex probability measure exists.

For a normalized bivariate centered Gaussian integral with marginal variances \(1/2\) and correlation \(\rho\), one has
\[
H(\rho)=\mathbb E[|X||Y|]
=\frac1\pi\big(\sqrt{1-\rho^2}+\rho\arcsin\rho\big),\qquad |\rho|<1. \tag{4}
\]
For real \(\rho\), differentiation under the Gaussian integral followed by two integrations by parts gives \(H'(\rho)=\tfrac12\mathbb E[\operatorname{sgn}(X)\operatorname{sgn}(Y)]\). The standard Gaussian quadrant calculation gives \(\mathbb E[\operatorname{sgn}(X)\operatorname{sgn}(Y)]=2\arcsin(\rho)/\pi\); the quadrant identity itself follows by differentiating the positive-quadrant probability in \(\rho\), obtaining \(1/(2\pi\sqrt{1-\rho^2})\). With \(H(0)=1/\pi\), integration yields (4). Both sides extend holomorphically through \(|\rho|<1\); the normalized Gaussian density retains a positive-definite real part there, so the identity also holds at the purely imaginary values needed below. In particular,
\[
H(0)=\frac1\pi,\qquad
H(\pm i/2)=\frac1{2\pi}\left(\sqrt5-\operatorname{arsinh}(1/2)\right).
\]
Since \(\Delta(X)=\tfrac12\sum_{j=1}^3|X_j|\), (3) has three zero entries and six entries of modulus \(i/2\), giving
\[
\mathbb E\Delta(x,s)=\mathbb E\Delta(y,t)=\frac{3}{2\sqrt\pi},
\]
\[
\mathbb E[\Delta(x,s)\Delta(y,t)]
=\tfrac14\big(3H(0)+6H(i/2)\big)
=\frac{3}{4\pi}\left(1+\sqrt5-\log\frac{1+\sqrt5}{2}\right). \tag{5}
\]
Here \(\operatorname{arsinh}(1/2)=\log((1+\sqrt5)/2)\).

**3. Cancellation.** Substituting (5) into the clipped-free version of (2) yields
\[
\operatorname{Tr}T_E^3=\frac{AB}{\pi}-\frac{3(A+B)}{2\pi^{3/2}}
+\frac{3}{4\pi^2}\left(1+\sqrt5-\log\frac{1+\sqrt5}{2}\right)
+O_{a,b}(e^{-cR^2}). \tag{6}
\]
In \(\operatorname{Tr}T_E-3\operatorname{Tr}T_E^2+2\operatorname{Tr}T_E^3\), the area and perimeter terms cancel exactly; (1) and (6) give the claimed universal constant. Positivity follows from \(\log((1+\sqrt5)/2)<\sqrt5-1\). The Fredholm-determinant expansion for determinantal point counts gives the stated third-cumulant equivalence. \(\square\)

## Verification
Execute `python3 CHECK.py` with SymPy installed. The standalone script exactly inverts the four-dimensional quadratic matrix, reconstructs all nine correlations, verifies area/perimeter cancellation in the final formula, and checks its positive numerical value. This finite test is supplementary; the integral identities, analytic continuation, trace-class justification, and Gaussian-tail estimate above constitute the proof.

## Relationship to prior work
Pfirsch, *A Szegő limit theorem for translation-invariant operators on polygons* (arXiv:1807.04714, first publicly available 2018-07-12), establishes broad polygon corner trace asymptotics for Fourier multipliers \(\mathcal F^*\sigma\mathcal F\). Its operator is translation invariant. The present Fock projection is **magnetically** translation covariant: its triangular phase \(u\overline v\) prevents an immediate reduction to that Fourier-multiplier theorem. Its general corner perspective motivates the question, but its printed theorem does not supply this constant.

Byun and Forrester, *Progress on the study of the Ginibre ensembles I: GinUE* (arXiv:2211.16223, first public 2022-11-29), §3.1, formulate determinantal number counts for general regions and give leading boundary-variance/central-limit results, without this rectangular third-cumulant constant. Charlier, *Asymptotics of determinants with a rotation-invariant weight and discontinuities along circles* (arXiv:2109.03660, first public 2021-09-08), proves refined disk-counting cumulants under rotation-invariant hypotheses; the disk result does not imply the rectangular-corner value. These standard trace/count identities are acknowledged as prior ingredients.

## Limitations
This establishes only axis-perpendicular rectangles with both side lengths proportional to the scaling parameter, in the infinite planar Ginibre/analytic Fock normalization. It does not assert the same constant for general polygons, smoothly bounded domains, finite matrix ensembles, higher Landau levels, or other spectral polynomials. The stated exponential error is not optimized. Historical priority is provisional: a mathematically equivalent result could be embedded in a more general theorem not identified in the literature comparisons; independent verification remains desirable.

## References
1. B. Pfirsch, *A Szegő limit theorem for translation-invariant operators on polygons*, arXiv:1807.04714 (v1, 2018-07-12), https://arxiv.org/html/1807.04714v1; especially §§1–2 and 5.
2. S.-S. Byun and P. J. Forrester, *Progress on the study of the Ginibre ensembles I: GinUE*, arXiv:2211.16223 (v1, 2022-11-29), https://arxiv.org/html/2211.16223v3; especially §3.1.
3. C. Charlier, *Asymptotics of determinants with a rotation-invariant weight and discontinuities along circles*, arXiv:2109.03660 (v1, 2021-09-08), https://arxiv.org/html/2109.03660v2; especially Theorem 1.1, Corollary 1.6, and Remark 1.7.
