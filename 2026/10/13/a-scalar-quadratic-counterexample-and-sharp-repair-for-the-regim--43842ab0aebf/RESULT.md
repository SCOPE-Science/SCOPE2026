# A scalar-quadratic counterexample and sharp repair for the Regime-0 KGD lower bound
## Finding

For Kahan's Regime-0 automatic step in Meng--Shen--Xue--Zhang, Definition 2.1 is
\[
\mathcal K_0(x;x,\Delta\tau)
=
\frac{\Delta\tau}
{\sqrt{
3+
\frac{24\left(f(x_{\rm new})-f(x)\right)}
{\Delta\tau\left(
\|G(x)+G(x_{\rm new})\|_2^2+4\|G(x)\|_2^2
\right)}
}},
\]
where
\[
x_{\rm new}=x-\Delta\tau G(x).
\]

Lemma 4.2 of arXiv:2508.06002v1 claims
\[
\mathcal K_0(x;x,\Delta\tau)
\ge
\frac{2}{\sqrt{12\xi L+3\Lambda_1}},
\]
where \(\xi\) bounds the gradient on the relevant sublevel set, \(L\) is a Hessian Lipschitz constant, and \(\Lambda_1\) is the source's upper Hessian Rayleigh bound.

That lower bound is false as stated. Take
\[
f(x)=2x^2,
\qquad
x_0=x=1,
\qquad
\Delta\tau=\frac12.
\]
Then the sublevel set is
\[
\Omega=[-1,1],
\]
the gradient and Hessian are
\[
G(x)=4x,
\qquad
H(x)=4,
\]
and valid source constants are
\[
\xi=4,
\qquad
\Lambda_1=4,
\qquad
L=\frac1{100}.
\]
The constant Hessian is Lipschitz with every positive \(L\), so this choice is admissible.

The trial point is
\[
x_{\rm new}=-1,
\]
hence
\[
f(x_{\rm new})-f(x)=0
\]
and Definition 2.1 gives
\[
\mathcal K_0(1;1,1/2)=\frac{1}{2\sqrt3}.
\]
The claimed lower bound instead equals
\[
\frac{2}{\sqrt{12(4)(1/100)+3(4)}}=\frac{5}{\sqrt{78}}.
\]
Squaring both positive quantities shows
\[
\frac1{12}<\frac{25}{78},
\]
so
\[
\frac{1}{2\sqrt3}<\frac{5}{\sqrt{78}}.
\]
Thus Lemma 4.2 fails even on a one-dimensional strongly convex quadratic whose whole trial segment remains inside the source sublevel set.

A correct replacement is obtained by using an operator-norm Hessian bound on the trial segment. If
\[
B\ge\sup_{z\in[x,x_{\rm new}]}\|H(z)\|_2,
\]
the Hessian is \(L\)-Lipschitz on that segment, and
\[
\|G(x)\|_2\le\xi,
\]
then
\[
\mathcal K_0(x;x,\Delta\tau)
\ge
\frac{2}{\sqrt{12\xi L+3B^2}}.
\]
In the positive-semidefinite case with
\[
H(z)\preceq\Lambda_1 I
\]
along the trial segment, one may take
\[
B=\Lambda_1,
\]
so the curvature contribution becomes
\[
3\Lambda_1^2
\]
rather than
\[
3\Lambda_1.
\]

The square is not a proof artifact. For the scalar quadratic
\[
f(x)=\frac{\lambda}{2}x^2
\]
with \(\lambda>0\), set
\[
z=\lambda\Delta\tau.
\]
A direct substitution gives
\[
\mathcal K_0(x;x,\Delta\tau)
=
\frac{1}{\lambda\sqrt3}
\sqrt{(z-2)^2+4}.
\]
Its minimum over \(z>0\) is
\[
\frac{2}{\sqrt3\,\lambda},
\]
attained at
\[
z=2.
\]
With the natural Hessian Lipschitz constant \(L=0\) and \(B=\lambda\), the repaired bound is exactly this value. Hence the \(B^2\) scaling is sharp on the quadratic subclass.

## Assumptions and scope

The counterexample uses exactly the Regime-0 step in Definition 2.1 and the constants permitted by Assumption 4.1 of arXiv:2508.06002v1. It does not rely on a large-dimensional construction or a limiting argument.

The repaired estimate assumes an operator-norm bound \(B\) on the Hessian along the trial segment. This is the quantity required to control the squared gradient difference. If the Hessian is positive semidefinite along that segment and the source Rayleigh upper bound is available there, then \(B\le\Lambda_1\).

For a general nonconvex Hessian, a one-sided inequality
\[
v^\top H(z)v\le\Lambda_1\|v\|_2^2
\]
does not control \(\|H(z)\|_2\); a separate operator-norm bound is needed.

No claim is made that the paper's global or local convergence theorems are false. The finding concerns the standalone lower bound of Lemma 4.2 and the corresponding proof step.

## Proof

Write
\[
g=G(x),
\qquad
g_+=G(x_{\rm new}),
\qquad
D=\|g+g_+\|_2^2+4\|g\|_2^2.
\]
The source's algebra rewrites the denominator of \(\mathcal K_0\) through
\[
A=
f(x_{\rm new})-f(x)+\frac{\Delta\tau}{8}D.
\]

The trapezoidal-gradient remainder satisfies
\[
\left|
f(x_{\rm new})-f(x)
-\frac12(g+g_+)^\top(x_{\rm new}-x)
\right|
\le
\frac{L}{2}\Delta\tau^3\|g\|_2^3.
\]
Also,
\[
\frac{\Delta\tau}{8}D
-\frac12(g+g_+)^\top(x_{\rm new}-x)
=
\frac{\Delta\tau}{8}\|g_+-g\|_2^2.
\]
If the trial segment has
\[
\|H(z)\|_2\le B,
\]
then the mean-value integral gives
\[
\|g_+-g\|_2
\le
B\Delta\tau\|g\|_2.
\]
Consequently,
\[
|A|
\le
\left(
\frac{\xi L}{2}+\frac{B^2}{8}
\right)
\Delta\tau^3\|g\|_2^2.
\]

For a trial where \(\mathcal K_0\) is real, the denominator after the source rearrangement is \(\sqrt{24A}\). Since
\[
D\ge4\|g\|_2^2,
\]
one obtains
\[
\mathcal K_0
=
\frac{\Delta\tau\sqrt{\Delta\tau D}}{\sqrt{24A}}
\ge
\frac{2}{\sqrt{12\xi L+3B^2}}.
\]

The source proof instead replaces
\[
\|g_+-g\|_2^2
\]
by a term proportional to \(\Lambda_1\Delta\tau^2\|g\|_2^2\). Under the stated Rayleigh bound, the natural estimate in the positive-semidefinite case is proportional to
\[
\Lambda_1^2\Delta\tau^2\|g\|_2^2.
\]
The scalar counterexample demonstrates that dropping this square changes a true scale into a false one.

For the sharp scalar formula, with
\[
f(x)=\frac{\lambda}{2}x^2
\]
and \(z=\lambda\Delta\tau\), the trial point is
\[
x_{\rm new}=(1-z)x.
\]
Substituting
\[
f(x_{\rm new})-f(x)
=
\frac{\lambda x^2}{2}\left((1-z)^2-1\right)
\]
and
\[
\|G(x)+G(x_{\rm new})\|_2^2+4\|G(x)\|_2^2
=
\lambda^2x^2\left((2-z)^2+4\right)
\]
into Definition 2.1 reduces the square-root denominator to
\[
\frac{\sqrt3\,z}{\sqrt{(z-2)^2+4}}.
\]
This yields the exact formula above, whose minimum is immediate.

## Verification

The standalone script `artifacts/verify_k0_lower_bound.py` checks the counterexample using exact rational arithmetic where possible, verifies the strict failure of the published bound, and checks the scalar closed form against Definition 2.1 for representative positive curvatures and trial steps.

The analytic proof establishes the universal repaired estimate under its stated segment assumptions. The finite script is only a replay of the algebra and the explicit witness.

## Relationship to prior work

The primary source introduces the Regime-0 KGD step in Definition 2.1, states Assumption 4.1, proves finite line-search termination in Lemma 4.1, and states the disputed uniform lower bound in Lemma 4.2. Its displayed proof of Lemma 4.2 contains the curvature term that the scalar quadratic contradicts.

Targeted searches using the paper identifier, the lemma number, the exact lower-bound structure, KGD and Regime-0 terminology, scalar quadratic counterexamples, and Hessian-norm-square repairs did not locate a published correction or an equivalent counterexample.

The source itself analyzes strongly convex quadratics primarily through the Regime-1 KGD/Barzilai--Borwein equivalence. The present scalar quadratic is instead used as a diagnostic for the Regime-0 safeguard formula that Algorithm 1 employs during its inner globalization step.

## Limitations

The finding does not show failure of Algorithm 1, Theorem 4.1, or Theorem 4.2. In the displayed proof of Theorem 4.1, finite acceptance is obtained from Lemma 4.1, not from the false numerical lower bound.

The repaired estimate requires a Hessian operator-norm bound on the actual trial segment. Under nonconvexity, the source's one-sided Rayleigh upper bound alone is insufficient for this purpose.

No statement is made about whether the authors intended \(\Lambda_1\) to denote a different, stronger constant than the one explicitly introduced in Assumption 4.1.

## References

1. Y. Meng, C. Shen, L. Xue, L.-H. Zhang, *Kahan's Automatic Step-Size Control for Unconstrained Optimization*, arXiv:2508.06002v1, first public 8 August 2025.
