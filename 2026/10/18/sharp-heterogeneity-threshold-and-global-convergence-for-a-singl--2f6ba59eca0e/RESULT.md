# Sharp heterogeneity threshold and global convergence for a single cooperative SIS hyperedge

## Finding

A single group in which infection of a susceptible member requires **every other group member** to be infectious admits a complete mean-field classification, even with a separate susceptibility and recovery rate at each member. Let \(n\ge3\), let \(a_i,r_i>0\), and consider the continuous-time deterministic system

\[
\dot x_i=-r_i x_i+\lambda a_i(1-x_i)\prod_{j\ne i}x_j,\qquad i=1,\ldots,n,\quad x\in[0,1]^n,\quad\lambda>0.
\]

Put \(b_i=a_i/r_i\), \(G=(\prod_{i=1}^n b_i)^{1/n}\), and let \(\varphi(z)\in(0,1)\) be the unique solution of \(\varphi(z)^2/(1-\varphi(z))=z\) for \(z>0\). Define

\[
X_i(s)=\varphi(b_i s),\qquad P(s)=\prod_i X_i(s),\qquad L(s)=\frac{s}{P(s)},\quad s>0.
\]

There is exactly one positive \(s_*\) satisfying

\[
\sum_{i=1}^{n}\frac{1-X_i(s_*)}{2-X_i(s_*)}=1.
\]

Write \(\lambda_*=L(s_*)\). If \(\lambda<\lambda_*\), the zero state is the **only** equilibrium and globally attracts the closed cube. At \(\lambda=\lambda_*\) the zero state coexists with exactly one interior nonhyperbolic equilibrium \(X(s_*)\), a simple saddle-node. For \(\lambda>\lambda_*\), there are precisely three equilibria: zero, a lower-branch interior saddle with exactly one positive eigenvalue, and an upper-branch interior equilibrium with all eigenvalues negative. Every trajectory in \([0,1]^n\) converges to one of the existing equilibria, including at the fold; in particular, no periodic or more complicated recurrent behavior occurs.

The fold threshold is strictly increased by individual heterogeneity at a fixed geometric mean of the infection-to-recovery ratios:

\[
\boxed{\displaystyle \lambda_*\ge\frac{(n-1)^{n-1}}{G(n-2)^{n-2}},}
\]

with **equality if and only if** \(b_1=\cdots=b_n=G\). More strongly, for fixed \(\sum_i\log b_i\), the threshold is strictly increasing under every nontrivial majorization of the vector of log-ratios (up to coordinate permutations). The exact log-sensitivity is

\[
\boxed{\displaystyle\frac{\partial\log\lambda_*}{\partial\log b_i}=-\frac{1-X_i(s_*)}{2-X_i(s_*)},\qquad\sum_i\frac{\partial\log\lambda_*}{\partial\log b_i}=-1.}
\]

This is a deterministic mean-field statement; it does not assert positive long-time prevalence for a finite stochastic SIS chain.

## Assumptions and scope

The integer \(n\ge3\) is arbitrary but fixed. Each \(x_i\) is a real fraction or marginal mean-field state, not a binary infected-individual state; \(x(0)\in[0,1]^n\). Recovery rates \(r_i\), infection coefficients \(a_i\), and the common transmission multiplier \(\lambda\) are strictly positive and constant. Infection is a **single full-order conjunctive group exposure**: vertex \(i\) receives no infection when any other group member has state zero. There are no additive pairwise channels, no overlapping hyperedges, and no stochastic fluctuation term. The cube is invariant because \(\dot x_i\ge0\) at \(x_i=0\) and \(\dot x_i=-r_i<0\) at \(x_i=1\). Every initial state exists uniquely for all nonnegative times.

The function \(\varphi(z)\) may be evaluated explicitly as \((\sqrt{z^2+4z}-z)/2\). It is smooth, strictly increasing and maps positive numbers to \((0,1)\). A numerically stable expression is \(2z/(z+\sqrt{z^2+4z})\).

## Proof

**1. Exhaustion of equilibria.** If a coordinate of an equilibrium is zero, the infection term in every other equation vanishes; then recovery makes every other coordinate zero as well. The only boundary equilibrium is the origin. At any positive equilibrium put \(P=\prod_i x_i>0\) and \(s=\lambda P\). The stationary equations, after multiplication by \(x_i\), become

\[
\frac{x_i^2}{1-x_i}=b_i s.
\]

Thus every positive equilibrium is exactly \(x=X(s)\) with \(L(s)=\lambda\). Conversely each such positive solution satisfies all the original equations. No division by a zero coordinate is used in the boundary case.

**2. Unique fold.** Implicit differentiation of \(x^2/(1-x)=z\) gives

\[
\frac{d\log\varphi(z)}{d\log z}=\frac{1-\varphi(z)}{2-\varphi(z)}.
\]

Consequently

\[
\frac{d\log L(s)}{d\log s}=1-E(s),\quad E(s):=\sum_i\frac{1-X_i(s)}{2-X_i(s)}.
\]

Each \(X_i\) increases strictly from zero to one, hence \(E(s)\) decreases strictly from \(n/2>1\) to zero. It crosses one exactly once. Moreover, as \(s\downarrow0\), the product \(P(s)\) is asymptotic to \(s^{n/2}(\prod b_i)^{1/2}\), so \(L(s)\to\infty\) because \(n\ge3\); also \(L(s)\to\infty\) as \(s\to\infty\). Therefore \(L\) has the unique nondegenerate global minimum \(\lambda_*=L(s_*)\), one root at the fold, and exactly two roots above it. Nondegeneracy follows from \(dE/d\log s<0\), giving a positive second logarithmic derivative of \(L\) at its minimum.

**3. Spectral classification.** At a positive equilibrium, direct differentiation, using the stationary identity, gives

\[
J_{ii}=-\frac{r_i}{1-x_i},\qquad J_{ij}=\frac{r_i x_i}{x_j}\quad(i\ne j).
\]

With \(D_x=\operatorname{diag}(x_i)\), \(D_r=\operatorname{diag}(r_i)\) and \(c_i=(2-x_i)/(1-x_i)\), the similar matrix \(D_x^{-1}JD_x\) is \(D_r(\mathbf1\mathbf1^\top-D_c)\). Further diagonal similarity makes it symmetric:

\[
S=zz^\top-\operatorname{diag}(r_i c_i),\qquad z_i=\sqrt{r_i}.
\]

By the rank-one inertia criterion, this matrix has exactly one positive eigenvalue if \(\sum_i1/c_i>1\), exactly one simple zero eigenvalue if the sum equals one, and exclusively negative eigenvalues if the sum is below one. Because \(\sum_i1/c_i=E(s)\), the lower branch is an index-one saddle, the upper branch is linearly asymptotically stable, and the unique fold has one simple zero eigenvalue with all other eigenvalues negative. The origin has Jacobian \(-D_r\), so is linearly asymptotically stable at every transmission rate.

**4. Global convergence, including the threshold.** On \([0,1)^n\), define the analytic potential

\[
\mathcal V(x)=\sum_i\frac{-x_i-\log(1-x_i)}{b_i}-\lambda\prod_i x_i.
\]

The equations obey the exact weighted-gradient identity

\[
\dot x_i=-r_i b_i(1-x_i)\,\partial_i\mathcal V,
\qquad
\frac{d\mathcal V}{dt}=-\sum_i r_i b_i(1-x_i)(\partial_i\mathcal V)^2.
\]

The nonnegative individual terms \(-x_i-\log(1-x_i)\) diverge as \(x_i\uparrow1\); the remaining product term is bounded below by \(-\lambda\). All sublevel sets of \(\mathcal V\) in \([0,1)^n\) are therefore compact, and the derivative vanishes precisely at equilibria. An initial coordinate equal to one enters the interior of that boundary immediately; thereafter the potential is finite. LaSalle's invariance principle traps every omega-limit set in the equilibrium set. The latter is finite (one, two, or three points), whereas any omega-limit set of a bounded continuous trajectory is connected. Hence every omega-limit set is a singleton and every trajectory converges. This argument includes points on invariant faces and the degenerate fold, and establishes global attraction of the origin below threshold.

**5. Heterogeneity inequality and sensitivity.** Put \(f(u)=\log\varphi(e^u)\). Differentiating the relation above gives

\[
 f'(u)=\frac{1-\varphi(e^u)}{2-\varphi(e^u)},\qquad
 f''(u)=-\frac{\varphi(e^u)(1-\varphi(e^u))}{(2-\varphi(e^u))^3}<0.
\]

For fixed \(G\), Jensen's strict inequality implies, for every \(s>0\),

\[
\log P(s)=\sum_i f(\log s+\log b_i)\le n f(\log s+\log G).
\]

Thus \(L(s)\ge s/\varphi(Gs)^n\). The right side has minimum at common prevalence \((n-2)/(n-1)\), found by substituting \(s=x^2/[G(1-x)]\), and this minimum equals \((n-1)^{n-1}/[G(n-2)^{n-2}]\). Strict Jensen at every finite \(s\) when ratios differ, together with the attained unique minimum of \(L\), proves strict inequality in this case. Karamata's inequality for strictly concave \(f\) yields the stronger majorization monotonicity. Finally the envelope theorem at the simple minimizing \(s_*\) gives

\[
\frac{\partial\log\lambda_*}{\partial\log b_i}=-f'(\log s_*+\log b_i)
=-\frac{1-X_i(s_*)}{2-X_i(s_*)}.
\]

The sum equals \(-1\) by the defining fold equation, completing the proof.

## Verification

The accompanying `verify.py` uses only the Python standard library. It calculates the unique fold by monotone bisection in \(\log s\), computes both interior equilibrium branches at supercritical parameters, checks their exact stationary residual identities numerically, compares the Jacobian against the rank-one formula, checks the heterogeneity bound and finite-difference log-sensitivities, and tests the potential-gradient identity. Five cases cover three through five members, including nonidentical recovery rates. For \(n=3\) and \(b=(1,1,1)\), it obtains \(\lambda_*=4\). For \(b=(1/4,1,4)\), with the same geometric mean, it obtains \(\lambda_*\approx4.586911204889\). For \(n=4\), the homogeneous bound is \(27/4\), while ratios \((1/4,1/2,2,4)\) give \(\lambda_*\approx8.383037599343\). The exact weighted-gradient algebra was also checked symbolically for three variables. All finite diagnostic tests passed. They validate implementations and examples, not the infinitely quantified theorem; the proof above supplies that conclusion.

Run `python3 verify.py` in a directory containing this file; no external package or data is needed.

## Relationship to prior work

Landry and Restrepo (arXiv:2006.15453, first submitted June 27, 2020) analyze collective hypergraph contagion and show how **hyperdegree and edge-overlap heterogeneity** affect bistability, especially through pairwise and three-body contacts. Here the graph has only one full-order group, and heterogeneity is instead in the **individual infection-to-recovery ratios**, yielding a sharp threshold and strict log-majorization law rather than a degree-distribution criterion. Their collective infection requirement is the same modeling motivation but their main equations and implications do not classify this system.

Cisneros-Velarde and Bullo (arXiv:2005.11404) analyze multiple population groups with pairwise and higher-order channels and obtain useful sufficient conditions for bistability under irreducible pairwise-contact hypotheses. Those conditions do not specify the exact fold without pairwise transmission. Higham and de Kergorlay (arXiv:2108.05451, Theorem 5.3) give a sufficient global-extinction spectral condition for collective contagion, not an if-and-only-if fold or complete endemic branch classification. Kiss et al. (arXiv:2309.12752) provide the bifurcation structure of **homogeneous**, fully connected simplicial populations; their exact homogeneous and low-order analyses do not cover node-dependent ratios in this single conjunctive group. Liang, Cui and Liu (arXiv:2408.08602, first posted August 16, 2024) address **discrete-time** hypergraph SIS and state sufficient stability and endemic conditions for general interactions, not this continuous-time exact classification. Bodó, Katona and Simon (2016) introduce hypergraph SIS mean fields for infection-rate functions of infected group counts and simulations, without the present sharp heterogeneous fold and gradient structure.

A prior discrete-Euler hypergraph-support criterion shows which positive support patterns can exist for sufficiently large transmission, but neither supplies the exact threshold nor proves convergence or the strict geometric-mean heterogeneity inequality. The present result makes no priority claim for the well-known scalar homogeneous saddle-node or for the general existence of bistability in cooperative contagion.

## Limitations

The single hyperedge and purely conjunctive assumptions are essential to the scalar equilibrium parametrization and exact potential. Allowing pairwise interactions, additional overlapping hyperedges, time-dependent coefficients, demographic noise or stochastic individual infections requires separate analysis. The theorem does not yield a closed elementary expression for \(s_*\) at arbitrary heterogeneous parameter vectors, though its defining scalar equation is strictly monotone and uniquely solvable. No exact basin-volume probability or extinction time for finite-population Markov chains is asserted. Related literature may contain an equivalent potential or a latent reduction in unindexed specialist work; this is an originality risk, not a substitute for the stated comparison.

## References

1. N. W. Landry and J. G. Restrepo, *The effect of heterogeneity on hypergraph contagion models*, arXiv:2006.15453v1 (2020-06-27), https://arxiv.org/abs/2006.15453.
2. P. Cisneros-Velarde and F. Bullo, *Multi-group SIS Epidemics with Simplicial and Higher-Order Interactions*, arXiv:2005.11404 (2020), https://arxiv.org/abs/2005.11404.
3. D. J. Higham and H.-L. de Kergorlay, *Mean Field Analysis of Hypergraph Contagion Model*, arXiv:2108.05451 (2021), https://arxiv.org/abs/2108.05451.
4. I. Z. Kiss, I. Iacopini, P. L. Simon and N. Georgiou, *Insights from exact social contagion dynamics on networks with higher-order structures*, arXiv:2309.12752 (2023), https://arxiv.org/abs/2309.12752.
5. L. Liang, S. Cui and F. Liu, *Discrete-time SIS Social Contagion Processes on Hypergraphs*, arXiv:2408.08602v1 (2024-08-16), https://arxiv.org/abs/2408.08602.
6. Á. Bodó, G. Y. Katona and P. L. Simon, *SIS epidemic propagation on hypergraphs*, Bull. Math. Biol. 78 (2016), 713–735, https://real.mtak.hu/39361/.
