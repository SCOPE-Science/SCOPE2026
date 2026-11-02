# Exact speed–wisdom Pareto frontier for degree-weighted learning on regular-base hub networks

## Finding

**Theorem.** Let \(H\) be any simple undirected \(d\)-regular graph on \(N\) vertices, where \(1\le d\le N-2\); it need not be connected. Let \(G=K_1\vee H\) add one universally adjacent hub \(h\). For the no-self-loop degree-weighted DeGroot rule, define \(\mu_1=d,\mu_2,\ldots,\mu_N\) as the adjacency eigenvalues of \(H\), with multiplicity and with just one copy of \(d\) distinguished. Let \(L=\max_{2\le j\le N}|\mu_j|\) and, for every \(\alpha\in\mathbb R\), put

\[
q=\left(\frac{N}{d+1}\right)^\alpha,\qquad p=\frac{q}{q+d}\in(0,1).
\]

Then \(1\le L\le d\) and the complete spectrum, stationary influence weights, sharp contraction rate and long-run estimation variance are

\[
\operatorname{spec}(T)=\left\{1,-p,\frac{1-p}{d}\mu_2,\ldots,\frac{1-p}{d}\mu_N\right\},
\]
\[
\pi_h=\frac{p}{1+p},\qquad\pi_v=\frac{1}{N(1+p)}\quad(v\in H),
\]
\[
\rho(p)=\max\left\{p,\frac Ld(1-p)\right\},\qquad
V(p)=\sigma^2\frac{p^2+1/N}{(1+p)^2}.
\]

The rate is the sharp worst-case contraction in stationary-weighted \(L^2\); variance assumes independent, unbiased initial errors of common variance \(\sigma^2>0\). The variance-minimizing and speed-minimizing parameters are each unique:

\[
p_{\mathrm{wis}}=\frac1N,\quad
\alpha_{\mathrm{wis}}=\frac{\log(d/(N-1))}{\log(N/(d+1))}<0,
\]
\[
p_{\mathrm{spd}}=\frac{L}{d+L},\quad
\alpha_{\mathrm{spd}}=\frac{\log L}{\log(N/(d+1))}\ge0,
\quad\rho_{\min}=\frac{L}{d+L}.
\]

The **entire** nondominated speed–variance Pareto set is

\[
\boxed{\quad p\in\left[\frac1N,\frac{L}{d+L}\right]
\quad\Longleftrightarrow\quad
\alpha\in[\alpha_{\mathrm{wis}},\alpha_{\mathrm{spd}}].\quad}
\]

The exact variance penalty for choosing maximal speed is

\[
\boxed{\frac{V(p_{\mathrm{spd}})}{V(p_{\mathrm{wis}})}
=\frac{(N+1)\big(NL^2+(d+L)^2\big)}{N(d+2L)^2}.}
\]

If \(H\) is disconnected or bipartite, then \(L=d\): the fastest parameter gives hub influence \(1/3\) and variance penalty \((N+1)(N+4)/(9N)\sim N/9\). Thus fastest DeGroot consensus can have nonvanishing error variance even when the minimum-variance consensus becomes consistent as network size grows.

## Assumptions and scope

The degrees in \(G\) are \(N\) at the hub and \(d+1\) at each peripheral vertex. For adjacent vertices \(u,v\), transition weights are

\[
T_{uv}=\frac{\mathbf1_{\{u\sim v\}}\deg_G(v)^\alpha}
{\sum_{w\sim u}\deg_G(w)^\alpha},\qquad b(t+1)=Tb(t).
\]

The hub and all peripheral vertices use the same exponent. There are no self-loops. For the statistical objective the initial beliefs are \(b_u(0)=\theta+\varepsilon_u\), with independent mean-zero errors of equal finite variance \(\sigma^2\); no Gaussian assumption is needed. Speed means SLEM or, equivalently here, worst-case stationary-weighted \(L^2\) contraction; variance means the limiting consensus mean squared error around \(\theta\). The two objectives are minimized jointly by Pareto order.

## Proof

**Block factorization.** A peripheral vertex puts probability \(p=q/(q+d)\) on the hub and \((1-p)/d\) on each of its \(d\) neighbors in \(H\). The hub puts probability \(1/N\) on every peripheral vertex. Consequently,

\[
T=\begin{pmatrix}0&\mathbf1^\top/N\\p\mathbf1&(1-p)A_H/d\end{pmatrix}.
\]

Because \(A_H\mathbf1=d\mathbf1\) and \(A_H\) is symmetric, the hub-plus-constant-periphery subspace has block matrix \(\left(\begin{smallmatrix}0&1\\p&1-p\end{smallmatrix}\right)\), eigenvalues \(1,-p\). The peripheral zero-sum subspace has action \((1-p)A_H/d\) and supplies the remaining eigenvalues, including extra copies of \(d\) in disconnected cases. This proves the full spectral formula with multiplicities.

**Stationarity and sharp rate.** The cone is connected, and every edge of \(H\) makes a triangle with the hub, so the Markov chain is irreducible and aperiodic. The stated stationary weights satisfy detailed balance, hence \(T\) is self-adjoint in \(L^2(\pi)\). Its consensus projector is \(\Pi=\mathbf1\pi^\top\), and for all integers \(t\ge1\),

\[
\|T^t-\Pi\|_{L^2(\pi)\to L^2(\pi)}
=\big[\max\{p,L(1-p)/d\}\big]^t.
\]

The adjacency norm gives \(L\le d\); the trace identity gives

\[
L^2\ge\frac{Nd-d^2}{N-1}
=1+\frac{(d-1)(N-d-1)}{N-1}\ge1.
\]

Thus the two linear branches of \(\rho\) have a unique intersection at \(p=L/(d+L)\), its unique minimum. Since \(p/(1-p)=q/d\), this yields \(\alpha_{\mathrm{spd}}\).

**Variance and Pareto interval.** Independently centered errors give

\[
V(p)=\sigma^2\sum_u\pi_u^2,
\qquad V'(p)=\frac{2\sigma^2(p-1/N)}{(1+p)^3}.
\]

The variance is minimized uniquely at \(p=1/N\), with \(V_{\min}=\sigma^2/(N+1)\); solve the parameter relation to obtain \(\alpha_{\mathrm{wis}}\). Since \(L\ge1\) and \(d+1<N\),

\[
\frac1N<\frac1{d+1}\le\frac{L}{d+L}.
\]

For smaller \(p\) than the variance optimum, increasing \(p\) reduces both \(V\) and \(\rho\). Above the rate optimum, decreasing \(p\) reduces both. On the interval between the optima, \(V\) strictly increases as \(\rho\) strictly decreases, so precisely this interval is nondominated. Substitution at \(p=L/(d+L)\) gives the displayed penalty.

**Structural extreme.** If \(H\) is disconnected, \(d\) has adjacency multiplicity at least two; if bipartite, \(-d\) is an eigenvalue. Hence either hypothesis implies \(L=d\), giving the explicit penalty and hub influence. For the infinite friendship-graph family, take \(H\) as a union of \(m\ge2\) disjoint edges: then \(N=2m\), \(d=L=1\); at the fastest parameter \(V\to\sigma^2/9\), whereas at the variance optimum \(V=\sigma^2/(2m+1)\to0\). Conversely, connected nonbipartite regular bases satisfy \(L<d\).

## Verification

Run `python3 verify.py` with Python 3 and SymPy. The included checker reconstructs the full characteristic polynomial and stationary detailed balance using exact rational matrices, verifies variance identities, and checks the linear-price specialization. It passed 145 exact cases: 48 full-matrix cases (12 regular-base graphs times four rational hub transition rates), 97 rational size/variance checks, plus a symbolic derivative identity. Example graphs include cycles, regular disconnected components, the triangular prism and the Petersen graph. Finite verification is diagnostic; the preceding argument proves the result for all permitted parameters.

## Relationship to prior work

Cheng, Han, Tong, Wu and Xing [1] introduce the same degree-weighted learning model, prove general stationary influence and weighted-spectral convergence formulas and discuss qualitative wisdom–speed tradeoffs. Their inspected propositions and stochastic-block-model Appendix C do not state the all-regular-base cone decomposition, the complete finite-network Pareto interval, or the exact divergent variance penalty. Kooij and Dubbeldam [2] calculate the Kemeny constant and unweighted spectral behavior of generalized windmills; their fixed simple-walk statistic differs from the popularity-parametrized objectives here. Olesker-Taylor and Zanetti [3] study fastest mixing with different admissible transition-law constraints. Santini [4] studies the same target-degree power bias on scale-free random graphs, but the accessible abstract optimizes exploration rather than the spectral speed and consensus-estimation variance of regular-base cones; the primary full text was inaccessible in this review. General reversible-chain identities are acknowledged as known; the contribution is their explicit all-size cone specialization and the resulting two-objective boundary, not a new generic Markov-chain spectral theorem.

## Limitations

The regular-base and universal-hub hypotheses, common exponent, and no-self-loop model are essential to the exact formulas as stated. Heteroscedastic or correlated initial errors change the variance criterion. The rate is weighted-\(L^2\) worst-case contraction, not total-variation mixing time, Kemeny's constant, or a finite-time prediction objective. Full publication priority against every specialist source is not established; no independent external audit has occurred.

## References

1. Chen Cheng, Xiao Han, Xin Tong, Yusheng Wu, Yiqing Xing, *Degree-Weighted Social Learning*, arXiv:2311.07010, first publicly posted 13 November 2023, https://arxiv.org/abs/2311.07010 ; relevant proof and appendices inspected in https://arxiv.org/html/2311.07010v3 .
2. Robert E. Kooij and Johan L. A. Dubbeldam, *Kemeny's constant for several families of graphs and real-world networks*, *Discrete Applied Mathematics* 285 (2020), 96–107, https://doi.org/10.1016/j.dam.2020.05.033 .
3. Sam Olesker-Taylor and Luca Zanetti, *Geometric bounds on the fastest mixing Markov chain*, arXiv:2111.05816, https://arxiv.org/abs/2111.05816 .
4. Simone Santini, *Popularity-driven random walks on a class of scale-free graphs*, *Physical Review E* 111 (2025), 054303, https://doi.org/10.1103/PhysRevE.111.054303 . The article abstract was available; the full text was not accessible.
