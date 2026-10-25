# Two-moment tomography and a sharp variance floor for a stochastically gated Brownian absorber

## Finding
Consider a Brownian searcher in a finite reflecting interval with a two-state, independently switching absorbing gate at its other endpoint. **Exactly its absorption-time mean and variance at one fixed initial position and stationary gate preparation globally determine both positive gate-switching rates.** More precisely, with the dimensionless mean \(m\) and variance \(v\) defined below, the complete set of realizable data is
\[
 m>\tfrac12,\qquad v>m^2-\tfrac13m+\tfrac1{12}.
\]
For every pair satisfying these strict inequalities, exactly one admissible pair of switching rates exists. The variance lower boundary is sharp but unattained by finite positive switching rates; at each fixed \(m>1/2\), the attainable variance has no upper bound.

## Assumptions and scope
Fix an interval \([0,L]\) and constants \(D,L>0\). A diffusion with generator \(D\partial_{xx}\) starts at \(x=L\), which is reflecting. At \(x=0\), the boundary is absorbing in gate state O and reflecting in state C. Independently, a continuous-time Markov chain switches C to O at rate \(\alpha>0\) and O to C at rate \(\beta>0\). The initial gate is stationary, with \(\Pr(O)=\alpha/(\alpha+\beta)\), independent of the initial Brownian motion. Let \(T\) be the absorption time and set \(m=D\mathbb E[T]/L^2\), \(v=D^2\operatorname{Var}(T)/L^4\). All formulas concern the continuous-time diffusion model, with exact unconditioned moments and known \(D,L\). Define the dimensionless total gate rate \(z=(\alpha+\beta)L^2/D\), the ratio \(q=\beta/\alpha\), and \(h(z)=\coth(\sqrt z)/\sqrt z\).

## Proof
**Laplace boundary problem.** Scale distance by \(L\), time by \(L^2/D\), and both gate rates correspondingly. For \(u\ge0\), let \(\phi_O(x,u)\), \(\phi_C(x,u)\) be the conditional transforms \(\mathbb E[\exp(-uDT/L^2)]\). The backward equations are
\[
\phi_O''=(u+\beta')\phi_O-\beta'\phi_C,\quad
\phi_C''=(u+\alpha')\phi_C-\alpha'\phi_O,
\]
where \(\alpha'=\alpha L^2/D\) and \(\beta'=\beta L^2/D\). At the left boundary \(\phi_O(0,u)=1\), \(\phi_C'(0,u)=0\); at the right boundary both derivatives vanish. Write \(p=\alpha'/(\alpha'+\beta')\), \(F=p\phi_O+(1-p)\phi_C\), and \(W=\phi_C-\phi_O\). Then \(F''=uF\), \(W''=(u+z)W\), and the right reflection gives \(F=A\cosh(\sqrt u(1-x))\), \(W=B\cosh(\sqrt{u+z}(1-x))\). The left conditions \(F(0)-(1-p)W(0)=1\) and \(F'(0)+pW'(0)=0\) imply the exact stationary-gate Laplace transform
\[
\Psi(u)=F(1,u)=\frac1{\cosh\sqrt u+q\sqrt u\sinh\sqrt u\,h(z+u)}.
\]
The expression is interpreted continuously at \(u=0\); the finite-interval absorbed process has finite moments of all orders.

**Exact first two moments.** Expand \(\Psi(u)^{-1}=1+(\tfrac12+qh(z))u+(\tfrac1{24}+q(h(z)/6+h'(z)))u^2+O(u^3)\). Coefficient comparison with \(\Psi(u)=1-mu+\tfrac12\mathbb E[(DT/L^2)^2]u^2+O(u^3)\) gives
\[
m=\tfrac12+qh(z),\qquad
v=m^2-\tfrac13m+\tfrac1{12}-2(m-\tfrac12)\frac{h'(z)}{h(z)}.
\]
In particular, \(h'(z)<0\) gives the stated strict variance floor.

**Global inverse and sufficiency.** Set \(\Delta=m-\tfrac12>0\), \(R=[m^2-m/3+1/12-v]/(2\Delta)<0\). By the classical Mittag–Leffler expansion,
\[
 h(z)=\frac1z+2\sum_{n=1}^{\infty}\frac1{z+\pi^2n^2}
     =\int_0^\infty e^{-zt}\left(1+2\sum_{n=1}^\infty e^{-\pi^2n^2t}\right)\,dt.
\]
The integral is finite for \(z>0\), and its integrand has strictly positive weight for every \(t>0\). Exponential tilting consequently yields \((\log h)''(z)=\operatorname{Var}_z(t)>0\), with strictly positive variance. Thus \(h'(z)/h(z)\) is strictly increasing. Since \(h(z)\sim 1/z\) as \(z\downarrow0\), and \(h(z)\sim z^{-1/2}\) as \(z\uparrow\infty\), its logarithmic derivative tends respectively to \(-\infty\) and \(0\). It is therefore a bijection \((0,\infty)\to(-\infty,0)\). There exists a unique \(z>0\) solving
\[
\frac{h'(z)}{h(z)}=R;\quad q=\frac{\Delta}{h(z)};\quad
\alpha=\frac DL^2\frac{z}{1+q},\quad
\beta=\frac DL^2\frac{zq}{1+q}.
\]
Both rates are positive, their mean and variance match the observations, and uniqueness is forced by the one-to-one logarithmic derivative and algebraic reconstruction. At fixed \(m\), taking \(z\to\infty\) or \(z\to0^+\) along \(q=\Delta/h(z)\) approaches the variance floor or sends \(v\to\infty\), respectively. Neither endpoint is reached by finite positive rates.

## Verification
The included standalone Python program `verification/check_gated_moments.py` independently solves the four-dimensional constant-coefficient backward boundary system by matrix exponentiation and compares it with the closed Laplace transform at 15 combinations of parameters and Laplace arguments. It also recovers both gate rates from five forward-computed moment pairs and checks the strict variance inequality. These finite numerical checks corroborate but do not replace the exact analytical proof. Requires Python, NumPy, and SciPy; execute `python verification/check_gated_moments.py`.

## Relationship to prior work
Bressloff and Lawley (2015) introduced and analyzed switching absorbing/reflecting diffusion boundaries, including backward mean-first-passage problems. Bressloff (2020) developed a gated-target Laplace-transform framework, with and without resetting, giving forward access to absorption-time moments for the same class of boundaries. Kumar, Scher, Reuveni and Santhanam (2022) established rate inference from the short-time detection-time regime and more extensive distributional information. This finding does **not** claim the gate, forward transform, mean calculation or general possibility of gating-rate inference as new. Its separate statement is the complete *two-scalar-moment* positive-rate identifiability and necessary-and-sufficient moment feasible region at one fixed initial position, proved by a strict logarithmic-convexity argument. A hidden equivalent treatment of this inverse subproblem in specialized literature cannot be excluded.

## Limitations
Exact moments at known \(D,L\) and stationary initial gate are essential. Measurement noise can place estimates outside the strict feasible region; global identifiability does not establish stable, finite-sample inference, especially near the feasible boundary. These results do not cover nonstationary initial gate mixtures, drift, partially absorbing gate states, random diffusivity, finite switching-state memory or alternative geometries. The demonstrated overlap screening is not a priority certificate or independent audit.

## References
1. P. C. Bressloff and S. D. Lawley, “Escape from a potential well with a randomly switching boundary,” *J. Phys. A* **48** (2015), 225001, DOI 10.1088/1751-8113/48/22/225001 (first published 2015-05-14).
2. P. C. Bressloff and S. D. Lawley, “Escape from Subcellular Domains with Randomly Switching Boundaries,” *Multiscale Model. Simul.* **13** (2015), DOI 10.1137/15M1019258.
3. P. C. Bressloff, “Diffusive search for a stochastically-gated target with resetting,” arXiv:2009.02739 (2020-09-06).
4. A. Kumar, Y. Scher, S. Reuveni and M. S. Santhanam, “Inference from gated first-passage times,” arXiv:2210.00678 (2022-10-03), *Phys. Rev. Research* **5**, L032043 (2023).
