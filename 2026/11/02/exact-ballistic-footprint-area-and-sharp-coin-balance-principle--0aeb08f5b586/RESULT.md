# Exact ballistic-footprint area and sharp coin-balance principle for planar quantum walks

## Finding

Consider the homogeneous two-state alternate-coin walk on \(\mathbb Z^2\), with one-step operator \(U=S_2C_2S_1C_1\). Let \(a=|a_1||a_2|>0\), \(b=|b_1||b_2|>0\) be its two nonzero coin-product moduli, with \(a+b\le 1\), as in [1]. Write \(\Sigma(a,b)\subset\mathbb R^2\) for the joint asymptotic group-velocity spectrum, not for an initial-state-dependent probability superlevel set. Its two-dimensional Lebesgue area is \(\mathcal A(a,b)=\operatorname{area}(\Sigma(a,b))\).

**Theorem (exact area and rigidity).** For every \(a,b>0\) with \(a+b\le1\), writing \(s=a+b\) and \(t=a-b\),

\[
\boxed{\mathcal A(a,b)=2\left[s\arcsin(s)\sqrt{1-t^2}-t\arcsin(t)\sqrt{1-s^2}\right].}
\]

The inverse sine is the principal branch on \([-1,1]\). The maximal *coordinate* ballistic speed in [1] is exactly \(v_{\max}=s\). Among all admissible walks of any given \(s\in(0,1]\), the area has the unique parameter-pair maximizer \(a=b=s/2\), and

\[
\boxed{\max_{a+b=s}\mathcal A(a,b)=2s\arcsin s.}
\]

In particular, \(\mathcal A(a,b)\le\pi\), with equality in the nondegenerate parameter region precisely at \(a=b=1/2\). For fixed \(s\), the area is strictly decreasing in \(|a-b|\) away from zero. Moreover, the **globally sharp quadratic rigidity inequality** is

\[
\boxed{2s\arcsin s-\mathcal A(a,b)\ge\left[s\arcsin s+2\sqrt{1-s^2}\right](a-b)^2,}
\]

with equality only at \(a=b\); the coefficient is optimal for every fixed \(s\) because it is the infinitesimal quadratic deficit. For fixed \(0<s<1\), as \(t\to0\),

\[
\mathcal A\left(\frac{s+t}{2},\frac{s-t}{2}\right)=2s\arcsin s-\left[s\arcsin s+2\sqrt{1-s^2}\right]t^2+O_s(t^4).
\]

The optimal area has the nonanalytic endpoint law

\[
\boxed{\pi-\max_{a+b=s}\mathcal A(a,b)\sim2\sqrt{2(1-s)}\quad(s\uparrow1).}
\]

Thus equal maximal coordinate speeds need not mean comparable two-dimensional velocity footprints. For example, \((a,b)=(0.3,0.3)\) and \((0.1,0.5)\) both have maximal coordinate speed \(0.6\), but their areas are approximately \(0.7722013306\) and \(0.4443634283\), respectively.

## Assumptions and scope

The on-site coin matrices are homogeneous and unitary, with the standard alternating coordinate shifts; the original model and the product parameters appear in [1, equations (4)–(10)] and in its revision [2, section II]. Coin phases do not modify the joint velocity spectrum. The parameter region is \(a,b>0\), \(s=a+b\le1\); every such pair is realizable by the coin family [1, figure 1; 2, lemma 2]. The theorem concerns the area of the **full joint spectral support** of the two asymptotic velocity operators, independent of the initial wave packet. A special initial state could occupy a proper subset of that support; neither its weighted probability measure nor its finite-time spread is evaluated here.

Write \(v_1,v_2\) for physical coordinate velocities and rotate orthogonally to

\[
u=(v_1+v_2)/\sqrt2,\qquad w=(v_1-v_2)/\sqrt2.
\]

The rotation preserves area. In the interior \(s<1\), [1, equations (14)–(19)] establish that the rotated joint velocity spectrum is the intersection of two centered, axis-aligned ellipses. Their precise equations are the only published input to the area calculation. At \(s=1\), the two ellipses coincide [1, section II.2; 2, theorem 9].

## Proof

**1. Two-ellipse support and its crossing.** Define

\[
\delta=\sqrt{(1-s^2)(1-t^2)},\qquad p=1+st,\qquad q=1-st.
\]

For \(s<1\), the equations of the two ellipses given in [1, equations (14)–(19)] become, after the orthogonal change of coordinates,

\[
E_R:\ \frac{u^2}{p+\delta}+\frac{w^2}{q-\delta}\le1,
\qquad E_T:\ \frac{u^2}{p-\delta}+\frac{w^2}{q+\delta}\le1.
\]

All four denominators are positive for \(a,b>0\) and \(s<1\). The two boundary curves meet at the four points \((u,w)=(\pm\sqrt2a,\pm\sqrt2b)\): substituting \(u^2=2a^2\), \(w^2=2b^2\) verifies both equalities directly. There are no other first-quadrant crossings because subtracting the two linear equations in \(u^2,w^2\) gives one ray, intersecting each ellipse once there. The \(E_R\) upper semicircle has the smaller vertical intercept, whereas \(E_T\) has the smaller horizontal intercept. Therefore, in the positive quadrant, the upper boundary of the intersection is the \(E_R\) arc until \(u_0=\sqrt2a\), followed by the \(E_T\) arc to \(\sqrt{p-\delta}\).

**2. Exact integration.** Fourfold reflection symmetry implies

\[
\begin{split}
\mathcal A(a,b)=4\Bigg[&\sqrt{q-\delta}\int_0^{\sqrt2a}\sqrt{1-\frac{u^2}{p+\delta}}\,du\\
+&\sqrt{q+\delta}\int_{\sqrt2a}^{\sqrt{p-\delta}}\sqrt{1-\frac{u^2}{p-\delta}}\,du\Bigg].
\end{split}
\]

Use the elementary primitive \(\int\sqrt{1-u^2/R^2}\,du=(u\sqrt{1-u^2/R^2}+R\arcsin(u/R))/2\). At the common crossing the two height contributions proportional to \(u\) cancel exactly. The remaining endpoints give

\[
\begin{split}
\mathcal A=2\bigg[&\sqrt{(p+\delta)(q-\delta)}\arcsin\frac{\sqrt2a}{\sqrt{p+\delta}}\\
+&\sqrt{(p-\delta)(q+\delta)}\arccos\frac{\sqrt2a}{\sqrt{p-\delta}}\bigg].
\end{split}
\]

Let \(\alpha=\arcsin s\) and \(\beta=\arcsin t\), so \(0<\alpha<\pi/2\) and \(-\alpha<\beta<\alpha\). Direct trigonometric identities imply

\[
\begin{array}{ll}
p+\delta=2\cos^2((\alpha-\beta)/2),&q-\delta=2\sin^2((\alpha-\beta)/2),\\
p-\delta=2\sin^2((\alpha+\beta)/2),&q+\delta=2\cos^2((\alpha+\beta)/2).
\end{array}
\]

Moreover, \(\sqrt2a=(s+t)/\sqrt2\), hence

\[
\arcsin\frac{\sqrt2a}{\sqrt{p+\delta}}=\frac{\alpha+\beta}{2},\qquad
\arccos\frac{\sqrt2a}{\sqrt{p-\delta}}=\frac{\alpha-\beta}{2}.
\]

Both equalities use the principal inverse-trigonometric branches; their arguments lie in the required intervals. Thus

\[
\mathcal A=(\alpha+\beta)\sin(\alpha-\beta)+(\alpha-\beta)\sin(\alpha+\beta)
=2\left[s\alpha\cos\beta-t\beta\cos\alpha\right],
\]

which is the claimed formula for \(s<1\). At \(s=1\), [1, section II.2] gives the single ellipse \(u^2/(2a)+w^2/(2b)\le1\), whose area equals \(2\pi\sqrt{ab}=\pi\sqrt{1-t^2}\). The formula above has the same \(s=1\) value, extending the identity to the entire nondegenerate triangle.

**3. Fixed-speed optimum and stability.** Since the area expression is even in \(t\), put \(r=|t|\in[0,s)\). For every fixed \(s\in(0,1]\), differentiating gives

\[
\frac{d\mathcal A}{dr}=-2\left[\frac{s\arcsin s\,r}{\sqrt{1-r^2}}+\sqrt{1-s^2}\left(\arcsin r+\frac r{\sqrt{1-r^2}}\right)\right]<0\qquad (0<r<s).
\]

The derivative remains strictly negative when \(s=1\). Therefore the unique maximum at fixed \(s\) is \(t=0\), equivalently \(a=b=s/2\), where the area is \(2s\arcsin s\). This maximal value increases strictly with \(s\in(0,1]\) because its derivative is \(2\arcsin s+2s/\sqrt{1-s^2}>0\) for \(s<1\). Its endpoint is \(\pi\), proving global maximality and rigidity. For global quantitative stability, use \(1-\sqrt{1-r^2}\ge r^2/2\) and \(r\arcsin r\ge r^2\), with strict inequalities for \(r>0\). Applying them to the exact area deficit proves the boxed quadratic rigidity inequality. Taylor expansion in \(t\) shows its coefficient cannot be increased uniformly over the admissible parameter pairs at fixed \(s\). Finally \(\arcsin(1-\varepsilon)=\pi/2-\sqrt{2\varepsilon}+O(\varepsilon^{3/2})\) yields the sharp square-root deficit as \(\varepsilon=1-s\downarrow0\). All quantifiers here concern fixed positive \(s\) and the stated limits; no joint scaling is asserted.

## Verification

Run the included standard-library-only Python program with `python3 VERIFY.py`. It independently integrates the two explicit ellipse profiles by midpoint quadrature, checks the boundary crossing, evaluates group velocities from the Bloch dispersion relation, tests containment in both ellipses, compares the degenerate single-ellipse limit, checks strict monotonicity on grids, and tests the sharp square-root coefficient. A successful run prints the exact number of numerical checks and exits with status zero. These finite checks corroborate, but do not replace, the preceding analytic proof.

## Relationship to prior work

Asahara, Funakawa, Seki and Suzuki [1, 2] derive the complete weak-limit laws, the intersection-of-two-ellipses support, and the identity \(v_{\max}=a+b\); those are explicitly used, not claimed anew. Their later revision [2] likewise describes the \(s=1\) circle and ellipse as known limiting regimes. The earlier two-dimensional Grover/alternate-walk results [3, 4] treat the single-ellipse family. The contribution proved here is the **two-parameter area formula, sharp fixed-coordinate-speed coin-balance maximizer, globally sharp quadratic imbalance penalty and square-root endpoint law**. In particular the envelope \(2s\arcsin s\) is not the trivial area of one of the two constituent ellipses. The comparison is a best-knowledge distinction between statements; it is not a certificate of publication priority.

## Limitations

The exact formula is for the full joint velocity-spectrum area in the specified two-state homogeneous alternating walk. It does not give the area or volume of probability superlevel sets, probability mass inside geometric subregions, finite-time quantum-walk trajectories, or general multi-coin/multi-band networks. Its positivity for every \(a,b>0\) does not assert that all states have strictly positive spectral density at every velocity. The original support characterization is a premise borrowed from [1, 2]. Independent review or exhaustive priority certification has not been performed.

## References

[1] K. Asahara, D. Funakawa, M. Seki, A. Suzuki, *Two dimensional quantum central limit theorem by quantum walks*, arXiv:2408.09578v1 (first posted 18 August 2024), sections I–III and equations (14)–(19), https://arxiv.org/html/2408.09578v1 .

[2] K. Asahara, D. Funakawa, M. Seki, A. Suzuki, *Two-dimensional quantum central limit theorem by quantum walks*, arXiv:2408.09578v2 (14 November 2025), sections II, III.1, III.4, V.1 and appendix D, https://arxiv.org/html/2408.09578v2 .

[3] C. Di Franco, M. Mc Gettrick, T. Machida, Th. Busch, *Alternate two-dimensional quantum walk with a single-qubit coin*, arXiv:1107.4400, section V, https://arxiv.org/pdf/1107.4400 .

[4] K. Watabe, N. Kobayashi, M. Katori, N. Konno, *Limit distributions of two-dimensional quantum walks*, arXiv:0802.2749, section III, https://arxiv.org/pdf/0802.2749 .
