# Sharp logistic Heun invariance frontier and square-root failure window

## Finding
For the scalar logistic equation \(Y'=aY-bY^2\) with \(a,b>0\), the standard explicit trapezoidal (Heun) two-stage second-order Runge–Kutta step preserves the physical carrying-capacity interval \([0,a/b]\) for **every initial value in that interval and for arbitrarily many iterates** if and only if
\[
0<h\le \frac{\sqrt{9+6\sqrt3}-1}{a}.
\]
At equality an interior, strictly positive initial value maps exactly to zero in one step. For every larger step there is a nonempty open interval of physically admissible initial values that maps strictly below zero immediately. At onset, the width of this interval in the normalized coordinate is asymptotic to an explicit positive constant times the square root of the step-parameter excess.

## Assumptions and scope
Let \(h>0\), put \(r=1+ah>1\), and normalize the physical state \(Y\) by \(x=bhY/r\). The carrying-capacity range \(0\le Y\le a/b\) is then precisely \(0\le x\le c_r\), where \(c_r=(r-1)/r\). Heun's two-stage method applies the Euler predictor \(z=rx(1-x)\) and takes the average of the old state and the second Euler predictor:
\[
P_r(x)=\frac12\{x+rz(1-z)\}=\frac{x}{2}\left[1+r^2(1-x)-r^3x(1-x)^2\right].
\]
The claim concerns exact-arithmetic, fixed-step iterates of this polynomial on the entire physical initial interval, not the stability of a single distinguished orbit. Denote
\[
r_*=\sqrt{9+6\sqrt3},\quad
 y_* =\frac{1+\sqrt{1-3/r_*}}3,\quad x_*=1-y_*.
\]
Numerically, \(r_*=4.403669475041612\) and \(x_*=0.478473514894113\).

For \(r>r_*\), there are precisely two roots \(1/r<y_-(r)<y_+(r)<1\) of
\[
g_r(y)=1+r^2y-r^3y^2(1-y),
\]
and the one-step negative-state interval is exactly
\[
\left(1-y_+(r),\,1-y_-(r)\right)\subset(0,c_r).
\]
Its normalized width obeys, as \(r\downarrow r_*\) from above,
\[
y_+(r)-y_-(r)=C\sqrt{r-r_*}+O(r-r_*),\qquad
C=2\sqrt{\frac{r_*y_*+3/r_*}{r_*^3(3y_*-1)}}=0.497048773763258\ldots.
\]
The minimum one-step output has the further first-order onset
\[
\min_{0\le x\le c_r}P_r(x)
=-\frac{x_*}{2}\left(r_*y_*+\frac3{r_*}\right)(r-r_*)+O((r-r_*)^2),
\]
with leading coefficient \(0.712418427401048\ldots\). No corresponding claim is made about statistical perturbations, variable steps or spatial discretization.

## Proof
**Step 1: nonnegative-output criterion.** For \(x>0\), writing \(y=1-x\) gives \(2P_r(x)/x=g_r(y)\). The endpoints satisfy \(g_r(0)=1\), \(g_r(1)=1+r^2\), and
\[
g_r'(y)=r^2\{1-2ry+3ry^2\}
=r^2\{1-r/3+3r(y-1/3)^2\}.
\]
For \(1<r\le3\), \(g_r\) is nondecreasing on \([0,1]\), hence positive. For \(r>3\), it has a local maximum at \(\frac{1-\sqrt{1-3/r}}3\) and a local minimum at \(\frac{1+\sqrt{1-3/r}}3\). A zero local minimum must solve \(g_r(y)=g_r'(y)=0\). Eliminating \(y\), or computing the cubic discriminant, yields
\[
\operatorname{disc}_y(g_r)=r^6(r^4-18r^2-27).
\]
The only possible zero of the local minimum for \(r>3\) is \(r=r_*\). Its value is \(2\) at \(r=3\), while at fixed \(y=2/3\) the polynomial tends to negative infinity as \(r\to\infty\). Hence the local minimum is strictly positive below \(r_*\), zero at \(r_*\), and strictly negative above \(r_*\). This proves nonnegativity of \(P_r\) for every \(x\in[0,1]\) precisely up to \(r_*\).

For \(r>r_*\), the negative set is one interval between two positive roots of \(g_r\). Since
\[
g_r(y)=1+r^2y\{1-ry(1-y)\}\ge1\quad (0\le y\le1/r),
\]
both roots lie in \((1/r,1)\). Thus the full negative-output interval lies inside the physical range \((0,c_r)\). At \(r=r_*\), the local-minimum root \(y_*\) is double and \(x_*=1-y_*\in(0,c_{r_*})\), so \(P_{r_*}(x_*)=P'_{r_*}(x_*)=0\).

**Step 2: the upper carrying-capacity bound.** The map fixes \(0\) and \(c_r\). Direct polynomial division gives, with \(u=rx\),
\[
P_r(x)-c_r=(x-c_r)Q_r(u),\qquad
Q_r(u)=1-\tfrac12u\left[u^2-(r+1)u+(r+1)\right].
\]
We show \(Q_r(u)>0\) for \(0\le u\le r-1\) whenever \(1<r\le r_*\). For \(0\le u\le1\),
\[
u\{u^2-(r+1)u+(r+1)\}
\le u+(r+1)u(1-u)
\le \frac{(r+2)^2}{4(r+1)}<2,
\]
using \(r_*<2+2\sqrt2\). For \(1\le u\le r-1\), necessarily \(r\ge2\) and \(r+1\ge u+2\), whence
\[
u\{u^2-(r+1)u+(r+1)\}
\le u\{u^2-(u+2)u+(u+2)\}=u(2-u)\le1.
\]
Thus \(Q_r>0\), and \(x-c_r\le0\) implies \(P_r(x)\le c_r\) for every \(x\in[0,c_r]\). Combined with Step 1, this proves interval invariance at and below \(r_*\) and immediate failure above it. Induction then proves preservation for any number of fixed steps in the safe range.

**Step 3: sharp creation of the negative interval.** At \((r_*,y_*)\),
\[
\partial_r g=-r_*y_*-3/r_*<0,\qquad
\partial_{yy}g=2r_*^3(3y_*-1)>0.
\]
(The first identity uses \(g_{r_*}(y_*)=0\).) Taylor expansion and the implicit-function theorem in the squared local coordinate give the two roots
\[
y_\pm(r)=y_*\pm\sqrt{\frac{r_*y_*+3/r_*}{r_*^3(3y_*-1)}}\sqrt{r-r_*}
+O(r-r_*).
\]
Subtracting gives the stated width. The perturbing minimizer of \(P_r\) is smooth near \(x_*\) because \(P''_{r_*}(x_*)=x_*\partial_{yy}g_{r_*}(y_*)/2>0\). The derivative of the minimum in \(r\) at onset equals \(\partial_rP_{r_*}(x_*)=x_*\partial_rg_{r_*}(y_*)/2\), proving the linear depth law.

## Verification
The accompanying `verify.py` is standalone Python with no nonstandard dependencies. It checks the Heun predictor identity, the polynomial factorization, the exact cubic-discriminant identity over rational inputs, the fixed-point identities, a rational finite grid of invariant-interval examples, the negative-interval geometry, and numerically converging square-root widths. On the packaged source, it reports `VERIFY_OK 2071`. The analytical argument above proves the universal and asymptotic statements; the finite checks only detect implementation and algebra mistakes.

## Relationship to prior work
Grammaticos, Tamizhmani, and Willox (2026), *On unconventional discretisations* (arXiv:2607.19413, first posted July 17, 2026), write the same Heun polynomial and report loss of positivity at a numerical parameter “around 4.4037”. That numerical observation and the underlying method belong to that paper and are not claimed here. The new statement is the exact algebraic threshold, a uniform if-and-only-if invariant-interval theorem over all physical initial data and all iterates, and a sharp square-root description of the newly forbidden initial-data interval and its output depth. Modified, nonstandard second-order positivity-preserving schemes such as Hoang–Ehrhardt (2025) are different algorithms and do not imply the exact Heun threshold. General Runge–Kutta method formulas are standard.

## Limitations
The proof treats the one-dimensional autonomous logistic equation and the classical Heun explicit trapezoidal method, not every explicit second-order Runge–Kutta tableau. For \(r>r_*\) it proves the existence of immediately negative outputs; it does not claim every positive initial state becomes negative, or classify the subsequent nonlinear attractors. The cited 2026 source already anticipated the numerical location \(4.4037\), so the claimed contribution is mathematical sharpness and the local bifurcation law, not discovery of positivity loss. No independent external validation or complete historical priority guarantee is claimed.

## References
1. B. Grammaticos, T. Tamizhmani, and R. Willox, *On unconventional discretisations*, arXiv:2607.19413 (first publicly posted 2026-07-17), https://arxiv.org/abs/2607.19413.
2. M. T. Hoang and M. Ehrhardt, *A Generalized Second-Order Positivity-Preserving Numerical Method for Non-Autonomous Dynamical Systems with Applications*, arXiv:2510.03420 (first posted 2025-10-03), https://arxiv.org/abs/2510.03420.
3. Standard explicit trapezoidal/Heun RK2 tableau: https://kauri.readthedocs.io/en/latest/pages/rk.html.
