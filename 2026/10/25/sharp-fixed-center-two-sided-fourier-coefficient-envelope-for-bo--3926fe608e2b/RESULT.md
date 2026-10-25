# Sharp fixed-center two-sided Fourier coefficient envelope for bounded harmonic disk maps

## Finding
Let \(f:\mathbb D\to\overline{\mathbb D}\) be any complex-valued harmonic map. Write its canonical expansion as
\[
f(re^{it})=a_0+\sum_{j\ge1}\bigl(a_jr^je^{ijt}+\overline{b_j}r^je^{-ijt}\bigr),\qquad 0\le r<1,
\]
and fix \(c=|a_0|\in[0,1]\). For every integer \(n\ge1\), the following is the exact best possible inequality:
\[
\boxed{|a_n|+|b_n|\le \mathcal B(c):=\inf_{\lambda\ge0}\left[\mathcal I(\lambda)-c\lambda\right]},
\qquad
\mathcal I(\lambda)=\frac1{2\pi}\int_0^{2\pi}\sqrt{\lambda^2+4\cos^2t}\,dt.
\]
The constant is independent of the coefficient index. It obeys \(\mathcal B(0)=4/\pi\), \(\mathcal B(1)=0\), and is strictly decreasing on \((0,1)\). For every \(0<c<1\), the minimizing \(\lambda=\lambda_c>0\) is the unique solution of
\[
c=\frac1{2\pi}\int_0^{2\pi}\frac{\lambda_c}{\sqrt{\lambda_c^2+4\cos^2t}}\,dt.
\]
At an interior center value, **all** equality traces, after rotating the value at the origin to the positive real axis, are precisely the angular translates of
\[
F_{c,n}(e^{it})=\frac{\lambda_c-2i\cos(nt)}{\sqrt{\lambda_c^2+4\cos^2(nt)}}.
\]
The equality functions are their Poisson extensions. At \(c=0\), every equality trace is a constant unit phase times \(\operatorname{sgn}(\cos(nt-\theta))\); at \(c=1\), only constants occur.

The envelope has the two sharp endpoint laws
\[
\boxed{\mathcal B(c)=2\sqrt{1-c}\,(1+o(1))\quad(c\uparrow1)},
\qquad
\boxed{\frac4\pi-\mathcal B(c)\sim\frac{\pi c^2}{2\log(1/c)}\quad(c\downarrow0)}.
\]
In particular the gain from conditioning at a small nonzero center has a logarithmically weakened quadratic order; near the maximum possible center it has a square-root order.

## Assumptions and scope
The unit disk is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\); the boundary circle carries normalized arclength \(dm(t)=dt/(2\pi)\). The maps need only have real and imaginary parts harmonic and satisfy \(|f(z)|\le1\) in the disk. No analytic, univalent, quasiregular, or orientation-preserving assumption is made. Bounded harmonic functions are Poisson extensions of \(L^\infty\) boundary traces \(F\), and the two-sided Fourier coefficients of those traces are the displayed \(a_n\) and \(\overline{b_n}\). The constraint fixes the *modulus* of the center, not a prescribed phase.

## Proof
**1. Boundary reduction and phase duality.** Let \(F\) denote the boundary trace; then \(|F|\le1\) almost everywhere and \(\int F\,dm=a_0\). Rotating \(f\) by a constant phase lets us assume \(a_0=c\ge0\). For every \(n\ge1\), the elementary duality of two complex absolute values gives
\[
|a_n|+|b_n|
=\sup_{\phi,\theta\in\mathbb R}\operatorname{Re}\int F(e^{it})\,2e^{i\phi}\cos(nt-\theta)\,dm(t).
\]
Indeed, independent unimodular phases multiplying the positive and negative Fourier coefficients reparametrize uniquely as a common phase and an angular displacement.

**2. The sharp upper envelope.** For any \(\lambda\ge0\), insert the real constant \(\lambda\) into the integrand, using \(\operatorname{Re}\int\lambda F\,dm=\lambda c\). Since \(|F|\le1\),
\[
\operatorname{Re}\int F\,2e^{i\phi}\cos(nt-\theta)\,dm
\le \int |\lambda+2e^{i\phi}\cos(nt-\theta)|\,dm-\lambda c.
\]
Pair the values of the cosine at \(u\) and \(-u\). Set \(A=\lambda^2+4u^2\) and \(B=4\lambda u\cos\phi\). Concavity of the square root yields
\[
\frac{\sqrt{A+B}+\sqrt{A-B}}2\le\sqrt A.
\]
The cosine distribution is symmetric, so the preceding integral is at most \(\mathcal I(\lambda)\), independently of \(n,\theta,\phi\). Taking the infimum over \(\lambda\) proves the inequality.

**3. Uniqueness of the dual parameter.** Differentiating under the integral for positive \(\lambda\) yields
\[
\mathcal I'(\lambda)=\int\frac{\lambda}{\sqrt{\lambda^2+4\cos^2t}}\,dm(t),\qquad
\mathcal I''(\lambda)=\int\frac{4\cos^2t}{(\lambda^2+4\cos^2t)^{3/2}}\,dm(t)>0.
\]
Moreover \(\mathcal I'(0+)=0\) and \(\mathcal I'(\infty)=1\). Thus for \(0<c<1\) there is exactly one minimizing positive \(\lambda_c\); the infimum for \(c=0\) is attained at zero. When \(c=1\), \(\mathcal I(\lambda)-\lambda\downarrow0\) as \(\lambda\to\infty\). The envelope is strictly decreasing because its derivative at interior points is \(-\lambda_c\).

**4. Simultaneous attainment and all equality functions.** For \(0<c<1\), put
\[
F(e^{it})=\frac{\lambda_c-2i\cos(nt-\theta)}{\sqrt{\lambda_c^2+4\cos^2(nt-\theta)}}.
\]
This trace is unimodular and its real mean is \(\mathcal I'(\lambda_c)=c\). Moreover
\[
\operatorname{Re}\int F\bigl(\lambda_c+2i\cos(nt-\theta)\bigr)\,dm=\mathcal I(\lambda_c),
\]
which gives equality in the sought bound by subtracting \(\lambda_c c\). The Poisson extension is admissible. Conversely, equality at positive \(\lambda_c\) requires equality in the paired square-root inequality, forcing \(\cos\phi=0\), because the strict-concavity defect vanishes only when \(\lambda_c\cos\phi=0\). Equality in the pointwise modulus bound then forces \(F\) to equal the displayed unimodular phase almost everywhere. Changing the sign of the imaginary phase is the same as translating \(\theta\) by \(\pi\). This classifies all equality cases. When \(c=0\), the \(\lambda=0\) modulus bound forces a unit-phase cosine sign. When \(c=1\), the harmonic maximum principle forces the constant map.

**5. Endpoint asymptotics.** The integral \(\mathcal I\) has the complete elliptic representation
\[
\mathcal I(\lambda)=\frac{2\sqrt{\lambda^2+4}}\pi E\!\left(\frac2{\sqrt{\lambda^2+4}}\right),\qquad
\mathcal I'(\lambda)=\frac{2\lambda}{\pi\sqrt{\lambda^2+4}}K\!\left(\frac2{\sqrt{\lambda^2+4}}\right),
\]
with \(E,K\) the complete elliptic integrals of the second and first kind, respectively, in modulus notation. As \(\lambda\to\infty\), expanding the square root under the integral gives
\[
\mathcal I(\lambda)=\lambda+\frac1\lambda+O(\lambda^{-3}),\qquad
\mathcal I'(\lambda)=1-\lambda^{-2}+O(\lambda^{-4}).
\]
It follows that \(\lambda_c\sim(1-c)^{-1/2}\) and \(\mathcal B(c)\sim2\sqrt{1-c}\). For small positive \(\lambda\), the standard elliptic logarithm \(K(k)=\log(4/\sqrt{1-k^2})+o(1)\) gives
\[
\mathcal I'(\lambda)\sim\frac\lambda\pi\log\frac8\lambda,
\quad \mathcal I(\lambda)-\mathcal I(0)\sim\frac{\lambda^2}{2\pi}\log\frac8\lambda.
\]
Consequently \(\lambda_c\sim\pi c/\log(1/c)\), and
\[
\mathcal I(0)-\mathcal B(c)
=\lambda_c c-\bigl(\mathcal I(\lambda_c)-\mathcal I(0)\bigr)
\sim\frac12\lambda_c c\sim\frac{\pi c^2}{2\log(1/c)}.
\]
The elliptic asymptotic used here is only the classical leading logarithm; it does not assume the desired coefficient bound.

## Verification
Run `python3 check_bound.py` in the same directory after installing NumPy and SciPy. The standalone script numerically integrates \(\mathcal I\) and its derivative, solves the stationarity equation, and independently Fourier-transforms the proposed unimodular boundary traces at indices \(1,3,7\) for center values \(0.03,0.2,0.5,0.9,0.99\). It also checks the center and the predicted sharp value, plus the near-one endpoint. Actual execution returned `VERIFY_OK extremal_Fourier_profiles=15 stationarity_cases=5 endpoint_checks=2`. These are finite consistency checks; Steps 1–5 provide the proof for all admissible maps, center values and indices.

## Relationship to prior work
The sharp unconditioned estimate \(|a_n|+|b_n|\le4/\pi\) was established in earlier harmonic-mapping coefficient literature, including the 2011 Liu–Liu–Zhu treatment (Lemma 2.1) and the 2012 Chen–Ponnusamy–Wang result. Chen–Huang–Jin–Li's September 2026 manuscript studies sharp harmonic Hardy coefficient constants across \(p\), recovering the unconditioned endpoint. These sources do not impose a nonzero prescribed center and thus do not supply the strict, complete fixed-center envelope or its equality family. Ahamed–Hossain (April 2026) studies a fixed-center harmonic Bohr majorant but applies separately valid unconditioned coefficient estimates; its displayed majorant radius is not an exact single-coefficient frontier. The published *Sharp square-root boundary law for center-conditioned harmonic Bohr radii* gives a global radius lower bound and its near-one asymptotic using Parseval, not the exact sharp one-frequency envelope here. The published *Sharp logarithmic stability of the harmonic Hardy coefficient extremizers* concerns proximity to the zero-center sign-cosine profile, not the fixed-center optimization. The independent boundary constraint and spectral objective are explicitly different in each comparison.

## Limitations
The statement optimizes **one** two-sided Fourier coefficient pair for each fixed index; distinct coefficients generally cannot attain their individual maxima simultaneously. In particular, the result does not determine the exact Bohr radius or the total coefficient majorant at any prescribed center. The new bound applies to all bounded complex harmonic maps and does not impose sense preservation or univalence. Although the stated comparisons identify no dominating prior theorem, historical priority is not asserted to have been exhaustively established, and no independent mathematical audit has been performed.

## References
1. S. Chen, M. Huang, L. Jin and Q. Li, *Sharp constant problems for harmonic mappings*, arXiv:2609.33159v1, publicly posted September 27, 2026, especially Section 1.2 and Theorem 1.3, https://arxiv.org/abs/2609.33159.
2. M. B. Ahamed and R. Hossain, *Bohr Radius and Landau-type Theorems for Harmonic Mappings with Boundary Functions in Lebesgue Spaces*, arXiv:2604.14217v1, publicly posted April 12, 2026, especially the fixed-center Bohr calculation, https://arxiv.org/abs/2604.14217.
3. M.-S. Liu, Z.-W. Liu and Y.-C. Zhu, *Landau's theorems for certain biharmonic mappings*, Acta Mathematica Sinica (Chinese Series) 54 (2011), 69–80, especially Lemma 2.1; accessible arXiv text https://arxiv.org/html/1511.04642v1.
4. S. Chen, S. Ponnusamy and X. Wang, *Integral means and coefficient estimates on planar harmonic mappings*, Annales Academiae Scientiarum Fennicae Mathematicae 37 (2012), 69–79, DOI: 10.5186/aasfm.2012.3707 (the \(4/\pi\) endpoint).
5. *Sharp square-root boundary law for center-conditioned harmonic Bohr radii* (2026), published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-square-root-boundary-law-for-center-conditioned-harmonic-b--4e234ffc1de0.
6. *Sharp logarithmic stability of the harmonic Hardy coefficient extremizers* (2026), published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-logarithmic-stability-of-the-harmonic-hardy-coefficient-ex--723bd47894d9.
