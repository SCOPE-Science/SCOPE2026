# Fifth-harmonic rigidity and a quantitative area gap for finite-Fourier bodies of constant width

## Finding
Let \(K\subset\mathbb R^2\) be any planar convex body of constant width \(w>0\) whose support function, relative to any origin, is a real trigonometric polynomial of degree at most five. Write its fifth Fourier coefficients as \(c_5,d_5\). Then
\[
\boxed{\operatorname{area}(K)\ \ge\ \frac{15\pi w^2}{64}+6\pi(c_5^2+d_5^2).}
\]
The first term is the **sharp minimum** in this full class, without an assumed reflection symmetry or restriction to real cosine coefficients. Equality in the **sharp minimum-area assertion** holds precisely when, up to a translation and rotation, the support function is
\[
\boxed{h_K(\theta)=\frac w2+\frac{w}{16}\cos(3\theta).}
\]
The displayed coefficient \(6\pi\) is an explicit uniform stability coefficient, **not asserted to be optimal**. In particular, permitting an arbitrary fifth-harmonic phase cannot improve the optimal area of the pure third-harmonic body.

## Assumptions and scope
The support function is \(h_K(\theta)=\max_{x\in K}x\cdot(\cos\theta,\sin\theta)\). Constant width means \(h_K(\theta)+h_K(\theta+\pi)=w\) for every real \(\theta\). A real trigonometric polynomial of degree at most five has the unique decomposition
\[
h_K(\theta)=\frac w2+p\cos\theta+q\sin\theta+a\cos3\theta+b\sin3\theta+c\cos5\theta+d\sin5\theta.
\]
Here \(p,q,a,b,c,d\in\mathbb R\); the cosine/sine phases of the third and fifth modes are completely independent. The translation terms \(p,q\) do not affect the curvature radius or area. The theorem covers convex bodies with some vanishing curvature radii, by the non-strict planar support criterion. The conclusion does not apply to bodies with seventh or higher Fourier modes.

## Proof
Put \(r=w/2\), \(\eta_3=\sqrt{a^2+b^2}\) and \(\eta_5=\sqrt{c^2+d^2}\). The classical planar support criterion asserts that a twice-differentiable periodic function is the support function of a convex body exactly when its curvature-radius function \(\rho=h+h''\) is nonnegative. Here
\[
\rho(\theta)=r+g(\theta),\quad
g(\theta)=-8(a\cos3\theta+b\sin3\theta)-24(c\cos5\theta+d\sin5\theta).
\]
Define \(R=8\eta_3\) and \(S=24\eta_5\). As \(g(\theta+\pi)=-g(\theta)\), nonnegative curvature is equivalent to \(\|g\|_{\infty}\le r\), where the norm is the maximum absolute value over all real \(\theta\).

We establish the key **phase-independent spectral inequality**
\[
\boxed{\|R\cos3\theta+S\cos(5\theta+\phi)\|_{\infty}^2\ge R^2+\tfrac12S^2}
\]
for every \(R,S\ge0\) and every phase \(\phi\). If \(R=0\), the assertion is immediate. Otherwise, rotate the angle to make the third-mode term \(R\cos3\theta\); this changes only the phase \(\phi\) of the fifth mode. Evaluate the sum at the six angles \(\theta=k\pi/3\). After multiplication by \((-1)^k\), the resulting values are
\[
R+S\cos(2\pi k/3+\phi).
\]
Among three equally spaced angles, at least one cosine is at least \(1/2\). Consequently, \(\|g\|_{\infty}\ge R+S/2\). The reverse triangle inequality separately gives \(\|g\|_{\infty}\ge S-R\). For \(S\le4R\),
\[
(R+S/2)^2-(R^2+S^2/2)=S(R-S/4)\ge0;
\]
for \(S\ge4R\),
\[
(S-R)^2-(R^2+S^2/2)=S(S/2-2R)\ge0.
\]
These inequalities prove the asserted spectral estimate for all phases. Thus convexity entails
\[
\boxed{R^2+\tfrac12S^2\le r^2.}
\]

The standard support-function area identity and Fourier orthogonality give
\[
\begin{aligned}
\operatorname{area}(K)&=\frac12\int_0^{2\pi}\bigl(h_K(\theta)^2-h_K'(\theta)^2\bigr)\,d\theta\\
&=\pi r^2-4\pi(a^2+b^2)-12\pi(c^2+d^2)\\
&=\pi r^2-\frac\pi{16}(R^2+S^2/3).
\end{aligned}
\]
As \(R^2+S^2/3\le r^2-S^2/6\),
\[
\operatorname{area}(K)\ge\frac{15\pi r^2}{16}+\frac{\pi S^2}{96}
=\frac{15\pi w^2}{64}+6\pi(c^2+d^2).
\]
If the area attains the sharp baseline \(15\pi w^2/64\), the positive fifth-amplitude gap forces \(S=0\), and the area identity then forces \(R=r\); conversely, these conditions attain the baseline. In this case \(\rho(\theta)=r+r\cos(3\theta-\alpha)\ge0\) for a suitable phase \(\alpha\), so every stated equality support function is indeed convex and has constant width \(w\). The terms \(p,q\) correspond precisely to translations, and a phase change is a rotation. This proves existence, sharpness and the exhaustive equality classification.

## Verification
The standalone standard-library script `verification/check.py` performs 1,682 deterministic checks: exact rational verification of the two algebraic branches, phase-sampling tests, exact extremal identities for three rational widths, convex curvature evaluations, and independent trapezoidal integration of random admissible Fourier supports. The discrete trapezoidal area computation is independently compared with the analytical Fourier-area formula. These finite tests do not establish any universal bound; the preceding proof does.

## Relationship to prior work
The 2026 work of Falcó and Myroshnychenko determines minimum-area constant-width bodies under prescribed finite-group symmetries. The present problem instead imposes a **Fourier bandlimit** and allows independent phases, so its optimizer and proof are not direct consequences of that symmetry classification.

Most importantly, Bayen and Henrion (2010 preprint; 2012 journal publication), §3.1.4, **already numerically observed** that the minimum of their fifth-degree, *real-coefficient cosine-only* example occurs with zero fifth coefficient and an extremal third coefficient. That numerical observation, and the pure third-mode area formula, are not claimed as new. What is proved here is the unrestricted four-real-coefficient theorem, the rigorous equality classification, and the explicit uniform fifth-amplitude gap. The accessible source passage specifies a numerical observation rather than a theorem; the full manuscript could not be accessed in this review, so older-priority uncertainty remains.

A published result on the first two dihedrally admissible harmonics uses frequencies \(n\) and \(3n\), not the independent frequencies three and five, and actually finds that its higher harmonic can improve the optimal area. Neither that result nor the classical area/curvature identities implies the present sampling inequality. Results on general support-function Fourier energies, including Hurwitz-type inequalities, supply background but not this sharp degree-five extremal claim.

## Limitations
This is a theorem only for finite Fourier support through degree five; no all-degree Blaschke–Lebesgue improvement is claimed. The uniform gap coefficient is not known here to be optimal. The earlier numerical fifth-degree example means that the optimizer shape itself had been anticipated; historical priority of equivalent analytic inequalities has not been exhaustively resolved. Independent mathematical audit has not been performed.

## References
1. J. Falcó and S. Myroshnychenko, *Area Minimization Among Group-Invariant Planar Convex Bodies of Constant Width*, arXiv:2608.05125 (first publicly posted 2026-08-05), https://arxiv.org/abs/2608.05125.
2. T. Bayen and D. Henrion, *Semidefinite programming for optimizing convex bodies under width constraints*, manuscript dated 2010; *Optimization Methods & Software* **27** (2012), 1073–1099, §3.1.4, https://doi.org/10.1080/10556788.2010.547580.
3. *A note on Hurwitz's inequality*, *Journal of Mathematical Analysis and Applications* (2017), §5 on constant-width support Fourier spectra, https://doi.org/10.1016/j.jmaa.2017.09.017.
4. *Sharp two-harmonic area minimum for dihedrally invariant constant-width bodies* (published research record, 2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-two-harmonic-area-minimum-for-dihedrally-invariant-constan--0094d4f2c8a9.
