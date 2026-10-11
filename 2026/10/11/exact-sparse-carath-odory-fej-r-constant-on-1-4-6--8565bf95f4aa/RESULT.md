# Exact sparse Carathéodory–Fejér constant on \(\{1,4,6\}\)
## Finding
Define
\[
\mathcal M_{4,6}=\sup\left\{a\in\mathbb R:\exists b,c\in\mathbb R,\ 1+a\cos\theta+b\cos(4\theta)+c\cos(6\theta)\ge 0\ \text{for every }\theta\in\mathbb R\right\}.
\]
Then
\[
\boxed{\mathcal M_{4,6}=\frac{\sqrt5}{2}}.
\]
The extremizer is unique. Its coefficients are
\[
a_*=\frac{\sqrt5}{2},\qquad b_*=\frac{7\sqrt5-12}{20},\qquad c_*=\frac{3\sqrt5-8}{20}.
\]
Equivalently, for real even positive-definite sequences \(\psi:\mathbb Z\to\mathbb R\) with \(\psi(0)=1\) and support contained in \(\{0,\pm1,\pm4,\pm6\}\), the sharp bound is \(\psi(1)\le\sqrt5/4\), with a unique extremal sequence.

## Assumptions and scope
The polynomial is required to be nonnegative at every real angle, not merely on a finite grid. Coefficients are real, and only harmonics \(1\), \(4\), and \(6\) are allowed. The result does not assert a formula for arbitrary pairs of higher harmonics or for sampled cyclic variants.

## Proof
Let
\[
T(\theta)=1+a\cos\theta+b\cos(4\theta)+c\cos(6\theta)
\]
be nonnegative. Evaluating at \(\theta=\pi\) gives
\[
1-a+b+c\ge0,
\]
so \(b+c\ge a-1\).

Now put
\[
r=\cos\left(\frac{4\pi}{5}\right)=-\frac{1+\sqrt5}{4}.
\]
At \(\theta=4\pi/5\), all three cosine factors are equal to \(r\), hence
\[
1+r(a+b+c)\ge0.
\]
Because \(r<0\), this is
\[
a+b+c\le-\frac1r=\sqrt5-1.
\]
On the other hand \(a+b+c\ge2a-1\). Therefore
\[
2a-1\le\sqrt5-1,
\]
which proves \(a\le\sqrt5/2\).

Suppose equality holds. Then both preceding inequalities are equalities, so
\[
b+c=a-1
\]
and \(T(4\pi/5)=0\). Since a nonnegative differentiable trigonometric polynomial has zero derivative at any zero, \(T'(4\pi/5)=0\). Writing \(s=\sin(\pi/5)>0\), one has
\[
\sin\left(\frac{4\pi}{5}\right)=s,\qquad
\sin\left(\frac{16\pi}{5}\right)=-s,\qquad
\sin\left(\frac{24\pi}{5}\right)=s,
\]
so the derivative condition is
\[
-a+4b-6c=0.
\]
Together with \(b+c=a-1\) and \(a=\sqrt5/2\), this forces
\[
b=\frac{7\sqrt5-12}{20},\qquad c=\frac{3\sqrt5-8}{20}.
\]
Thus there can be at most one extremizer.

It remains to prove that these coefficients are feasible. Put \(x=\cos\theta\), and let \(T_k\) denote the Chebyshev polynomial characterized by \(T_k(\cos\theta)=\cos(k\theta)\). For the displayed coefficients, direct exact expansion gives
\[
1+a_*x+b_*T_4(x)+c_*T_6(x)=(x+1)(x-r)^2R(x),
\]
where
\[
R(x)=\frac{24\sqrt5-64}{5}x^3+\frac{36-4\sqrt5}{5}x^2+\frac{9-15\sqrt5}{5}x+\frac{14-2\sqrt5}{5}.
\]
Its derivative is a quadratic with negative leading coefficient, because \(3\sqrt5<8\), and discriminant
\[
\Delta=\frac{32}{25}\left(1063-477\sqrt5\right)<0.
\]
The last inequality follows exactly from \(1063^2-5\cdot477^2=-7676<0\). Hence \(R'(x)<0\) for every real \(x\). Also
\[
R(1)=-1+\frac{3\sqrt5}{5}>0.
\]
Therefore \(R(x)>0\) throughout \([-1,1]\), while \(x+1\ge0\) and \((x-r)^2\ge0\). The factorization proves nonnegativity for every \(\theta\), so the upper bound is attained. The equality argument above proves uniqueness.

## Verification
The accompanying `verify_exact.py` reconstructs the Chebyshev polynomial symbolically, checks the two equality constraints, verifies the exact factorization, computes the derivative discriminant, and checks the integer inequalities used to certify its sign. These algebraic checks reproduce the critical identities in the proof; they are not a substitute for the universal sign argument given above.

## Relationship to prior work
Krenedits and Révész formulate the Carathéodory–Fejér extremal quantity for prescribed Fourier support on locally compact Abelian groups and recover the classical circle problem as a special case. Their framework contains the present optimization problem but does not supply the support-specific value above. Nearby exact sparse cases with different higher-frequency sets, as well as a qualitative criterion deciding when adding one higher harmonic leaves a singleton optimum unchanged, do not imply the value for \(\{1,4,6\}\): for the pair \((4,6)\), that criterion only yields the strict inequality \(\mathcal M_{4,6}>\sec(\pi/8)\).

The positive-definite-sequence formulation follows from the standard correspondence between a real even positive-definite sequence supported on \(\{0,\pm1,\pm4,\pm6\}\) and its nonnegative trigonometric polynomial. Kolountzakis and Révész provide broader positive-definite extremal context, but their Turán objective is different from maximizing one Fourier coefficient.

## Limitations
The theorem is support-specific. It does not classify \(\mathcal M_{m,n}\) for general \((m,n)\), does not address complex nonsymmetric coefficients, and does not determine finite-grid analogues. Literature searches did not reveal an implication-equivalent published formula for this support, but older sparse-positive-polynomial literature could use substantially different notation; that residual originality risk remains.

## References
1. G. Krenedits and Sz. Gy. Révész, *The Carathéodory-Fejér type extremal problem on locally compact Abelian groups*, arXiv:1304.0071v1, first public 2013-03-30; primary MSC 43A35, 43A70.
2. M. N. Kolountzakis and Sz. Gy. Révész, *Turán's extremal problem for positive definite functions on groups*, arXiv:math/0312218v1, first public 2003-12-10; primary MSC 43A35.
