# Exact consensus selection and a discontinuous weight threshold on weighted-median stars

## Finding
Consider the continuous-time weighted-median opinion dynamics on a bidirectional star with one hub and any finite number \(m\ge2\) of leaves. Each leaf puts all its influence weight on the hub. The hub puts arbitrary strictly positive weights \(w_1,\ldots,w_m\), summing to one, on the leaves and no weight on itself. Define \([L_0,U_0]\) to be the minimizing weighted-median interval of the initial leaf opinions, and let \(h_0\) be the initial hub opinion. **All opinions converge to the same exact limit**
\[
 z=\begin{cases}
 (h_0+L_0)/2,&h_0<L_0,\\
 h_0,&L_0\le h_0\le U_0,\\
 (h_0+U_0)/2,&h_0>U_0.
 \end{cases}
\]
This selection rule is valid for arbitrary leaf multiplicities, positive weights, and real starting opinions. Moreover, the limiting consensus is not generally continuous as a function of the influence weights, even when every entry corresponding to an existing edge stays strictly positive. In the two-leaf star with initial leaf opinions \(0,1\) and hub opinion \(2/5\), set the hub weights to \((w,1-w)\), \(0<w<1\). The exact final consensus is \(1/5\) for \(w>1/2\), \(2/5\) for \(w=1/2\), and \(7/10\) for \(w<1/2\). Thus both one-sided limits differ from each other and from the value at the exact tie.

## Assumptions and scope
The influence matrix has \(m+1\) agents: hub \(0\) and leaves \(1,\ldots,m\). Its nonzero entries are \(W_{0i}=w_i>0\) with \(\sum_i w_i=1\), and \(W_{i0}=1\) for each leaf; in particular \(W_{00}=0\). Agents obey the autonomous equation
\[
 \dot x_i(t)=\operatorname{Med}_i(x(t);W)-x_i(t).
\]
The operator chooses among the agents' current opinion values that satisfy the two weighted-median inequalities, breaking a nonunique-median tie by selecting the admissible value closest to the updating agent's own opinion. A zero-influence opinion, including the hub's own opinion, remains an eligible *candidate value* when it satisfies the inequalities; this is important at exact half-weight ties. At any time \(t\), the weighted-median interval \([L(t),U(t)]\) is the set of all real minimizers of \(\sum_i w_i|s-x_i(t)|\), considering only the leaf arguments and weights. Its endpoints are leaf opinions. All initial opinions may coincide, in which case the formula applies unchanged.

## Proof
First, every leaf satisfies \(\dot\ell_i=h-\ell_i\), with \(h=x_0\). Consequently
\[
 \ell_i(t)=e^{-t}\ell_i(0)+\int_0^t e^{-(t-s)}h(s)\,ds,
 \qquad \ell_i(t)-\ell_j(t)=e^{-t}\bigl(\ell_i(0)-\ell_j(0)\bigr).
\]
Hence every ordering and equality among leaf opinions persists. Weighted cumulative ranks are therefore unchanged, so the endpoints \(L(t),U(t)\) of their median interval follow two fixed initial leaf indices, or their shared values in case of ties. In particular, \(\dot L=h-L\) and \(\dot U=h-U\).

The hub's selected weighted median is the point of \([L,U]\) closest to \(h\). To see this directly, a candidate strictly below \(L\) or above \(U\) violates a median inequality; both endpoints are eligible leaf opinions. If \(h\in[L,U]\), the hub's current opinion itself is an eligible candidate because it is a value among the full collection of agents' opinions, notwithstanding its zero weight in the hub's influence row. It is then uniquely closest to itself. Thus the hub equation is exactly
\[
 \dot h=\operatorname{proj}_{[L,U]}(h)-h.
\]

If \(h_0\in[L_0,U_0]\), set \(h(t)=h_0\). Every leaf then has \(\ell_i(t)=h_0+(\ell_i(0)-h_0)e^{-t}\). It follows that \(L(t)\le h_0\le U(t)\) at every time, making this a valid global solution and yielding \(z=h_0\).

If \(h_0<L_0\), the proposed hub trajectory solves the linear pair \(\dot h=L-h\), \(\dot L=h-L\), namely
\[
 h(t)=\tfrac12(h_0+L_0)+\tfrac12(h_0-L_0)e^{-2t},\qquad
 L(t)=\tfrac12(h_0+L_0)-\tfrac12(h_0-L_0)e^{-2t}.
\]
The difference \(h(t)-L(t)=(h_0-L_0)e^{-2t}<0\) retains its sign for all finite \(t\), so the hub always selects the lower median endpoint. Every other leaf satisfies \(\ell_i(t)=L(t)+(\ell_i(0)-L_0)e^{-t}\). Thus all agents converge to \((h_0+L_0)/2\). The case \(h_0>U_0\) is identical with \(U\) in place of \(L\). These formulas also cover equality at the relevant endpoint by continuity. Existence and uniqueness of the weighted-median flow, also established in the primary source, confirm that the constructed trajectories are the model's solutions.

For the discontinuity, take \(m=2\), \(\ell_1(0)=0\), \(\ell_2(0)=1\), and \(h_0=2/5\). If \(w>1/2\), the median interval is \([0,0]\) and the first case gives \(z=(2/5+0)/2=1/5\). If \(w<1/2\), the interval is \([1,1]\) and the third case gives \(z=(2/5+1)/2=7/10\). Exactly at \(w=1/2\), it is \([0,1]\), so the second case gives \(z=2/5\). Every listed influence matrix is row-stochastic and has precisely the same positive-edge support. This proves the asserted two-sided weight sensitivity.

## Verification
The included standalone \(\texttt{verify.py}\) script reproduces the three exact rational consensus values for arbitrarily small positive rational perturbations of the half-weight tie. It also tests the closed-form trajectories for two- and multi-leaf stars against independently evaluated weighted-median differential equations using centered finite differences, and verifies their limiting values. Run with \(\texttt{python verify.py}\); no third-party packages are used. The analytic argument above, rather than this finite collection of tests, proves the arbitrary-size statement.

## Relationship to prior work
Han, Chen, Dörfler, and Mei introduced the continuous-time weighted-median dynamics in arXiv:2404.16318v1 (25 April 2024), establishing existence, equilibrium characterization, global convergence, and graph criteria for consensus. A revised manuscript by Han, Hendrickx, Chen, and Mei, arXiv:2404.16318v3, includes further pinning-control results. Those broad convergence results do not themselves specify the consensus value for every initial state on an arbitrarily weighted star, nor do they provide the above exact weight-tie discontinuity. The present statement specializes their model and adds a complete consensus-selection functional and a concrete weight-sensitivity boundary. The star specialization does not alter or contradict their global convergence theorem.

## Limitations
The exact formula requires all leaves to assign unit weight to the hub and the hub to assign no weight to itself. It is not asserted for generic influence matrices, nonautonomous weights, other tie-breaking conventions, or finite discrete-time updates. The sensitivity discontinuity concerns perturbations of influence weights, not perturbations of initial opinions at a fixed influence matrix. The comparison with broader literature is best-knowledge, not an exhaustive originality certificate. Independent external mathematical audit is not claimed.

## References
1. Y. Han, G. Chen, F. Dörfler, and W. Mei, *The Continuous-Time Weighted-Median Opinion Dynamics*, arXiv:2404.16318v1, first public 25 April 2024. https://arxiv.org/html/2404.16318v1
2. Y. Han, J. M. Hendrickx, G. Chen, and W. Mei, *Modeling, Analysis, and Control of Continuous-Time Weighted-Median Opinion Dynamics*, arXiv:2404.16318v3, 26 November 2025 (revised comparison, not used as first public date). https://arxiv.org/html/2404.16318v3
