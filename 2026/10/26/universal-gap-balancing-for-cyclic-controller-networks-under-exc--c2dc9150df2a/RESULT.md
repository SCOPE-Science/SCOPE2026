# Universal gap balancing for cyclic controller networks under exchangeable vertex failures

## Finding

Consider a simple cycle \(C_n\) with \(n\ge3\) vertices and an integer \(2\le k\le n\). Install controllers at a fixed set \(D\) of exactly \(k\) distinct vertices. An attacked set \(A\), sampled **independently of the placement** from a permutation-exchangeable probability law on subsets of vertices, is deleted, including any controllers located at deleted vertices. A nondeleted vertex is *served* exactly if its component in \(C_n-A\) contains an undeleted controller. Write \(S(D,A)\) for the number of served vertices.

The clockwise distances between successive controllers are positive integers \(d_1,\ldots,d_k\) summing to \(n\). For \(0\le r\le n\), define \(\binom ab=0\) if \(a<0\), \(b<0\), or \(b>a\), and
\[
F_{n,r}(d)=\sum_{t=1}^{d-1}\left[\binom{n-1}{r}-\binom{n-1-t}{r}-\binom{n-1-d+t}{r}+\binom{n-1-d}{r}\right],\qquad 1\le d\le n-1.
\]
Let \(\pi_r=\Pr(|A|=r)\). The **exact expected served count**, for every admissible placement and every such law, is
\[
\boxed{\mathbb E S(D,A)=n-\sum_{r=0}^n r\pi_r-\sum_{r=0}^n\frac{\pi_r}{\binom nr}\sum_{i=1}^k F_{n,r}(d_i).}
\]
Every placement with the inter-controller gaps as equal as possible maximizes this expected served count *simultaneously for every permutation-exchangeable failure law*: if \(n=kq+s\) with \(0\le s<k\), take \(k-s\) gaps of length \(q\) and \(s\) gaps of length \(q+1\), in any cyclic order. The corresponding optimum is obtained by substituting \((k-s)F_{n,r}(q)+sF_{n,r}(q+1)\) for the inner gap sum. When \(k=n\), the \(q+1\) term is absent.

The balancing conclusion is *sharp as a gap characterization* if \(\pi_2>0\): every optimal placement has exclusively gaps \(q\) and \(q+1\) (the order of these gaps need not be unique). This same characterization holds for fixed \(r\) failures whenever \(2\le r<k\). By contrast, a failure law supported on zero or one deleted vertex makes every placement equally good, showing the relevance of the strictness assumption.

For exactly two uniformly chosen deletions, the gap count simplifies to \(F_{n,2}(d)=\binom{d+1}{3}\), giving
\[
\mathbb ES(D,A)=n-2-\frac{\sum_i\binom{d_i+1}{3}}{\binom n2}.
\]
For independent deletion probability \(p\in(0,1)\) at each vertex, put \(u=1-p\) and define
\[
H_p(d)=u\sum_{t=1}^{d-1}(1-u^t)(1-u^{d-t}).
\]
Then \(\mathbb ES(D,A)=nu-\sum_iH_p(d_i)\), and the same balanced-gap characterization is necessary and sufficient for optimality. Both the exchangeable cardinality law and the independent-failure law are exact finite-\(n\) statements, not asymptotic approximations.

## Assumptions and scope

The network is the unweighted, undirected simple cycle; failure removes vertices, not merely edges, and deleted vertices do not count as served. Controller failures are not exempted. Exactly \(k\) controllers are placed before sampling the failure set; the failure law is permutation-invariant on all \(n\) vertices, with no dependence on \(D\). Such a law is a mixture of uniform fixed-cardinality laws, regardless of correlations among failures. There is no routing-distance, capacity, cost, or attack-adaptation constraint. The result optimizes the *expected number of served vertices*, not a worst-case attack or the entire distribution of served counts. For \(k=n\), all vertices have controllers and the sum of noncontroller outage penalties vanishes. For \(r=0\) or \(r=1\), the corresponding \(F_{n,r}\) is zero.

## Proof

**1. Local failure characterization.** Fix a non-controller vertex \(w\), and let \(u,v\) be its predecessor and successor controllers in cyclic order. Their clockwise distance is \(d\), and \(w\) is \(t\) edges clockwise from \(u\), for some \(1\le t\le d-1\). There are exactly two ways out of this controller-free gap: the clockwise and counterclockwise paths to the two boundary controllers. Vertex \(w\) is undeleted but unserved if and only if at least one of the \(t\) vertices on the first path (including its boundary controller but excluding \(w\)) is deleted **and** at least one of the disjoint \(d-t\) vertices on the second path is deleted. The two directions are the only simple paths to any controller. Every undeleted controller is automatically served, so only these interior vertices contribute to the outage count.

**2. Fixed-cardinality formula.** Conditional on \(|A|=r\), exchangeability gives a uniform \(r\)-subset. The number of such subsets that omit \(w\) and meet both disjoint blocking paths is, by inclusion-exclusion,
\[
\binom{n-1}{r}-\binom{n-1-t}{r}-\binom{n-1-d+t}{r}+\binom{n-1-d}{r}.
\]
Summing over interior \(w\) in one gap proves \(F_{n,r}(d)\). Summing over gaps and dividing by \(\binom nr\) gives the expected number of *undeleted yet unserved* vertices. The expected number deleted is \(\sum_r r\pi_r\); these two sets are disjoint. Subtracting both from \(n\) proves the displayed expectation formula. The formula also handles deletion of all controllers and the boundary cases \(r=0,1,n\), without replacing a missing controller.

**3. Exact discrete convexity.** Pascal's identity and a finite hockey-stick sum yield, for \(1\le d\le n-2\),
\[
F_{n,r}(d+1)-F_{n,r}(d)=\binom{n-1}{r}-\binom{n-1-d}{r}-d\binom{n-2-d}{r-1}.
\]
Consequently, for \(2\le d\le n-2\),
\[
\boxed{F_{n,r}(d+1)-2F_{n,r}(d)+F_{n,r}(d-1)=d\binom{n-d-2}{r-2}\ge0.}
\]
For \(r=0\) or \(1\), this is zero. Thus each \(F_{n,r}\), and every nonnegative mixture of the normalized functions, is discretely convex on feasible gap sizes. If two gaps have lengths \(a,b\) with \(a\ge b+2\), moving one vertex of the longer gap into the shorter gap does not increase the outage penalty. Iterating this transfer reaches the balanced gaps, proving simultaneous optimality for every exchangeable law.

**4. Equality.** For \(r=2\), the second difference is exactly \(d>0\); the first difference is strictly increasing, so every nonbalanced gap vector has a strictly improving transfer. If the law has \(\pi_2>0\), strict improvement survives the mixture. For fixed \(2\le r<k\), every second difference in the feasible gap range is strictly positive, since \(d\le n-k\) at a possible transfer boundary implies \(n-d-2\ge k-2\ge r-1\). Hence each optimizer has balanced gaps under either strictness condition, with no requirement that the cyclic *ordering* of the two allowed gap lengths be unique.

**5. Explicit specializations.** Direct summation gives \(F_{n,2}(d)=\sum_{t=1}^{d-1}t(d-t)=\binom{d+1}{3}\). Under independent failures, a vertex in position \(t\) remains present with probability \(u\), while the two blocking events have respective probabilities \(1-u^t\) and \(1-u^{d-t}\) and are independent. Summation gives \(H_p\). Alternatively, mix the exact fixed-cardinality formula with \(\pi_r=\binom nr p^r u^{n-r}\). Mixing the discrete second differences gives the strict formula
\[
H_p(d+1)-2H_p(d)+H_p(d-1)=d p^2u^d>0,
\]
proving the optimality and equality claims for independent failures.

## Verification

The standalone standard-library script `check_cycle.py` independently builds the surviving connected components of \(C_n-A\), enumerates every placement and fixed-size attack for \(3\le n\le9\), \(2\le k\le n\), and \(2\le r\le n\), and compares the exact integer sum against the gap formula. It also checks the global balanced-gap optimum and the characterization when \(k>r\). For \(4\le n\le31\), it checks the second-difference and two-failure identities by integer binomial coefficients. Run from this directory with `python3 check_cycle.py` (no third-party dependencies).

As a concrete instance, with \(n=12\), \(k=3\), and two uniformly deleted vertices, gaps \((4,4,4)\) yield expected served count \(105/11\); clustered gaps \((1,1,10)\) yield only \(15/2\). This is a genuine reliability improvement, not a consequence of changing the attack budget or removing attacks at controller locations.

## Relationship to prior work

Gutowski, Junosza-Szaniawski, Lauerbach, and Wolff (2026) study the same component-survival controller-placement payoff under worst-case pure and strategic mixed attacks, classify computational complexity, and give algorithms for restricted graph classes. Their explicit results concern worst-case attack/defense optimization and do not give the stated *all-cardinalities exchangeable failure law* or the gap-convexity formula on cycles. Pióro, Mycek, Tomaszewski, Junosza-Szaniawski, and Nogalski (2023) explicitly analyze a \(2\)-controller, \(2\)-attack cycle strategic mixed equilibrium, using antipodal controller pairs and a **nonuniform** family of attack pairs; that earlier antipodal observation is not a new claim here. An equilibrium for that specific strategically selected attack distribution neither supplies uniform fixed-size outage expectations for arbitrary \(k,r\), nor the universal optimality statement for all exchangeable failure laws. The present claim is the exact average-case all-budget gap law and robust balanced-gap optimization, not discovery of the controller model, cyclic layouts, or the general appeal of separated facilities.

## Limitations

The statement is specific to cycle graphs and exchangeable vertex-failure distributions. Nonexchangeable spatially correlated failures, heterogeneous vertex weights, edge failures, capacity limits, and adversarial failure laws depending on the controller placement may have different optimal configurations. Optimizing the expectation does not imply stochastic dominance of the entire served-count distribution. The cited earlier mixed-strategy cycle example is close enough to warrant further bibliographic priority review for additional unpublished or implicit special-case formulas. The enumerations are finite supporting checks; the proof, not finite enumeration, establishes the all-size claim. No external independent audit has been performed.

## References

1. G. Gutowski, K. Junosza-Szaniawski, A. Lauerbach, A. Wolff, *Modelling Network Resilience: The Complexity of Some Graph Division Games*, arXiv:2605.17572v1, first posted 2026-05-17, https://arxiv.org/abs/2605.17572.
2. M. Pióro, M. Mycek, A. Tomaszewski, K. Junosza-Szaniawski, D. Nogalski, *Finding Optimal Mixed Strategies in a Matrix Game Between the Attacker and the Network Operator*, RNDM 2023, DOI:10.1109/RNDM59149.2023.10293051.
3. K. Junosza-Szaniawski, D. Nogalski, *Game-theoretic Approach to Attack Planning and Controller Placement in Software Defined Networks*, ICMCIS 2023, DOI:10.1109/ICMCIS59922.2023.10253594 (related framework).
