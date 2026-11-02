# Bipartite greediness and a tripartite cover-time counterexample

## Finding

For the discrete-time two-choice random walk on a finite graph, each step independently offers two uniformly sampled neighbors, with replacement, and a controller chooses one. A *greedy-first-visit* policy chooses an unvisited neighbor whenever exactly one offered neighbor is unvisited. The cover time includes the initially visited vertex.

**Theorem (structural boundary).** Every complete bipartite graph \(K_{a,b}\), for integers \(a,b\ge1\), has a greedy-first-visit policy that stochastically minimizes cover time from every starting vertex, even among history-dependent policies. In contrast, in the complete tripartite graph \(K_{1,2,6}\), starting at a vertex of the two-vertex part, **every** greedy-first-visit policy has expected cover time at least \(G\), but an explicit policy that occasionally prefers an already visited vertex has expectation \(D\), where

\[
G-D=\frac{2285849200770243971848}{4016620735540189127344279}>0.00056.
\]

The exact values are \(G=18.803347183744457\ldots\) and \(D=18.802778086149420\ldots\). These are expected numbers of transitions. The strict inequality is certified by rational arithmetic, not stochastic simulation. No claim is made that the alternative policy is globally optimal or that nine vertices is the minimum size of any counterexample.

## Assumptions and scope

The graph is simple and loopless. At each transition, the two random neighbors are independent and uniform **with replacement**; the controller sees both and the entire visited history. All finite cover-time expectations are taken under the resulting stochastic process. Greedy policies are constrained only to choose new over visited in a mixed pair; they can optimize all other choices, use randomization, and depend on history. The comparison graph \(K_{1,2,6}\) has three independent sets \(A,B,C\) of sizes \(1,2,6\), and every cross-part edge is present.

## Proof

**Bipartite assertion.** A walk on \(K_{a,b}\) alternates deterministically between its parts, regardless of the controller. Visits to each part occur at a predetermined subsequence of times, and the offers for that part are independent of the other part's offers. Conditional on having visited \(k\) different vertices of a part of size \(m\), an arbitrary policy can increase this count with probability at most \(1-(k/m)^2\); the greedy-first-visit rule attains the upper bound. Couple visited-count processes using common uniforms. When their counts coincide, the greedy increment can include every competing increment; when the greedy count is larger, a single competing increment cannot make it overtake. Hence in each part the greedy count dominates pathwise at all its visit opportunities, simultaneously for the two parts. The greedy cover time is therefore stochastically no larger than for any competing policy. Choosing between two as-yet-unvisited vertices does not affect the count transition law by within-part symmetry.

**Tripartite reduction.** Let \(s=(s_A,s_B,s_C)\) count previously visited vertices in each part, and \(i\) be the current part, with \(s_i\ge1\). Automorphism invariance and finite-state stochastic shortest-path dynamic programming show that the optimal value within the greedy-restricted class depends only on \((s,i)\). At terminal state \(s=(1,2,6)\), the value is zero. At any nonterminal state, each neighbor category \(c=(j,\epsilon)\), with \(j\ne i\) and \(\epsilon\in\{0,1\}\), consists respectively of \(s_j\) visited or \(a_j-s_j\) new vertices. Its multiplicity is \(m_c\). Write \(s+c=s+\epsilon e_j\). For any fixed deterministic offered-pair rule \(\phi\), the expectations satisfy the exact equations

\[
W_i(s)=1+\frac1{(9-a_i)^2}\sum_{c,d}m_cm_d\,W_{j_{\phi(c,d)}}(s+\phi(c,d)).
\]

These equations are solved in descending order of \(s_A+s_B+s_C\). Terms with \(\epsilon=0\) form a linear system of at most three equations at fixed \(s\); terms with \(\epsilon=1\) have already been computed. There is a unique finite solution because every stationary policy is proper: a connected finite graph cannot have a nonterminal closed class under forced identical neighbor offers.

**Exact greedy certificate.** The standalone verification program enumerates all attainable occupancy/current-part states, constructs a candidate greedy policy, evaluates it in exact fractions using the displayed equations, and verifies all 608 ordered offered-pair Bellman comparisons. For mixed new/visited pairs it enforces greedy selection. For equal novelty status it proves that the chosen option has no larger exact continuation value. This proves optimality among all greedy-first-visit policies, not only the particular candidate policy.

In the greedy continuation values, at state \(s=(0,2,2)\) with the walker in \(C\), an offer of the sole new vertex in \(A\) together with a visited vertex in \(B\) has the strict comparison

\[
W_A(1,2,2)-W_B(0,2,2)
=\frac{3210462360632365129}{1379009216128693567275}>0.
\]

The state is reachable with positive probability from a starting vertex in \(B\): identical paired offers can force a path from \(B_1\) to \(C_1\), then to \(B_2\), then to a distinct \(C_2\), without visiting \(A\). Hence visiting \(B\) is locally better even though visiting \(A\) would immediately gain a vertex. Define an admissible modified policy that agrees with the certified greedy policy everywhere except at precisely this state and this mixed pair of offers, where it chooses \(B\). Rational solution of the same policy-evaluation equations gives the displayed exact positive root improvement when starting in \(B\). This completes the counterexample.

## Verification

Run `python3 verify_choice.py` with a standard Python 3 interpreter from the directory containing this file. It requires no third-party packages, input files, random seeds, external services, or internet access. It regenerates all states and ordered offered-pair rules, solves rational linear systems, verifies constrained greedy Bellman optimality, evaluates the modified policy, and checks both exact positive fractions. The expected output ends with `all exact Bellman checks passed`. A floating-point iteration is used only to propose a policy; no floating-point assertion is part of the proof certificate.

## Relationship to prior work

Georgakopoulos, Haslegrave, Sauerwald, and Sylvester study the two-choice random walk and establish broad hitting/cover-time bounds and general algorithms, including the finite-state Markov decision formulation for optimal coverage (arXiv:1911.05170, first posted 2019-11-12, sections 2 and 7). Their generic optimal-policy characterization does not state which action wins for this particular tripartite graph; the new result is an explicit exact witness to failure of the apparently natural greedy-first-visit restriction, together with the bipartite contrast. Avin and Krishnamachari's earlier empirical study concerns a different local rule (preferring fewer previous visits) and reports simulations, not the strict expected-time comparison here. This work does not claim novelty of the two-choice model, Markov decision techniques, or general NP-hardness results.

## Limitations

Only complete bipartite graphs receive a universal stochastic-optimality statement. The counterexample certifies one nine-vertex tripartite graph and one root class; it neither optimizes unrestricted cover time exactly nor classifies all multipartite graphs. The gain is numerically small, although its sign is rigorously positive. No independent audit or exhaustive historical-priority determination is asserted.

## References

1. A. Georgakopoulos, J. Haslegrave, T. Sauerwald and J. Sylvester, *The Power of Two Choices for Random Walks*, arXiv:1911.05170v1 (2019-11-12); full text v2 at https://arxiv.org/html/1911.05170v2 ; *Combinatorics, Probability and Computing* 31 (2022), 73–100, DOI:10.1017/S0963548321000183.
2. C. Avin and B. Krishnamachari, *The power of choice in random walks: an empirical study*, Proceedings of MSWiM 2006, pp. 219–228, DOI:10.1145/1164717.1164757.
