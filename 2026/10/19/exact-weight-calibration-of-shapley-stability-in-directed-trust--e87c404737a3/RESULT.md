# Exact weight calibration of Shapley stability in directed trust games

## Finding

For the directed trust game of Bandhana, Kroupa and García, analyzed by Ryzák and Kroupa, a complete inverse-design criterion determines when the Shapley allocation coincides with the unique stable core allocation if each recipient has one common positive incoming-edge weight.

Let \(G=(V,E)\) be a finite, loopless, strongly connected directed graph with \(n=|V|\ge2\), adjacency matrix \(A\) defined by \(A_{ij}=1\) precisely when \(i\to j\), and indegrees \(d_j=\sum_i A_{ij}\ge1\). Give every edge entering vertex \(j\) the same recipient-dependent weight \(w_j\in(0,1]\). Write \(\phi\) for the Shapley value, \(c\) for the unique core allocation, and
\[
 f(d)=\frac{d-1}{2(d+1)},\qquad
 D=\operatorname{diag}(d_1,\ldots,d_n),\qquad
 Q=AD^{-1}.
\]
The matrix \(Q\) is column-stochastic and irreducible. Its unique normalized positive stationary vector is \(\pi\), so \(Q\pi=\pi\), \(\sum_i\pi_i=1\). The exact deviation identity is
\[
 \phi_i-c_i=\sum_{j:i\to j}w_jf(d_j)-d_iw_if(d_i),
 \qquad c_i=d_iw_i.
\]
Thus **exactly one of the following three possibilities holds**.

1. If every \(d_i=1\), then \(\phi=c\) for every choice of positive recipient weights.
2. If some \(d_i=1\) and some \(d_j\ge2\), then \(\phi\ne c\) for every choice of positive recipient weights.
3. If every \(d_i\ge2\), then \(\phi=c\) holds **if and only if** for one common \(\kappa>0\),
\[
 \boxed{\quad w_i=\frac{\kappa\pi_i}{d_if(d_i)}\quad(i\in V).\quad}
\]
The scaling \(\kappa\) may always be chosen so that \(0<w_i\le1\). Hence the positive trust-weight ratios achieving stability and fairness are unique.

An additional exact rigidity result follows for any finite simple undirected graph represented by reciprocal arcs carrying one common weight \(a\in(0,1]\). Its Shapley allocation lies in the core **if and only if every connected component is regular**. On a connected irregular component a specific coalition of all vertices except a suitable minimum-degree vertex blocks the Shapley allocation. Explicitly, with \(g_i=f(d_i)\),
\[
 \phi_i-c_i=a\sum_{j\sim i}(g_j-g_i),\qquad
 \sum_i g_i(\phi_i-c_i)=-a\sum_{\{i,j\}\in E_{\rm und}}(g_i-g_j)^2.
\]
This Dirichlet-energy certificate is strictly negative whenever some component is irregular.

## Assumptions and scope

For a coalition \(S\subseteq V\), the trust-game worth is
\[
 v(S)=\sum_{\substack{i,j\in S\\i\to j}}w_j
 +\sum_{j\in S:\,\exists\,i\notin S,\,i\to j}
    \min_{\substack{i\notin S\\ i\to j}}w_j.
\]
The minimum over an empty set contributes zero by convention. In the recipient-dependent model the second sum simplifies to \(\sum_{j\in S:\,\exists i\notin S,\,i\to j}w_j\). Each arc is oriented, including both orientations of an undirected edge when applicable. Self-loops are excluded; weights are strictly positive and at most one, as required by the motivating trust-game model. Strong connectivity is imposed only in the inverse-calibration trichotomy; the reciprocal-graph corollary permits disconnected undirected graphs and isolated vertices. The conclusions concern exact transferable-utility allocations, not strategic incentives for agents to report weights truthfully.

The core is the collection of efficient vectors \(x\) with \(\sum_{i\in S}x_i\ge v(S)\) for every coalition \(S\). The Shapley value is the average incremental contribution over all \(n!\) orders of player arrival.

## Proof

**1. A direct core calculation.** For each \(i\), put \(c_i=d_iw_i\). At the grand coalition, \(\sum_i c_i=v(V)\). For any \(S\), summing incoming weights over vertices in \(S\) counts all internal arcs plus all arcs from its complement. At each \(j\in S\), the latter sum dominates the minimum incoming weight from outside \(S\), proving \(\sum_{j\in S}c_j\ge v(S)\). Thus \(c\) is in the core. Also,
\[
 v(V\setminus\{i\})=v(V)-d_iw_i:
\]
removing \(i\) deletes the incoming arcs to \(i\), while each outgoing arc \(i\to j\) is replaced by the outside-minimum term at \(j\). Any core vector \(x\) therefore satisfies \(x_i\le d_iw_i=c_i\); efficiency and \(\sum_i c_i=v(V)\) force \(x=c\). The core is exactly \(\{c\}\).

**2. The Shapley contributions of one recipient.** Decompose \(v=\sum_jv_j\), where \(v_j(S)=0\) if \(j\notin S\), and otherwise
\[
 v_j(S)=w_j\bigl(k_j(S)+\mathbf1_{\{k_j(S)<d_j\}}\bigr),
 \quad k_j(S)=\#\{i\in S:i\to j\}.
\]
Consider a uniformly random arrival ordering. The number \(k\) of incoming neighbors preceding \(j\) is uniform on \(\{0,1,\ldots,d_j\}\). Before \(j\) arrives the component \(v_j\) is zero; its marginal contribution at arrival is \(w_j(k+\mathbf1_{\{k<d_j\}})\). Its expected contribution is therefore
\[
 \phi_j(v_j)=w_j\left(\frac{d_j}{2}+\frac{d_j}{d_j+1}\right)
 =d_jw_j(1-f(d_j)).
\]
All \(d_j\) incoming neighbors are exchangeable for \(v_j\). By Shapley efficiency and \(v_j(V)=d_jw_j\), each such neighbor receives exactly \(w_jf(d_j)\). All others receive zero. Summing over recipients proves the displayed deviation identity, including the \(d_j=1\) case with \(f(1)=0\).

**3. A stationary-distribution equation.** Let \(h_i=d_iw_if(d_i)\). Because \(d_i\ge1\), the vector identity is
\[
 \phi-c=(AD^{-1}-I)h=(Q-I)h.
\]
Column \(j\) of \(Q\) sums to one because \(\sum_iA_{ij}=d_j\). Reversing every arc preserves strong connectivity, so \(Q\) is irreducible. By the finite irreducible Markov-chain stationary-vector theorem, its nonnegative fixed vectors are exactly the nonnegative multiples of the strictly positive \(\pi\). If all indegrees equal one, \(f(d_i)=0\) and \(h=0\); balance holds for every \(w\). If some degree equals one and another exceeds one, positivity of all weights makes \(h\) nonzero with a zero coordinate; it cannot be a fixed vector. If all degrees exceed one, \(h\) is strictly positive and balance holds precisely when \(h=\kappa\pi\). Solving \(d_iw_if(d_i)=\kappa\pi_i\) gives the unique projective formula. Scaling \(\kappa\) down enforces all \(w_i\le1\) without changing the equality.

**4. Reciprocal graphs, regularity and explicit blocking.** If both orientations of each undirected edge have weight \(a\), the identity in step 2 becomes \(\phi_i-c_i=a\sum_{j\sim i}(f(d_j)-f(d_i))\) on all non-isolated vertices, with zero deviation at isolated vertices. Pairing terms across undirected edges gives the exact Dirichlet identity in the Finding section. Since \(f(d)=1/2-1/(d+1)\) is strictly increasing for integer \(d\ge1\), vanishing of the energy forces equal degrees along every edge, hence regularity of every connected component. Conversely componentwise regularity makes every deviation zero. For a connected irregular component, take a minimum-degree vertex \(i\) incident to some higher-degree vertex; all neighboring degrees are at least \(d_i\), so \(\phi_i-c_i>0\). For the complementary coalition \(S=V\setminus\{i\}\),
\[
 v(S)-\sum_{j\in S}\phi_j=\phi_i-c_i>0,
\]
so the Shapley value is blocked. The same construction works with isolated components by taking \(i\) on an irregular component.

## Verification

The standalone standard-library program `verify.py` independently evaluates the trust-game characteristic function for every coalition and computes its Shapley value from the factorial-weighted definition, rather than calling the derived formula. It compared direct values to the theorem for all 771 connected labeled simple undirected graphs on two through five vertices, verified the regularity criterion, and checked exact rational strongly connected directed examples. A four-node irregular digraph made from a bidirected four-cycle plus \(0\to2\) has indegrees \((2,2,3,2)\), stationary vector \((4,3,3,3)/13\), and balancing target weights \((1,3/4,1/3,3/4)\); its direct Shapley allocation equals \((2,3/2,1,3/2)\), the unique core vector. On the three-vertex undirected path with common unit weight, the direct Shapley vector is \((7/6,5/3,7/6)\) while the core is \((1,2,1)\). The exact computations support but do not replace the proof for arbitrary network size.

Run `python3 verify.py` with Python 3.9 or later. No nonstandard packages are required.

## Relationship to prior work

Bandhana, Kroupa and García (2024) introduced this coalition-value construction and established existence of a core allocation and its use as a trust score. Ryzák and Kroupa (2026, arXiv:2605.18157v1) established the singleton core and general polynomial-time formulas for Shapley and Banzhaf allocations on arbitrary weighted directed graphs. Those results, the definition of the game, and classical irreducible-chain Perron theory are pre-existing and not claimed here as new.

The present claim is an **inverse classification**: it asks whether *there exist positive recipient-constant weights* that cause fairness and stability to agree, and if so classifies **all** such weight vectors by a canonical reverse-walk stationary measure. It also proves a sharp obstruction from mixed indegree-one vertices and a componentwise-regularity criterion plus an explicit blocking/energy certificate for uniform reciprocal networks. Neither source's main claims state this global feasibility, uniqueness, obstruction, or graph-rigidity classification. Their forward formulas are used as relevant broader prior information; no independent historical-priority audit has been performed.

## Limitations

The calibration trichotomy requires a strongly connected simple digraph and equal positive weights on all edges entering a given recipient. It does not characterize arbitrary edge-specific weights, non-strongly connected digraphs, or nonpositive weights. The undirected graph corollary with a common weight concerns a narrower reciprocal subclass; it does not say every irregular topology is impossible to calibrate when asymmetric, recipient-dependent weights are allowed. The finite checks do not certify infinitely many cases. Broader historical literature could contain a similar inverse-allocation characterization; novelty has only been examined against the identified sources and available mathematical records.

## References

1. D. Ryzák and T. Kroupa, *A Tractable Class of Cooperative Games Defined by Directed Networks: Unanimity Decomposition and Shapley Value*, arXiv:2605.18157v1 (first public 2026-05-18), particularly Sections 2, 3 and 5. https://arxiv.org/abs/2605.18157
2. A. Bandhana, T. Kroupa and S. García, *Trust in Shapley: A Cooperative Quest for Global Trust in P2P Network*, AAMAS 2024, pp. 132–140, particularly Sections 3 and 3.1. https://aamas.csc.liv.ac.uk/Proceedings/aamas2024/pdfs/p132.pdf
3. A. Khmelnitskaya, O. Selcuk and D. Talman, *The Shapley value for directed graph games*, Operations Research Letters 44 (2016), 143–147. Its underlying graph-constrained cooperative solution concept differs from the minimum-external-incoming-weight trust game. https://doi.org/10.1016/j.orl.2015.12.009
