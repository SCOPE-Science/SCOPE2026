# Sharp two-level Wigner annulus concentration and its coherent transition

## Finding

Let \(h_0(x)=2^{1/4}e^{-\pi x^2}\) and \(h_1(x)=2\sqrt\pi\,x h_0(x)\). For arbitrary \(0<s<t<\infty\), let
\[
\Omega_{s,t}=\{(x,\xi)\in\mathbb R^2:s<4\pi(x^2+\xi^2)<t\}.
\]
Among all \(L^2\)-normalized functions \(f\in\operatorname{span}_{\mathbb C}\{h_0,h_1\}\), the exact sharp squared local Wigner norm \(\int_{\Omega_{s,t}}|W_f|^2\) and **all** extremizing populations are as follows. Define
\[
U=s e^{-s}-t e^{-t},\qquad
V=s(2-s)e^{-s}-t(2-t)e^{-t},\qquad C=e^{-s}-e^{-t}.
\]
Writing \(f=a h_0+c h_1\) with \(|a|^2+|c|^2=1\), its first-excited-level population \(b=|c|^2\in[0,1]\) has local concentration
\[
\mathcal E_{s,t}(b)=C+4Ub-(2U+V)b^2.
\]
There is precisely one extremizing population, given by
\[
b_*(s,t)=\begin{cases}
0,&U\le0,\\
1,&U>0,\ V\le0,\\
\displaystyle\frac{2U}{2U+V},&U>0,\ V>0.
\end{cases}
\]
The maximum is \(\mathcal E_{s,t}(b_*)\). In the intermediate regime \(U,V>0\) every relative phase is permitted, and coherent superpositions strictly outperform both unmixed Hermite states. The exact advantage over the better of these two states is
\[
\boxed{\frac{\min\{4U^2,V^2\}}{2U+V}>0.}
\]
In the thin-shell limit \(t=s+\delta\), \(\delta\downarrow0\), the optimizing population converges to
\[
\lim_{\delta\downarrow0}b_*(s,s+\delta)=
\begin{cases}
0,&0<s\le1,\\
\displaystyle\frac{2(s-1)}{-s^2+6s-4},&1<s<2+\sqrt2,\\
1,&s\ge2+\sqrt2.
\end{cases}
\]
Thus two exact dimensionless radii mark the transition from a pure vacuum to a coherent mixture and then to a pure first-excited oscillator mode.

## Assumptions and scope

We use the Wigner normalization
\[
W_f(x,\xi)=\int_{\mathbb R} f(x+y/2)\,\overline{f(x-y/2)}e^{-2\pi i\xi y}\,dy.
\]
The phase-space Lebesgue measure is \(dx\,d\xi\). The local functional is the **square** of the \(L^2\)-norm of \(W_f\), not its signed integral. The states are restricted to the first two normalized Hermite levels at the origin; no translations, dilations or higher Hermite modes are optimized. Both annular bounds are strictly positive and finite. The area of \(\Omega_{s,t}\) equals \((t-s)/4\).

## Proof

**Gaussian cross-Wigner identities.** The Gaussian Fourier transform
\[
\int_{\mathbb R}e^{-\pi y^2/2-2\pi i\xi y}\,dy=\sqrt2\,e^{-2\pi\xi^2}
\]
and its first derivative in \(\xi\), substituted directly into the definition, give, for \(r^2=x^2+\xi^2\),
\[
W_{h_0}=2e^{-2\pi r^2},\quad
W_{h_1}=2(4\pi r^2-1)e^{-2\pi r^2},\quad
W(h_0,h_1)=4\sqrt\pi(x+i\xi)e^{-2\pi r^2}.
\]
The last expression uses \(W(f,g)=\int f(x+y/2)\overline{g(x-y/2)}e^{-2\pi i\xi y}\,dy\); the other cross term is its complex conjugate. Orthonormality of \(h_0,h_1\) gives \(|a|^2+|c|^2=1\).

**Angular elimination and exact integral.** Put \(u=4\pi r^2\) and \(b=|c|^2\). At fixed radius, the Wigner function is
\[
W_f=2e^{-u/2}\bigl[1-2b+bu+2\sqrt u\,\operatorname{Re}(a\overline c e^{i\theta})\bigr]
\]
(up to the harmless sign convention for \(\theta\)). Its squared angular average is
\[
4e^{-u}\bigl[(1-2b+bu)^2+2u b(1-b)\bigr]
=4e^{-u}\bigl[1+4(u-1)b+(u^2-6u+4)b^2\bigr].
\]
Since \(2\pi r\,dr=du/4\), radial integration gives
\[
\mathcal E_{s,t}(b)=\int_s^t e^{-u}\bigl[1+4(u-1)b+(u^2-6u+4)b^2\bigr]\,du.
\]
The linear coefficient integrates to \(4U\), and
\[
\frac{d}{du}\bigl[u(4-u)e^{-u}\bigr]=(u^2-6u+4)e^{-u},
\]
so the quadratic coefficient is \(-(2U+V)\). In particular, \(\mathcal E_{s,t}'(0)=4U\), \(\mathcal E_{s,t}'(1)=-2V\), and
\[
\mathcal E_{s,t}(1)-\mathcal E_{s,t}(0)=s^2e^{-s}-t^2e^{-t}=2U-V.
\]

**Global maximization and equality.** If \(U\le0\), then \(s e^{-s}\le t e^{-t}\) implies \(s^2e^{-s}<t^2e^{-t}\), because \(0<s<t\). Hence the value at \(b=1\) is strictly below the value at \(b=0\). If the quadratic is concave, its nonpositive initial derivative makes \(b=0\) the unique maximizer; if convex or linear, comparison of endpoints proves the same conclusion. If \(U>0\) and \(V\le0\), both endpoint derivatives are nonnegative and the endpoint value difference \(2U-V\) is positive; concavity or convexity likewise makes \(b=1\) uniquely optimal. Finally, if \(U,V>0\), the derivative is positive at zero and negative at one, forcing strict concavity and the unique critical population \(2U/(2U+V)\). Thus the three cases are exhaustive, including their equality boundaries. The relative phase is arbitrary because the angular integral depends only on \(|c|^2\). Subtracting the two endpoint values from the vertex value gives \(4U^2/(2U+V)\) and \(V^2/(2U+V)\), proving the stated strict coherent advantage.

**Thin-shell transitions.** With \(t=s+\delta\), the mean-value theorem yields
\[
\frac U\delta\longrightarrow (s-1)e^{-s},\qquad
\frac V\delta\longrightarrow(-s^2+4s-2)e^{-s}.
\]
The first expression changes sign at \(s=1\). Once \(s>1\), the second changes sign at \(s=2+\sqrt2\). Substituting into the exact population formula gives the claimed limits, including endpoints by continuity and the boundedness \(0\le b_*\le1\). This concludes the proof.

## Verification

The accompanying standalone Python program `check_wigner_annulus.py` evaluates the defining Wigner Fourier integral independently of the closed formula, independently integrates \(|W_f|^2\) over physical polar coordinates, and compares the claimed optimizer against random competitors. It also verifies the strict coherent-gain identity and the thin-shell limits. With Python 3, NumPy and SciPy installed, run `python check_wigner_annulus.py`. The recorded run passed 36 direct Fourier-integral evaluations, 24 independent annular integrations, 400 random-parameter global-maximizer comparisons (five competitors each), and 20 shell-limit comparisons. These tests are finite diagnostic checks; the all-parameter conclusions follow from the analytic quadratic proof above.

## Relationship to prior work

Stra, Svela and Trapasso prove existence of maximizers for the **unrestricted** Wigner \(L^p\) concentration problem on any positive finite-measure phase-space set, including \(p=2\) [1, Theorem 1.1]. That theorem does not specify the first-two-Hermite restricted optimizer or annular transition parameters. Their sequel concerns the distinct Born–Jordan distribution [2]. The Gaussian/Hermite Wigner polynomials used in our proof are standard and are not claimed as new. For comparison, the signed linear functional \(\int_{\Omega_{s,t}}W_f\) is affine in \(b\) because its cross term has zero angular mean; it therefore never strictly prefers a coherent mixture over both pure Hermite states. The squared Wigner concentration analyzed here is nonlinear and does admit a genuinely strict mixed-state advantage. The contribution is the exact global optimization over all complex first-two-level superpositions for **every** concentric annulus, the three-region equality classification, the strict coherent advantage and the sharp thin-shell transition. The unrestricted maximizer from [1] need not belong to this two-dimensional family.

## Limitations

No assertion is made about the best value or optimizer over all of \(L^2(\mathbb R)\), translated or squeezed states, higher Hermite levels, nonconcentric masks, or \(L^p\) concentration for \(p\ne2\). This is an exact natural two-mode benchmark, not a solution of the general nonlinear Wigner concentration problem. A historically unindexed equivalent two-mode annulus calculation remains a priority risk. Computational tests alone do not certify the all-parameter claim.

## References

[1] F. Stra, E. A. T. Svela and S. I. Trapasso, *On the existence of optimizers for nonlinear time-frequency concentration problems: the Wigner distribution*, arXiv:2510.18683 (first posted 2025-10-21), https://arxiv.org/abs/2510.18683.

[2] F. Stra, E. A. T. Svela and S. I. Trapasso, *On the existence of optimizers for nonlinear time-frequency concentration problems: the Born–Jordan distribution*, arXiv:2605.10535 (first posted 2026-05-11), https://arxiv.org/abs/2605.10535.
