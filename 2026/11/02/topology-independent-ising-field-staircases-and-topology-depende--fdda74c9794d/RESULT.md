# Topology-independent Ising field staircases and topology-dependent matching entropy on biregular line graphs

## Finding

For every finite simple biregular bipartite graph \(G=(U\sqcup W,E)\), the entire zero-temperature antiferromagnetic line-graph Ising fixed-magnetization energy is a degree-only function. This yields an exact field staircase with \(r+s-\gcd(r,s)+1\) strictly stable magnetization sectors, independent of incidence geometry. At the saturation field, however, its exact degeneracy is the number of matchings of \(G\), which can distinguish two connected graphs with identical degrees and staircase.

Write \(|U|=m\), \(|W|=n\), with every \(U\)-vertex of degree \(r\) and every \(W\)-vertex of degree \(s\), so \(N=|E|=mr=ns\). At each edge \(e\) place \(\sigma_e\in\{-1,+1\}\), and let \(J_U,J_W>0\). The Hamiltonian is
\[
H(\sigma)=J_U\sum_{u\in U}\sum_{\{e,f\}\subseteq E(u)}\sigma_e\sigma_f
+J_W\sum_{w\in W}\sum_{\{e,f\}\subseteq E(w)}\sigma_e\sigma_f-h\sum_{e\in E}\sigma_e.
\]
A simple bipartite graph cannot have a pair of distinct edges sharing both endpoints, so this is the two-coupling antiferromagnetic Ising Hamiltonian on \(L(G)\).

For \(K\in\{0,\ldots,N\}\), set \(a=\lfloor K/m\rfloor\), \(t=K-ma\), \(b=\lfloor K/n\rfloor\), \(z=K-nb\). The exact lowest energy among configurations with exactly \(K\) up spins is
\[
\begin{aligned}
E_K(h)&=\frac{J_U}{2}\bigl[(m-t)(2a-r)^2+t(2a-r+2)^2-mr\bigr]\\
&\quad+\frac{J_W}{2}\bigl[(n-z)(2b-s)^2+z(2b-s+2)^2-ns\bigr]-h(2K-N).
\end{aligned}
\]
Every minimizer, and only a minimizer, has \(a\) or \(a+1\) up-spin edges at every vertex of \(U\), and \(b\) or \(b+1\) at every vertex of \(W\). Both conditions are simultaneously realizable in every biregular bipartite graph, for every \(K\).

Set
\[
H_K=J_U(2\lfloor K/m\rfloor-r+1)+J_W(2\lfloor K/n\rfloor-s+1),\quad 0\le K<N.
\]
The consecutive-sector relation is \(E_{K+1}(h)-E_K(h)=2(H_K-h)\). For fields distinct from the \(H_K\), the unique minimizing *magnetization* sector is an element of
\[
\{0,N\}\cup\{K:0<K<N,\ m\mid K\text{ or }n\mid K\},
\]
and every sector in this set is stable on a nonempty open field interval. There are precisely \(r+s-\gcd(r,s)+1\) such sectors. At a critical field \(h=H_K\), all sectors across the corresponding maximal consecutive run of identical \(H_K\) coexist.

At \(h_{\mathrm{sat}}=J_U(r-1)+J_W(s-1)\), the complete set of ground states consists of the all-up configuration with an arbitrary matching of down-spin edges. The exact saturation degeneracy is therefore
\[
\Omega_{\mathrm{sat}}(G)=\sum_{j\ge0}\mathsf m_j(G),
\]
where \(\mathsf m_j(G)\) is the number of size-\(j\) matchings in \(G\).

Two explicit connected, cubic bipartite examples have six vertices on each side and edges \((i,i+t\bmod6)\), \(i\in\mathbb Z/6\mathbb Z\), with \(t\in\{0,1,2\}\) or \(t\in\{0,1,3\}\). Both have identical field breakpoints \(-4J,0,4J\) when \(J_U=J_W=J\), but their saturation degeneracies are respectively \(1104\) and \(1092\). Thus degree-only energy and topology-dependent critical entropy coexist even in connected regular networks.

## Assumptions and scope

The finite base graph is simple, bipartite, and \((r,s)\)-biregular; \(m,n,r,s\ge2\) and \(mr=ns\). No connectivity, girth, transitivity or planarity assumption is needed. Couplings \(J_U,J_W\) are positive and field \(h\) is real. Spins are classical \(\pm1\) on the edges of the base graph (equivalently, the vertices of its line graph). Every conclusion concerns zero temperature, and the energy formula concerns every integer magnetization sector \(K\in[0,N]\).

## Proof

**Exact lower bound.** At a base vertex \(u\) of degree \(d\), let \(k_u\) be the number of incident up spins. Its spin sum is \(2k_u-d\), and the pair-interaction identity is
\[
\sum_{\{e,f\}\subseteq E(u)}\sigma_e\sigma_f=\frac{(2k_u-d)^2-d}{2}.
\]
For fixed total \(\sum_{u\in U}k_u=K\), strict discrete convexity of \(k\mapsto(2k-r)^2\) implies that its sum is minimized precisely when every \(k_u\in\{a,a+1\}\), with exactly \(t\) larger entries. The same argument on \(W\), independently, gives \(\{b,b+1\}\) and exactly \(z\) larger entries. Adding these two lower bounds yields the displayed exchange-energy expression.

**Simultaneous attainment for all sectors.** Consider a directed flow network with arcs source-to-\(u\) of integral lower/upper capacities \([a,a+1]\), each original arc \(u\)-to-\(w\) of capacity \([0,1]\), arcs \(w\)-to-sink of integral capacities \([b,b+1]\), and a sink-to-source return arc with both capacities equal to \(K\). Assign each original arc the fractional value \(K/N\); each source-to-\(u\) flow is \(rK/N=K/m\), and each \(w\)-to-sink flow is \(sK/N=K/n\). This is a feasible circulation. The incidence matrix of a directed network is totally unimodular and all arc bounds are integers, so an integral feasible circulation exists. Its \(0/1\) flows on original arcs select exactly \(K\) up-spin edges with all vertex counts balanced on *both* sides. Therefore both lower bounds are attained simultaneously. The strictly convex local costs and positive couplings also establish the stated necessary and sufficient description of all fixed-sector minimizers.

**Field staircase.** Adding the \((K+1)\)-st up spin changes the degree-balanced \(U\) exchange contribution by \(2J_U(2\lfloor K/m\rfloor-r+1)\), and similarly for \(W\). The Zeeman term changes by \(-2h\). Consequently the exact adjacent energy difference is \(2(H_K-h)\). The \(H_K\) form a nondecreasing sequence; increments are strictly positive at exactly those \(K\) divisible by \(m\) or \(n\) with \(0<K<N\), because both couplings are positive. A minimizing sector away from critical fields can therefore occur only at these breakpoints or the endpoints, and each such breakpoint has a nonempty stability interval between two distinct consecutive threshold levels. There are \(r-1\) interior multiples of \(m\), \(s-1\) interior multiples of \(n\), and \(\gcd(r,s)-1\) common interior multiples of \(\operatorname{lcm}(m,n)\), giving the exact count \(r+s-\gcd(r,s)+1\). At a common threshold the adjacent differences vanish on the complete corresponding run and the coexisting sectors follow.

**Saturation degeneracy.** Relative to the all-up state, flipping a subset \(F\subseteq E\) costs
\[
\Delta H=2(h-h_{\mathrm{sat}})|F|+4J_U\sum_{u\in U}\binom{\deg_F(u)}{2}+4J_W\sum_{w\in W}\binom{\deg_F(w)}{2}.
\]
Indeed each flipped spin changes its field and all incident pair contributions; a pair of flipped adjacent spins restores the original pair energy, producing the displayed positive correction. At \(h=h_{\mathrm{sat}}\) the difference is nonnegative, and vanishes exactly when \(F\) has no two edges sharing an endpoint, namely when \(F\) is a matching. This proves the bijection and matching count. For the six-by-six witnesses, exact subset dynamic programming over the six vertices on one bipartite side yields totals \(1104\) and \(1092\); their common staircases follow from the degree parameters.

## Verification

Run `python3 verify.py` with Python 3.8 or later. Its finite brute-force checker enumerates all spin configurations for five small, explicitly constructed biregular bipartite base graphs under four coupling pairs, checking the analytic fixed-sector energy for all \(204\) sectors across \(20\) full enumerations. It independently counts matchings by exhaustive edge masks and a bipartite subset recursion; it compares critical degeneracy to Ising energy minima, checks all predicted field breakpoints, and evaluates two connected cubic witnesses. All checks passed as recorded in `CHECK_RESULT.txt`. These finite experiments support, but cannot replace, the preceding general network-integrality proof.

## Relationship to prior work

Saturation entropy and magnetization plateaux of antiferromagnetic Ising models on kagome and ladder geometries were studied by Varma (2013). Dyer, Heinrich, Jerrum and Müller (2020) study finite-temperature approximation of antiferromagnetic Ising partition functions on general line graphs. The present assertion is about an **exact zero-temperature fixed-magnetization energy and complete field staircase** uniformly valid over arbitrary sparse biregular bipartite base graphs, plus the distinction between degree-universal energy and graph-dependent matching degeneracy. It does not claim as new the pair-spin square identity, the total-unimodularity method, the standard matching representation at saturation, or previously known complete-bipartite special cases. The existence of a mathematically equivalent treatment elsewhere remains possible.

## Limitations

The theorem excludes nonbiregular base graphs, nonbipartite base graphs, sign-changing or nonuniform-in-a-part couplings, nonuniform magnetic fields, quantum spin interactions and positive-temperature thermodynamics. Beyond the matching sum at saturation and illustrative examples, it does not provide a general closed formula for each critical-field ground-state multiplicity. An exhaustive mathematical-literature priority search or independent audit has not been performed.

## References

- V. K. Varma, *Antiferromagnetic Ising model saturation field entropies: ladders and kagome lattice*, arXiv:1305.4606, first submitted 20 May 2013, https://arxiv.org/abs/1305.4606.
- M. Dyer, M. Heinrich, M. Jerrum and H. Müller, *Polynomial-time approximation algorithms for the antiferromagnetic Ising model on line graphs*, arXiv:2005.07944, first submitted 16 May 2020, https://arxiv.org/abs/2005.07944.
- D. de Werra, *On the use of alternating chains and hypergraphs in edge coloring*, Journal of Graph Theory 3 (1979), https://doi.org/10.1002/jgt.3190030208. The combinatorial balancing background is credited; no assertion about its full text is made here.
