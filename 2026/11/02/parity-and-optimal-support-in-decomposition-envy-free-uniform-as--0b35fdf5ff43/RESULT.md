# Parity and optimal support in decomposition-envy-free uniform assignments

## Finding

Consider \(n\geq2\) agents and \(n\) indivisible objects, all agents having the **same strict ranking**. Fix the uniform assignment matrix \(U\) whose entries are \(1/n\). Among probability distributions over distinct deterministic bijective allocations realizing \(U\), require *decomposition envy-freeness* (Dec-EF): for every ordered pair of distinct agents, the probability that the first agent receives a worse-ranked object than the second is at most \(1/2\).

Let \(s(n)\) be the minimum number of allocations with strictly positive probability in such a distribution. Then

\[
\boxed{s(n)=n\quad\text{for every even }n\geq2,}
\]
\[
\boxed{n+2\leq s(n)\leq2n\quad\text{for every odd }n\geq3,}
\]
with the **exact first odd case** \(s(3)=6\). At \(n=3\), there is exactly one Dec-EF distribution realizing \(U\): it puts mass \(1/6\) on each of the six permutations. A separate structural statement valid for all \(n\geq2\) is that **no** uniform \(n\)-by-\(n\) assignment matrix can be implemented using exactly \(n+1\) distinct positive-weight permutations (with or without Dec-EF).

## Assumptions and scope

Label agents and object ranks \(0,\ldots,n-1\), with smaller object rank strictly preferred. Each deterministic assignment is a permutation \(P\), where \(P(i)\) denotes the rank received by agent \(i\). A lottery \(\lambda\) assigns a positive probability to each member of its support. The induced matrix is uniform exactly when \(\sum_{P:P(i)=j}\lambda(P)=1/n\) for every agent \(i\) and rank \(j\). Because rankings are strict and common, for distinct \(i,j\) exactly one of \(P(i)>P(j)\) and \(P(j)>P(i)\) holds. Hence Dec-EF for both orders is equivalent to the exact pairwise balancing identity

\[
\Pr_{P\sim\lambda}[P(i)>P(j)]=1/2\quad(i\ne j).
\]

All probabilities are exact and no assumption of independent object allocation is made; the allocations are perfect matchings.

## Proof

**1. The marginal lower bound.** Fix an agent. In the uniform matrix she receives every one of \(n\) objects with positive probability. An individual permutation gives her only one object. Hence any implementing lottery must have at least \(n\) distinct supported permutations. If it has exactly \(n\), each rank for that agent occurs once and its permutation has weight \(1/n\). The same observation holds for every agent. Pairwise comparison probabilities are therefore integral multiples of \(1/n\), so they cannot equal \(1/2\) when \(n\) is odd. Thus odd \(n\) cannot achieve the \(n\)-support lower bound.

**2. There is no support of exactly \(n+1\) for the uniform matrix.** Suppose \(n+1\) *distinct* permutations have positive weights \(w_1,\ldots,w_{n+1}\), and give every agent each object with probability \(1/n\). No individual weight can exceed \(1/n\), since that permutation gives some agent some object with at least its own probability. For any fixed agent, \(n+1\) support occurrences cover \(n\) objects of positive marginal probability, so exactly one object is received in *two* supported permutations and the other \(n-1\) objects each in one. The \(n-1\) singleton weights must equal \(1/n\), and the two remaining weights are strictly below \(1/n\) and add to \(1/n\). In particular the two sub-\(1/n\) support permutations are globally identifiable by their weights, and the same two must be paired on the same object in every agent's row. But then those two permutations assign the same object to **every** agent, contradicting their distinctness. Consequently no \(n+1\)-support representation exists, regardless of Dec-EF. Combining this fact with Step 1 gives \(s(n)\geq n+2\) for odd \(n\).

**3. Optimal constructions for all even sizes.** Write \(n=2m\) and form a permutation of ranks

\[
q=(0,1,\ldots,m-1,\,2m-1,2m-2,\ldots,m).
\]

For each shift \(t\in\{0,\ldots,n-1\}\), choose the assignment \(P_t(i)=q((i+t)\bmod n)\), with probability \(1/n\). These \(n\) assignments are distinct, and each agent receives each rank exactly once. The key identity is

\[
q((k+m)\bmod n)=n-1-q(k).
\]

Therefore \(P_{t+m}(i)=n-1-P_t(i)\) for all agents \(i\), so the assignments \(P_t\) and \(P_{t+m}\) reverse every strict pairwise rank comparison. Pair the \(n\) shifts into the \(m\) disjoint pairs \(\{t,t+m\}\). For every two agents, in exactly one assignment in each pair the first envies the second. Thus the envy probability is exactly \(m/n=1/2\), satisfying Dec-EF. The marginal bound proves \(s(n)=n\).

**4. Universal odd-size upper bound.** For odd \(n\geq3\), take the \(n\) cyclic assignments \(F_t(i)=(i+t)\bmod n\), and their rank-reversals \(R_t(i)=n-1-F_t(i)\). Each family independently realizes the uniform matrix, so taking all \(2n\) assignments with probability \(1/(2n)\) does too. For \(n\geq3\), the forward shifts and reversed shifts are disjoint: equality of one forward and one reversed shift would force \(2\equiv0\pmod n\) by subtracting their values at two consecutive agents. Reversing each assignment flips all pairwise comparisons. Hence all envy probabilities equal \(1/2\), establishing \(s(n)\leq2n\).

**5. Three-agent uniqueness.** List the six assignments as

\[
(012),(021),(102),(120),(201),(210).
\]

Solving the nine uniform-marginal equations shows that **every** decomposition of \(U\) has weight vector

\[
(1/3-\tau,\ \tau,\ \tau,\ 1/3-\tau,\ 1/3-\tau,\ \tau),
\qquad0\leq\tau\leq1/3.
\]

For the ordered pair of agents \((0,1)\), the first envies the second in assignments \((102),(201),(210)\), with combined probability \(1/3+\tau\). Dec-EF for both orientations requires exactly \(1/2\), so \(\tau=1/6\). This makes every permutation's weight \(1/6\). The resulting uniform lottery is Dec-EF by permutation symmetry. It is the sole feasible lottery, and \(s(3)=6\).

## Verification

The self-contained `verify_support.py` uses standard-library exact fractions, verifies the explicit even-size support for \(n=2,4,\ldots,20\), the odd-size upper constructions for \(n=3,5,\ldots,19\), and independently solves all exact marginal and pairwise-balance equations for the six three-agent permutations by rational row reduction. Run it with `python verify_support.py`. All test cases pass. The universally quantified claims are proved in the preceding steps; testing finitely many sizes is not used as proof.

## Relationship to prior work

Kawase, Suksompong, Sumita and Yokoi (2026) introduced Dec-EF; their Example 1 contrasts a three-permutation cyclic decomposition of the uniform three-agent matrix, which fails Dec-EF, with the six-permutation uniform decomposition, which satisfies it. Their main theorems concern *existence* for small agent counts and restricted preference diversity. The result here determines that the six-permutation lottery in their example is **forced**, and gives support-optimality and parity obstructions for an infinite uniform family. Their discussion of minimal-support Birkhoff decompositions motivates the support-minimization question but does not state these bounds. Li, He and Li (2026) study existence for four and five agents, entropy-selected decompositions and hardness; an inaccessible complete text leaves unresolved whether it contains an equivalent support statement.

## Limitations

The strict ranking must be common to all agents and the prescribed matrix must be uniform. The result does not give the exact minimum for odd \(n\geq5\), does not establish sparse Dec-EF decompositions for arbitrary bistochastic matrices, and does not replace the general existence results in the literature. An unpublished or uninspected equivalent support construction remains possible; independent assessment has not been conducted.

## References

- Y. Kawase, W. Suksompong, H. Sumita and Y. Yokoi, *Decomposition Envy-Freeness in Random Assignment*, arXiv:2604.16973v1, first posted 18 April 2026. https://arxiv.org/abs/2604.16973
- K. Li, Y. He and Q. Li, *Envy-Free Decompositions of Random Assignments: Settling Four Agents, and What Lies Beyond*, arXiv:2609.35192v1, first posted 28 September 2026. https://arxiv.org/abs/2609.35192
