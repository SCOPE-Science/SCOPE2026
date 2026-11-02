# Topology-sensitive spectral correction for emptying a dense symmetric-exclusion branch

## Finding
Let \(G=(V,E)\) be a fixed finite connected undirected graph with \(N=|V|\ge 2\), symmetric positive edge-exchange rates, and one distinguished reservoir vertex \(o\). Write \(q\in(0,1)\) for the vacancy probability and \(p=1-q\) for the particle probability. A particle is injected at an empty root at rate \(p\), removed from an occupied root at rate \(q\), and an occupied-vacant pair exchanges across edge \(xy\) at rate \(c_{xy}=c_{yx}>0\).

Let \(B_q\) be the first return to the entirely empty configuration, starting immediately after injection of one particle at the root into an empty branch. Denote by \(K_q\) the generator restricted to all nonempty occupation configurations, with transitions into the empty configuration killed, and by \(\lambda_q>0\) its smallest positive decay rate (so \(-\lambda_q\) is its spectral bound). Then:

\[
\boxed{\mathbb E[B_q]=\frac{q^{-N}-1}{1-q}}\qquad (0<q<1),
\]

\[
\boxed{q^NB_q\ \xrightarrow[q\downarrow0]{\mathrm{law}}\ \operatorname{Exp}(1),\qquad \lim_{q\downarrow0}\mathbb E[(q^NB_q)^s]=\Gamma(1+s)\quad(s>0).}
\]

Define the single-particle symmetric random-walk generator \((L_Gf)(x)=\sum_{y:xy\in E}c_{xy}(f(y)-f(x))\) and the diagonal matrix \(D_o=\operatorname{diag}(\mathbf1_{x\ne o})\). The positive constant

\[
T_G=\langle\delta_o,(D_o-L_G)^{-1}\delta_o\rangle
\]

is the expected total time spent at the root by a single walk started at the root and killed at rate one whenever outside the root. The first correction to the principal decay rate is

\[
\boxed{\lambda_q=(1-q)q^N\bigl[1-qT_G+O_G(q^2)\bigr].}
\]

For unit-rate edges and root at a path endpoint, \(T_{P_N}=F_{2N-1}/F_{2N-2}\), with \(F_0=0\), \(F_1=1\), and \(F_{m+2}=F_{m+1}+F_m\). For a unit-rate star with reservoir at the center, \(T_{S_N}=2/(N-1)\). Both families have the same exact busy-period mean for each fixed \(N\) and \(q\), but different first spectral corrections when \(N\ge3\). At \(N=3\) this distinguishes the reservoir position on the same unrooted path, whereas at \(N\ge4\) it distinguishes nonisomorphic branch geometries.

## Assumptions and scope
Time is continuous. Each edge exchange is an independent exponential-rate event acting only when its endpoints differ. The root injection and removal rates add to one. The finite graph, root, and edge rates remain fixed as \(q\downarrow0\). There is only one particle reservoir. The excursion starts from the specific one-particle root configuration \(a\), never from the stationary nonempty ensemble. An empty branch waits for a rate-\(p\) injection; that holding time is *not* included in \(B_q\).

A path is the single-file side-branch setting: because particles cannot pass one another, the particle entering an initially empty branch is its last particle to leave; its residence duration is precisely \(B_q\). On graphs with junctions or loops, \(B_q\) describes emptying the full branch, not the residence of any particular labeled particle.

## Proof
**1. Exact excursion mean.** The stationary law is the independent Bernoulli product law

\[\pi_q(\eta)=p^{|\eta|}q^{N-|\eta|}.\]

Indeed every particle-hole exchange is reversible and every root injection/removal pair satisfies detailed balance \(q p = p q\) after accounting for the common occupations of other vertices. Thus \(\pi_q(\varnothing)=q^N\). Successive visits to the empty state are regenerative. Each renewal cycle consists of the empty holding time \(E\sim\operatorname{Exp}(p)\) followed by \(B_q\) started from \(a\). The renewal-reward relation gives

\[q^N=\frac{\mathbb E E}{\mathbb E E+\mathbb E B_q}=\frac{1/p}{1/p+\mathbb E B_q}.\]

Rearranging proves the exact formula for every \(0<q<1\).

**2. A single isolated slow eigenvalue.** At \(q=0\), root removal is absent and particle number never decreases. Since the graph is finite and connected, every nonempty configuration can reach the fully occupied configuration \(\mathbf F\) by finitely many allowed moves and injections. Therefore \(K_0\) has exactly one recurrent state, \(\mathbf F\); zero is a simple eigenvalue, its right eigenvector is the all-ones vector \(\mathbf1\), its left eigenvector is \(\delta_{\mathbf F}\), and all other eigenvalues have strictly negative real parts. For \(0<q<1\), the killed nonempty chain is irreducible as a nonnegative semigroup. Consequently its spectral bound \(-\lambda_q\) is simple with a strictly positive right eigenvector \(h_q\). Finite-dimensional analytic perturbation at \(q=0\) gives \(\lambda_q\) and \(h_q\) analytic for small \(q\), normalized by \(h_q(\mathbf F)=1\), with \(h_0\equiv1\).

The row sums of the killed generator are zero except at \(a\), where \((K_q\mathbf1)(a)=-q\). Thus \(\partial_qK_q|_{q=0}\mathbf1=-\mathbf1_{\{a\}}\). Differentiating \(K_qh_q=-\lambda_qh_q\) at zero and multiplying by \(\delta_{\mathbf F}\) shows \(\lambda'_0=0\). Writing \(h_q=\mathbf1-qg+O_G(q^2)\), coefficient comparison gives

\[K_0g=-\mathbf1_{\{a\}},\qquad g(\mathbf F)=0.\]

The unique solution is the occupation-time potential

\[g(\eta)=\mathbb E^{q=0}_\eta\!\left[\int_0^{T_{\mathbf F}}\mathbf1_{\{\eta_t=a\}}\,dt\right].\]

Once two particles are present at \(q=0\), the configuration can never return to \(a\), so \(g=0\) on every two-or-more-particle state. Before the first injection, a single particle performs the walk with generator \(L_G\); an extra particle is injected at unit rate whenever the walk is off the root. Therefore \(g(a)=T_G\) as defined above. The matrix \(D_o-L_G\) is strictly positive definite because \(G\) is connected, ensuring \(T_G\) is finite and positive. In particular,

\[h_q(a)=1-qT_G+O_G(q^2).\]

**3. Exact flux identity and first correction.** Detailed balance for the *unkilled* chain implies \(\pi_q\) is a left reversible weight for \(K_q\). Multiply the eigenvector equation by the restriction of \(\pi_q\) to nonempty states and sum. All internal transitions cancel, leaving only the loss from \(a\) into empty:

\[\lambda_q\sum_{\eta\ne\varnothing}\pi_q(\eta)h_q(\eta)=q\,\pi_q(a)h_q(a).\]

Since \(\pi_q(a)=p q^{N-1}\), and \(h_q(\mathbf F)=1\), the left sum is \(1+O_G(q^2)\): the fully occupied state's mass is \(1-O(q)\), other states have total mass \(O(q)\), and on those states \(h_q-1=O_G(q)\); the missing empty mass is \(q^N=O(q^2)\). Inserting the expression for \(h_q(a)\) proves

\[\lambda_q=pq^N(1-qT_G+O_G(q^2)).\]

**4. Exponential law and moments.** The spectral projection \(P_q\) for \(-\lambda_q\) converges to \(\mathbf1\,\delta_{\mathbf F}\) as \(q\downarrow0\). The complementary spectrum remains uniformly bounded away from the imaginary axis. Consequently for some constants \(C,c>0\) independent of sufficiently small \(q\),

\[e^{tK_q}=e^{-\lambda_qt}P_q+R_q(t),\qquad \|R_q(t)\|\le Ce^{-ct},\quad t\ge0.\]

Starting from \(a\), \(\mathbb P(B_q>t)=e_a^\top e^{tK_q}\mathbf1\), where \(e_a\) is the coordinate vector at state \(a\). Because \(e_a^\top P_q\mathbf1\to1\) and \(\lambda_q/q^N\to1\), setting \(t=u/q^N\) yields \(\mathbb P(q^NB_q>u)\to e^{-u}\) for each \(u>0\). The same estimate, together with \(\lambda_q\ge cq^N\) for small \(q\), gives \(\mathbb P(q^NB_q>u)\le C'e^{-c'u}\). Integrating \(s\int_0^\infty u^{s-1}\mathbb P(q^NB_q>u)\,du\) and applying dominated convergence proves all positive-moment limits.

**5. Exact geometry constants.** For the unit-rate path rooted at an endpoint, \(D_o-L_G\) is tridiagonal with diagonal \((1,3,\ldots,3,2)\) and adjacent entries \(-1\). The cofactor formula and the recurrence for its continuants yield \(((D_o-L_G)^{-1})_{oo}=F_{2N-1}/F_{2N-2}\). For the unit-rate star with root at its center, its block matrix has root diagonal \(N-1\), leaf block \(2I\), and root-leaf entries \(-1\). The Schur complement at the root is \((N-1)-(N-1)/2=(N-1)/2\); its reciprocal is \(2/(N-1)\). This proves both explicit formulas and the same-size geometry contrast.

## Verification
The standalone file `verify.py` constructs the *actual finite-state killed generator* and the one-particle Green matrix independently, checks stationary product weights, validates the exact excursion mean by solving the linear first-passage system for several densities and graphs, compares the first spectral correction to direct diagonalization, and verifies finite-time survival against the claimed exponential scaling. This finite check supports but does not replace the above all-graph proof. Execute with `python verify.py` using Python 3, NumPy and SciPy.

## Relationship to prior work
Chatterjee, Ramola and Dhar (arXiv:2609.32314) establish the symmetric-exclusion side-branch model and its product steady state, and identify a hierarchy of rare-vacancy decay rates scaling as powers of \(q\). In their Section III.2 and appendices, the finite-dimensional restricted generators are used for numerical survival approximations. The present statement does not re-claim the generator or the power-law exponent: it distinguishes the exact empty-to-empty excursion from steady-state tagged waiting, establishes its full limiting law, and extracts the first graph-resolved coefficient of the rarest decay rate.

Iyer, Barma, Singh and Dhar (arXiv:2312.15508) study the earlier asymmetric-exclusion branch residence problem and employ rare-configuration/Kac reasoning; that classical reasoning is sufficient to motivate the exact mean here, and the mean formula by itself is not asserted as a standalone new principle. Santos and Schütz (Phys. Rev. E **64**, 036107, 2001) obtain open-SEP time correlations on a semi-infinite chain, rather than a finite-branch clearing-time spectral correction. Floreani and González Casanova (arXiv:2307.02481) treat general SEP reservoir steady states, with emphasis on multiple boundaries, not this dense single-reservoir first-passage coefficient. The spectral expansion uses standard finite-state perturbation theory; priority for this specific asymptotic coefficient remains subject to broader specialist comparison.

## Limitations
The theorem is for a *fixed* finite graph as density approaches one. The implicit constant in \(O_G(q^2)\) depends on the graph; no uniform-in-\(N\) limit is claimed. For non-path graphs the excursion is a global clearing event and need not be the residence of the first entering tagged particle. The model has one reversible reservoir, not an asymmetric or correlated environment. Both the exact mean and leading-order scaling are consequences of established Markov-chain structures; the specifically assessed contribution is the graph-dependent next order and its explicit path/star separation. A published restricted-generator representation could implicitly contain the coefficient, so independent literature-priority verification remains open.

## References
1. A. Chatterjee, K. Ramola, D. Dhar, *Continuously varying exponents in the distribution of waiting times in the symmetric exclusion process on a percolation cluster*, arXiv:2609.32314, first submitted 2026-09-26. https://arxiv.org/abs/2609.32314
2. C. Iyer, M. Barma, H. Singh, D. Dhar, *Asymmetric simple exclusion process on the percolation cluster: Waiting time distribution in side-branches*, arXiv:2312.15508, first submitted 2023-12-24. https://arxiv.org/abs/2312.15508
3. J. E. Santos, G. M. Schütz, *Exact time-dependent correlation functions for the symmetric exclusion process with open boundary*, Phys. Rev. E **64**, 036107 (2001). https://doi.org/10.1103/PhysRevE.64.036107
4. S. Floreani, A. González Casanova, *Non-equilibrium steady state of the symmetric exclusion process with reservoirs*, arXiv:2307.02481, first submitted 2023-07-05. https://arxiv.org/abs/2307.02481
