# Two-leader coherence transitions in weighted clique windmills

## Finding
For every integer \(r,s\ge2\) and every real \(b>0\), consider the network \(G_{r,s}(b)=K_1\vee(rK_s)\) with unit conductance from the hub to every outer vertex and conductance \(b\) inside each outer clique. For any distinct leaders \(u,v\), put \(S=\{u,v\}\) and let \(L_{FF}\) be the principal weighted Laplacian on the remaining followers \(F=V\setminus S\). Set \(J(S)=\operatorname{tr}(L_{FF}^{-1})\). Define
\[A=\frac{(rs-1)(1+2b)+s(r-1)b^2}{(1+b)(1+sb)},\qquad \Delta=\frac{rs-3+b[s(r-4)+1]}{2(1+sb)}.\]
The exact global optimum is \(\min_{|S|=2}J(S)=A+\min\{0,\Delta\}\). When \(\Delta>0\), precisely the \(rs\) sets consisting of the hub and one outer vertex minimize \(J\). When \(\Delta<0\), precisely the \(\binom r2s^2\) pairs of outer vertices in different cliques minimize it. At \(\Delta=0\), all these and only these two classes tie. Pairs in one clique are never optimal.

The classification has three sharp regimes: for \(r\ge4\), always \(\Delta>0\). For \(r=3\), \(\Delta\) changes sign at \(b=3\), independently of \(s\). For \(r=2\), it changes sign at \(b=(2s-3)/(2s-1)\). In the latter two cases hub-peripheral pairs win below the threshold and cross-clique peripheral pairs win above it.

## Assumptions and scope
There are \(r\) mutually disjoint petals, each a complete graph on \(s\) vertices. Exactly one additional vertex (the hub) has a unit-conductance edge to each peripheral vertex. There are no edges between distinct petals. Every internal petal edge has conductance \(b>0\). The weighted Laplacian is \(L_{ii}=\sum_{j\ne i}c_{ij}\), \(L_{ij}=-c_{ij}\). Leaders are two distinct, noiseless, pinned vertices. The quantity \(J\) omits the conventional global factor \(1/2\) for stochastic coherence. Because \(G_{r,s}(b)\) is connected, every proper grounded Laplacian \(L_{FF}\) is positive definite. No result is asserted for noisy leaders, heterogeneous edge weights or three or more leaders.

## Proof
**Grounding identity.** For a connected resistive graph with effective resistance \(R_{xy}\), and three distinct vertices \(x,u,v\), the resistance from \(x\) to the pair obtained by identifying/grounding \(u,v\) is
\[\Phi(R_{xu},R_{xv},R_{uv})=\frac{R_{xu}+R_{xv}}2-\frac{R_{uv}}4-\frac{(R_{xu}-R_{xv})^2}{4R_{uv}}.\]
This is the diagonal entry \((L_{FF}^{-1})_{xx}\). To prove the identity, perform Kron reduction onto \(\{x,u,v\}\). The resulting three-node network is uniquely determined by its three pairwise effective resistances; alternatively, represent the unit electrical flow from \(x\) as a convex combination of unit flows to \(u\) and \(v\), then minimize its energy over the current split. Polarization gives \(\langle f_{xu},f_{xv}\rangle=(R_{xu}+R_{xv}-R_{uv})/2\); energy minimization yields the displayed formula. If \(x\) is itself a leader, its contribution is zero.

**Resistance reduction.** Each petal together with the hub is a weighted complete graph on \(s+1\) vertices with hub-to-peripheral conductance \(1\) and within-petal conductance \(b\). Spectral decomposition on the constant and zero-sum peripheral subspaces gives the hub-to-peripheral resistance \(\alpha=(1+b)/(1+sb)\) and same-petal peripheral-to-peripheral resistance \(\beta=2/(1+sb)\). Two peripherals in different petals have resistance \(2\alpha\), because the hub is an articulation point. These exhaust all resistance types.

**Exhaustive orbit computation.** The automorphisms of the weighted network partition unordered leader pairs into three classes. Let \(A\) be the cost for a hub and a peripheral vertex, \(B\) for two peripherals in the same petal, and \(C\) for two peripherals in different petals. Summing the grounding identity over all followers gives
\[\begin{aligned}
A&=(s-1)\Phi(\alpha,\beta,\alpha)+(r-1)s\Phi(\alpha,2\alpha,\alpha),\\
B&=(s-2)\Phi(\beta,\beta,\beta)+\Phi(\alpha,\alpha,\beta)+(r-1)s\Phi(2\alpha,2\alpha,\beta),\\
C&=\Phi(\alpha,\alpha,2\alpha)+2(s-1)\Phi(\beta,2\alpha,2\alpha)+(r-2)s\Phi(2\alpha,2\alpha,2\alpha).
\end{aligned}\]
Straight expansion and cancellation, valid for the stated entire parameter domain, yields
\[A=\frac{(rs-1)(1+2b)+s(r-1)b^2}{(1+b)(1+sb)},\]
\[C-A=\frac{rs-3+b[s(r-4)+1]}{2(1+sb)}=\Delta,\]
\[B-C=\frac{b[brs+2bs+b+rs+3]}{2(1+b)(1+sb)}>0.\]
Thus \(B\) cannot minimize regardless of the sign of \(C-A\). Since every unordered pair is in exactly one class, the exact global optimum is \(\min(A,C)=A+\min(0,\Delta)\). This proves exhaustive global optimality without a relaxation, heuristic or finite-size hypothesis.

**Boundary and equality analysis.** All denominators above are positive. If \(r\ge4\), the numerator of \(\Delta\) is positive because \(rs-3>0\) and \(s(r-4)+1\ge1\). If \(r=3\), then \(\Delta=(s-1)(3-b)/(2(1+sb))\). If \(r=2\), then \(\Delta=[2s-3-(2s-1)b]/[2(1+sb)]\) with positive critical ratio \((2s-3)/(2s-1)\). The strict inequality \(B>C\) eliminates same-petal ties. The orbit cardinalities are exactly \(rs\) for hub-peripheral and \(\binom r2s^2\) for cross-petal peripheral pairs. All asserted minimizers and no others follow.

## Verification
Run `python verify_windmill.py` with the version-compatible SymPy in `requirements.txt`. The independent matrix construction checks exact rational inverse traces of the grounded Laplacians against all three symbolic orbit formulas and enumerates all two-leader pairs on selected small graphs. The exact symbolic identities \(A=A_0\), \(C-A=\Delta\), and \(B-C\) are checked for indeterminate \(r,s,b\). Finite enumeration only tests implementations; the argument above proves the result for all admissible parameters. Recorded output is included in `verification_output.txt`.

## Relationship to prior work
Fitch and Leonard (2014), *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, derive general graph-based criteria and explicit path/cycle leader placements. Patterson, Yi and Zhang (2017), *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873, derive resistance grounding methods and characterize several graphs including paths, cycles and selected trees. Those general formulas can be applied to this graph, but neither examined text states the present all-parameter weighted windmill transition. Earlier work on the **unit-conductance windmill with finite-gain noisy leaders** already covers the unit-weight limiting leader type; no separate novelty is attributed to \(b=1\). Sun, Li and Liu (2020), *Noisy consensus dynamics in windmill-type graphs*, DOI 10.1063/5.0020696, studies windmill leader-follower coherence with freely assigned leaders and is especially close: the available abstract does not establish this variable-conductance two-leader phase classification, but its full text could not be accessed and therefore is a substantive residual originality risk.

## Limitations
This is a self-contained algebraic proof with self-review, **not** an independently validated or peer-reviewed novelty assertion. Originality could change if the inaccessible 2020 full text or other specialist literature proves a stronger weighted theorem. The classical factor \(1/2\) in stationary coherence does not change optimal placements but halves all displayed \(J\) values. The problem is not the finite-gain leader model and the result does not generalize automatically to heterogeneous conductances.

## References
1. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, first arXiv version 2014-07-07, https://arxiv.org/abs/1407.1569.
2. S. Patterson, Y. Yi and Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, first arXiv version 2017-08-23, https://arxiv.org/abs/1708.06873.
3. W. Sun, Y. Li and S. Liu, *Noisy consensus dynamics in windmill-type graphs*, Chaos 30 (2020) 123131, https://doi.org/10.1063/5.0020696. Only its public abstract was examined; the article full text was unavailable.
