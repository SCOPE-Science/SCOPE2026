# Sharp one-step objective-descent frontier for SAV gradient descent on the scalar double well

## Finding

For the **unrelaxed** scalar auxiliary-variable (SAV) gradient-descent update of Liu, Shen and Zhang with zero linear splitting, consider
\[
F(x)=\frac{(x^2-1)^2}{4},\qquad C=\frac14,
\]
with an arbitrary real initial value \(x\), initialized auxiliary variable \(r=\sqrt{F(x)+C}\), and nominal step \(h>0\). There is a unique, sharp positive constant
\[
\boxed{h_*=0.97493280401545327419\ldots}
\]
such that **the original objective decreases or stays equal after the first step for every real initialization if and only if** \(0<h\le h_*\). For \(0<h<h_*\), equality occurs only at the equilibria \(x=0,\pm1\). At \(h=h_*\), the two extra equal-energy initializations are exactly \(x=\pm\sqrt{1+u_*}\), where \(u_*\) is defined below. Every larger step size has a real starting point whose original objective strictly increases, even though the auxiliary energy \(r^2\) strictly decreases for every nonstationary starting point and every positive step.

Define the scalar function
\[
d(u)=\sqrt{1-u^2}+\frac{(1+u)(1-3u^2)}{1+u^2},\qquad 0\le u<1.
\]
Its derivative has exactly one zero \(u_*\in(0,1)\), which is its strict global maximizer on that interval, and
\[
\boxed{h_* =\frac{2}{d(u_*)},\qquad
u_*=0.09974525904287852385\ldots.}
\]
In particular, the global descent cutoff is **strictly below** the local linear stability threshold \(h=1\) at the minimizers.

The discrepancy can be arbitrarily severe. For \(0<\varepsilon<1\), initialize at \(x=\sqrt{1-\varepsilon}\) and take \(h=\varepsilon^{-3}\). As \(\varepsilon\downarrow0\), the original starting energy tends to zero, but the first-step original energy tends to infinity, while the updated auxiliary energy tends to zero:
\[
F(x)=\frac{\varepsilon^2}{4},\qquad
F(x^+)\sim\frac{1}{64\varepsilon^4},\qquad
(r^+)^2\sim\frac{\varepsilon^2}{16}.
\]
This is a statement about the **first unrelaxed step**, not about the long-time behavior of relaxed SAV or improved SAV methods.

## Assumptions and scope

All variables are real and all calculations use exact arithmetic. The potential \(F\), positive shift \(C=1/4\), initial relation \(r=\sqrt{F(x)+C}\), and zero linear splitting are fixed. For arbitrary \(h>0\) the update is
\[
\begin{aligned}
r^+&=\frac{r}{1+h\,F'(x)^2/[2(F(x)+C)]},\\
x^+&=x-h\frac{r^+}{\sqrt{F(x)+C}}F'(x).
\end{aligned}
\]
The claim concerns the original energy \(F(x^+)\) and the modified energy \((r^+)^2\). It is not an unconditional energy statement for subsequent steps with an independently evolving auxiliary variable. This is not the relaxed algorithm or an algorithm with nonzero positive-semidefinite linear splitting.

## Proof

**1. Scalar reduction.** Put \(t=x^2\ge0\), \(u=t-1\), and
\[
\beta(t)=\frac{F'(x)^2}{2(F(x)+C)}
=\frac{2t(t-1)^2}{1+(t-1)^2},\qquad
\alpha=\frac{h}{1+h\beta(t)}.
\]
Since \(F'(x)=x(t-1)\), the exact first step becomes
\[
\boxed{x^+=x[1-\alpha(t-1)]},\qquad
\boxed{r^+=\frac{r}{1+h\beta(t)}}.
\]
For \(t\notin\{0,1\}\), \(\beta(t)>0\) and hence \(0<(r^+)^2<r^2\) for every \(h>0\). For \(t=0\) and \(t=1\), the method leaves \(x\) unchanged.

**2. No obstruction at large amplitude.** Suppose \(t\ge2\) and set \(u=t-1\ge1\). Then
\[
0<\alpha u<\frac{u}{\beta(t)}=
\frac{1+u^2}{2u(1+u)}\le\frac12.
\]
Consequently \(0<(x^+)^2\le t\). Because \(t\ge2\), the elementary inequality \((s-1)^2\le(t-1)^2\) holds for every \(s\in[0,t]\). Thus \(F(x^+)<F(x)\) whenever \(t\ge2\) and \(h>0\). The inequality is strict because the step moves \(t\) strictly downward and does not reach zero.

**3. Complete energy comparison inside the well.** Let \(0<t<2\) and \(t\ne1\), and first restrict to \(0<h\le1\). Then \(0<\alpha\le1\), so \(x^+\) retains the sign of \(x\). For \(t<1\), its magnitude increases; for \(t>1\), it decreases. The same-energy partner on the other side of the minimum satisfies
\[
(x^+)^2=2-t.
\]
The exact test for not passing that partner is, in both ranges \(0<t<1\) and \(1<t<2\),
\[
F(x^+)\le F(x)
\quad\Longleftrightarrow\quad
\alpha\le\frac{2}{t+\sqrt{t(2-t)}}.
\]
Substitution of the expression for \(\alpha\) and multiplication by strictly positive denominators turns this into
\[
\boxed{h\,d(t-1)\le2},
\]
where
\[
d(u)=1+u+\sqrt{1-u^2}-\frac{4(1+u)u^2}{1+u^2}
=\sqrt{1-u^2}+\frac{(1+u)(1-3u^2)}{1+u^2}.
\]
This equivalence remains valid when \(d\le0\), in which case the inequality is automatic.

**4. Exact maximizer.** On \(-1<u<0\), the term subtracted in the first expression for \(d(u)\) is nonnegative; moreover \(1+u+\sqrt{1-u^2}<2\). Hence \(d(u)<2\). On \(0<u<1\), direct differentiation gives
\[
\begin{aligned}
d'(u)&=-\frac{u}{\sqrt{1-u^2}}
-\frac{3u^4+10u^2+8u-1}{(1+u^2)^2},\\
d''(u)&=-\frac{1}{(1-u^2)^{3/2}}
+\frac{8(u-1)(u^2+4u+1)}{(1+u^2)^3}<0.
\end{aligned}
\]
As \(d'(0)=1\) and \(d'(u)\to-\infty\) as \(u\uparrow1\), there is exactly one critical point \(u_*\in(0,1)\); it is a strict maximum with \(d(u_*)>d(0)=2\). Comparison with the negative half-interval shows it is the unique global maximizer for \(-1<u<1\). Therefore \(h_*=2/d(u_*)\) lies strictly between zero and one. Steps \(0<h\le h_*\) satisfy the inequality from Step 3 for every \(t\in(0,2)\), and Step 2 handles \(t\ge2\). Strictness and the equality cases follow from uniqueness of \(u_*\).

**5. Sharpness beyond the frontier.** For \(h_*<h\le1\), choose \(t=1+u_*\). The sharp inequality in Step 3 reverses, so \(F(x^+)>F(x)\) for either sign of \(x=\sqrt{1+u_*}\). For \(h>1\), linearizing the first-step map at either minimizer \(x=1\) or \(x=-1\) gives multiplier \(1-2h\). Since \(F\) has a nondegenerate quadratic minimum there,
\[
\lim_{x\to1,\ x\ne1}\frac{F(x^+)}{F(x)}=(1-2h)^2>1.
\]
Thus every \(h>h_*\) fails universal first-step objective descent. The criterion and equality characterization are both sharp.

**6. Unbounded mismatch.** Let \(x=\sqrt{1-\varepsilon}\), \(h=\varepsilon^{-3}\). Then \(t=1-\varepsilon\),
\[
\beta(t)=\frac{2(1-\varepsilon)\varepsilon^2}{1+\varepsilon^2},\qquad
x^+=\sqrt{1-\varepsilon}
\left[1+\frac{\varepsilon^{-2}}{1+\varepsilon^{-3}\beta(t)}\right].
\]
Since \(1+h\beta(t)\sim2/\varepsilon\), we obtain \(x^+\sim1/(2\varepsilon)\) and \((r^+)^2=[(1+\varepsilon^2)/4]/[1+h\beta(t)]^2\sim\varepsilon^2/16\). Substituting \(x^+\) into \(F\) proves \(F(x^+)\sim1/(64\varepsilon^4)\), whereas \(F(x)=\varepsilon^2/4\). This completes the claim.

## Verification

The accompanying standalone `verify.py` computes the SAV map independently from the algorithm equations, differentiates the rational part of \(d\) symbolically, checks a strictly positive rational counterexample, verifies all displayed \(\varepsilon\)-limits symbolically, and numerically isolates \(u_*\) and \(h_*\) to high precision. It also runs 4,000 reproducible cross-checks below the predicted threshold. The cross-checks are not used to prove the universal statement.

The derivative signs at the rational endpoints \(u=0.099745258\) and \(u=0.099745260\) are positive and negative respectively, and strict concavity makes this a unique root bracket. For a fully rational witness beyond the threshold, take \(x=21/20\) and \(h=49/50\). Exact fraction arithmetic yields
\[
F(x^+)-F(x)
=\frac{775376339938187054333462400249481938957}
{15295474376164894850934442779966751705088000}>0.
\]
The leading first-step auxiliary energy decreases simultaneously. Running `python verify.py` requires SymPy and mpmath; no external data or unpublished certificate is required.

## Relationship to prior work

Liu, Shen and Zhang introduced the explicit unrelaxed SAV gradient-descent update and established unconditional decrease of its **modified auxiliary energy**; its general convergence analysis treats convex/Lipschitz and quadratic situations under additional hypotheses. Those statements do not establish the exact all-initialization descent frontier for the present nonconvex quartic potential. Their relaxation method is a different algorithm.

The broader observation that standard SAV methods may fail to dissipate the original energy is already established in the literature. Chen, Wang and Zhao analyze an improved and stabilized SAV scheme that targets original energy stability and report double-well experiments for other SAV discretizations. Liu, Zhang and Li develop energy-optimal SAV corrections; Huang and collaborators develop a weighted SAV approach. None of these accessible statements or inspected relevant primary-text sections gives the exact scalar optimization frontier \(h_*\), its uniqueness proof or the present divergent first-step original-versus-auxiliary energy construction for the specified Liu–Shen–Zhang update. The distinction between an existing qualitative defect and the sharp quantitative theorem is essential.

Relevant published mathematical-record findings on objective spikes for FISTA, NIPG, Polyak steps and Allen–Cahn extrapolation concern different algorithms and do not imply this SAV formula. Bibliographic coverage is not a proof of priority.

## Limitations

The exact constant depends on the chosen normalization of the double-well potential, the positive shift \(C=1/4\), initial auxiliary consistency, and zero linear splitting. It is a **one-step, original-objective** theorem only. It neither proves a multi-step rate nor rules out safeguards, different shifts, stabilizations, relaxed SAV, or improved SAV schemes. Floating-point overflow, implementation reliability and nonlinear PDE stability are outside its scope. The universal proofs are analytic; the symbolic checker corroborates selected algebraic identities and asymptotic limits. Literature-priority uncertainty remains because no finite search excludes all equivalent analyses.

## References

1. X. Liu, J. Shen, X. Zhang, *An efficient and robust SAV based algorithm for discrete gradient systems arising from optimizations*, arXiv:2301.02942, first public version 2023-01-07; especially Section 2.1, equations (2.4)–(2.5), and Section 4. https://arxiv.org/abs/2301.02942
2. R. Chen, T. Wang, X. Zhao, *Improved scalar auxiliary variable schemes for original energy stability of gradient flows*, arXiv:2405.03403, first public 2024-05-06; especially Sections 2 and 4.1. https://arxiv.org/abs/2405.03403
3. Z. Liu, Y. Zhang, X. Li, *A novel energy-optimal scalar auxiliary variable (EOP-SAV) approach for gradient flows*, arXiv:2304.11288, first public 2023-04-22. https://arxiv.org/abs/2304.11288
4. Q.-A. Huang, W. Jiang, J. Z. Yang, C. Yuan, *A weighted scalar auxiliary variable method for solving gradient flows: bridging the nonlinear energy-based and Lagrange multiplier approaches*, arXiv:2411.17403, first public 2024-11-26; Sections 2–3. https://arxiv.org/abs/2411.17403
