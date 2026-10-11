# Exact Carathéodory–Fejér constant for the three lowest odd harmonics
## Finding
Define
\[
M_{135}=\sup\left\{a\in\mathbb R:\exists b,c\in\mathbb R,\ 1+a\cos\theta+b\cos(3\theta)+c\cos(5\theta)\ge0\ \text{for every }\theta\in\mathbb R\right\}.
\]
Then
\[
M_{135}=\frac{1+\sqrt2}{2}.
\]
The extremizer is unique. Its coefficients are
\[
a=\frac{1+\sqrt2}{2},\qquad b=\frac{2-3\sqrt2}{8},\qquad c=\frac{2-\sqrt2}{8}.
\]
Equivalently, if \(\psi\) is a real positive-definite sequence on \(\mathbb Z\), normalized by \(\psi(0)=1\) and supported in \(\{0,\pm1,\pm3,\pm5\}\), then
\[
\psi(1)\le\frac{1+\sqrt2}{4},
\]
and equality determines the even sequence uniquely.

## Assumptions and scope
Only real coefficients are considered, exactly as in the real Carathéodory–Fejér problem. The allowed nonconstant frequencies are \(1,3,5\); coefficients at \(3\) and \(5\) may vanish. Nonnegativity is required for every real \(\theta\), not only on a finite grid. The positive-definite formulation follows from the Herglotz correspondence for finitely supported sequences, with cosine coefficient \(a\) corresponding to \(2\psi(1)\).

## Proof
Write
\[
Q(\theta)=a\cos\theta+b\cos(3\theta)+c\cos(5\theta).
\]
Because all three frequencies are odd,
\[
Q(\pi-\theta)=-Q(\theta).
\]
Thus \(1+Q(\theta)\ge0\) for every \(\theta\) implies \(-1\le Q(\theta)\le1\) for every \(\theta\).

At \(\theta=0\),
\[
a+b+c\le1.
\]
At \(\theta=\pi/4\), since \(\cos(\pi/4)=1/\sqrt2\) and \(\cos(3\pi/4)=\cos(5\pi/4)=-1/\sqrt2\),
\[
\frac{a-b-c}{\sqrt2}\le1.
\]
Adding the two inequalities gives
\[
2a\le1+\sqrt2,
\]
so \(a\le(1+\sqrt2)/2\).

For equality, both displayed pointwise inequalities must be equalities. Hence an extremizer has
\[
Q(0)=Q(\pi/4)=1.
\]
Since \(\pi/4\) is an interior maximum point of the differentiable function \(Q\), also \(Q'(\pi/4)=0\). These three linear conditions are
\[
a+b+c=1,\qquad \frac{a-b-c}{\sqrt2}=1,\qquad a+3b-5c=0,
\]
and have the unique solution
\[
a=\frac{1+\sqrt2}{2},\qquad b=\frac{2-3\sqrt2}{8},\qquad c=\frac{2-\sqrt2}{8}.
\]
It remains to verify admissibility. Put \(x=\cos\theta\), \(r=1/\sqrt2\), and let \(Q_*(x)\) denote the resulting odd polynomial after using \(\cos(3\theta)=4x^3-3x\) and \(\cos(5\theta)=16x^5-20x^3+5x\). Direct expansion gives
\[
1-Q_*(x)=(4-2\sqrt2)(1-x)(x-r)^2\left(x^2+(1+\sqrt2)x+1+\frac{\sqrt2}{2}\right).
\]
The quadratic factor has discriminant \(-1\), so it is positive for every real \(x\). Hence \(1-Q_*(x)\ge0\) on \([-1,1]\). Since \(Q_*\) is odd, \(1+Q_*(x)=1-Q_*(-x)\ge0\) there as well. Therefore \(|Q_*|\le1\), so \(1+Q_*\ge0\), proving attainment. The equality conditions above also prove uniqueness.

## Verification
The standalone checker `verify.py` performs exact arithmetic in \(\mathbb Q(\sqrt2)\). It verifies the three contact equations, the exact factorization of \(1-Q_*\), and the discriminant \(-1\) of the remaining quadratic. It additionally samples \(20001\) points as a nonessential numerical corroboration. The exact factorization, not the sampling, proves global nonnegativity.

## Relationship to prior work
Kolountzakis and Révész formulate the Carathéodory–Fejér-type problem for prescribed higher-frequency sets and prove its equivalence with pointwise positive-definite extremal problems. Their 2003 paper records exact values for interval supports, singleton higher supports, complements of singletons, and the full odd or full even higher-frequency sets, but not the finite higher-frequency set \(\{3,5\}\). Krenedits and Révész later extend the reduction framework to arbitrary locally compact Abelian groups and emphasize that exact calculation for a specified support remains a separate extremal problem.

The present support is incomparable with the previously evaluated support \(\{1,2,5\}\) and with the family \(\{1,2,n\}\); neither statement implies the value here. Current semantic searches also found nearby exact results for supports corresponding to higher-frequency sets \(\{2,4\}\), \(\{3,4\}\), and the isolated third harmonic, but no result for \(\{3,5\}\).

## Limitations
This result is only for the continuous real problem with the three frequencies \(1,3,5\). It does not determine the corresponding discretized cyclic-grid extremum, complex-coefficient variants with a different normalization, or a general formula for arbitrary two-element higher-frequency sets. A residual literature risk is that the same constant may appear in older cosine-polynomial literature under a dual or differently indexed formulation; targeted searches and the inspected primary sources did not reveal such a statement.

## References
1. M. N. Kolountzakis and Sz. Gy. Révész, “On pointwise estimates of positive definite functions with given support,” arXiv:math/0302193v1, first public 2003-02-17; later Canadian Journal of Mathematics 58 (2006), 401–418.
2. S. Krenedits and Sz. Gy. Révész, “The Carathéodory–Fejér type extremal problem on locally compact Abelian groups,” arXiv:1304.0071v1, first public 2013-03-30.
