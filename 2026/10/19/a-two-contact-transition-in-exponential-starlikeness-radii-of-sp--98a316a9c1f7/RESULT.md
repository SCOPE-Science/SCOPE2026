# A two-contact transition in exponential starlikeness radii of spirallike functions

## Finding
Let \(\mathcal S_\alpha\) be the normalized \(\alpha\)-spirallike class, \(-\pi/2<\alpha<\pi/2\). Its sharp exponential-starlikeness radius is the largest \(R(\alpha)\) for which every \(f\in\mathcal S_\alpha\) has
\[
\left|\log\left(\frac{zf'(z)}{f(z)}\right)\right|<1\qquad(|z|<R(\alpha)).
\]
Here the logarithm is the analytic branch taking value zero at the origin. Put \(a=|\alpha|\),
\[
 H(s)=\cosh\sqrt{1-s^2},\quad
 \Phi_a(s)=H'(s)\cos(s+a)+H(s)\sin(s+a)-\sin a,
\]
for \(-1\le s\le1\), and define the exact transition
\[
 a_*=\arctan\frac{\sin1-\cos1}{\sin1+\cos1-1}
      =0.6679160965181599\ldots.
\]
For \(0<a<a_*\), there is a unique \(s_a\in(-1,0)\) with \(\Phi_a(s_a)=0\). Set \(s_0=0\). Then the sharp radius has the complete two-branch formula
\[
 R(\alpha)=
 \begin{cases}
 \displaystyle\sqrt{\frac{H(s_a)-\cos s_a}{H(s_a)+\cos(s_a+2a)}},&0\le a<a_*,\\[7pt]
 \displaystyle\frac{\sin(1/2)}{\cos(a-1/2)},&a_*\le a<\pi/2.
 \end{cases}
\]
In particular, \(R(0)=\tanh(1/2)\), \(R(a_*)=0.4862647618817629\ldots\), and \(R(a)\to1\) as \(a\uparrow\pi/2\). For \(\alpha>0\), the sharp boundary contact in logarithmic target coordinates has *two* points \(w=\pm\sqrt{1-s_a^2}+is_a\) for \(0\le a<a_*\), and only \(w=-i\) for \(a\ge a_*\). For negative angles these contacts are reflected in the real axis. The radius is continuously differentiable in \(a\) at \(a_*\), but is not twice differentiable there. Moreover,
\[
 R(a)=\tanh(1/2)+\frac{e(e-1)(3-e)}{2(e+1)^2}a^2+O(a^4)\qquad(a\to0).
\]

## Assumptions and scope
Functions are holomorphic on the open unit disk \(\mathbb D\), normalized by \(f(0)=0\), \(f'(0)=1\), and satisfy \(\operatorname{Re}(e^{i\alpha}zf'(z)/f(z))>0\). The class is invariant under rotation of the independent variable; reflection conjugates \(\alpha\) and \(-\alpha\). The exponential target is \(\exp(\mathbb D)\); it is not the half-plane, parabola, or Bernoulli lemniscate. A radius is universal over the whole class, and boundary equality means an extremal at \(|z|=R\), whereas the asserted strict inequality is for \(|z|<R\). The definition \(H(\pm1)=1\) uses continuous/analytic extension and \(H'(\pm1)=\mp1\).

## Proof
**1. Exact disk model.** Put \(p=zf'/f\). Rotating the right half-plane gives the standard Schwarz representation
\[
 p(z)=M_\alpha(\omega(z)),\qquad
 M_\alpha(\zeta)=1+\frac{(1+e^{-2i\alpha})\zeta}{1-\zeta},
\]
where \(\omega:\mathbb D\to\mathbb D\), \(\omega(0)=0\). By Schwarz's lemma \(|\omega(z)|\le|z|\). Conversely each such \(\omega\) determines a normalized analytic \(f\) through \(zf'/f=p\). The target \(E=\exp(\mathbb D)\) has a simple Jordan boundary \(\{e^w:|w|=1\}\) because exponential is one-to-one on the closed unit disk. As \(M_\alpha(0)=1\in E\), the largest centered input disk mapped inside \(E\) has radius
\[
 R(\alpha)=\inf_{|w|=1}\left|M_\alpha^{-1}(e^w)\right|
 =\inf_{|w|=1}\left|\frac{e^w-1}{e^w+e^{-2i\alpha}}\right|.
\]
Points at which the displayed inverse denominator is zero are assigned modulus \(+\infty\); they cannot minimize. This boundary formula can also be viewed as an application of a general sharp subordination-radius principle, and is not itself a new principle.

**2. One-variable reduction.** For \(\alpha=a\ge0\), write \(w=\pm\sqrt{1-s^2}+is\) with \(-1\le s\le1\). The half-angle identities imply that either sign has the same squared inverse modulus,
\[
 F_a(s)=\frac{H(s)-\cos s}{H(s)+\cos(s+2a)}.
\]
For interior points with positive denominator, direct differentiation gives
\[
 \frac{d}{ds}F_a(s)=\frac{2\cos a}{[H(s)+\cos(s+2a)]^2}\Phi_a(s).
\]
The denominator is nonnegative everywhere and can vanish only at \(s=1\) and \(a=(\pi-1)/2\), where \(F_a=+\infty\), never an extremum. The key strictly positive derivative identity is
\[
 \Phi_a'(s)=\bigl(H''(s)+H(s)\bigr)\cos(s+a),\quad
 H''(s)+H(s)=\frac{v\cosh v-\sinh v}{v^3}>0,
 \quad v=\sqrt{1-s^2},
\]
with continuous endpoint limit \(1/3\). Positivity follows by differentiating \(v\cosh v-\sinh v\), which starts at zero and has derivative \(v\sinh v>0\).

**3. Unique minimizer and transition.** For \(-1\le s\le0\), \(\cos(s+a)>0\), so \(\Phi_a\) is strictly increasing. Its endpoint values are
\[
 \Phi_a(0)=(\cosh1-1)\sin a,\qquad
 \Phi_a(-1)=B\sin a-A\cos a,
\]
where \(A=\sin1-\cos1>0\) and \(B=\sin1+\cos1-1>0\). Thus there is one interior root on \((-1,0)\) exactly when \(0<a<a_*\); at \(a=0\) the unique root is \(s=0\), and for \(a\ge a_*\), \(\Phi_a\ge0\) on \([-1,0]\). On \([0,1]\), the derivative \(\Phi_a'\) changes sign at most once from positive to negative. Therefore \(\Phi_a\) has its minimum at an endpoint. Both endpoint values are nonnegative and, for \(0<a<\pi/2\), strictly positive:
\[
 \Phi_a(0)=(\cosh1-1)\sin a>0,\qquad
 \Phi_a(1)=A\cos a+B\sin a>0.
\]
For \(a=0\), \(\Phi_0(0)=0\) and \(\Phi_0(s)>0\) for \(s>0\). Hence the global minimum of \(F_a\) occurs exactly at \(s_a\) for \(a<a_*\), and exactly at \(s=-1\) for \(a\ge a_*\). Substitution at \(s=-1\) yields
\[
 F_a(-1)=\frac{1-\cos1}{1+\cos(2a-1)}
 =\frac{\sin^2(1/2)}{\cos^2(a-1/2)},
\]
which proves the stated formula and uniqueness of the imaginary coordinates of all target contacts. The two signs for real \(w\) merge only at \(s=-1\).

**4. Extremals and sharpness.** For every minimizing boundary point \(w\), let
\[
 \lambda=\frac{1}{R(\alpha)}\,
 \frac{e^w-1}{e^w+e^{-2i\alpha}},\qquad |\lambda|=1.
\]
Then
\[
 f_\lambda(z)=z(1-\lambda z)^{-(1+e^{-2i\alpha})}
\]
is a normalized \(\alpha\)-spirallike function, satisfies \(zf_\lambda'/f_\lambda=M_\alpha(\lambda z)\), and meets \(\partial E\) at \(z=R(\alpha)\). No larger universal radius is possible. Conversely, equality at an interior-domain point \(|z|=R(\alpha)\) forces \(|\omega(z)|=|z|\) by the boundary-distance minimum; Schwarz's equality case forces \(\omega(\zeta)=\lambda\zeta\), giving precisely these extremals. This supplies all boundary equality cases, up to rotation.

**5. Regularity and small-angle law.** At \(a_*\), \(\Phi_{a_*}(-1)=0\), \(\Phi_s(-1,a_*)=\frac13\cos(a_*-1)>0\), and \(\Phi_a(-1,a_*)=B\cos a_*+A\sin a_*>0\). Thus the interior critical point reaches the endpoint transversely. Writing \(m(a)=R(a)^2\), its one-sided second derivatives satisfy
\[
 m''(a_*+)-m''(a_*-)=
 \frac{F_{as}(-1,a_*)^2}{F_{ss}(-1,a_*)}>0,
\]
while the first derivatives agree (because \(F_s(-1,a_*)=0\)). Hence \(R\) is \(C^1\) but not \(C^2\) there. Finally implicit differentiation at the nondegenerate minimizer at \(a=0\) gives
\[
 s_a=-\frac{(e-1)^2}{2}a+O(a^3),
\]
and substitution into \(F_a(s_a)\), followed by a square root, yields the displayed even expansion of \(R(a)\).

## Verification
The file `CHECK.py` is a standalone Python-standard-library numerical cross-check. It verifies the exact endpoint/transition constants, solves the unique stationary equation by bisection, independently scans the complex boundary parametrization with 36,000 points per angle, compares a 4,001-point real grid against the proposed minimum, and checks the quadratic small-angle term. Execute `python CHECK.py`. These grids and floating-point calculations corroborate the identities but do not establish the continuum inequalities; those are proved analytically above.

## Relationship to prior work
Arul and Ravichandran introduced a recent study of sharp *parabolic* and *lemniscate* radii in the same \(\alpha\)-spirallike source class (arXiv:2610.06175, initially posted 2026-10-05). Palanisamy and Ravichandran (arXiv:2610.12006, initially posted 2026-10-08) provide a general boundary-minimum subordination-radius principle; the boundary-minimum representation in Step 1 is consistent with that prior result and is not claimed as an independent contribution. The claimed contribution is the explicit evaluation for the exponential target, the unique angle threshold, complete contact geometry, the non-\(C^2\) transition, and the small-angle law. The original papers' full PDF text was not accessible for a complete section-by-section comparison; this historical-priority risk remains, especially for unpublished examples of the general theorem. The 2026 work of Kazımoğlu et al. concerns exponential starlikeness radii of specific \(q\)-special functions rather than the universal \(\alpha\)-spirallike class.

## Limitations
No assertion is made about parabolic, lemniscate, or other target domains; no claim is made that the abstract minimum-over-boundary principle is new. The results are universal over normalized holomorphic \(\alpha\)-spirallike functions with \(|\alpha|<\pi/2\). Values at \(|\alpha|=\pi/2\) are limiting values, not part of the class theorem. Target contacts refer to \(\log(zf'/f)\) at the first radius, not multiple zeros of \(f\). Complete full-text historical priority has not been established and no independent validation was performed.

## References
1. L. Arul and V. Ravichandran, *Radii of Starlikeness of Spirallike Functions*, arXiv:2610.06175 (first posted 2026-10-05), https://arxiv.org/abs/2610.06175.
2. P. Palanisamy and V. Ravichandran, *A Unified Approach to Sharp Subordination Radii*, arXiv:2610.12006 (first posted 2026-10-08), https://arxiv.org/abs/2610.12006.
3. S. Kazımoğlu, E. Deniz, L.-I. Cotîrlă and D. Breaz, *Exponential radii of starlikeness and convexity of q-special functions*, Journal of Inequalities and Applications **2026**, article 74 (2026), DOI:10.1186/s13660-026-03480-1.
