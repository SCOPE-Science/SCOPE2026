# Sharp four-player welfare reversals from adding a competitive network link

## Finding

Consider a homogeneous, quadratic game of strategic substitutes played on a finite connected simple graph. Increasing the network's connectedness can **increase** the sum of players' equilibrium payoffs even though the total equilibrium action falls. This reversal is impossible on two or three vertices but possible on four. Moreover, all four-vertex edge additions admit an exact classification: the only welfare-increasing transitions are from a cycle to a diamond, or from a path to a paw, each above a sharp interaction threshold.

Let \(C_4\) be a four-cycle, \(P_4\) the four-vertex path, a *paw* a triangle with one pendant vertex, and a *diamond* the graph \(K_4\) with one edge removed. Define
\[
C(t)=12t^3-12t^2-3t+2,\qquad Q(t)=4t^6+t^5-4t^4+11t^3-8t^2-4t+2.
\]
Let \(\alpha\) be the unique zero of \(C\) in \((0,1/2)\), and \(\gamma\) the unique zero of \(Q\) in \((0,\sqrt2-1)\). Exact isolating intervals are \(349/1000<\alpha<350/1000\) and \(357/1000<\gamma<358/1000\). Within the strictly positive unique-equilibrium regime, the cycle-to-diamond welfare increase occurs exactly when \(\alpha<\beta<1/2\); the path-to-paw increase occurs exactly when \(\gamma<\beta<\sqrt2-1\). All other edge additions on connected graphs with at most four vertices strictly *decrease* total equilibrium payoff.

## Assumptions and scope

Fix \(n\in\{2,3,4\}\), a connected, undirected, unweighted simple graph \(G=(V,E)\) with \(n\) players, and a constant \(0<\beta<1/2\). Each player selects an action \(x_i\ge0\) and has payoff
\[
u_i(x)=x_i-\frac{x_i^2}{2}-\beta x_i\sum_{j:\,ij\in E}x_j.
\]
For a missing edge \(e\), compare the game on \(G\) with the game on \(G+e\) at the *same* \(\beta\). The theorem restricts the comparison to those \(\beta\) for which the equilibria on both graphs are strictly positive. Write \(W(G,\beta)=\sum_i u_i(x^*(G,\beta))\) for total Nash payoff and \(T(G,\beta)=\sum_i x_i^*(G,\beta)\) for aggregate action. No social-planner optimum, corner-equilibrium, or endogenous-link-formation interpretation is claimed.

## Proof

Let \(A\) denote the symmetric zero-diagonal adjacency matrix. The potential
\[
\Phi(x)={\bf 1}^{\mathsf T}x-\frac12 x^{\mathsf T}(I+\beta A)x
\]
has gradient components equal to the respective payoff derivatives. For every connected graph on at most four vertices, the smallest adjacency eigenvalue is at least \(-2\). This follows by checking the six connected four-vertex isomorphism types, together with the two- and three-vertex graphs; the accompanying program checks the exact principal-minor condition at \(I+A/2\). Consequently \(I+\beta A\) is positive definite whenever \(0<\beta<1/2\), because it is a positive combination of \(I\) and the positive-semidefinite matrix \(I+A/2\). Thus the potential is strictly concave on the nonnegative orthant and there is a unique Nash equilibrium. When the equilibrium is interior,
\[
x^*=(I+\beta A)^{-1}{\bf1}.
\]
At every such equilibrium the first-order condition \(1-x_i-\beta\sum_{j\sim i}x_j=0\) implies \(u_i(x^*)=x_i^2/2\), hence
\[
W(G,\beta)=\frac12\left\|(I+\beta A)^{-1}{\bf1}\right\|_2^2.
\]
This is *not* the potential's optimal value, which is \(T/2\); monotonicity of \(T\) need not imply monotonicity of \(W\).

There is no edge to add to the connected two-vertex graph. On three vertices, the only graph-to-graph addition is a path becoming a triangle, with
\[
\Delta W=-\frac{\beta(6\beta^3-4\beta^2-\beta+2)}{(1+2\beta)^2(2\beta^2-1)^2}<0,
\]
since the numerator's cubic parenthesis exceeds \(2-4(1/2)^2-1/2=1/2\) on the stated interval.

On four vertices, connected graphs have six isomorphism types: a star, a path, a paw, a four-cycle, a diamond, and the complete graph. Their nonisomorphic single-edge additions are exactly six. The list below gives the **complete** exact algebraic differences \(\Delta W=W(G+e,\beta)-W(G,\beta)\). For brevity, write
\[
H=\beta^3+3\beta^2-\beta-1,\quad P=\beta^2-\beta-1,\quad J=4\beta^2-\beta-1.
\]
All displayed denominators are strictly positive on their applicable interior domains.

| Addition | Difference in total Nash payoff |
|---|---|
| star to paw | \(\displaystyle \frac{\beta(\beta-1)R(\beta)}{(3\beta^2-1)^2H^2}\) |
| path to paw | \(\displaystyle -\frac{\beta Q(\beta)}{P^2H^2}\) |
| path to cycle | \(\displaystyle -\frac{\beta(2\beta^3+3\beta+2)}{(1+2\beta)^2P^2}\) |
| paw to diamond | \(\displaystyle -\frac{\beta S(\beta)}{J^2H^2}\) |
| cycle to diamond | \(\displaystyle -\frac{\beta C(\beta)}{(1+2\beta)^2J^2}\) |
| diamond to complete graph | \(\displaystyle -\frac{\beta(13\beta^3-8\beta^2+\beta+2)}{(1+3\beta)^2J^2}\) |

Here the remaining polynomials are
\[
R(t)=3t^6-9t^5-14t^4+16t^3-3t^2-3t+2,\qquad
S(t)=11t^7-8t^5-14t^4+25t^3-8t^2-4t+2.
\]
The star has a strictly positive equilibrium only for \(\beta<1/3\). The paw has a strictly positive equilibrium only for \(\beta<\sqrt2-1\). All remaining four-vertex types have positive equilibria throughout \(0<\beta<1/2\). Therefore, admissible star-to-paw comparisons have \(0<\beta<1/3\), and path-to-paw and paw-to-diamond comparisons have \(0<\beta<\sqrt2-1\).

Every Bernstein coefficient of the degree-six polynomial \(R(t)\), rescaled to \(0\le t\le1/3\), is strictly positive. Listed in increasing Bernstein index they are
\[
2,\ \frac{11}{6},\ \frac{74}{45},\ \frac{79}{54},\ \frac{1588}{1215},\ \frac{286}{243},\ \frac{256}{243}.
\]
Similarly, every Bernstein coefficient of degree-seven \(S(t)\) rescaled to \(0\le t\le5/12\) is positive:
\[
2,\ \frac{37}{21},\ \frac{551}{378},\ \frac{13777}{12096},\ \frac{61357}{72576},\ \frac{48971}{81648},\ \frac{87791}{217728},\ \frac{9116911}{35831808}.
\]
Since \(\sqrt2-1<5/12\), these certificates settle the star-to-paw and paw-to-diamond signs. The remaining always-negative cases follow from positivity of their elementary factors; in particular \(13t^3-8t^2+t+2>2-8(1/2)^2=0\).

The derivative \(C'(t)=36t^2-24t-3\) is negative on \((0,1/2)\). The derivative of \(Q\) is
\[
Q'(t)=t^3(24t^2+5t-16)+t(33t-16)-4<0
\]
on \((0,\sqrt2-1)\); each parenthesized expression there is negative. The polynomials start positive, become negative at their respective upper endpoints, and have the rational isolating intervals stated above. This proves the two claimed necessary-and-sufficient thresholds and excludes any other four-player reversal in the specified regime.

For a particularly simple exact witness, set \(\beta=3/8\). On \(C_4\), each player chooses \(4/7\). After adding a diagonal the two degree-three players choose \(4/13\) and the two degree-two players choose \(10/13\). Consequently
\[
\begin{aligned}
T(C_4,3/8)&=16/7,&T(\mathrm{diamond},3/8)&=28/13,\\
W(C_4,3/8)&=32/49,&W(\mathrm{diamond},3/8)&=116/169.
\end{aligned}
\]
Thus the action difference is \(-12/91\), whereas the payoff difference is \(+276/8281\). Both are exact, not floating-point estimates.

## Verification

The standalone file `verify.py` reconstructs the adjacency matrices of every connected graph of orders two through four using NetworkX's built-in graph atlas; it proves the requisite positive-semidefinite conditions exactly, symbolically recomputes every unique graph-edge class difference using SymPy, verifies the two positive Bernstein certificates, isolates both roots by exact endpoint evaluations and derivative decompositions, and checks the explicit four-cycle witness in rational arithmetic. Run `python verify.py` with compatible Python, SymPy and NetworkX installations. This code is auxiliary evidence; the algebraic proof and listed finite sign certificates above establish the result without numerical extrapolation.

## Relationship to prior work

Bramoullé, Kranton and D'Amours introduce the precise strategic-substitutes quadratic payoff model and its potential-game analysis. Their working-paper Proposition 5 shows that adding links decreases *aggregate activity* (equivalently the maximal potential in this normalization), not that it decreases the sum of individual equilibrium utilities. The witness above exhibits the distinction directly and the classification resolves its smallest-graph boundary.

Ballester, Calvó-Armengol and Zenou analyze Bonacich centrality and key players in linear-quadratic network games, notably with local complementarity and global substitutability. Their key-player removal results do not imply the present one-edge strategic-substitutes total-utility thresholds. Chadha and Kulkarni study equilibrium welfare in the related but different positive-spillover local-public-goods model, with global graph-statistic bounds rather than these payoff sums for negative cross-term utility. The precise four-player polynomial cutoffs and six transition classes were not located in the compared sources; this limited literature comparison does not prove universal novelty.

## Limitations

Only connected finite simple graphs of orders at most four, homogeneous payoff coefficients, and \(0<\beta<1/2\) with strictly positive unique equilibria at both endpoints are classified. The result says nothing about arbitrary larger networks, zero-action equilibria, heterogeneity, stable link-formation incentives, player-optimal transfers, or socially optimal activity. The increase in payoff is small for the exhibited parameters; its value is the exact qualitative reversal and sharp boundary, not an asserted empirical magnitude. Although relevant literature and mathematical implication were checked, unindexed equivalent results may exist.

## References

1. Y. Bramoullé, R. Kranton, M. D'Amours, *Strategic Interaction and Networks*. CIRPÉE Working Paper 10-18, first publicly posted 21 May 2010, DOI 10.2139/ssrn.1612369. Author-hosted January 2011 manuscript: https://sites.duke.edu/rachelkranton/files/2016/09/strategicinteractionandnetworksjan2011final.pdf . AER 104 (2014), 898–930, DOI 10.1257/aer.104.3.898.
2. C. Ballester, A. Calvó-Armengol, Y. Zenou, *Who's Who in Networks. Wanted: The Key Player*. Econometrica 74 (2006), 1403–1417, DOI 10.1111/j.1468-0262.2006.00709.x.
3. K. N. Chadha, A. A. Kulkarni, *Aggregate Play and Welfare in Strategic Interactions on Networks*. arXiv:1906.07630 (first version 2019), https://arxiv.org/pdf/1906.07630 .
