# The strong-colonization extinction coefficient is universal on trees and cycle-controlled on unicyclic networks

## Finding

Fix an arbitrary finite, connected, simple, undirected graph \(G=(V,E)\) with \(n=|V|\ge 2\). A patch at vertex \(v\) is either occupied or empty. Occupied vertices independently become empty at rate \(1\); each empty vertex becomes occupied at rate \(\lambda\) per occupied neighbor, where \(\lambda>0\). Start with all patches occupied, and let \(T_G(\lambda)\) be the first time all patches are empty (the empty state is absorbing).

For every nonempty proper vertex set \(S\subsetneq V\), define its edge-boundary size \(c_G(S)=|\{\{u,v\}\in E:u\in S,v\notin S\}|\). For an ordering \(\pi=(\pi_1,\ldots,\pi_n)\) of the vertices set \(S_k^\pi=V\setminus\{\pi_1,\ldots,\pi_k\}\). Define the positive graph constant

\[
Z(G)=\sum_{\pi\in\mathfrak S(V)}\prod_{k=1}^{n-1}\frac1{c_G(S_k^\pi)}.
\]

**Theorem (exact leading extinction coefficient).** For every such fixed graph,

\[
\lim_{\lambda\to\infty}\lambda^{1-n}\,\mathbb E[T_G(\lambda)]=\frac1{Z(G)}.
\]

The same constant has the geometry-dependent integral representation, for any fixed anchor vertex \(r\in V\),

\[
Z(G)=\int_{\mathbb R^{V\setminus\{r\}}}\exp\left(-\sum_{\{u,v\}\in E}|t_u-t_v|\right)\prod_{v\ne r}dt_v,\qquad t_r=0.
\]

In particular, **all trees with \(n\) vertices have the same leading persistence**, independent of their degrees, branching, and diameter:

\[
Z(G)=2^{n-1},\qquad \mathbb E[T_G(\lambda)]\sim(\lambda/2)^{n-1}.
\]

If \(G\) is unicyclic with unique cycle of length \(\ell\ge3\), then

\[
Z(G)=2^{n-\ell}\frac{\binom{2\ell-2}{\ell-1}}{2^{\ell-1}},\qquad
\mathbb E[T_G(\lambda)]\sim (\lambda/2)^{n-1}\frac{4^{\ell-1}}{\binom{2\ell-2}{\ell-1}}.
\]

Consequently attached tree geometry does not affect the leading unicyclic coefficient; at fixed \(n\) its multiplier relative to trees strictly increases with cycle length \(\ell\), with successive multipliers in the ratio \(2\ell/(2\ell-1)>1\).

## Assumptions and scope

This is a continuous-time *finite-state, homogeneous contact/colonization process*, not the discrete-time incidence model of the motivating source. Only the one-parameter limit \(\lambda\to\infty\) at each **fixed** connected graph is asserted. The extinction rate is normalized to \(1\); dividing time by a common rate \(\delta>0\) gives the corresponding general homogeneous-rate version. Edges are unweighted and bidirectional; vertices have no spontaneous immigration. The initial state is full occupancy, and \(T_G(\lambda)\) is finite almost surely at each finite \(\lambda\) because finite runs of local extinctions can empty every patch.

## Proof

**1. One rare extinction excursion.** Let \(F=V\) and \(0=\varnothing\). Begin at \(F\). The first loss has waiting time of mean \(1/n\), and deletes each \(v\in V\) with probability \(1/n\). Call the path from the resulting \(F\setminus\{v\}\) to its first arrival at either \(F\) or \(0\) an excursion. Whenever the occupied set \(S\) is nonempty and proper, the jump rates are \(|S|\) downwards and \(\lambda c_G(S)\) upwards. Connectivity guarantees \(c_G(S)\ge1\). A specified downward move from \(S\) has embedded-chain probability

\[
\frac1{|S|+\lambda c_G(S)}=\frac1{\lambda c_G(S)}+O_G(\lambda^{-2}).
\]

A successful excursion with no upward move deletes the remaining \(n-1\) vertices in a specified order. Summing these disjoint orders and the uniformly distributed initial vertex therefore gives the success probability

\[
p_\lambda:=\Pr_F(\text{excursion reaches }0\text{ before }F)
=\frac{Z(G)}{n\lambda^{n-1}}+O_G(\lambda^{-n}).
\]

For rigor in the error: any excursion hitting \(0\) after \(u\ge1\) upward jumps must contain \(n-1+u\) downward jumps after its first loss. For \(\lambda\ge 2n\) each specified downward step has probability at most \(\lambda^{-1}\); at each step there are at most \(n\) possible vertices. Summing over all such state paths by their \(u\) and using an upper bound of the form \(C_G^u\lambda^{-(n-1+u)}\) proves that the total contribution of successful paths with one or more upwards steps is \(O_G(\lambda^{-n})\) for sufficiently large \(\lambda\). The expansion of each of finitely many monotone paths has the same error order.

Every proper nonempty state has colonization total rate at least \(\lambda\). Starting at such a state, the next \(n-1\) embedded moves can fill every empty patch with conditional probability bounded below by \(1/2\) for all sufficiently large \(\lambda\). Each holding time before absorption in \(F\) or \(0\) has mean at most \(\lambda^{-1}\). Dividing the embedded path into \(n-1\)-step blocks gives a uniform geometric tail for its length and hence an excursion mean duration \(O_G(\lambda^{-1})\).

**2. Renewal at full occupancy.** Each return to \(F\) starts an independent trial. The mean trial time is \(1/n+O_G(\lambda^{-1})\); the success probability is \(p_\lambda\). The first-step renewal equation is valid whether or not success affects the trial duration and yields

\[
\mathbb E[T_G(\lambda)]
=\frac{1/n+O_G(\lambda^{-1})}{Z(G)/(n\lambda^{n-1})+O_G(\lambda^{-n})}
=\frac{\lambda^{n-1}}{Z(G)}(1+O_G(\lambda^{-1})).
\]

**3. The cut integral.** Fix an anchor vertex \(r\) and write \(t_r=0\). Decompose \(\mathbb R^{n-1}\), up to measure-zero equal-coordinate hyperplanes, into its \(n!\) chambers indexed by the total order \(\pi\) of all \(n\) coordinates. On each chamber, the \(n-1\) consecutive nonnegative spacings \(g_k\) are coordinates with absolute Jacobian \(1\), even when the anchor \(r\) is in the middle of the order. An edge crosses precisely those consecutive gaps separating its endpoints. Therefore

\[
\sum_{\{u,v\}\in E}|t_u-t_v|
=\sum_{k=1}^{n-1}c_G(S_k^\pi)g_k.
\]

Integrating the independent gaps \(g_k\in(0,\infty)\) produces exactly the product in \(Z(G)\), and summing chambers proves the integral formula.

**4. Trees.** For a tree \(G\), orient edges from \(r\). The variables \(x_e=t_{\mathrm{child}(e)}-t_{\mathrm{parent}(e)}\) are integer-triangular coordinates with absolute Jacobian \(1\) and \(\sum_{\{u,v\}\in E}|t_u-t_v|=\sum_e|x_e|\). Thus the integral factors as \(\prod_e\int_\mathbb R e^{-|x|}\,dx=2^{n-1}\).

**5. Unicyclic graphs.** Repeatedly integrate leaf-edge coordinates of every tree attached to the unique cycle. Each removed leaf multiplies the integral by \(2\), independent of attachment location. The remaining \(\ell\)-cycle integral equals

\[
I_\ell=\int_{\mathbb R^{\ell-1}}e^{-|x_1|-\cdots-|x_{\ell-1}|-|x_1+\cdots+x_{\ell-1}|}\,dx_1\cdots dx_{\ell-1}.
\]

If \(X_1,\ldots,X_\ell\) are independent variables with the Laplace density \(e^{-|x|}/2\), then \(I_\ell=2^\ell f_{X_1+\cdots+X_\ell}(0)\). Their characteristic function is \((1+t^2)^{-1}\), so Fourier inversion and the beta integral give

\[
f_{X_1+\cdots+X_\ell}(0)=\frac1{2\pi}\int_{-\infty}^\infty(1+t^2)^{-\ell}\,dt
=\frac{\binom{2\ell-2}{\ell-1}}{2^{2\ell-1}}.
\]

Therefore \(Z(G)=2^{n-\ell}I_\ell\), proving the stated formula. With \(a_\ell=4^{\ell-1}/\binom{2\ell-2}{\ell-1}\), elementary binomial simplification gives \(a_{\ell+1}/a_\ell=2\ell/(2\ell-1)\), which is greater than \(1\).

## Verification

Run `python3 verify.py` in the directory containing the accompanying standalone program; no nonstandard libraries or additional files are needed. It checks the exact subset-recursion formula on every labeled tree on 2–6 vertices (1,441 trees) and every connected labeled unicyclic graph on 3–5 vertices (238 graphs), including their cycle lengths. Six further examples use exact rational continuous-time Markov-chain solutions at \(\lambda=20\) and \(\lambda=60\), independently compare direct permutation sums and subset recursion, and test convergence of their normalized means toward the analytical coefficient. These are finite corroborations, **not** an exhaustive test over all graphs or an infinite-parameter proof.

For example, all five-vertex trees have coefficient \(\mathbb E[T_G(\lambda)]/\lambda^4\to1/16\). A triangle with two appended tree vertices yields \(1/6\); a square with one pendant vertex yields \(1/5\); and a five-cycle yields \(8/35\). The full analytical proof above, not the finite computation, establishes every graph-family statement.

## Relationship to prior work

McVinish and Pollett (2014, publicly indexed online in 2016) study Hanski's **discrete-time** stochastic patch-occupancy model as patch number increases, and designate primary MSC 92D40. Their model motivates the question of how persistence varies with habitat connectivity, but their limit is not the fixed-network, high-colonization limit here. Van de Bovenkamp and Van Mieghem (2015) give exact mean SIS survival expressions for complete and star graphs, rather than a stated cut-integral or all-tree invariant. Holme and Tupikina (2018) compute mean SIS extinction times across 12,110 small connected graphs, and obtain computational evidence for \(\lambda^{n-1}\) growth and graph-dependent prefactors. Their Section 3.3 and Appendix derive high-rate features for that finite census, while Section 3.4 explores empirical structural predictors; the cycle-length and tree-shape formulas stated here are not established by the inspected full article. The present result turns the high-rate coefficient into an exact finite graph integral and classifies tree/unicyclic topology for arbitrary fixed sizes. No assertion that the general contact process, graph-cut identities, or Laplace convolution are themselves new is made.

## Limitations

The claim does not describe the finite-rate ordering of graphs, the next term in the asymptotic series, limits jointly in graph size and colonization rate, heterogeneous rates, directed transmission, or stochastic external catastrophes. The factor \(\lambda^{n-1}\) depends on the normalization that each graph edge independently transmits at rate \(\lambda\). For the 2015 complete/star comparison, only the publisher's abstract and indexed metadata were accessible, not its full primary text; this is a residual risk for precise priority claims. The later 2018 article was read substantially in full, and the 2014 model's full PDF and metadata were inspected. The result has not been independently audited.

## References

1. R. McVinish and P. K. Pollett, *The Limiting Behaviour of Hanski's Incidence Function Metapopulation Model*, Journal of Applied Probability 51 (2014), 297–316, DOI: 10.1239/jap/1402578626 (publisher publicly indexes online posting February 19, 2016; primary MSC 92D40).
2. R. van de Bovenkamp and P. Van Mieghem, *Survival time of the susceptible-infected-susceptible infection process on a graph*, Physical Review E 92 (2015), 032806, DOI: 10.1103/PhysRevE.92.032806.
3. P. Holme and L. Tupikina, *Epidemic extinction in networks: Insights from the 12,110 smallest graphs*, New Journal of Physics 20 (2018), 113042, DOI: 10.1088/1367-2630/aaf016, arXiv:1802.08849.
