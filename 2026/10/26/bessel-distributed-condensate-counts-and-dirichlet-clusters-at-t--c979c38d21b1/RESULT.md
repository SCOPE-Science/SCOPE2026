# Bessel-distributed condensate counts and Dirichlet clusters at the fast-rate zero-range transition

## Finding
Fix an integer \(A\ge2\), positive weights \(u_0=1,u_1,\ldots,u_{A-1}\), and a sequence of canonical zero-range stationary ensembles on \(L\) sites with \(N_L\) particles. Their single-site weights are
\[
w_L(n)=\begin{cases}u_n,&0\le n<A,\\\theta_L^{-1},&n\ge A.\end{cases}
\]
Set
\[
z=\sum_{n=0}^{A-1}u_n,\qquad
\mu=\frac1z\sum_{n=0}^{A-1}nu_n,\qquad
e=\rho-\mu,\qquad b=\frac{e}{\Theta z}.
\]
Suppose \(N_L/L\to\rho>\mu\) and \(\theta_L/L^2\to\Theta\in(0,\infty)\). Write \(K_L=\#\{x:\eta_x\ge A\}\) for the number of condensed sites. Then \(K_L\) converges in distribution to an integer \(K\ge1\) with the **Bessel count law**
\[
\mathbb P(K=k)=\frac{b^{k-1}}{k!(k-1)!W(b)},\qquad
W(b)=\sum_{j=1}^\infty\frac{b^{j-1}}{j!(j-1)!}
=\frac{I_1(2\sqrt b)}{\sqrt b},\quad k=1,2,\ldots .
\]
Conditioned on \(K_L=k\), list the condensed sites in increasing site-label order. Their occupations divided by \(L\) converge jointly to
\[
e(V_1,\ldots,V_k),\qquad (V_1,\ldots,V_k)\sim\operatorname{Dirichlet}(1,\ldots,1).
\]
For \(k=1\), the Dirichlet distribution is the deterministic vector \((1)\). Both statements hold jointly in the disjoint union of finite-dimensional simplices; the limiting finite number of sites carries total mass \(e\). In particular,
\[
\mathbb P(K=1)=\frac{\sqrt b}{I_1(2\sqrt b)},\qquad
\mathbb E K=\frac{\sqrt b\,I_0(2\sqrt b)}{I_1(2\sqrt b)}.
\]

## Assumptions and scope
The canonical probability of a configuration \(\eta\in\mathbb N_0^L\) with \(\sum_x\eta_x=N_L\) is proportional to \(\prod_xw_L(\eta_x)\). These weights arise, for example, in any irreducible zero-range process with balanced spatial hopping and departure rates \(g_L(n)=w_L(n-1)/w_L(n)\) for \(n\ge1\): there is one large rate \(g_L(A)=u_{A-1}\theta_L\), while \(g_L(n)=1\) for \(n>A\). The quantities \(A\), the finite sequence \((u_n)\), \(\rho\), and \(\Theta\) are fixed independently of \(L\). No statement is made for critical bulk density \(\rho=\mu\), for nonquadratic scalings of \(\theta_L\), or for time-dependent mixing or dynamics. The primary subject is the condensed phase of an interacting nonequilibrium particle system (MSC2020 82C22); probabilistic enumeration is the proof technique.

## Proof
**1. Exact partition by cluster number.** Let \(Z_{L,N}^{(k)}\) denote the partition-function contribution from configurations with precisely \(k\) sites having occupation at least \(A\). Let \(X\) have \(\mathbb P(X=n)=u_n/z\) for \(0\le n<A\), and let \(S_j\) be the sum of \(j\) independent copies of \(X\). For \(k\ge1\), condition on the choice of the \(k\) cluster sites and the total bulk occupation \(S_{L-k}=s\). Each cluster has occupation \(A+m_i\), with \(m_i\ge0\) and \(\sum_i m_i=N_L-s-Ak\). Counting weak compositions gives the **finite exact identity**
\[
Z_{L,N_L}^{(k)}={L\choose k}\theta_L^{-k}z^{L-k}
\mathbb E\!\left[
{N_L-S_{L-k}-Ak+k-1\choose k-1}
\mathbf1_{\{S_{L-k}\le N_L-Ak\}}
\right]. \tag{1}
\]
In the indicator event, the binomial coefficient is ordinary and nonnegative; it is interpreted as zero outside that event. The zero-cluster term is
\[
Z_{L,N_L}^{(0)}=z^L\mathbb P(S_L=N_L).\tag{2}
\]

**2. Fixed count asymptotics.** For each fixed \(k\ge1\), the bounded-variable law of large numbers gives \(S_{L-k}/L\to\mu\) in probability. Thus \((N_L-S_{L-k}-Ak)/L\to e>0\). Since the bracketed binomial coefficient in (1), divided by \(L^{k-1}\), is uniformly bounded and tends to \(e^{k-1}/(k-1)!\), bounded convergence applies. Using \({L\choose k}\sim L^k/k!\) and \(\theta_L\sim\Theta L^2\), one gets
\[
\frac{Z_{L,N_L}^{(k)}}{z^{L-1}L/\theta_L}
\longrightarrow \frac{b^{k-1}}{k!(k-1)!}.\tag{3}
\]
For \(k=1\), this limit equals \(1\). For \(k=0\), Hoeffding's inequality yields \(\mathbb P(S_L=N_L)\le\exp(-cL)\) for some \(c>0\), because \(N_L/L\to\rho>\mu\). Equations (2) and \(\theta_L=O(L^2)\) imply \(Z^{(0)}_{L,N_L}/(z^{L-1}L/\theta_L)\to0\).

**3. Uniform domination and normalization.** Choose constants \(R,c_0>0\) such that \(N_L\le RL\) and \(\theta_L\ge c_0L^2\) for all sufficiently large \(L\). In (1), the binomial factor is at most \(((R+1)L)^{k-1}/(k-1)!\), for every feasible \(k\le L\). Together with \({L\choose k}\le L^k/k!\), this proves the uniform bound
\[
0\le\frac{Z_{L,N_L}^{(k)}}{z^{L-1}L/\theta_L}
\le\frac{B^{k-1}}{k!(k-1)!},\quad B=\frac{R+1}{c_0z}.\tag{4}
\]
It also holds with zero left side for infeasible \(k\). The bounding series converges. Dominated convergence across the full series in \(k\), combined with (2)–(3), gives
\[
\frac{Z_{L,N_L}}{z^{L-1}L/\theta_L}\longrightarrow
W(b)=\frac{I_1(2\sqrt b)}{\sqrt b}.\tag{5}
\]
Dividing each sector by (5) proves the count law. The same factorial domination gives convergence of count moments, including the expression for \(\mathbb EK\) by differentiating the series: \(\sum_{k\ge1}k b^{k-1}/[k!(k-1)!]=I_0(2\sqrt b)\).

**4. Joint macroscopic masses.** For each fixed \(k\ge1\), conditional on the number of cluster sites, the distribution of the bulk sum \(S_{L-k}\) is the original product-sum distribution multiplied by the polynomial factor in (1). The denominator of this reweighting grows like \(L^{k-1}e^{k-1}/(k-1)!\); its numerator on the event \(|S_{L-k}/L-\mu|>\varepsilon\) is bounded by \(O(L^{k-1})\exp(-c_\varepsilon L)\). Hence the reweighted bulk still has \(S_{L-k}/L\to\mu\) in probability. Consequently the total cluster excess \(M_L=N_L-S_{L-k}-Ak\) satisfies \(M_L/L\to e\). Conditional on \(M_L\) and \(k\), the ordered excess occupations are **exactly uniform** among weak compositions \((m_1,\ldots,m_k)\) of \(M_L\), because each cluster has the same weight \(\theta_L^{-1}\). Standard lattice Riemann sums on the simplex give \((m_1/M_L,\ldots,m_k/M_L)\Rightarrow\operatorname{Dirichlet}(1,\ldots,1)\). Adding \(A/L\to0\) to each coordinate proves the conditional mass law. Finally the count law and factorial tightness in (4) combine the conditional statements into the claimed joint convergence. \(\square\)

## Verification
The standalone `checker.py` reconstructs the canonical partition function by exact-integer coefficient generation and a stable logarithmic evaluation. It tests two natural bulk occupation laws, \(A=2\) and \(A=3\), with \(\rho=1\) and \(\rho=2\), respectively, \(\Theta=1/2\), and \(L\in\{40,80,160\}\). The observed \(\ell^1\) discrepancy in the count distribution falls from approximately \(0.048\) to \(0.012\) in each case; the reported limiting first four probabilities agree with the displayed Bessel count law. These finite calculations check the exact partition decomposition and scaling consistency only. The proof of the infinite-size limit is analytic and does not depend on extrapolating the computations. Run `python checker.py` from the extracted package folder using Python 3 with no third-party packages.

## Relationship to prior work
Jatuviriyapornchai and Grosskinsky (2024), *Condensation in Zero-Range Processes with a Fast Rate* (arXiv:2404.02590; J. Stat. Phys. 191, 147), introduce precisely these stationary weights up to harmless normalization, proving independent mesoscopic clusters for \(0<\gamma<2\) and a single macroscopic cluster for \(\gamma>2\) when \(\theta_L\asymp L^\gamma\). Their Section 4 explicitly identifies the transition \(\gamma=2\) as a difficult unresolved case with multiple macroscopic clusters. The present theorem gives its number distribution and full conditional mass partition, not an alternative proof of either neighboring regime.

Blank, Chleboun, Grosskinsky, and Jatuviriyapornchai (2026), arXiv:2603.00806, extend a related stationary-weight model to polynomial large-occupation tails; their transition line \(\gamma=\kappa+2\) is explicitly left open. The present case corresponds to a constant condensed weight, \(\kappa=0\), and quadratic scaling, not to their proved off-line theorems. Earlier inclusion-process results of Jatuviriyapornchai, Chleboun, and Grosskinsky (2019/2020) establish Poisson–Dirichlet macroscopic partitions for asymptotically \(1/n\) condensed weights. Those weights and the resulting random partition law differ from the constant-weight, finite-count Bessel–Dirichlet mixture here.

## Limitations
The result concerns the stationary canonical measure for a positive fixed bulk support and the single fast-rate defect, with \(\rho>\mu\) and \(\theta_L/L^2\to\Theta>0\). It gives no rates of convergence, no dynamical equilibration or metastable times, and no uniform simultaneous regime as \(\Theta\to0\) or \(\Theta\to\infty\). The finite count \(K\) is not Poisson–Dirichlet; conditional Dirichlet vectors have random **finite** dimension.

## References
1. W. Jatuviriyapornchai and S. Grosskinsky, *Condensation in Zero-Range Processes with a Fast Rate*, arXiv:2404.02590 (first posted 2024-04-03), Journal of Statistical Physics **191**, 147 (2024), DOI 10.1007/s10955-024-03362-0. Full text: https://link.springer.com/article/10.1007/s10955-024-03362-0
2. J. Blank, P. Chleboun, S. Grosskinsky, and W. Jatuviriyapornchai, *Condensation in Stochastic Lattice Gases with Size-Dependent Stationary Weights*, arXiv:2603.00806 (2026), https://arxiv.org/html/2603.00806v1
3. W. Jatuviriyapornchai, P. Chleboun, and S. Grosskinsky, *Structure of the Condensed Phase in the Inclusion Process*, Journal of Statistical Physics **178**, 682–710 (2020; first online 2019), DOI 10.1007/s10955-019-02451-9, https://link.springer.com/article/10.1007/s10955-019-02451-9
4. MSC2020, category 82C22, *Interacting particle systems in time-dependent statistical mechanics*, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=82C22
