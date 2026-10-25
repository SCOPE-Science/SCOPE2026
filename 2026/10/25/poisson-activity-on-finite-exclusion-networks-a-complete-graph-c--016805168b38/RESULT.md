# Poisson activity on finite exclusion networks: a complete graph classification

## Finding

**Theorem.** Let \(G=(V,E)\) be a finite, connected, undirected simple graph with \(N=|V|\ge4\). Fix \(1\le k\le N-1\). In continuous-time symmetric simple exclusion with \(k\) indistinguishable particles, each occupied-to-vacant endpoint exchange along an edge occurs at rate one. Let \(C_T\) count successful exchanges during \([0,T]\). Start from the uniform equilibrium law on the \(\binom Nk\) configurations. Set \(\mu=2|E|k(N-k)/(N(N-1))\) and
\[
F(G,k)=\lim_{T\to\infty}\frac{\operatorname{Var}(C_T)}{\mathbb E C_T}.
\]
This limit exists and \(F(G,k)\ge1\). The following three assertions are equivalent:

1. \(F(G,k)=1\).
2. The stationary successful-exchange counting process is a homogeneous Poisson process (indeed, this holds from every deterministic initial configuration).
3. The number \(|\partial S|\) of edges with one endpoint in \(S\) and the other outside \(S\) is independent of the configuration \(S\subseteq V\), \(|S|=k\).

For \(k=1\) or \(k=N-1\), these equivalent assertions hold **exactly when \(G\) is regular**, and then the Poisson rate is its common degree. For every genuinely interacting occupancy \(2\le k\le N-2\), they hold **exactly** in the following two cases:

- \(G\cong K_N\), with Poisson rate \(k(N-k)\);
- \(N=2k\) and \(G\cong K_{1,N-1}\), with Poisson rate \(k\).

In every other connected, simple network with \(2\le k\le N-2\), one has the **strict** fluctuation inequality \(F(G,k)>1\). The balanced star is the sole non-complete graph supporting exactly Poissonian many-particle jump activity. No further parity or symmetry exceptions exist.

## Assumptions and scope

A configuration is a \(k\)-element set \(S\subset V\). For an edge \(\{u,v\}\in E\) with exactly one occupied endpoint, replace the occupied endpoint by the vacant endpoint at rate one. Rejected particle jumps are not counted. There are no reservoirs, creation, annihilation, or edge-dependent rates. For \(1\le k\le N-1\), connectedness ensures irreducibility; unit symmetric exchanges ensure reversibility with the uniform stationary measure \(\pi\). The number of allowed transitions from \(S\) is
\[
q(S)=|\partial S|=\sum_{u\in S}\deg(u)-2|E(G[S])|.
\]
The generator on functions of configurations is
\[
(Lf)(S)=\sum_{\substack{\{u,v\}\in E\\|\{u,v\}\cap S|=1}}[f(S\triangle\{u,v\})-f(S)].
\]
All scalar products below use \(\langle f,h\rangle_\pi=\binom Nk^{-1}\sum_{|S|=k}f(S)h(S)\). The pseudoinverse \((-L)^+\) is zero on constants and the inverse of \(-L\) on mean-zero functions.

## Proof

**1. Exact fluctuation identity.** Every edge has its endpoints separated by a uniformly random \(k\)-set with probability \(2k(N-k)/(N(N-1))\). Thus \(\mu=\langle q,1\rangle_\pi>0\). Write \(g=q-\mu\). The moment-generating tilted generator of the successful-jump count is
\[
L_z=e^zB-\operatorname{diag}(q),\qquad
(Bf)(S)=\sum_{S'\ne S}r(S,S')f(S'),
\]
where \(r(S,S')\in\{0,1\}\) is the exchange rate and \(B1=q\). On the finite irreducible state space, the analytic maximal eigenvalue \(\Lambda(z)\), normalized by \(\Lambda(0)=0\), gives the limiting cumulant generating function per unit time near \(z=0\). Its simple right eigenvector \(v_z\) can be normalized by \(\langle1,v_z\rangle_\pi=1\). Differentiating \(L_zv_z=\Lambda(z)v_z\) at zero yields
\[
\Lambda'(0)=\mu,\qquad (-L)v'_0=g,\qquad \langle1,v'_0\rangle_\pi=0.
\]
Consequently \(v'_0=(-L)^+g\). Symmetry of \(B\) in the uniform inner product gives \(\langle 1,Bh\rangle_\pi=\langle q,h\rangle_\pi\). Differentiating twice therefore yields
\[
\boxed{\quad \lim_{T\to\infty}\frac{\operatorname{Var}(C_T)}{T}
=\mu+2\langle g,(-L)^+g\rangle_\pi.\quad}
\]
For a connected exclusion configuration graph, \(-L\) is strictly positive on mean-zero functions. Therefore \(F=1+2\langle g,(-L)^+g\rangle_\pi/\mu\ge1\), and equality holds if and only if \(g\equiv0\), namely if and only if all \(k\)-vertex edge cuts have the same size. This uses the complete finite-state spectrum and does not confuse a sample-variance calculation with an infinite-time limit.

**2. Exact Poisson process criterion.** When \(q(S)\equiv\mu\), each state has an exponential holding time of rate \(\mu\). Successive holding times are independent of past transitions by the strong Markov property and have the same law, so the complete sequence of jump times is homogeneous Poisson of rate \(\mu\) from any starting configuration. Conversely a stationary Poisson jump process has asymptotic Fano ratio one, and step 1 forces constant cuts. This proves the three-way equivalence.

**3. Classification of constant-size cuts.** The boundary identity immediately gives \(q(\{u\})=\deg(u)\) and \(q(V\setminus\{u\})=\deg(u)\), proving the one-particle and one-hole cases. Now fix \(2\le k\le N-2\) and suppose every \(k\)-set has equal boundary. Fix distinct vertices \(u,v\), and put \(W=V\setminus\{u,v\}\). For every \((k-1)\)-element set \(T\subset W\), equality of boundaries for \(T\cup\{u\}\) and \(T\cup\{v\}\) implies
\[
0=\deg(u)-\deg(v)-2\sum_{w\in T}(A_{uw}-A_{vw}),
\]
with \(A\) the simple adjacency matrix. Since \(1\le k-1\le |W|-1\), comparison of two such sets differing in only one element forces \(A_{uw}-A_{vw}\) to be constant over all \(w\in W\). Denote this common number by \(c_{uv}\in\{-1,0,1\}\). Summing over \(W\) then gives \(\deg(u)-\deg(v)=(N-2)c_{uv}\). Substitution into the displayed equation yields
\[
(N-2k)c_{uv}=0\quad\text{for all }u\ne v.
\]
If \(N\ne2k\), all \(c_{uv}=0\). Then any two vertices have identical adjacency to every third vertex; symmetry of \(A\) forces all off-diagonal adjacency entries to coincide. Since \(G\) is connected, \(G\cong K_N\).

When \(N=2k\), either all \(c_{uv}=0\) and \(G\cong K_N\), or choose and orient \(u,v\) so that \(c_{uv}=1\). The vertex \(u\) is adjacent to all \(w\in W\), whereas \(v\) is adjacent to none of them. For any distinct \(w,z\in W\), the vectors of their adjacency to \(u\) agree, forcing \(c_{wz}=0\). It follows that all edges within \(W\) have one common indicator \(a\in\{0,1\}\). Let \(e=A_{uv}\). Comparing adjacency vectors of \(u\) and \(w\in W\) at \(v\) and at a different \(z\in W\) yields \(e=1-a\). If \(a=0\), then \(e=1\), giving exactly the star centered at \(u\). If \(a=1\), then \(e=0\), giving the disconnected graph consisting of a clique on \(V\setminus\{v\}\) and an isolated \(v\), contrary to connectedness. The star is therefore the only remaining possibility. The argument requires \(|W|\ge2\), ensured by \(N\ge4\).

**4. Sufficiency and exact intensities.** Every \(k\)-set in \(K_N\) has \(k(N-k)\) crossing edges. For a star with \(N=2k\), if the center is vacant there are \(k\) occupied leaves adjacent to it; if the center is occupied there are exactly \(N-k=k\) vacant leaves. Thus all configurations again have exactly \(k\) allowed exchanges. This proves every claimed case and exhausts the classification.

## Verification

The standalone standard-library script `verify.py` checks the constant-cut criterion against the classification exhaustively on **every connected labeled simple graph with four, five, or six vertices** and all nontrivial particle numbers. For genuinely interacting fillings the constant-cut graph counts, including labeled copies, are respectively five for \((N,k)=(4,2)\), one for each of \((5,2)\) and \((5,3)\), and seven for \((6,3)\). It also builds nine independent finite exclusion generators and solves their stationary Poisson equations using exact rational arithmetic. For example, the computed Fano ratios are \(1\) for a six-site three-particle star, \(26/25\) for a five-site two-particle star, \(7/6\) for a five-cycle with two particles, and \(19/15\) for a six-cycle with three particles.

Run `python verify.py` in the same directory; no packages beyond the Python standard library are required. The exhaustive range is finite; the all-order claim follows only from the analytic proof above.

## Relationship to prior work

Appert-Rolland, Derrida, Lecomte and van Wijland [1] introduce the tilted activity generator and derive cumulants for exclusion on a one-dimensional periodic ring. The general methodology in proof step 1 is a direct finite reversible-chain specialization of this established counting framework; it is not claimed independently. Their ring calculations do not provide the network-wide Poisson graph classification.

Caputo, Liggett and Richthammer [2] establish spectral-gap equality for interchange and random-walk processes on arbitrary weighted graphs, including the exclusion setting by projection. Their spectral-gap theorem neither classifies constant cut size for each particle number nor evaluates the counting-process equality case.

Lee, Loh and Sudakov [3] investigate extremal bisections and explicitly observe that all balanced bisections of a star have the same size. That known example is incorporated and credited; their bounds and existence theorems do not directly state that these are, with complete graphs, the only connected constant-bisection graphs, or extend the rigidity to every interior occupancy and Poisson jump counting. The new contribution assessed here is the complete equivalence and graph classification. This literature comparison cannot establish absolute historical priority.

## Limitations

Only finite, connected, unweighted, undirected **simple** graphs and indistinguishable hard-core particles under symmetric unit edge rates are covered. At most one successful exchange occurs at a time almost surely. The count omits rejected attempts. Exact Poisson behavior concerns the total count, not any tagged current; no full counting-law classification is claimed when \(F>1\). The strict lower bound is asymptotic in observation time and is not a uniform quantitative gap above one over all graphs. Edge-dependent conductances, disconnected graphs and particle-reservoir models may have additional equality cases and are excluded. The mathematical originality assessment is relative to the inspected literature, not a claim of exhaustive priority.

## References

[1] C. Appert-Rolland, B. Derrida, V. Lecomte, F. van Wijland, *Universal cumulants of the current in diffusive systems on a ring*, arXiv:0804.2590v1 (first posted 2008-04-16), https://arxiv.org/abs/0804.2590, particularly Section II, equations (1)–(12).

[2] P. Caputo, T. M. Liggett, T. Richthammer, *Proof of Aldous' spectral gap conjecture*, arXiv:0906.1238 (first posted 2009-06-06), https://arxiv.org/abs/0906.1238, particularly Section 1 and Theorem 1.1.

[3] C. Lee, P.-S. Loh, B. Sudakov, *Bisections of graphs*, arXiv:1109.3180 (first posted 2011-09-14), https://arxiv.org/abs/1109.3180, particularly Introduction, Theorem 1.3 and the star examples.
