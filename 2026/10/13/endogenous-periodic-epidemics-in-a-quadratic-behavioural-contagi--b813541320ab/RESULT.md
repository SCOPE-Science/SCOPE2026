# Endogenous periodic epidemics in a quadratic behavioural-contagion SIS model

## Finding

The transmission-modulated complex-contagion SIS model of Plank et al. [1], equations (7)–(8), has strictly positive nonconstant periodic solutions even without seasonal forcing or additional exposed/recovered compartments. In particular, set

\[
\mathcal R_0=\frac{640}{437},\quad q_c=1,\quad q_s=0,\quad
\tau=\frac{39}{10},\quad\chi=1,\quad\alpha=2.
\]

Its only equilibria in the physical square, in infection–behaviour coordinates \((I,B)\), are the disease-free saddle \((0,0)\) and the endemic repelling focus

\[
(I_*,B_*)=\left(\frac{43}{480},\frac14\right).
\]

For **every** initial condition \((I(0),B(0))\in(0,1)^2\) other than this equilibrium, the forward \(\omega\)-limit set is a nonconstant periodic orbit contained in \((0,1)^2\). This establishes sustained endogenous infection and behaviour oscillations for parameters with \(\tau<4\), where the model has no disease-free equilibrium with positive behaviour. The existence conclusion also persists for all \(q_c\) sufficiently close to \(1\) from below, keeping the other parameters fixed.

## Assumptions and scope

The source considers four disease–behaviour compartments [1]. Its transmission-modulated specialization has \(q_s=0\). For initial conditions independent across disease and behaviour, the exact invariant relation \(S_B(t)=S(t)B(t)\) reduces the full model to the two-dimensional system [1, equations (7)–(8), Supplement S1.1]. Put \(I=1-S\), where \(I\) is the total infectious fraction. At the parameters above, the reduced equations are

\[
\begin{aligned}
\dot I&=I\left[\frac{640}{437}(1-I)(1-B)-1\right]=:f(I,B),\\
\dot B&=2\left[\left(\frac{39}{10}B^2+I\right)(1-B)-B\right]=:g(I,B).
\end{aligned}
\]

The physical domain is \(0\le I,B\le1\), with dimensionless recovery rate equal to one. Parameters are within the source's allowed ranges: \(\mathcal R_0>1\), \(0\le q_c\le1\), and \(\alpha,\tau,\chi>0\). The theorem concerns deterministic autonomous mean-field trajectories. Initial conditions on invariant boundaries are excluded from the assertion about nonconstant periodic \(\omega\)-limits.

## Proof

**1. Invariance and equilibria.** On the faces \(I=0\), \(I=1\), \(B=0\), and \(B=1\) of the physical square, the respective normal components are \(0\), \(-1\), \(2I\ge0\), and \(-2\). Thus the square is forward invariant, and a solution starting in its interior remains interior by uniqueness and these strict inward/zero normal components.

The disease-free equation \(I=0\) gives \(\dot B=2B[(39/10)B(1-B)-1]\). Because \(B(1-B)\le1/4\) and \(39/40<1\), the only disease-free equilibrium is \((0,0)\). Its Jacobian eigenvalues are \(\mathcal R_0-1=203/437>0\) and \(-2<0\), so it is a saddle.

At a positive equilibrium, the infection nullcline implies

\[
I=I_0(B):=1-\frac{437}{640(1-B)},\qquad
0<B<b_0:=\frac{203}{640}.
\]

The behaviour nullcline becomes \(h(B)=0\), where

\[
h(B)=\frac{B}{1-B}-\frac{39}{10}B^2-I_0(B).
\]

The endpoint signs are \(h(0)=-203/640<0\) and \(h(b_0)=b_0/(1-b_0)-(39/10)b_0^2>0\): the latter is positive since \((39/10)b_0(1-b_0)<39/40<1\). Furthermore, for every \(0\le B\le b_0\),

\[
(1-B)^2h'(B)
=\frac{1077}{640}-\frac{39}{5}B(1-B)^2
\ge\frac{1077}{640}-\frac{39}{5}\frac4{27}
=\frac{15185}{28800}>0.
\]

Here \(B(1-B)^2\le4/27\) for \(B\in[0,1]\). Hence there is exactly one positive equilibrium. Direct substitution gives \((I_*,B_*)=(43/480,1/4)\).

**2. The endemic equilibrium repels.** The Jacobian, with row and column order \((I,B)\), is exactly

\[
J_*=
\begin{pmatrix}
-43/437&-43/360\\
3/2&31/120
\end{pmatrix}.
\]

Its trace, determinant, and discriminant are

\[
\operatorname{tr}J_*=\frac{8387}{52440}>0,\qquad
\det J_*=\frac{1075}{6992}>0,\qquad
(\operatorname{tr}J_*)^2-4\det J_*=-\frac{1620848231}{2749953600}<0.
\]

Thus both eigenvalues have strictly positive real part, and the equilibrium is a hyperbolic repelling focus. In particular, no distinct forward trajectory can have this equilibrium in its \(\omega\)-limit set: a sufficiently small positive-definite quadratic neighbourhood has strictly outward-pointing flow, as follows from the linear Lyapunov theorem for a repelling hyperbolic equilibrium.

**3. Uniform separation from the boundary.** Set \(R=640/437\), \(\tau=39/10\), and write \(g_0(B)=g(0,B)\). Since \(\tau B(1-B)\le39/40\),

\[
g_0(B)=2B[\tau B(1-B)-1]\le-\frac{B}{20}.
\]

For \(I>0\), define \(L=I e^{-30B}\). Its logarithmic derivative satisfies

\[
\begin{aligned}
\frac{d}{dt}\log L
&=R(1-I)(1-B)-1-30g(I,B)\\
&\ge(R-1)+(\tfrac32-R)B-(R+60)I\\
&\ge(R-1)-(R+60)I,
\end{aligned}
\]

using \(\tfrac32-R=31/874>0\). Define

\[
\varepsilon=\frac{R-1}{2(R+60)}=\frac{203}{53720}>0,
\qquad \delta=\varepsilon e^{-30}>0.
\]

If \(L\le\delta\), then \(I=Le^{30B}\le\varepsilon\), and the preceding bound implies \(\dot L/L\ge(R-1)/2>0\). Therefore the barrier \(L(t)\ge m:=\min\{L(0),\delta\}>0\) holds for all \(t\ge0\). Since \(I\ge L\), this yields \(I(t)\ge m\). When \(B\le m/4\), the inequality

\[
\dot B\ge2[I(1-B)-B]\ge2[m(1-m/4)-m/4]\ge m>0
\]

provides the lower barrier \(B(t)\ge\min\{B(0),m/4\}>0\). At \(I\ge1-1/(2R)\), \(\dot I\le-I/2<0\). At \(B\ge9/10\),

\[
\dot B\le 2[(\tau+1)(1-B)-B]
\le-\frac{41}{50}<0.
\]

Consequently, every forward interior orbit is contained in a compact rectangle strictly inside \((0,1)^2\), with bounds depending only on its positive initial condition.

**4. Periodic \(\omega\)-limits.** The trajectory therefore has a nonempty compact \(\omega\)-limit set in the plane's open physical square. The only equilibrium in that square is the hyperbolic repelling focus, which cannot lie in this \(\omega\)-limit set unless the trajectory is the equilibrium itself. By the Poincaré–Bendixson theorem, the \(\omega\)-limit set of every other interior trajectory is a nonconstant periodic orbit. This proves existence and the stronger forward-orbit statement.

**5. Non-extremal transmission protection.** For general \(q_c\in[0,1]\) near one, replace \((1-B)\) by \((1-q_cB)\) in the infection equation. The unique endemic equilibrium varies continuously by the implicit-function theorem because \(h'(1/4)>0\), and remains a repelling focus. Uniform strict positivity of \(h'\) on the entire admissible equilibrium interval at \(q_c=1\) gives, by compactness and continuity, uniqueness for all sufficiently close \(q_c<1\). The disease-free saddle and forward square invariance persist. The barrier proof is unchanged because \(R q_c\le R<3/2\). Consequently the Poincaré–Bendixson argument still applies for a nonempty interval of strictly incomplete transmission protection \(q_c<1\). No numerical width for that interval is asserted.

## Verification

Run `python3 verify.py` using only Python's standard library. Its `fractions.Fraction` checks reproduce both equilibrium equations, the Jacobian, exact trace/determinant/discriminant, the strict uniqueness and persistence inequalities, and the invariant-face bounds. Expected terminal output: `VERIFY_OK`. The analytic Poincaré–Bendixson step is justified by the proof, not by a finite numerical run. The program does not claim to certify all continuous trajectories computationally.

## Relationship to prior work

Plank et al. [1] introduced this precise nonlinear behavioural-uptake model, its two-dimensional invariant reduction, its equilibrium nullclines, and a ten-regime bifurcation atlas. Their displayed time series and publicly released numerical parameter sets use \(\alpha=1/4\) and \(\chi=1/5\) [1,2], whereas the present parameter set uses faster behavioural adjustment and stronger incidence feedback. The full text and supplementary classifications inspected do not contain the exact periodic-orbit construction or a theorem that implies it.

Zhou, Levin, and Leonard [3] obtained Hopf oscillations for a heterogeneous two-risk-class active-control SIS model, not the homogeneous two-variable quadratic social-contagion system above. Their homogeneous risk-averter submodel instead has a stable endemic equilibrium. Ryan et al. [4] developed the earlier *linear* behavioural-contagion model; that is a distinct vector field. Hence general behavioural epidemic oscillations and the Poincaré–Bendixson theorem are not claimed as new: the contribution is an explicit admissible autonomous parameter set, a rigorous global periodic-orbit conclusion, and the missing oscillatory regime for [1].

## Limitations

This is a theorem about deterministic mean-field dynamics, not a data-calibrated disease forecast. It does not establish uniqueness, hyperbolicity, or an exact period/amplitude of the periodic orbit. It makes no assertion for arbitrary four-compartment initial conditions lacking the invariant independence relation, nor for parameters outside the specified point and its demonstrated neighbourhood. A computational check of finitely many states is not the proof. Future versions of the motivating preprint or other unpublished analyses could contain related observations; literature comparisons cannot prove absolute uniqueness of this result.

## References

[1] M. J. Plank, M. Ryan, L. Chapman, R. I. Hickson, T. House, E. McBryde, and J. M. McCaw, *How complex behavioural contagion can prevent infectious diseases from becoming endemic*, arXiv:2604.10995v1 (first public version 2026-04-13). https://arxiv.org/abs/2604.10995. Equations (7)–(8), Secs. 2.1.1 and 3, Supplement S1.1–S1.3.

[2] M. J. Plank and J. M. McCaw, *Behaviour and disease SIS model with complex social contagion*, publicly released code associated with [1], `getPar.m` and `myVectorField.m`. https://github.com/michaelplanknz/behaviour_and_disease_SIS_model.

[3] Y. Zhou, S. A. Levin, and N. E. Leonard, *Active Control and Sustained Oscillations in actSIS Epidemic Dynamics*, IFAC-PapersOnLine 53(5), 807–812 (2020), arXiv:2007.01424. https://arxiv.org/abs/2007.01424.

[4] M. Ryan, E. Brindal, M. Roberts, and R. I. Hickson, *A behaviour and disease transmission model: Incorporating the Health Belief Model for human behaviour into a simple transmission model*, J. R. Soc. Interface 21 (2024), 20240038. https://doi.org/10.1098/rsif.2024.0038.
