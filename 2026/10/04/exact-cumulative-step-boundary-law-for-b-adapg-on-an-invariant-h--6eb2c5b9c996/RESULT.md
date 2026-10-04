# Exact cumulative-step boundary law for B-adaPG on an invariant Hellinger ray

## Finding
Let \(n\ge 2\), let \(u\in\mathbb{{R}}^n\) satisfy \(\|u\|_2=1\), and fix \(c>1\). Consider
\[
f(x)=\frac12\|x-cu\|_2^2,
\]
with \(g\equiv0\), over the closed unit ball, enforced by the Legendre kernel
\[
\phi(x)=-\sqrt{{1-\|x\|_2^2}}
\]
on \(\|x\|_2\le1\) and \(+\infty\) outside. Run B-adaPG from \(x^0=t_0u\), where \(-1<t_0<1\), using any positive initialization steps allowed by the method. If \(\gamma_k\) denotes the generated Bregman-proximal-gradient stepsize and
\[
S_k=\sum_{{j=1}}^k\gamma_j,
\]
then every iterate has the form \(x^k=t_ku\), with \(-1<t_k<1\), and
\[
\frac{{t_{{k+1}}}}{{\sqrt{{1-t_{{k+1}}^2}}}}
=
\frac{{t_k}}{{\sqrt{{1-t_k^2}}}}+\gamma_{{k+1}}(c-t_k).
\]
Moreover,
\[
t_k\uparrow1,\qquad S_k\to\infty,
\]
and the exact cumulative-step asymptotics are
\[
\frac{{t_k/\sqrt{{1-t_k^2}}}}{{S_k}}\longrightarrow c-1,
\]
\[
1-t_k\sim\frac{{1}}{{2(c-1)^2S_k^2}},
\qquad
f(x^k)-f(u)\sim\frac{{1}}{{2(c-1)S_k^2}}.
\]
This gives full-sequence convergence for a symmetric boundary-active instance using the source paper's nonseparable Hellinger-ball kernel, even though that kernel fails the paper's Bregman-zone assumption in dimensions \(n\ge2\).

## Assumptions and scope
The statement is for the exact B-adaPG iteration of Ou--Latafat--Themelis, not for an arbitrary adaptive rule. The objective is the radial least-squares model \(f(x)=\tfrac12\|x-cu\|_2^2\), the boundary minimizer is \(u\), and the initialization is collinear with \(u\). The conclusion does not claim robustness to non-collinear perturbations. The asymptotic rate is expressed in endogenous cumulative step mass \(S_k\); it does not by itself imply an iteration-count rate without further information about \(S_k\).

The kernel is exactly the nonseparable function treated in Example 2.5 of Ou--Latafat--Themelis. That example states that it is Legendre and 1-coercive and that, for \(n\ge2\), it violates their Assumption 2.4. Their Assumption 2.1 still applies here: the quadratic \(f\) is convex and twice differentiable, \(g\equiv0\) is proper closed convex, and the closed-ball problem has the unique solution \(u\).

## Proof
Put
\[
h(t)=\frac{t}{\sqrt{1-t^2}},\qquad -1<t<1.
\]
For \(x=tu\), radial symmetry gives \(\nabla\phi(x)=h(t)u\). The Bregman proximal-gradient update with \(g\equiv0\) satisfies
\[
\nabla\phi(x^{{k+1}})=\nabla\phi(x^k)-\gamma_{{k+1}}\nabla f(x^k).
\]
Since \(\nabla f(t_ku)=(t_k-c)u\), induction from \(x^0=t_0u\) shows that all iterates remain collinear and that, with \(y_k=h(t_k)\),
\[
y_{{k+1}}=y_k+\gamma_{{k+1}}(c-t_k).
\]
The B-adaPG stepsizes are strictly positive. Because \(t_k<1<c\), the right-hand increment is positive, so \(y_k\), and therefore \(t_k=h^{{-1}}(y_k)\), increase strictly. Thus \(t_k\to t_\infty\) for some \(t_\infty\le1\), and
\[
f(x^k)=\frac12(c-t_k)^2
\]
decreases to \(\tfrac12(c-t_\infty)^2\).

Theorem 2.7 of Ou--Latafat--Themelis, under their basic Assumption 2.1 and without Assumption 2.4, gives
\[
\inf_k f(x^k)=\min_{{\|x\|_2\le1}}f(x)=\frac12(c-1)^2.
\]
Since the preceding scalar objective sequence is decreasing, its limit equals this infimum. As \(c>1\), this forces \(t_\infty=1\). Hence \(x^k\to u\), despite the failure of the Bregman-zone assumption for this kernel when \(n\ge2\).

Now let \(S_k=\sum_{{j=1}}^k\gamma_j\). Telescoping the exact recursion yields
\[
y_k=y_0+\sum_{{j=1}}^k\gamma_j(c-t_{{j-1}}).
\]
Because \(t_k\to1\), one has \(y_k=h(t_k)\to\infty\). Also \(c-t_{{j-1}}\le c+1\), so bounded \(S_k\) would make the displayed right-hand side bounded, a contradiction. Thus \(S_k\to\infty\). Positivity of the weights and \(c-t_{{j-1}}\to c-1\) then give, by the weighted Cesàro principle,
\[
\frac{y_k}{S_k}\longrightarrow c-1.
\]
Finally, \(h^{{-1}}(y)=y/\sqrt{{1+y^2}}\), and therefore
\[
1-h^{{-1}}(y)\sim\frac1{2y^2}
\]
as \(y\to\infty\). Substitution of \(y_k\sim(c-1)S_k\) proves the first asymptotic. For the objective,
\[
f(t_ku)-f(u)=(c-1)(1-t_k)+\frac12(1-t_k)^2,
\]
which gives the second asymptotic.

## Verification
The proof uses only the exact optimality identity of the Bregman proximal-gradient subproblem, positivity of B-adaPG steps, and the source theorem's unconditional objective-infimum property. No finite experiment is used as an infinite proof. A small standalone checker, `check_boundary_law.py`, numerically replays the scalar dual recursion for an independent positive, divergent step schedule and verifies the two asymptotic constants; it is a consistency check only.

The critical source facts were checked in the full arXiv text of arXiv:2508.01353v2: Assumption 2.1; Example 2.5, which exhibits failure of Assumption 2.4 for the nonseparable Hellinger-ball kernel when \(n\ge2\); Theorem 2.7, which still guarantees \(\inf_k f(x^k)=\min f\); and Section 5.6, which numerically studies boundary-active least-squares problems with the same kernel outside Assumption 2.4.

## Relationship to prior work
Ou--Latafat--Themelis provide the method, the Hellinger-ball counterexample to their Bregman-zone assumption, the objective-infimum guarantee, and numerical evidence on boundary-active least squares. Their text does not state the invariant-ray convergence theorem or the exact cumulative-step asymptotic above.

Azizian--Iutzeler--Malick--Mertikopoulos analyze convergence rates of Bregman proximal methods and explicitly study Hellinger geometry. Their one-dimensional examples identify boundary effects, and their general rate theorem admits variable steps under its step conditions, with bounds involving cumulative steps. This prior work covers the general phenomenon that Hellinger boundary geometry can produce polynomial behavior; the present statement does not claim that phenomenon as new. The additional point here is method-specific: for B-adaPG on the source paper's \(n\ge2\) nonseparable Hellinger kernel, the source theorem itself forces the endogenous cumulative step mass to diverge on the invariant ray, and the exact scalar recursion then yields full-sequence convergence and the stated leading constants without a monotonicity or externally imposed small-step condition.

## Limitations
The invariant ray is a special symmetric subproblem. The result does not prove full-sequence convergence for general boundary-active B-adaPG instances using this kernel, nor does it control angular perturbations. The rate is in cumulative steps \(S_k\), so a rate in the iteration counter requires additional information about how B-adaPG's adaptive steps grow or decay. The literature comparison found a recent general iterate-convergence framework for Bregman proximal methods (arXiv:2608.05536), but its full PDF could not be retrieved during this check; its abstract was inspected, so possible overlap beyond the abstract remains a residual literature risk.

## References
1. H. Ou, P. Latafat, A. Themelis, “Linesearch-free adaptive Bregman proximal gradient for convex minimization under local relative smoothness,” arXiv:2508.01353v2, 2026. Earliest arXiv version: 2 August 2025.
2. W. Azizian, F. Iutzeler, J. Malick, P. Mertikopoulos, “The Rate of Convergence of Bregman Proximal Methods: Local Geometry Versus Regularity Versus Sharpness,” arXiv:2211.08043; SIAM Journal on Optimization.
3. H. Chen, J. Fan, A. M.-C. So, “A Unified Framework for Iterate Convergence of Bregman Proximal Methods,” arXiv:2608.05536, 2026. Abstract inspected; full-text retrieval was unavailable during this verification.
