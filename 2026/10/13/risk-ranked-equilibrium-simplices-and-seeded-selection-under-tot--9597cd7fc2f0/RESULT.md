# Risk-ranked equilibrium simplices and seeded selection under total infected lockdown

## Finding

For the mass-action two-strain patch SIS system with **no movement of infected individuals**, every equilibrium and every trajectory's eventual risk stratum can be classified exactly. The model is the total infected-lockdown limit explicitly identified as an open extension in Doumatè, Issa, and Salako.

Let \(k\ge2\) patches form a connected, weighted, undirected graph. Write \(L\) for its symmetric Laplacian with nonnegative off-diagonal weights and zero row sums, \(d>0\) for the susceptible dispersal rate, and \(N>0\) for the conserved total population. For each strain-patch cell \(v=(\ell,j)\), \(\ell\in\{1,2\}\), define
\[
\beta_v=\beta_{\ell j}>0,\qquad
\gamma_v=\gamma_{\ell j}>0,\qquad
r_v=\frac{\gamma_v}{\beta_v}>0.
\]
The equations are
\[
\dot S_j=d\sum_{i=1}^k L_{ji}S_i-\sum_{\ell=1}^2\beta_{\ell j}(S_j-r_{\ell j})I_{\ell j},
\qquad
\dot I_{\ell j}=\beta_{\ell j}(S_j-r_{\ell j})I_{\ell j},
\]
subject to
\[
S_j,I_{\ell j}\ge0,\qquad
\sum_{j=1}^k(S_j+I_{1j}+I_{2j})=N.
\]
Put \(c=N/k\), let \(\mathcal R\) be the finite set of distinct risks \(r_v\), and set \(m(r)=\#\{v:r_v=r\}\).

**Exact equilibrium stratification.** The only disease-free equilibrium is
\[
E_0=(c\mathbf 1,0,0).
\]
For every \(r\in\mathcal R\) with \(r<c\), there is exactly the following endemic component:
\[
\boxed{\mathcal E_r=\left\{S_j=r\ \forall j,\quad I_v=0\ \text{if }r_v\ne r,\quad I_v\ge0\ \text{if }r_v=r,\quad\sum_{r_v=r}I_v=N-kr\right\}.}
\]
This is a simplex of dimension \(m(r)-1\). There are no other equilibria. Full positive coexistence of both strains on every patch occurs only if all \(2k\) ratios coincide; coexistence at any subset of patches requires a risk level shared by cells from both strains. With pairwise distinct ratios, every endemic component is an isolated vertex, and no two-strain endemic equilibrium exists.

**Global selection by the initially present risk.** Write
\[
C_0=\{v:I_v(0)>0\},\qquad r_*=\min_{v\in C_0}r_v.
\]
If \(C_0\) is empty, the disease-free state is approached. Otherwise:

- If \(r_*\ge c\), then the solution converges to \(E_0\).
- If \(r_*<c\), then its distance to the face of \(\mathcal E_{r_*}\) supported on the initially infected cells tends to zero. Precisely,
\[
S_j(t)\to r_*\quad\text{for every }j,\qquad
I_v(t)\to0\quad\text{when }r_v>r_*,\qquad
\sum_{v\in C_0:\,r_v=r_*}I_v(t)\to N-kr_*.
\]
If exactly one initially seeded cell attains \(r_*\), the entire trajectory converges to the unique vertex carrying infected mass \(N-kr_*\) in that cell.

Cells with zero initial infection stay empty for all time. Consequently, lockdown produces a **seed-contingent** winner: a better-risk cell that was never infected cannot displace an inferior but initially seeded cell. This is a global all-\(d>0\) conclusion, not a perturbation as infected dispersal approaches zero.

**Full local spectral classification.** At any \(X^*\in\mathcal E_r\), put
\[
D_j=\sum_{\ell=1}^2\beta_{\ell j}I^*_{\ell j},\qquad
M=dL-\operatorname{diag}(D_1,\ldots,D_k).
\]
The symmetric matrix \(M\) is strictly negative definite. In the mass-conserving tangent hyperplane the characteristic spectrum consists of the \(k\) negative eigenvalues of \(M\), the \(2k-m(r)\) real nonzero exponents
\[
\beta_v(r-r_v),\qquad r_v\ne r,
\]
and \(m(r)-1\) semisimple zeros tangent to the risk-tied equilibrium simplex. The unstable dimension is exactly
\[
\#\{v:r_v<r\}.
\]
Hence every non-minimum-risk endemic component is unstable in the full mass simplex, whereas a global minimum-risk component has no unstable transverse mode. With a unique global risk minimizer, its endemic equilibrium is a hyperbolic sink provided \(r_{\min}<c\).

The disease-free state is globally asymptotically stable on the entire mass simplex **if and only if**
\[
c\le r_{\min}=\min_v r_v.
\]
At the equality boundary it is nonhyperbolic but still globally asymptotically stable; above the boundary it has a positive infection eigenvalue.

## Assumptions and scope

There are exactly two mutually exclusive SIS strains, \(k\ge2\) patches, positive mass-action transmission and recovery coefficients, symmetric irreducible nonnegative migration weights, and positive susceptible mobility \(d>0\). Both infected mobility rates are **exactly zero**. Total population \(N\) is fixed and positive.

The global selection theorem concerns the nonnegative compact population simplex. Its convergence-to-face conclusion does not assert that, when several minimum-risk cells were seeded, their individual shares necessarily have a unique limit. If there is a unique seeded minimum-risk cell, convergence to one explicit equilibrium point is proved.

The local spectrum is calculated on the \((3k-1)\)-dimensional tangent hyperplane to conserved total mass. Zero eigenvalues are neutral equilibrium-composition directions, not indicators of exponential growth.

## Proof

**1. Positivity and conservation.** Each infected coordinate has the exact representation
\[
I_v(t)=I_v(0)\exp\left(\int_0^t\beta_v(S_{j(v)}(s)-r_v)\,ds\right).
\]
Thus its initially positive/zero status is preserved for finite time. At a susceptible boundary coordinate \(S_j=0\), the migration inflow and recovery terms are nonnegative, so the nonnegative cone is invariant. Since the graph Laplacian has zero column sums and the infection terms cancel, total mass is conserved. The nonnegative mass simplex is therefore compact and positively invariant, giving global solutions.

**2. Exact equilibria.** At equilibrium, for every \(v\),
\[
I_v(S_{j(v)}-r_v)=0.
\]
Each infection and recovery term in the susceptible equations separately vanishes, leaving
\[
dLS=0.
\]
Connectivity makes the kernel of \(L\) consist of constant vectors, so \(S_j=s\) for all patches. If every infected component is zero, mass conservation gives \(s=c\). Otherwise a positive infected component forces \(s=r_v\) for its cell; every other positive cell has the same risk and the total infected mass is \(N-ks>0\). Conversely every point of the displayed \(\mathcal E_s\) satisfies all equations. Hence the above list is exhaustive.

**3. Dissipation and convergence to the equilibrium set.** Define
\[
\mathcal V(S,I)=\frac12\sum_j S_j^2+\sum_v r_v I_v.
\]
Differentiating and using symmetry of \(L\) gives the identity
\[
\dot{\mathcal V}=-\frac d2\sum_{i,j}L_{ij}(S_i-S_j)^2
-\sum_v\beta_v I_v(S_{j(v)}-r_v)^2\le0.
\]
If \(\dot{\mathcal V}=0\), connectivity forces \(S=s\mathbf1\), and each positive infected coordinate forces \(r_v=s\). These are exactly the equilibria from Step 2. LaSalle's invariance principle on the compact mass simplex therefore places every omega-limit set inside the equilibrium set.

On \(\mathcal E_r\), the Lyapunov value is independent of infection composition and equals
\[
F(r)=Nr-\frac{k}{2}r^2,
\]
whereas \(\mathcal V(E_0)=N^2/(2k)=F(c)\). The function \(F\) is strictly increasing for \(0<r<c\). Because \(\mathcal V(t)\) has a limit, an omega-limit set can meet only one of these finitely many components. Distance to that component therefore tends to zero.

**4. Selection of the seeded minimum.** The initially seeded support \(C_0\) is invariant. Hence the only possible endemic omega-limit component has level \(r\ge r_*\). Suppose it instead approached an endemic component with \(r>r_*\), or approached \(E_0\) with \(c>r_*\). In either case each susceptible coordinate tends to a limit \(s_\infty>r_*\). For any initially positive cell \(v_*\) with \(r_{v_*}=r_*\), the exact infected equation eventually gives
\[
\dot I_{v_*}\ge\frac12\beta_{v_*}(s_\infty-r_*)I_{v_*}>0.
\]
It would make \(I_{v_*}\) unbounded, contradicting total mass \(N\). Thus for \(r_*<c\) only \(\mathcal E_{r_*}\) is possible. If \(r_*\ge c\), there is no accessible endemic component because every endemic risk must be below \(c\); the limit is \(E_0\). If \(C_0\) is empty, all infections remain zero and connected susceptible diffusion tends to \(c\mathbf 1\). The precise componentwise limits and unique-minimum vertex statement follow directly.

**5. Endemic spectral decomposition.** Fix \(X^*\in\mathcal E_r\). The susceptible derivative with respect to susceptible variables is
\[
M=dL-\operatorname{diag}(D_j),\qquad D_j=\sum_\ell\beta_{\ell j}I^*_{\ell j}.
\]
At least one \(D_j>0\). For every nonzero vector \(y\),
\[
y^TMy=-\frac d2\sum_{i,j}L_{ij}(y_i-y_j)^2-\sum_jD_jy_j^2<0;
\]
indeed equality would force a constant \(y\) and then \(y=0\). Thus all \(k\) eigenvalues of \(M\) are negative.

Order linearized coordinates as: infection cells with \(r_v\ne r\), susceptible cells, then cells with \(r_v=r\). The linearization is block lower triangular. Every off-risk cell contributes the scalar diagonal block \(\beta_v(r-r_v)\). The susceptible block is \(M\). The risk-tied infection block is zero, because \(S^*_{j(v)}=r_v\). Since \(M\) is invertible and the off-risk exponents are nonzero, the full zero eigenvalue is semisimple with multiplicity \(m(r)\); its eigenvectors have zero susceptible and off-risk components. One zero direction changes total mass and is removed on the conserved-mass hyperplane, leaving exactly \(m(r)-1\) tangent zeros. Every other eigenvalue is listed above. Positive off-risk exponents correspond exactly to risks below \(r\), giving the claimed unstable dimension.

**6. Closed disease-free threshold.** At \(E_0\) the infection exponents are \(\beta_v(c-r_v)\); the susceptible Laplacian contributes \(k-1\) strictly negative exponents on the mass hyperplane. Thus \(E_0\) is unstable if \(c>r_{\min}\). If \(c\le r_{\min}\), the global selection theorem gives attraction from every initial state. Moreover
\[
\mathcal V-\mathcal V(E_0)=\frac12\sum_j(S_j-c)^2+\sum_v(r_v-c)I_v\ge0,
\]
with equality only at \(E_0\) on the mass simplex; together with \(\dot{\mathcal V}\le0\), this proves Lyapunov stability even at equality. Hence \(E_0\) is globally asymptotically stable exactly at and below the stated threshold.

## Verification

The bundled standalone Python checker uses only the standard library and exact rational arithmetic. It reconstructs the six-dimensional Jacobian in two patches and checks characteristic polynomials for a unique minimum-risk vertex, a higher-risk unstable vertex, a tie-simplex interior point, and a tie-simplex vertex. It also evaluates the exact mass-conservation and Lyapunov identities at a rational test state. It prints `VERIFY_OK` only if every check succeeds.

The finite calculation is corroborative: the proof for arbitrary \(k\) is the graph energy inequality, the exact dissipation identity, omega-limit selection, and the block-triangular Jacobian argument. Numerical integration is not used as proof.

## Relationship to prior work

Doumatè, Issa, and Salako study the two-strain patch model with **positive** susceptible and infected dispersal rates. Their discussion explicitly sets aside the total-lockdown case for infected movements as a question for future work. The exact risk-indexed equilibrium components and local invasion spectrum here cover that degenerate boundary rather than relabeling a positive-dispersal theorem.

Salako and Wu study a **single-strain continuum** SIS reaction-diffusion model with infected mobility exactly zero. Their Lyapunov method already yields analogous susceptible homogenization, risk concentration, and dependence on the initially infected support. These general qualitative ideas are acknowledged as prior; the two-strain finite-patch equilibrium simplex stratification, strain coexistence tie condition, complete all-initial-state selection, and full linear invasion spectrum do not follow as statements about their single-strain PDE.

Salako and Wu's separate one-strain patch paper analyzes mass-action transmission and asymptotic endemic profiles as a **positive** infected dispersal rate tends to zero. Such a singular limit is not the same as a classification of every equilibrium and every trajectory at the **exact** zero-dispersal boundary. Earlier multistrain diffusive theory likewise generally treats positive infected mobility or different incidence rules.

Source-identifier, zero-infected-dispersal, two-strain, risk-ratio, simplex, and patch-equilibrium searches found no publication stating this precise classification. A later single-strain patch-equilibrium article concerns endemic curves as susceptible mobility varies rather than an exact two-strain infected-lockdown spectral classification. Absence of a located publication is not itself proof of novelty.

## Limitations

Global convergence is proved to the selected equilibrium **face** when more than one minimum-risk cell was initially seeded. No individual limiting infection share is asserted in that tied case. Stability spectra are local, and the result does not analyze the small-positive-infected-mobility perturbation or transient time scales as lockdown is lifted.

The theorem requires a symmetric, connected susceptible migration graph, mass-action transmission, positive rates, two mutually exclusive strains, and **both** infected dispersal rates exactly zero. Asymmetric dispersal and models with mutation, superinfection, demographic turnover, or standard-incidence normalization are outside its scope.

The selected risk depends on which cells were infected initially: the full-state minimum is not guaranteed to be selected if it was never seeded. Related one-strain continuum results already establish risk selection; source-specific novelty rests on the exact two-strain patch theorem, its equilibrium strata, and its invasion spectrum. An equivalent formulation could exist under terminology not indexed in the searches.

## References

1. J. T. Doumatè, T. B. Issa, R. B. Salako, “Competition-exclusion and coexistence in a two-strain SIS epidemic model in patchy environments,” *Discrete and Continuous Dynamical Systems - B* 29 (2024), 3058–3096. DOI: 10.3934/dcdsb.2023213. arXiv:2308.10348 (first public 20 August 2023).
2. R. B. Salako, Y. Wu, “On degenerate reaction-diffusion epidemic models with mass action or standard incidence mechanism,” *European Journal of Applied Mathematics* 35 (2024), 634–661. DOI: 10.1017/S0956792523000359. See Section 3.2 and Theorem 3.11.
3. R. B. Salako, Y. Wu, “On the dynamics of an epidemic patch model with mass-action transmission mechanism and asymmetric dispersal patterns,” *Studies in Applied Mathematics* 152 (2024), 1208–1250. arXiv:2311.06437; DOI: 10.1111/sapm.12674.
