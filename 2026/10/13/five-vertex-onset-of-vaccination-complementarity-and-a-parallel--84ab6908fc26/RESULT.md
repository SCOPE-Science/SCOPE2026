# Five-vertex onset of vaccination complementarity and a parallel-route identity

## Finding

**Theorem (sharp onset and exact five-cycle phase).** Let \(G\) be a finite simple undirected contact graph with \(n\) vertices. Vaccinate a set \(S\) of vertices before independently retaining each remaining contact edge with probability \(p\in[0,1]\). Choose one potential initial infected vertex uniformly among the original \(n\) vertices; if vaccinated, it starts no outbreak. Let \(R_G(S,p)\) denote expected outbreak size, and let the vaccination benefit be \(B_G(S,p)=R_G(\varnothing,p)-R_G(S,p)\).

1. For **every graph with at most four vertices**, \(B_G(\cdot,p)\) is a submodular set function for every \(p\in[0,1]\). In fact, this remains true with independent, nonidentical edge-retention probabilities. For **every forest of any order** it is submodular under arbitrary independent edge probabilities.
2. On the five-cycle \(C_5\), the benefit is submodular **if and only if** \(0\le p\le\rho\), where \(\rho\) is the unique zero in \((0,1)\) of \(1+3p+5p^2-10p^3\); numerically \(\rho\approx0.935152824805653\). For two nonadjacent vaccine sites \(a,b\), the mixed difference of the unnormalized outbreak burden at the empty set equals
\[
\Delta_{C_5,p}(\varnothing;a,b)
=2p^2(1+3p+5p^2-10p^3).
\]
Thus **five vertices is the sharp minimum** for failure of diminishing returns under this outbreak and seeding model. At \(p=19/20\), the mixed difference is exactly \(-61009/160000\), so the vaccination-benefit submodularity difference is \(-61009/800000\).
3. For every deterministic contact graph, the mixed difference has the exact **parallel-route identity** in the proof below. It quantifies positive fragmentation effects against negative effects from parallel alternate connections between two vaccinated sites.

## Assumptions and scope

Let \(G=(V,E)\), \(n=|V|\ge1\), and \(S\subseteq V\). For every edge of \(G-S\), a Bernoulli variable independently declares transmission possible. The resulting open graph has components \(\mathcal C\). An outbreak starting at a uniformly selected original vertex infects its entire open component, and a seed in \(S\) produces zero cases. The uniform selection is from **all original vertices**, not merely unvaccinated ones; this keeps the denominator fixed across vaccination policies. Then
\[
R_G(S,p)=\frac1n\mathbb E_p\!\left[\sum_{C\in\mathcal C(G-S)}|C|^2\right],\qquad
F_G(S,p)=nR_G(S,p).
\]
The empty graph has burden zero. A benefit \(B\) is submodular precisely when, for every \(S\subseteq V\) and distinct \(a,b\in V\setminus S\),
\[
\Delta_{G,p}(S;a,b):=F_G(S,p)+F_G(S\cup\{a,b\},p)
-F_G(S\cup\{a\},p)-F_G(S\cup\{b\},p)\ge0.
\]
The \(n\) scaling does not change signs. Distinct transmission probabilities are allowed in parts 1 and 3; the exact five-cycle threshold assumes a common probability \(p\).

## Proof

**1. Deterministic parallel-route identity.** First fix a deterministic open graph \(H\) and a vaccinated set \(S\). If \(a,b\) belong to different components of \(H-S\), the mixed difference of \(F_H(S)=\sum_C|C|^2\) is zero. Otherwise let \(W\) be their common component. Remove \(a,b\) from \(W\) and classify every residual component by adjacency in \(W\) to \(a\) only, \(b\) only, or both. Write \(A\) and \(B\) for the combined sizes of the first two classes, and \(c_1,\ldots,c_r\) for the sizes of the doubly attached components. Every component is in one of these classes because \(W\) is connected. Put \(C=\sum_i c_i\).

The component \(W\) contributes \((2+A+B+C)^2\) before deleting either site. After deleting \(a\), the component containing \(b\) has size \(1+B+C\); all \(a\)-only components occur separately. Interchanging \(a,b\) is analogous. After deleting both, every residual component occurs separately. The squared sizes of the singly attached components cancel in the alternating sum, leaving
\[
\begin{aligned}
\Delta_{H}(S;a,b)
&=(2+A+B+C)^2-(1+B+C)^2-(1+A+C)^2+\sum_i c_i^2\\
&=2\left[(A+1)(B+1)-\sum_{1\le i<j\le r}c_ic_j\right].
\end{aligned}
\]
This is the announced identity. The negative term exists only when at least two disjoint residual components each independently connect \(a\) and \(b\). The same formula applies to the deterministic realization of every independent-edge model; expectation commutes with this linear mixed difference.

**2. Universal four-vertex bound.** If \(|V(H)|\le4\), the graph \(W\setminus\{a,b\}\) contains at most two vertices. Thus the sum over distinct doubly attached components is either zero or at most one, while \((A+1)(B+1)\ge1\). The deterministic mixed difference is nonnegative for every \(S,a,b\) and for every deterministic subgraph \(H\). Averaging over independently open edges proves the assertion for arbitrary edge-retention parameters, including \(0\) and \(1\).

**3. Forest bound.** On a forest, the unique path \(P_{uv}\) between connected vertices \(u,v\) is traversable precisely when all its edges are open and none of its vertices is vaccinated. Consequently
\[
F_G(S)=\sum_{\substack{(u,v)\in V^2\\u,v\text{ connected in }G}}
\left(\prod_{e\in E(P_{uv})}p_e\right)
\mathbf1\{S\cap V(P_{uv})=\varnothing\}.
\]
The path for \(u=v\) has no edges. Each function \(S\mapsto\mathbf1\{S\cap T=\varnothing\}\) is supermodular: its mixed difference is \(1\) if \(a,b\in T\) and \(S\cap T=\varnothing\), and is zero otherwise. All coefficients are nonnegative. Hence \(F_G\) is supermodular and \(B_G\) submodular for any forest, regardless of its size or independent edge probabilities.

**4. The complete five-cycle phase.** Label the five-cycle consecutively \(0,1,2,3,4\), with edges joining consecutive labels modulo five. Take \(a=0\) and \(b=2\), which are nonadjacent. The probability of connecting any given adjacent pair is \(p+p^4-p^5\), and of connecting any pair at cycle distance two is \(p^2+p^3-p^5\). Since there are five unordered pairs of each type and diagonal pairs contribute five, direct pair counting gives
\[
F_{C_5}(\varnothing,p)=5+10(p+p^4-p^5)+10(p^2+p^3-p^5).
\]
Deleting one vertex leaves a four-vertex path, while deleting vertices \(0\) and \(2\) leaves one isolated vertex and one edge. Thus
\[
F_{C_5}(\{0\},p)=F_{C_5}(\{2\},p)=4+6p+4p^2+2p^3,
\qquad F_{C_5}(\{0,2\},p)=3+2p.
\]
Subtracting yields exactly \(2p^2(1+3p+5p^2-10p^3)\).

It remains to prove this pair is the *only possible* source of negative mixed differences. If \(S\ne\varnothing\), the graph \(C_5-S\) is a forest, so part 3 applies. If \(S=\varnothing\) and \(a,b\) are adjacent, the three residual vertices form a path with at most one component attached to both \(a\) and \(b\) in any open-edge realization. The negative term of the parallel-route identity is therefore zero, and the mixed difference is nonnegative. The dihedral symmetry of \(C_5\) makes all nonadjacent pairs equivalent to \(\{0,2\}\). Consequently all submodularity inequalities hold precisely when the displayed polynomial is nonnegative.

Write \(h(p)=1+3p+5p^2-10p^3\). Its derivative \(h'(p)=3+10p-30p^2\) has exactly one positive zero, at which \(h\) changes from increasing to decreasing. Since \(h(0)=1>0\) and \(h(1)=-1<0\), \(h\) has exactly one zero \(\rho\in(0,1)\), is positive below it, and is negative above it. At \(p=0\), the factor \(p^2\) makes every mixed difference zero. At \(p=19/20\), \(h(p)=-169/800\), giving \(\Delta=-61009/160000\). Since each smaller graph is covered by part 2, five vertices is sharp. \(\square\)

## Verification

`CHECK/verify.py` uses only the Python standard library. From the directory containing its parent `CHECK` folder, run `python CHECK/verify.py`. The verifier enumerates every labeled undirected simple graph on two through five vertices, every choice of two distinct vaccination sites, and every possible previously vaccinated subset; it checks the deterministic parallel-route identity exactly and verifies nonnegativity on orders at most four. It also enumerates every one of the 32 open-edge states of the five-cycle to reconstruct the claimed polynomial in integer arithmetic, and checks the rational witness \(p=19/20\).

The exact checker output is:

`VERIFY_OK structural_and_small_graph_cases=83506 C5_coefficients=[0, 0, 2, 6, 10, -20] C5_gap_at_19_over_20=-61009/160000`

Finite enumeration only corroborates the general deterministic identity and forest theorem; the displayed algebra and unique-path argument prove those statements for all graph orders.

## Relationship to prior work

Schneider, Mihaljev, Havlin, and Herrmann (2011) motivate vaccination through network fragmentation and expected reachability. Holme (2017) analyzes exact epidemic importance on small graphs in a different stochastic epidemic model. Srivastava and Teng (2024) establish that immunization objectives can be non-submodular and develop approximation guarantees. Li, Huang, Lee, and Eun (2023) prove tree submodularity in a **different fixed-source, delayed-immunization SI model**. The present theorem does **not** claim that vaccination non-submodularity, path-based influence, or fragmentation susceptibility was previously unknown. Its assessed contribution is the exact parallel-route mixed-difference identity for uniform-original-seed outbreak burden, the sharp universal four-vertex guarantee, and the complete five-cycle transmissibility threshold. Brightwell and Winkler's (2009) similarly titled “Submodular Percolation” concerns chains in a modular lattice and does not address vertex-vaccination outbreak submodularity.

## Limitations

The epidemic is a static, independent bond-transmission/reachability model with perfect vaccines. The initial potential source is sampled uniformly from the **original** vertex set, including removed vertices that then produce zero infections. Choosing uniformly only from surviving vertices changes the set function and need not preserve the theorem. The result provides neither finite-sample statistical estimates of transmission risk nor an approximation guarantee for vaccination optimization. We make no claim that the same sharp threshold holds for time-dependent SIR or heterogeneous primary infection sources. Previously unindexed coverage in network reliability or immunization literature remains possible; independent audit has not been performed.

## References

1. C. M. Schneider, T. Mihaljev, S. Havlin, and H. J. Herrmann, “Suppressing epidemics with a limited amount of immunization units,” arXiv:1102.1929 (first publicly posted 2011-02-09), later *Physical Review E* 84, 061911 (2011). https://arxiv.org/abs/1102.1929
2. P. Holme, “Three faces of node importance in network epidemiology: Exact results for small graphs,” arXiv:1708.06456 (2017). https://arxiv.org/abs/1708.06456
3. A. Srivastava and S.-H. Teng, “Overcoming Non-Submodularity: Towards Constant Approximation for Network Immunization,” arXiv:2410.19205 (2024). https://arxiv.org/abs/2410.19205
4. J. Li, L. Huang, D. Lee, and D. Y. Eun, “Controlling Epidemic Spread Under Immunization Delay Constraints” (2023). https://dyeun.wordpress.ncsu.edu/files/2023/05/ifip-networking23-final-ver.pdf
5. G. R. Brightwell and P. Winkler, “Submodular Percolation,” *SIAM Journal on Discrete Mathematics* 23 (2009), 1149–1178. https://doi.org/10.1137/07069078X
