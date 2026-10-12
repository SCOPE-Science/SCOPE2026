# Exact two-state Tustin positivity threshold and a correction to a published determinant test

## Finding
Consider a continuous-time positive two-state system
\[
\dot x=Ax,
\qquad
A=
\begin{pmatrix}
-a&b\\
c&-d
\end{pmatrix},
\]
with
\[
a,d>0,\qquad b,c\ge0,\qquad
\Delta:=ad-bc>0.
\]
The Tustin, or first-order diagonal Padé, discretization is
\[
T_h=
\left(I+\frac h2A\right)
\left(I-\frac h2A\right)^{-1},
\qquad h\ge0.
\]

Its exact positivity interval is
\[
\boxed{
T_h\ge0
\iff
0\le h\le h_\star
}
\]
with
\[
h_\star=
\frac{\sqrt{(a-d)^2+4\Delta}-|a-d|}{\Delta}
=
\frac4{|a-d|+\sqrt{(a+d)^2-4bc}}.
\]
Equivalently, if
\[
\alpha=\frac2h,
\]
then the exact condition is
\[
\alpha^2-|a-d|\alpha-\Delta\ge0.
\]

A directly relevant 2010 source writes the correct two-state Padé matrix but then states that
\[
\Delta\le\alpha^2
\]
is sufficient for nonnegativity. That intermediate statement is false. For
\[
A=\operatorname{diag}(-10,-1),
\qquad
\alpha=4,
\qquad
h=\frac12,
\]
one has
\[
\Delta=10\le16=\alpha^2,
\]
but
\[
T_h=
\operatorname{diag}
\left(-\frac37,\frac35\right),
\]
so the first state changes sign.

The same source's later condition
\[
\alpha\ge\max\{a,d\},
\qquad
h\le\frac2{\max\{a,d\}},
\]
is valid. The exact threshold shows precisely how conservative that safe condition can be: equality holds when \(bc=0\), strict improvement holds when \(bc>0\), and the improvement factor is unbounded as a stable, symmetric, strongly coupled two-state system approaches the Hurwitz boundary.

There is also an exact all-dimensional criterion. For every Hurwitz Metzler \(A\), define
\[
M=I-\frac h2A.
\]
Then
\[
M^-1\ge0,
\qquad
T_h=2M^-1-I.
\]
Therefore
\[
T_h\ge0
\iff
(M^-1)_{ii}\ge\frac12
\quad\text{for every }i.
\]
The two-state formula above is the closed-form evaluation of this resolvent-diagonal test.

## Assumptions and scope
The matrix \(A\) is real, Metzler, and Hurwitz. The sharp closed form is proved for two states. The all-dimensional statement is an exact test in terms of the diagonal of a resolvent, not a closed formula in entries.

The result concerns entrywise positivity of the one-step Tustin map. Schur stability is a separate property: because the Cayley transform maps the open left half-plane into the open unit disk, \(T_h\) is Schur stable for every \(h>0\) whenever \(A\) is Hurwitz, even when positivity fails.

The correction is limited to the intermediate two-state determinant sufficiency sentence in the 2010 source. Its subsequent stronger sampling-time bound remains correct, and no claim is made that the source's later results depending only on that stronger bound fail.

## Proof
Put
\[
M=I-\frac h2A.
\]
Since \(A\) is Hurwitz Metzler, \(-A\) is a nonsingular \(M\)-matrix. Thus
\[
M=I+\frac h2(-A)
\]
is also a nonsingular \(M\)-matrix, so
\[
M^-1\ge0.
\]
Moreover
\[
I+\frac h2A
=
2I-M.
\]
Hence
\[
T_h=(2I-M)M^-1=2M^-1-I.
\]
This proves the all-dimensional criterion immediately: every off-diagonal entry is nonnegative, and the only possible negative entries are the diagonal ones. Therefore
\[
T_h\ge0
\iff
(M^-1)_{ii}\ge\frac12
\quad\text{for all }i.
\]

Now specialize to two states. Write
\[
x=\frac h2.
\]
Then
\[
M=
\begin{pmatrix}
1+ax&-bx\\
-cx&1+dx
\end{pmatrix}
\]
and
\[
\det M
=
1+(a+d)x+\Delta x^2>0.
\]
Direct inversion gives
\[
T_h=
\frac1{1+(a+d)x+\Delta x^2}
\begin{pmatrix}
1+(d-a)x-\Delta x^2&2bx\\
2cx&1+(a-d)x-\Delta x^2
\end{pmatrix}.
\]
The denominator and off-diagonal entries are nonnegative. Thus positivity is equivalent to the two diagonal inequalities
\[
1+(d-a)x-\Delta x^2\ge0,
\]
\[
1+(a-d)x-\Delta x^2\ge0.
\]
Their conjunction is
\[
1-|a-d|x-\Delta x^2\ge0.
\]
Since \(\Delta>0\), this holds exactly for
\[
0\le x\le
\frac{\sqrt{(a-d)^2+4\Delta}-|a-d|}{2\Delta}.
\]
Multiplying by \(2\) yields
\[
h_\star=
\frac{\sqrt{(a-d)^2+4\Delta}-|a-d|}{\Delta}.
\]
Rationalizing the numerator and using
\[
(a-d)^2+4(ad-bc)
=
(a+d)^2-4bc
\]
gives the second displayed form.

For the reciprocal parameter \(\alpha=1/x=2/h\), the diagonal conditions are
\[
\alpha^2\pm(a-d)\alpha-\Delta\ge0,
\]
which combine to
\[
\alpha^2-|a-d|\alpha-\Delta\ge0.
\]

The published determinant-only condition
\[
\Delta\le\alpha^2
\]
drops the linear term. The diagonal counterexample
\[
a=10,\quad d=1,\quad b=c=0,\quad \alpha=4
\]
has \(\Delta=10\le16\), but
\[
\alpha^2-|a-d|\alpha-\Delta
=
16-36-10<0.
\]
Direct Cayley evaluation gives the displayed negative first diagonal entry.

To compare with the conservative published condition, let
\[
m=\max\{a,d\}.
\]
The step \(h=2/m\) corresponds to \(\alpha=m\). If \(a\ge d\),
\[
m^2-|a-d|m-\Delta
=
a^2-(a-d)a-(ad-bc)
=
bc\ge0,
\]
and the case \(d\ge a\) is symmetric. Hence the conservative bound is always safe. Equality with the exact threshold holds precisely when \(bc=0\); if \(bc>0\), the exact interval is strictly larger.

For
\[
a=d=1,\qquad b=c=t,\qquad 0\le t<1,
\]
one has
\[
\Delta=1-t^2,
\qquad
h_\star=\frac2{\sqrt{1-t^2}},
\]
while the conservative bound remains \(2\). The ratio therefore diverges as \(t\uparrow1\).

## Verification
The embedded `verify.py` uses exact rational arithmetic.

It verifies the published-criterion counterexample
\[
A=\operatorname{diag}(-10,-1),
\qquad
h=\frac12,
\]
including
\[
\Delta\le\alpha^2
\]
and the exact negative Tustin entry.

It also checks a coupled example
\[
A=
\begin{pmatrix}
-1&3/4\\
1&-1
\end{pmatrix},
\]
for which
\[
\Delta=\frac14,
\qquad
h_\star=4.
\]
At \(h=3\),
\[
T_h=
\frac1{73}
\begin{pmatrix}
7&36\\
48&7
\end{pmatrix}>0,
\]
at \(h=4\) the two diagonal entries are zero, and at \(h=5\) they are negative. The conservative bound \(h\le2\) is therefore safe but not exact.

The verifier also reconstructs the identity
\[
T_h=2\left(I-\frac h2A\right)^{-1}-I
\]
on a three-state rational Metzler-Hurwitz example and confirms that all possible sign failures lie on the diagonal.

## Relationship to prior work
Zappavigna, Colaneri, Kirkland, and Shorten study Padé discretization of positive systems and give a general sufficient sampling-time condition for the first-order diagonal Padé map. Their two-state section writes the exact matrix formula with diagonal numerators
\[
\beta_1=\alpha^2-(a-d)\alpha-\Delta,
\qquad
\beta_2=\alpha^2+(a-d)\alpha-\Delta.
\]
The exact positivity condition is therefore the conjunction \(\beta_1,\beta_2\ge0\). The following sentence in that source states instead that \(\Delta\le\alpha^2\) is sufficient. The counterexample above shows that this implication omits the necessary linear term. The source then imposes the stronger \(\alpha\ge\max\{a,d\}\), which is valid.

The later article “Essentially Negative News About Positive Systems” gives a correct general sufficient condition for first-order Padé positivity in terms of the diagonal entries of a Metzler-Hurwitz matrix. Its inspected full-text version does not state the coupling-sensitive exact two-state threshold derived here.

Fallat and Tsatsomeros study Cayley transforms of matrix positivity classes and record the basic resolvent identity underlying the calculation. Their matrix-class results provide algebraic context but do not state the positive-system sampling threshold or correct the two-state determinant test.

Positive-system control literature establishes the role of Metzler matrices and the invariance of the positive orthant. The present statement isolates the exact time-discretization boundary inside that setting.

## Limitations
The closed-form threshold uses the two-state structure. In higher dimensions the exact criterion
\[
\operatorname{diag}
\left(I-\frac h2A\right)^{-1}
\ge\frac12\mathbf1
\]
is necessary and sufficient, but it is not reduced here to a simple formula in matrix entries.

The result is for first-order diagonal Padé, equivalently Tustin or Crank--Nicolson discretization of a linear autonomous system. Higher diagonal Padé orders can have qualitatively different positivity behavior.

The exact threshold controls one-step entrywise positivity, not monotonicity with respect to a norm, transient amplification, or preservation under rounding errors.

Residual originality risk remains that older nonnegative-matrix or Cayley-transform literature may encode the same two-state threshold in a different parametrization. The closest full texts inspected contain the matrix formula, general Cayley identities, or conservative sufficient conditions, but not the corrected iff threshold and its unbounded-conservatism consequence.

## References
1. A. Zappavigna, P. Colaneri, S. Kirkland, and R. N. Shorten, “On the preservation of co-positive Lyapunov functions under Padé discretization for positive systems,” 19th International Symposium on Mathematical Theory of Networks and Systems, Budapest, 5–9 July 2010.
2. A. Zappavigna, P. Colaneri, S. Kirkland, and R. N. Shorten, “Essentially Negative News About Positive Systems,” Linear Algebra and its Applications 436 (2012), 3425–3442, DOI 10.1016/j.laa.2011.12.021.
3. S. M. Fallat and M. J. Tsatsomeros, “On the Cayley transform of positivity classes of matrices,” Electronic Journal of Linear Algebra 9 (2002), 190–196.
4. L. Fainshil and M. Margaliot, “A Maximum Principle for the Stability Analysis of Positive Bilinear Control Systems with Applications to Positive Linear Switched Systems,” SIAM Journal on Control and Optimization 50 (2012), 2193–2215, DOI 10.1137/11083808X.
