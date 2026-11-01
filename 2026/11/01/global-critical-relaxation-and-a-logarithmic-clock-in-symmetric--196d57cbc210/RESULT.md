# Global critical relaxation and a logarithmic clock in symmetric Ricker competition

## Finding
For every fixed \(0<\gamma<1\), consider the positive planar map
\[
T_\gamma(x,y)=\bigl(xe^{2-x-\gamma y},\;ye^{2-y-\gamma x}\bigr).
\]
Every orbit starting at \((x_0,y_0)\in(0,\infty)^2\) converges to \(P_\gamma=(2/(1+\gamma),2/(1+\gamma))\). Introduce normalized mean and imbalance coordinates
\[
q_n=\frac{1+\gamma}{2}(x_n+y_n)-2,
\qquad w_n=\frac{1+\gamma}{2}(x_n-y_n).
\]
There exists a local \(C^3\) invariant *strong-stable curve* through \((q,w)=(0,0)\), and its global forward basin of preimages \(\mathcal E_\gamma\) has planar Lebesgue measure zero. Every positive initial condition in \(\mathcal E_\gamma\) converges exponentially to \(P_\gamma\). For every positive initial condition outside \(\mathcal E_\gamma\), the following full sharp expansion holds with a finite real orbit-dependent constant \(C\):
\[
\boxed{\quad q_{2n}^{-2}=\frac23 n+\frac25\log n+C+o(1)\quad(n\to\infty).}\tag{1}
\]
In particular, for a sign \(\sigma\in\{-1,1\}\) depending on the initial condition,
\[
\lim_{m\to\infty}(-1)^m\sqrt m\,q_m=\sigma\sqrt3,
\qquad |w_m|=O_\gamma(\rho^m),\quad |(x_m-y_m)|=O_\gamma(\rho^m)
\]
for some \(|(3\gamma-1)/(1+\gamma)|<\rho<1\), where implicit constants may also depend on the orbit. The local strong-stable curve is the graph \(q=\psi_\gamma(w)\) with the explicit nonzero curvature
\[
\boxed{\quad\psi_\gamma(w)
=-\frac{\gamma(1-\gamma)}{1-2\gamma+5\gamma^2}\,w^2+O_\gamma(w^4).\quad}\tag{2}
\]
Consequently the logarithmic coefficient \(2/5\) and the leading amplitude \(\sqrt3\) are independent of the competition coefficient, although the exceptional curve is not.

## Assumptions and scope
The state space is the open positive quadrant; the parameter is any fixed real \(\gamma\in(0,1)\). Iteration is in the original discrete clock, beginning at \(m=0\). The relation (1) holds for all sufficiently large positive integers \(n\) on each nonexceptional orbit; those late \(q_{2n}\) are nonzero. The set \(\mathcal E_\gamma\) is defined precisely in Step 4 below, without claiming that it is globally a single embedded curve. The theorem does not concern parameter endpoints \(\gamma=0\) or \(\gamma=1\), or initial conditions on the coordinate axes.

## Proof
**1. Global convergence.** The global convergence theorem of Baigent, Hou, Elaydi, Balreira and Luís [1, Theorem 3.4] applies to the Ricker competition map with \(r=s=2\) and positive cross-couplings. It establishes convergence of every nonnegative orbit to a fixed point. In the present case the fixed points in the closed quadrant are the origin, \((2,0)\), \((0,2)\), and \(P_\gamma\). Along a strictly positive orbit the origin is not a possible limit: in a sufficiently small neighborhood both coordinates grow by a factor bounded above \(1\). The axial point \((2,0)\) is not a possible limit because along a putative convergent positive orbit \(y_{m+1}/y_m\to e^{2(1-\gamma)}>1\), and analogously for \((0,2)\). Thus every positive orbit converges to \(P_\gamma\). Notice that [1] establishes the convergence, not the rates derived below.

**2. Exact transverse/slow decomposition.** Set \(\kappa=(1-\gamma)/(1+\gamma)\) and \(\eta=1-2\kappa=(3\gamma-1)/(1+\gamma)\), so \(|\eta|<1\). Direct substitution gives the exact coordinate map
\[
\begin{aligned}
q'&=e^{-q}\bigl[(2+q)\cosh(\kappa w)-w\sinh(\kappa w)\bigr]-2,\\
w'&=e^{-q}\bigl[w\cosh(\kappa w)-(2+q)\sinh(\kappa w)\bigr].
\end{aligned}\tag{3}
\]
The diagonal \(w=0\) is invariant; its map is \(f(q)=(2+q)e^{-q}-2\). Near the origin, uniformly for fixed \(\gamma\),
\[
q'=f(q)+(\kappa^2-\kappa)w^2+O(qw^2+w^4),\qquad
w'=\eta w+O(qw+w^3).\tag{4}
\]
Given any \(\rho\in(|\eta|,1)\), a small neighborhood has \(|w'|\le\rho|w|\). The analytic scalar expansion below implies \(|f^2(q)|\le|q|\) on a sufficiently small interval. Its two-step perturbation by the exponentially summable \(O(w_m^2)\) terms shows that a sufficiently small bidisk remains inside a slightly larger small bidisk under forward iteration. Since every positive orbit tends to the origin in \((q,w)\)-coordinates, all sufficiently late tails lie in such a neighborhood, and \(w_m=O(\rho^m)\).

**3. A quantitative asymptotic-phase construction.** Here is an explicit local construction that also handles the noninvertible case \(\eta=0\). On a sufficiently small interval, \(f\) is a decreasing local diffeomorphism; write \(h=f^{-1}\), with Lipschitz constant \(L>1\) arbitrarily close to \(1\). Shrink the neighborhood and choose \(\rho\in(|\eta|,1)\) so that \(L\rho^2<1\). For an actual local orbit write \(q_{m+1}=f(q_m)+d_m\), where \(|d_m|\le K|w_0|^2\rho^{2m}\). Seek a sequence \(e_m=O(\rho^{2m})\) satisfying
\[
e_m=h\bigl(f(q_m)+d_m+e_{m+1}\bigr)-q_m.\tag{5}
\]
On the Banach space of sequences with norm \(\sup_m\rho^{-2m}|e_m|\), the right-hand side of (5) has contraction ratio at most \(L\rho^2<1\) and maps an appropriate small weighted ball to itself. It therefore has a unique solution; define \(z_m=q_m+e_m\). Equation (5) implies \(z_{m+1}=f(z_m)\) and
\[
|q_m-f^m(z_0)|\le K_0\rho^{2m}|w_0|^2.\tag{6}
\]
Contraction with differentiated sequence equations (shrinking the domain so that the corresponding finite-order derivative bounds also contract) gives a \(C^3\) local phase map \(\pi_\gamma(q,w)=z_0\). It obeys \(\pi_\gamma(q,0)=q\), \(\pi_\gamma(T_\gamma(q,w))=f(\pi_\gamma(q,w))\), and \(\pi_\gamma(q,w)=q+O(w^2)\). Thus \(\partial_q\pi_\gamma(0,0)=1\) and its zero set is a unique \(C^3\) local graph \(q=\psi_\gamma(w)\). Invariance and exchange symmetry of the two species make this graph invariant and even in \(w\). On that graph, (6) forces \(q_m=O(\rho^{2m})\), while \(w_m=O(\rho^m)\).

**4. Exact exceptional set and its smallness.** Let \(U\) denote the local neighborhood in Steps 2–3 and \(W^{ss}_{\mathrm{loc}}=\{(q,w)\in U:\pi_\gamma(q,w)=0\}\). In original positive coordinates define \(\mathcal E_\gamma\) as all initial points with an iterate lying on \(W^{ss}_{\mathrm{loc}}\), remaining in the local neighborhood thereafter. Every positive orbit enters and remains in \(U\), so this definition is independent of the particular sufficiently small choice of \(U\). The first coordinate of \(T_\gamma\) is real analytic and its Jacobian determinant is not identically zero (indeed it is nonzero at \(P_\gamma\) unless \(\eta=0\), and at other positive points even when \(\eta=0\)). Hence its critical set has planar measure zero. Outside that set, \(T_\gamma\) is a local diffeomorphism; the inverse image of any planar null set is itself null, up to the critical set. Iterating this observation proves that the countable preimage union \(\mathcal E_\gamma\) has planar measure zero. Equations (5)–(6) show both that its orbits converge exponentially and that no orbit with nonzero phase can do so, using Step 5's algebraic asymptotics.

**5. Exact scalar critical clock.** Taylor expansion of the exact scalar map, not a truncated model, gives
\[
f^2(z)=z-\frac13z^3+\frac1{30}z^5+\frac1{72}z^6+O(z^7).\tag{7}
\]
For every sufficiently small \(z\ne0\), \(f^2\) preserves the sign of \(z\) and strictly decreases its absolute value; hence its even iterates tend to zero and are never eventually zero. Put \(Z_n=f^{2n}(z)\), \(U_n=Z_n^{-2}\). Elementary substitution in (7) yields
\[
U_{n+1}-U_n=\frac23+\frac4{15}U_n^{-1}+O(U_n^{-3/2}).\tag{8}
\]
First (8) implies \(U_n/n\to2/3\); then \(U_n=(2/3)n+O(\log n)\). Consequently
\[
\bigl(U_{n+1}-U_n\bigr)-\frac23-\frac25\log(1+1/n)
=O\!\left(\frac{\log n}{n^2}+n^{-3/2}\right),
\]
which is absolutely summable. Therefore \(U_n-(2/3)n-(2/5)\log n\) converges to a finite constant. Moreover \((-1)^m\sqrt m f^m(z)\to \operatorname{sgn}(z)\sqrt3\). Every nonexceptional planar orbit shadows one such nonzero scalar orbit with exponentially small mean-coordinate error (6), which leaves the constant-level inverse-square expansion unchanged: its reciprocal-square discrepancy is exponentially small times a polynomial in \(m\). This proves (1) and the signed amplitude law.

**6. Curvature of the exceptional curve.** Species-exchange symmetry and smoothness give \(\psi_\gamma(w)=a_\gamma w^2+O(w^4)\). Substitute this graph into (4), use \(f(q)=-q+O(q^2)\), and impose graph invariance: \(a_\gamma\eta^2=-a_\gamma+\kappa^2-\kappa\). Consequently
\[
a_\gamma=\frac{\kappa^2-\kappa}{1+\eta^2}
=-\frac{\gamma(1-\gamma)}{1-2\gamma+5\gamma^2},
\]
which is strictly negative for \(0<\gamma<1\). This proves (2).

## Verification
The standalone `VERIFY.py` reproduces the exact rational Taylor coefficients in (7) and (8) using symbolic algebra, checks the exact coordinate conjugacy numerically against the original map for four interior competition coefficients, checks the exceptional graph's quadratic invariance identity, and compares the asymptotic clock at two large finite iterate indices. All packaged tests passed. Numerical finite-iterate agreement is not a proof of the global statement, asymptotic existence of the constant, or smooth phase map: those are proved in Steps 1–6.

## Relationship to prior work
Baigent et al. [1] proved convergence to a fixed point throughout the larger \(r,s\le2\) Ricker domain. Their Theorem 3.4 is explicitly used in Step 1; their dynamical classification for \(r,s<2\) does not assert the endpoint's precise two-term decay or the exceptional strong-stable set. The numerical bifurcation study of Kulakov, Neverova and Frisman [2] investigates multistable cycles, not this critical relaxation asymptotic. Balreira, Elaydi and Luís [3] study local-to-global stability under additional geometric hypotheses. Their abstract and accessible metadata do not state the logarithmic clock, but the full article could not be inspected during this comparison. Jiang and Rogers [4] studied symmetric planar competition, with an unavailable complete manuscript; its precise priority relationship remains uncertain. Related published critical-relaxation calculations for different nonlinear systems do not imply (1)–(2) for this planar Ricker map.

## Limitations
The result is for one natural symmetric critical subfamily rather than all planar Ricker parameters. No uniform rate is claimed as \(\gamma\uparrow1\), where transverse contraction degenerates. The exceptional set is specified as a countable preimage union; no global topological classification of its connected components is claimed. The value of the orbit-dependent constant \(C\) is not given in elementary closed form. Bibliographic searches and inspected full text do not establish mathematical priority beyond all unindexed or inaccessible prior literature; independent mathematical audit has not been performed.

## References
[1] S. Baigent, Z. Hou, S. Elaydi, E. C. Balreira and R. Luís, *A global picture for the planar Ricker map: convergence to fixed points and identification of the stable/unstable manifolds*, Journal of Difference Equations and Applications 29 (2023), 575–591, doi:10.1080/10236198.2023.2222855. First publicly verified online 2023-06-26; complete open-access text inspected via the London Metropolitan University repository.

[2] M. Kulakov, G. Neverova and E. Frisman, *The Ricker Competition Model of Two Species: Dynamic Modes and Phase Multistability*, Mathematics 10 (2022), 1076, doi:10.3390/math10071076, open-access indexed full article, relevant dynamics and mode-classification passages read.

[3] E. C. Balreira, S. Elaydi and R. Luís, *Local stability implies global stability for the planar Ricker competition model*, Discrete and Continuous Dynamical Systems B 19 (2014), 323–351, doi:10.3934/dcdsb.2014.19.323, abstract and bibliographic metadata inspected; full text unavailable in this check.

[4] H. Jiang and T. D. Rogers, *The discrete dynamics of symmetric competition in the plane*, Journal of Mathematical Biology 25 (1987), 573–596, doi:10.1007/BF00275495, abstract and bibliographic information inspected; full text unavailable in this check.
