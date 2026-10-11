# Sharp stationary second-moment corridor for the Newton–Leipnik flow

## Finding
For the nominal Newton–Leipnik flow
\[
\dot x=-\frac25x+y+10yz,\qquad
\dot y=-x-\frac25y+5xz,\qquad
\dot z=\frac7{{40}}z-5xy,
\]
let \(\mu\) be a compactly supported invariant Borel probability measure and set
\[
A=\int x^2\,d\mu,\qquad B=\int y^2\,d\mu,\qquad C=\int z^2\,d\mu.
\]
Then
\[
A+B=\frac{{21}}{{16}}C.
\]
If \(C>0\), the ratio \(t=A/C\) lies in the sharp interval
\[
t_-\le t\le t_+,
\qquad
t_\pm=\frac{{637\pm35\sqrt{{257}}}}{{928}}.
\]
Numerically, \(t_-\approx0.08179667676093867\) and \(t_+\approx1.2910481508252682\).

Equality has a complete rigidity description. Define
\[
z_\pm=\frac{{5\pm\sqrt{{257}}}}{{100}},
\qquad
\lambda_\pm=\frac{{\pm\sqrt{{257}}-15}}{{8}},
\qquad
r_\pm=\sqrt{{\frac{{7z_\pm}}{{200\lambda_\pm}}}}.
\]
For each sign \(\varepsilon\in\{{-1,1\}}\), let
\[
p_{{\pm,\varepsilon}}=(\varepsilon r_\pm,\varepsilon\lambda_\pm r_\pm,z_\pm).
\]
The lower endpoint \(t_-\) occurs exactly for invariant measures supported on \(\{{0,p_{{-,1}},p_{{-,-1}}\}}\) with positive total mass on the two nonzero points. The upper endpoint \(t_+\) has the analogous characterization with the \(+\) branch. Consequently every non-equilibrium ergodic invariant measure satisfies both inequalities strictly. If \(C=0\), then \(A=B=0\) and \(\mu=\delta_0\).

## Assumptions and scope
The statement uses the classical nominal feedback parameters \(2/5\) and \(7/40\). The measure is assumed compactly supported so that the polynomial generator identities below can be integrated without boundary or integrability issues. No assumption of absolute continuity, uniqueness, mixing, or physicality is imposed.

The conclusion concerns all compact stationary statistical states of this fixed flow, including equilibrium mixtures, periodic-orbit measures, and any invariant measures carried by the two classical strange-attractor regimes.

## Proof
For a polynomial observable \(F\), invariance and compact support give \(\int LF\,d\mu=0\), where \(L\) is the vector-field generator.

Take
\[
F_1=\frac{x^2}{2}+z^2.
\]
Direct differentiation gives
\[
LF_1=-\frac25x^2+xy+\frac7{20}z^2,
\]
so, with \(M=\int xy\,d\mu\),
\[
M=\frac25A-\frac7{20}C.
\]
Next take
\[
F_2=\frac{y^2+z^2}{2}.
\]
Then
\[
LF_2=-xy-\frac25y^2+\frac7{40}z^2,
\]
and hence
\[
M=\frac7{40}C-\frac25B.
\]
Equating the two expressions for \(M\) yields
\[
A+B=\frac{21}{16}C.
\]
If \(C=0\), nonnegativity gives \(A=B=0\), so the measure is concentrated at the origin.

Assume \(C>0\) and set \(t=A/C\). Then
\[
\frac{B}{C}=\frac{21}{16}-t,
\qquad
\frac{M}{C}=\frac25t-\frac7{20}.
\]
Cauchy–Schwarz, \(M^2\le AB\), is therefore equivalent to
\[
464t^2-637t+49\le0.
\]
Its two roots are precisely \(t_-\) and \(t_+\), proving the corridor.

For equality, Cauchy–Schwarz forces \(y=\lambda x\) on the support for some constant \(\lambda\). Because the support of an invariant probability measure is flow invariant, the vector field must be tangent to this plane. On \(y=\lambda x\),
\[
\frac{d}{dt}(y-\lambda x)
=x\bigl(-(1+\lambda^2)+(5-10\lambda^2)z\bigr).
\]
A nonzero support point therefore has constant height
\[
z=\frac{1+\lambda^2}{5-10\lambda^2}.
\]
Local invariance then forces \(\dot z=0\), and hence \(x^2\) is constant there; consequently the point is an equilibrium. Solving the equilibrium equations gives exactly the two sign-pairs \(p_{{-,\varepsilon}}\) and \(p_{{+,\varepsilon}}\) above, in addition to the origin. Their ratios \(x^2/z^2\) are respectively \(t_-\) and \(t_+\). Thus equality measures are exactly the stated mixtures, and ergodicity makes every non-equilibrium stationary state strict.

## Verification
An independent symbolic-algebra script included with this result expands both generator identities, factors the Cauchy–Schwarz defect, solves the endpoint polynomial exactly, and substitutes both equilibrium branches back into all three differential equations. Its recorded output is `VERIFY_OK` with the two exact endpoint roots and their decimal values.

The proof itself is analytic. No finite trajectory simulation or numerical enumeration is used to infer an infinite-time statement.

## Relationship to prior work
Leipnik and Newton introduced the rigid-body model with linear feedback and reported its two strange attractors in 1981. A later full-text treatment by Song studies the same Newton–Leipnik equation with upper and lower strange attractors and develops feedback controls for moving between or stabilizing those regimes. Those sources motivate the need for exact statistics that apply simultaneously to both coexisting recurrent regimes.

The inspected same-object literature discusses the attractors, equilibria, bifurcation/control behavior, and synchronization questions. No inspected statement supplies the sharp stationary second-moment ratio interval together with its equality classification. The corridor is not a consequence of merely knowing that two attractors coexist: it uses two exact generator cancellations and the equality case of the positive-semidefinite second-moment constraint.

## Limitations
The result is for the nominal Newton–Leipnik coefficients only. It does not prove existence, uniqueness, ergodicity, mixing, or absolute continuity of either strange-attractor measure, and it does not compute a full invariant density.

The original 1981 article's complete body was not available in the inspected lawful sources, so an equivalent short moment calculation could in principle appear there or in differently indexed rigid-body literature. This is a residual originality risk. The later same-object full text and targeted statement-level searches did not reveal such a formula.

## References
1. R. B. Leipnik and T. A. Newton, “Double strange attractors in rigid body motion with linear feedback control,” *Physics Letters A* 86(2), 63–67 (2 November 1981), DOI 10.1016/0375-9601(81)90165-1.
2. Y.-Z. Song, “The open-plus-closed loop (OPCL) method for chaotic systems with multiple strange attractors,” *Chinese Physics B* 16(7), 1918–1922 (2007), DOI 10.1088/1009-1963/16/7/019.
