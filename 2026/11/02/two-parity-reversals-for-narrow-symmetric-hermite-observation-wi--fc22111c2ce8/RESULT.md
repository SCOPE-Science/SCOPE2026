# Two parity reversals for narrow symmetric Hermite observation windows

## Finding
Let \(h_j(x)=\pi^{-1/4}(2^j j!)^{-1/2}H_j(x)e^{-x^2/2}\), \(j=0,1,2\), be the first three orthonormal real Hermite functions. Restrict signals from \(V=\operatorname{span}\{h_0,h_1,h_2\}\) to the two symmetric observation intervals
\[
E_{a,\varepsilon}=[-a-\varepsilon,-a+\varepsilon]\cup[a-\varepsilon,a+\varepsilon],\qquad a>\varepsilon>0.
\]
Let \(\Lambda_{\rm even}(a,\varepsilon)\) be the larger eigenvalue of the concentration Gram matrix restricted to \(\operatorname{span}\{h_0,h_2\}\), and let \(\Lambda_{\rm odd}(a,\varepsilon)=\int_{E_{a,\varepsilon}}h_1(x)^2\,dx\). There is \(\varepsilon_0>0\) such that for all \(0<\varepsilon<\varepsilon_0\) there are **exactly two** distinct centers \(a_-(\varepsilon)<a_+(\varepsilon)\) in \((\varepsilon,\infty)\) where the largest even and odd concentrations coincide. They are real analytic in \(\varepsilon^2\) near zero and satisfy
\[
a_-(\varepsilon)^2=\frac12+\frac{\varepsilon^2}{3}+O(\varepsilon^4),\qquad
 a_+(\varepsilon)^2=\frac32+\frac{\varepsilon^2}{3}+O(\varepsilon^4).
\]
The maximum of \(\int_{E_{a,\varepsilon}}|f|^2\) over all unit vectors \(f\in V\) lies in the **even** sector for \(\varepsilon<a<a_-\) and for \(a>a_+\), but in the **odd** sector for \(a_-<a<a_+\). Each crossing has a two-dimensional top eigenspace (one even and one odd direction); there is no third top mode. Thus a pair of symmetric narrow detectors induces two and only two switches of the maximizing oscillator parity as the detector separation grows, and both threshold squared radii move outward by the same \(\varepsilon^2/3\) term.

## Assumptions and scope
All functions use the physicists' Hermite-polynomial convention \(H_0=1\), \(H_1=2x\), \(H_2=4x^2-2\). Intervals are disjoint because \(a>\varepsilon\); endpoints have measure zero. The observation operator is the orthogonal compression of multiplication by \(\mathbf1_{E_{a,\varepsilon}}\) onto the **three-dimensional** space \(V\). The classification is uniform over every center \(a>\varepsilon\) once the fixed half-width \(\varepsilon\) is sufficiently small. The theorem does not address larger Hermite bands or arbitrary nonsymmetric windows.

## Proof
**Parity reduction and exact integral formula.** Since the mask is even and \(h_j(-x)=(-1)^j h_j(x)\), the Hermite concentration matrix is the direct sum of an even \(2\times2\) matrix \(B\) and the scalar \(q\) from \(h_1\). Put \(c=\pi^{-1/4}\), \(\ell=a-\varepsilon\), \(u=a+\varepsilon\), and \(I_{2m}=\int_{\ell}^{u}x^{2m}e^{-x^2}\,dx\). Then
\[
 B=2c^2\begin{pmatrix}
 I_0&(2I_2-I_0)/\sqrt2\\
 (2I_2-I_0)/\sqrt2&2I_4-2I_2+I_0/2
 \end{pmatrix},\qquad q=4c^2I_2.
\]
For \(\varepsilon>0\), \(B\) is positive definite because its columns are integrals of two independent real-analytic functions on a nonempty open interval. Its largest eigenvalue is \((\operatorname{tr}B+\sqrt{(B_{00}-B_{22})^2+4B_{02}^2})/2\). This yields an exact nonnumerical test for the parity ordering.

**Thin-window limit and its two simple zeros.** Let \(v(x)=(h_0(x),h_2(x))^T\), \(S(x)=\|v(x)\|^2\), \(Q(x)=h_1(x)^2\), and
\[
 F(a,\varepsilon)=\frac{\Lambda_{\rm even}(a,\varepsilon)-\Lambda_{\rm odd}(a,\varepsilon)}{4\varepsilon}.
\]
On compact subsets of \((0,\infty)\), \(B/(4\varepsilon)=v(a)v(a)^T+O(\varepsilon^2)\) in the differentiable and real-analytic sense, and \(q/(4\varepsilon)=Q(a)+O(\varepsilon^2)\). The positive simple eigenvalue of the rank-one leading term is \(S(a)>0\), so \(F\) extends real-analytically in \((a,\varepsilon^2)\) near \(\varepsilon=0\). Writing \(y=a^2\) gives
\[
F(a,0)=\pi^{-1/2}e^{-y}\left(2y^2-4y+\frac32\right)
=2\pi^{-1/2}e^{-y}(y-\tfrac12)(y-\tfrac32).
\]
Its only positive zeros are \(a=1/\sqrt2\) and \(a=\sqrt{3/2}\), both simple.

**The shared quadratic shift.** The symmetric integral expansion gives
\[
\frac{B}{4\varepsilon}=vv^T+\frac{\varepsilon^2}{6}(vv^T)''+O(\varepsilon^4),\qquad
\frac{q}{4\varepsilon}=Q+\frac{\varepsilon^2}{6}Q''+O(\varepsilon^4).
\]
For a simple rank-one eigenvalue, first-order matrix perturbation implies
\[
 F(a,\varepsilon)=S-Q+\frac{\varepsilon^2}{6}
 \left((S-Q)''-2\frac{(v_1v_2'-v_2v_1')^2}{S}\right)+O(\varepsilon^4).
\]
Set \(P(y)=2y^2-2y+3/2\), so \(S=\pi^{-1/2}e^{-y}P(y)\) and \((v_1v_2'-v_2v_1')^2/S=\pi^{-1/2}e^{-y}\,8y/P(y)\). For \(D(y)=2y^2-4y+3/2\), direct differentiation yields
\[
 \frac{(S-Q)''}{\pi^{-1/2}e^{-y}}=8y^3-52y^2+70y-11.
\]
At \(y=1/2\), the coefficient of \(\varepsilon^2\) in \(F/(\pi^{-1/2}e^{-y})\) equals \(2/3\), while \(D'(y)=-2\). At \(y=3/2\) these numbers are \(-2/3\) and \(2\), respectively. Applying the analytic implicit-function theorem **in squared center \(y\)** gives the common shift \(\delta y=\varepsilon^2/3+O(\varepsilon^4)\).

**No other crossings, including unbounded centers.** The analytic expansion converges in \(C^1\) uniformly for \(a\in[3/5,3/2]\), and \(F(a,0)\) has just the above two simple zeros there. The implicit-function theorem on small neighborhoods of the zeros, and uniform nonvanishing on the compact complement, therefore give precisely two zeros in that interval and the asserted alternating signs. For \(\varepsilon<1/20\) and \(a\le3/5\), every \(x\in[a-\varepsilon,a+\varepsilon]\) has \(x^2<1/2\), whence \(h_0(x)^2>h_1(x)^2\); therefore \(\Lambda_{\rm even}>q\). For \(a\ge3/2\), the inequality \(x^2>1+\sqrt3/2\) holds for all \(x\in[a-\varepsilon,a+\varepsilon]\) when \(\varepsilon<1/20\); the identity
\[
 h_2(x)^2-h_1(x)^2=\pi^{-1/2}e^{-x^2}\left(2x^4-4x^2+\tfrac12\right)>0
\]
then again gives \(\Lambda_{\rm even}>q\). These two pointwise comparisons exclude crossings outside the compact interval, for the same sufficiently small width. At either crossing the lower even eigenvalue is \(O(\varepsilon^3)\) locally, whereas the common top eigenvalue is a strictly positive multiple of \(\varepsilon\); hence exactly two top eigenvectors occur.

## Verification
The accompanying standalone program `hermite_two_windows_checker.py` independently forms the Gram matrix from error functions and elementary boundary terms, tests the precise parity signs and both crossing locations for decreasing widths, verifies the asymptotic coefficient numerically, and checks the symbolic second-order formulas by exact differentiation. These finite tests support the proof but do not establish the all-center classification; that follows from the compactness, pointwise inequalities, and analytic-implicit-function arguments above. Run with `python hermite_two_windows_checker.py` (Python 3 with SymPy, SciPy and NumPy).

## Relationship to prior work
Boiti, Jornet and Oliaro (first public arXiv version 14 April 2023) establish harmonic-oscillator and Wigner mean-dispersion principles, with Hermite functions as equality cases. That result concerns full-line moments of orthonormal sequences, not the maximum concentration on two short disjoint intervals. Dicke, Seelmann and Veselić prove spectral inequalities for finite Hermite bands on geometrically controlled observation sets; their quantitative lower bounds and control-theoretic statements neither determine the parity of the **largest** rank-three concentration eigenvector nor give these two switching centers. Castro and Grünbaum treat commuting operators for time-band limiting with **exceptional** orthogonal-polynomial families and half-line truncation; the constructions are distinct from the present ordinary three-mode, two-window parity classification. The classical Hermite identities, parity splitting and rank-one perturbation formula are standard and not claimed as new. The claimed new content is the global exactly-two-switch classification and the common explicit quadratic drift for positive but small window width.

## Limitations
The theorem is asymptotic in window half-width; it does not give a numerical universal cutoff, and it does not classify wide windows, higher modes, or optimizing detector locations under an area constraint. Historical priority beyond the inspected literature cannot be guaranteed, and the analysis has not undergone independent validation.

## References
1. C. Boiti, D. Jornet and A. Oliaro, *Mean-Dispersion Principles and the Wigner Transform*, arXiv:2304.06965 (first submitted 14 April 2023); *J. Geom. Anal.* 34, 159 (2024), doi:10.1007/s12220-024-01601-0.
2. A. Dicke, A. Seelmann and I. Veselić, *Uncertainty Principle for Hermite Functions and Null-Controllability with Sensor Sets of Decaying Density*, *J. Fourier Anal. Appl.* 29, 11 (2023), doi:10.1007/s00041-022-09989-5.
3. M. M. Castro and F. A. Grünbaum, *A new commutativity property of exceptional orthogonal polynomials*, arXiv:2210.13928; *Rev. R. Acad. Cienc. Exactas Fis. Nat. Ser. A Mat.* 118, 81 (2024), doi:10.1007/s13398-024-01570-7.
