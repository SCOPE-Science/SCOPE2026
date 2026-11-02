# Sharp 20-percent seed threshold and 40-percent jump ceiling at the earliest SIR peak switch

## Finding
For the mass-action forward-Euler susceptible–infectious–removed (SIR) map with unit time step, the earliest possible **downward discontinuity** of cumulative attack by the day of maximum infectious prevalence, occurring when the prevalence peak moves from day two to day one as transmission increases, has two sharp universal constants:

1. Such a transversal, strictly positive-state two-to-one peak switch is possible **if and only if** the initially infectious fraction is greater than \(1/5\), assuming no initially removed individuals and allowing the recovery parameter to vary in \((0,1)\).
2. At every such switch, the size \(J\) of the downward jump satisfies \(0<J<2/5\). The supremum \(2/5\) is sharp, although no strictly positive-state transversal switch attains it.

Both statements quantify the same precise first peak-switch mechanism. In particular, at initial infectious fraction \(2/5\), a strictly admissible example has critical transmission \(4/3\), recovery \(28/75\), and downward attack-fraction jump exactly \(5992/28125\) (approximately \(0.21305\)). The threshold and supremum are not claims about later peak-switches or stochastic contact-network epidemics.

## Assumptions and scope
Use normalized fractions \((S_t,I_t,R_t)\) satisfying \(S_0=1-a\), \(I_0=a\), \(R_0=0\), with \(0<a<1\). For transmission \(\beta>0\) and recovery \(0<\gamma<1\), apply simultaneously at integer \(t\ge0\)
\[
 S_{t+1}=S_t-\beta S_t I_t,\qquad
 I_{t+1}=I_t+\beta S_t I_t-\gamma I_t,\qquad
 R_{t+1}=R_t+\gamma I_t.
\]
Here \(\beta\) is the mass-action coefficient per unit time step, **not** a per-contact Bernoulli probability; it may exceed one. All trajectories considered are strictly positive in the susceptible and infectious coordinates and nonnegative in the removed coordinate. This is guaranteed locally at the crossing by the inequalities given below, not assumed as a property of arbitrary Euler parameters.

For parameter values with a unique global infectious maximum at day \(p(\beta)\), the cumulative ever-infected fraction by the peak is \(H(\beta)=1-S_{p(\beta)}\). When two adjacent peak days tie, define one-sided limits of \(H\), independently of the tie-breaking convention.

A *transversal day-two-to-day-one peak switch* at \(\beta_*=\beta\) means that with \(a,\gamma\) fixed, for every sufficiently small \(h>0\), the unique global maximum is on day two at \(\beta-h\) and on day one at \(\beta+h\); at the crossing \(I_1=I_2>I_0,I_3\), and the derivative of \(\beta S_1(\beta)-\gamma\) with respect to transmission is negative.

## Proof
**1. Exact parameterization and positivity.** Set \(r=(1-a)/a\) and \(u=\beta a\). Then \(S_1=(1-a)(1-u)\). The crossing condition \(I_2=I_1>0\) is equivalent to \(\beta S_1=\gamma\), hence
\[
 \beta=u(1+r),\qquad \gamma=u(1-u)r,\qquad
 I_1=\frac{1+u^2r}{1+r}.
\]
The derivative of \(\beta S_1(\beta)\) with respect to \(\beta\) at fixed \(a\) is \((1-a)(1-2u)\). Its negativity is exactly \(u>1/2\). Positivity of \(S_1\) requires \(u<1\). At the crossing, the maximal infectious prevalence is \(I_1=I_2\), so strict Euler positivity requires \(\beta I_1<1\), or
\[
 \frac12<u<1,\qquad 0<r<\frac{1-u}{u^3}.\tag{1}
\]
Conversely (1) implies \(0<\gamma<1\): indeed \(\gamma<(1-u)^2/u^2<1\). It also implies strict positivity of \(S_1,S_2\), \(I_1=I_2>I_0\), and \(I_3<I_2\), since \(S_2<S_1=\gamma/\beta\). As \(S_t\) decreases, subsequent infectious prevalences decrease, so day one and day two are the only global maximizers at the crossing. By continuity, in a sufficiently small transmission neighborhood the full states remain positive, the infectious maximum is day two to the left and day one to the right. To justify indefinite positivity, note that after the strict peak the infectious sequence decreases; therefore the condition \(\beta I_t<1\) continues to hold, and the susceptible recurrence retains a positive factor. The tie is harmless because the claimed jump uses one-sided limits.

**2. Sharp seed threshold.** On \(u>1/2\), \((1-u)/u^3<4\). Thus (1) implies \(r<4\), equivalently \(a>1/5\). Conversely, given any \(a>1/5\), its \(r=(1-a)/a\) is less than four. Choose \(u>1/2\) sufficiently near \(1/2\) so that \(r<(1-u)/u^3\). The constructed \(\beta,\gamma\) then satisfy (1), yielding a strictly positive, transversal day-two-to-day-one switch. Thus the condition \(a>1/5\) is necessary and sufficient.

**3. Exact jump and its universal sharp upper bound.** At the crossing the left branch uses day two and the right branch day one, so
\[
 J=\lim_{h\downarrow0}H(\beta-h)-\lim_{h\downarrow0}H(\beta+h)
 =S_1-S_2=\beta S_1 I_1=\gamma I_1
 =\frac{u(1-u)r(1+u^2r)}{1+r}.
\]
For fixed \(u\), this expression increases strictly with \(r>0\) (differentiate \(r(1+u^2r)/(1+r)\)). Substituting the strict upper bound on \(r\) from (1) gives
\[
 0<J<\frac{(1-u)^2}{1-u+u^3}<\frac25,
\]
because
\[
 2(1-u+u^3)-5(1-u)^2
 =(2u-1)(u^2-2u+3)>0\quad(u>1/2).
\]
Sharpness follows by taking \(u\downarrow1/2\) and \(r\uparrow(1-u)/u^3\) from below. Each pair remains inside (1), while \(J\to2/5\); simultaneously \(a\to1/5\), \(\gamma\to1\) and \(\beta I_1\to1\). The limiting boundary point is deliberately **not** claimed to be an admissible transversal strictly positive switch.

**4. Exact nondegenerate witness.** Choose \(a=2/5\), \(r=3/2\), \(u=8/15\). Then \(\beta_*=4/3\), \(\gamma=28/75\), \(S_1=7/25\), \(I_1=214/375\), and \(\beta_* I_1=856/1125<1\). The derivative \((1-a)(1-2u)=-1/25\) is nonzero, and
\[
 J=\gamma I_1=\frac{5992}{28125}.
\]
Here \(H(\beta_*^-) =1-S_2\), \(H(\beta_*^+)=1-S_1=18/25\); the strictly positive disparity is the displayed \(J\).

## Verification
Run `python3 verify.py` using Python's standard library. The included checker reconstructs the witness, verifies the exact jump, checks the one-sided peak indices and state positivity at three rational transmission offsets, tests 840 rational admissible pairs for the derived inequalities, and verifies a rational family approaching the \(2/5\) supremum. Its finite tests support but do not replace the general algebraic proof. No infinite-time numerical truncation is invoked to prove global peak placement: monotonicity of \(S_t\) and the stepwise prevalence sign settle all subsequent times.

## Relationship to prior work
Ozbay, Nielsen, and Nguyen [1] introduced numerical studies of bifurcations in the peak-time cumulative attack fraction, observed jumps in its dependence on transmissibility, and explained qualitatively how shifts in the peak day cause them. Their deterministic Euler comparison and its equations are in Figure 6 and Methods. The present theorem *does not claim that peak jumps or nonmonotonicity are new*. Its contribution is the exact joint sharp seed threshold and jump ceiling for the earliest nontrivial downward branch switch within the strictly positive-state Euler SIR map, with a necessary-and-sufficient parametric characterization.

Diekmann, Othmer, Planqué, and Bootsma [2] develop a general discrete-time renewal formulation and investigate incidence peaks, without this Euler two-to-one switch extremal result. Lemos-Silva, Vaz, and Torres [3] instead construct a nonstandard difference scheme with a different incidence denominator and positivity properties. Nguyen, Freedman, Ozbay, and Levin [4] bound **continuous-time post-peak epidemic overshoot**, which is a distinct quantity from a discrete-time **discontinuity of attack by peak day**.

## Limitations
The bound \(2/5\) and seed cutoff \(1/5\) pertain only to the day-two-to-day-one transversal switch, zero initially removed fraction, mass-action forward Euler updating, and strict physical positivity. They do **not** bound jumps at later peak-day switches, stochastic graph epidemics, alternative SIR discretizations, changes of recovery alongside transmission, or an initially removed population. A strict single-day peak is used only off the crossing, where it holds. The supremum is approached but not attained in the strictly admissible class. Bibliographic searches cannot prove universal uniqueness; equivalent unindexed analysis remains possible. Independent assessment has not occurred.

## References
[1] S. A. Ozbay, B. F. Nielsen, and M. M. Nguyen, *Bifurcations in the Herd Immunity Threshold for Discrete-Time Models of Epidemic Spread*, arXiv:2212.06995, first publicly posted 2022-12-14, especially Figure 6, Discussion, Methods. https://arxiv.org/abs/2212.06995

[2] O. Diekmann, H. G. Othmer, R. Planqué, and M. C. J. Bootsma, *The discrete-time Kermack–McKendrick model: A versatile and computationally attractive framework for modeling epidemics*, PNAS 118 (2021), e2106332118. https://doi.org/10.1073/pnas.2106332118

[3] M. Lemos-Silva, S. Vaz, and D. F. M. Torres, *Exact solution for a discrete-time SIR model*, arXiv:2409.09157, 2024. https://arxiv.org/abs/2409.09157

[4] M. M. Nguyen, A. S. Freedman, S. A. Ozbay, and S. A. Levin, *Fundamental bound on epidemic overshoot in the SIR model*, J. R. Soc. Interface 20 (2023), 20230322. https://doi.org/10.1098/rsif.2023.0322
