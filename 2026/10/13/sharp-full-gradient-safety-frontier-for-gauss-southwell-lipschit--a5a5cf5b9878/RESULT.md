# Sharp full-gradient safety frontier for Gauss–Southwell–Lipschitz coordinate minimization

## Finding
Consider the strictly convex quadratic
\[
f(x)
=
\frac12x^{\mathsf T}Ax-b^{\mathsf T}x,
\qquad
A=
\begin{pmatrix}
a&c\\
c&b_2
\end{pmatrix}
=A^{\mathsf T}>0.
\]
Let
\[
g=\nabla f(x).
\]
The Gauss–Southwell–Lipschitz rule chooses
\[
i\in
\operatorname*{arg\,max}_{j\in\{1,2\}}
\frac{|g_j|}{\sqrt{A_{jj}}},
\]
and exact coordinate minimization then sets
\[
x^+
=
x-\frac{g_i}{A_{ii}}e_i.
\]
For a quadratic,
\[
f(x)-f(x^+)
=
\frac{g_i^2}{2A_{ii}},
\]
so this is exactly the coordinate giving the largest immediate objective decrease.

Define
\[
\delta_*
=
\sqrt{\frac{97-26\sqrt{13}}{27}}
\]
and
\[
\kappa_*
=
\frac{1+\delta_*}{1-\delta_*}
=
2.0639445610119587707\ldots.
\]
Equivalently, \(\kappa_*\) is the unique real root greater than one of
\[
9\kappa^4+\kappa^3-43\kappa^2+\kappa+9=0.
\]

Then
\[
\boxed{
\kappa_2(A)\le\kappa_*
\quad\Longrightarrow\quad
\|\nabla f(x^+)\|_2
\le
\|\nabla f(x)\|_2
}
\]
for every point \(x\) and every allowed GSL tie-breaking.

The threshold is sharp. For every
\[
\kappa>\kappa_*,
\]
there is a \(2\times2\) SPD quadratic of condition number exactly \(\kappa\) and a point at which the GSL choice is unique but
\[
\|\nabla f(x^+)\|_2
>
\|\nabla f(x)\|_2.
\]

For a fixed matrix, if coordinate \(1\) is selected, put
\[
q=\frac{|c|}{a},
\qquad
s=\sqrt{\frac{b_2}{a}}.
\]
Then the exact fixed-matrix criterion is
\[
\boxed{
\text{every GSL-admissible update of coordinate \(1\) is gradient-norm nonexpansive}
\iff
q^2+2qs\le1.
}
\]

A rational witness is
\[
A=
\begin{pmatrix}
1&1/2\\
1/2&1
\end{pmatrix},
\qquad
g=
\begin{pmatrix}
1\\
-9/10
\end{pmatrix}.
\]
The eigenvalues of \(A\) are \(1/2\) and \(3/2\), so
\[
\kappa_2(A)=3.
\]
GSL uniquely selects coordinate \(1\), and exact minimization gives
\[
g^+
=
\begin{pmatrix}
0\\
-7/5
\end{pmatrix}.
\]
Therefore
\[
\frac{\|g^+\|_2^2}{\|g\|_2^2}
=
\frac{196}{181}>1,
\]
while the objective decreases by exactly
\[
\frac12.
\]

## Assumptions and scope
The result concerns exact arithmetic, two real coordinates, a strictly convex quadratic, the single-coordinate GSL selection rule, and exact coordinate minimization.

The monitored quantity is the Euclidean norm of the complete gradient after one coordinate update. This differs from the objective value, which always decreases under exact coordinate minimization, and from the selected partial derivative, which becomes exactly zero.

The theorem is a complete robust classification in dimension two. It does not claim the same threshold in dimensions three or larger, for block GSL rules, for approximate coordinate minimization, for proximal composite objectives, or for inexact coordinate Lipschitz constants.

## Proof
Assume coordinate \(1\) is selected. If
\[
g_1=0,
\]
then GSL admissibility forces
\[
g_2=0,
\]
so there is nothing to prove. Hence suppose
\[
g_1\ne0.
\]

Write
\[
r=\frac{g_2}{g_1},
\qquad
q=\frac{|c|}{a},
\qquad
s=\sqrt{\frac{b_2}{a}}.
\]
The GSL selection condition is
\[
\frac{|g_1|}{\sqrt a}
\ge
\frac{|g_2|}{\sqrt{b_2}},
\]
equivalently
\[
|r|\le s.
\]

Exact minimization of coordinate \(1\) gives
\[
g^+
=
g-\frac{g_1}{a}Ae_1
=
\begin{pmatrix}
0\\
g_2-\frac ca g_1
\end{pmatrix}.
\]
Therefore
\[
\frac{\|g^+\|_2^2}{\|g\|_2^2}
=
\frac{(r-c/a)^2}{1+r^2}.
\]
For fixed \(|r|\), the largest value is obtained when \(r\) has sign opposite to \(c\), so gradient-norm nonexpansion for every GSL-admissible \(r\) is equivalent to
\[
(|r|+q)^2\le1+r^2
\]
for every
\[
0\le|r|\le s.
\]
After cancellation this becomes
\[
q^2+2q|r|\le1.
\]
The left-hand side increases with \(|r|\), proving the fixed-matrix criterion
\[
q^2+2qs\le1.
\]

It remains to determine the smallest condition number at which this criterion can fail. Scale the matrix so that
\[
a=1.
\]
Then
\[
A=
\begin{pmatrix}
1&\pm q\\
\pm q&s^2
\end{pmatrix},
\qquad
s^2>q^2.
\]
Define the spectral spread parameter
\[
\delta
=
\frac{\kappa_2(A)-1}{\kappa_2(A)+1}.
\]
For a real symmetric \(2\times2\) matrix,
\[
\delta^2
=
\frac{(1-s^2)^2+4q^2}{(1+s^2)^2}.
\]

Put
\[
u=q^2,
\qquad
y=s^2.
\]
For fixed \(u\),
\[
\delta^2(u,y)
=
\frac{(1-y)^2+4u}{(1+y)^2},
\]
and
\[
\frac{\partial}{\partial y}\delta^2(u,y)
=
\frac{4(y-1-2u)}{(1+y)^3}.
\]
Thus the unconstrained minimum in \(y\) occurs at
\[
y=1+2u.
\]

The unsafe region is
\[
u+2\sqrt{uy}>1.
\]
For
\[
0<u<\frac13,
\]
its boundary is
\[
y_0(u)
=
\frac{(1-u)^2}{4u}.
\]
If
\[
0<u\le\frac17,
\]
then
\[
y_0(u)\ge1+2u,
\]
so the smallest spectral spread compatible with unsafe behavior is attained on the boundary \(y=y_0(u)\). Substitution gives
\[
\phi(u)
=
\frac{u^3+51u^2-13u+1}{(1+u)^3}.
\]
Its derivative is
\[
\phi'(u)
=
-\frac{16(3u^2-8u+1)}{(1+u)^4}.
\]
The unique critical point in
\[
\left(0,\frac17\right)
\]
is
\[
u_*
=
\frac{4-\sqrt{13}}{3},
\]
and it is the minimum. There,
\[
\phi(u_*)
=
\frac{97-26\sqrt{13}}{27}.
\]

For
\[
u\ge\frac17,
\]
the unconstrained minimizer \(y=1+2u\) is feasible for the unsafe region, and the resulting minimum is
\[
\frac{u}{1+u}
\ge
\frac18.
\]
Because
\[
\frac{97-26\sqrt{13}}{27}
<
\frac18,
\]
the global onset of unsafe behavior is exactly
\[
\delta_*^2
=
\frac{97-26\sqrt{13}}{27}.
\]
Converting
\[
\delta=\frac{\kappa-1}{\kappa+1}
\]
gives the stated \(\kappa_*\). Eliminating the radicals yields
\[
9\kappa_*^4+\kappa_*^3-43\kappa_*^2+\kappa_*+9=0.
\]

Sharpness for every larger condition number follows from the same construction. Fix
\[
q_*=\sqrt{u_*}
\]
and let \(s_*\) be the boundary value satisfying
\[
q_*^2+2q_*s_*=1.
\]
Since
\[
u_*<\frac17,
\]
one has
\[
s_*^2>1+2u_*.
\]
Therefore
\[
\delta(q_*,s)
\]
is strictly increasing for
\[
s\ge s_*,
\]
starting at \(\delta_*\) and tending to \(1\) as \(s\to\infty\). Hence every
\[
\delta>\delta_*
\]
is attained by a unique \(s>s_*\), where
\[
q_*^2+2q_*s>1.
\]
Choosing a gradient ratio with sign opposite to \(c\) and magnitude slightly below \(s\) makes coordinate \(1\) the unique GSL choice while preserving strict gradient amplification.

The coordinate-\(2\) case is identical after swapping indices.

## Verification
The embedded `verify.py` checks the exact rational condition-\(3\) witness, including the GSL selection, exact coordinate minimization, objective decrease, and gradient-norm amplification.

It also checks to high precision that
\[
u_*=\frac{4-\sqrt{13}}3
\]
satisfies
\[
3u_*^2-8u_*+1=0,
\]
that
\[
\delta_*^2
=
\frac{97-26\sqrt{13}}{27},
\]
that the resulting
\[
\kappa_*
=
\frac{1+\delta_*}{1-\delta_*}
\]
satisfies
\[
9\kappa_*^4+\kappa_*^3-43\kappa_*^2+\kappa_*+9=0,
\]
and that representative matrices on both sides of the frontier obey the predicted fixed-matrix criterion.

Finite replay is supporting evidence only. The universal threshold is established by the analytic minimization in the proof.

## Relationship to prior work
Nesterov develops coordinate-descent methods and analyzes progress from partial updates, placing the subject under primary MSC \(90C25\). His coordinate-descent framework and objective-decrease analysis are prior work.

Nutini, Schmidt, Laradji, Friedlander, and Koepke introduce the Gauss–Southwell–Lipschitz rule
\[
i_k
=
\operatorname*{arg\,max}_i
\frac{|\nabla_i f(x^k)|}{\sqrt{L_i}},
\]
and show that for quadratic functions it is the optimal myopic coordinate update: together with exact coordinate minimization it chooses the coordinate and step producing the largest immediate objective decrease. Those facts are prior work.

The finding here concerns a different diagnostic: monotonicity of the Euclidean norm of the complete gradient after that locally optimal coordinate update. The full GSL paper was inspected around its exact-optimization and GSL sections; targeted full-text searches found no gradient-norm monotonicity or condition-number classification.

The closest published comparison located by semantic search concerns Euclidean transient amplification after a complete prescribed two-coordinate Gauss–Seidel sweep. That theorem studies solution error after two sequential updates and coordinate ordering. It does not imply the one-coordinate full-gradient criterion here.

Targeted searches under GSL, myopic coordinate selection, exact coordinate minimization, full-gradient norm, gradient monotonicity, and condition number did not locate the threshold
\[
\kappa_*
=
2.0639445610119587707\ldots
\]
or the fixed-matrix condition
\[
q^2+2qs\le1.
\]

## Limitations
The sharp classification is two-dimensional. Higher-dimensional GSL updates couple the selected coordinate to several unselected gradient components, so a separate analysis is required.

The result assumes exact knowledge of the coordinate Lipschitz constants
\[
L_i=A_{ii}
\]
and exact coordinate minimization. Approximate GSL rules and inexact line minimization can have different frontiers.

The gradient norm is a stationarity diagnostic, not the objective. The objective decreases at every step by construction, so no contradiction with coordinate-descent convergence theory is implied.

Older coordinate-relaxation literature is extensive. A differently phrased two-dimensional full-gradient observation may exist outside the inspected sources; this remains the main originality risk.

## References
1. Yu. Nesterov, “Efficiency of coordinate descent methods on huge-scale optimization problems,” Optimization Online, posted 2010-01-22; later SIAM Journal on Optimization 22 (2012), 341–362. DOI 10.1137/100802001.
2. J. Nutini, M. Schmidt, I. H. Laradji, M. P. Friedlander, and H. Koepke, “Coordinate Descent Converges Faster with the Gauss-Southwell Rule Than Random Selection,” arXiv:1506.00552, first submitted 2015-06-01; PMLR 37 (2015), 1632–1641.
