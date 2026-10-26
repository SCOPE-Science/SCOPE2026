# Exact positivity threshold for alternating-grid BDF2

## Finding

Let \(\lambda>0\), \(h>0\), and \(r\ge1\), and set \(H=rh\) and \(z=\lambda h\). For the scalar decay equation

\[
y'(t)=-\lambda y(t),\qquad y(0)=y_0>0,
\]

use backward Euler on the first step of length \(H\), then use variable-step BDF2 on the repeating step pattern \(H,h,H,h,\ldots\). In exact arithmetic, every numerical value is strictly positive if and only if

\[
0<z\le \frac{2}{(\sqrt r+1)^2}.
\]

Equivalently, the largest-step boundary is

\[
\lambda H\le \frac{2r}{(\sqrt r+1)^2}.
\]

The right-hand side increases from \(1/2\) at \(r=1\) toward \(2\) as \(r\to\infty\). This is a sharp positivity condition for this alternating-grid scalar problem, not a claim about arbitrary variable grids or nonlinear systems.

## Assumptions and scope

The parameter \(\lambda\) is positive, the base step \(h\) is positive, and the long-to-short ratio \(r=H/h\) is at least one. The initial value satisfies \(y_0>0\). The startup is exactly one backward-Euler step, \(y_1=y_0/(1+\lambda H)\). For all later steps, BDF2 uses the actual adjacent step ratio. Positivity means \(y_n>0\) at every finite index \(n\), with exact arithmetic. The result does not assert positivity for general nonperiodic step sequences, nonlinear reaction equations, spatially discretized PDEs, or finite-precision arithmetic.

## Proof

Write \(h_n\) for the step length at index \(n\), \(r_n=h_n/h_{n-1}\), and \(z_n=\lambda h_n\). Applying variable-step BDF2 to \(y'=-\lambda y\) gives, for \(n\ge2\),

\[
\bigl(1+2r_n+(1+r_n)z_n\bigr)y_n=(1+r_n)^2y_{n-1}-r_n^2y_{n-2}.
\]

For a long step, \(r_n=r\) and \(z_n=rz\); for a short step, \(r_n=1/r\) and \(z_n=z\). Define the positive denominators

\[
D_H=1+2r+r(1+r)z,\qquad D_L=r(r+2)+r(1+r)z,
\]

and coefficients

\[
c_H=\frac{(1+r)^2}{D_H},\quad d_H=\frac{r^2}{D_H},\quad c_L=\frac{(1+r)^2}{D_L},\quad d_L=\frac1{D_L}.
\]

Whenever the ratios are defined, \(q_n=y_n/y_{n-1}\) therefore obeys \(q_n=c_L-d_L/q_{n-1}\) on a short step and \(q_n=c_H-d_H/q_{n-1}\) on a long step. The map from one long-step ratio to the next is

\[
F(q)=c_H-\frac{d_H}{c_L-d_L/q}.
\]

Its fixed points are the roots of

\[
p(q)=c_Lq^2-Bq+c_Hd_L,\qquad B=c_Hc_L-d_H+d_L.
\]

Direct expansion yields the exact discriminant identity

\[
B^2-4c_Lc_Hd_L=\frac{r^2(1+r)^4}{D_H^2D_L^2}\left((r-1)^2z^2-4(r+1)z+4\right).
\]

For \(r>1\), the bracket has roots \(z_-=2/(\sqrt r+1)^2\) and \(z_+=2/(\sqrt r-1)^2\); for \(r=1\), it reduces to \(4-8z\), with threshold \(z_-=1/2\). Thus the first loss of real fixed points occurs at \(z_-=2/(\sqrt r+1)^2\).

For \(0<z\le z_-\), the coefficient \(B\) is positive and exceeds \(2d_L\). Indeed, \(z_-\le2/r\) gives \(2(r+1)-r(r-1)z\ge4\) and \(D_H\le4r+3\), so

\[
\frac{B}{d_L}=\frac{(1+r)^2\bigl(2(r+1)-r(r-1)z\bigr)}{D_H}\ge\frac{4(1+r)^2}{4r+3}>2.
\]

Hence the two roots \(q_-\le q_+\) of \(p\) are positive and \(q_+>d_L/c_L\). The startup ratio is \(q_1=1/(1+rz)\). Exact substitution gives

\[
q_1-\frac{B}{2c_L}=\frac{r\bigl((r^2-r)z^2+(r-1)z+2\bigr)}{2(1+rz)D_H}>0
\]

and

\[
p(q_1)=\frac{r^2z^2(1+r)^2}{(1+rz)^2(D_L/r)D_H}\ge0.
\]

Because \(q_1\) lies to the right of the vertex of \(p\), these identities imply \(q_1\ge q_+\). On \(q>d_L/c_L\), the map \(F\) is increasing and

\[
F(q)-q=-\frac{p(q)}{c_Lq-d_L}.
\]

Consequently, for \(q\ge q_+\), one has \(q_+\le F(q)\le q\). The long-step ratios remain at least \(q_+\), while the intervening short-step ratios are positive because \(q_+>d_L/c_L\). This proves strict positivity for every finite index, including the repeated-root boundary \(z=z_-\).

For \(z>z_-\), if the startup ratio is already at most \(d_L/c_L=1/(1+r)^2\), the next short-step value is nonpositive. Otherwise, while the long-step ratios remain in the positive domain, the same identity makes them strictly decrease because \(p(q)>0\): between the two roots of the discriminant bracket, \(p\) has no real roots; beyond the larger root, \(B<0\) and \(p(q)>0\) for all \(q>0\). A positive decreasing sequence of long-step ratios cannot stay above \(d_L/c_L\) forever, since its limit would be a positive fixed point, which does not exist in these regimes. It must therefore cross the threshold, making a later short-step ratio nonpositive. Thus the condition is also necessary. Multiplying \(z_-\) by \(r\) gives the stated long-step boundary.

## Verification

The recurrence and discriminant were derived algebraically. The accompanying standard-library script `verify_threshold.py` uses exact rational arithmetic to check representative perfect-square ratios at and above the proposed boundary. These finite checks are reproducibility checks only; the all-index result follows from the fixed-point argument above, not from numerical enumeration.

## Relationship to prior work

Liao, Tang, and Zhou study variable-step BDF2 for the nonlinear Allen–Cahn equation and prove a discrete maximum principle under a step-ratio restriction and a practical step-size condition. Their theorem concerns a spatially discretized nonlinear PDE and supplies sufficient conditions; it does not state the exact necessary-and-sufficient threshold for the scalar linear decay equation on a strictly alternating grid. Wang, Mao, and Wang study stability and error estimates for variable-step BDF2 on linear and semilinear parabolic equations, but the abstract does not identify an exact alternating-grid positivity criterion. The constant-step limit \(r=1\) of the present formula is \(z\le1/2\); for \(r>1\), the result gives a distinct sharp tradeoff between the short and long steps. The literature search did not establish novelty by absence alone; the comparison is limited to the sources and materials listed here.

## Limitations

The theorem is restricted to one scalar linear decay mode, one backward-Euler startup, and an exactly alternating pair of step lengths. It does not settle positivity for arbitrary adaptive grids, coupled systems, nonlinear PDEs, or roundoff-affected implementations. One related variable-step BDF2 stability paper was available only at abstract level during this run, so a broader claim of literature-wide novelty would be unwarranted.

## References

1. H. Liao, T. Tang, and T. Zhou, “On energy stable, maximum-principle preserving, second order BDF scheme with variable steps for the Allen-Cahn equation,” arXiv:2003.00421, first submitted 2020-03-01; SIAM Journal on Numerical Analysis 58(4), 2294–2314 (2020). https://arxiv.org/abs/2003.00421
2. W. Wang, M. Mao, and Z. Wang, “Stability and error estimates for the variable step-size BDF2 method for linear and semilinear parabolic equations,” arXiv:2003.03534, first submitted 2020-03-07; Advances in Computational Mathematics 47(1), article 8 (2021). https://arxiv.org/abs/2003.03534
