# Random-greedy thinning and exact uniformity obstruction for clique coronas

## Finding
Let \(H\) be any finite simple graph with \(n\ge1\) labeled vertices and \(s\ge1\). Form the *clique corona* \(W_s(H)=H\odot K_s\): for each core vertex \(v\) add \(s\) private vertices, pairwise adjacent and adjacent to \(v\), with no edges from these private vertices to other clusters. Process the \(n(s+1)\) vertices in a uniformly random order, accepting a vertex exactly when it has no previously accepted neighbor. Write \(S\subseteq V(H)\) for the accepted core vertices, and put \(p=1/(s+1)\). Let \(g_{H[A]}(S)\) be the number of orders of \(A\) whose greedy independent set in the induced core graph \(H[A]\) equals \(S\), with \(g_\varnothing(\varnothing)=1\).

**Thinning law.** For each independent set \(S\subseteq V(H)\),
\[
\Pr(S)=\sum_{A\supseteq S} p^{|A|}(1-p)^{n-|A|}\frac{g_{H[A]}(S)}{|A|!}.
\]
Conditional on the selected core set \(S\), the private selection is an independent uniform choice from the \(s\) private vertices in each cluster outside \(S\). Thus each particular maximal independent set \(I\) with core set \(S\) satisfies
\[
\Pr(I)=s^{-(n-|S|)}\Pr(S).
\]
In particular, \(\Pr(S=\varnothing)=(s/(s+1))^n\). The entire greedy law is uniform over maximal independent sets **if and only if** \(H\) is edgeless.

**Exact bias for complete cores.** For \(H=K_n\), the total-variation distance between the greedy and uniform laws on maximal independent sets is
\[
\boxed{d_{\mathrm{TV}}\bigl(W_s(K_n)\bigr)=\frac{s}{s+n}-\left(\frac{s}{s+1}\right)^n.}
\]
It is positive whenever \(n\ge2\), and is zero for \(n=1\). For fixed \(s\), it is asymptotic to \(s/n\) as \(n\to\infty\).

## Assumptions and scope
All graphs are finite, simple, undirected and vertex-labeled. Integers satisfy \(n,s\ge1\). The greedy ordering is uniform among all \((n(s+1))!\) permutations; there are no ties. A maximal independent set of \(W_s(H)\) contains **exactly one** vertex in each core/private clique: at most one by the clique property, at least one because otherwise a private vertex could be added. Its selected core set is independent in \(H\), and conversely every independent core set and one private choice at each other cluster specifies a maximal independent set. The count is
\[
M_s(H)=\sum_{S\in\mathcal I(H)}s^{n-|S|},
\]
where \(\mathcal I(H)\) includes the empty independent set. No connectedness or degree restrictions on \(H\) are assumed.

## Proof
Use independent continuous, identically distributed uniform priorities for all vertices, equivalent almost surely to a uniform random ordering. For each cluster \(C_v\) of \(s+1\) vertices, let \(T_v\) be its earliest priority and let \(B_v\) indicate that its earliest vertex is the core vertex \(v\). The \(B_v\) are independent Bernoulli variables with success probability \(p=1/(s+1)\). Within a cluster the identity of its earliest member is independent of its minimum priority; the minima \(T_v\) are independent identically distributed continuous random variables across clusters. Consequently the relative order of the minima restricted to \(A=\{v:B_v=1\}\) is uniform, conditional on \(A\).

If \(B_v=0\), a private vertex arrives first and is accepted; it blocks its core vertex. If \(B_v=1\), the core vertex arrives before every private vertex in its cluster, and is accepted precisely when no previously accepted *adjacent core vertex* exists. Private vertices in other clusters have no influence on this decision. Thus the selected core set is exactly the greedy independent set of \(H[A]\) in the order of the cluster minima. Conditioning on \(A\) yields the thinning formula.

For every selected core set \(S\), exactly one private vertex is eventually accepted in each cluster outside \(S\): the first such private vertex, after the core is absent or rejected. Independently permuting private vertex labels within each cluster preserves the event that the selected core set is \(S\), and acts transitively on all \(s^{n-|S|}\) private-choice patterns. Therefore the conditional private-choice vector is uniform on the Cartesian product and its coordinates are independent. This proves the full terminal-set formula.

The event \(S=\varnothing\) occurs exactly when \(A=\varnothing\), because if \(A\ne\varnothing\), the core vertex having earliest cluster minimum within \(A\) is accepted. Hence the probability of any one specified private-only maximal independent set is \((s+1)^{-n}\), and there are exactly \(s^n\) such sets. If \(H\) has an edge, its family of independent sets is strictly smaller than the full power set; therefore
\[
M_s(H)=\sum_{S\in\mathcal I(H)}s^{n-|S|}<\sum_{S\subseteq V(H)}s^{n-|S|}=(s+1)^n.
\]
The uniform probability of the same private-only set would be \(1/M_s(H)>(s+1)^{-n}\), so the greedy law cannot be uniform. Conversely, if \(H\) is edgeless, the graph is a disjoint union of \(n\) copies of \(K_{s+1}\); each independently chooses its first-arriving vertex, so all \((s+1)^n\) maximal independent sets are equiprobable.

For \(H=K_n\), the independent core sets are empty or singletons; therefore \(M_s(K_n)=s^n+ns^{n-1}=s^{n-1}(s+n)\). By symmetry, each specified core vertex is accepted with probability \((1-(s/(s+1))^n)/n\). Each private-only output has probability \((s+1)^{-n}\); every remaining output (with one core vertex) has probability \((1-(s/(s+1))^n)/(n s^{n-1})\). For \(n\ge2\), the binomial theorem gives \((s+1)^n>s^{n-1}(s+n)\), so the private-only outputs lie below uniform probability and all other outputs above it. Total variation equals the total deficit on the \(s^n\) private-only outputs:
\[
\frac{s^n}{M_s(K_n)}-\frac{s^n}{(s+1)^n}=\frac{s}{s+n}-\left(\frac{s}{s+1}\right)^n.
\]
The same formula is zero for \(n=1\). Fixed-\(s\) asymptotics follow immediately.

## Verification
The standalone Python verifier `verify.py` enumerates all permutations of the actual clique-corona graph, constructs greedy outputs independently of the thinning formula, and compares exact rational probabilities with Bernoulli-minimum predictions. Six distinct pairs \((H,s)\) were tested: \(K_3\) and \(P_3\) with \(s=2\), and \(K_4,C_4,P_4,\overline K_4\) with \(s=1\). The test examines \(887{,}040\) vertex permutations in total and verifies every core-set probability and all conditional private-choice probabilities; complete-core total-variation formulas are also compared exactly. The saved output is `verification_output.txt`. These finite tests are corroboration; the proof above establishes all \(H,s\).

## Relationship to prior work
Fairfax-Ball, *Greedy Uniformity on Trees* (2026, arXiv:2610.02276v1), proves exact nonuniformity for nontrivial trees and gives full greedy output probabilities for an explicit mixed-spider family. Its tree analysis and random-order model motivate asking for full laws under a graph operation, but its theorems do not state the clique-corona thinning identity, nor do they classify uniformity for arbitrary base graphs \(H\). Krivelevich--Mészáros--Michaeli--Shikhelman (2020) develop general random-order greedy independent-set analysis focused on densities and local limits. The first-vertex recurrence and random-priority coupling themselves are established tools and are not claimed as novel. Public mathematical research records on threshold and chain graph greedy laws treat special graph classes; clique coronas of graphs containing an edge generally contain an induced \(P_4\), and for \(H=K_3\) contain triangles, so neither class supplies the full theorem. Search absence does not certify global novelty.

## Limitations
The formula reduces the clique-corona law to the greedy law of random induced subgraphs of the core; for an arbitrary core the formula need not yield a polynomial-time numerical evaluation. It does not imply uniqueness or worldwide novelty and makes no claim about other greedy conventions, weighted/nonuniform vertex priorities, or graphs other than clique coronas. Prior research on random sequential adsorption may contain equivalent thinning couplings under different terminology; this is an outstanding literature risk. Independent external validation has not been performed.

## References
- J. Fairfax-Ball, *Greedy Uniformity on Trees: Exact Obstruction and Near-Uniform Spiders*, arXiv:2610.02276v1, first version dated 2026-10-01, https://arxiv.org/abs/2610.02276v1.
- M. Krivelevich, T. Mészáros, P. Michaeli, C. Shikhelman, *Greedy Maximal Independent Sets via Local Limits*, AofA 2020, DOI:10.4230/LIPIcs.AofA.2020.20, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.AofA.2020.20.
