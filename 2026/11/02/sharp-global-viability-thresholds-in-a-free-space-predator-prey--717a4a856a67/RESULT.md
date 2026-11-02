# Sharp global viability thresholds in a free-space predator–prey–parasite model

## Finding

For the three-species free-space eco-evolutionary system of Nag Chowdhury, Banerjee, Perc and Ghosh [1], the physically admissible population simplex is forward invariant **if and only if** three explicit parameter inequalities hold. Writing the mortality coefficients as \(d_P=1-\alpha\), \(d_Q=\varepsilon\beta\), and \(d_R=\xi\), the exact conditions are

\[
\boxed{\alpha\le1,\qquad
1-\eta\le(\sqrt{1-\alpha}+\sqrt{\xi})^2,\qquad
\delta-\varepsilon\gamma\le(\sqrt{\varepsilon\beta}+\sqrt{\xi})^2.}
\]

Each inequality is sharp, including equality. The conditions are independent of the three nonnegative free-space benefit coefficients \(\psi_1,\psi_2,\psi_3\). Moreover, whenever \(\alpha\le1\), the **greatest outward velocity at full occupancy** occurs on at least one of the two edges having only prey and parasites or only predators and parasites; no genuinely three-species full-occupancy state is needed to witness failure.

At the principal parameter set in [1], holding all parameters except parasite mortality fixed, the exact global viability cutoff is \(\xi\ge9/10\). The paper's reference value \(\xi=21/50\) lies strictly below that cutoff. For example the fully occupied state \((p,q,r)=(9/10,0,1/10)\) has \(\dot s=-39/1000\); the strictly positive three-species boundary state \((89/100,1/100,1/10)\) has \(\dot s=-1529/50000\). These statements concern **all initial states in the closed simplex**; they do not contradict the possibility that a particular plotted trajectory stays inside it.

## Assumptions and scope

Let \(p,q,r\) be the nonnegative densities of prey, predators and parasites, and define free space by \(s=1-p-q-r\). The dynamics are the source's original equations (6)–(7), equivalently

\[
\begin{aligned}
\dot p &=p[-q+r+\psi_1s-(1-\alpha)],\\
\dot q &=q[\varepsilon p-\varepsilon\gamma r+\psi_2s-\varepsilon\beta],\\
\dot r &=r[-\eta p+\delta q+\psi_3s-\xi],\\
\dot s &=-\dot p-\dot q-\dot r.
\end{aligned}
\]

Assume \(\alpha,\beta,\gamma,\delta,\eta,\xi>0\), \(0<\varepsilon\le1\), and \(\psi_1,\psi_2,\psi_3\ge0\). No symmetry, equilibrium, or small-parameter assumption is imposed. The closed physical simplex is

\[
\Delta=\{(p,q,r)\in\mathbb R_{\ge0}^3:p+q+r\le1\}.
\]

Forward invariance means that **every** solution starting in \(\Delta\) exists for all \(t\ge0\) and remains in \(\Delta\). When \(\alpha>1\), the first displayed criterion is deemed false and no square root of \(1-\alpha\) is evaluated.

## Proof

**1. Nonnegative faces and the empty-space boundary.** Each of \(\dot p,\dot q,\dot r\) is its corresponding density times a polynomial, so the three coordinate faces are tangent, and a locally existing nonnegative solution cannot cross any coordinate hyperplane. On \(s=0\), summing the three species equations gives

\[
\dot s=F(p,q,r)=d_Pp+d_Qq+d_Rr+(1-\varepsilon)pq-(1-\eta)pr-(\delta-\varepsilon\gamma)qr,
\qquad p+q+r=1.
\]

The benefit terms vanish identically on this boundary. A polynomial vector field leaves the compact convex polytope \(\Delta\) forward invariant exactly when it is tangent or inward on every defining face (the usual tangent-cone criterion, or its elementary local-exit proof). Thus invariance is equivalent to \(F\ge0\) on the full-occupancy triangle, with the three nonnegative faces already settled. Under this condition, the bounded vector field on the forward-invariant compact simplex also gives global existence. If \(F<0\) at a boundary point, the local solution there satisfies \(s(t)<0\) for all sufficiently small positive \(t\), disproving invariance.

**2. Necessity of nonnegative prey mortality.** At \((p,q,r)=(1,0,0)\) one has \(\dot s=1-\alpha\). Hence \(\alpha\le1\) is necessary. From now on assume this inequality, so \(d_P,d_Q,d_R\ge0\).

**3. Reduction from a triangle to two edges.** Fix \(r\in[0,1]\), substitute \(q=1-r-p\), and vary \(p\in[0,1-r]\). The expression \(F(p,1-r-p,r)\) has second derivative

\[
\frac{\partial^2 F}{\partial p^2}= -2(1-\varepsilon)\le0.
\]

Consequently its minimum on each segment of constant parasite density occurs at \(p=0\) or \(q=0\). It follows that

\[
\min_{p,q,r\ge0,\,p+q+r=1}F(p,q,r)
=\min_{i\in\{P,Q\}}\min_{0\le u\le1}
\big[d_i u+d_R(1-u)-e_i u(1-u)\big],
\]

where \(e_P=1-\eta\), \(e_Q=\delta-\varepsilon\gamma\), and \(u\) is the occupied fraction of the relevant non-parasite species. This is the announced exact edge-extremizer statement, not just a sufficient estimate.

**4. Exact two-species boundary criterion.** Fix \(d_i,d_R\ge0\), and write \(e=e_i\). For \(0<u<1\), dividing the edge expression by \(u(1-u)>0\) gives

\[
\frac{d_i u+d_R(1-u)-e u(1-u)}{u(1-u)}
=\frac{d_i}{1-u}+\frac{d_R}{u}-e.
\]

The infimum on the right before subtracting \(e\) is \((\sqrt{d_i}+\sqrt{d_R})^2\) by Cauchy–Schwarz (or AM–GM), including zero-coefficient endpoint limits. The edge endpoints have nonnegative flux. Therefore flux is nonnegative on an entire edge if and only if

\[
e_i\le(\sqrt{d_i}+\sqrt{d_R})^2.\]

Apply this equivalence to \(i=P,Q\) and combine with Step 3. This proves all three necessary and sufficient inequalities, with equality included. If an edge inequality fails, a strictly interior point of that edge has strictly negative flux; by continuity, there are also nearby three-species-positive full-occupancy points with negative flux. For a constructive exact-rational witness when the coefficients are rational and \(e_i>(\sqrt{d_i}+\sqrt{d_R})^2\), the minimizing fraction is

\[
u_i^\star=\frac{e_i+d_R-d_i}{2e_i}\in(0,1),\]

and the other non-parasite density is zero. This fraction is strictly interior because the strict inequality forces \(e_i>\max(d_i,d_R)\).

**5. Sharp threshold at the motivating parameters.** The reference values in [1] are

\[
\alpha=1,\quad\beta=\tfrac45,\quad\varepsilon=\tfrac1{10},\quad
\gamma=1,\quad\delta=\tfrac{139}{100},\quad\eta=\tfrac1{10},
\]

with arbitrary nonnegative \(\psi_i\). The prey–parasite inequality becomes \(9/10\le\xi\). The predator–parasite inequality becomes

\[
\tfrac{129}{100}\le\left(\sqrt{\tfrac2{25}}+\sqrt\xi\right)^2,
\]

which already holds at \(\xi=9/10\) and then at every larger \(\xi\). Thus \(\xi=9/10\) is the **exact** global viability threshold. At the reference \(\xi=21/50\), direct substitution yields

\[
F(\tfrac9{10},0,\tfrac1{10})=-\tfrac{39}{1000},\qquad
F(\tfrac{89}{100},\tfrac1{100},\tfrac1{10})=-\tfrac{1529}{50000}.
\]

Every step is independent of the free-space benefit coefficients because they carry the factor \(s\).

## Verification

The standalone `verify.py` uses exact rational arithmetic to compute the flux \(F\) from the printed differential equations and to compare the square-root criteria without floating point. It checks 5,000 parameter tuples and 330,000 rational full-occupancy grid points. It also compares the exact boundary minimum with the criterion in every tuple, checks both outward-flux witnesses, and checks the exact reference cutoff \(\xi=9/10\) against \(\xi=899/1000\). Running `python3 verify.py` prints `EXACT_CHECK_OK` when these checks succeed. These finite checks corroborate the algebra but do **not** prove the theorem over real parameters: Steps 1–5 above provide that proof.

## Relationship to prior work

Nag Chowdhury, Banerjee, Perc and Ghosh [1] derive this ecological system, establish coordinate-wise nonnegativity, and numerically investigate biologically bounded trajectories and bifurcations for selected initial conditions. The present theorem determines a different, stronger invariant-region property: **all** biologically admissible initial compositions remain feasible for all time. The key extra steps are the full-occupancy boundary flux, its concavity in the prey/predator split, and two sharp pairwise square-root thresholds. The result does not claim a new form of the tangent-cone criterion or of the elementary two-variable minimization used in the proof.

The balance/carrying-simplex literature [2,3] studies attracting invariant surfaces of Lotka–Volterra flows, which need not be the fixed, physically normalized triangle \(p+q+r\le1\) analyzed here. Those general constructions do not provide these conditions for the source's ten-parameter mortality-and-free-space equations. A later strategic-species model [4], with symmetric pairwise win–loss coefficients \(a,b,c\), has interaction terms that cancel in the total-density derivative at full occupancy; it is not a generalization covering the present model's asymmetric conversion coefficients \(\varepsilon,\eta,\gamma,\delta\). Its stability and sensitivity analyses do not imply these necessary and sufficient viability inequalities.

## Limitations

The theorem is solely about **forward invariance for every initial configuration**, not persistence, permanence, stability, global convergence, basin structure, existence or absence of periodic orbits, or whether any **particular** initial trajectory stays physically feasible when the inequalities fail. The boundary test is specific to the source's independent death-rate equations and its restriction \(0<\varepsilon\le1\); allowing \(\varepsilon>1\) invalidates the concave edge reduction. The exact tests do not establish priority relative to all possible earlier specialized work. Independent external validation has not been performed.

## References

[1] S. Nag Chowdhury, J. Banerjee, M. Perc and D. Ghosh, “Eco-evolutionary cyclic dominance among predators, prey, and parasites,” *Journal of Theoretical Biology* **564** (2023), 111446, DOI: 10.1016/j.jtbi.2023.111446, first available online 2023-03-02. Full text: https://www.matjazperc.com/publications/JTheorBiol_564_111446.pdf ; preprint: https://arxiv.org/abs/2303.08158 (first posted 2023-03-14).

[2] S. Baigent and A. Ching, “Balance simplices of 3-species May–Leonard systems,” *Journal of Biological Dynamics* **14** (2020), 187–199, DOI: 10.1080/17513758.2020.1736656.

[3] E. C. Zeeman and M. L. Zeeman, “An n-dimensional competitive Lotka–Volterra system is generically determined by the edges of its carrying simplex,” *Nonlinearity* **15** (2002), 2019–2032, DOI: 10.1088/0951-7715/15/6/312.

[4] S. Roy, S. Ghosh, A. Saha, P. C. Mali, M. Perc and D. Ghosh, “The eco-evolutionary dynamics of strategic species,” *Proceedings of the Royal Society A* **480** (2024), 20240127, DOI: 10.1098/rspa.2024.0127, full text: https://www.matjazperc.com/publications/ProcRSocA_480_20240127.pdf .
