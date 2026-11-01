# Sharp isoperimetric Willmore envelope and curvature-mode rigidity for planar-core tubes

## Finding
For every embedded, once-traversed simple closed planar core \(\gamma\) with an embedded Euclidean radius-\(r\) tube, fix the tube's surface area \(S\) and enclosed volume \(V\). Define the dimensionless ratio
\[
\rho=\frac{S^3}{16\pi^2V^2}>1.
\]
The Willmore energy \(\mathcal W=\int H^2\,dA\), with \(H\) the arithmetic mean of the principal curvatures, satisfies the **sharp restricted-class isoperimetric law**
\[
\mathcal W\ge\frac{\pi^2\rho^2}{\sqrt{\rho^2-1}}.
\]
Equality holds exactly for circular planar cores. This is a sharp statement within planar-core constant-radius tubes, **not** a global inequality asserting the same bound for all embedded tori.

Writing \(L\) for core length, \(\kappa\) for its signed curvature, and \(q=2\pi r/L\), there is the quantitative gap
\[
\mathcal W-\frac{\pi^2\rho^2}{\sqrt{\rho^2-1}}\ge
\frac{\pi r}{4(1-q^2)^{3/2}}\int_0^L\left(\kappa(s)-\frac{2\pi}{L}\right)^2ds.
\]
The coefficient gives a valid global curvature control; no claim of best possible global coefficient is made.

For a circle of radius \(R=L/(2\pi)>r\), write a nearby strictly convex core by its support function \(h_\epsilon(\phi)=R+\epsilon f(\phi)\), where \(f\) is smooth with vanishing mean and vanishing first Fourier harmonics (the latter only remove translations). With tube radius \(r\) fixed, hence with \(S,V\) fixed, the **exact quadratic expansion** is
\[
\mathcal W_\epsilon-\mathcal W_0=
\frac{\pi r(R^2+2r^2)}{4(R^2-r^2)^{5/2}}\epsilon^2
\int_0^{2\pi}(f+f'')^2\,d\phi+O_f(\epsilon^3).
\]
Its spectral gap relative to \(\int f^2\) is exactly \(9\) times the displayed prefactor. Equality in the limiting Rayleigh quotient holds exactly for degree-two harmonics \(f=a\cos(2\phi)+b\sin(2\phi)\), not for higher modes.

## Assumptions and scope
The oriented curve \(\gamma:\mathbb R/L\mathbb Z\to\mathbb R^2\) is \(C^4\), regular, simple, traversed once, and oriented counterclockwise; its signed curvature obeys \(\int_0^L\kappa\,ds=2\pi\). The radius satisfies \(0<r<\operatorname{reach}(\gamma)\), guaranteeing that the solid tube is embedded and \(|r\kappa(s)|<1\) everywhere. Tangent and inward normal are chosen consistently. The tube lies in \(\mathbb R^3\) around \(\gamma\) in its horizontal plane.

The two physical constraints determine the tube radius and core length:
\[
S=2\pi rL,\qquad V=\pi r^2L,\qquad r=\frac{2V}{S},\qquad L=\frac{S^2}{4\pi V}.
\]
Consequently \(\rho=L/(2\pi r)\). Feasible constraints require \(\rho>1\), since any simple closed planar core with embedded tube has \(L>2\pi r\). For each feasible \(\rho>1\), the equality-case circle of radius \(R=\rho r\) is admissible.

## Proof
**1. Exact geometry and classical forward integral.** With arclength \(s\), inward normal \(n(s)\) and vertical unit vector \(e_z\), parametrize the surface by
\[
F(s,\theta)=\gamma(s)+r\cos\theta\,n(s)+r\sin\theta\,e_z.
\]
Its unsigned area element is \(r(1-r\kappa(s)\cos\theta)\,ds\,d\theta\). Up to common orientation reversal, the principal curvatures are \(1/r\) and \(-\kappa\cos\theta/(1-r\kappa\cos\theta)\). Therefore
\[
H^2dA=\frac{(1-2r\kappa\cos\theta)^2}{4r(1-r\kappa\cos\theta)}\,ds\,d\theta.
\]
The algebraic identity \((1-2tc)^2/(1-tc)=1/(1-tc)-4tc\), together with \(\int_0^{2\pi}(1-t\cos\theta)^{-1}d\theta=2\pi/\sqrt{1-t^2}\) for \(|t|<1\), yields
\[
\mathcal W=\frac\pi{2r}\int_0^L \frac{ds}{\sqrt{1-r^2\kappa(s)^2}}.
\]
This expression is a specialization and explicit angular integration of established tubular-surface curvature/Willmore formulas; the **forward formula itself is not claimed original**.

**2. Sharp fixed-constraint bound.** Set \(g(z)=(1-z)^{-1/2}\), strictly convex on \([0,1)\); put \(q=r(2\pi/L)\). Its supporting line at \(q^2\) gives
\[
g(r^2\kappa^2)\ge g(q^2)+\frac{r^2\kappa^2-q^2}{2(1-q^2)^{3/2}}.
\]
Integration, \(\int\kappa=2\pi\), and \(\int_0^L(\kappa^2-\kappa_0^2)ds=\int_0^L(\kappa-\kappa_0)^2ds\) give the quantitative inequality stated above. Dropping its nonnegative right-hand side and substituting \(L=2\pi\rho r\) gives exactly \(\mathcal W\ge\pi^2\rho^2/\sqrt{\rho^2-1}\). Equality requires \(\kappa\equiv\kappa_0\), hence the embedded once-traversed core is a circle. Conversely that circle attains equality.

**3. Sharp constrained spectral mode.** A strictly convex planar curve with support function \(h\) has curvature radius \(p=h+h''\), turning-angle arclength \(ds=p\,d\phi\), and curvature \(\kappa=1/p\). Thus
\[
\mathcal W=\frac\pi{2r}\int_0^{2\pi}F(p(\phi))\,d\phi,
\qquad F(p)=\frac{p^2}{\sqrt{p^2-r^2}},\ p>r.
\]
For \(p=R+\epsilon(f+f'')\), the fixed-perimeter assumption \(\int f=0\) makes the first variation vanish. Exact differentiation gives
\[
F''(R)=\frac{r^2(R^2+2r^2)}{(R^2-r^2)^{5/2}},
\]
which yields the asserted Taylor expansion. If \(f=\sum_{k\ge2}(a_k\cos k\phi+b_k\sin k\phi)\), then Parseval yields
\[
\frac{\int_0^{2\pi}(f+f'')^2d\phi}{\int_0^{2\pi}f^2d\phi}
=\frac{\sum_{k\ge2}(k^2-1)^2(a_k^2+b_k^2)}{\sum_{k\ge2}(a_k^2+b_k^2)}\ge9.
\]
Equality occurs exactly in the nonzero degree-two eigenspace. Trigonometric support perturbations for sufficiently small \(\epsilon\) retain \(p>r\) and an embedded tube, so equality cases in the limiting Rayleigh quotient are genuinely approachable.

## Verification
The standalone `check.py` recomputes \(\int_\Sigma H^2dA\) using the two-angle tube parametrization, independently evaluates the one-dimensional curvature integral for several noncircular convex cores, checks the global curvature-deficit bound and volume normalization, and compares the second-order coefficient in degrees two through four. It uses the Python standard library. Execute `python check.py` from the extracted package. The sample program reports `DIRECT_SURFACE_INTEGRALS_AND_GLOBAL_RIGIDITY_PASSED`, `SHARP_SECOND_VARIATION_AND_MODE_TWO_PASSED`, and `CLIFFORD_PROFILE_AND_ALL_CHECKS_PASSED`. Numerical quadrature is a consistency test, not the proof of the universal assertions; steps 1–3 provide the analytic proof.

## Relationship to prior work
The all-tori Willmore inequality and the constrained isoperimetric problem are established subjects (Marques–Neves; Keller–Mondino–Rivière). Yu–Chen (arXiv:2003.13116, posted 2020-03-29) study the Clifford torus under prescribed isoperimetric ratio, with a different ambient class. Ertem Kaya (2021, DOI 10.35414/akufemubid.977234), particularly its Theorem 4.1, explicitly treats the **forward Willmore energy of tubular surfaces**; the tubular principal-curvature input is therefore not a new contribution. The comparison is at the level of implications: existing forward integrands make the present bound accessible by convexity, but the inspected sources do not give the claimed sharp fixed-\(S,V\) global classification, quantitative curvature remainder, or the exact fixed-constraint Fourier Hessian and degree-two spectral equality class. The 2018 Geometric Analysis Lectures project explicitly proposes studying Willmore on tubes over general plane curves but does not supply this exact constrained result. Priority beyond the inspected literature is uncertain.

## Limitations
The minimization is **only** over embedded constant-radius tubes around simple closed planar cores with the stated fixed \(S,V\). It is not a claim about all embedded genus-one surfaces, all variable-radius tubes, or nonplanar cores. The global curvature remainder is a proved positive coefficient, not asserted to be quantitatively optimal. The sharp Fourier coefficient is local near a circle within the fixed-perimeter convex support-function family. No noisy data or global shape-distance estimate is proved. Some older tube-specialized priority sources may not be indexed; no independent audit has been performed.

## References
1. T. Yu and J. Chen, *On the Uniqueness of Clifford Torus with Prescribed Isoperimetric Ratio*, arXiv:2003.13116 (first public version 2020-03-29), https://arxiv.org/abs/2003.13116.
2. F. Ertem Kaya, *Energies with Constant Mean Curvature of Tubular Surfaces by Bishop Frame*, *Afyon Kocatepe Univ. J. Sci. Eng.* 21 (2021), 1324–1329, DOI 10.35414/akufemubid.977234, https://dergipark.org.tr/en/download/article-file/1902879.
3. L. G. A. Keller, A. Mondino and T. Rivière, *Embedded surfaces of arbitrary genus minimizing the Willmore energy under isoperimetric constraint*, arXiv:1305.5470 (2013), https://arxiv.org/abs/1305.5470.
4. F. C. Marques and A. Neves, *Min-max theory and the Willmore conjecture*, *Ann. of Math.* 179 (2014), 683–782.
5. *Geometric Analysis Lectures: Project 1, The Willmore conjecture (theorem)*, 2018 course project, https://sites.ualberta.ca/~mathirl/IUSEP/IUSEP_2018/projects/woolgar_project1.pdf.
