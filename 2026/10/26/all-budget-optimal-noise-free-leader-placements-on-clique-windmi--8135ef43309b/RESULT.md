# All-budget optimal noise-free leader placements on clique windmills

## Finding

Let \(k,s\ge 2\) and let \(W_{k,s}=K_1\vee(kK_s)\) have unit edge conductances. The common vertex is the hub and the \(k\) peripheral cliques, each of order \(s\), are blades. For each integer budget \(1\le m\le ks\), pin exactly \(m\) distinct vertices as noise-free leaders and minimize \(J(S)=\operatorname{tr}(L_{V\setminus S,V\setminus S}^{-1})\), where \(L\) is the unnormalized combinatorial Laplacian.

**Exact all-budget classification:** Among placements that include the hub, and separately among those that omit it, the minimizing leader sets are *exactly* those with blade occupancy counts differing by at most one. Let \(b(j)\) be the length-\(k\) vector consisting of \(k-r\) copies of \(a\) and \(r\) copies of \(a+1\), where \(j=ka+r\), \(0\le r<k\). Define, for integers \(0\le t\le s\),
\[
 F_s(t)=\frac{s-t-1}{s+1}+\frac1{t+1},\qquad
 g_s(t)=\frac{s-t}{(t+1)^2},\qquad
 h(t)=\frac{t}{t+1}.
\]
For each allowed budget, write
\[
 H_{k,s}(m)=\sum_{i=1}^{k}F_s(b_i(m-1)),
\]
\[
 P_{k,s}(m)=\sum_{i=1}^{k}F_s(b_i(m))+
 \frac{1+\sum_{i=1}^{k}g_s(b_i(m))}{(s+1)\sum_{i=1}^{k}h(b_i(m))}.
\]
The denominator is positive because \(m\ge1\). Then the global minimum is **exactly**
\[
 J_{\min}(k,s,m)=\min\{H_{k,s}(m),P_{k,s}(m)\}.
\]
If \(H<P\), the optimal sets comprise the hub and a balanced allocation of the remaining \(m-1\) leaders. If \(P<H\), optimal sets omit the hub and have a balanced allocation of all \(m\) leaders. If \(H=P\), both classes, and no others, are optimal. These rules include endpoint budgets, all integer parameters, and all ties.

For \(j\in\{m-1,m\}\) and \((a,r)=(\lfloor j/k\rfloor,j-k\lfloor j/k\rfloor)\), the number of balanced subsets with \(j\) peripheral leaders is
\[
 B_{k,s}(j)=\binom{k}{r}\binom{s}{a}^{k-r}\binom{s}{a+1}^{r}.
\]
Consequently the number of globally optimal unordered leader sets is
\[
 \mathbf1_{\{H\le P\}}B_{k,s}(m-1)+\mathbf1_{\{P\le H\}}B_{k,s}(m).
\]
In particular, the complete three-leader phase boundary is: for \(k=2\), only peripheral leaders win when \(s=2,3,4\); both statuses tie when \(s=5\); and only hub-containing sets win when \(s\ge6\). For \(k=3\) only three peripheral leaders in different blades win. For \((k,s)=(4,2)\) the two statuses tie. For all other \(k\ge4\), only hub-containing sets win. In the hub case the two peripheral leaders lie in distinct blades; in the no-hub case the leaders are balanced (occupancies \((2,1)\) for \(k=2\), otherwise one in each of three blades).

## Assumptions and scope

The graph is finite, simple, connected, unweighted, and exactly \(W_{k,s}\) with integer \(k,s\ge2\). Leaders are perfectly pinned (noise-free); only the followers experience independent equal-intensity additive disturbances. The optimization is over *every* \(m\)-element subset of vertices; it does not assume automorphism-invariant leader sets. The objective \(J\) is the trace of the inverse grounded Laplacian; with unit-intensity white noise and the conventional Ornstein–Uhlenbeck normalization, steady-state total follower variance is \(J/2\). The classification is unchanged by that constant factor.

The largest budget treated is \(m=ks\), leaving the hub as a possible sole follower. The case of pinning all \(ks+1\) vertices has no follower inverse and is deliberately excluded. Empty peripheral blocks contribute zero to inverse traces. The balanced-count formula uses \(\binom{s}{s+1}^{0}=1\) when that exponent vanishes.

## Proof

**Step 1: a grounded blade.** Fix \(t\) peripheral leaders in one blade and put \(u=s-t\). Its follower principal block, whether or not the hub is pinned, is
\[
 B_t=(s+1)I_u-\mathbf1_u\mathbf1_u^{\mathsf T}.
\]
For \(u>0\), its eigenvalues are \(t+1\) on the constant vector and \(s+1\) on the \(u-1\) orthogonal contrasts. Thus it is positive definite and
\[
 \operatorname{tr}(B_t^{-1})=F_s(t),\quad
 \mathbf1_u^{\mathsf T}B_t^{-1}\mathbf1_u=\frac{s-t}{t+1},\quad
 \mathbf1_u^{\mathsf T}B_t^{-2}\mathbf1_u=g_s(t).
\]
The identities remain valid for \(t=s\) under the empty-block convention: each is zero, including \(F_s(s)=0\).

**Step 2: exact cost for an arbitrary placement.** Let \((t_1,\ldots,t_k)\) be its peripheral leader counts. If the hub is a leader, the follower Laplacian is block diagonal with blocks \(B_{t_i}\), yielding
\[
 J(S)=\sum_i F_s(t_i).
\]
If the hub is a follower, its diagonal Laplacian entry is \(ks\), and it couples to the remaining peripheral followers by \(-\mathbf1\). The Schur complement of the peripheral blocks is
\[
 Q=ks-\sum_i\frac{s-t_i}{t_i+1}=(s+1)\sum_i\frac{t_i}{t_i+1}=(s+1)\sum_i h(t_i).
\]
At least one peripheral leader is present, so \(Q>0\). Applying the block inverse formula and taking its trace gives
\[
 J(S)=\sum_i F_s(t_i)+\frac{1+\sum_i g_s(t_i)}{(s+1)\sum_i h(t_i)}.
\]
This is an independent derivation of both exact objective formulas; these formulas themselves are not asserted to be historically novel.

**Step 3: strict balancing.** On \(0\le t\le s\), considered as a real interval,
\[
 F_s''(t)=\frac2{(t+1)^3}>0,\qquad
 g_s''(t)=\frac{6s-2t+4}{(t+1)^4}>0,\qquad
 h''(t)=-\frac2{(t+1)^3}<0.
\]
If any two integer counts obey \(t_i\ge t_j+2\), transferring one leader from blade \(i\) to blade \(j\) strictly decreases \(\sum F_s\) and \(\sum g_s\), and strictly increases \(\sum h\). For hub-pinned placements, this strictly decreases \(J\). For hub-unpinned placements, it strictly decreases both the additive base and the positive correction, since its numerator decreases and its positive denominator increases. Repeating transfers terminates exactly at the balanced vector \(b(j)\), up to permutation. Every nonbalanced placement is strictly dominated, while all balanced placements at a fixed hub status are related by graph automorphisms. This proves the **if and only if** classification, not merely existence of a balanced optimum.

**Step 4: two candidate costs and exact counting.** A hub-containing set has \(j=m-1\) peripheral leaders; a hub-omitting set has \(j=m\). Substituting their balanced vectors into Step 2 gives \(H_{k,s}(m)\) and \(P_{k,s}(m)\) respectively. Their lesser value is the global optimum. A balanced profile has \(r\) blades with \(a+1\) leaders and \(k-r\) blades with \(a\) leaders, giving precisely \(\binom{k}{r}\binom{s}{a}^{k-r}\binom{s}{a+1}^{r}\) subsets. The hub adds no multiplicity. At equality between costs, the two mutually exclusive hub statuses are both optimal and their counts add.

**Step 5: sharp three-leader corollary.** Among hub-containing triples, one leader in each of two distinct blades is better than two in one blade by exactly \(1/3\); the better cost is
\[
 J_H=\frac{2ks-s-3}{s+1}.
\]
For \(k\ge3\), among triples omitting the hub, three different blades strictly win over the \((2,1)\) and \((3)\) occupancy patterns, by Step 3; their cost is
\[
 J_P=\frac{8ks-9s-13}{3(s+1)}.
\]
Their difference is \(J_P-J_H=2((k-3)s-2)/(3(s+1))\), producing the claimed \(k\ge3\) phases, including the unique tie parameters \((k,s)=(4,2)\). For \(k=2\), the best hub-omitting profile is \((2,1)\), whose cost is
\[
 J_P=\frac{2(10ks-9s-13)}{7(s+1)};
\]
the difference \(J_P-J_H=(s-5)/(7(s+1))\) proves the stated \(k=2\) transition. All comparisons are strict away from the displayed ties.

## Verification

Execute `python verify.py` with Python 3.10+ and SymPy 1.10+. The verifier checks the symbolic second derivatives exactly; all occupancy profiles for \(2\le k,s\le5\); the three-leader phase pattern across \(2\le k\le11,2\le s\le14\); exact inverse grounded-Laplacian traces computed separately from the Schur-complement formula; exhaustive three-leader choices on eight small graphs; and optimizer counts. It prints:

`VERIFY_OK symbolic_derivatives=3 occupancy_profiles=29856 triple_phase_cases=130 exact_grounded_inverses=224 exhaustive_three_leader_inverses=819 optimizer_count_checks=8`

The finite checks are reproducibility evidence only. The infinite-domain statements follow from Steps 1–5, particularly the strict convexity/concavity transfer.

## Relationship to prior work

Fitch and Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks* (first available 7 July 2014, arXiv:1407.1569), formulate the general noise-free-leader coherence objective and joint centrality, and work out paths and cycles; they do not present this all-budget blade-balancing classification. Patterson, McGlohon and Dyagilev (arXiv:1412.6595) give exact leader selection on one-dimensional formations, distinct from clique windmills. Patterson, Yi and Zhang (arXiv:1708.06873) derive resistance-based formulas and selected special graph families; the inspected full text does not provide this theorem. General grounded-inverse, Schur-complement and convex-balancing techniques are classical and not claimed as new.

Sun, Li and Liu, *Noisy consensus dynamics in windmill-type graphs* (2020), DOI 10.1063/5.0020696, is especially close: its abstract asserts exact leader–follower coherence formulas for windmill-type graphs with freely assigned leaders. Its full paper was not accessible through lawful open sources or available institutional access at this review. **It may already imply or state part or all of the present result.** Neither its exact graph parameters nor whether it optimizes all leader placements is determined from its abstract. The present claimed contribution is the if-and-only-if *all-budget placement optimization*, exact optimizer count and sharp three-leader phase, not novelty of the arbitrary-placement coherence formula. This source is an explicit substantial priority risk, not classified as not covering.

## Limitations

The graph family is symmetric, simple, unweighted, and has equal-sized peripheral cliques; unequal blade sizes and weighted networks are not classified. The objective assumes perfectly pinned noise-free leaders and equal follower noise. The two-candidate formula is an exact closed decision rule for any budget but does not simplify to a uniform single-threshold formula in all three integers. Independent audit has not been performed. The inaccessible, highly relevant 2020 windmill-type paper creates material residual novelty uncertainty; mathematical correctness does not resolve priority.

## References

1. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, 2014, https://arxiv.org/abs/1407.1569 (first public date 2014-07-07).
2. S. Patterson, N. McGlohon and K. Dyagilev, *Efficient Optimal k-Leader Selection for Coherent One-Dimensional Formations*, arXiv:1412.6595, 2014, https://arxiv.org/abs/1412.6595.
3. S. Patterson, Y. Yi and Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873, 2017, https://arxiv.org/abs/1708.06873.
4. W. Sun, Y. Li and S. Liu, *Noisy consensus dynamics in windmill-type graphs*, Chaos 30, 123131 (2020), https://doi.org/10.1063/5.0020696 (abstract inspected; full text unavailable).
