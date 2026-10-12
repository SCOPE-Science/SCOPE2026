# Adult survival creates a strict stage-specific invasion gap on prey cycles
## Finding
In Seno and Goyal's discrete-time system with a shared prey and predators specializing on juvenile versus adult prey, the predator-free prey map is
\[
H_{n+1}=\sigma H_n+F(H_n)H_n,
\qquad 0\le\sigma<1.
\]
The two predators differ at low density: the juvenile-specific predator reproduces in proportion to the newborn cohort \(F(H_n)H_n\), whereas the adult-specific predator reproduces in proportion to the standing cohort \(H_n\).

For every positive nonconstant prey-only period-\(p\) orbit and strictly positive adult survival \(0<\sigma<1\), this distinction creates a **strict disadvantage for juvenile-specific invasion** when the predator coefficients are matched so that their linear replacement factors are equal at the positive prey equilibrium. With \(\beta_J=\rho_J a_J\), \(\beta_A=\rho_A a_A\), and \(\beta_A=(1-\sigma)\beta_J\), their transverse Floquet multipliers obey
\[
\frac{\Lambda_J}{\Lambda_A}
=\frac{\prod_{j=0}^{p-1}F(h_j)}{(1-\sigma)^p}<1.
\]
The inequality is an exact consequence of strict logarithmic concavity, not a numerical comparison of two simulated trajectories.

This gap produces an exact qualitative split in the Ricker-type response explicitly discussed in the article. For the parameter choice
\[
\sigma=\frac14,\qquad r_0=\frac{49}4,\qquad\nu=1,
\]
\[
F(H)=\frac{49}4e^{-4H/49},\qquad
\Pi_J(P)=\Pi_A(P)=e^{-P},
\]
\[
\rho_J=\frac4{49\log7},\qquad
\rho_A=\frac3{49\log7},
\]
the predator-free prey states
\[
h_-=\frac{49}4\log7,
\qquad h_+=\frac{49}2\log7
\]
form an attracting exact two-cycle on the prey axis. The two-step linearization has the three eigenvalues
\[
\frac{(7\log7-8)(\log7-1)}8,
\qquad\frac78,
\qquad\frac98.
\]
The first is strictly between zero and \(3/4\). Hence the two-cycle is locally attracting in the juvenile-only predator-prey model but repelling in the adult-predator direction. Both predators nevertheless have the same equilibrium replacement factor
\[
B_J=B_A=\frac{3\log(49/3)}{4\log7}>1.
\]
The example isolates a new invasion boundary in the high-growth, non-monotone Ricker regime that the article expressly leaves beyond its main persistence theorems.

## Assumptions and scope
For the general theorem, let \(F:(0,\infty)\to(0,\infty)\), \(0<\sigma<1\), \(\rho_J,\rho_A>0\), and let the encounter-escape functions satisfy
\[
\Pi_\bullet(0)=1,\qquad \Pi_\bullet'(0)=-a_\bullet<0.
\]
Assume a positive nonconstant period-\(p\) orbit exists for the predator-free map, with integer \(p\ge2\); no claim is made that every positive \(F\) has such an orbit.

The multiplier comparison is between predators having the same linear replacement factor at a positive prey equilibrium \(K\), where \(F(K)=1-\sigma\); that is,
\[
\rho_Aa_A=(1-\sigma)\rho_Ja_J.
\]
For \(\sigma=0\), the comparison becomes equality, not a strict inequality. The exact example chooses the source's exponential encounter-escape functions and Ricker-type density dependence, but leaves the monotone-offspring hypothesis assumed in the source's main theorems. The state space is the positive prey axis and nonnegative predator coordinates.

"Invasive" and "noninvasive" describe positive versus negative **local linear Floquet growth** at the predator-free periodic orbit. They do not claim global persistence, extinction from every initial condition, or final multispecies coexistence.

## Proof
The article's three-species map is
\[
\begin{aligned}
H'&=\sigma\Pi_A(A)H+\Pi_J(J)F(\Pi_A(A)H)\Pi_A(A)H,\\
J'&=\rho_J\{1-\Pi_J(J)\}F(\Pi_A(A)H)\Pi_A(A)H,\\
A'&=\rho_A\{1-\Pi_A(A)\}H.
\end{aligned}
\]
At \((H,0,0)\), the Jacobian is upper triangular, with diagonal
\[
\sigma+F(H)+HF'(H),\quad \beta_JF(H)H,\quad \beta_AH.
\]
(The off-diagonal top-row couplings do not affect the eigenvalues of the period monodromy.) Consequently the product of Jacobians around the prey orbit remains upper triangular, with transverse multipliers
\[
\Lambda_J=\beta_J^p\prod_jF(h_j)h_j,
\qquad\Lambda_A=\beta_A^p\prod_jh_j.
\]

For each \(j\), write
\[
q_j=\frac{h_{j+1}}{h_j}=\sigma+F(h_j)>\sigma,
\qquad u_j=\log q_j.
\]
Periodic telescoping gives \(\prod_jq_j=1\) and \(\sum_ju_j=0\). On the domain \(e^u>\sigma\), the function
\[
\phi(u)=\log(e^u-\sigma)
\]
has
\[
\phi''(u)=-\frac{\sigma e^u}{(e^u-\sigma)^2}<0.
\]
Jensen's inequality is therefore strict for every nonconstant orbit:
\[
\frac1p\sum_j\log F(h_j)
=\frac1p\sum_j\phi(u_j)
<\phi\left(\frac1p\sum_ju_j\right)
=\log(1-\sigma).
\]
If all \(u_j\) were equal, their mean zero would force \(q_j=1\) and \(h_{j+1}=h_j\), contrary to nonconstancy. Exponentiating gives the strict ratio formula for \(\beta_A=(1-\sigma)\beta_J\). At \(\sigma=0\), \(\phi(u)=u\) and equality holds.

For the explicit realization, abbreviate
\[
L=\log7,\qquad c=\frac{49}4.
\]
With \(\sigma=1/4\), \(F(H)=ce^{-H/c}\), and \(h_-=cL\), \(h_+=2cL\), direct substitution yields
\[
F(h_-)=\frac74,\qquad F(h_+)=\frac14,
\]
and hence
\[
f(h_-)=h_-\left(\frac14+\frac74\right)=h_+,
\]
\[
f(h_+)=h_+\left(\frac14+\frac14\right)=h_-.
\]
These are different positive points. The prey derivative is
\[
f'(H)=\frac14+F(H)\left(1-\frac Hc\right).
\]
Therefore
\[
f'(h_-)=2-\frac74L,
\qquad f'(h_+)=\frac{1-L}{2},
\]
so the two-step prey multiplier is
\[
m_H=\frac{(7L-8)(L-1)}8.
\]
The elementary bound \(3/2<L<2\) gives \(0<m_H<3/4<1\). It can be verified without floating point by bounding \(e^{3/2}<7<e^2\) using rational exponential-series sums and tails.

With \(\Pi_\bullet(P)=e^{-P}\), the slopes are \(a_J=a_A=1\), so the chosen reproduction parameters give
\[
\beta_J=\frac1{h_-},\qquad\beta_A=\frac3{4h_-}.
\]
The juvenile per-step factors are \(7/4\) and \(1/2\), and the adult factors are \(3/4\) and \(3/2\); hence
\[
\Lambda_J=\frac74\cdot\frac12=\frac78,
\qquad\Lambda_A=\frac34\cdot\frac32=\frac98.
\]
All two-step eigenvalues are thus explicit. Restricting to the two-dimensional juvenile-only system leaves \(m_H\) and \(7/8\), both inside the open unit circle, proving local asymptotic stability of the two-cycle by the discrete-time linearization theorem. The adult-only system has the real multiplier \(9/8>1\), proving instability; in the full three-species system the adult-specific transverse direction is unstable and the juvenile-specific one stable.

Finally, the positive predator-free equilibrium is
\[
K=c\log\left(\frac{c}{1-\sigma}\right)
=\frac{49}4\log(49/3).
\]
At that equilibrium the linear replacement factors are
\[
B_J=\beta_J(1-\sigma)K
=\beta_AK=B_A
=\frac{3\log(49/3)}{4\log7}.
\]
Since \(\log(49/3)=2\log7-\log3\), the inequality \(B_J>1\) is equivalent to \(3\log3<2\log7\), equivalently \(27<49\), which proves the stated supercritical equilibrium comparison.

## Verification
The bundled script `verification/verify.py` reconstructs the *actual* three-dimensional map and its two Jacobians symbolically using exact SymPy expressions. It verifies that the two proposed prey values map into one another, multiplies the Jacobians in the correct time order, and verifies all three diagonal monodromy entries against the displayed exact expressions.

The checker establishes the bound \(3/2<\log7<2\) using finite rational exponential-series bounds; this is an analytic inequality, not an inference from a finite search. It also checks the strict-concavity derivative identity and the exact source-specific matching of replacement factors. The general inequality follows from the displayed strict Jensen argument independently of the script.

## Relationship to prior work
Seno and Goyal (2026), Eq. (13), introduce the joint three-species stage-specific recurrence; Eqs. (18)–(19) give equilibrium replacement factors. Their positive-persistence theory assumes monotonicity of \(F(H)H\) below equilibrium capacity. The authors explicitly point out that the high-growth Ricker response violates that assumption and leave the extension of their results open. The present claim is **restricted to that excluded dynamical regime**; it does not invalidate their theorems.

Seno's public 2025 conference poster describes the same biological model and emphasizes juvenile-stage advantage in the equilibrium-oriented, Beverton–Holt setting, but does not present a periodic-prey Floquet criterion. May and Hassell (1981) establish multiparasitoid dynamics in a different host-stage arrangement. Jia et al. (2024) analyze a Ricker-type two-parasitoid system whose prey has no explicit adult-survival term and whose two predator offspring equations differ from the two stage-specific cohorts of the present source. Their coexistence and bifurcation theory is substantial prior work but does not imply the strict \(\sigma>0\) cycle inequality here.

More generally, multiplier products on periodic orbits and Jensen's inequality are classical tools. The source-specific contribution is the **strict stage ordering under matched equilibrium factors**, together with a positive, stable Ricker-type prey two-cycle on which the two predator types have opposite local invasion outcomes \(7/8\) and \(9/8\).

## Limitations
This is a local Floquet result, not a global persistence or basin-classification theorem. In the full three-species system the predator-free cycle is a saddle, not a stable attractor; only the juvenile-only restriction is locally attracting. The adult-only restriction is unstable to adult-predator introduction.

The exact Ricker example violates the paper's seventh (monotone-offspring) hypothesis and therefore lies outside its main convergence and persistence theorems. The upper point of the prey cycle is above the positive equilibrium \(K\); the lower point is below \(K\). This is possible precisely because the monotonicity hypothesis no longer makes the interval below \(K\) forward invariant.

The strict stage comparison requires positive adult survival and matching \(\beta_A=(1-\sigma)\beta_J\). It is not claimed under arbitrary unmatched predator reproduction parameters. The sign of the multipliers cannot alone determine eventual fate after appreciable predator perturbations.

## References
1. H. Seno and A. Goyal, “Discrete-time exploitative competition model of different stage-specific predators,” *Journal of Mathematical Biology* 93 (2026), article 11. DOI: 10.1007/s00285-026-02427-w.
2. H. Seno, “Discrete time exploitative competition model of different stage-specific predators,” poster POS-30, ACMB–JSMB2025 (2025), official public abstract; first scheduled core poster presentation July 9, 2025.
3. L. Jia, Y. Roh, G. Piao and I. H. Jung, “Dynamic Complexities in Competing Parasitoid Species on a Shared Host,” *International Journal of Bifurcation and Chaos* 34 (2024), 2450014. DOI: 10.1142/S0218127424500147.
4. R. M. May and M. P. Hassell, “The Dynamics of Multiparasitoid-Host Interactions,” *The American Naturalist* 117 (1981), 234–261. DOI: 10.1086/283704.
