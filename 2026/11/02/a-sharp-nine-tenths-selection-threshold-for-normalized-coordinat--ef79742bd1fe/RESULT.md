# A sharp nine-tenths selection threshold for normalized coordination on a three-vertex path

## Finding
Consider the original degree-normalized binary coordination payoff of Zhang and Vasconcelos (2023), extended from regular graphs to the three-vertex path \(P_3\). For each \(3/4<\theta<3/2\), asynchronous uniform-player log-linear learning at common inverse noise \(\beta>0\) has a unique stationary law \(\pi_{\beta,\theta}\). Its two deterministic pure equilibria are \(000\) and \(111\), with \(111\) strictly Pareto dominating \(000\). The low-noise limit is exactly
\[
\lim_{\beta\to\infty}(\pi_{\beta,\theta}(000),\pi_{\beta,\theta}(111))=
\begin{cases}(0,1),&3/4<\theta<9/10,\\(2/5,3/5),&\theta=9/10,\\(1,0),&9/10<\theta<3/2.\end{cases}
\]
In each case all other six profiles have limiting probability zero. In particular, for \(9/10<\theta<1\), the all-zero equilibrium is uniquely stochastically selected even though all-one uniquely maximizes the game's degree-weighted potential.

## Assumptions and scope
The underlying undirected graph is the labeled path with leaf vertices \(1,3\) and hub \(2\). Each \(a_i\in\{0,1\}\), with \(d_1=d_3=1\), \(d_2=2\), and \(N=3\). The payoff is
\[
U_i(a)=a_i\left(\frac{\sum_{j\sim i}a_j}{d_i}-\frac{d_i\theta}{3}\right).
\]
At each discrete update, one of the three vertices is selected uniformly and sets its action to \(1\) with probability \((1+\exp[-\beta\Delta_i])^{-1}\), where \(\Delta_i=U_i(1,a_{-i})-U_i(0,a_{-i})\); otherwise it sets action \(0\). Every \(\beta>0\) gives an irreducible and aperiodic finite chain. The assertion concerns its stationary distribution as \(\beta\) tends to infinity, not almost-sure pathwise convergence for a fixed positive noise.

## Proof
**Pure equilibria and weighted potential.** Write \(k=a_1+a_3\), \(c=a_2\). The leaf payoff gain for switching to action \(1\) is \(\Delta_\ell=c-\theta/3\); the hub gain is \(\Delta_h=k/2-2\theta/3\). For \(3/4<\theta<3/2\), the only profiles with every player's action a best response are \(000\) and \(111\), with no indifference at those two profiles. At \(111\), each leaf gains \(1-\theta/3>0\) and the hub gains \(1-2\theta/3>0\); at \(000\), everyone's payoff is zero. Define
\[
\Psi(a)=a_1a_2+a_2a_3-\frac\theta3(a_1+4a_2+a_3).
\]
For any unilateral move by player \(i\), \(\Psi\) changes by \(d_i\) times that player's payoff change. Thus strictly improving moves strictly increase \(\Psi\), ruling out any other zero-resistance recurrent classes. When \(\theta<1\), maximizing \(\Psi\) conditional on \(a_2=0\) gives \(000\) with value \(0\); maximizing conditional on \(a_2=1\) gives \(111\) with value \(2-2\theta>0\). Hence \(111\) is the unique maximizer for \(\theta<1\).

**Transition resistances.** Ignoring the common factor \(1/3\), the six-state chain lumped by \((k,c)\) has positive transition rates \((2-k)\sigma(\beta\Delta_\ell)\) for \(k\mapsto k+1\), \(k[1-\sigma(\beta\Delta_\ell)]\) for \(k\mapsto k-1\), \(\sigma(\beta\Delta_h)\) for \(c:0\mapsto1\), and \(1-\sigma(\beta\Delta_h)\) for \(c:1\mapsto0\), where \(\sigma(x)=1/(1+e^{-x})\). Every such rate is a positive integer prefactor times \(e^{-\beta r}(1+o(1))\) with \(r=(-\Delta)_+\) for a \(0\to1\) move or \(r=(\Delta)_+\) for a \(1\to0\) move.

To leave \(000\) for \(111\), consider the first hub activation. If \(k=0,1,2\) leaves are active immediately before it, the minimum cost paid is bounded below respectively by \(2\theta/3\), \(\theta/3+(2\theta/3-1/2)=\theta-1/2\), and \(2\theta/3\). The middle option is smallest for \(\theta<3/2\), and is realized by a leaf activation, then hub activation, then the other leaf's free activation. Thus
\[
R_{000\to111}=\theta-1/2.
\]
For a path from \(111\) to \(000\), consider the first hub deactivation. With \(0,1,2\) leaf deactivations beforehand, the costs are bounded below by \(1-2\theta/3\), \(1-\theta/3\), \(2(1-\theta/3)\), respectively. Deactivating the hub first and then both leaves attains the smallest, so
\[
R_{111\to000}=1-2\theta/3.
\]
These are also the minimum directed in-tree resistances rooted at the respective *destination* equilibrium. Indeed, each in-tree must contain a route from the other equilibrium, providing the lower bound. Both minima can be attained by attaching all remaining three transient states with zero-resistance best-response edges: for the \(111\)-root, use \(000\to(1,0)\to(1,1)\to111\), plus \((2,0)\to111\) and \((0,1)\to000\); for the \(000\)-root, use \(111\to(2,0)\to(1,0)\to000\), plus \((1,1)\to(1,0)\) and \((0,1)\to000\).

A transient-root in-tree necessarily contains an exit from each equilibrium, so its total resistance is at least \(\theta/3+(1-2\theta/3)=1-\theta/3\). This exceeds \(\min\{\theta-1/2,1-2\theta/3\}\) on the entire open parameter interval: for \(\theta\le9/10\), compare against \(\theta-1/2\), and for \(\theta\ge9/10\), against \(1-2\theta/3\). Therefore every transient-root tree is asymptotically negligible. The finite-state Markov chain tree formula gives the strict-inequality cases. The two equilibrium tree resistances cross precisely at \(\theta=9/10\).

**Critical probability weights.** At \(\theta=9/10\), put \(q=e^{-\beta/10}\) and use the six states in order \((0,0),(1,0),(2,0),(0,1),(1,1),(2,1)\). The exact rational transition gains and multiplicity factors imply that the minimal directed in-tree exponent/coefficient pairs are, in that order, \((4,12),(7,24),(8,6),(10,4),(8,12),(4,18)\). Exhaustive enumeration of all admissible directed in-trees is supplied in `verify.py`; the code derives each edge resistance from the payoff equations, checks reachability to the root, and sums the product of each tree's leading rate coefficients. Thus the tree weights for \(000\) and \(111\) are respectively \(12q^4(1+o(1))\) and \(18q^4(1+o(1))\). Dividing by the total gives \(2/5\) and \(3/5\). Because leaf-permuting symmetry yields a strongly lumpable chain, these six-state stationary masses exactly equal the corresponding masses in the eight-profile chain.

## Verification
Run `python3 verify.py` (Python 3 standard library only). It computes exact rational transition resistances, independently checks the degree-weighted potential identity for every unilateral action move over five rational parameter choices, computes the minimal resistance paths, and exhaustively enumerates all rooted in-arborescences of the six-state transition graph at the critical parameter. Its expected final line is `CRITICAL_LIMIT 000=2/5, 111=3/5; THRESHOLD=9/10`. The symbolic inequalities and in-tree constructions above, rather than the finite parameter tests alone, justify the entire parameter interval.

## Relationship to prior work
Zhang and Vasconcelos, arXiv:2309.16931v1 (2023), introduced the degree-normalized payoff and analyzed log-linear learning on **regular** interaction graphs, where a common degree supplies an exact potential. The same authors' arXiv:2403.15683v1 (2024) analyzes **irregular** graphs with the materially different *unnormalized* interaction payoff \(a_i[\sum_{j\sim i}a_j-d_i\theta/N]\). That model is an exact-potential game on all undirected graphs, so its Gibbs selection conclusions do not apply to the original normalized payoff on \(P_3\). Generic log-linear-learning and finite-state resistance-tree methods are established; the claim here is the concrete original-payoff three-vertex selection transition, the exact critical mixture, and disagreement with both payoff and weighted-potential dominance. Targeted comparisons found no stated result implying these conclusions.

## Limitations
This is a theorem for the specified three-vertex path, identical finite-rationality parameter across players, and \(3/4<\theta<3/2\). The endpoints are excluded because some zero-noise best responses are indifferent. It is not a characterization of larger irregular graphs, heterogeneous inverse noise, finite-time consensus, or pathwise almost-sure convergence at positive noise. Although targeted source comparisons did not locate an equivalent result, an unindexed equivalent small-network calculation remains a bibliographic risk. Independent validation has not been performed.

## References
1. Y. Zhang and M. M. Vasconcelos, *Rationality and connectivity in stochastic learning for networked coordination games*, arXiv:2309.16931v1, first public 2023-09-29. https://arxiv.org/abs/2309.16931
2. Y. Zhang and M. M. Vasconcelos, *On the role of network structure in learning to coordinate with bounded rationality*, arXiv:2403.15683v1, first public 2024-03-23. https://arxiv.org/abs/2403.15683
3. D. Monderer and L. S. Shapley, *Potential games*, Games and Economic Behavior 14 (1996), 124–143. https://doi.org/10.1006/game.1996.0044
4. J. R. Marden and J. S. Shamma, *Revisiting log-linear learning: Asynchrony, completeness and payoff-based implementation*, Games and Economic Behavior 75 (2012), 788–808. https://doi.org/10.1016/j.geb.2012.02.005
