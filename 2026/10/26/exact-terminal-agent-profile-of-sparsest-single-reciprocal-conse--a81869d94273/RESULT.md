# Exact terminal-agent profile of sparsest single-reciprocal consensus networks

## Finding

Fix a labeled set \(V\) of \(n\ge3\) agents and a designated unordered pair \(\{p,q\}\). Consider loopless *simple* directed communication networks with precisely \(2(n-1)\) directed arcs, whose **only** directly reciprocal pair is \(p\leftrightarrow q\), and which ensure consensus in the rational-learning model under the sure-thing principle. Let \(F_n\) count these networks for fixed \(p,q\), and let \(R_{n,k}\) count them by the number \(k\) of noncore agents whose removal preserves the same properties with the remaining \(n-1\) agents and minimum \(2(n-2)\) arcs.

Define \(F_2=1\) and, for each \(m\ge3\),
\[
F_m=\sum_{r=1}^{m-2}(-1)^{r+1}\binom{m-2}{r}F_{m-r}\bigl((m-r)(m-r-1)\bigr)^r.
\]
Then for all \(n\ge3\) and \(1\le k\le n-2\),
\[
\boxed{R_{n,k}=\binom{n-2}{k}\sum_{j=0}^{n-2-k}(-1)^j\binom{n-2-k}{j}F_{n-k-j}\bigl((n-k-j)(n-k-j-1)\bigr)^{k+j}.}
\]
Moreover \(\sum_{k=1}^{n-2}R_{n,k}=F_n\), no such network has zero terminal-removable noncore agents, and precisely \(2^{n-2}\) networks have all \(n-2\) noncore agents terminal-removable. The exact profiles \((R_{n,1},\ldots,R_{n,n-2})\) for \(n=3,4,5,6\) are \((2)\), \((16,4)\), \((312,192,8)\), and \((11520,12192,1664,16)\), respectively.

The scalar totals \(F_n=1,2,20,512,25392,\ldots\) beginning at \(n=2\) **already occur** as OEIS A103353. The terminal-agent refinement, rather than that pre-existing integer sequence, is the claimed contribution.

## Assumptions and scope

All directed graphs are finite, labeled, loopless, and allow at most one arc of a given direction between each distinct pair. One reciprocated dyad means *both* arcs joining those two agents are present. The distinguished dyad \(p\leftrightarrow q\) is fixed in advance, so the formulas do not add the factor \(\binom n2\) that counts possible dyads. Consensus uses the model and quantifiers of Sugiura, *Learning to Agree under Pseudo-Reciprocity*, arXiv:2608.22234: for all decision environments obeying the sure-thing principle and all admissible initial profiles, terminal communication leads to agreement. Corollary 2 of that paper says that with exactly one direct mutual pair, consensus holds exactly when the digraph admits a *single-core order*: first the mutual dyad, then the other agents in some order, each having at least one inbound arc from the previous core and at least one outbound arc to it. Proposition 2 gives the minimum arc count \(2(n-1)\).

At the minimum arc count, those at-least-one conditions become exactly one inbound and exactly one outbound arc added at every stage. Their old endpoints must differ, or a second directly mutual dyad would appear. Thus networks here are precisely the distinct, un-ordered directed graphs obtainable from the initial reciprocal dyad by adding each new agent with \(u\to v\) and \(v\to w\), where \(u\ne w\) are older agents. An attachment order is a *witness*, not part of the counted object; different orders can yield the same graph.

A noncore vertex is *terminal-removable* exactly when its indegree and outdegree in the full graph are both one. Its unique inbound and outbound neighbors are automatically distinct, because there is no second mutual dyad.

## Proof

**1. A terminal agent can always be postponed.** Choose a single-core construction of a given graph. If a noncore vertex \(v\) has final indegree and outdegree both one, those arcs are exactly the two introduced when \(v\) joined the core: every later attachment to \(v\) would raise at least one of its degrees. No later agent attaches to \(v\). Moving \(v\) to the final position therefore preserves all other attachment requirements and leaves exactly its two original arcs to distinct earlier vertices. Deleting \(v\) yields a valid smaller minimum-link single-core network. Conversely, deleting an agent and losing precisely two arcs while preserving a minimum-link network forces its indegree-plus-outdegree to equal two; the original single-core construction ensures each noncore agent has at least one of each, so both equal one.

**2. Several terminal agents can be postponed together.** Two distinct terminal-removable noncore vertices cannot be adjacent by an arc: whichever was added later would have increased an in- or outdegree of the earlier vertex beyond one. Consequently, for any set \(S\) of terminal-removable vertices, no arcs join members of \(S\), and none of the other agents' required attachments use a member of \(S\) (because those attachments would increase that member's degree). One may therefore place all members of \(S\) after every other agent in any order, and delete them simultaneously. The remaining graph is again in the same family, now on \(n-|S|\) vertices.

Conversely, start with any valid graph on the \(n-r\) remaining labeled vertices, with the same fixed reciprocal dyad, and add each of \(r\) specified distinct outside vertices using exactly two directed arcs to the remaining old vertices: one inbound from an old vertex \(u\), one outbound to a different old vertex \(w\). There are \((n-r)(n-r-1)\) choices of ordered pair \((u,w)\) for each added vertex, independently. The resulting network is a valid minimum-link consensus network in which all \(r\) specified vertices are terminal-removable; this construction is bijective because deleting those labeled vertices recovers the old network and their two unique arcs.

**3. Intersection counts.** Let \(A_v\) be the class of valid networks where noncore agent \(v\) is terminal-removable. For any fixed \(r\)-element subset \(S\subseteq V\setminus\{p,q\}\), the bijection in Step 2 proves
\[
\left|\bigcap_{v\in S} A_v\right|=F_{n-r}\bigl((n-r)(n-r-1)\bigr)^r.\tag{1}
\]
Every graph has a terminal agent: take the last agent of any single-core order. Inclusion-exclusion over the \(n-2\) noncore agents therefore yields, for \(n\ge3\),
\[
F_n=\sum_{r=1}^{n-2}(-1)^{r+1}\binom{n-2}{r}F_{n-r}\bigl((n-r)(n-r-1)\bigr)^r.
\]
This, together with \(F_2=1\), determines all the totals.

**4. Exact distribution.** Fix \(k\) noncore vertices required to be terminal-removable. Among the remaining \(n-2-k\), use inclusion-exclusion to demand that none are terminal-removable. Summing (1) over the fixed size-\(k\) sets produces the boxed formula. Equivalently, writing \(I_{n,r}\) for the total count of incidences between a network and an \(r\)-set of its terminal-removable agents,
\[
I_{n,r}=\binom{n-2}{r}F_{n-r}\bigl((n-r)(n-r-1)\bigr)^r=\sum_{k=r}^{n-2}\binom{k}{r}R_{n,k},
\]
and ordinary binomial inversion gives the same result. The case \(k=n-2\) forces all noncore vertices to attach directly to the distinguished dyad, with one of two possible orientations per vertex, giving \(R_{n,n-2}=2^{n-2}\). The recurrence also proves every \(R_{n,k}\) is a nonnegative integer because it counts a set of graphs, not merely because of numerical experimentation.

## Verification

The included standalone \(`verification.py`\) uses Python's standard library and separately implements (i) the recurrence and histogram, (ii) generation of *distinct graph edge sets* by all admissible attachment orders, (iii) exhaustive enumeration of fixed-dyad directed edge sets at orders three through five followed by an independent reverse-deletion membership test. Exact integer outputs match for each size examined. Generating graphs on six vertices yields \(25392\) distinct edge sets and exact histogram \((11520,12192,1664,16)\), also matching the formula. The proof, not these finite experiments, establishes the result for all orders.

## Relationship to prior work

Sugiura (2026, Corollary 2 and Proposition 2) establishes the single-core characterization and sharp number of arcs but does not provide a refined enumeration by terminal-removable agents. The *unrefined* sequence \(F_2,F_3,\ldots\) is **not new**: it is precisely OEIS A103353, recorded since 2005, and arises in Priez and Virmaux's (2014/2015) generalized-parking-functions enumeration for \(\chi(m)=m^2+m\). In particular, the unrefined totals and their recurrence are excluded from any novelty claim. Neither the cited OEIS entries A103353/A103244 nor the inspected generalized parking-functions work assigns those terms to minimum-link one-dyad consensus networks or tabulates this graph-theoretic terminal-removable histogram. The numbers \(R_{n,k}\) are a distinct, network-dependent refinement and characterize the number of possible final agents in reverse construction. General strong-digraph enumeration counts substantially larger families without the one-mutual-pair, consensus, and minimum-arc constraints.

## Limitations

The claim is only for simple directed graphs with a fixed unique mutual dyad and the exact sharp link budget. It does not describe networks with additional links, multiple reciprocated pairs, or general stochastic agreement speeds. The count of possible last agents measures combinatorial reverse-construction flexibility, not the probability of successful learning under weaker decision assumptions. The parking-function sequence coincidence raises a priority risk that more refined equivalent formulas exist in other combinatorial languages; no absence-of-prior-results assertion is made. The finite checker provides corroboration, not an all-orders certificate.

## References

1. S. Sugiura, *Learning to Agree under Pseudo-Reciprocity*, arXiv:2608.22234 (first public 23 August 2026), particularly Section 4.2 and Corollary 2/Proposition 2. https://arxiv.org/abs/2608.22234
2. OEIS Foundation, A103353, *First column of triangular matrix A103244*, https://oeis.org/A103353 (existing unrefined sequence).
3. OEIS Foundation, A103244, *Inverse-matrix triangle*, https://oeis.org/A103244.
4. J.-B. Priez and A. Virmaux, *Non-commutative Frobenius characteristic of generalized parking functions: Application to enumeration*, arXiv:1411.4161 (2014/2015), https://arxiv.org/abs/1411.4161.
5. X. Pérez-Giménez and N. Wormald, *Asymptotic enumeration of strongly connected digraphs by vertices and edges*, arXiv:1005.1285 (2010), https://arxiv.org/abs/1005.1285.
