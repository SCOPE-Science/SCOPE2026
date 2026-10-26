# Sharp fair-percolation isolation–edge covariance bounds on trees and their degree-five extremizers

## Finding

Let \(T\) be any finite simple tree on \(n\ge 2\) vertices. Retain each of its edges independently with probability \(1/2\). Write \(I\) for the number of isolated vertices of the resulting spanning forest (all original vertices remain present), \(M\) for its number of retained edges, and \(d_v\) for the degree of \(v\) in the original tree. Then
\[
\operatorname{Cov}(I,M)=-\frac12\sum_{v\in V(T)}\frac{d_v}{2^{d_v}}.
\]
For every such tree, the sharp lower bound is
\[
-\frac n4\leq\operatorname{Cov}(I,M),
\]
with equality exactly for the path (up to isomorphism). The sharp upper bound for \(n\ge5\), writing \(B=n-2\) and \((\delta_0,\delta_1,\delta_2,\delta_3)=(0,3,2,1)\), is
\[
\operatorname{Cov}(I,M)\leq-\frac n4+\frac{11B-\delta_{B\bmod 4}}{256}.
\]
Equality holds exactly for the following degree multisets (with every degree not listed equal to one), where the indicated counts are required to be nonnegative integers:

* If \(B\equiv0\pmod4\): \(B/4\) vertices of degree five.
* If \(B\equiv1\pmod4\): either one vertex of degree six together with \((B-5)/4\) of degree five, or three vertices of degree four together with \((B-9)/4\) of degree five. The latter family is possible only if \(B\ge9\).
* If \(B\equiv2\pmod4\): two vertices of degree four together with \((B-6)/4\) of degree five.
* If \(B\equiv3\pmod4\): one vertex of degree four together with \((B-3)/4\) of degree five.

Every listed degree multiset is realized by at least one tree, and **every** tree with that multiset attains equality. In the remaining small orders, \(n=2,3\) have the path as both extremizers and \(n=4\) has the three-leaf star as the unique upper-bound extremizer, with covariance \(-15/16\). Thus the upper-bound extremizers are not eventually paths or stars: degree-five hubs dominate, with prescribed small residue corrections. Along \(n=4m+2\), the maximizing trees have exactly \(m\) degree-five vertices and all other vertices leaves.

## Assumptions and scope

Only independent, identically distributed, fair **bond** percolation on a fixed tree is considered. Isolated vertices retain their identities after the edges are deleted. The optimization is over all unrooted simple trees of a fixed order \(n\). There is no assumption about a random tree distribution. The main formula is exact for every \(n\ge2\); the residue-class classification applies for every \(n\ge5\).

## Proof

**1. Covariance identity.** For a vertex \(v\), let \(J_v\) be its isolated-vertex indicator. All incident edges must be absent, hence \(\mathbb E J_v=2^{-d_v}\). Conditional on \(J_v=1\), the \(n-1-d_v\) nonincident edges remain independent fair edges, giving \(\mathbb E[M\mid J_v=1]=(n-1-d_v)/2\); unconditionally \(\mathbb E M=(n-1)/2\). Therefore
\[
\operatorname{Cov}(J_v,M)=-\frac{d_v}{2}\,2^{-d_v}.
\]
Sum this identity over vertices to obtain the first formula.

**2. Degree budget.** Define \(g(d)=1/2-d/2^d\) for \(d\ge3\). Degrees one and two both contribute exactly \(1/2\) to \(\sum_v d_v/2^{d_v}\); thus
\[
\operatorname{Cov}(I,M)=-\frac n4+\frac12\sum_{v:d_v\ge3}g(d_v).
\]
All \(g(d)>0\). The minimum is \(-n/4\), with equality exactly when all degrees are at most two, i.e. \(T\) is a path.

Write \(u\) for the number of degree-two vertices and let the degrees at least three be \(h_1,\dots,h_k\). The tree degree-sum identity \(\sum_v(d_v-2)=-2\) yields the exact degree-budget constraint
\[
u+\sum_{j=1}^k(h_j-1)=n-2=:B.
\]
Conversely, every choice of nonnegative \(u\) and degrees \(h_j\ge3\) satisfying that identity can be completed by \(n-k-u\) leaves to a tree degree sequence: the total degrees then equal \(2n-2\), and the standard Prüfer-sequence construction realizes it. Accordingly, maximizing covariance is exactly an unbounded integer knapsack problem with item cost \(h-1\), profit \(g(h)\), and unused budget represented by degree-two vertices.

**3. Strict exchanges.** For degrees three through six, profits in units of \(1/32\) are respectively \(4,8,11,13\), with respective costs \(2,3,4,5\). No maximizing configuration for \(B\ge3\) contains degree seven or more: any single such hub costs at least six and has profit strictly less than \(1/2\), whereas two degree-four hubs cost six and have profit exactly \(1/2\). Other strictly improving, cost-preserving replacements are:
\[
(3,3)\to(5),\quad(3,4)\to(6),\quad(3,5)\to(4,4),\quad(3,6)\to(4,5),
\]
\[
(4,4,4,4)\to(5,5,5),\qquad(6,6)\to(4,4,5).
\]
Here each parenthesis lists hub degrees, not vertex labels, and every arrow preserves the total \(\sum(h-1)\) while increasing \(\sum g(h)\). These exchanges imply at most one degree-three hub, at most three degree-four hubs, and at most one degree-six hub. A remaining degree-three hub cannot coexist with any other hub; if alone and \(B\ge3\), at least one degree-two budget unit remains, allowing strict improvement by upgrading degree three to four. Thus there are no degree-three hubs in any optimum for \(B\ge3\).

Nor can any optimum for \(B\ge3\) contain degree-two vertices. If \(u\ge2\), inserting a degree-three hub, using two units, strictly increases profit. If \(u=1\), at least one hub exists (otherwise \(B=1\)); a degree-four hub can be upgraded to degree five, a degree-five hub to degree six, or a degree-six hub replaced by two degree-four hubs, each using the spare unit and strictly increasing profit. Therefore \(u=0\).

**4. Residue optimization.** Every optimum with \(n\ge5\) consequently has \(a\) degree-four hubs, \(b\) degree-five hubs, and \(c\) degree-six hubs, where
\[
3a+4b+5c=B,\qquad 0\le a\le3,\qquad 0\le c\le1.
\]
Its profit is \(P=(8a+11b+13c)/32\), whence the crucial exact identity
\[
128P=11B-a-3c.
\]
At fixed \(B\) we must therefore minimize \(a+3c\), subject to the displayed cost equation. Modulo four, \(3a+c\equiv B\pmod4\). Checking the eight possible pairs \((a,c)\) gives minima \(\delta_0=0\), \(\delta_1=3\), \(\delta_2=2\), and \(\delta_3=1\), attained respectively at \((0,0)\); \((0,1)\) or \((3,0)\); \((2,0)\); and \((1,0)\). The requirement \(b\ge0\) removes \((3,0)\) for \(B=5\), and the other selected pairs are feasible for every \(B\ge3\) of their respective residue classes. Substituting \(P=(11B-\delta_{B\bmod4})/128\) into the covariance formula proves the upper bound and exhaustive equality classification. When \(n=4\), the only degree possibilities are those of the path and the three-leaf star; the star has one degree-three hub, yielding covariance \(-15/16\). The cases \(n=2,3\) are immediate.

## Verification

The standalone standard-library script `verify.py` separately enumerates every attainable tree degree multiset for \(2\le n\le16\) and checks the sharp extrema and equality cases by exact rational arithmetic. For \(2\le n\le10\), it additionally constructs a representative tree for **every** degree multiset via a Prüfer word and explicitly averages over all \(2^{n-1}\) edge-retention patterns to reproduce the covariance identity; this is exhaustive over degree profiles but not over all labeled trees, which is sufficient because the proof shows covariance depends only on the profile. A separate exact dynamic program verifies the residue formula for every \(5\le n\le120\). Running `python verify.py` prints `VERIFY_OK`; these finite checks supplement, and do not replace, the preceding all-order proof.

## Relationship to prior work

Berzunza, Cai and Holmgren (2019, arXiv:1902.08109) study bond-percolation giant-cluster fluctuations on random split trees and regular trees, mainly in an order-dependent supercritical regime. Betken (2019, arXiv:1910.02668) gives isolated-vertex count central limit theorems for a distinct growing preferential-attachment random graph. Neither study's examined main definitions/results supplies fixed-host, fair-percolation covariance extrema across arbitrary trees. The covariance identity itself uses elementary independent-edge conditioning; the contribution assessed here is the sharp all-order **optimization and complete residue-dependent extremizer classification**, not the known definition of percolation or the general principle of conditioning. Generic degree-index optimization techniques can potentially be adapted to the resulting knapsack objective; no claim that the optimization machinery is globally new is made.

## Limitations

No statement is made for edge-retention probabilities other than \(1/2\), for non-tree host graphs, or for asymptotic percolation models with a random host. The proof classifies equality by **degree multiset**, not the isomorphism types of every maximizing tree; many nonisomorphic maximizing trees share a degree multiset. Historical-priority uncertainty remains, especially generic graph-degree-index literature; absence of a retrieved matching result is not proof that none exists.

## References

1. Gabriel Berzunza, Xing Shi Cai and Cecilia Holmgren, *The fluctuations of the giant cluster for percolation on random split trees*, initial public version 2019-02-21, arXiv:1902.08109, https://arxiv.org/abs/1902.08109.
2. Carina Betken, *A central limit theorem for the number of isolated vertices in a preferential attachment random graph*, initial public version 2019-10-07, arXiv:1910.02668, https://arxiv.org/abs/1910.02668.
