# Infinitely many distant two-cycles for a bounded Halley correction on nearly linear equations

## Finding

For every fixed \(0<\delta<1\), the real-analytic, strictly increasing, bijective function
\[
f_\delta(x)=x+\delta\sin x
\]
has the unique zero \(0\), with \(1-\delta\le f_\delta'(x)\le1+\delta\) for all \(x\in\mathbb R\). Nevertheless, the positive bounded Halley-type root iteration introduced in arXiv:2609.08110v1 has infinitely many distinct, nonzero prime period-two orbits \(\{\pm c_{\delta,n}\}\). More precisely, for all sufficiently large integers \(n\ge0\), exactly one such orbit has its positive point in
\[
\left(2\pi n+\frac{5\pi}{4},\;2\pi n+\frac{3\pi}{2}\right).
\]
Writing \(B_n=2\pi n+3\pi/2\), its location obeys
\[
c_{\delta,n}=B_n-\frac{1+1/(4\delta^2)}{B_n}+O_\delta(B_n^{-2}).
\]
In contrast, when \(0<\delta<1/3\), ordinary, undamped Newton iteration for the **same** function converges to \(0\) from every real initial value, with the global error bound
\[
|x_{k+1}|\le\frac{2\delta}{1-\delta}|x_k|.
\]
In particular, the bounded-correction method can have nonconvergent orbits even when the derivative condition number \((1+\delta)/(1-\delta)\) is arbitrarily close to one. No assertion is made that the constructed two-cycles are attracting.

## Assumptions and scope

All calculations are in exact real arithmetic. The parameter \(\delta\) is fixed in \((0,1)\); the Newton comparison uses \(\delta<1/3\). Set
\[
A(z)=\frac{1-z+z^2/2}{1-z+z^2},\qquad
R(z)=\sqrt{1+z^2}-z,\qquad
C_*(z)=\frac{2}{1+A(z)R(z)}.
\]
The denominator in \(A\) is positive on \(\mathbb R\); both \(A\) and \(R\) are strictly positive, so \(0<C_*(z)<2\). For a twice differentiable \(f\) with \(f'\ne0\), let
\[
L_f(x)=\frac{f(x)f''(x)}{f'(x)^2},\qquad
T_f(x)=x-C_*(L_f(x))\frac{f(x)}{f'(x)}.
\]
These are precisely the source method's scalar correction and update. Here \(f_\delta'\ge1-\delta>0\), so the update is defined at every real point. The intervals above are locations of the claimed cycles, not a classification of all possible periodic orbits.

## Proof

**Exact cycle criterion.** For \(t>0\), put
\[
p(t)=1+\delta\cos t,\quad
\ell(t)=-\frac{\delta(t+\delta\sin t)\sin t}{p(t)^2},\quad
Q(t)=C_*(\ell(t))\frac{t+\delta\sin t}{t p(t)}.
\]
Then \(T_{f_\delta}(t)=t(1-Q(t))\). Since \(f_\delta\) is odd, \(f_\delta'\) is even, and \(f_\delta''\) is odd, \(\ell(-t)=\ell(t)\) and \(T_{f_\delta}(-t)=-T_{f_\delta}(t)\). Therefore any \(c>0\) solving \(Q(c)=2\) gives the exact prime period-two orbit \(c\mapsto-c\mapsto c\). It is prime because \(c\ne0\).

**Existence in every sufficiently distant window.** Set
\[
a_n=2\pi n+5\pi/4,\qquad B_n=2\pi n+3\pi/2.
\]
At \(t=B_n\), \(\sin t=-1\), \(\cos t=0\) and \(\ell(t)=\delta(t-\delta)>0\), hence
\[
Q(B_n)=C_*(\delta(B_n-\delta))\left(1-\frac{\delta}{B_n}\right)<2.
\]
At \(t=a_n\), \(\sin t=\cos t=-1/\sqrt2\); since \(\ell(a_n)\to+\infty\), \(C_*(\ell(a_n))\to2\), so
\[
\lim_{n\to\infty}Q(a_n)=\frac{2}{1-\delta/\sqrt2}>2.
\]
Continuity therefore yields at least one \(c_{\delta,n}\in(a_n,B_n)\) with \(Q(c_{\delta,n})=2\) for all sufficiently large \(n\). These intervals are pairwise disjoint.

**Eventual uniqueness.** Uniformly for \(t=2\pi n+u\), \(u\in[5\pi/4,3\pi/2]\), we have \(\sin u\le-1/\sqrt2\), \(p(t)\ge1-\delta/\sqrt2>0\), and
\[
\ell(t)=t\frac{-\delta\sin u}{p(t)^2}+O_\delta(1),\qquad
\ell(t)\asymp_\delta t,\qquad \ell'(t)=O_\delta(t).
\]
The explicit correction satisfies, as \(z\to+\infty\),
\[
C_*(z)=2-\frac1{2z}+O(z^{-2}),\qquad C_*'(z)=O(z^{-2}).
\]
Differentiating \(Q\) and using these uniform bounds gives
\[
Q'(t)=\frac{2\delta\sin u}{(1+\delta\cos u)^2}+O_\delta(t^{-1}).
\]
The leading term is uniformly negative over the window, so \(Q'<0\) there for all sufficiently large \(n\). Thus the root in each such interval is unique.

**Asymptotic location.** The same derivative bound and \(Q(B_n)=2-O_\delta(B_n^{-1})\) show that \(B_n-c_{\delta,n}=O_\delta(B_n^{-1})\). Write \(t=B_n-a/B_n\) for bounded \(a\). Direct uniform Taylor expansion gives
\[
\frac{t+\delta\sin t}{t(1+\delta\cos t)}
=1+\frac{\delta(a-1)}{B_n}+O_\delta(B_n^{-2}),
\qquad
C_*(\ell(t))=2-\frac{1}{2\delta B_n}+O_\delta(B_n^{-2}).
\]
Consequently,
\[
Q(t)-2=\frac{2\delta(a-1)-1/(2\delta)}{B_n}+O_\delta(B_n^{-2}).
\]
The unique zero has \(a=1+1/(4\delta^2)+O_\delta(B_n^{-1})\), proving the stated formula.

**Global Newton comparison.** For \(x\ne0\), the mean-value theorem expresses \(f_\delta(x)=d_x x\) with \(d_x\in[1-\delta,1+\delta]\). Since \(f_\delta'(x)\) lies in the same interval, the ratio \(r_x=f_\delta(x)/(x f_\delta'(x))\) lies in \([\kappa^{-1},\kappa]\), where \(\kappa=(1+\delta)/(1-\delta)\). Hence the Newton update \(N(x)=x-f_\delta(x)/f_\delta'(x)\) satisfies
\[
\frac{|N(x)|}{|x|}=|1-r_x|\le\kappa-1=\frac{2\delta}{1-\delta}<1
\]
when \(\delta<1/3\). The root is unique by strict monotonicity, so convergence from every initial point follows. This does not assert convergence for every Halley-corrected initial point: the constructed exact cycles exclude it.

## Verification

The standalone file `verify_cycles.py` implements \(C_*\), the scalar iteration, endpoint bracketing, bisection, and the ordinary Newton comparison using only the Python standard library. Running `python verify_cycles.py` on the embedded original produced `PASS 142 finite tests; analytic asymptotics proved separately`. The tests include selected positive/negative cycle residuals, bounded-derivative values, Newton one-step contraction inequalities, and asymptotic location checks. All infinite statements, eventual monotonicity, and limit formulae above are justified analytically, not by finite computation. Floating-point bisection is not an exact root certificate.

## Relationship to prior work

Mukasa, *Third-order Halley-type iterative method with positive and bounded correction function* (arXiv:2609.08110v1; publicly submitted September 8, 2026), defines exactly \(C_*\) and proves its positivity, boundedness, local cubic convergence, and sufficient global-convergence conditions. The present claim does **not** challenge the stated sufficient conditions; it constructs globally monotone, analytic near-linear equations with infinitely many exceptional nonconvergent orbits. The source's introduction, construction and early theoretical sections were inspected directly; the later text was unavailable during this comparison, so absence of this particular theorem from the complete paper is not asserted.

Martin, *Root-finding: from Newton to Halley and beyond* (arXiv:2312.12305v1), discusses oscillations for Newton and a different positive correction on the equation \(\tanh x=0\), and turning-point issues. Its constructions neither concern Mukasa's bounded correction nor show that the same analytic equation has Newton global contraction while the bounded correction admits infinitely many distant cycles. An independently published mathematical-research record establishes the sharp derivative-sector frontier for **Newton** iteration, which supplies context but does not imply the claim for \(C_*\).

## Limitations

The two-cycles are proven to exist, but no stability classification beyond their exact period is established. Their locations escape to infinity as the derivative variation \(\delta\) decreases; the example is close to linear in the uniform derivative norm, **not** in a global second-derivative-to-error ratio. The result is restricted to the particular scalar correction \(C_*\) and does not contradict convergence theorems with stronger curvature or initial-neighborhood hypotheses. Priority beyond the directly inspected literature and database searches remains subject to additional historical checking. There is no independent mathematical audit.

## References

1. H. Mukasa, *Third-order Halley-type iterative method with positive and bounded correction function*, arXiv:2609.08110v1, September 8, 2026. https://arxiv.org/abs/2609.08110
2. R. J. Martin, *Root-finding: from Newton to Halley and beyond*, arXiv:2312.12305v1, December 19, 2023. https://arxiv.org/html/2312.12305v1
3. Published mathematical research record, *Sharp minimax relaxation frontier for scalar Newton under derivative-sector bounds*, public record identifier `46b773bf52ed` (used for statement-level overlap comparison only).
