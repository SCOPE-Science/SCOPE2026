# A sharp bridge-placement phase diagram for SIS thresholds in clique–star communities

## Finding
Fix an integer \(k\ge 1\). Define the contact community \(G_k\) by taking a five-vertex clique with distinguished vertex \(a\), attaching a hub \(h\) to \(a\), and attaching \(k\) pendant vertices to \(h\). A second community is a two-vertex clique \(K_2\). Connect one fixed vertex of \(K_2\) to any vertex \(v\) of \(G_k\) by a single symmetric contact of weight \(w>0\), with every internal contact of weight one. Write \(B_{k,v}(w)\) for the resulting symmetric nonnegative matrix and \(\Lambda_{k,v}(w)=\rho(B_{k,v}(w))\). The mean-field discrete-time SIS threshold is \(\tau_{k,v}(w)=1/\Lambda_{k,v}(w)\).

**Complete optimal placement classification.** For every \(w>0\), a vertex minimizing the global SIS threshold is necessarily either \(a\) or \(h\). More precisely:

1. For \(1\le k\le 4\), \(a\) uniquely minimizes \(\tau_{k,v}(w)\) for every \(w>0\).
2. For \(5\le k\le 13\), put \(z_k=3k/(k-4)\), let \(P_k(z)=z^4-3z^3-(k+5)z^2+(3k+3)z+4k\), and define
   \[
   w_k^2=\frac{P_k(z_k)(z_k^2-1)}{z_k(z_k-3)(z_k^2-k)}>0.
   \]
   If \(0<w<w_k\), \(a\) uniquely minimizes the global threshold; if \(w>w_k\), \(h\) uniquely minimizes it. At \(w=w_k\), precisely \(a\) and \(h\) tie, each giving \(\Lambda=z_k\), and both beat every other placement.
3. For every \(k\ge 14\), \(h\) uniquely minimizes the global threshold for every \(w>0\).

In particular, for \(k=7\), the sharp crossover is \(w_7=\sqrt{40}=2\sqrt{10}\). The hub has internal degree \(8\) and \(a\) has degree \(5\), yet attaching to \(a\) has the lower epidemic threshold for every \(w<2\sqrt{10}\). Thus a static degree ranking does not determine the most epidemic-promoting bridge endpoint.

**Exact opposite SIS outcomes at the same biological parameters.** In the \(k=7\) graph, set \(\delta=1/2\) and use the weighted SIS recursion stated below. At \(w=6\) and \(\beta=149/2000\), attaching the bridge at \(a\) produces a supercritical positive endemic fixed point, while attaching at \(h\) produces exponential extinction from every initial probability vector. At \(w=7\) and \(\beta=263/4000\), the two outcomes reverse: \(a\) gives extinction and \(h\) permits a positive endemic fixed point. All four contact probabilities are admissible (\(0\le\beta B_{ij}\le1\)); these are exact strict sign comparisons, not floating-point inferences.

## Assumptions and scope
The graph \(G_k\) has \(k+6\) vertices and \(B_{k,v}(w)\) has \(k+8\). The bridge is undirected, of weight \(w\), and is the only contact between the two fixed communities. The local threshold set \(\{1/\rho(A(G_k)),1\}\) is independent of the chosen bridge endpoint and its weight, while the global threshold depends on both. All spectral claims hold for every integer \(k\ge1\), every real \(w>0\), and every vertex \(v\) of \(G_k\). This is a weighted-contact extension of the unweighted network SIS setting, not a statement about arbitrarily structured communities.

The mean-field SIS map is, for coordinates \(p_i(t)\in[0,1]\),
\[
 F_i(p)=1-[1-(1-\delta)p_i]\prod_{j\ne i}(1-\beta B_{ij}p_j),
 \quad 0<\delta<1,\quad \beta>0,\quad \beta\max_{ij}B_{ij}\le1.
\]
It is the independence-closure nonlinear dynamical system, **not** the exact finite-population stochastic epidemic chain. Its Jacobian at the disease-free state is \((1-\delta)I+\beta B\). Away from equality, \(\beta\rho(B)<\delta\) yields global exponential extinction and \(\beta\rho(B)>\delta\) yields a positive endemic fixed point and persistence from every nonzero initial probability vector. The equality case is not asserted.

## Proof
Write \(A_k=A(G_k)\), \(R(z)=(zI-A_k)^{-1}\), and \(g_v(z)=R(z)_{vv}\) for \(z>\rho(A_k)\). The clique \(K_5\) is a proper connected subgraph, so \(\rho(A_k)>4\). Symmetry reduction into the distinguished clique vertex, the other four clique vertices, the hub, and the leaves gives
\[
 \det(zI-A_k)=z^{k-1}(z+1)^3P_k(z),\qquad
 P_k(z)=z^4-3z^3-(k+5)z^2+(3k+3)z+4k.
\]
In particular \(P_k(z)>0\) for \(z>\rho(A_k)\). Cramer's rule, or the same four-class block elimination, gives
\[
 g_a(z)=\frac{(z-3)(z^2-k)}{P_k(z)},\qquad
 g_h(z)=\frac{z(z-4)(z+1)}{P_k(z)}.
\]
If \(b\) is any of the four other clique vertices and \(\ell\) is any pendant, the remaining comparisons are
\[
 \begin{aligned}
 g_a-g_h&=\frac{(4-k)z+3k}{P_k(z)},\\
 g_a-g_b&=\frac{z(z-2)}{(z+1)P_k(z)}>0,\\
 g_a-g_\ell&=\frac{4(z^2-k+1)}{zP_k(z)}>0,\\
 g_h-g_\ell&=\frac{k(z-4)(z+1)+4}{zP_k(z)}>0.
 \end{aligned}
\]
The third inequality follows since \(\rho(A_k)>\sqrt{k+1}\) (the graph contains the \((k+1)\)-leaf star around \(h\) as a proper connected subgraph). Thus only \(a\) or \(h\) can maximize \(g_v(z)\) at any \(z>\rho(A_k)\).

The diagonal resolvent of the fixed endpoint of \(K_2\) is \(g_*(z)=z/(z^2-1)\). The rank-one bridge Schur complement and positivity give the **unique** Perron root \(\Lambda_{k,v}(w)>\rho(A_k)\) as the unique solution of
\[
 w^2g_v(z)g_*(z)=1. \tag{1}
\]
Uniqueness follows because both positive diagonal resolvents decrease strictly from a divergent value to zero as \(z\) runs from \(\rho(A_k)\) to infinity. Equation (1) also proves the comparison rule: if \(g_u(z)>g_v(z)\) at the root for placement \(u\), then \(\Lambda_{k,u}(w)>\Lambda_{k,v}(w)\) and hence \(\tau_{k,u}(w)<\tau_{k,v}(w)\).

For \(k\le4\), \((4-k)z+3k>0\), proving the first regime. For \(k>4\), the two resolvents can cross only at \(z_k=3k/(k-4)\). For \(5\le k\le15\), \(P_k(4)=-4\) and \(P'_k(4)=5(15-k)\ge0\), \(P''_k(4)=2(55-k)>0\), \(P^{(3)}_k(4)=78>0\), so \(P_k\) increases strictly on \((4,\infty)\) and has exactly one root there, namely \(\rho(A_k)\). Direct substitution yields
\[
 P_k(z_k)=\frac{4k(k^2-20k+28)(k^2-14k+4)}{(k-4)^4}.
\]
This is positive for all integers \(5\le k\le13\), and negative for \(k=14,15\). Thus \(z_k>\rho(A_k)\) exactly for \(5\le k\le13\) in this range. For \(k\ge16\), \(z_k\le4<\rho(A_k)\). Accordingly, \(h\) dominates throughout the physical resolvent domain if \(k\ge14\). For \(5\le k\le13\), the continuous strictly increasing root \(\Lambda_{k,a}(w)\) crosses \(z_k\) at the unique weight \(w_k\) in the statement, and the resolvent inequalities on either side prove the claimed switch and exclusivity. At \(k=7\), \(P_7(7)=980\), \(g_a(7)=g_h(7)=6/35\), and \(g_*(7)=7/48\), hence \(w_7^2=40\).

For the exact SIS reversal, compare the positive scalar \(w^2g_v(z)g_*(z)-1\) to zero at \(z=\delta/\beta\); its sign equals that of \(\Lambda_{7,v}(w)-z\). The four exact values, in order \((w,v,z)=(6,a,1000/149),(6,h,1000/149),(7,a,2000/263),(7,h,2000/263)\), are
\[
 \frac{161921311387069}{30945671139799931}>0,\quad
 -\frac{75260970757}{80798096970757}<0,\quad
 -\frac{10771563216311279}{2415836082953935779}<0,\quad
 \frac{3475861420267}{1067536934579733}>0.
\]
The indicated values \(z\) exceed \(\rho(A_7)\): indeed \(\rho(A_7)<5\), verified by the strict positive Collatz supersolution with values \(1\) at clique vertices, \(1/2\) at the hub and \(1/5\) at leaves. Each displayed rational \(z\) exceeds \(5\).

Finally the SIS map is order preserving on the cube. By the union bound, \(F(p)\le((1-\delta)I+\beta B)p\), so strict subcriticality gives global exponential extinction. In the strict supercritical case, a positive Perron vector \(u\) yields \(F(\varepsilon u)>\varepsilon u\) for all sufficiently small \(\varepsilon>0\), because \(DF(0)u=((1-\delta)+\beta\rho(B))u>u\). Monotone bounded iteration from \(\varepsilon u\) converges to a strictly positive fixed point. Since \(0<\delta<1\), any nonzero nonnegative initial state eventually has all coordinates strictly positive on the connected graph and then dominates a suitable \(\varepsilon u\), proving positive lower persistence. This finishes the stated claims.

## Verification
Run `python verify_bridge.py` with SymPy installed. The script builds the actual finite adjacency matrices, rechecks all Green-function comparisons algebraically and against exact matrix inversions, verifies the dimension and quartic identities, evaluates the sharp crossover for every \(k\in\{5,\dots,13\}\), and checks all four rational SIS sign certificates. It also checks the full \(15\)-vertex matrices at the two example contact weights. All infinite-family assertions follow from the symbolic proof, not from finite enumeration.

## Relationship to prior work
Dung and Phuc (2026) study the discrete-time SIS threshold set of community contact networks and prove local thresholds are no smaller than the global threshold. Their local thresholds and the global Rayleigh comparison remain valid after suitable weighted generalization, but they do not classify where a single weighted intercommunity contact should attach. The present result fixes the two communities and varies **only the endpoint and weight of their sole bridge**, obtaining an exact change of the risk-maximizing endpoint while the two local thresholds remain constant.

Li, Eliassi-Rad, and Zhang (2023) develop edge-centrality interventions for weighted network spreading; their derivatives and optimization concepts do not contain this integer-leaf trichotomy or its exact threshold. Ma, Valdez, and Braunstein (2020) analyze different bridge-node regimes in stochastic SIR/percolation on modular random networks, which is neither the deterministic weighted SIS threshold nor the exact fixed-graph endpoint question here. The Schur complement, resolvent, Perron theory, and SIS linearization are standard tools and are not asserted to be new. The proposed contribution is their exact model-specific synthesis into the **complete \(k\)-by-\(w\) optimal placement phase diagram** and a strict opposite-outcome witness.

## Limitations
This is a two-community graph family with one weighted bridge and a mean-field independence-closure SIS map. The proof does not treat multiple bridges, arbitrary community topology, transmission dependencies, the true absorbing finite-state stochastic SIS chain, prevalence or time-to-extinction optimization, or the exact threshold boundary \(\beta\rho(B)=\delta\). Exact placement optimality concerns minimizing \(1/\rho(B)\), not maximizing a finite-horizon infection count. The earlier stochastic SIR bridge study is related but not directly comparable. A more general existing graph-spectral attachment theorem could imply some spectral components after specialization; no independent novelty certification is claimed.

## References
1. H. P. Dung and N. H. Phuc, *An Epidemic Threshold Set for Networks*, arXiv:2607.14048, first public 2026-07-15, https://arxiv.org/abs/2607.14048.
2. D. Li, T. Eliassi-Rad, and H. R. Zhang, *Optimal Intervention on Weighted Networks via Edge Centrality*, arXiv:2303.09086, https://arxiv.org/abs/2303.09086.
3. J. Ma, L. D. Valdez, and L. A. Braunstein, *Role of bridge nodes in epidemic spreading: Different regimes and crossovers*, arXiv:2005.14170, https://arxiv.org/abs/2005.14170.
