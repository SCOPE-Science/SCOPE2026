# Strict connectivity-event correlations in weighted cactus forests

## Finding

Let \(G=(V,E)\) be any finite, connected, simple **cactus graph**: every biconnected block is either a single edge or a simple cycle. Give each edge an arbitrary strictly positive finite weight \(w_e\). Sample an acyclic spanning edge set \(F\subseteq E\) with probability
\[
\mathbb P_w(F)=\frac{\prod_{e\in F}w_e}{\sum_{H\subseteq E:\ H\text{ acyclic}}\prod_{e\in H}w_e}.
\]
For distinct vertices \(u,v\), let \(A_{uv}\) be the event that \(u\) and \(v\) belong to the same connected component of \((V,F)\). Denote by \(\mathcal B(u,v)\) the set of blocks traversed by the unique \(u\)-to-\(v\) path in the vertex–block incidence tree of \(G\).

**Theorem.** For every two unordered vertex pairs \(\{u,v\}\), \(\{s,t\}\) with \(u\ne v\) and \(s\ne t\), without requiring the pairs to be disjoint,
\[
\operatorname{Cov}_w(\mathbf1_{A_{uv}},\mathbf1_{A_{st}})\ge0,
\]
with the sharp dichotomy
\[
\operatorname{Cov}_w(\mathbf1_{A_{uv}},\mathbf1_{A_{st}})>0
\quad\Longleftrightarrow\quad
\mathcal B(u,v)\cap\mathcal B(s,t)\ne\varnothing.
\]
When the two block routes are disjoint, the connection events are exactly independent. The result holds simultaneously for every finite cactus and every vector of positive edge weights; it establishes the cactus case of the 2026 vertex-connectivity correlation conjecture of Çiçeksiz and Ravichandran.

## Assumptions and scope

A spanning forest here need not be connected or have a prescribed number of edges; \(F\) includes every vertex and may contain isolated vertices. The weights are attached to present edges only and need not be equal. For a bridge block \(B\), its local law is a Bernoulli edge with probability \(w_e/(1+w_e)\). For a cycle block, every proper subset of its edges is allowed, including the empty subset. A cactus has no cycles spanning different blocks. The vertex–block incidence tree has one node for every original vertex and one for every block, joined by incidence; its unique path specifies both the traversed blocks and the distinct entry/exit vertices within each traversed block.

## Proof

### 1. Factorization and connection along block routes

Every cycle of a cactus is wholly contained in one cycle block. Thus \(F\) is acyclic precisely when its edge restriction to each cycle block omits at least one edge; bridge restrictions are unrestricted. Since the blocks partition \(E\), the forest partition function factorizes over blocks, and random edge restrictions to distinct blocks are independent.

Fix distinct vertices \(u,v\). In the block-incidence tree, the path from \(u\) to \(v\) visits a unique sequence of blocks. For each traversed block \(B\), let \(L_{B,uv}\) be the event that the entry and exit vertices on this path are connected by edges of \(F\cap E(B)\). By the absence of any alternate route around a block, 
\[
\mathbf1_{A_{uv}}=\prod_{B\in\mathcal B(u,v)}\mathbf1_{L_{B,uv}}.
\]
The same holds for \(s,t\). Consequently,
\[
\mathbb P(A_{uv}\cap A_{st})
=\prod_B \mathbb P(L_{B,uv}\cap L_{B,st}),\qquad
\mathbb P(A_{uv})\mathbb P(A_{st})
=\prod_B \mathbb P(L_{B,uv})\mathbb P(L_{B,st}),
\]
where a pair's local event is taken to be certain at blocks it does not traverse. Every local connection event on a traversed block has probability strictly between zero and one. It remains to show that two local terminal-connection events in one cycle have strictly positive covariance. For a bridge shared by both routes, the local events coincide and have strictly positive variance.

### 2. A weighted cycle lemma

Consider a simple cycle, with independent Bernoulli edge indicators of opening probabilities \(p_e=w_e/(1+w_e)\). The forest law on that cycle is exactly this Bernoulli product law conditioned on at least one edge being closed. Mark either two, three, or four distinct terminal vertices as appropriate. Divide the cycle into the nonempty consecutive edge arcs between these marked vertices. For an arc \(J\), put
\[
q_J=\prod_{e\in J}p_e,\qquad x_J=\frac{1-q_J}{q_J}>0.
\]
Call an arc **failed** when at least one of its edges is closed. Before conditioning, different arc-failure indicators are independent, and after conditioning on at least one failure, any nonempty set \(S\) of failed arcs has unnormalized mass \(\prod_{J\in S}x_J\). Connectivity between two terminals means that all failed arcs lie entirely in one of the two complementary arcs between those terminals.

For the cases below, let \(Z\) be the sum of these masses over all nonempty failed-arc sets; let \(U,V,W\) be the corresponding unnormalized masses of the first connection event, the second event, and their intersection. The covariance is exactly \((WZ-UV)/Z^2\). We prove \(WZ-UV>0\) in every case.

**Three distinct terminals with one shared terminal.** In cyclic order \(1,2,3\), write the odds for arcs \(1\!\to\!2\), \(2\!\to\!3\), \(3\!\to\!1\) as \(a,b,c>0\), and take the pairs \((1,2)\), \((1,3)\). Write \(L=a+b+c\). Directly enumerating which failed arcs can belong to one of the two complementary terminal routes gives
\[
Z=(1+a)(1+b)(1+c)-1,\quad U=L+bc,\quad V=L+ab,\quad W=L.
\]
Therefore
\[
WZ-UV=ac(a+b+c+ab+bc)>0.
\]
Every three-terminal configuration with a shared endpoint reduces to this case by relabeling and reversing cyclic orientation.

**Four distinct terminals, nonalternating pairs.** In cyclic order \(1,2,3,4\), label arc odds \(a,b,c,d>0\) consecutively, and take pairs \((1,2)\), \((3,4)\). Put \(L=a+b+c+d\). The admissible failed-arc sets give
\[
\begin{aligned}
Z&=(1+a)(1+b)(1+c)(1+d)-1,\\
U&=L+bc+bd+cd+bcd,\\
V&=L+ab+ad+bd+abd,\\
W&=L+bd.
\end{aligned}
\]
Expansion and factorization yield
\[
WZ-UV=ac\big[(1+b)(1+d)(1+a+c)-1\big]>0.
\]
The alternative nonalternating pairing is the same case after a cyclic relabeling.

**Four distinct terminals, alternating pairs.** Take pairs \((1,3)\), \((2,4)\) in cyclic order. Let \(L=a+b+c+d\) and \(T=abc+abd+acd+bcd\). This time
\[
U=L+ab+cd,\qquad V=L+bc+ad,\qquad W=L,
\]
with the same \(Z\). Straight expansion gives
\[
WZ-UV=L(ac+bd)+LT-(ab+cd)(bc+ad)+Labcd.
\]
Here \((ab+cd)(bc+ad)=ab^2c+a^2bd+bc^2d+acd^2\). Each of these four positive monomials already occurs in \(LT\) with coefficient at least one. Thus \(LT-(ab+cd)(bc+ad)\) is a polynomial with nonnegative coefficients, and \(L(ac+bd)>0\) proves strict positivity.

**Identical terminal pairs.** Their indicators coincide. Strictly positive weights give positive probabilities of both connection and disconnection, so their covariance is their strictly positive variance.

These cases exhaust all possible two nontrivial terminal pairs on one cycle, proving the weighted cycle lemma.

### 3. Assemble the cactus

The local lemma and the bridge observation show, for every block \(B\),
\[
\mathbb P(L_{B,uv}\cap L_{B,st})\ge
\mathbb P(L_{B,uv})\mathbb P(L_{B,st}),
\]
with strict inequality if and only if both block paths traverse \(B\). All factors on the right are positive. Taking products across independent blocks gives the claimed nonnegative global covariance, and strictness if at least one block is shared. If no block is shared, each event depends on a disjoint collection of independent block restrictions, proving exact independence. This finishes the proof. \(\square\)

## Verification

Run `python3 checker.py` with Python 3 and its standard library. The checker independently enumerates the nonempty failed-arc patterns for the three-terminal, crossing four-terminal, and noncrossing four-terminal algebraic identities at exact rational odds. It also enumerates all acyclic edge subsets of seven concrete weighted cactus graphs (cycles, bridges, joined cycles, and cycle chains), computes their full weighted connection indicators, and verifies the sign and precise shared-block equality criterion for every ordered pair of vertex pairs in each example. It passes 4,152 exact integer/rational assertions. These finite checks corroborate algebra and examples but are not used as infinite proofs; Steps 1–3 establish the universal statement.

## Relationship to prior work

Çiçeksiz and Ravichandran (2026), Conjecture 6.2, posit nonnegative covariances of arbitrary two vertex-pair connection events in multivariate arboreal gas. Their Proposition 6.1 proves only a large-equal-fugacity asymptotic in a particular edge-deletion setup; its hypotheses do not yield the all-positive-weight cactus result. The present result establishes a genuine structural graph class at all strictly positive weight vectors, with a strictness/independence classification. Erickson (2012) proves the Rayleigh (negative **edge-occupancy** correlation) property for spanning forests on series-parallel graphs. Even though cacti are series-parallel, that statement concerns different random events and supplies no stated nonnegative vertex-connectivity covariance or equality characterization.

## Limitations

The theorem does not apply to arbitrary series-parallel graphs or graphs with overlapping cycle blocks; nor does it address the random-cluster measures with \(0<q<1\) directly. The proof requires finite positive weights; limiting zero or infinite weights may eliminate strictness. Publication priority against formulations under graph-block random-cluster decompositions or other older equivalences remains a residual literature risk. No independent audit has been performed.

## References

1. R. Altar Çiçeksiz and M. Ravichandran, *Negative Correlation for Forests and the \(q<1\) Random-Cluster Model* (2026), arXiv:2610.00549v1, especially Proposition 6.1 and Conjecture 6.2 (publicly posted 2026-09-30).
2. A. Erickson, *Sums of squares and negative correlation for spanning forests of series parallel graphs*, *Australasian Journal of Combinatorics* **52** (2012), 75–87.
