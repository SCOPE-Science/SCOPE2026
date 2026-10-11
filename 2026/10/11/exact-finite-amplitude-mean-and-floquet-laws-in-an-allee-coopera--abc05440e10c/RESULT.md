# Exact finite-amplitude mean and Floquet laws in an Allee–cooperation predator–prey cycle
## Finding
For the Xue predator–prey system \(\dot x=x(a-bx-m/(x+\alpha))-cxy\), \(\dot y=y(-e+\varepsilon c x)/(y+\beta)\), with all parameters positive, \(0<\varepsilon<1\), and positive coexistence equilibrium \(x_*=e/(\varepsilon c)\), \(y_*=[a-bx_*-m/(x_*+\alpha)]/c>0\), every compactly supported invariant Borel probability measure \(\mu\) whose support lies in \((0,\infty)^2\) satisfies \(\int x\,d\mu=x_*\) and the exact predator-mean defect law \[y_*-\int y\,d\mu=\frac{m}{c(x_*+\alpha)^2}\int\frac{(x-x_*)^2}{x+\alpha}\,d\mu.\] Equality in the second law holds only for the coexistence-equilibrium Dirac measure; hence every non-equilibrium compact interior invariant measure, in particular every positive nonconstant periodic orbit, has mean predator density strictly below \(y_*\) while its mean prey density is exactly \(x_*\). Moreover, if \(\Gamma\) is a positive nonconstant periodic orbit of period \(T\), its nontrivial planar Floquet multiplier is exactly \[\rho_\Gamma=\exp\!\left(\int_0^T x(t)\left[-b+\frac{m}{(x(t)+\alpha)^2}\right]dt\right).\] For the source's Example 4 parameters \((a,b,c,e,m,\alpha,\beta,\varepsilon)=(3,9/10,2,1,23/10,1,2,9/10)\), every positive nonconstant cycle therefore obeys \(\bar x=5/9\) and \[\bar y=\frac{143}{280}-\frac{1863}{3920}\frac1T\int_0^T\frac{(x(t)-5/9)^2}{x(t)+1}\,dt<\frac{143}{280}.\]

## Assumptions and scope
Consider the autonomous planar system
\[
\dot x=x\left(a-bx-\frac{m}{x+\alpha}\right)-cxy,\qquad
\dot y=\frac{y}{y+\beta}(-e+\varepsilon c x),
\]
with \(a,b,c,e,m,\alpha,\beta>0\), \(0<\varepsilon<1\), and
\[
x_*=\frac{e}{\varepsilon c},\qquad
y_*=\frac1c\left(a-bx_*-\frac{m}{x_*+\alpha}\right)>0.
\]
The invariant-measure statements concern compactly supported invariant Borel probability measures whose support is contained in the strict positive quadrant. The Floquet statement concerns a positive nonconstant periodic orbit. No assertion is made about existence of a periodic orbit outside parameter regimes where one is independently known to exist.

## Proof
Put \(H(y)=y+\beta\log y\). On the strict positive quadrant,
\[
\frac{d}{dt}H(y)=\left(1+\frac{\beta}{y}\right)\dot y=-e+\varepsilon c x=\varepsilon c(x-x_*).
\]
For an invariant probability measure with compact interior support, integration of this smooth coboundary gives
\[
\int x\,d\mu=x_*.
\]
Next, with \(G(x)=\log x\),
\[
\frac{d}{dt}G(x)=a-bx-\frac{m}{x+\alpha}-cy.
\]
Stationarity and the first identity yield
\[
c\int y\,d\mu=a-bx_*-m\int\frac1{x+\alpha}\,d\mu.
\]
Subtract the coexistence-equilibrium relation \(cy_*=a-bx_*-m/(x_*+\alpha)\). For \(u=x+\alpha\) and \(u_0=x_*+\alpha\), the exact algebraic identity
\[
\frac1u-\frac1{u_0}=-\frac{u-u_0}{u_0^2}+\frac{(u-u_0)^2}{u u_0^2}
\]
and \(\int(u-u_0)\,d\mu=0\) give
\[
y_*-\int y\,d\mu=
\frac{m}{c(x_*+\alpha)^2}
\int\frac{(x-x_*)^2}{x+\alpha}\,d\mu.
\]
The right-hand side is nonnegative. If it vanishes then \(x=x_*\) on the support. Invariance then forces \(y=y_*\), because \(\dot x=cx_*(y_*-y)\) on the line \(x=x_*\). Thus equality occurs only for the Dirac measure at the coexistence equilibrium.

For the periodic-orbit multiplier, write the vector field as \(F=(f,g)\). Direct differentiation gives the exact divergence decomposition
\[
\nabla\!\cdot F=
\frac d{dt}\log x+
\frac d{dt}\log\left(\frac y{y+\beta}\right)
+x\left(-b+\frac{m}{(x+\alpha)^2}\right).
\]
Both logarithmic terms integrate to zero over a positive period. Liouville's formula for the planar variational equation says that the product of the two Floquet multipliers is the exponential of the divergence integral; one multiplier is \(1\) from time translation. Hence the other multiplier is
\[
\rho_\Gamma=\exp\!\left(\int_0^T x(t)\left[-b+\frac{m}{(x(t)+\alpha)^2}\right]dt\right).
\]
This proves the stated finite-amplitude laws.

## Verification
A dependency-free exact-arithmetic checker is supplied as `verify.py`. It verifies the transformed-predator coboundary algebra, the reciprocal identity used in the defect formula, the divergence decomposition at rational test points, and the exact Example 4 fractions
\[
x_*=\frac59,\qquad y_*=\frac{143}{280},\qquad
\frac{m}{c(x_*+\alpha)^2}=\frac{1863}{3920}.
\]
These computations are consistency checks; the proof above is symbolic and does not rely on numerical simulation.

## Relationship to prior work
Xue's article defines exactly this model, gives the coexistence equilibrium, proves a Hopf condition, proves a single-limit-cycle result under stated hypotheses, and numerically exhibits an attracting cycle in Example 4. The article does not state the finite-amplitude invariant-measure mean identities, the exact predator deficit, or the simplified nontrivial Floquet multiplier derived here.

The classical Volterra literature contains time-average-equals-equilibrium statements for Volterra interaction systems. That does not directly imply this result: the present predator equation has the nonlinear mortality/cooperation factor \(y/(y+\beta)\), and the prey equation contains the reciprocal additive-Allee term \(m/(x+\alpha)\). The observable \(y+\beta\log y\) is what restores an exact prey-mean law here, while the reciprocal Allee term produces a strictly positive, explicitly weighted predator-mean defect. The multiplier formula uses a second cancellation specific to the same nonlinear predator factor.

## Limitations
The result is conditional on compact interior recurrence and does not prove that such recurrence exists for arbitrary parameters. It does not determine the sign of the Floquet exponent from parameters alone, because the remaining integral depends on the cycle's prey distribution. It does not classify boundary invariant measures. A residual literature risk remains that a sufficiently general Kolmogorov-system averaging theorem may subsume part of the mean-law derivation, although no checked source states the exact source-specific predator defect and Floquet formula together.

## References
1. Y. Xue, “Analysis of a prey-predator system incorporating the additive Allee effect and intraspecific cooperation,” *AIMS Mathematics* 9(1) (2024), 1273–1290. DOI: 10.3934/math.2024063. First public date: 2023-12-07.
2. N. S. Goel, S. C. Maitra, and E. W. Montroll, “On the Volterra and Other Nonlinear Models of Interacting Populations,” *Reviews of Modern Physics* 43 (1971), 231–276. DOI: 10.1103/RevModPhys.43.231.
3. C. Zhang and W. Yang, “Dynamic behaviors of a predator–prey model with weak additive Allee effect on prey,” *Nonlinear Analysis: Real World Applications* 55 (2020), 103137. DOI: 10.1016/j.nonrwa.2020.103137.
