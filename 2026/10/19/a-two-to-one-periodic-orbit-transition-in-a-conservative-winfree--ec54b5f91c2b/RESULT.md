# A two-to-one periodic-orbit transition in a conservative Winfree triad

## Finding
For the three-oscillator conservative Winfree system
\[
\dot\theta_i=A_\varepsilon(\theta_i)\sum_{j=1}^3B_{ij}A_\varepsilon'(\theta_j),\qquad A_\varepsilon(s)=1+\varepsilon\cos s,\quad B=\begin{pmatrix}0&1&-1\\-1&0&1\\1&-1&0\end{pmatrix},
\]
with every real \(0<\varepsilon<1\), an explicit smooth circle change of variable \(t_i=k\int_0^{\theta_i}A_\varepsilon(s)^{-1}\,ds\pmod{2\pi}\), where \(k=\sqrt{1-\varepsilon^2}\), produces a conserved phase sum \(C=t_1+t_2+t_3\pmod{2\pi}\) and a Hamiltonian on each invariant two-torus. On the distinguished leaf \(C=0\), the Hamiltonian is
\[
h(p,q)=-\log(1-\varepsilon\cos p)-\log(1-\varepsilon\cos q)-\log(1-\varepsilon\cos(p+q)),
\]
and the equations are \(\dot p=k^2\partial_qh\), \(\dot q=-k^2\partial_ph\).

This leaf has **exactly six equilibria for every \(0<\varepsilon<1\)**: two strict minima with transformed phases \((\pm2\pi/3,\pm2\pi/3,\pm2\pi/3)\); three hyperbolic saddles, the permutations of \((0,\pi,\pi)\); and one strict maximum \((0,0,0)\). Their three, strictly ordered, Hamiltonian levels are
\[
E_{\min}=-3\log(1+\varepsilon/2),\quad E_{\mathrm{sep}}=-\log((1-\varepsilon)(1+\varepsilon)^2),\quad E_{\max}=-3\log(1-\varepsilon).
\]
For **every** \(E_{\min}<E<E_{\mathrm{sep}}\), the level \(h^{-1}(E)\) consists of exactly **two** disjoint periodic orbits; for **every** \(E_{\mathrm{sep}}<E<E_{\max}\), it consists of exactly **one** periodic orbit. No claim about the number of separatrix arcs at \(E=E_{\mathrm{sep}}\) is needed. The center/saddle classification and the transition do not require small \(\varepsilon\).

More generally, for any number of zero-natural-frequency oscillators with positive smooth periodic common response \(A\) and real skew-symmetric coupling matrix \(B\), the global coordinates \(u_i=\int_0^{\theta_i}ds/A(s)\) make the system a constant-Poisson Hamiltonian flow \(\dot u=B\nabla H\) with \(H=\sum_i\log A(\theta_i(u_i))\). This structural identity is used here to obtain the complete leafwise portrait, not to infer a phase-portrait classification for arbitrary \(B\).

## Assumptions and scope
All phase variables are circle-valued, and the equations use **zero natural frequencies**. The coupling matrix, positive response function, and exact parameter interval are as displayed. The leaf \(C=0\) is a two-dimensional torus, not an assertion about the entire three-torus. All periodic-orbit counts concern *connected components of regular Hamiltonian level sets*, equivalently distinct closed integral curves at the indicated fixed energy. At the three critical levels, the statement only identifies equilibria and critical values, not a generic-orbit count. The definitions are independent of representatives of the angle classes because the change of coordinate is an orientation-preserving circle diffeomorphism.

## Proof
**1. Global Poisson conjugacy.** If \(A(s)>0\), then \(u_i=\int_0^{\theta_i} A(s)^{-1}ds\) is an increasing circle coordinate of circumference \(L=\int_0^{2\pi}A(s)^{-1}ds\). With zero natural frequencies, \(\dot u_i=\sum_j B_{ij}A'(\theta_j)\). Since \(\partial_{u_j}\log A(\theta_j)=A'(\theta_j)\), the vector field equals \(B\nabla H\). Skew-symmetry gives \(\dot H=\nabla H^{\mathsf T}B\nabla H=0\). For the present response, \(L=2\pi/k\) (elementary tangent-half-angle integral), and the rescaled coordinates \(t_i=ku_i\) have standard circle period \(2\pi\). The tangent-half-angle identity gives \(A_\varepsilon(\theta_i)=k^2/(1-\varepsilon\cos t_i)\), whence
\[
\dot t=k^2B\nabla_t\mathcal H,\qquad \mathcal H(t)=-\sum_{j=1}^3\log(1-\varepsilon\cos t_j).
\]
The row and column sums of \(B\) vanish, so \(C=\sum t_i\pmod{2\pi}\) is conserved. On \(C=0\), put \(p=t_1\), \(q=t_2\), \(t_3=-p-q\). Because \(\partial_qh=\partial_{t_2}\mathcal H-\partial_{t_3}\mathcal H\), the first row of \(B\) gives \(\dot p=k^2\partial_qh\); similarly \(\dot q=-k^2\partial_ph\).

**2. Exhausting all stationary points.** Put \(g(t)=\varepsilon\sin t/(1-\varepsilon\cos t)\). Stationarity is equivalent to \(g(t_1)=g(t_2)=g(t_3)\). A fixed nonzero level \(g(t)=v\) is described, with \(z=\tan(t/2)\), by the quadratic \(v((1-\varepsilon)+(1+\varepsilon)z^2)-2\varepsilon z=0\). The zero level comprises the two phases \(t=0,\pi\). Therefore every fixed level of \(g\) contains at most two distinct angles: among three stationary phases, at least two coincide. Write them \(t_1=t_2=w\), without loss of generality, and use the constraint to obtain \(t_3=-2w\pmod{2\pi}\). The equation \(g(w)=g(-2w)\) reduces, after multiplication by positive denominators, to
\[
\sin w\,(2\cos w+1)\,(1+\varepsilon-2\varepsilon\cos w)=0.
\]
The last factor is at least \(1-\varepsilon>0\). Thus \(\sin w=0\) or \(\cos w=-1/2\). The former gives \((0,0,0)\) and permutations of \((0,\pi,\pi)\); the latter gives exactly the two indicated fully equal minima. No additional critical points exist.

**3. Nondegeneracy and levels.** For \(f(t)=-\log(1-\varepsilon\cos t)\),
\[
f''(t)=-\frac{\varepsilon(\cos t-\varepsilon)}{(1-\varepsilon\cos t)^2}.
\]
At \(t=0\) it is negative, at \(t=\pm2\pi/3\) positive, and at \(t=\pi\) positive. For equal-coordinate critical points, the Hessian of \(h(p,q)\) equals \(f''(t)\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}\), giving the asserted definite extrema. At a mixed critical point, set \(a=f''(\pi)=\varepsilon/(1+\varepsilon)\) and \(b=f''(0)=-\varepsilon/(1-\varepsilon)\). The Hessian determinant equals \(a(a+2b)=-\varepsilon^2(1+3\varepsilon)/((1-\varepsilon)(1+\varepsilon)^2)<0\), so all three mixed equilibria are hyperbolic saddles. Evaluation of \(\mathcal H\) yields the three displayed levels. Strict inequalities follow from
\[
(1+\varepsilon/2)^3-(1-\varepsilon)(1+\varepsilon)^2=\frac{\varepsilon(9\varepsilon^2+14\varepsilon+4)}8>0
\]
and \((1-\varepsilon)(1+\varepsilon)^2-(1-\varepsilon)^3=4\varepsilon(1-\varepsilon)>0\).

**4. Periodic-orbit census.** The function \(h\) is a smooth Morse function on the compact two-torus with precisely the six nondegenerate critical points and no other critical values. Just above its minimum value, its level is a small simple closed curve around each of its two minima and thus has exactly two components. Just below its maximum, the level is one small simple closed curve around its unique maximum. Between the minimum and saddle levels, and between the saddle and maximum levels, \(h\) has no critical points; compact regular-level continuation by the gradient flow preserves the number of connected level components throughout each interval. Each component is a circle on which the Hamiltonian vector field is everywhere nonzero, hence is exactly one periodic orbit. This proves the uniform two-to-one transition for all admissible \(\varepsilon\).

## Verification
Run `python3 verify_triad.py` with Python 3 (standard library only). This checks 1,000 deterministic randomly chosen phase states against two independently implemented transformed vector fields, energy conservation and phase-sum conservation; all 30 equilibrium Hessian classifications and energy inequalities for five parameter values; and exact rational polynomial/sign identities at three rational parameters. It prints `VERIFY_OK`. These finite checks are corroboration only: the complete statement is established by the analytic quadratic-level argument, exact Hessians, and compact Morse-level continuation in the proof.

## Relationship to prior work
Pikovsky, *Conservative dynamics in phase oscillator networks* (arXiv:2603.25431v1, 26 March 2026), equation (9), introduces exactly the arbitrary skew-matrix, common-response Winfree-type network and demonstrates phase-volume conservation, including numerical chaos at nonzero frequencies. The present result adds a global Poisson reduction for its positive-response, zero-frequency subclass and derives an exact, parameter-uniform periodic-orbit census on one invariant two-torus; these statements are not given by its divergence-free criterion. Burylko, Mielke, Wolfrum, and Yanchuk (2018) treat skew-coupled oscillator rings with *phase-difference* interactions \(g(\theta_i-\theta_j)\), proving Hamiltonian-like and dissipative region structure; these are different equations from the separable-product interaction \(A(\theta_i)A'(\theta_j)\) here. Their periodic orbit families do not by themselves imply the explicit critical-level and component-count formulas proved above. The general claim that any smooth Morse function with this critical-value pattern has the corresponding regular-level topology is standard; the nonstandard content is identifying and proving that exact six-point pattern in this motivated oscillator family for the full parameter range.

## Limitations
The periodic-orbit census is **only** on \(C=0\), not on arbitrary Casimir leaves or in a network with nonzero natural frequencies. The separatrix level is identified by its energy and three saddles; its individual heteroclinic connections are not enumerated. No small-perturbation persistence or global integrability statement for the nonzero-frequency model is claimed. A published equivalence under a non-obvious coordinate transformation remains a general literature risk; the cited primary model classes and inspected specific propositions do not establish the present formulas. Numerical sampling is not used as a substitute for the all-parameter proof.

## References
- A. Pikovsky, *Conservative dynamics in phase oscillator networks*, arXiv:2603.25431v1 (first public version 2026-03-26), https://arxiv.org/html/2603.25431v1, in particular Sec. III.1, Eq. (9), and Sec. III.3.
- O. Burylko, A. Mielke, M. Wolfrum, S. Yanchuk, *Coexistence of Hamiltonian-Like and Dissipative Dynamics in Rings of Coupled Phase Oscillators with Skew-Symmetric Coupling*, SIAM J. Appl. Dyn. Syst. 17 (2018), 2076–2105, doi:10.1137/17M1155685; lawful full text https://imath.kiev.ua/files/uploads/26/BMWY_SIAM_2018.pdf, especially Secs. 2, 5, 6.
