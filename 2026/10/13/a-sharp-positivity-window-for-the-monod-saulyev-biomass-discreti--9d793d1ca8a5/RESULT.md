# A sharp positivity window for the Monod–Saulyev biomass discretization

## Finding
For the forward-sweep Saulyev update specified in equations (3.3) and (3.6) of Vongkok, Chumsri and Pochai (2026), universal nonnegativity of numerical biomass has an exact, two-part criterion. For every nonnegative initial concentration profile and every nonnegative left Dirichlet input, the full discrete trajectory stays nonnegative if and only if
\[
 u\Delta x\le 2D,\qquad
 \Delta t\bigl(D/(\Delta x)^2-M+m\bigr)\le1.
\]
The endpoint inequalities are inclusive. In particular, this criterion is **not satisfied** by the mesh and biomass-growth parameters reported in the source article. On that mesh a finite, explicitly constructed nonnegative biomass profile becomes negative at the first step for each of the three published flow velocities, independently of the source's nitrogen and light choices.

## Assumptions and scope
Fix an integer \(J\ge3\), positive spacings \(\Delta x,\Delta t\), diffusion \(D>0\), downstream advection \(u\ge0\), production coefficient \(M>0\), loss coefficient \(m\ge0\), and a constant nonnegative Monod growth exponent \(\mu\ge0\). The latter is fixed by nonnegative nutrient and light inputs as in the source paper. Write \(t_n=n\Delta t\) for all integers \(n\ge0\), and let \(C_i^n\) be biomass on nodes \(0\le i\le J\). We impose arbitrary \(C_i^0\ge0\) at all interior/right nodes, a prescribed sequence \(C_0^n=h_n\ge0\), and the source's zero-flux right boundary in the precise discrete form of its equation (3.6).

The underlying linear advection–diffusion–reaction equation is
\[
 \partial_t C=-u\partial_x C+D\partial_{xx}C+(M e^{\mu t}-m)C.
\]
Define \(\lambda=D\Delta t/(\Delta x)^2\), \(\gamma=u\Delta t/\Delta x\), and
\[
 a=\frac{\lambda+\gamma/2}{1+\lambda},\quad
 b_n=\frac{1-\lambda+(M e^{\mu t_n}-m)\Delta t}{1+\lambda},\quad
 c=\frac{\lambda-\gamma/2}{1+\lambda}.
\]
The source's interior forward sweep and right boundary read, for each \(n\ge0\),
\[
 C_i^{n+1}=aC_{i-1}^{n+1}+b_n C_i^n+cC_{i+1}^{n}
 \quad(1\le i\le J-1),
\]
\[
 C_J^{n+1}=\frac{2\lambda}{1+\lambda}C_{J-1}^{n+1}+b_n C_J^n.
\]
Here *universal nonnegativity* means preservation of the closed coordinatewise nonnegative cone for **all** initial arrays and all nonnegative boundary sequences under this specific update. It is not a statement about one chosen plotted trajectory or about all alternative Saulyev schemes.

## Proof
Because \(u\ge0\), \(a\ge0\), and \(2\lambda/(1+\lambda)>0\). Because \(M>0\) and \(\mu\ge0\), \(b_n\ge b_0\) for every \(n\ge0\).

First assume \(u\Delta x\le2D\) and \(\Delta t(D/(\Delta x)^2-M+m)\le1\). The first inequality is equivalent to \(c\ge0\), and the second is equivalent to \(b_0\ge0\). Therefore all coefficients \(a,b_n,c,2\lambda/(1+\lambda)\) are nonnegative. For any nonnegative input at level \(n\), begin with \(h_{n+1}\ge0\), sweep successively through nodes \(i=1,\ldots,J-1\), and finally use the right-end formula. Every output is nonnegative. Induction on \(n\) proves preservation for every step.

Conversely, if \(u\Delta x>2D\), then \(c<0\). With boundary \(h_0=h_1=0\), initial values \(C_1^0=0\), \(C_2^0=1\) and all other initial values zero, the first interior update gives \(C_1^1=c<0\). Thus nonnegativity fails in one step, for every \(\Delta t>0\). If instead \(\Delta t(D/(\Delta x)^2-M+m)>1\), then \(b_0<0\). With \(h_0=h_1=0\), \(C_1^0=1\), \(C_2^0=0\), and the other initial entries zero, one obtains \(C_1^1=b_0<0\). Either violation defeats universal preservation; this proves the necessity and the inclusive sharpness of both conditions. Small positive perturbations of zero initial entries preserve either strict sign violation by continuity.

For the published parameter values \(D=0.09\), \(M=0.990\), \(m=0.400\), and \(\Delta x=\Delta t=0.01\), exact arithmetic gives
\[
 \lambda=9,\qquad b_0=-\frac{79941}{100000}=-0.79941,
 \qquad \Delta t_{\mathrm{max}}=\frac{100}{89941}<0.00112.
\]
This positive-step ceiling is more than eight times smaller than the reported step size. For each published flow velocity \(u\in\{0.05,0.35,0.65\}\), retain the source's left input \(h_1=25+e^{0.01}\), choose \(C_1^0=100\), \(C_2^0=0\), and take all other initial interior nodes nonnegative. The first updated interior node is
\[
 C_1^1=\frac{9+u/2}{10}(25+e^{0.01})-79.941
 <\frac{373}{400}\,27-79.941=-54.7635<0.
\]
The estimate uses only \(e^{0.01}<2\), and so is independent of \(\mu\), nutrient levels and illumination: at \(t_0=0\), the reaction coefficient is \(M-m\) regardless of these inputs. The selected initial array is not the constant profile used in the paper's plotted experiments.

## Verification
Run `python3 verify.py` with the standard Python library. It checks the exact rational coefficients and the stated three-velocity negative witness, compares the two sharp inequalities against coefficient signs on several boundary cases, and propagates one positive-cone example for 30 steps. The proof above is the basis for the unbounded-time assertion; finite tests alone do not establish it. The right-boundary coefficient is checked independently against the source's equation (3.6).

## Relationship to prior work
Vongkok, Chumsri and Pochai introduce the Monod-enhanced biomass equation, forward-sweep discretization (3.3), boundary formula (3.6), and the specific reported grids and coefficients; their accessible text does not supply an if-and-only-if universal positivity theorem or a negative-concentration witness at their reported mesh. Their numerical figures illustrate particular data, and their descriptive discussion of stability must not be confused with positivity for all data.

Samalerk and Pochai (2020) present a related parameterized Saulyev method for a decaying water pollutant with a different advection/diffusion split; its equations (3.4)–(3.5) do not state a sharp all-input positivity criterion for the 2026 biomass stencil. Samalerk and Pochai (2018) use a Saulyev discretization for a different water-quality transport problem and discuss high-Péclet behavior but do not state this criterion for the 2026 extended-Monod biomass model. Pourghanbar and coauthors (2020), Section 4.2, prove a sufficient monotonicity restriction for another nonlinear Saulyev-related scheme; this supports the general need for positivity restrictions but does not give this source-specific necessary-and-sufficient boundary and parameter-grid witness. Classic coefficientwise positivity tests underlie the proof, and no invention of that general principle is claimed. A positive alternative numerical method in Chen-Charpentier and Kojouharov (2013) is a different scheme. These comparisons limit the contribution to the exact classification and consequential data-level counterexample for the named 2026 formula.

## Limitations
The claim concerns the source's *printed* forward recurrence with fixed nonnegative \(\mu\) and a zero right Neumann input; it neither certifies nor invalidates the paper's particular constant-initial-value simulations. It does not address negative-flow sweeps, other boundary discretizations, adaptive steps, changing nutrient fields coupled to biomass, spectral stability, or numerical convergence. An inappropriate positivity guarantee does not automatically mean a reported plot contains a negative value. Comparison with some older high-Péclet literature is limited by partial full-text availability; general finite-difference cone-preservation theory is classical.

## References
1. A. Vongkok, A. Chumsri, N. Pochai, *Numerical Simulation of Phycoremediation for Nutrient Removal Using the Extended Monod Model with Saulyev Technique*, International Journal of Analysis and Applications **24** (2026), article 39, DOI: 10.28924/2291-8639-24-2026-39, equations (2.1), (3.3), (3.6), Table 1 and Section 4.
2. P. Samalerk, N. Pochai, *Numerical Simulation of a One-Dimensional Water-Quality Model in a Stream Using a Saulyev Technique with Quadratic Interpolated Initial-Boundary Conditions*, Abstract and Applied Analysis (2018), article 1926519, DOI: 10.1155/2018/1926519.
3. P. Samalerk, N. Pochai, *A Saulyev Explicit Scheme for an One-Dimensional Advection-Diffusion-Reaction Equation in an Opened Uniform Flow Stream*, Thai Journal of Mathematics **18** (2020), 677–683, equations (3.4)–(3.5).
4. S. Pourghanbar et al., *An Efficient Alternating Direction Explicit Method for Solving a Nonlinear Partial Differential Equation*, Mathematical Problems in Engineering (2020), article 9647416, DOI: 10.1155/2020/9647416, Section 4.2.
5. B. M. Chen-Charpentier, H. V. Kojouharov, *An unconditionally positivity preserving scheme for advection–diffusion reaction equations*, Mathematical and Computer Modelling **57** (2013), 2177–2185, DOI: 10.1016/j.mcm.2011.05.005.
