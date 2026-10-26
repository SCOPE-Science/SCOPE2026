# Fixed-floor Patankar correction: exact shadow dynamics and a three-regime equilibrium bias

## Finding

For the final-only Patankar predictor–corrector equation (25) of Nurkhametova–Gomillion–Subrahmanya–Sandu, built on their two-stage SDIRK21 predictor (29) and using a *fixed*, rather than step-dependent, denominator floor \(\varepsilon>0\), timestep refinement generally converges to a **different ordinary differential equation**. On a two-species reversible exchange system the limiting differential equation and its unique attracting equilibrium can be determined exactly. There is a sharp three-regime transition from a square-root rate ratio, through a mixed quadratic branch, to the true linear rate ratio. The original equilibrium can be displaced at *every* positive stepsize while mass and positivity remain preserved.

## Assumptions and scope

Let \(\alpha>\beta>0\), \(m>0\), \(\varepsilon>0\), and
\[
G=\begin{pmatrix}-\alpha&\beta\\\alpha&-\beta\end{pmatrix},\qquad
\dot y=Gy,\qquad y=(x,m-x)^\top\ge0.
\]
The exact equation conserves mass \(m\), and its equilibrium is
\(y^\dagger=(m\beta/(\alpha+\beta),m\alpha/(\alpha+\beta))^\top\).
Use the source's **final-only** correction, not the different stage-by-stage correction. Set
\(\gamma=1-1/\sqrt2\), \(b_1=1-\gamma\), \(b_2=\gamma\); for an input \(y\) and timestep \(h>0\), predict
\[
(I-h\gamma G)Y_1=y,\quad
(I-h\gamma G)Y_2=y+h(1-\gamma)GY_1,\quad p=Y_2.
\]
Define \(S_j=\operatorname{diag}(\max((Y_j)_i,0)/\max(p_i,\varepsilon))_{i=1}^2\),
\(B_h(y)=G(b_1S_1+b_2S_2)\), and corrected step
\(T_h(y)=(I-hB_h(y))^{-1}y\). Maxima act componentwise; \(\varepsilon\) is kept constant as \(h\downarrow0\). The clip is the one in the source's definition (21) and equations (25a–c). For \(h\) sufficiently small, all stage entries are nonnegative; the stated formula also covers clipping outside that range.

Define \(\phi_\varepsilon(u)=u^2/\max(u,\varepsilon)\) for \(u\ge0\), and \(r=\beta/\alpha\in(0,1)\).

**Refinement-limit theorem.** For every \(T>0\) and every initial \(y_0\ge0\) of mass \(m\), iterating \(T_{T/N}\) exactly \(N\) times converges as \(N\to\infty\) to the time-\(T\) value of
\[
\dot x=\beta\phi_\varepsilon(m-x)-\alpha\phi_\varepsilon(x),\qquad
\dot y_2=-\dot x.
\]
The global error against this modified equation is \(O_T(N^{-1})\). This statement is **not** convergence to the original equation unless the two flows happen to agree on the trajectory.

**Exact shadow-equilibrium classification.** The modified flow has exactly one equilibrium \(x_*\in(0,m)\), attracting every initial concentration on the mass simplex. Its explicit value is
\[
x_*=\begin{cases}
\displaystyle\frac{m\sqrt r}{1+\sqrt r},&0<m\le\varepsilon(1+\sqrt r),\\[5pt]
\displaystyle\frac{\sqrt{r^2\varepsilon^2+4r\varepsilon m}-r\varepsilon}{2},
&\varepsilon(1+\sqrt r)<m<\varepsilon(1+r^{-1}),\\[5pt]
\displaystyle\frac{mr}{1+r},&m\ge\varepsilon(1+r^{-1}).
\end{cases}\]
At either boundary the adjacent formulas coincide. The shadow equilibrium agrees with the exact one **if and only if** \(\varepsilon\le m\beta/(\alpha+\beta)\). For larger fixed floors, the minority species has a strictly positive equilibrium bias.

**A finite-timestep obstruction.** If \(\varepsilon>m\) and the starting state is the exact equilibrium \(y^\dagger=(x,z)\), then for **every** \(h>0\)
\[
(T_h(y^\dagger))_1-x
=\frac{h\,\alpha\beta m^2(\alpha-\beta)/(\alpha+\beta)^2}
{\varepsilon+2h\alpha\beta m/(\alpha+\beta)}>0.
\]
More generally, for any \(\varepsilon>0\) the original equilibrium is fixed by this corrected step if and only if \(\varepsilon\le x\). Nevertheless every corrected step preserves total mass and maps nonnegative vectors to nonnegative vectors.

For the exact-rational choice \((\alpha,\beta,m,\varepsilon)=(4,1,1,2)\) with \(y_0=(1/5,4/5)\), the true solution is stationary. The modified limit instead has
\[
 x(T)=\frac{3e^{2T}-1}{9e^{2T}+1},\qquad
 \lim_{N\to\infty}\big|(T_{T/N}^{\,N}(y_0))_1-1/5\big|
 =\frac{3e^{2T}-1}{9e^{2T}+1}-\frac15>0\quad(T>0).
\]
In particular, for \(h=1\) the corrected first component is exactly \(1/3\), rather than \(1/5\).

## Proof

**Positivity, mass and reconstruction.** Each predicted stage equals a rational matrix function of \(hG\); since \(I-h\gamma G\) is invertible and \(G\) is fixed, \(Y_j=y+O(h)\) and \(p=y+O(h)\) uniformly for \(0\le x\le m\), as \(h\downarrow0\). By the source definition, \(B_h=G\operatorname{diag}(s_1,s_2)\) for \(s_i\ge0\). It has nonnegative off-diagonals, nonpositive diagonals and zero column sums. Thus the resolvent is a nonnegative, column-stochastic matrix for all \(h>0\), proving positivity and mass preservation without assuming either property in the subsequent asymptotics.

**Local limit and convergence.** The map \(u\mapsto1/\max(u,\varepsilon)\) is Lipschitz and bounded on the relevant compact interval, and clipping is Lipschitz. Hence, uniformly on the mass simplex,
\[
 s_i=\frac{y_i}{\max(y_i,\varepsilon)}+O(h),\quad
 B_h=G\operatorname{diag}\left(\frac{y_i}{\max(y_i,\varepsilon)}\right)+O(h).
\]
Expanding the resolvent in the bounded matrix \(B_h\) yields
\(T_h(y)=y+hG(\phi_\varepsilon(y_1),\phi_\varepsilon(y_2))^\top+O(h^2)\), uniformly. The modified vector field is Lipschitz on the compact simplex. The predictor maps, positive-part, denominator floor, and inverse resolvent are uniformly Lipschitz in \(y\) for small \(h\), giving \(\|T_h(u)-T_h(v)\|\le(1+Ch)\|u-v\|\). Comparing each step against the modified ODE's exact time-\(h\) map, a discrete Grönwall inequality supplies the uniform finite-horizon \(O(h)\) global bound. This proves the refinement-limit theorem even for boundary initial states.

**Unique equilibrium and sharp branches.** The scalar right-hand side
\(f(x)=\beta\phi_\varepsilon(m-x)-\alpha\phi_\varepsilon(x)\) is strictly decreasing for \(0\le x\le m\), with \(f(0)>0>f(m)\); thus it has a unique globally attracting zero. At any such zero, \(x<m-x\), since \(\alpha>\beta\) and \(\phi_\varepsilon\) is strictly increasing. Both values below the floor give \(\alpha x^2=\beta(m-x)^2\) and the square-root branch, valid up to \(m=\varepsilon(1+\sqrt r)\). With \(x<\varepsilon\le m-x\), the equation becomes \(x^2=r\varepsilon(m-x)\), giving the positive quadratic root; its two validity inequalities are exactly the middle parameter range. Finally if \(\varepsilon\le x<m-x\), the equation reduces to \(\alpha x=\beta(m-x)\) and requires \(m\ge\varepsilon(1+r^{-1})\). There is no missing region by uniqueness; the formulas agree at transition points.

**Exact finite-step defect.** At the true equilibrium, both SDIRK predictor stages and predicted endpoint are exactly \(y^\dagger\) for every \(h>0\). Therefore \(B_h=G\operatorname{diag}(x/\max(x,\varepsilon),z/\max(z,\varepsilon))\). For any such column-conservative two-state matrix, direct inversion gives
\[
 (T_h(y^\dagger))_1-x
 =\frac{h\{\beta z^2/\max(z,\varepsilon)-\alpha x^2/\max(x,\varepsilon)\}}
{1+h\{\alpha x/\max(x,\varepsilon)+\beta z/\max(z,\varepsilon)\}}.
\]
Since \(\alpha x=\beta z>0\) and \(z>x\), the numerator is zero precisely when \(\varepsilon\le x\), otherwise positive. If \(\varepsilon>m\), both denominators equal \(\varepsilon\); inserting \(x=m\beta/(\alpha+\beta)\) and \(z=m\alpha/(\alpha+\beta)\) yields the displayed sharp defect. For the numeric example, the modified equation reads \(\dot x=(1-2x-3x^2)/2\); the transformed coordinate \((1-3x)/(1+x)\) decays exactly as \(e^{-2T}\), proving the closed-form nonzero limiting error. No finite simulation or finite grid is used to assert the infinite-iteration conclusion.

## Verification

Run `python verify.py` with NumPy available. The standalone script independently solves both SDIRK predictor linear systems and the corrected resolvent at each timestep, checks conservation and positivity, exactly verifies the rational one-step equilibrium defect for four timestep values, and checks the proposed equilibrium branches on a parameter grid. It compares a refined trajectory to the independently solved modified differential equation. Symbolic algebra and the preceding uniform-error proof, not this finite experiment, establish the theorem for all parameters and refinements.

## Relationship to prior work

Nurkhametova, Gomillion, Subrahmanya and Sandu (arXiv:2602.15271v1), definitions (21), (25) and SDIRK2 example (29), define the scheme and establish positivity, conservation and an error estimate with an additive \(O(\varepsilon)\) contribution (their equation (34)); Remark 3.19 proposes \(\varepsilon=O(h^{p+1})\). This work examines the different, explicitly fixed-\(\varepsilon\) regime and determines its limiting modified vector field, complete two-state equilibrium diagram, and exact finite-step equilibrium displacement. The source's additive error estimate alone neither asserts nor implies these exact identities; no assertion contradicts its recommended step-dependent scaling.

Torlo, Öffner and Ranocha (arXiv:2108.07347), section 2.7, analyze equilibrium and near-zero-state behavior of earlier, distinct modified Patankar schemes. Their equilibrium-preservation statements do not cover the fixed-denominator-floor final-only correction (25). No universal novelty claim is made beyond the material inspected: a specialized equivalent derivation may exist in other work.

## Limitations

The theorem concerns the **final-only** corrector (25) with the stated two-stage SDIRK predictor, fixed \(\varepsilon\), two constant-rate reversible compartments and exact arithmetic. It does not apply to the alternative stage-by-stage corrector (28)/(31), to a floor shrinking with \(h\), to arbitrary nonlinear reaction networks, or to adaptive tolerance selection. The \(O(h)\) rate refers to the *modified* limiting equation, not the original equation. The equilibrium diagram is for the continuous shadow equation, not a complete classification of fixed-positive-stepsize numerical attractors. Earlier specialized bibliographic coverage remains possible.

## References

1. K. Nurkhametova, R. J. Gomillion, A. N. Subrahmanya, A. Sandu, *A Patankar predictor-corrector approach for positivity-preserving time integration*, arXiv:2602.15271v1 (first public 2026-02-17), especially Definition 3.13, equations (25), (29), (34), Remark 3.19. https://arxiv.org/abs/2602.15271
2. D. Torlo, P. Öffner, H. Ranocha, *Issues with Positivity-Preserving Patankar-type Schemes*, arXiv:2108.07347v1 (2021), especially section 2.7. https://arxiv.org/abs/2108.07347
