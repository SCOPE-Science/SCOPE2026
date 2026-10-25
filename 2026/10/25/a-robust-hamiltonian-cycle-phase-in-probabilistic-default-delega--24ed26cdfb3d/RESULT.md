# A robust Hamiltonian-cycle phase in probabilistic default delegation

## Finding

**Theorem (robust complete-cycle equilibria and their three-voter boundary).** Consider the default-delegation game defined below with any integer \(n\ge 2\), independently voting agents having probabilities \(0<p_i<1\), a common strictly positive tolerance \(\tau\), and positions \(x_i\in[0,1]\). Set
\[
q_i=1-p_i,\qquad p_{\min}=\min_i p_i,\qquad q_{\max}=\max_i q_i,\qquad Q=\prod_{i=1}^{n}q_i,\qquad \Delta=\max_i x_i-\min_i x_i.
\]
If
\[
\boxed{\Delta<\frac{\tau p_{\min}Q}{q_{\max}^{2}},}
\]
then **all and only** directed Hamiltonian cycles are pure Nash equilibria. There are exactly \((n-1)!\) such delegation profiles, regardless of the heterogeneity of the probabilities \(p_i\). The condition is a sufficient robustness bound, not a claimed optimal bound.

This structural conclusion fails if close ideological proximity is replaced merely by mutual acceptability. In the three-voter family with \(x=(0,a,b)\), \(0<a<b<1\), \(p_i=1/2\), \(\tau=1\), and the nonspanning delegation profile \(d=(2,1,2)\), the profile is a Nash equilibrium **if and only if**
\[
\boxed{b\ge\max\left\{2a,\frac{1+a}{2}\right\}.}
\]
The nonspanning equilibrium already occurs, for example, at \(a=1/10\), \(b=9/10\). Two voters cannot produce such a nonspanning equilibrium when both mutually accept one another and have nondegenerate participation probabilities; thus three is the smallest possible electorate for the phenomenon under common tolerance and complete mutual acceptance.

## Assumptions and scope

Every voter \(i\in\{1,\ldots,n\}\) names one default delegate \(d(i)\in\{1,\ldots,n\}\), including possibly themselves. All delegation choices are permitted (complete awareness). Voter \(i\) casts a ballot independently with probability \(p_i\in(0,1)\); when they do not cast, their ballot follows the default-delegation arrows until reaching the first casting voter or closing a directed cycle. A successful representation of voter \(i\) by casting voter \(j\) gives utility \(\tau-|x_i-x_j|\); an unrepresented ballot has utility zero. Voters maximize expected utility by unilateral delegation changes. Self-delegation is allowed. Positions may be taken distinct (as in the original model's general-position convention), and the strict robustness inequality automatically implies \(\Delta<\tau\), hence strict mutual acceptance.

For profile \(d\), let \(v_0=i,v_1,\ldots,v_{L-1}\) be the successive distinct vertices encountered by following delegation from \(i\), ending just before the first repeated vertex. Write \(S_i(d)=\{v_0,\ldots,v_{L-1}\}\). The expected utility is exactly
\[
U_i(d)=\sum_{t=0}^{L-1}\left(\prod_{h<t}q_{v_h}\right)p_{v_t}(\tau-|x_i-x_{v_t}|).
\]
The products are empty products equal to one. There is no external randomness besides the independent ballot-casting indicators.

## Proof

**1. A position-free core and a uniform error estimate.** For any nonempty set \(S\), put \(Q_S=\prod_{j\in S}q_j\). The probability that some vertex on the successive distinct delegation path casts is \(1-Q_{S_i(d)}\). Thus
\[
U_i(d)=\tau(1-Q_{S_i(d)})-D_i(d),
\]
where \(D_i(d)\) is the nonnegative expected distance penalty. Since each distance is at most \(\Delta\), and the penalty at \(v_0=i\) is zero,
\[
0\le D_i(d)\le \Delta(1-p_i)\le\Delta q_{\max}.
\]
Consequently any unilateral payoff difference deviates from its position-free version by at most \(\Delta q_{\max}\). For every proper subset \(S\subsetneq\{1,\ldots,n\}\), its omitted vertices have abstention product at most \(q_{\max}\), because each \(q_i<1\). Therefore
\[
Q_S\ge \frac{Q}{q_{\max}}.
\]
If one adds at least one previously unvisited vertex to a path, without dropping existing vertices, the position-free utility gain is at least \(\tau p_{\min}Q/q_{\max}\). The same bound follows if a path consisting of a cycle \(C\) is changed to visit its starting vertex \(i\) followed by a different cycle \(T\) with \(Q_C\ge Q_T\): the gain is
\[
\tau(Q_C-q_iQ_T)\ge\tau p_i Q_T\ge\frac{\tau p_{\min}Q}{q_{\max}}.
\]

**2. Every Hamiltonian cycle is stable.** Fix a directed Hamiltonian cycle. From any voter \(i\), its original delegation walk encounters all \(n\) voters. Keeping the same delegate changes nothing; changing \(i\)'s arrow to any other vertex closes a cycle strictly before all voters have been encountered. For the new proper path set \(S\) and its nonempty complement \(R\), the original minus new position-free payoff is
\[
\tau(Q_S-Q)=\tau Q_S(1-Q_R)\ge\frac{\tau p_{\min}Q}{q_{\max}}.
\]
The assumed bound on \(\Delta\) makes this strictly larger than \(\Delta q_{\max}\). Hence every Hamiltonian cycle is a strict Nash equilibrium.

**3. Every non-Hamiltonian profile has a profitable deviation.** A finite directed graph in which every vertex has exactly one outgoing arrow consists of disjoint weak components, each with one directed cycle and directed in-trees feeding into it. Suppose there are at least two distinct directed cycles. Choose a cycle \(C\) of maximal abstention product \(Q_C\), and another cycle \(T\) with \(Q_T\le Q_C\). A voter \(i\) on \(C\) redirects to any vertex of \(T\). Their old path contains exactly \(C\); their new path contains \(i\) followed by the entirety of \(T\). The position-free gain is bounded below as in step 1.

Otherwise there is exactly one cycle \(C\). Because the profile is not Hamiltonian, at least one voter lies in a tree feeding into \(C\). Choose such a vertex \(t\); its original path first reaches the cycle at vertex \(c\). Let \(i\) be the immediate predecessor of \(c\) along the cycle, including \(i=c\) when \(C\) is a self-loop. Redirect \(i\) to \(t\). The new path from \(i\) visits all of \(C\) as before and at least one additional tree vertex. Again the position-free gain is at least \(\tau p_{\min}Q/q_{\max}\). In both cases it exceeds the maximum possible change in distance penalty, \(\Delta q_{\max}\), so this deviation is profitable. Hence no non-Hamiltonian profile is a Nash equilibrium. The number of directed Hamiltonian cycles on labeled voters is \((n-1)!\).

**4. Exact three-voter crossover.** Let \(p_i=1/2\), \(\tau=1\), \(x=(0,a,b)\), \(0<a<b<1\), and \(d=(2,1,2)\). Voter 1's current utility is \(3/4-a/4\); changing their delegate to voter 3 gives \(7/8-b/4-a/8\). This deviation is not profitable precisely when \(2b\ge 1+a\). Voter 2's current utility is \(3/4-a/4\); changing to voter 3 gives \(3/4-(b-a)/4\), so this deviation is not profitable precisely when \(b\ge2a\). Self-delegation is inferior for both voters because \(a<1\).

Voter 3 currently receives \(7/8+a/4-3b/8\). Delegating instead to voter 1 gives \(7/8+a/8-3b/8\), strictly less because \(a>0\); self-delegation gives \(1/2\), strictly less because \(b<1\). Thus the two stated inequalities are jointly necessary and sufficient. At two voters, if their distance is strictly below their common tolerance and both participation probabilities are in \((0,1)\), any self-delegating voter improves by pointing to the other voter. The unique Nash equilibrium is their mutual two-cycle. This proves minimality.

## Verification

The standalone `verify.py` uses standard-library rational arithmetic. It compares the displayed expected-utility formula against direct enumeration of casting outcomes for every delegation profile on two through four voters, exhaustively checks all profiles on two through five voters in several heterogeneous small-diameter instances, and tests the three-voter boundary at rational grid points and exact equality cases. It reports 8,027 successful exact assertions. In the small-diameter tests, all and only the predicted \((n-1)!\) Hamiltonian cycles survive unilateral-deviation checks. The general proof above, not finite enumeration, establishes the infinite family of claims.

Run `python3 verify.py` from the directory containing this file. No third-party dependencies or network access are required.

## Relationship to prior work

Brill et al. (COMSOC 2025 manuscript and arXiv:2607.12610, §§2–4 and Appendix B) introduced the stochastic default-delegation utility and established that nontrivial components of certain equilibria contain cycles. Their Theorems 5 and 8 give componentwise structure, not a complete spanning-cycle characterization, exact equilibrium count, or a quantitative diameter regime with arbitrary heterogeneous voting probabilities. Their Theorem 14 constructs an optimal delegation path for a *single* voter and does not establish the simultaneous Nash property or exclusion of all non-Hamiltonian profiles. Their three-voter mutual-acceptance existence theorem does not give the displayed exact nonspanning-cycle boundary.

Escoffier, Gilbert, and Pass-Lanneau (2018/2019) analyze strategic delegation under different, nonprobabilistic representation semantics. Markakis and Papasotiropoulos (2023/2024) analyze temporal resolution of delegation paths. Neither framework directly entails the stochastic default-delegation equilibrium characterization here. Standard functional-graph decomposition and finite-product inequalities are used as known tools, not claimed as inventions.

## Limitations

The diameter bound is sufficient and can be conservative; no claim of sharpness is made for the general \(n\)-voter bound. The classification assumes unrestricted candidate delegates, common strictly positive tolerance, independent nondegenerate turnout, and one-dimensional positions. It makes no claim about restricted awareness graphs, correlated turnout, differing tolerances, mixed strategies, or learning dynamics. The exact three-voter criterion applies to one specified non-Hamiltonian profile and the stated one-parameter family; it is not a classification of all three-voter Nash equilibria. Mathematical correctness was checked analytically and by exact arithmetic, but independent scientific validation and absolute historical-priority certification have not been performed.

## References

- Markus Brill, Rachael Colley, Anne-Marie George, Grzegorz Lisowski, Georgios Papasotiropoulos, and Ulrike Schmidt-Kraepelin, *Cycles in Liquid Democracy: A Game-Theoretic Justification*, COMSOC 2025 manuscript, https://www.ac.tuwien.ac.at/comsoc2025/comsoc2025-papers/49.pdf; expanded version, arXiv:2607.12610, https://arxiv.org/html/2607.12610.
- Bruno Escoffier, Hugo Gilbert, and Adèle Pass-Lanneau, *The Convergence of Iterative Delegations in Liquid Democracy in a Social Network*, arXiv:1904.05775, https://arxiv.org/abs/1904.05775.
- Evangelos Markakis and Georgios Papasotiropoulos, *As Time Goes By: Adding a Temporal Dimension Towards Resolving Delegations in Liquid Democracy*, arXiv:2307.12898, https://arxiv.org/abs/2307.12898.
