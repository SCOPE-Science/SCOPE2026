# Sharp local spectral geometry at the half-density first-Hermite Gabor obstruction

## Finding

Let \(g(t)=t e^{-\pi t^2}\), let \(a>0\), and put \(b=1/(2a)\). Define the Zak transform and the nonnegative, two-channel Zak energy by
\[
 Z_a g(x,\omega)=\sum_{n\in\mathbb Z}g(x-an)e^{2\pi ian\omega},\qquad
 H_a(x,\omega)=a\left(|Z_a g(x,\omega)|^2+|Z_a g(x,\omega-b)|^2\right).
\]
The energy is periodic under \(x\mapsto x+a\) and \(\omega\mapsto\omega+1/a\). The two symmetry-forced zero points \((0,0)\) and \((0,b)\) on this torus are **nondegenerate quadratic minima for every** \(a>0\). At either point, with \(u=x\) and \(v=\omega-\omega_0\) interpreted as local real coordinates,
\[
 H_a(u,\omega_0+v)=X(a)u^2+Y(a)v^2+O_a\big((|u|+|v|)^4\big),
 \qquad \omega_0\in\{0,b\},
\]
where, writing
\[
 A_j(a)=\sum_{n\in\mathbb Z}(-1)^{jn}(1-2\pi a^2n^2)e^{-\pi a^2n^2},\quad
 B_j(a)=-2\pi a^2\sum_{n\in\mathbb Z}(-1)^{jn}n^2e^{-\pi a^2n^2}\quad (j=0,1),
\]
we have the exact positive curvatures
\[
 X(a)=a(A_0(a)^2+A_1(a)^2)>0,\qquad
 Y(a)=a(B_0(a)^2+B_1(a)^2)>0.
\]
They obey the **exact Fourier-duality law**
\[
 X(a)=Y\left(\frac1{2a}\right),\qquad
 Y(a)=X\left(\frac1{2a}\right).
\]
Thus \(X(1/\sqrt2)=Y(1/\sqrt2)\). The transverse curvatures become exponentially anisotropic at either extreme:
\[
 \begin{aligned}
 a\downarrow0:\quad&X(a)\sim \pi^2a^{-5}e^{-\pi/(2a^2)},\qquad Y(a)\sim a^{-1},\\
 a\to\infty:\quad&X(a)\sim2a,\qquad
 Y(a)\sim32\pi^2a^5e^{-2\pi a^2}.
 \end{aligned}
\]
In sufficiently small, fixed disjoint coordinate neighborhoods \(U_0,U_b\) of the two indicated points, each measured using ordinary \(dx\,d\omega\) area, one has, as \(\varepsilon\downarrow0\),
\[
 \operatorname{Area}\{(x,\omega)\in U_{\omega_0}:H_a(x,\omega)\le\varepsilon\}
 =\frac{\pi\varepsilon}{\sqrt{X(a)Y(a)}}+O_a(\varepsilon^2).
\]
The exact leading coefficient \(L(a)=\pi/\sqrt{X(a)Y(a)}\) therefore satisfies
\[
 L(a)\sim a^3e^{\pi/(4a^2)}\quad(a\downarrow0),\qquad
 L(a)\sim\frac{e^{\pi a^2}}{8a^3}\quad(a\to\infty).
\]
No assertion is made that these are the only zeros of \(H_a\) on the whole phase torus.

## Assumptions and scope

All parameters are real with \(a>0\) and \(b=1/(2a)\); the window is exactly the *unnormalized* first Hermite function \(g(t)=t e^{-\pi t^2}\). All infinite series defining the energy and its derivatives converge absolutely and locally uniformly with all derivatives. The two-channel energy is defined explicitly above, avoiding any convention-dependent normalization of a frame-operator fiber. The underlying rectangular lattice has density parameter \(ab=1/2\).

The statement describes the **local** nonnegative spectral multiplier at two forced zeros and its local sublevel sets. The limit \(\varepsilon\downarrow0\) is taken for each fixed \(a\). Asymptotics as \(a\to0\) or \(a\to\infty\) concern only the exact leading coefficient, not a jointly uniform two-parameter sublevel theorem.

## Proof

**1. Parity and the quadratic Taylor form.** Oddness of \(g\) and symmetry of the integers imply
\[
 Z_ag(-x,-\omega)=-Z_ag(x,\omega).
\]
Moreover \(Z_ag(x,\omega+1/a)=Z_ag(x,\omega)\). At \(x=0\), both \(\omega=0\) and \(\omega=b\) give zero, by pairing the terms with indices \(n\) and \(-n\). Since \(2b=1/a\), the two channels exchange their roles at these two points. At \((0,0)\), direct termwise differentiation gives
\[
 \partial_x Z_ag(0,-jb)=A_j(a),\qquad
 \partial_\omega Z_ag(0,-jb)=iB_j(a),\qquad j=0,1.
\]
Both displayed coefficients are real. Consequently, the cross term vanishes upon taking absolute squares:
\[
 H_a(u,v)=a\sum_{j=0}^{1}|A_j(a)u+iB_j(a)v|^2+O_a((|u|+|v|)^4).
\]
There is no cubic term: the transform is odd about the relevant torus points, so its Taylor series has only odd total degrees; taking squared moduli gives an even expansion. At \((0,b)\), exchanging the two channels gives the same expansion.

**2. Strict ellipticity.** Under the Fourier convention \(\widehat f(\xi)=\int f(t)e^{-2\pi it\xi}\,dt\),
\[
 \widehat g(\xi)=-i\xi e^{-\pi\xi^2},\qquad
 \widehat{g'}(\xi)=2\pi\xi^2e^{-\pi\xi^2}.
\]
Poisson summation thus gives
\[
 A_0(a)=\frac{2\pi}{a^3}\sum_{k\in\mathbb Z}k^2e^{-\pi k^2/a^2}>0.
\]
Also \(B_0(a)=-2\pi a^2\sum_n n^2e^{-\pi a^2n^2}<0\). Hence both \(X(a)\) and \(Y(a)\) are strictly positive for every \(a>0\).

**3. Exact Fourier duality.** The shifted Poisson formula yields
\[
 A_1(a)=\frac{2\pi}{a^3}\sum_{k\in\mathbb Z}(k+\tfrac12)^2e^{-\pi(k+1/2)^2/a^2}.
\]
Put \(c=1/(2a)\). Separating the even and odd indices in these two dual sums and comparing with the definitions of \(B_0(c),B_1(c)\) gives
\[
 A_0(a)=-\frac{B_0(c)+B_1(c)}{2a},\qquad
 A_1(a)=-\frac{B_0(c)-B_1(c)}{2a}.
\]
Thus \(A_0(a)^2+A_1(a)^2=(B_0(c)^2+B_1(c)^2)/(2a^2)\). Multiplication by \(a\) proves \(X(a)=Y(c)\); interchanging \(a\) and \(c\) proves its companion identity.

**4. The thin and wide limits.** As \(a\downarrow0\), the shifted dual Poisson series has the two dominant half-integer terms, giving
\[
 A_1(a)\sim \pi a^{-3}e^{-\pi/(4a^2)},\qquad A_0(a)=O(a^{-3}e^{-\pi/a^2}).
\]
Ordinary Gaussian Riemann sums, or the differentiated Jacobi identity, give
\[
 B_0(a)\sim-a^{-1},\qquad B_1(a)=o(a^{-1}).
\]
The stated small-\(a\) estimates follow. As \(a\to\infty\), the \(n=0\) terms of \(A_0,A_1\) both tend to one, while the \(n=\pm1\) terms dominate \(B_0,B_1\):
\[
 A_0(a)^2+A_1(a)^2\sim2,\quad
 B_0(a)\sim-4\pi a^2e^{-\pi a^2},\quad
 B_1(a)\sim+4\pi a^2e^{-\pi a^2}.
\]
This yields the wide-\(a\) asymptotics. Inserting them into \(L(a)=\pi/\sqrt{X(a)Y(a)}\) proves the two sharp exponential area-coefficient limits.

**5. Local sublevel area.** Positive definiteness of the quadratic form provides a neighborhood containing no other zero. In polar coordinates \((u,v)=r(\cos\theta,\sin\theta)\), the expansion takes the form \(H_a=r^2q_a(\theta)+O_a(r^4)\), with \(q_a(\theta)=X(a)\cos^2\theta+Y(a)\sin^2\theta\) uniformly bounded below by a positive constant. Hence the radial sublevel boundary satisfies \(r^2=\varepsilon/q_a(\theta)+O_a(\varepsilon^2)\), uniformly in angle. Integrating \(r^2/2\) and using
\[
 \frac12\int_0^{2\pi}\frac{d\theta}{X\cos^2\theta+Y\sin^2\theta}
 =\frac{\pi}{\sqrt{XY}}
\]
proves the local area law.

## Verification

The standalone `check.py` independently evaluates the two Zak channels and their derivative sums using 50-digit precision. It compares the computed local curvature with direct finite-difference quotients for six lattice shapes, verifies the two exact duality identities to stringent numerical precision, probes both exponential asymptotic regimes, and computes local sublevel areas by numerical radial integration at two thresholds. The recorded executable output is in `check_output.txt`. The proof above does **not** use finite numerical tests to establish the infinitely many parameter assertions.

## Relationship to prior work

Lyubarskii and Nes, *Gabor frames with rational density* (2011 preprint; 2013 journal), established the universal nonframe obstruction for odd windows at rectangular densities \((q-1)/q\), including \(1/2\), via a rank-deficient Zibulski–Zeevi matrix. That prior theorem supplies the structural reason for studying these forced zero points; the zero locations and nonframe phenomenon are **not** claimed as new.

Horst, Lemvig and Videbæk (2023 preprint; 2025 journal) analyze Zak-transform zero symmetries and higher-Hermite nonframe obstructions. Faulhuber and Petersen (2026) determine the complete first-Hermite Gabor frame set, a much broader qualitative result. The portions inspected do not supply the present exact local Hessian, its duality identity, the two extreme-lattice exponential curvature scales, or the local small-energy area law. In particular, this local result neither strengthens nor replaces the complete frame-set theorem.

The much earlier literature on von Neumann lattices and harmonic-oscillator Zak zeros, especially Boon–Zak–Zucker (1983), is relevant to priority. Its complete text was not accessible in this comparison. No claim of exhaustive novelty or independent publication priority is made.

## Limitations

The results quantify only the two specified symmetry-forced zeros. They do not identify all global zero points of the two-channel energy, prove a global small-sublevel-area asymptotic, give a quantitative perturbation law as the density \(ab\) moves away from \(1/2\), or establish frame bounds at other densities. The local sublevel expansion is not asserted uniformly as \(a\) approaches zero or infinity. Normalizing the window by a nonunit scalar multiplies the energy and both curvatures by its squared magnitude. The historical full-text access limitation noted above leaves a residual originality risk.

## References

1. Y. Lyubarskii and P. Gråberg Nes, *Gabor frames with rational density*, arXiv:1108.2684, first submitted 2011-08-12; *Applied and Computational Harmonic Analysis* 34 (2013), 488–494. https://arxiv.org/html/1108.2684v1
2. A. Horst, J. Lemvig and A. E. Videbæk, *On the non-frame property of Gabor systems with Hermite generators and the frame set conjecture*, arXiv:2311.01547, first submitted 2023-11-02; *Applied and Computational Harmonic Analysis* 76 (2025). https://arxiv.org/html/2311.01547v2
3. M. Faulhuber and P. Petersen, *The frame set of the first Hermite function*, arXiv:2609.02610, first submitted 2026-09-02. https://arxiv.org/html/2609.02610v1
4. M. Boon, J. Zak and I. J. Zucker, *Rational von Neumann lattices*, *Journal of Mathematical Physics* 24 (1983), 316–323, DOI:10.1063/1.525682. (Full text not inspected.)
