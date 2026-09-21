# Sharp black-box robustness frontier for scalar Aitken-Steffensen acceleration

## Result

Let \(g:\mathbb R\to\mathbb R\) be a global contraction with
\[
|g(x)-g(y)|\le q|x-y|,\qquad 0\le q<1,
\]
and let \(x_*\) be its unique fixed point. Starting from \(x\ne x_*\), form two
Picard images
\[
x_1=g(x),\qquad x_2=g(x_1),
\]
and the restarted Aitken delta-squared (Steffensen) point
\[
S(x)=x-\frac{(x_1-x)^2}{x_2-2x_1+x}.
\]
All statements below are in exact real arithmetic.

The denominator is automatically nonzero. More precisely,
\[
|x_2-2x_1+x|\ge (1-q)|x_1-x|>0.
\]

The exact worst-case fixed-point-error factor over all scalar global
\(q\)-contractions and all nonfixed starting points is
\[
\boxed{
\sup \frac{|S(x)-x_*|}{|x-x_*|}
=
W(q):=
\frac{2q^2}{(1-q)(1+2q)}
}.
\]
For every \(q\in(0,1)\) the supremum is attained by a continuous piecewise-affine
\(q\)-contraction.

Consequently, one restarted Aitken-Steffensen cycle is guaranteed to be
nonexpansive in fixed-point error for every scalar \(q\)-contraction exactly when
\[
\boxed{
q\le q_{\rm AS}:=\frac{1+\sqrt{17}}8
=0.640388203202\ldots
}.
\]
For \(q<q_{\rm AS}\), repeated restarted cycles therefore converge globally with
cycle factor at most \(W(q)\). This is a sufficient global guarantee; no claim is
made that crossing the threshold forces eventual divergence.

The same two evaluations used without extrapolation give two Picard steps, whose
exact worst-case factor is \(q^2\). Under only the global contraction assumption,
Aitken-Steffensen is therefore strictly worse in minimax one-cycle error:
\[
W(q)>q^2,\qquad
\frac{W(q)}{q^2}
=\frac{2}{1+q-2q^2}
\ge \frac{16}{9}
\quad(0<q<1).
\]
Thus the acceleration can improve smooth local asymptotics while having a worse
black-box global robustness guarantee at the same evaluation count.

If \(g\) is additionally nondecreasing, the exact frontier improves to
\[
\boxed{
\sup \frac{|S(x)-x_*|}{|x-x_*|}
=
W_\uparrow(q):=\frac{q^2}{1-q^2}
}.
\]
Hence the universal nonexpansion threshold in the monotone subclass is exactly
\[
\boxed{q\le 1/\sqrt2}.
\]
Even there \(W_\uparrow(q)>q^2\) for every \(q>0\).

## Computational model and norm

The map is accessed only through the two values \(g(x)\) and \(g(g(x))\) in each
cycle. The class parameter \(q\) is used for analysis and need not be supplied to
the algorithm. The norm is absolute value on \(\mathbb R\). The claims concern
exact arithmetic and one restarted cycle (plus the immediate repeated-cycle
corollary when the factor is below one).

## Proof

Translate and rescale a nonfixed state so that \(x_*=0\) and the current error is
\(x=1\). Write
\[
a=g(1),\qquad c=g(a),\qquad
t=\frac{c-a}{a-1}.
\]
Contraction gives
\[
|a|\le q,\qquad |c|\le q|a|,\qquad |t|\le q.
\]
Also
\[
c=a(1+t)-t.
\]
Since \(t<1\),
\[
c-2a+1=(1-a)(1-t),
\]
so the denominator is positive in normalized coordinates and the announced
lower bound follows. The normalized accelerated error is
\[
s:=S(1)=\frac{a-t}{1-t}.
\]

### Positive branch

If \(a>0\), then \(|c|\le qa<a\), so \(t>0\). The constraint
\(|c|\le qa\) is equivalent to
\[
\frac{t}{1+t+q}\le a\le \frac{t}{1+t-q},
\qquad 0<t\le q.
\]
For fixed \(t\), the maximum of \(|a-t|/(1-t)\) is attained at an endpoint.

At the lower endpoint,
\[
F_-(t)=
\frac{t(t+q)}{(1+t+q)(1-t)}.
\]
Its derivative has positive numerator
\[
(q+1)(q+2t),
\]
so it increases on \((0,q]\). Therefore
\[
F_-(t)\le F_-(q)
=\frac{2q^2}{(1-q)(1+2q)}=W(q).
\]

At the upper endpoint,
\[
F_+(t)=
\frac{t(q-t)}{(1+t-q)(1-t)}
=
\frac{v}{1-q+v},
\qquad v=t(q-t)\le \frac{q^2}{4}.
\]
Hence
\[
F_+(t)\le \frac{q^2}{(2-q)^2}<W(q)
\quad(0<q<1).
\]

### Negative branch

If \(a<0\), write \(a=-u\), \(t=-r\), with \(u,r>0\). Then
\[
\frac{u(1-q)}{1+u}\le r\le
\frac{u(1+q)}{1+u},\qquad 0<u\le q.
\]
The two endpoint magnitudes are
\[
G_-(u)=\frac{u(u+q)}{1+2u-uq},
\qquad
G_+(u)=\frac{u(q-u)}{1+2u+uq}.
\]
The first is increasing because its derivative has positive numerator
\[
(u+1)(q+2u-qu),
\]
and therefore
\[
G_-(u)\le \frac{2q^2}{1+2q-q^2}<W(q).
\]
The second obeys
\[
G_+(u)\le u(q-u)\le \frac{q^2}{4}<W(q).
\]
The case \(a=0\) gives zero accelerated error. This proves the global upper bound.

### Sharp witness

For \(q\in(0,1)\), put
\[
a_q=\frac{q}{1+2q}
\]
and define
\[
g_q(z)=
\begin{cases}
-qz,&z\le a_q,\\
qz-2qa_q,&z\ge a_q.
\end{cases}
\]
This map is continuous, has slopes of magnitude \(q\), and has the unique fixed
point \(0\). Starting from \(1\),
\[
1\longmapsto a_q\longmapsto -qa_q.
\]
Here \(t=q\), and
\[
S(1)=-\frac{2q^2}{(1-q)(1+2q)},
\]
which proves sharpness. For \(q=0\) the result is immediate.

Solving \(W(q)\le1\) gives
\[
4q^2-q-1\le0,
\]
hence the stated threshold. Solving \(W(q)\le q\) gives \(q\le1/2\), so only
below one half is the accelerated cycle guaranteed even to beat one Picard step.
Finally,
\[
\frac{W(q)}{q^2}=\frac{2}{1+q-2q^2},
\]
whose denominator is maximized at \(q=1/4\) with value \(9/8\), giving the
\(16/9\) same-evaluation minimax gap.

### Nondecreasing contractions

Affine normalization preserves monotonicity even when the original error is
negative. Thus \(0\le c\le qa\), and for a nontrivial orbit \(a,t>0\). The feasible
interval becomes
\[
\frac{t}{1+t}\le a\le\frac{t}{1+t-q},
\qquad 0<t\le q.
\]
At the lower endpoint,
\[
\frac{|a-t|}{1-t}=\frac{t^2}{1-t^2},
\]
which increases to \(q^2/(1-q^2)\). The upper endpoint is bounded by
\(q^2/(2-q)^2\), strictly smaller because
\[
(2-q)^2-(1-q^2)=3-4q+2q^2>0.
\]
Sharpness is attained by
\[
a_q=\frac{q}{1+q},\qquad
g_q^\uparrow(z)=
\begin{cases}
0,&z\le a_q,\\
q(z-a_q),&z\ge a_q.
\end{cases}
\]
This nondecreasing \(q\)-contraction sends \(1\mapsto a_q\mapsto0\), and its
Aitken point has magnitude \(q^2/(1-q^2)\). The threshold \(1/\sqrt2\) follows
from \(W_\uparrow(q)\le1\).

## Relation to prior work

Steffensen acceleration and Aitken's delta-squared process are classical.
Schmidt (1966), Johnson--Scholz (1968), Pavaloiu (1968), Hofmann (1975),
Schneider (1981), Baptist (1982), and Voller (1985) study convergence,
monotonicity, enclosure, or error estimates for Steffensen-type procedures under
various divided-difference, convexity, monotonicity, or semilocal hypotheses.
Baptist's accessible theorem, for example, gives monotone enclosure under
convexity and a sign-changing bracket rather than the bare global Lipschitz
hypothesis used here. Modern fixed-point acceleration work analyzes Anderson
acceleration, often locally or with coefficient/nondegeneracy assumptions, and a
2025 Acta Numerica survey places Aitken acceleration in that broader history.

In the sources checked, we did not find the exact black-box factor
\(2q^2/((1-q)(1+2q))\), the threshold \((1+\sqrt{17})/8\), the sharp monotone
factor \(q^2/(1-q^2)\), or the \(16/9\) same-evaluation minimax comparison.
The closest older literature is broad enough that historical equivalence under
different notation remains the principal originality uncertainty.

## Limitations

- Scalar real contractions only; no vector, Hilbert-space, or Anderson-acceleration
  analogue is claimed.
- Exact arithmetic only. Near a small second difference, floating-point Aitken
  extrapolation can have additional numerical instability not covered here.
- The main theorem assumes only a global Lipschitz contraction; smoother or more
  structured maps can have much stronger local behavior, including the familiar
  quadratic convergence of Steffensen's method.
- The sharp threshold is a universal one-cycle nonexpansion threshold. Its failure
  above the threshold does not imply that restarted Steffensen must diverge.
- Several older highly relevant papers were not available here at full theorem
  level, notably Schmidt (1966), Johnson--Scholz (1968), Hofmann (1975), and
  Schneider (1981). They remain the main residual risk to the originality claim.

## Reproducibility

`artifacts/verify.py` checks the sharp witnesses with high-precision decimal
arithmetic, verifies the two threshold identities and the \(16/9\) minimax ratio,
and stress-tests the derived feasible \((a,c)\) region with deterministic random
sampling. `artifacts/verification.txt` records the verified output.

## References

1. J. W. Schmidt, *Konvergenzgeschwindigkeit der Regula falsi und des
   Steffensen-Verfahrens im Banachraum*, ZAMM 46 (1966), 146--148.
   https://doi.org/10.1002/zamm.19660460211
2. L. W. Johnson and D. R. Scholz, *On Steffensen's Method*, SIAM Journal on
   Numerical Analysis 5 (1968), 296--302. https://doi.org/10.1137/0705026
3. I. Pavaloiu, *On the Steffensen method for solving nonlinear operator
   equations*, Rev. Roumaine Math. Pures Appl. 13 (1968), 857--861.
   https://ictp.acad.ro/steffensen-method-solving-nonlinear-operator-equations/
4. W. Hofmann, *Monotonieeigenschaften des Steffensen-Verfahrens*,
   Aequationes Mathematicae 12 (1975), 21--31.
   https://doi.org/10.1007/BF01834035
5. N. Schneider, *Results about monotone convergence of Steffensen-like-methods*,
   BIT 21 (1981), 347--354.
6. P. Baptist, *Konvergenz und monotone Einschliessung fuer das
   Steffensen-Verfahren*, Elemente der Mathematik 37 (1982), 33--40.
   https://doi.org/10.5169/seals-36387
7. R. L. Voller, *A-posteriori bounds for Steffensen-like methods*,
   Anal. Numer. Theor. Approx. 14 (1985), 159--170.
   https://ictp.acad.ro/jnaat/journal/article/view/1985-vol14-no2-art10
8. A. Toth and C. T. Kelley, *Convergence Analysis for Anderson Acceleration*,
   SIAM Journal on Numerical Analysis 53 (2015), 805--819.
   https://doi.org/10.1137/130919398
9. C. Evans, S. Pollock, L. G. Rebholz, and M. Xiao, *A Proof That Anderson
   Acceleration Improves the Convergence Rate in Linearly Converging Fixed-Point
   Methods (But Not in Those Converging Quadratically)*, SIAM Journal on
   Numerical Analysis 58 (2020), 788--810.
   https://doi.org/10.1137/19M1245384
10. O. A. Krzysik, H. De Sterck, and A. Smith, *Asymptotic Convergence of
    Restarted Anderson Acceleration for Certain Normal Linear Systems*, SIAM
    Journal on Scientific Computing (2025).
    https://doi.org/10.1137/24M1672262
11. Y. Saad, *Acceleration methods for fixed-point iterations*, Acta Numerica 34
    (2025), 805--890. https://doi.org/10.1017/S0962492924000096
