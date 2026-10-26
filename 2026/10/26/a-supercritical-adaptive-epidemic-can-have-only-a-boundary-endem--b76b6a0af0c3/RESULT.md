# A supercritical adaptive epidemic can have only a boundary endemic state

## Finding

For the multigroup adaptive susceptible–infectious–susceptible system of Achterberg, Sensi and Sottile, a reproduction number larger than one does **not**, without further hypotheses, force an endemic equilibrium with positive infection in every group. An explicit strongly connected two-group model with positive epidemiological rates and nonnegative, monotone, twice-continuously-differentiable contact responses has
\[
\mathcal R_0=\frac{9+\sqrt{65}}8>1,
\]
but only two equilibria: the disease-free equilibrium and one **locally asymptotically stable partial-endemic equilibrium**. There is no fully endemic equilibrium. The counterexample is complemented by a general positive result: when link creation remains strictly positive at every prevalence vector whose coordinates are below one, and link-equilibrium denominators stay positive, the implication \(\mathcal R_0>1\Rightarrow\) existence of a fully endemic equilibrium **does** hold for every finite irreducible infection matrix. Thus persistence of potential contact creation is a sufficient structural assumption missing from the unconditional implication.

## Assumptions and scope

Take an integer \(n\ge2\), infection prevalences \(y_i\in[0,1]\), directed link densities \(z_{ij}\in[0,1]\), and mean prevalence \(\bar y=n^{-1}\sum_i y_i\). The model is
\[
\begin{aligned}
\dot y_i&=-\delta_i y_i+(1-y_i)\sum_{j=1}^n\beta_{ij}y_jz_{ij},\\
\dot z_{ij}&=-\zeta_{ij}z_{ij}f_{\mathrm{br},ij}(y_i,y_j,\bar y)
+\xi_{ij}(1-z_{ij})f_{\mathrm{cr},ij}(y_i,y_j,\bar y).
\end{aligned}
\]
Assume \(\delta_i>0\), \(\zeta_{ij},\xi_{ij}>0\), \(B=(\beta_{ij})\ge0\) irreducible, and the nonnegative response functions are continuous on the prevalence cube. Define, for each directed edge \(\beta_{ij}>0\),
\[
Q_{ij}(y)=\zeta_{ij}f_{\mathrm{br},ij}(y_i,y_j,\bar y)+\xi_{ij}f_{\mathrm{cr},ij}(y_i,y_j,\bar y),\qquad
Z_{ij}(y)=\frac{\xi_{ij}f_{\mathrm{cr},ij}(y_i,y_j,\bar y)}{Q_{ij}(y)}.
\]
For the positive existence statement suppose \(Q_{ij}(y)>0\) on the entire closed cube for every infection-carrying edge and \(f_{\mathrm{cr},ij}(y_i,y_j,\bar y)>0\) whenever all coordinates of \(y\) are strictly below one. Set \(D=\operatorname{diag}(\delta_i)\), \(H=(\beta_{ij}Z_{ij}(0))\), and \(\mathcal R_0=\rho(D^{-1}H)\). This is equivalent to the next-generation spectral radius used in the source; the spectral radii of \(D^{-1}H\) and \(HD^{-1}\) coincide. No monotonicity of the responses is needed for the sufficient existence theorem. It is retained in the counterexample.

An **endemic equilibrium** here means \(0<y_i<1\) for every group, matching the all-group definition in the motivating work. A **partial-endemic equilibrium** has positive infection in some, but not all, groups.

## Proof

**Part I: existence if every infection-carrying link can be recreated.** On every infection-carrying edge, the stationary link equation uniquely gives \(z_{ij}=Z_{ij}(y)\). On a nonedge with \(\beta_{ij}=0\), the independent link equation admits some stationary density in \([0,1]\), even if both response rates vanish. Substitution on the infection-carrying edges gives the continuous reduced vector field
\[
G_i(y)=-\delta_i y_i+(1-y_i)\sum_j\beta_{ij}y_jZ_{ij}(y).
\]
Since \(Z_{ij}\) is continuous at the origin, \(G(y)=Ay+o(\|y\|)\) on the nonnegative cube with \(A=H-D\). Irreducibility and \(\mathcal R_0>1\) imply that the Metzler matrix \(A\) has a strictly positive spectral bound \(\lambda>0\) and a strictly positive left eigenvector \(w\), so \(w^{\mathsf T}A=\lambda w^{\mathsf T}\). Hence, uniformly for nonnegative \(y\) sufficiently near zero,
\[
w^{\mathsf T}G(y)>0\quad\text{whenever}\quad w^{\mathsf T}y=\varepsilon>0
\]
for any sufficiently small fixed \(\varepsilon\). The uniform estimate follows because \(\|y\|\le Cw^{\mathsf T}y\) in the nonnegative cone.

Consider the nonempty compact convex truncated cube
\[
K_\varepsilon=\{y\in[0,1]^n:w^{\mathsf T}y\ge\varepsilon\}.
\]
On its cut face the vector field points strictly inward. On each face \(y_i=0\), \(G_i(y)\ge0\), and on each face \(y_i=1\), \(G_i(y)=-\delta_i<0\). A continuous vector field with these inward normal inequalities has a zero in this convex polytope. To see this directly, for fixed \(h>0\) apply Brouwer's theorem to \(T(y)=\Pi_{K_\varepsilon}(y+hG(y))\), where \(\Pi\) denotes Euclidean projection. At a fixed point, \(hG(y)\) is an outward normal of \(K_\varepsilon\). It can be written as a nonnegative combination of normals to active faces. Every active outward normal \(\nu\) obeys \(\nu^{\mathsf T}G(y)\le0\), so
\(h\|G(y)\|^2\le0\). Thus \(G(y)=0\).

The zero cannot have any coordinate equal to one because \(G_i=-\delta_i\) there. If one coordinate vanishes at this zero, its stationary infection equation and positivity of \(Z_{ij}(y)\) on infection-carrying edges force all its incoming neighbors' prevalences to vanish. By irreducibility, all coordinates vanish, contradicting \(w^{\mathsf T}y\ge\varepsilon\). Therefore every coordinate lies strictly between zero and one, and the corresponding link densities yield a fully endemic equilibrium of the complete system. This proves existence but does not imply uniqueness or stability.

**Part II: exact counterexample when a contact-creation response can vanish.** Let \(n=2\), set every recovery, link-breaking and link-creation rate equal to one, and take
\[
B=\begin{pmatrix}4&1\\1&1/2\end{pmatrix}.
\]
Set every link-breaking response equal to one, every link-creation response equal to one **except**
\[
f_{\mathrm{cr},21}(y_2,y_1,\bar y)=\phi(y_1),\qquad
\phi(u)=\bigl(\max\{1-2u,0\}\bigr)^3.
\]
All responses are nonnegative and nonincreasing (creation) or nondecreasing (breaking) in each indicated prevalence argument; \(\phi\) is \(C^2\) on the entire real line. The underlying matrix \(B\) has all entries positive and is irreducible. At zero prevalence, every stationary link density equals \(1/2\), and consequently
\[
\mathcal R_0=\rho(B/2)=\frac{9+\sqrt{65}}8>1.
\]
Its smallest next-generation row sum is \(3/4<1\), so this example lies outside the stronger row-sum sufficient condition in the motivating publication.

At every equilibrium, \(z_{11}=z_{12}=z_{22}=1/2\) and
\[
z_{21}=\frac{\phi(y_1)}{1+\phi(y_1)}.
\]
The first stationary infection equation is exactly
\[
0=y_1(1-2y_1)+\frac12(1-y_1)y_2.
\]
If both prevalences were positive and \(y_1\le1/2\), the right-hand side would be strictly positive. Thus a fully endemic equilibrium would require \(y_1>1/2\). Then \(\phi(y_1)=0\), hence \(z_{21}=0\), and the second stationary infection equation reduces to
\[
0=-y_2+\frac14(1-y_2)y_2=-\frac{y_2(3+y_2)}4<0,
\]
an impossibility. There are no fully endemic equilibria. If \(y_1=0\) and \(y_2>0\), the first equation is strictly positive, also impossible. If \(y_2=0\), the first equation is \(y_1(1-2y_1)=0\). Therefore the **only** equilibria are the disease-free state and the partial-endemic state
\[
(y_1,y_2,z_{11},z_{12},z_{21},z_{22})
=\left(\frac12,0,\frac12,\frac12,0,\frac12\right).
\]
The latter is hyperbolically attracting. In the displayed coordinate order, the full Jacobian at this state is
\[
\begin{pmatrix}
-1&1/4&1&0&0&0\\
0&-3/4&0&0&1/2&0\\
0&0&-2&0&0&0\\
0&0&0&-2&0&0\\
0&0&0&0&-1&0\\
0&0&0&0&0&-2
\end{pmatrix},
\]
whose eigenvalues are \(-1,-1,-3/4,-2,-2,-2\). The two-state equilibrium classification and the attracting partial-endemic state demonstrate why disease-free instability alone does not guarantee endemic infection in every community.

## Verification

The companion `verify.py` checks, using exact rational and symbolic calculations, the next-generation eigenvalues, the two equilibrium equations, the six-dimensional boundary Jacobian and its complete spectrum. It also evaluates an explicit positive-creation parameter example with a supercritical spectral radius and a subcritical row sum. The analytic inward-pointing-field argument supplies the general existence proof; the code does not purport to enumerate arbitrary functions or networks.

## Relationship to prior work

Achterberg, Sensi and Sottile introduced the precise multigroup adaptive model and formula for \(\mathcal R_0\). Their Theorem 5 gives an endemic-existence criterion requiring the minimum next-generation row sum to exceed one, and their Conjecture 6 proposes the unrestricted implication from \(\mathcal R_0>1\). The present result settles the unrestricted formulation negatively with a smooth two-group counterexample and establishes a distinct sufficient structural condition under which that implication holds. The source permits nonnegative monotone functional responses and directed link densities that can become zero. This is not an assertion about fixed-network SIS models or static multigroup compartment systems; their threshold theorems do not control endogenous disappearance of a directed infection pathway.

## Limitations

The counterexample depends on a contact-creation rule that vanishes on a prevalence interval. Strictly positive contact creation prevents this counterexample mechanism and is sufficient for existence under the stated denominator assumptions, but it is not claimed to be individually necessary. The sufficient theorem guarantees existence, not uniqueness, permanence, or stability. The explicit boundary equilibrium is locally stable; the proof does not claim global attraction of its full basin or address stochastic finite-population extinction. Publication-priority searching is necessarily nonexhaustive.

## References

1. M. A. Achterberg, M. Sensi, S. Sottile, *A minimal model for multigroup adaptive SIS epidemics*, arXiv:2407.17639, first posted 24 July 2024; *Chaos* **35**, 033127 (2025), doi:10.1063/5.0246228. Source model Eq. (2), Theorem 5 and Conjecture 6. https://arxiv.org/abs/2407.17639 ; https://doi.org/10.1063/5.0246228
2. M. A. Achterberg and M. Sensi, *A minimal model for adaptive SIS epidemics*, arXiv:2209.01224 (2022); *Nonlinear Dynamics* **111** (2023), 12657–12670. Earlier one-community adaptive framework. https://arxiv.org/abs/2209.01224
3. J. Zhang, J. Pang and J. Wang, *Stability Analysis of a Multigroup Epidemic Model with General Exposed Distribution and Nonlinear Incidence Rates*, *Abstract and Applied Analysis* (2013), article 354287, doi:10.1155/2013/354287. Related fixed-incidence multigroup thresholds, without adaptive contact erasure. https://doi.org/10.1155/2013/354287
