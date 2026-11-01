# Two preference reversals between marketing regimes with customer attrition

## Finding

For two finite-duration innovation–imitation–attrition regimes acting on one adopter fraction, the difference between the two possible campaign orders has **at most two strict sign reversals** as initial adoption varies over \((0,1)\). This bound is sharp even when both regimes have the **same strictly positive attrition rate**. An exact pair of positive-parameter regimes has two distinct interior crossovers, and the phenomenon persists under sufficiently small parameter perturbations preserving common attrition. Conversely, if the regimes share an equilibrium, their ordering difference has constant sign (or vanishes identically); in particular, the classical attrition-free Bass model cannot display even one such reversal.

The order means applying regime 1 for its prescribed duration followed by regime 2, versus regime 2 followed by regime 1 for their respective prescribed durations. Only the final adopter fraction is compared; the conclusion is not about optimizing general time-varying controls.

## Assumptions and scope

For \(i=1,2\), let \(p_i,q_i,r_i,T_i>0\), and let \(\Phi_i:[0,1]\to[0,1]\) be the time-\(T_i\) flow of
\[
\frac{dx}{dt}=(p_i+q_i x)(1-x)-r_i x.
\]
Here \(p_i\) is external innovation, \(q_i\) imitation and \(r_i\) departure or abandonment. The field is strictly positive at \(x=0\) and strictly negative at \(x=1\), hence \([0,1]\) is forward invariant. Define the order difference
\[
\Delta(x)=\Phi_2(\Phi_1(x))-\Phi_1(\Phi_2(x)).
\]
A *strict preference reversal* is an interior zero at which the sign of \(\Delta\) changes. Ties without a sign change are not counted.

## Proof

**1. Projective representation and universal bound.** Put \(\beta_i=q_i-p_i-r_i\) and \(\sigma_i=\sqrt{\beta_i^2+4p_iq_i}\), and define
\[
L_i=\begin{pmatrix}\beta_i/2&p_i\\q_i&-\beta_i/2\end{pmatrix},\qquad E_i=e^{T_iL_i}.
\]
The scalar Riccati equation is \(\dot x=p_i+\beta_i x-q_ix^2\). If \(E_i=(e^{(i)}_{jk})\), the standard linear-system quotient identity gives
\[
\Phi_i(x)=\frac{e^{(i)}_{11}x+e^{(i)}_{12}}{e^{(i)}_{21}x+e^{(i)}_{22}}.
\]
Since \(L_i^2=(\sigma_i^2/4)I\), explicitly
\[
E_i=\cosh(\sigma_iT_i/2)I+
\frac{2\sinh(\sigma_iT_i/2)}{\sigma_i}L_i.
\]
All four entries of \(E_i\) are positive: the off-diagonal entries are positive; for the diagonal entries use \(\sigma_i>|\beta_i|\) and \(\cosh u>\sinh u\) for \(u>0\). Thus all projective denominators are strictly positive on \([0,1]\).

Let \(P=E_2E_1=(P_{jk})\) and \(Q=E_1E_2=(Q_{jk})\). Direct subtraction yields
\[
\Delta(x)=\frac{N(x)}{(P_{21}x+P_{22})(Q_{21}x+Q_{22})},
\]
where
\[
N(x)=(P_{11}x+P_{12})(Q_{21}x+Q_{22})
-(Q_{11}x+Q_{12})(P_{21}x+P_{22}).
\]
The numerator is a polynomial of degree at most two. It is either zero identically, in which case the schedules tie for every initial condition, or has at most two distinct interior sign-changing roots. This proves the bound for arbitrary positive parameters and durations.

**2. Exact realization with common attrition.** Choose
\[
(p_1,q_1,r_1,T_1)=\left(6,7,12,\frac{\log 2}{17}\right),\qquad
(p_2,q_2,r_2,T_2)=\left(2,15,12,\frac{\log 2}{11}\right).
\]
For these regimes, \((\beta_1,\sigma_1)=(-11,17)\) and \((\beta_2,\sigma_2)=(1,11)\). In the formula for \(E_i\), \(e^{\sigma_i T_i}=2\), so multiplication by an irrelevant **positive** common factor yields the exact projective representatives
\[
A=\begin{pmatrix}40&12\\14&62\end{pmatrix},\qquad
B=\begin{pmatrix}34&4\\30&32\end{pmatrix}.
\]
More precisely, \(E_1=A/(34\sqrt2)\) and \(E_2=B/(22\sqrt2)\). Consequently the two compositions may be represented by
\[
P=BA=\begin{pmatrix}1416&656\\1648&2344\end{pmatrix},\qquad
Q=AB=\begin{pmatrix}1720&544\\2336&2040\end{pmatrix}.
\]
In these projective representatives the order difference is **exactly**
\[
\Delta(x)=\frac{128(3697x^2-3962x+493)}
{(1648x+2344)(2336x+2040)}.
\]
The numerator is positive at \(x=0\), negative at \(x=1/2\), and positive at \(x=1\). Its distinct simple roots are
\[
x_{\pm}=\frac{1981\pm2\sqrt{525435}}{3697},\qquad
0<x_-<\frac12<x_+<1.
\]
Numerically, \(x_-\approx0.143700863579282\) and \(x_+\approx0.927978876750715\). The first-then-second order wins below \(x_-\) and above \(x_+\), while the reverse order wins strictly between them. Both stages have abandonment rate \(12\), and their distinct stable equilibria are \(3/7\) and \(2/5\).

**3. Robustness.** The sign inequalities \(\Delta(0)>0\), \(\Delta(1/2)<0\), \(\Delta(1)>0\) are strict. The flow matrices depend continuously on all strictly positive model parameters and durations. They therefore persist in an open relative neighborhood of the exhibited parameters under the constraint \(r_1=r_2>0\). Two intermediate-value roots remain in \((0,1/2)\) and \((1/2,1)\); the universal quadratic bound shows there are exactly two simple sign-changing roots. This is a robust physical-parameter phenomenon, not an isolated symbolic coincidence.

**4. Shared-equilibrium obstruction.** Suppose the two flows share an equilibrium \(e\in[0,1]\). They then both fix \(e\), so \(\Delta(e)=0\). Their derivatives at \(e\) are well-defined and positive, and by the chain rule the derivative of each composition at \(e\) equals \(\Phi_2'(e)\Phi_1'(e)\); hence \(\Delta'(e)=0\). The rational expression above has a strictly positive denominator at \(e\), so \(N(e)=N'(e)=0\). As \(\deg N\le2\), necessarily \(N(x)=C(x-e)^2\) for some real constant \(C\) (including \(C=0\)). Therefore the schedule preference cannot reverse anywhere on \([0,1]\). In particular, if \(r_1=r_2=0\), both classical Bass fields have equilibrium \(e=1\), so attrition-free Bass switching has no preference reversal. The same rigidity holds for positive attrition whenever the equilibria coincide.

## Verification

The accompanying standalone `verify.py` checks the exact integer-matrix products and polynomial identity with rational arithmetic, locates the two distinct roots, verifies the physical-parameter projective lifts and their equilibria, and compares both composed flows against 200 independently integrated Runge–Kutta trajectories. Run with `python3 verify.py`; no third-party packages are required. These finite checks support, but do not replace, the preceding universal proof.

## Relationship to prior work

Bass (1969) introduced the innovation–imitation diffusion mechanism without the attrition term; the no-attrition shared equilibrium is acknowledged as the original case, not a new model. Fruchter and Van den Bulte (2011) study optimal spending controls in generalized Bass adoption and provide no fixed two-regime, nonzero-attrition initial-share crossover classification in the inspected model and appendices. Shi, Li and Bigdeli (2016) discuss churn in new-product diffusion and model selection, but the inspected model and empirical sections do not give these equal-attrition two-regime composition comparisons. Standard linear-fractional algebra already entails the quadratic bound; the specialized contribution is the sharp **physically admissible, equal-attrition two-reversal witness**, robustness, and the contrasting fixed-equilibrium obstruction in this application. Searches did not establish historical uniqueness; general results about composition of positive Riccati flows may cover this behavior.

## Limitations

This is a deterministic, well-mixed adopter-fraction model with each regime constant during its allotted duration, nonnegative state and ideal instantaneous switches. The result makes no claim about realized market campaigns, stochastic churn, finite-population fluctuations, price responses, or global optimal scheduling over many periods. Originality is conditional on the inspected literature and search coverage; no independent audit or independent historical-priority certification has occurred.

## References

1. Bass, F. M. (1969), *A New Product Growth for Model Consumer Durables*, Management Science 15(5), 215–227, DOI: 10.1287/mnsc.15.5.215 (publisher metadata: 1969-01-01).
2. Fruchter, G. E. and Van den Bulte, C. (2011), *Why the Generalized Bass Model Leads to Odd Optimal Advertising Policies*, International Journal of Research in Marketing 28, DOI: 10.1016/j.ijresmar.2011.03.005 (open-access manuscript inspected).
3. Shi, W., Li, Y. and Bigdeli, A. Z. (2016), *An Examination of NPD Models in the Context of Business Models*, Journal of Business Research, DOI: 10.1016/j.jbusres.2015.10.087 (open-access manuscript, relevant churn/model sections inspected).
