# Exact transverse crossings of the integer-parameter Hilbert beta curves

## Finding

For an integer \(m\ge1\), let
\[
(\mathcal H_m f)(z)=\int_0^1\frac{(1-t)^m f(t)}{(1-tz)^{m+1}}\,dt
\quad\text{on complex }H^2(\mathbb D).
\]
Write \(M_m(\xi)=\mathrm B(m+\tfrac12-i\xi,\tfrac12+i\xi)\). The known Fredholm essential spectrum is the image of this curve, completed at zero. The completed curve has **exactly \(\lfloor(m-1)/2\rfloor\) nonzero self-intersections**, all transverse double points. Each integer \(j\ge1\) with \(2j<m\) gives one crossing \(M_m(\xi_{m,j})=M_m(-\xi_{m,j})\), where \(\xi_{m,j}>0\) is the unique solution to
\[
\sum_{r=0}^{m-1}\arctan\frac{\xi_{m,j}}{r+\tfrac12}=j\pi.
\]
The crossing has sign \((-1)^j\) on the real axis; its magnitude is
\[
\frac{\pi}{m!\cosh(\pi\xi_{m,j})}\prod_{r=0}^{m-1}\sqrt{(r+\tfrac12)^2+\xi_{m,j}^2}.
\]
In particular, \(m=1,2\) have no nonzero crossings, the first appears at \(m=3\), and each subsequent odd integer increases the count by one.

## Assumptions and scope

Self-intersections refer to coincident values at distinct parameters of the curve \(\xi\in\mathbb R\), completed by the common limiting point zero. The theorem does not count zero, classify noninteger parameters, or determine the full operator spectrum.

## Proof

The completed beta-function Fredholm boundary for every real \(b>0\), and the Hilbert–Schmidt comparison with convolution on a half-line, are established in [The beta-curve Fredholm spectrum of generalized Hilbert operators on \(H^2\)](https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-the-beta-curve-fredholm-spectrum-of-generalized-hilbert-operator--1bea671ee6d5), Finding and Proof §§1–5. Its beta arguments are written in the opposite order, which is immaterial. Using the boundary as an input, we classify its nonzero singularities when \(b=m\) is a positive integer.

Put \(a_r=r+\tfrac12\). The gamma recurrence and reflection formula give
\[
M_m(\xi)=\frac{\pi}{m!\cosh(\pi\xi)}\prod_{r=0}^{m-1}(a_r-i\xi).
\]
For \(\xi\ge0\), let \(R_m(\xi)=|M_m(\xi)|\) and use the argument \(\theta_m(\xi)=-\sum_{r=0}^{m-1}\arctan(\xi/a_r)\). The derivative of \(\theta_m\) is strictly negative, and the angle decreases from zero toward \(-m\pi/2\), without attaining this endpoint. The Euler product for \(\cosh\) gives
\[
\frac{R_m(\xi)}{R_m(0)}=
\prod_{r=0}^{m-1}(1+\xi^2/a_r^2)^{-1/2}
\prod_{r=m}^\infty(1+\xi^2/a_r^2)^{-1}.
\]
Logarithmic differentiation on compact intervals is justified by the bound \(2\xi/a_r^2\) for the derivatives of the tail logarithms, so \(R_m'(\xi)<0\) for every \(\xi>0\). The curve has no zero at finite parameter and satisfies \(M_m(-\xi)=\overline{M_m(\xi)}\). Equal values at distinct finite parameters must therefore come from \(\xi>0\) and \(-\xi\), and their value must be real. This is exactly the condition \(\theta_m(\xi)=-j\pi\) for an integer \(1\le j<m/2\). The monotone phase gives each parameter once; monotone radii make the resulting values pairwise distinct. At a crossing the derivatives are \(M_m'(\xi)=(-1)^j(R_m'(\xi)+iR_m(\xi)\theta_m'(\xi))\) and \(M_m'(-\xi)=-\overline{M_m'(\xi)}\). Both the real and imaginary parts of the first vector are nonzero, so these vectors span distinct real tangent lines. This proves transversality and exhausts the nonzero intersections.

## Relation to prior work

Li–Pan–Zhou ([arXiv:2608.19660](https://arxiv.org/abs/2608.19660), Eq. (1.1), Theorem 1.1) and Bhuyan–Naik ([DOI:10.1108/AJMS-07-2024-0111](https://doi.org/10.1108/AJMS-07-2024-0111), Eqs. (1)–(2)) study this same operator. It also lies in the Hausdorff-matrix family of Bellavita et al. ([arXiv:2307.15334](https://arxiv.org/abs/2307.15334), §2): their matrix entries specialize under \(d\mu(t)=(1-t)^b\,dt\) to
\[
\binom{n+k}{n}\mathrm B(k+1,n+b+1)=
\frac{\Gamma(n+b+1)\Gamma(n+k+1)}{\Gamma(n+1)\Gamma(n+k+b+2)},
\]
the entries of \(\mathcal H_b\). These operator and norm references are not the source of the Fredholm beta boundary. That boundary and its half-line model are credited above; the standard scalar Wiener–Hopf winding index is a direct corollary of that model, not an additional originality claim. The contribution here is the global crossing classification: it distinguishes the geometry of the Fredholm boundary as the integer parameter increases, determines its nonzero transverse meeting points and excludes other nonzero intersections. The earlier boundary result gives the explicit special case \(b=1\), but does not analyze this complete crossing pattern.

## Verification

Steps above prove the all-integer statement without numerical approximations. The existing `CHECK.py` contains finite numerical checks of the reflection symmetry, phase, modulus and crossing locations (integer parameters up to 15 in the crossing test); it also checks some features of the known operator model. These are diagnostics, not a proof of the infinite-parameter theorem or its priority.
