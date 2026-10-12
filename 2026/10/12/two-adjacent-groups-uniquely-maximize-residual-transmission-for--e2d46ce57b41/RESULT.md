# Two adjacent groups uniquely maximize residual transmission for small vaccine budgets on the five-cycle

## Finding
Consider the undirected five-cycle mixing model in which the next-generation matrix \(K\) is the adjacency matrix of \(C_5\) and the fraction of group \(i\) remaining unvaccinated is \(\eta_i\). Write
\[
R_e(\eta)=\rho(K\operatorname{Diag}(\eta)),\qquad
C(\eta)=\frac15\sum_{i=0}^4(1-\eta_i).
\]
For every sufficiently small positive dose budget \(\varepsilon=5C(\eta)\), the **only** strategies maximizing \(R_e\) among all admissible strategies of that cost are the five cyclic rotations of
\[
\eta^{\mathrm{adj}}(\varepsilon)
=(1-\varepsilon/2,\,1-\varepsilon/2,\,1,\,1,\,1).
\]
Thus the worst allocation for transmission suppresses two **adjacent** groups equally, not one group exclusively. The maximal reproduction number obeys
\[
\max_{\substack{0\le\eta_i\le1\\C(\eta)=\varepsilon/5}}R_e(\eta)
=2-\frac25\varepsilon+\frac1{25}\varepsilon^2+O(\varepsilon^3)
\quad(\varepsilon\downarrow0).
\]
For comparison, concentrating the whole dose in a single group gives \(2-2\varepsilon/5+O(\varepsilon^3)\). In particular, the optimal adjacent split has a strictly larger reproduction number for every sufficiently small positive budget.

## Assumptions and scope
There are exactly five equal-sized groups indexed modulo \(5\). A group can transmit to its two cyclic neighbors at unit next-generation intensity, but not directly to itself or other groups:
\[
K_{ij}=\begin{cases}1,&i-j\equiv\pm1\pmod5,\\0,&\text{otherwise.}\end{cases}
\]
Vaccination is perfectly protective, with independently selectable remaining-susceptible fractions \(0\le\eta_i\le1\). All comparisons fix the **exact** cost \(C(\eta)=\varepsilon/5\). The existence assertion is that some \(\varepsilon_0>0\) exists such that the classification holds for **every** \(0<\varepsilon<\varepsilon_0\); no numerical value for \(\varepsilon_0\) is claimed. For these budgets all groups retain positive fractions because \(\varepsilon<1\). The finding concerns anti-Pareto (maximal residual transmission) allocation, not the transmission-minimizing Pareto policy, and does not model nonlinear epidemic trajectories.

## Proof
**Step 1: uniform analytic expansion.** Write \(\eta_i=1-\varepsilon u_i\), where \(u_i\ge0\) and \(\sum_i u_i=1\); denote this compact simplex by \(\Delta\). Put \(F(\varepsilon,u)=\rho(K(I-\varepsilon\operatorname{Diag}u))\). At \(\varepsilon=0\), the symmetric matrix \(K\) has a simple Perron eigenvalue \(2\), with right vector \({\bf1}\) and normalized left vector \({\bf1}^{\mathsf T}/5\). Its other eigenvalues are \(2\cos(2\pi/5)\) (twice) and \(2\cos(4\pi/5)\) (twice), so the eigenvalue \(2\) is isolated and the Perron branch is real analytic uniformly over \(u\in\Delta\) for small \(\varepsilon\). Define
\[
J=\frac15{\bf1}{\bf1}^{\mathsf T},\qquad
R=(2I-K+J)^{-1}-J.
\]
Then \(R\) is the reduced resolvent of \(K\) at eigenvalue \(2\): \((2I-K)R=I-J\) and \(R{\bf1}=0\). With \(B=-K\operatorname{Diag}u\), elementary simple-eigenvalue perturbation gives
\[
F(\varepsilon,u)=2-\frac25\varepsilon+\varepsilon^2Q(u)+O(\varepsilon^3),
\qquad Q(u)=\frac15{\bf1}^{\mathsf T}BRB{\bf1}=\frac25u^{\mathsf T}RKu.
\]
The remainder and its derivatives in \(u\), up to any fixed finite order, are uniformly bounded on the compact simplex. The first-order coefficient is independent of the allocation because the total budget is fixed.

**Step 2: the exact quadratic and its global maximizers.** Exact matrix inversion yields
\[
\frac25RK=\frac1{25}
\begin{pmatrix}
0&2&-2&-2&2\\
2&0&2&-2&-2\\
-2&2&0&2&-2\\
-2&-2&2&0&2\\
2&-2&-2&2&0
\end{pmatrix}.
\]
Introduce the edge and nonedge pair sums (indices modulo \(5\))
\[
E(u)=\sum_{i=0}^{4}u_iu_{i+1},\qquad
N(u)=\sum_{i=0}^{4}u_iu_{i+2}.
\]
Every unordered pair is represented once in exactly one of these sums, and
\[
Q(u)=\frac4{25}\bigl(E(u)-N(u)\bigr).
\]
The elementary inequality \(E(u)\le1/4\) holds for every \(u\in\Delta\). To prove it, if two nonadjacent coordinates are both positive, fix their sum and all other coordinates. Since no edge joins the two, \(E\) is affine in how their combined mass is split; moving all mass to one of them can only increase \(E\) and reduces the number of positive coordinates. Repeat until the support is a clique. Every clique of \(C_5\) has at most two vertices. For adjacent masses \(a,b\ge0\) with \(a+b\le1\), \(E=ab\le(a+b)^2/4\le1/4\). This proves the bound without assuming that every maximizing support is a clique.

Since \(N(u)\ge0\), it follows that \(Q(u)\le1/25\). Equality forces \(N(u)=0\), so no nonadjacent vertices can both have positive mass; the support is a clique. It also forces \(E(u)=1/4\). These equalities hold **only** for
\[
v^{(j)}=\tfrac12(e_j+e_{j+1}),\qquad j=0,1,2,3,4,
\]
where \(e_j\) is a coordinate unit vector. Thus the quadratic has exactly five isolated global maximizers.

**Step 3: exact persistence of the optimizer, not merely asymptotic optimality.** For \(\varepsilon\ne0\) define the rescaled objective
\[
G(\varepsilon,u)=\frac{F(\varepsilon,u)-2+(2/5)\varepsilon}{\varepsilon^2},
\]
and extend it continuously at \(\varepsilon=0\) by \(G(0,u)=Q(u)\). The preceding analytic expansion shows that this extension is \(C^2\) in \(u\), uniformly near \(\varepsilon=0\), and \(G(\varepsilon,\cdot)\to Q\) in \(C^2(\Delta)\). Since \(\Delta\) is compact and the five maximizers of \(Q\) are isolated, every global maximizer of \(G(\varepsilon,\cdot)\) must lie in an arbitrarily small neighborhood of one of the five \(v^{(j)}\), for sufficiently small \(\varepsilon>0\).

Fix \(v^{(0)}=(1/2,1/2,0,0,0)\). The gradient of the exact quadratic at this point is
\[
\nabla Q(v^{(0)})=\frac1{25}(2,2,0,-4,0).
\]
Consequently, in a sufficiently small neighborhood of \(v^{(0)}\), and for all sufficiently small \(\varepsilon\),
\[
\partial_{u_0}G(\varepsilon,u)>
\partial_{u_k}G(\varepsilon,u)\quad(k=2,3,4).
\]
If any outside coordinate \(u_k\) were positive at a maximizing allocation in this neighborhood, transferring a small positive quantity from \(u_k\) to \(u_0\) would preserve the simplex and increase the objective. Hence every such maximizer lies on the face \(u=(a,1-a,0,0,0)\) with \(a\) close to \(1/2\). On that face,
\[
Q(a,1-a,0,0,0)=\frac4{25}a(1-a),\qquad
\frac{d^2}{da^2}Q=-\frac8{25}<0.
\]
By uniform \(C^2\) convergence, the restriction of \(G(\varepsilon,\cdot)\) remains strictly concave near \(a=1/2\). The reflection automorphism of the undirected cycle exchanging vertices \(0\) and \(1\) makes this restriction invariant under \(a\mapsto1-a\). Its unique local maximum is therefore exactly \(a=1/2\). Cyclic symmetry applies the same argument to all five neighborhoods. This establishes **all** global maximizers exactly, for every sufficiently small positive \(\varepsilon\), not merely their limiting shapes.

**Step 4: objective expansion and one-group comparison.** Inserting the unique optimizer into the perturbation expansion gives \(Q(v^{(j)})=1/25\). For the one-group strategy \(u=e_0\), the quadratic coefficient vanishes. The asserted asymptotic comparison follows. In addition, direct characteristic-polynomial factorization for the adjacent split gives
\[
\det(zI-K\operatorname{Diag}(\eta^{\mathrm{adj}}))
=\frac14\left(2z^2+2z-2-\varepsilon(z-1)\right)
\left(2z^3-2z^2-6z+4+\varepsilon(z^2+z-2)\right),
\]
whose Perron root is the real root near \(2\) and independently yields the same Taylor expansion.

## Verification
The standalone program `verify_cycle.py` uses exact rational symbolic arithmetic. It reconstructs \(K\), \(R\), the quadratic coefficient matrix, the edge/nonedge identity, the five-cycle optimizer gradient and edge-face restriction, and the exact characteristic polynomials for adjacent splitting and single-vertex vaccination. It checks the second-order Perron-root coefficients from those polynomials, printing `VERIFY_OK` when all assertions pass. Execute with Python 3 and SymPy as stated in `requirements.txt`. The support-reduction inequality, compactness argument, and uniform \(C^2\) perturbation reasoning are mathematical proofs above, not inferred from numerical trials or the finite checker.

## Relationship to prior work
Delmas, Dronnier and Zitt [1] study exactly this symmetric-circle next-generation matrix and anti-Pareto vaccination problem. In their Section 2.4 they identify the general \(N\ge5\) optimization as difficult, prove the separate **minimum** cost needed to make transmission vanish, and report a **numerical** anti-Pareto heuristic for \(N=12\) in which available vaccination is initially concentrated in one group. Those statements do not entail an exact answer for the worst allocation at \(N=5\). This finding supplies that answer near zero cost and shows why the numerical one-group-first heuristic cannot be universally extrapolated to the smallest unresolved odd cycle.

Delmas, Dronnier and Zitt [2] prove that a disconnecting vaccination allocation cannot maximize residual transmission, but the allocations considered here leave every group partially or fully susceptible, so do not disconnect the cycle. Their result gives no five-cycle small-budget optimizer. Their general convexity/concavity analysis [3] also does not determine it: the undirected five-cycle adjacency matrix has two positive non-Perron eigenvalues and two negative eigenvalues, so neither the all-nonnegative nor the one-positive-eigenvalue sufficient hypothesis applies. Poghotanyan et al. [4] treat the **minimization** of the reproduction number under an inverse-\(M\)-matrix assumption not satisfied by this mixed-sign spectrum. These comparisons are about logical implication and model hypotheses, not about matching words in titles.

## Limitations
The small-budget range is existential, not a computable sharp bound on \(\varepsilon_0\), and no assertion is made for medium or large budgets. The theorem assumes five **equal-size** groups, undirected **nearest-neighbor** contacts, a fixed unit interaction normalization, perfectly protective vaccination and the exact cost functional defined above. It describes a spectral threshold, not time-dependent epidemic outcomes or clinical effectiveness. The general graph-support inequality is elementary; novelty is attributed to its combination with the specific spectral quadratic and a rigorous optimizer-persistence argument for the stated epidemiological model. Literature comparisons cannot exclude all unindexed or otherwise inaccessible equivalent results.

## References
1. J.-F. Delmas, D. Dronnier, P.-A. Zitt, *Optimal vaccination: various (counter) intuitive examples*, arXiv:2112.08756 (initial public version 2021-12-16); *Journal of Mathematical Biology* **86**, 26 (2023), DOI: 10.1007/s00285-022-01858-5, Section 2.4.
2. J.-F. Delmas, D. Dronnier, P.-A. Zitt, *Optimal vaccinations: Cordons sanitaires, reducible population and optimal rays*, arXiv:2209.07381 (2022), Example 1.1 and Proposition 5.3.
3. J.-F. Delmas, D. Dronnier, P.-A. Zitt, *The effective reproduction number: Convexity, concavity and invariance*, DOI: 10.4171/JEMS/1431, Theorem 1.1 (online 2024).
4. G. Poghotanyan, Z. Feng, J. W. Glasser, A. N. Hill, *Constrained minimization problems for the reproduction number in meta-population models*, *Journal of Mathematical Biology* **77** (2018), 1795–1831, DOI: 10.1007/s00285-018-1216-z, Theorem 4.7.
