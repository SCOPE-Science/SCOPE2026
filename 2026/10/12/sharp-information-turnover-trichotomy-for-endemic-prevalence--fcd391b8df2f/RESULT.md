# Sharp information-turnover trichotomy for endemic prevalence
## Finding
For the reduced SIRM system in Fang, Liu and Du (2026), put \(p=p_0\sigma\), \(u_1=u_0\sigma\), and \(k=a/b\). When \(\mathcal R_0>1\), define
\[
c=(p+\mu)(\mathcal R_0-1)>0.
\]
The unique endemic infective level \(I_k\) from the source's equation (19) obeys
\[
c=I_k\left(\beta+\frac{k u_1}{1+k u_2 I_k}\right).
\]
It is strictly decreasing in \(k\), with the exact representation
\[
I_k=\frac{2c}{\beta+k(u_1-cu_2)+\sqrt{[\beta+k(u_1-cu_2)]^2+4\beta k u_2c}}.
\]
Moreover, the large-information-turnover limit has a sharp trichotomy:
\[
\begin{cases}
kI_k\to \dfrac{c}{u_1-cu_2},&u_1>cu_2,\\[4pt]
\sqrt{k}\,I_k\to \sqrt{\dfrac{c}{\beta u_2}},&u_1=cu_2,\\[6pt]
I_k\to \dfrac{c-u_1/u_2}{\beta},&u_1<cu_2.
\end{cases}
\]
Thus increasing the information growth-to-decay ratio can lower endemic prevalence even though it leaves \(\mathcal R_0\) unchanged. If the maximal information-driven vaccination strength \(u_1/u_2\) exceeds the excess endemic drive \(c\), prevalence can be driven arbitrarily close to zero at rate \(k^{-1}\); at equality the suppression rate slows to \(k^{-1/2}\); below equality a positive endemic floor remains.

## Assumptions and scope
The claim uses the source's reduced \(\tau=0\) decoupled system (18), with positive \(\beta,u_1,u_2,a,b\), and \(\mathcal R_0>1\). The source defines \(p=p_0\sigma\) and \(u_1=u_0\sigma\), and its endemic equilibrium has \(M^*=(a/b)I^*\). The parameter \(k=a/b\) is varied while the other reduced-system parameters are fixed.

The result is only an equilibrium statement. It does not assert local or global stability for every \(k\), does not claim finite-\(k\) eradication, and does not transfer automatically to the finite-delay perturbed system.

## Proof
The source's equation (19), together with \(\widetilde u_1=ku_1\) and \(\widetilde u_2=ku_2\), is exactly
\[
c=I_k\left(\beta+\frac{ku_1}{1+ku_2I_k}\right).
\]
Define
\[
F(I,k)=\beta I+\frac{ku_1I}{1+ku_2I}-c.
\]
For \(I>0\) and \(k>0\),
\[
F_I=\beta+\frac{ku_1}{(1+ku_2I)^2}>0,
\qquad
F_k=\frac{u_1I}{(1+ku_2I)^2}>0.
\]
The source proves there is one positive endemic root. The implicit-function theorem therefore gives
\[
\frac{dI_k}{dk}=-\frac{F_k}{F_I}<0,
\]
which proves strict monotonic decrease.

Multiplying the equilibrium equation by \(1+ku_2I_k\) yields
\[
\beta ku_2 I_k^2+[\beta+k(u_1-cu_2)]I_k-c=0.
\]
The positive quadratic root, rationalized to avoid cancellation, is
\[
I_k=\frac{2c}{\beta+k(u_1-cu_2)+\sqrt{[\beta+k(u_1-cu_2)]^2+4\beta ku_2c}}.
\]
If \(u_1>cu_2\), divide the denominator by \(k\) to obtain \(kI_k\to c/(u_1-cu_2)\). If \(u_1=cu_2\), the quadratic becomes
\[
\beta ku_2I_k^2+\beta I_k-c=0,
\]
and division by \(k\), followed by the scaling \(J_k=\sqrt{k}\,I_k\), gives \(J_k\to\sqrt{c/(\beta u_2)}\). Finally, if \(u_1<cu_2\), divide the quadratic by \(k\). Any nonnegative limit solves
\[
\beta u_2 I^2+(u_1-cu_2)I=0.
\]
The positive branch therefore converges to
\[
\frac{cu_2-u_1}{\beta u_2}=\frac{c-u_1/u_2}{\beta}.
\]
These three alternatives exhaust the sign of \(u_1-cu_2\).

## Verification
The algebra was reconstructed directly from equations (18)--(21) of the cited source. The bundled `verify.py` evaluates the exact root formula at high precision in all three regimes, checks the equilibrium residual, verifies monotonicity over a geometric sequence of \(k\)-values, and checks convergence of the three scaled limits. These computations are consistency checks; the proof above is analytic and does not rely on finite sampling.

## Relationship to prior work
Fang, Liu and Du derive the reproduction number, note that \(u_0,u_2,a,b\) do not enter it, and prove existence of a unique endemic equilibrium when \(\mathcal R_0>1\). Their numerical section varies \(u_0\) and \(u_2\) to study infection peaks and saturation. The inspected full text does not state monotonic dependence of endemic prevalence on \(a/b\), nor the three-regime large-\(a/b\) asymptotic above.

Buonomo, d'Onofrio, Kassa and Workineh (2022) study a different information-dependent meningitis model. Their numerical analysis reports that endemic infection decreases with information coverage and a vaccination-sensitivity slope, but those parameters are not the information growth-to-decay ratio used here and their model does not imply this saturation trichotomy. Kumar, Srivastava and Gupta (2019) study information-induced vaccination together with saturated treatment and report multiple endemic equilibria and bifurcations in a different SVIR model; accessible abstract-level material did not supply the present reduced-equilibrium law.

## Limitations
The result is source-specific to the reduced SIRM equilibrium equation and does not establish stability, transient peak monotonicity, or a theorem for positive information delay. The limit \(k\to\infty\) is a mathematical parameter limit; biological feasibility of arbitrarily large information growth-to-decay ratios is not asserted. A closely related closed-form asymptotic could exist in literature not recovered by the searches, especially in the broad behavioral-epidemiology literature.

## References
1. J. Fang, J. Liu, and Z. Du, “Dynamics of multiple time scale SIRM model with information-dependent vaccination,” *Discrete and Continuous Dynamical Systems - B* 39 (2026), 272–297. DOI: 10.3934/dcdsb.2026090.
2. B. Buonomo, A. d'Onofrio, S. M. Kassa, and Y. H. Workineh, “Modeling the effects of information-dependent vaccination behavior on meningitis transmission,” *Mathematical Methods in the Applied Sciences* 45 (2022), 732–748. DOI: 10.1002/mma.7808.
3. A. Kumar, P. K. Srivastava, and R. P. Gupta, “Nonlinear dynamics of infectious diseases via information-induced vaccination and saturated treatment,” *Mathematics and Computers in Simulation* 157 (2019), 77–99. DOI: 10.1016/j.matcom.2018.09.024.
