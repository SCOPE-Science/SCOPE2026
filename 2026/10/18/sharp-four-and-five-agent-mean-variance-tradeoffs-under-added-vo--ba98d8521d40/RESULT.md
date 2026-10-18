# Sharp four- and five-agent mean–variance tradeoffs under added voter-model links

## Finding

For the unbiased binary voter model with **link dynamics**, adding one undirected edge can make consensus faster on average but more variable, or slower on average but less variable. These two opposite interventions have different **sharp minimal** network orders: \(4\) and \(5\), respectively. Both thresholds apply to the attempted-update count and to a continuous-time link-update model with uniform total rate.

Precisely, let \(G\) be connected, simple and undirected, with \(n\ge2\) vertices; every vertex independently starts with opinion zero or one, with probability \(1/2\) each. Let \(K_G\) denote the number of attempted updates until first consensus, counting attempted updates that leave all opinions unchanged. In each attempt an edge is selected uniformly and one of its endpoints uniformly copies the other endpoint's opinion. For a missing edge \(e\), write \(\Delta f=f(G+e)-f(G)\).

* **Faster but less predictable:** the least possible order admitting \(\Delta\mathbb EK<0<\Delta\operatorname{Var}(K)\) is \(4\). At that order all qualifying additions join two leaves of a star (one edge orbit).
* **Slower but more predictable:** the least possible order admitting \(\Delta\mathbb EK>0>\Delta\operatorname{Var}(K)\) is \(5\). At that order precisely one graph/nonedge isomorphism class qualifies, represented by \(K_5\) missing edges \(01,24,34\), followed by insertion of \(01\).

For the associated continuous-time variable \(T_G\), defined by giving each attempted update an independent exponential waiting time of rate \(n\), the same sharp thresholds hold with \(K\) replaced by \(T\). Here and below exact statements average over both the initially random opinions and the update randomness.

## Assumptions and scope

A **test** is an unlabeled connected simple graph of order \(n\) together with one specified nonedge in a fixed canonical labeled representative. The census includes every nonedge of each representative; distinct tests may represent equivalent edge-orbits. We analyze all orders \(2\le n\le5\), yielding respectively \(1,2,6,21\) connected unlabeled graph classes and \(0,1,11,80\) tests. No other edge weights, external stubborn agents, or initial biases enter the model.

If \(K_G\) is the number of discrete attempts, independent exponential holding times give
\[
\mathbb E T_G=\frac{\mathbb EK_G}{n},\qquad
\operatorname{Var}(T_G)=\frac{\operatorname{Var}(K_G)+\mathbb EK_G}{n^2}.
\]
Thus the count and time variances must each be evaluated; their changes do not in general share signs merely because the corresponding means do.

## Proof

For a configuration \(s\in\{0,1\}^n\), let \(d_s(v)\) be the number of neighbors of \(v\) with an opposite opinion. In the continuous-time model, the rate of an actual flip at \(v\) is
\[
r_s(v)=\frac{n\,d_s(v)}{2|E(G)|}.
\]
If \(s^v\) flips coordinate \(v\), the transient rate matrix \(Q\), defined as the negative generator on nonconsensus states, satisfies \(Q_{ss}=\sum_v r_s(v)\) and \(Q_{s,s^v}\) receives \(-r_s(v)\) whenever \(s^v\) is transient. In the absorbing case there is no off-diagonal contribution. Opposite configurations \(s\) and \(1-s\) have identical hitting-time distributions; quotienting by this symmetry leaves \(2^{n-1}-1\) transient classes. Because \(G\) is connected, consensus is attained almost surely, making \(Q\) invertible.

First-step conditioning yields exact linear equations for the first two raw moments:
\[
Qm_1=\mathbf1,\qquad Qm_2=2m_1.
\]
The average over independent fair initial bits is
\[
\mu_G=\frac1{2^{n-1}}\sum_s m_1(s),\qquad
\sigma_G^2=\frac1{2^{n-1}}\sum_s m_2(s)-\mu_G^2,
\]
where the sum runs over one representative of each nonconsensus complementary pair, and the two consensus configurations contribute zero. All entries are rational; the included verifier solves both systems by fraction-preserving Gauss–Jordan elimination and independently checks the matrix equations by substitution.

**Complete finite census.** For each \(n=2,3,4,5\), the verifier iterates all \(2^{\binom n2}-1\) nonempty labeled simple graphs, discards disconnected graphs by breadth-first search, and collapses isomorphic graphs using the lexicographically minimal adjacency bitstring over all \(n!\) vertex permutations. Every possible connected unlabeled graph is consequently represented. For every missing edge of every representative, exact moment pairs are computed before and after addition, and both opposed-sign conditions are tested. The complete outcomes are:

| \(n\) | Connected classes | Edge-addition tests | \(\Delta\mu<0<\Delta\sigma^2\) | \(\Delta\mu>0>\Delta\sigma^2\) |
|---:|---:|---:|---:|---:|
| 2 | 1 | 0 | 0 | 0 |
| 3 | 2 | 1 | 0 | 0 |
| 4 | 6 | 11 | 3 | 0 |
| 5 | 21 | 80 | 0 | 1 |

Here \(\mu\) and \(\sigma^2\) refer to continuous time. The same counts hold for the update-count clock after applying the exact transformation \(\Delta\operatorname{Var}(K)=n^2\Delta\sigma^2-n\Delta\mu\). At order \(4\), the three tests are the three equivalent pairs of leaves of \(K_{1,3}\); at order \(5\), the single reverse test has no different labeled representative within the chosen exhaustive census. In particular both minimum-order and uniqueness assertions are established by a finite exact certificate, not by numerically sampling update paths.

**Explicit four-agent witness.** Set \(E(G)=\{01,02,03\}\) and add \(12\). The exact after-minus-before differences are
\[
\Delta\mathbb ET=-\frac1{68},\quad
\Delta\operatorname{Var}(T)=\frac{6257}{18496},
\]
while the count differences are
\[
\Delta\mathbb EK=-\frac1{17},\quad
\Delta\operatorname{Var}(K)=\frac{6325}{1156}.
\]

**Explicit five-agent witness.** Let \(G\) be \(K_5\) with exactly the three edges \(01,24,34\) removed, and add \(01\). Direct rational evaluation yields
\[
\Delta\mathbb ET=\frac{123113}{152733984}>0,\qquad
\Delta\operatorname{Var}(T)=-\frac{22700792201015951}{583191746712806400}<0,
\]
and
\[
\Delta\mathbb EK=\frac{615565}{152733984}>0,\qquad
\Delta\operatorname{Var}(K)=-\frac{22794809895876911}{23327669868512256}<0.
\]
These exact witnesses and the complete smaller-order census establish the theorem.

## Verification

Run `python verify_link_dynamics.py` using Python 3 and only its standard library. The verifier enumerates all \(6\) and \(21\) connected unlabeled graphs at orders \(4\) and \(5\), calculates every required mean and variance using exact `fractions.Fraction` arithmetic, checks both moment-system identities directly, counts every eligible edge addition, and asserts all eight witness rational equalities. Its completed execution printed `ALL EXACT CERTIFICATES PASSED`. The code, not execution output alone, provides the finite-search certificate; the proof above establishes the completeness of the search space.

## Relationship to prior work

Sood, Antal and Redner, *Voter Models on Heterogeneous Networks* (2008, arXiv first version 2007-12-27), define the link-dynamics update rule and study network-dependent consensus properties and mean-time scaling. Iwamasa and Masuda, *Networks Maximising the Consensus Time of Voter Models* (2014), give first-moment methods and exact/approximate mean consensus times for several update rules and network constructions. In particular, earlier mean-time edge-addition phenomena under link dynamics are **not** claimed here as new. Masuda, *Voter model on the two-clique graph* (2014), also studies mean consensus under link dynamics. The present comparison concerns two opposing **mean–variance** shifts and the jointly exhaustive, sharp minimal orders, which are not consequences of those works' reported first-moment results.

## Limitations

This is a finite-order theorem with a complete census only through five vertices. It does not classify larger networks, alternate voter-update clocks such as vertex updates or invasion dynamics, biased initial conditions, or fixed nonrandom initial patterns. Exact moment linear equations are standard and are used here as tools rather than claimed as an original identity. As with any literature comparison, an unlocated earlier classification could affect originality; independent bibliographic assessment is outstanding.

## References

1. V. Sood, T. Antal and S. Redner, *Voter Models on Heterogeneous Networks*, arXiv:0712.4288 (first posted 2007-12-27). https://arxiv.org/abs/0712.4288
2. Y. Iwamasa and N. Masuda, *Networks Maximising the Consensus Time of Voter Models*, arXiv:1404.6360 (2014). https://arxiv.org/abs/1404.6360
3. N. Masuda, *Voter model on the two-clique graph*, arXiv:1403.4763 (2014). https://arxiv.org/abs/1403.4763
