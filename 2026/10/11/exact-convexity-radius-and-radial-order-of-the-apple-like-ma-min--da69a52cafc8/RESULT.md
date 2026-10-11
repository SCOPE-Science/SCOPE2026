# Exact convexity radius and radial order of the apple-like Ma–Minda starlike class

## Finding
Put \(\phi(w)=e^w\sqrt{1+w}\) (principal square root). Let \(\mathcal S^*_{\rm AP}\) be the class of normalized analytic functions \(f\) on \(\mathbb D\) with
\[
\frac{zf'(z)}{f(z)}=\phi(\omega(z)),\qquad \omega:\mathbb D\to\mathbb D\ \text{analytic},\ \omega(0)=0.
\]
Define
\[
H(r)=e^{-r}\sqrt{1-r}-r\left(1+\frac1{2(1-r)}\right).
\]
There is a unique \(R\in(1/3,17/50)\) such that \(H(R)=0\); numerical evaluation gives \(R=0.33387693225135744484210636081305\ldots\). The exact sharp radial order is, for every \(0\le r\le R\),
\[
\boxed{\ \inf_{f\in\mathcal S^*_{\rm AP}}\min_{|z|=r}\operatorname{Re}\left(1+\frac{zf''(z)}{f'(z)}\right)=H(r)\ }.
\]
Thus \(R\) is the sharp universal radius of *classical convexity* for the apple-like starlike class. Equality at every allowed radius is attained by the same canonical function
\[
f_*(z)=z\exp\left(\int_0^z\frac{\phi(t)-1}{t}\,dt\right)
\]
at the negative real point \(z=-r\).

## Assumptions and scope
The disk is \(\mathbb D=\{z\in\mathbb C:|z|<1\}\). At the origin all quotients are interpreted by analytic continuation. The target \(\phi\) is analytic on \(\mathbb D\). The Schwarz function may be any analytic disk self-map fixing zero; no restriction to real coefficients is imposed. The convexity test is the classical condition \(\operatorname{Re}(1+zf''/f')>0\). The claimed radial equality is only asserted through the sharp radius \(R\), not beyond it.

The class consists of univalent functions: indeed \(\operatorname{Re}\phi(w)>0\) on \(\mathbb D\), as established in the proof, hence every \(f\) is starlike and has no derivative zeros away from the origin.

## Proof
**1. Positivity of the target and the normalization.** Since
\[
\log\phi(w)=w+\tfrac12\log(1+w),
\]
on the boundary \(w=e^{i\theta}\), for \(-\pi<\theta<\pi\), its imaginary part is \(\sin\theta+\theta/4\). On the upper semicircle this attains its maximum at \(\theta_*=\arccos(-1/4)<2\) and the maximum is
\[
\frac{\sqrt{15}}4+\frac{\theta_*}4<\frac32<\frac\pi2.
\]
The lower semicircle gives the negative. By the harmonic maximum principle, the argument of \(\phi\) stays strictly between \(-\pi/2\) and \(\pi/2\) throughout \(\mathbb D\). Thus \(\operatorname{Re}\phi>0\), and every normalized solution is starlike and univalent.

**2. A radial lower bound for the target.** Write \(\phi(w)=\sum_{n\ge0}a_n w^n\). Its differential equation
\[
(1+w)\phi'(w)=(\tfrac32+w)\phi(w)
\]
gives \(a_0=1\), \(a_1=3/2\) and
\[
(n+1)a_{n+1}=(\tfrac32-n)a_n+a_{n-1}\qquad(n\ge1).
\]
In particular \(a_2=7/8\), \(a_3=17/48\), \(a_4=11/128\), \(a_5=107/3840>0\), \(a_6=-89/46080<0\). Induction in the recurrence yields \(a_n>0\) for odd \(n\ge5\) and \(a_n<0\) for even \(n\ge6\). All these tail contributions to
\(\operatorname{Re}\phi(se^{i\theta})-\phi(-s)\) are nonnegative, because \(\cos(n\theta)-(-1)^n\) is nonnegative for odd \(n\) and nonpositive for even \(n\). The same is true at \(n=3\). For even \(n\),
\[
1-\cos(n\theta)\le n^2(1+\cos\theta)
\]
(by \(|\sin(mu)|\le m|\sin u|\) and \(n=2m\)). Consequently,
\[
\operatorname{Re}\phi(se^{i\theta})-\phi(-s)
\ge s(1+\cos\theta)\left(\frac32-\frac72s-\frac{11}{8}s^3\right)\ge0
\quad(0\le s\le17/50).
\]
The last parenthesis is decreasing and strictly positive at \(17/50\). Hence \(\operatorname{Re}\phi(w)\ge\phi(-|w|)\) throughout this smaller disk, sharply on its negative radius.

**3. Schwarz–Pick controls the logarithmic derivative.** For \(z\ne0\), put \(r=|z|\), \(w=\omega(z)\), and \(s=|w|\le r\). The function \(g(z)=\omega(z)/z\) extends analytically and satisfies \(|g|\le1\). Schwarz–Pick gives
\[
|z\omega'(z)-w|=|z^2g'(z)|\le\frac{r^2-s^2}{1-r^2},
\qquad
|z\omega'(z)|\le m_r(s):=s+\frac{r^2-s^2}{1-r^2}.
\]
Since \(\phi'/\phi=1+1/[2(1+w)]\),
\[
1+\frac{zf''(z)}{f'(z)}
=\phi(w)+z\omega'(z)\left(1+\frac1{2(1+w)}\right).
\]
For \(s\le17/50\), set \(L(s)=1+1/[2(1-s)]\). The preceding bounds imply
\[
\operatorname{Re}\left(1+\frac{zf''}{f'}\right)
\ge \phi(-s)-m_r(s)L(s)=:K_r(s).
\]
For \(0\le s\le r\le17/50\), \(m_r'(s)=1-2s/(1-r^2)>0\); also \(\phi'(-s)>0\), \(m_r(s)\ge0\), \(L(s)>0\) and \(L'(s)>0\). Therefore \(K_r'(s)<0\), so
\[
K_r(s)\ge K_r(r)=\phi(-r)-rL(r)=H(r).
\]
At \(z=0\) this conclusion holds by continuity with value \(1=H(0)\).

**4. Exact radius and sharpness.** The function \(H\) is strictly decreasing for \(0<r<1\): \(\phi(-r)\) decreases and \(rL(r)\) increases. For an exact root bracket, the alternating exponential expansion and rational square-root comparisons give
\[
e^{-1/3}>58/81,\quad\sqrt{2/3}>102/125,
\quad H(1/3)>\frac{13}{13500}>0.
\]
Also \(e^{-17/50}<1-17/50+(17/50)^2/2\), \(\sqrt{33/50}<41/50\), whence
\[
H(17/50)<-\frac{74083}{8250000}<0.
\]
Thus there is a unique root \(R\in(1/3,17/50)\). For \(r\le R\), the bound above is sharp: choose \(\omega(z)=z\), which gives \(f_*\), and evaluate at \(z=-r\), where \(1+zf_*''/f_*'=H(r)\). For any \(s>R\) close enough to \(R\), the same evaluation is negative, so the common convexity radius cannot exceed \(R\). This establishes both the full stated radial identity and sharp radius.

## Verification
The accompanying standard-library Python file `verify_apple_convexity.py` independently checks the first 120 exact rational Taylor coefficients and their signs; the rational positivity brackets and derivatives; a 62-digit decimal bisection for the root; and 5,000 seeded Schwarz–Blaschke numerical spot checks of the radial inequality. Run `python3 verify_apple_convexity.py`. The exact analytic arguments above, not a finite numerical sweep, establish the theorem for all Schwarz functions and all allowed radii.

## Relationship to prior work
Sana, Saliu, and Riaz introduced the apple-like Ma–Minda starlike/convex classes and proved coefficient, Hankel, logarithmic-coefficient, and standard growth/distortion theorems. Those statements do not give the sharp *classical convexity radius of the starlike class* or its full radial lower order. Das and Sarkar study inverse logarithmic coefficients and determinant functionals for the same starlike target; their announced statements concern different functionals. Their companion paper treats the *apple-like convex class*, not the radius at which every member of the apple-like **starlike** class becomes classically convex. General radius theorems for other Ma–Minda target functions do not directly imply the exact target-specific sharpness and radial phase inequality here.

## Limitations
The theorem concerns \(0\le r\le R\) and classical convexity, not a global convexity assertion on the full unit disk. The displayed decimal is explanatory; \(H(R)=0\) defines the exact value. No claim is made about higher-order coefficient functionals or the corresponding apple-like convex class. The complete manuscript of the directly related June 2026 starlike coefficient preprint was not available for full-text comparison; an equivalent uninspected statement cannot be excluded. Independent external verification has not been carried out.

## References
1. A. Sana, A. Saliu, S. Riaz, *Coefficient Inequalities Related With Apple-Like Functions*, Journal of Function Spaces (first published 12 May 2026), DOI: 10.1155/jofs/5570573. https://doi.org/10.1155/jofs/5570573
2. P. Das, N. Sarkar, *Sharp coefficient Estimates for the class \(\mathcal S^*_{\mathcal{AP}}\)*, arXiv:2606.15488v1 (13 June 2026). https://arxiv.org/abs/2606.15488
3. P. Das, N. Sarkar, *Inverse Logarithmic Coefficients and Associated Sharp Estimates for the Apple-Like Convex Subclass \(\mathcal C_{\mathcal{AP}}\)*, arXiv:2606.15780v1 (14 June 2026). https://arxiv.org/abs/2606.15780
4. N. E. Cho et al., *Differential subordination and radius estimates for starlike functions associated with the Booth lemniscate*, Turkish Journal of Mathematics 42 (2018), 1380–1399, DOI: 10.3906/mat-1706-49. https://doi.org/10.3906/mat-1706-49
