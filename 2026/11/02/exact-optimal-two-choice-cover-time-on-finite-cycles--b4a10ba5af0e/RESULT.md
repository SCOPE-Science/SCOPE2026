# Exact optimal two-choice cover time on finite cycles

## Finding
Let \(C_n\) be the simple cycle with \(n\ge 3\) vertices. A walker starts at any vertex, which is already counted as visited. At each transition it is offered two independent uniformly sampled neighbours, **with replacement**, and its controller chooses either offer using the past and current offers, without future information. Let \(T_n\) be the first time every vertex has been visited. The exact minimum expected cover time over all admissible controllers is

\[
\inf_{\pi}\mathbb E_{\pi}T_n=
\begin{cases}
2n-\dfrac92+\dfrac{9}{2\cdot3^{n/2}},&n\text{ even},\\[3pt]
2n-\dfrac92+\dfrac{5}{2\cdot3^{(n-1)/2}},&n\text{ odd}.
\end{cases}
\]

In particular, \(\inf_{\pi}\mathbb E_{\pi}T_n=2n-\frac92+O(3^{-n/2})\). An optimal deterministic policy keeps track of the already visited arc: when its two offered neighbours differ, select the neighbour closer to an end of that arc; at a tie either choice is optimal. In particular, always select a newly unvisited neighbour if one is offered.

## Assumptions and scope
The graph is an undirected simple cycle of size \(n\ge3\). Offers are i.i.d. uniform on the two graph neighbours, independently across times, and sampled with replacement. The controller may observe the full previously visited set and all past offers, but cannot see future offers. Cover time counts transitions and counts the initial vertex as already visited. The result is an exact *minimum of expectation*, not a stochastic-order statement about the entire cover-time distribution.

## Proof
**1. A connected visited arc and identical continuation values.** Until complete coverage, the visited vertices form a cyclic interval of size \(k\in\{1,\ldots,n-1\}\). Each first visit of a new vertex occurs by stepping out of one of the two ends of that interval and lands on an end of the new, enlarged interval. Every such enlarged configuration with \(k+1\) visited vertices and the walker at a newly visited end is equivalent under rotation and reflection. The conditional distribution of future offers is independent of the past. Therefore the optimal expected remaining cover time from an enlargement depends only on \(k+1\), not on which end was just enlarged, the path taken, or the past history. The principle of optimality reduces each phase, with \(k\) vertices already visited, to minimizing the expected number of transitions until the next new vertex; summing the resulting minimal means gives the global optimum.

**2. Exact optimal exit problem.** Label a currently visited interval \(0,\ldots,k-1\) and make the two neighbouring positions \(-1,k\) absorbing. (When \(k=n-1\), these two positions represent the same last unvisited cycle vertex, but they remain two distinct possible neighbour directions and both have value zero.) Let \(h_k(i)\) be the optimal expected time to reach either absorbing position when starting at \(i\). Set \(h_k(-1)=h_k(k)=0\). Each neighbour appears in at least one of the two offers with probability \(3/4\), and both offers are the other neighbour with probability \(1/4\). Consequently the optimal Bellman equations are

\[
h_k(i)=1+\frac34\min\{h_k(i-1),h_k(i+1)\}
          +\frac14\max\{h_k(i-1),h_k(i+1)\},
\quad 0\le i<k.
\tag{1}
\]

**3. Closed Bellman solution and optimality.** The following explicit functions satisfy (1), with reflection about the midpoint of the interval. Write \(j=\min\{i,k-1-i\}\):

\[
\begin{aligned}
 h_{2m}(i)&=2(j+1)+3^{-m}-3^{j+1-m}, &&m\ge1,\quad 0\le i<2m;\\
 h_{2m+1}(i)&=2(j+1)+\tfrac12 3^{-m}-\tfrac12 3^{j+1-m}, &&m\ge0,\quad 0\le i<2m+1.
\end{aligned}
\tag{2}
\]

For either parity, these expressions strictly increase while moving from a boundary toward the center (except for the two equal central values when \(k\) is even). Indeed the consecutive differences on the left half equal \(2-2\cdot3^{j+1-m}>0\) for \(k=2m\), and \(2-3^{j+1-m}>0\) for \(k=2m+1\), whenever the two indices lie on that half. Hence the minimum on the right of (1) is always attained by the neighbour closer to the nearer boundary. Substitution in the interior gives the linear recurrence

\[
h_k(i)=1+\frac34h_k(i-1)+\frac14h_k(i+1)
\]

on the left half, with the reflected recurrence on the right. The exponential term has characteristic ratio \(3\); the linear term has slope \(2\). At a central odd vertex the two neighbour values coincide and \(h_k(m)=1+h_k(m-1)\); at either central even vertex the midpoint reflection gives the corresponding equation with a tied central edge. These conditions and the absorbing values directly verify (1) everywhere, including \(k=1,2\). All values in (2) are nonnegative and finite.

For completeness, (1) uniquely determines the optimal finite value: for any fixed deterministic choice rule, the underlying walk has at least probability \(4^{-k}\) of making \(k\) consecutive outward moves in a specified direction, regardless of the rule, because an offer consisting of that direction twice forces it. Thus absorption has a uniformly bounded geometric tail and all policies are proper. The standard first-step dynamic programming comparison, or repeated iteration of the monotone Bellman operator followed by this uniform tail bound, shows that any finite solution of (1) is the optimal hitting-time function. A minimizer chooses the neighbour with the lower displayed value whenever both neighbours are offered.

**4. Cover time and parity.** From a newly visited end, the \(k\)-vertex phase has optimal expected duration

\[
 h_{2m}(0)=2-2\cdot3^{-m},\qquad
 h_{2m+1}(0)=2-3^{-m}.
\tag{3}
\]

There is one phase of each size \(k=1,\ldots,n-1\). Hence

\[
\inf_{\pi}\mathbb E_\pi T_n=\sum_{k=1}^{n-1}h_k(0).
\]

For \(n=2m\) the deficits from \(2\) sum to \(\sum_{j=0}^{m-1}3^{-j}+2\sum_{j=1}^{m-1}3^{-j}=\frac52-\frac92 3^{-m}\). For \(n=2m+1\) they sum to \(\sum_{j=0}^{m-1}3^{-j}+2\sum_{j=1}^{m}3^{-j}=\frac52-\frac52 3^{-m}\). Subtracting each deficit from \(2(n-1)\) gives the formulas in the finding. The policy described above attains each phase minimum and therefore the global minimum. \(\square\)

## Verification
The accompanying standalone `checker.py` uses only the Python standard library and exact rational arithmetic. Reproduce with `python3 checker.py` from the extracted package. It checks the Bellman equation, reflection, monotonicity and the policy's exact value for all \(1\le k\le104\); exhaustively compares every deterministic memoryless two-choice exit policy for \(1\le k\le9\); and checks both parity formulas against independent stage summation for \(3\le n\le104\). It passes 21,972 rational assertions. The finite diagnostic does not establish the all-size theorem: the analytic argument in the proof does.

For comparison, the ordinary simple random walk has mean \(k\) for the same interval-exit phase from a boundary, by the classical symmetric gambler's-ruin formula; its cycle cover mean is \(\sum_{k=1}^{n-1}k=n(n-1)/2\). Thus the leading expected-time speedup for optimal two-choice control is of order \(n/4\), with the exact optimal constant established above.

## Relationship to prior work
Georgakopoulos, Haslegrave, Sauerwald and Sylvester introduced and analyzed this independent-offer-with-replacement choice random walk. Their primary 2020-MSC classification includes 60J10. Their Theorem 5.3 gives only \(\Theta(n)\) optimal cover time for fixed-dimensional discrete tori, which includes cycles; it does not identify the exact cycle value or the boundary-directed policy. Their preliminary ITCS 2020 paper addresses general hitting, cover-time bounds and computational hardness, not the finite-cycle exact expression. Their papers are the model and order-of-growth antecedents, not a claim of exact-formula novelty here. The earlier empirical choice-walk work of Avin and Krishnamachari studies a different visit-count choice rule; its reported results are empirical rather than an optimal exact cycle theorem.

The exact conditional interval exit calculation is a special two-control-state dynamic-programming problem, and standard first-step/biased-walk methods supply tools, not the full cycle-cover statement. A semantically matching historical theorem could still exist under a different terminology; no absolute historical-priority assertion is made.

## Limitations
This result concerns undirected simple cycles of size at least three, two independent uniform offers with replacement, unrestricted history-dependent control without foresight and the minimum *expected* time to cover all vertices. It does not establish stochastic minimality of the cover-time distribution, the full cover-time law, or analogous formulas for paths with non-uniform degrees, larger offer counts, arbitrary tori or general graphs. The checker verifies finite instances only; the proof is the basis for the infinite claim. Independent audit has not been performed.

## References
1. A. Georgakopoulos, J. Haslegrave, T. Sauerwald and J. Sylvester, *The Power of Two Choices for Random Walks*, arXiv:1911.05170 (first posted 2019-11-12), *Combinatorics, Probability and Computing* **31** (2022), 73–100, doi:10.1017/S0963548321000183. Full open text: https://arxiv.org/abs/1911.05170 and https://wrap.warwick.ac.uk/152060/7/WRAP-Power-two-choices-random-walks-2021.pdf.
2. A. Georgakopoulos, J. Haslegrave, T. Sauerwald and J. Sylvester, *Choice and Bias in Random Walks*, ITCS 2020, article 76, doi:10.4230/LIPIcs.ITCS.2020.76. Full open text: https://wrap.warwick.ac.uk/id/eprint/130053/13/WRAP-Choice-bias-random-walks-Haslegrave-2020.pdf.
3. C. Avin and B. Krishnamachari, *The power of choice in random walks: an empirical study*, *Computer Networks* **52** (2008), 44–60; conference version MSWiM 2006, doi:10.1145/1164717.1164757.
