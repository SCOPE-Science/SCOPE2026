# Power-free \(o(1/t)\) Frank–Wolfe convergence on strictly convex bodies

## Finding

**Theorem (qualitative curvature suffices).** Let \(C\subset\mathbb R^n\) be a nonempty finite-dimensional compact convex set that is **strictly convex in its affine hull**: every open chord joining distinct points of \(C\) lies in the relative interior of \(C\). Let \(f\) be a differentiable convex function on a neighborhood of \(C\), with \(L\)-Lipschitz gradient on \(C\) for some \(L>0\). Let \(x_0\in C\) be arbitrary. For every iterate having a positive Frank–Wolfe gap, choose an exact linear minimizer \(s_t\in\arg\min_{s\in C}\langle\nabla f(x_t),s\rangle\), put \(g_t=\langle\nabla f(x_t),x_t-s_t\rangle\) and \(d_t=\|x_t-s_t\|\), and update \(x_{t+1}=x_t+\gamma_t(s_t-x_t)\) with either

\[
\gamma_t=\min\{1,g_t/(Ld_t^2)\}
\]

or **exact line search** over \([0,1]\). On a zero gap stop at the optimum. Then, with \(f_*=\min_{x\in C}f(x)\),

\[
\boxed{\lim_{t\to\infty}t\bigl(f(x_t)-f_*\bigr)=0.}
\]

The proof establishes no uniform numerical rate across the class: the assertion is a per-instance asymptotic little-o theorem. It applies even when no power-type local dual sharpness holds anywhere around a support tip. Both step-size rules are covered; arbitrary inexact oracles and the classical prescribed open-loop rule are not claimed.

## Assumptions and scope

All norms and inner products are Euclidean; affine-hull directions are identified with their translated linear span \(E\). If \(C\) is a singleton, the statement is immediate. Otherwise its diameter \(D>0\), and the projected gradient \(v_t=\Pi_E\nabla f(x_t)\) can be used in place of the full gradient for both the oracle and all inner products with differences of points in \(C\).

For every unit direction \(u\in E\), strict convexity makes its exposed minimizer
\[
s(u)=\operatorname*{arg\,min}_{z\in C}\langle u,z\rangle
\]
unique. Its continuity follows from compactness: each convergent subsequence of \(s(u_j)\), when \(u_j\to u\), minimizes the limiting linear form and so equals \(s(u)\). Fix any \(0<\varepsilon<D/2\). Define the **power-free exposure modulus**
\[
\omega_C(\varepsilon)=\min\bigl\{\langle u,z-s(u)\rangle:\ u\in E,\ \|u\|=1,\ z\in C,\ \|z-s(u)\|\ge\varepsilon\bigr\}.
\]
The constraint set of this minimum is compact and nonempty for such \(\varepsilon\). Since an equality \(\langle u,z-s(u)\rangle=0\) would give another exposed minimizer, compactness yields \(\omega_C(\varepsilon)>0\). The modulus is nondecreasing. No power lower bound in \(\varepsilon\) is asserted or needed.

## Proof

**1. Standard descent and approach to the minimizer set.** Let \(F_t=f(x_t)-f_*\ge0\). At a nonoptimal iterate, convexity implies \(g_t\ge F_t>0\); hence \(v_t\ne0\) and \(d_t>0\). The smoothness inequality along the segment to \(s_t\), minimized over \([0,1]\), gives for both step rules
\[
F_t-F_{t+1}\ge\tfrac12\min\{g_t,g_t^2/(Ld_t^2)\}
\ge\tfrac12\min\{F_t,F_t^2/(LD^2)\}.\tag{1}
\]
This proves monotonicity and \(F_t\to0\): a positive limiting value would force a fixed positive decrease. The minimizer set \(M=\{x\in C:f(x)=f_*\}\) is nonempty compact; because \(C\) is compact and \(F_t\to0\), the distances \(\delta_t=\operatorname{dist}(x_t,M)\) tend to zero. Indeed a subsequence bounded away from \(M\) would have a convergent subsequence with objective value \(f_*\), a contradiction.

If any \(F_t=0\), both rules terminate or remain optimal, so assume henceforth \(F_t>0\) for all \(t\). Choose \(p_t\in M\) nearest \(x_t\), then \(\delta_t>0\). Convexity at \(x_t\) gives
\[
F_t\le\langle v_t,x_t-p_t\rangle\le\|v_t\|\delta_t.\tag{2}
\]

**2. Support separation without a power law.** Normalize \(u_t=v_t/\|v_t\|\); the oracle returns \(s_t=s(u_t)\). For any fixed \(\varepsilon\in(0,D/2)\), whenever \(d_t\ge\varepsilon\), the preceding modulus and (2) imply
\[
g_t=\|v_t\|\langle u_t,x_t-s_t\rangle
\ge\|v_t\|\omega_C(\varepsilon)
\ge\frac{F_t}{\delta_t}\omega_C(\varepsilon).\tag{3}
\]
The continuity and strict positivity in this step are where compact strict convexity is essential.

**3. Diverging inverse-gap increments.** Set \(H_t=1/F_t\). Since \(F_{t+1}\le F_t\) and both are positive,
\[
H_{t+1}-H_t=\frac{F_t-F_{t+1}}{F_tF_{t+1}}
\ge\frac{F_t-F_{t+1}}{F_t^2}.\tag{4}
\]
If \(g_t\ge Ld_t^2\), equations (1), (4) and \(g_t\ge F_t\) give
\[
H_{t+1}-H_t\ge\frac1{2F_t}\longrightarrow+\infty.\tag{5}
\]
If \(g_t<Ld_t^2\), equations (1) and (4) yield
\[
H_{t+1}-H_t\ge\frac{g_t^2}{2Ld_t^2F_t^2}\ge\frac1{2Ld_t^2}.\tag{6}
\]
For \(d_t\ge\varepsilon\), (3) additionally yields
\[
H_{t+1}-H_t\ge\frac{\omega_C(\varepsilon)^2}{2L\delta_t^2d_t^2}
\ge\frac{\omega_C(\varepsilon)^2}{2L\delta_t^2D^2}\longrightarrow+\infty.\tag{7}
\]
To handle all mixed subsequences rigorously, fix arbitrary \(K>0\). First choose \(\varepsilon\in(0,D/2)\) so small that \(1/(2L\varepsilon^2)>K\). For sufficiently large \(t\), (5) exceeds \(K\). On the remaining indices (the second branch), (6) exceeds \(K\) if \(d_t<\varepsilon\), while (7) exceeds \(K\) if \(d_t\ge\varepsilon\), since \(\delta_t\to0\) and \(\omega_C(\varepsilon)>0\). Thus **every sufficiently late** reciprocal increment exceeds \(K\), i.e.
\[
H_{t+1}-H_t\longrightarrow+\infty.\tag{8}
\]
Its Cesàro mean therefore diverges: \(H_t/t\to\infty\). Consequently \(tF_t=t/H_t\to0\), as claimed. No finite computation, power exponent, or regularity of the support map beyond continuity is used.

**4. Explicit non-power-type example.** Put \(a=1/4\) and define on \([-a,a]\)
\[
h(x)=\begin{cases}e^{-1/x^2},&x\ne0,\\0,&x=0,\end{cases}\qquad
k(x)=h(a)+a^2-x^2,
\]
\[
C_a=\{(x,y)\in\mathbb R^2:|x|\le a,\ h(x)\le y\le k(x)\}.
\]
Direct differentiation for \(x\ne0\) gives \(h''(x)=e^{-1/x^2}(4/x^6-6/x^4)>0\) for \(0<|x|\le a\); continuity and the strict increase of \(h'\) through zero make \(h\) strictly convex. The function \(k\) is strictly concave, and \(h\le k\) with equality only at the horizontal endpoints. Hence every open chord of \(C_a\) lies in its interior: \(C_a\) is compact, full-dimensional and strictly convex.

The vertical supporting direction \(u=(0,1)\) has the unique exposed minimizer \(s(u)=(0,0)\). Along \(z(x)=(x,h(x))\) as \(x\to0\), its support gap equals \(h(x)=e^{-1/x^2}\) while \(\|z(x)-s(u)\|\ge|x|\). For every fixed finite \(q>0\),
\[
\frac{\langle u,z(x)-s(u)\rangle}{\|z(x)-s(u)\|^q}
\le\frac{e^{-1/x^2}}{|x|^q}\longrightarrow0.
\]
Thus no inequality \(A\|v\|\|z-s(v)\|^q\le\langle v,z-s(v)\rangle\) with fixed positive \(A\) and finite \(q\) can hold near that tip. Nevertheless the theorem applies to **every** smooth convex objective on \(C_a\), for both stated step rules. This witnesses a strict enlargement beyond power-type local dual sharpness. For a concrete zero-gradient instance, choose \(f(x,y)=\tfrac12(x^2+y^2)\) on \(C_a\): its unique feasible minimizer is \((0,0)\), and its gradient there is zero. Thus the exposed-optimum modulus formed with the gradient at the minimizer is identically zero, unlike the new separation modulus evaluated at current iterate directions.

## Verification

All steps are analytic. To reproduce, first prove the compactness and positivity of \(\omega_C(\varepsilon)\) for any fixed nonzero separation threshold. Apply the standard smoothness one-step descent bound (1), and check both branches of (4)–(7). In the small-displacement branch, positivity of \(\omega_C\) is *not* used; in the large-displacement branch it is used only at one fixed \(\varepsilon\). This is why super-polynomially flat support geometry does not invalidate the conclusion. To check the example, differentiate \(h\) twice and observe \(4-6x^2>0\) on \([-1/4,1/4]\) outside zero. No numerical experiment is required to validate the infinite-time limit.

## Relationship to prior work

Pokutta, *Frank–Wolfe Beyond 1/t Convergence* (arXiv:2604.28006, first submitted 2026-04-30), proves little-o rates for all smooth convex objectives under **power-type** local dual sharpness with parameters \((A,q)\), including short steps and exact line search (Definition 3.1, Theorem 3.5, Corollary 3.8). Its Remark A.4 explicitly demonstrates that compact strict convexity need not imply its LDS hypothesis, using precisely the superflat boundary mechanism. The present proof replaces power-type sharpness by the positive qualitative support-separation modulus, removes the exponent from the inverse-gap argument, and establishes the conclusion for the class that Remark A.4 leaves outside the published theorem. The technical starting descent inequality and minimizer-distance observation are standard and are credited to this prior work.

Kerdreux, d'Aspremont and Pokutta, *Projection-Free Optimization on Uniformly Convex Sets* (AISTATS 2021, PMLR 130:19–27), define an arbitrary set-curvature modulus in Definition 1.1, but their actual short-step/line-search convergence theorems (especially Theorem 2.2) impose a **power-law** curvature modulus and a uniform gradient-norm lower bound, with other results assuming power local scaling or error bounds. Consequently that work does not state or imply the present all-objectives, all-compact-strictly-convex conclusion by its quantified hypotheses. No algorithmic acceleration exponent is claimed here.


Dunn's earlier *Rates of Convergence for Conditional Gradient Algorithms Near Singular and Nonsingular Extremals* (SIAM J. Control Optim. 17, 1979) describes in its accessible abstract an \(o(1/t)\) bound for two conditional-gradient step rules when an exposed-optimum modulus \(a(\sigma)=\inf\{\langle\nabla f(\xi),z-\xi\rangle:z\in C,\ \|z-\xi\|\ge\sigma\}\) is positive for all \(\sigma>0\). On a strictly convex body with a nonzero-gradient constrained minimizer, that condition automatically holds. **This historical nonzero-gradient subcase is not presented as new here.** When \(\nabla f(\xi)=0\), however, Dunn's displayed \(a(\sigma)\) vanishes identically, so its abstract-stated sufficient condition does not apply. Dunn's 1980 sequel considers implicit line minimization and the same optimum-gradient-dependent growth function. Their complete texts were inaccessible, so we do not assert that they lack other pertinent conclusions. The contribution here is an unconditional theorem applying also to zero-gradient minimizers.

## Limitations

The conclusion is **strict little-o** for each fixed instance, not a specified uniform rate, and the proof does not quantify its speed on superflat bodies. It concerns only exact linear minimization and global short steps/exact line search; it does not cover approximate oracles, away-step variants, arbitrary line-search approximations, or the fixed open-loop step schedule. Finite dimensionality, compactness and strict convexity in the affine hull are used in the proof. The proof does not assert that strict convexity is necessary, nor that the result is the optimal characterization of all feasible sets. Other published or unindexed equivalent qualitative-modulus theorems could exist.

## References

1. Sebastian Pokutta, *Frank–Wolfe Beyond 1/t Convergence*, arXiv:2604.28006v3, originally submitted 2026-04-30; especially Proposition 2.1, Proposition 2.2, Definition 3.1, Theorem 3.5, Corollary 3.8, Remark A.4. https://arxiv.org/abs/2604.28006 ; full text: https://arxiv.org/html/2604.28006v3
2. Thomas Kerdreux, Alexandre d'Aspremont, Sebastian Pokutta, *Projection-Free Optimization on Uniformly Convex Sets*, Proceedings of Machine Learning Research 130 (2021), 19–27, particularly Definition 1.1 and Theorem 2.2. https://proceedings.mlr.press/v130/kerdreux21a.html ; PDF: https://proceedings.mlr.press/v130/kerdreux21a/kerdreux21a.pdf
3. J. C. Dunn, *Rates of Convergence for Conditional Gradient Algorithms Near Singular and Nonsingular Extremals*, SIAM Journal on Control and Optimization 17 (1979), 187–211, DOI 10.1137/0317015. https://doi.org/10.1137/0317015
4. J. C. Dunn, *Convergence Rates for Conditional Gradient Sequences Generated by Implicit Step Length Rules*, SIAM Journal on Control and Optimization 18 (1980), 473–487, DOI 10.1137/0318035. https://doi.org/10.1137/0318035
5. Martin Jaggi, *Revisiting Frank–Wolfe: Projection-Free Sparse Convex Optimization*, Proceedings of Machine Learning Research 28 (2013), 427–435; classical \(O(1/t)\) background. https://proceedings.mlr.press/v28/jaggi13.html
