# Sharp residual-monotonicity frontier for a prescribed two-coordinate Gauss–Seidel sweep

## Finding
Let
\[
A\in\mathbb R^{2\times2},
\qquad
A=A^{\mathsf T}>0,
\qquad
\kappa=\frac{\lambda_{\max}(A)}{\lambda_{\min}(A)}.
\]
Apply one exact forward Gauss–Seidel sweep in the prescribed order \(1\to2\) to
\[
Ax=b.
\]
If \(r^-\) and \(r^+\) denote the Euclidean residuals immediately before and after the completed sweep, then
\[
\sup_{\substack{A=A^{\mathsf T}>0\\\kappa_2(A)=\kappa}}
\ \sup_{r^-\ne0}
\frac{\|r^+\|_2}{\|r^-\|_2}
=
\max_{u\ge0}\sqrt{\Phi_\kappa(u)},
\]
where
\[
\Phi_\kappa(u)
=
\frac{(\kappa-1)^2u}{(\kappa+u)^2}
\left(
1+\frac{(\kappa-1)^2u}{(1+\kappa u)^2}
\right).
\]

There is a sharp universal residual-monotonicity frontier:
\[
\boxed{
\|r^+\|_2\le\|r^-\|_2
\text{ for every prescribed forward sweep}
\iff
1\le\kappa\le\kappa_*
}
\]
with
\[
\kappa_*
=
5.36076789614546\ldots.
\]
It is the unique root greater than one of
\[
32\kappa^6
-131\kappa^5
-144\kappa^4
-362\kappa^3
-144\kappa^2
-131\kappa
+32
=
0.
\]
Because this polynomial is reciprocal, writing
\[
x=\kappa+\kappa^{-1}
\]
reduces the frontier equation to
\[
32x^3-131x^2-240x-100=0.
\]

An exact witness above the frontier is
\[
A=
\begin{pmatrix}
5&2\\
2&2
\end{pmatrix},
\qquad
\kappa_2(A)=6,
\]
with initial residual
\[
r^-=
\begin{pmatrix}
2\\-5
\end{pmatrix}.
\]
After one forward sweep,
\[
r^+=
\begin{pmatrix}
29/5\\0
\end{pmatrix},
\]
so
\[
\frac{\|r^+\|_2}{\|r^-\|_2}
=
\frac{\sqrt{29}}5
>1.
\]

## Assumptions and scope
The theorem concerns exact arithmetic, one completed classical Gauss–Seidel sweep, a real \(2\times2\) SPD coefficient matrix, Euclidean residual norm, and a prescribed coordinate order. The initial residual is arbitrary and therefore represents every possible initial iterate and right-hand side.

No claim is made about the best of the two possible coordinate orderings, higher dimensions, randomized coordinate selection, symmetric Gauss–Seidel, SOR, asynchronous updates, or finite precision.

The condition number is the spectral condition number. Multiplying \(A\) by a positive scalar does not change either the condition number or the residual amplification operator for a complete sweep, so the spectral interval may be normalized to \([1,\kappa]\).

## Proof
Write
\[
A=
\begin{pmatrix}
a&c\\
c&b
\end{pmatrix},
\qquad
a>0,\quad b>0,\quad ab-c^2>0.
\]
Let
\[
r^-=
\begin{pmatrix}
r_1\\r_2
\end{pmatrix}.
\]
The first coordinate update adds
\[
\delta_1=\frac{r_1}{a}
\]
to the first component of the iterate. The intermediate residual is therefore
\[
\begin{pmatrix}
0\\
r_2-\frac{c}{a}r_1
\end{pmatrix}.
\]
The second update adds
\[
\delta_2
=
\frac1b
\left(
r_2-\frac{c}{a}r_1
\right)
\]
to the second component. Hence the completed residual is
\[
r^+
=
\begin{pmatrix}
-\dfrac{c}{b}
\left(
r_2-\dfrac{c}{a}r_1
\right)\\[1ex]
0
\end{pmatrix}.
\]
The exact residual-amplification operator norm for this matrix and order is thus
\[
\frac{|c|}{b}
\sqrt{
1+\frac{c^2}{a^2}
}.
\]

Normalize the two eigenvalues of \(A\) to \(1\) and \(\kappa\). After an orthogonal rotation, put
\[
u=\tan^2\theta\ge0.
\]
Then, up to the sign of \(c\),
\[
a=\frac{1+\kappa u}{1+u},
\qquad
b=\frac{\kappa+u}{1+u},
\qquad
|c|=\frac{(\kappa-1)\sqrt u}{1+u}.
\]
Substitution gives exactly
\[
\Phi_\kappa(u)
=
\frac{(\kappa-1)^2u}{(\kappa+u)^2}
\left(
1+\frac{(\kappa-1)^2u}{(1+\kappa u)^2}
\right).
\]

For \(\kappa>1\), the derivative of \(\Phi_\kappa\) has the sign of
\[
-H_\kappa(u),
\]
where
\[
H_\kappa(u)
=
\kappa^3u^4
-\kappa(\kappa-2)(\kappa^2+1)u^3
-3\kappa(\kappa-1)(\kappa+1)u^2
-(2\kappa-1)(\kappa^2+1)u
-\kappa.
\]
If \(1<\kappa<2\), the descending coefficient signs of \(H_\kappa\) are
\[
+,+,-,-,-,
\]
and if \(\kappa\ge2\) they are
\[
+,-,-,-,-.
\]
Descartes' rule of signs therefore gives exactly one positive zero. Since
\[
H_\kappa(0)=-\kappa<0
\]
and the leading coefficient is positive, \(\Phi_\kappa\) increases to one unique interior maximum and then decreases.

At the frontier this unique maximum is tangent to the level \(1\). Clearing positive denominators from
\[
\Phi_\kappa(u)=1
\]
and from
\[
\frac{\partial\Phi_\kappa}{\partial u}=0
\]
gives two quartic polynomials in \(u\). Direct polynomial elimination gives
\[
\operatorname{Res}_u
=
-\kappa^6(\kappa-1)^{20}(\kappa^2+\kappa+1)
\left(
32\kappa^6
-131\kappa^5
-144\kappa^4
-362\kappa^3
-144\kappa^2
-131\kappa
+32
\right).
\]
For \(\kappa>1\), only the last factor can vanish.

Dividing that reciprocal factor by \(\kappa^3\) and setting
\[
x=\kappa+\kappa^{-1}
\]
gives
\[
32x^3-131x^2-240x-100.
\]
On \(x\ge2\), this cubic first decreases and then increases to \(+\infty\), while its value at \(x=2\) is negative. Hence it has exactly one root \(x_*>2\), which yields exactly one root \(\kappa_*>1\). Since the maximal amplification is continuous in \(\kappa\), equals zero at \(\kappa=1\), and exceeds one at the explicit \(\kappa=6\) witness below, this unique tangency is the desired universal frontier.

For the witness
\[
A=
\begin{pmatrix}
5&2\\
2&2
\end{pmatrix},
\]
the trace and determinant are \(7\) and \(6\), so its eigenvalues are \(1\) and \(6\). With
\[
r^-=(2,-5)^{\mathsf T},
\]
the first update uses \(\delta_1=2/5\), producing the intermediate second residual
\[
-5-2(2/5)=-29/5.
\]
The second update uses
\[
\delta_2=-29/10.
\]
The final residual is therefore
\[
r^+=(29/5,0)^{\mathsf T},
\]
which gives the stated factor \(\sqrt{29}/5>1\).

## Verification
The embedded `verify.py` uses only the Python standard library. It verifies the exact rational witness, isolates the unique root \(\kappa_*>1\) of the reciprocal degree-six polynomial, checks the equivalent cubic in \(\kappa+\kappa^{-1}\), and numerically maximizes the closed one-variable expression on both sides of the frontier.

These computations corroborate the algebraic threshold. The universal reduction to \(\Phi_\kappa\), the uniqueness of its positive stationary point, and the implication from the resultant are proved analytically above.

## Relationship to prior work
Gauss–Seidel on an SPD system is cyclic exact coordinate descent for the associated strictly convex quadratic. Modern coordinate-descent literature therefore analyzes the same update from optimization and numerical-linear-algebra viewpoints.

Hefny, Needell, and Ramdas explicitly write the SPD coordinate-descent update
\[
x_{t+1}
=
x_t+
\frac{b_i-A^ix_t}{A_{ii}}e_i
\]
and identify randomized Gauss–Seidel with randomized coordinate descent. Their analysis emphasizes expected convergence in energy- or least-squares-related quantities; it does not state a sharp deterministic one-sweep Euclidean residual amplification frontier.

Later worst-case cyclic-coordinate-descent work studies asymptotic or epochwise convergence rates and the effect of update ordering. Those results motivate order-sensitive analysis but do not give the displayed residual-norm threshold.

A closely related published two-coordinate result gives a sharp Euclidean *solution-error* transient bound for choosing between the two Gauss–Seidel orderings. That statement does not imply the present theorem: the residual is \(Ae\), the norm is different, and the present claim fixes a prescribed order rather than optimizing over the two orders. Targeted searches for residual-norm amplification, condition-number frontiers, and two-dimensional SPD Gauss–Seidel found no implication-equivalent statement.

## Limitations
The coordinate order is prescribed. Permuting the two coordinates can substantially change the residual amplification for a particular matrix, and this theorem does not optimize over that choice.

The theorem is two-dimensional. It does not claim that the same threshold controls higher-dimensional cyclic sweeps.

The result concerns one completed sweep. It does not contradict classical convergence of Gauss–Seidel for SPD matrices or monotonic decrease of the quadratic objective in exact coordinate descent.

The originality search leaves a residual risk that older matrix-iterative-analysis literature may encode the same one-sweep Euclidean residual norm calculation without modern coordinate-descent terminology.

## References
1. A. Hefny, D. Needell, and A. Ramdas, “Rows vs. Columns: Randomized Kaczmarz or Gauss-Seidel for Ridge Regression,” arXiv:1507.05844v1, submitted July 21, 2015; later SIAM Journal on Scientific Computing 39 (2017), S528–S542. DOI 10.1137/16M1077891.
2. P. Xiao, Z. Xiao, and R. Sun, “Two Symmetrized Coordinate Descent Methods Can Be \(O(n^2)\) Times Slower Than the Randomized Version,” SIAM Journal on Optimization 31 (2021), 2726–2752. DOI 10.1137/19M1292473.
