# The contact-creation boundary for spectral endemicity in adaptive multigroup SIS networks

## Finding

For the multigroup adaptive SIS equations (2) of Achterberg, Sensi and Sottile [1], a supercritical disease-free reproduction number need **not** imply any equilibrium with positive infection in every community, even for two groups and strictly positive infection and adaptation-rate matrices. An explicit continuously differentiable, monotone two-group system has \(\mathcal R_0=(17+\sqrt{241})/8>1\) but its only nonzero equilibrium is \((y_1,y_2)=(3/4,0)\). Conversely, for **any** number of groups and an irreducible underlying infection graph, if every existing directed contact has *strictly positive contact creation at every prevalence*, then \(\mathcal R_0>1\) guarantees a fully positive endemic equilibrium. Moreover, restoring arbitrarily small positive contact creation on the severed link in the example produces endemic equilibria with precise first-order prevalence \(y_2=\eta+O(\eta^2)\). This identifies permanent adaptive edge loss—not a spectral defect—as a sharp logical obstruction to the proposed reproduction-number criterion.

## Assumptions and scope

Fix an integer \(n\geq2\). The state consists of prevalence \(y_i\in[0,1]\) and directed contact fractions \(z_{ij}\in[0,1]\). We use the source's precise orientation: \(z_{ij}\) multiplies transmission **from** group \(j\) **to** group \(i\). Write \(\bar y=n^{-1}\sum_i y_i\). The system is

\[
\dot y_i=-\delta_i y_i+(1-y_i)\sum_{j=1}^n\beta_{ij}z_{ij}y_j,
\quad
\dot z_{ij}=-\zeta_{ij}z_{ij}b_{ij}(y_i,y_j,\bar y)
+\xi_{ij}(1-z_{ij})c_{ij}(y_i,y_j,\bar y).
\]

Here \(\delta_i>0\), \(\beta_{ij}\geq0\), and the directed graph of \(B=(\beta_{ij})\) is strongly connected. The functions \(b_{ij},c_{ij}\) are nonnegative and continuous. In the counterexample they are continuously differentiable, \(b_{ij}\) nondecreasing and \(c_{ij}\) nonincreasing in each argument. In the sufficient-condition theorem, assume on every edge \(\beta_{ij}>0\) that \(\xi_{ij}>0\), \(\zeta_{ij}\geq0\), and \(c_{ij}\) is **strictly positive on the whole closed prevalence cube** (in particular at the disease-free state). On nonedges no conditions on their unused link equations are needed. Positivity of creation can be weakened to positivity of the stationary contact fraction everywhere; it is stated in a directly checkable form.

Under those conditions define \(Z_{ij}(y)=\xi_{ij}c_{ij}(y)/(\zeta_{ij}b_{ij}(y)+\xi_{ij}c_{ij}(y))\) on edges, with \(y\) supplying the three arguments indicated above. Set \(K_{ij}=\beta_{ij}Z_{ij}(0)/\delta_i\) and \(\mathcal R_0=\rho(K)\); this is the threshold computed from the disease-free infection linearization and has the same eigenvalues relevant to the source's next-generation convention. A **fully endemic** equilibrium means \(0<y_i<1\) for every \(i\), not merely positive total prevalence. A nonzero equilibrium with some \(y_i=0\) is *partially endemic*.

## Proof

**1. Explicit counterexample.** Take \(n=2\), all recovery, contact-breaking, and contact-creation rate constants \(\delta_i=\zeta_{ij}=\xi_{ij}=1\), and

\[
B=\begin{pmatrix}4&1/2\\1&1/4\end{pmatrix}.
\]

For \((i,j)\ne(2,1)\) put \(b_{ij}\equiv0\), \(c_{ij}\equiv1\). On the directed transmission link \(1\to2\), put \(b_{21}\equiv1\) and

\[
c_{21}(y_2,y_1,\bar y)=q(y_1),\qquad
q(s)=\bigl(\max\{0,1-2s\}\bigr)^2.
\]

The function \(q\) is \(C^1\) on \([0,1]\), nonnegative, and nonincreasing; the other adaptation functions are constant and therefore satisfy all the monotonicity assumptions. All entries of \(B\) and all rates are strictly positive. The link fractions at disease freedom are \(Z_{11}(0)=Z_{12}(0)=Z_{22}(0)=1\) and \(Z_{21}(0)=1/2\). Therefore

\[
K=\begin{pmatrix}4&1/2\\1/2&1/4\end{pmatrix},\qquad
\mathcal R_0=\frac{17+\sqrt{241}}8>1.
\]

At every stationary point \(z_{11}=z_{12}=z_{22}=1\) and \(z_{21}=q(y_1)/(1+q(y_1))\). The prevalence equations read

\[
y_1=(1-y_1)(4y_1+y_2/2),\qquad
y_2=(1-y_2)\bigl(z_{21}y_1+y_2/4\bigr).
\]

If \(y_1=0\), the first equation gives \(y_2=0\). If \(y_1>0\), then
\[
y_1\geq4(1-y_1)y_1,\quad\text{so}\quad y_1\geq 3/4>1/2.
\]

Consequently \(q(y_1)=0\), hence \(z_{21}=0\). The second stationary equation reduces to \(y_2=(1-y_2)y_2/4\); since \((1-y_2)/4<1\), this forces \(y_2=0\). Substitution into the first equation yields \(y_1=3/4\). Thus the only stationary prevalence vectors are \((0,0)\) and \((3/4,0)\); there is no fully endemic equilibrium. The latter is a genuine partially endemic equilibrium with \(Z=\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)\).

**2. Sufficient condition for arbitrary \(n\).** Suppose instead that every existing contact has strictly positive continuous creation on the full prevalence cube. Eliminate links at equilibrium using their unique stationary values \(Z_{ij}(y)\in(0,1]\). Define for \(y\in[0,1]^n\)

\[
G_i(y)=\sum_j\beta_{ij}Z_{ij}(y)y_j,
\qquad T_i(y)=\frac{G_i(y)}{\delta_i+G_i(y)}.
\]

The map \(T:[0,1]^n\to[0,1)^n\) is continuous; \(T(0)=0\). By continuity of the stationary link fractions, \(T(y)=Ky+o(\|y\|)\) as \(y\to0\) in the nonnegative cone. The irreducible nonnegative matrix \(K\) has a strictly positive **left** Perron vector \(\ell\), normalized arbitrarily, with \(\ell^\top K=\rho(K)\ell^\top\). If \(\rho(K)>1\), choose \(0<\gamma<\rho(K)-1\). Positivity of \(\ell\) and the uniform little-o estimate imply that some \(r>0\) satisfies

\[
0<\|y\|\leq r,\ y\geq0\quad\Longrightarrow\quad
\ell^\top T(y)\geq(1+\gamma)\ell^\top y.
\tag{*}
\]

For \(0<\eta<1\), let \(T_\eta(y)=(1-\eta)T(y)+\eta\mathbf1/2\). Brouwer's theorem supplies a fixed point \(y^\eta\in(0,1)^n\). Consider any \(\eta_k\downarrow0\). Compactness provides a convergent subsequence whose limit \(y^*\) is a fixed point of \(T\). Such a subsequential limit **cannot be zero**: if \(y^{\eta_k}\to0\), then for sufficiently large \(k\), estimate (*) and the positive perturbation give

\[
\ell^\top y^{\eta_k}
= (1-\eta_k)\ell^\top T(y^{\eta_k})
 +\frac{\eta_k}{2}\ell^\top\mathbf1
> (1-\eta_k)(1+\gamma)\ell^\top y^{\eta_k}
>\ell^\top y^{\eta_k},
\]

a contradiction. Hence \(y^*\ne0\). If some coordinate \(y_i^*=0\), then its fixed-point identity forces \(G_i(y^*)=0\). Every in-neighbor \(j\) with \(\beta_{ij}>0\) must then have \(y_j^*=0\), because \(Z_{ij}(y^*)>0\). Backward propagation along the strongly connected directed graph would force all coordinates to vanish, impossible. Thus \(y_i^*>0\) for every \(i\); also \(y_i^*<1\) by the formula for \(T_i\). Setting \(z_{ij}^*=Z_{ij}(y^*)\) on edges yields a fully endemic equilibrium of the original coupled ODE. This completes the threshold-existence theorem without any additional row-sum or monotonicity hypothesis.

**3. Infinitesimal restoration demonstrates the boundary.** In the two-group counterexample, replace only \(c_{21}\) by \(q(y_1)+\eta\), where \(\eta>0\). Near the former partially endemic equilibrium, \(q(y_1)=0\) identically and the stationary link is \(z_{21}=w=\eta/(1+\eta)\). Put

\[
F_1=-y_1+(1-y_1)(4y_1+y_2/2),\quad
F_2=-y_2+(1-y_2)(wy_1+y_2/4).
\]

At \((y_1,y_2,w)=(3/4,0,0)\),

\[
D_{(y_1,y_2)}F=\begin{pmatrix}-3&1/8\\0&-3/4\end{pmatrix},
\qquad
\partial_wF=\begin{pmatrix}0\\3/4\end{pmatrix}.
\]

The Jacobian is nonsingular. The implicit-function theorem gives a unique local smooth equilibrium branch, with derivative \((dy_1/dw,dy_2/dw)=(1/24,1)\). Since \(w=\eta+O(\eta^2)\), as \(\eta\downarrow0\),

\[
y_1=3/4+\eta/24+O(\eta^2),\qquad
y_2=\eta+O(\eta^2)>0.
\]

Thus arbitrarily small strictly positive creation restores **existence**, not necessarily uniqueness or stability, and the limiting low-prevalence community vanishes linearly.

## Verification

Run the adjacent standard-library-only script `check_adaptive_sis.py` with Python 3. It checks the exact rational disease-free contact matrix, the characteristic polynomial of \(K\), stationary residuals, and the algebraic inequalities excluding a fully endemic counterexample. It also independently solves the restored equilibrium equations by bisection over five positive creation parameters, confirming the asymptotic derivatives. The arbitrary-group assertion and impossibility conclusion are proved analytically above; finite calculations alone would not establish either universal assertion.

## Relationship to prior work

Achterberg, Sensi and Sottile [1, Sec. III.E, Theorem 5 and Conjecture 6] establish a minimum-row-sum sufficient condition and explicitly conjecture fully positive endemicity for every \(\mathcal R_0>1\). In the counterexample the minimum row and column sums of the disease-free threshold matrix both equal \(3/4<1\), so [1, Theorem 5] does not apply. Their model permits nonnegative rather than strictly positive creation responses and explicitly allows adaptive contact weights to reach zero [1, Sec. II]. The example refutes this unrestricted conjecture as formulated, rather than merely sharpening its numerical bound. Their assertion that nonzero equilibrium infection must spread across a strongly connected underlying network fails if an **adaptive** stationary contact vanishes; that implication becomes valid under the restored positivity assumption, which also allows the Perron–Brouwer existence proof.

The preceding one-community adaptive SIS analysis [2] cannot express directed intercommunity disconnection. The state-dependent network SIS theorem of Wang et al. [3] concerns a different discrete-time prevalence feedback without separately evolving adaptive contact densities and does not imply the mixed endemic counterexample or the present sufficient-condition theorem. Standard autonomous SIS Perron thresholds apply to contact structures that remain positive; they do not cover the zero-contact boundary exhibited here.

## Limitations

The positive-creation assumption is **sufficient**, not claimed necessary for all particular systems. The counterexample relies on a contact-creation law reaching zero at high infection levels; it does not disprove conjectural variants imposing everywhere-positive creation. This analysis addresses existence of equilibria only, not their number away from the example, linear stability, global attraction, or persistence of every infection from every positive initial state. The restoration asymptotics are local in \(\eta\); numerical checks are illustrative, not infinite proofs. Published and indexed work was compared, but a differently phrased equivalent result in unindexed literature cannot be excluded. No independent validation has been performed.

## References

[1] M. A. Achterberg, M. Sensi and S. Sottile, *A minimal model for multigroup adaptive SIS epidemics*, arXiv:2407.17639 (initial public version 24 July 2024); *Chaos* **35**, 033127 (2025), doi:10.1063/5.0246228. Full published text: https://pure.tudelft.nl/ws/portalfiles/portal/241262677/033127_1_5.0246228.pdf .

[2] M. A. Achterberg and M. Sensi, earlier adaptive SIS one-community model, arXiv:2209.01224.

[3] Y. Wang, S. Gracy, H. Ishii and K. H. Johansson, *Suppressing the endemic equilibrium in SIS epidemics: A state dependent approach*, arXiv:2106.00122 (2021).
