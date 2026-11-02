# Exact two-choice cover times on paths and the first failure of unvisited-first control

## Finding
Consider the path with vertices \(0,1,\ldots,N\), for any integer \(N\ge1\). At each step, two neighbors of the present vertex are independently sampled uniformly **with replacement**, and a controller must choose one of the two offered neighbors. Every vertex already visited is remembered. Write \(C_N(x)\) for the minimum expected number of additional edge steps required to visit every vertex, starting at \(x\) with only \(x\) initially visited. Controllers may use the complete past and all realized offers but not future offers.

For integers \(0\le x\le N\), define
\[
 L_N=2N-\frac32(1-3^{-N}),\qquad d=\min\{x,N-x\},\qquad m=\lfloor N/2\rfloor,
\]
and the following symmetric endpoint-exit value:
\[
 E_N(x)=\begin{cases}
 2d-\dfrac{3^{d+1}-3}{2\cdot3^m},&N=2m,\\[5pt]
 2d-\dfrac{3^{d+1}-3}{3^{m+1}},&N=2m+1.
 \end{cases}
\]
Then the **exact optimal expected cover time** is
\[
 \boxed{C_N(x)=L_N+E_N(x)}\qquad(N\ge1,\ 0\le x\le N).
\]
For any already visited interval, an optimal policy is: *until either endpoint has been visited, prefer the offered neighbor closer to the nearer endpoint of the whole path; after one endpoint has been visited, prefer the offered neighbor in the direction of the other endpoint.* Equal-value offers may be resolved arbitrarily. Consequently the maximum, over starts, is attained at the center and equals \(3N+O(1)\) as \(N\to\infty\).

There is a sharp boundary for **unvisited-first** decisions (the requirement to choose an offered unvisited neighbor whenever the other offered neighbor was visited). On every path of at most five vertices some optimal policy obeys unvisited-first at every history. On every path of at least six vertices an unvisited-first decision is strictly suboptimal at a reachable history. Specifically, with \(n=N+1\ge5\), visited interval \(\{1,2\}\), current vertex \(2\), and offered neighbors \(\{1,3\}\), choosing the *unvisited* vertex \(3\) instead of the visited vertex \(1\) incurs the strictly quantified extra optimal continuation cost
\[
 \Delta_n=\begin{cases}
 4-\dfrac4{3^{(n-5)/2}}, & n\text{ odd},\\[5pt]
 4-\dfrac8{3^{(n-4)/2}}, & n\text{ even}.
 \end{cases}
\]
It is zero for \(n=5\), positive for every \(n\ge6\), and tends to \(4\). For six vertices, the two continuation costs, after the respective immediate move, are exactly \(833/81\) and \(941/81\), a difference of \(4/3\). The cutoff refers to paths and to the local requirement of unvisited-first control; no minimum-order claim is made among arbitrary graphs.

## Assumptions and scope
The graph is the simple, undirected path \(P_{N+1}\). Offers are independent at every step, including the possibility that both offers coincide. Edge steps, rather than offer rounds with possible stays, are counted. A vertex is counted visited upon arrival, including the initial vertex. Optimality concerns **expected cover time**, not stochastic dominance of the entire cover-time distribution. The controller knows the path, location, visit history and current offers. No edge weights, outside vertices or additional choice options are assumed.

## Proof
**1. Endpoint reduction.** On a path, the set of visited vertices is always an interval, and all vertices have been visited if and only if both endpoints \(0,N\) have been visited. Define \(H_N(x)\) as the minimum expected steps to first hit the right endpoint \(N\) from \(x\). By reflection, the optimal cost to hit the left endpoint is \(H_N(N-x)\). Once the *first* endpoint is reached, the walker stands there and has yet to reach the other endpoint; the optimal remaining cost is the common constant \(L_N=H_N(0)\), independent of which endpoint was reached. Since every admissible completion necessarily visits an endpoint first, optimizing the whole cover reduces exactly to optimizing the first entrance time of \(\{0,N\}\), followed by constant \(L_N\). Therefore \(C_N(x)=E_N(x)+L_N\), provided the two displayed target-hitting values and strategies are optimal.

**2. Hitting the far endpoint.** At an interior vertex an offered preferred neighbor is present with probability \(1-(1/2)^2=3/4\). A policy always preferring the right neighbor has transition probability \(3/4\) to the right and \(1/4\) to the left at every interior vertex; at \(0\) the step to \(1\) is forced. Let
\[
 H_N(x)=\sum_{j=x}^{N-1}(2-3^{-j}),\quad 0\le x\le N.
\]
The adjacent difference \(H_N(x)-H_N(x+1)=2-3^{-x}>0\) confirms that a rightward offer always has lower continuation cost. Direct substitution verifies
\[
 H_N(N)=0,\quad H_N(0)=1+H_N(1),\quad
 H_N(i)=1+\frac14 H_N(i-1)+\frac34 H_N(i+1)
\]
for every \(0<i<N\). Thus this candidate solves the *minimizing Bellman equation*: at each interior vertex, the smaller of the two possible continuation values is chosen whenever offered. Summation gives
\[
 H_N(0)=\sum_{j=0}^{N-1}(2-3^{-j})=2N-\frac32(1-3^{-N})=L_N.
\]

**3. Hitting either endpoint.** The displayed \(E_N\) is symmetric, vanishes at \(0,N\), and is strictly increasing as the position moves toward the center. For \(N=2m\), on the left half its successive increments are
\[
 E_N(i)-E_N(i-1)=2-3^{i-m}\qquad(1\le i\le m).
\]
For \(N=2m+1\), they are
\[
 E_N(i)-E_N(i-1)=2-2\cdot3^{i-m-1}\qquad(1\le i\le m),
\]
and the two central vertices have equal values. All these increments are positive. Their geometric relations, with the central reflection and the forced endpoint steps, verify at each interior position \(i\) the Bellman identity
\[
 E_N(i)=1+\frac{3\min\{E_N(i-1),E_N(i+1)\}
 +\max\{E_N(i-1),E_N(i+1)\}}4.
\]
Thus preferring the offered neighbor whose position has smaller \(E_N\), i.e. a neighbor pointing toward the nearer endpoint, is optimal. The Bellman verification is legitimate even among history-dependent randomized controls: the nonnegative candidate produces a submartingale lower bound on expected stopping time under every policy, whereas the indicated stationary policy achieves equality. Absorption is almost sure with finite mean because along either specified neighboring direction the probability of the necessary offer is bounded below by \(1/4\) and the state space is finite. This proves the cover formula and policy. The central maximum follows from strict increase toward the center, together with the explicit formulas for \(E_N\) and \(L_N\).

**4. The unvisited-first threshold.** If an endpoint is already visited, every offered unvisited neighbor (if any) moves toward the other endpoint, as an optimal policy requires. Before either endpoint has been visited, the visited set is an interval \([\ell,r]\) strictly inside \([0,N]\). A conflict between unvisited-first and optimal control can arise only at an interval frontier: one offered neighbor lies outside the visited interval, the other inside it. For \(N\le4\), elementary inspection of the finitely many frontier positions shows that the fresh neighbor is never strictly farther from its nearer endpoint than the visited neighbor. Hence one can resolve every such conflict in favor of the fresh neighbor without increasing the optimal continuation value; other offered ties can be chosen according to the preceding optimal policy. This proves existence of an optimal unvisited-first policy on paths of order at most five.

For \(N\ge4\), the history \([1,2]\) with current position \(2\) is reachable by traversing \(1\) to \(2\) before any endpoint has been seen. With offers \(\{1,3\}\), the two next positions and visited intervals are \((1,[1,2])\) and \((3,[1,3])\). Neither step touches an endpoint when \(N\ge4\), so their optimal costs after that step are respectively \(L_N+E_N(1)\) and \(L_N+E_N(3)\). The cost difference is \(E_N(3)-E_N(1)\). Substituting \(N=n-1\) into the explicit symmetric formulas gives precisely the two parity-dependent expressions for \(\Delta_n\) above. They are zero when \(n=5\), strictly positive when \(n\ge6\), and converge to \(4\). In the six-vertex case, direct rational evaluation gives \(L_5+E_5(1)=833/81\), \(L_5+E_5(3)=941/81\). The immediate transition costs are both one, so they cancel in the comparison. Any policy insisting on the fresh neighbor at that positive-probability offered pair has strictly greater expected remaining cover time than an otherwise optimal policy, proving the sharp cutoff.

## Verification
The companion self-contained script `check_path_choices.py` uses exact \(\mathbb Q\)-arithmetic. It checks the Bellman optimality equation for every position and every contiguous visited interval for every path order from two through twenty-one, and it checks every frontier unvisited-first conflict through five vertices. Separately it enumerates every deterministic stationary two-offer direction preference for one-target and two-endpoint hitting on paths of up to nine vertices, solves each rational hitting-time linear system, and takes the exact minimum over all those policies. It also checks the stated parity gap and six-vertex rational witness. The replay reports 45,150 exact rational checks with no assertion failures. These finite checks corroborate, but do not replace, the arbitrary-order proof above.

## Relationship to prior work
Georgakopoulos, Haslegrave, Sauerwald and Sylvester introduced this with-replacement two-choice walk and established linear-order cover-time bounds on bounded-degree trees, as well as algorithms for optimal hitting controls and general computational hardness of cover-control decisions [1,2]. In their Section 3 they note that optimal path hitting time is approximately twice the number of edges; the exact finite path cover expression, two-phase endpoint policy, and first path order of failure for unvisited-first control are not among their stated results. Their general Bellman framework is a background method rather than an implication of these closed-form constants or the sharp threshold. Orenshtein and Shinkar's greedy random walk [3] always privileges previously untraversed *edges* without a random two-offer restriction; its edge-cover results do not imply the present vertex-cover control classification. The earlier empirical two-choice visit-count preference studied by Avin and Krishnamachari [4] also differs from the exact first-visit preference considered here. These are distinctions in mathematical statements and assumptions, not a certification of historical priority.

## Limitations
The theorem is about paths only and about minimization of expected time; it does not claim a cover-time stochastic-order optimum, universal unvisited-first failure on other graph classes, or uniqueness of every optimal tie-breaking choice. The smallest obstruction is among paths, not among all connected graphs. The independent rational checks cover finite orders, while the proof uses exact Bellman verification for arbitrary \(N\). Unknown other presentations of an equivalent closed formula remain a historical-priority risk.

## References
[1] A. Georgakopoulos, J. Haslegrave, T. Sauerwald, J. Sylvester, *The Power of Two Choices for Random Walks*, arXiv:1911.05170, first posted 2019-11-12. https://arxiv.org/abs/1911.05170

[2] A. Georgakopoulos, J. Haslegrave, T. Sauerwald, J. Sylvester, *Choice and Bias in Random Walks*, ITCS 2020, DOI:10.4230/LIPIcs.ITCS.2020.76. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ITCS.2020.76

[3] T. Orenshtein, I. Shinkar, *Greedy Random Walk*, arXiv:1101.5711. https://arxiv.org/abs/1101.5711

[4] C. Avin and B. Krishnamachari, *The Power of Choice in Random Walks: An Empirical Study*, Computer Networks 52 (2008). https://doi.org/10.1016/j.comnet.2007.09.012
