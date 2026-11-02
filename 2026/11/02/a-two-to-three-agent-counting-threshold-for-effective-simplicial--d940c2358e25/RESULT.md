# A two-to-three-agent counting threshold for effective simplicial secrecy events

## Finding

Fix a finite pure chromatic simplicial epistemic complex with facet set \(F\), and an agent-coloured vertex \(v\) of colour \(a\). Write \(\operatorname{St}(v)\) for its facet star and define the **effective secrecy-event capacity**
\[
E(v)=\#\{U\subseteq F:\operatorname{St}(v)\subseteq U\text{ and }U\text{ satisfies external uncertainty (SN) at }v\}.
\]
An event counted by \(E(v)\) is legally designatable as a secrecy event at \(v\) and, if assigned as the truth set of a propositional atom, can make that atom secret for the owner throughout \(\operatorname{St}(v)\).

**Theorem (sharp agent-count dichotomy).** With two agents, the capacity of every local state is computable in polynomial time by an explicit degree-product formula. With three agents, computing the same integer is \(\#\mathrm P\)-complete, already on pure complexes with two vertices of the owner's colour and a complete rectangular star at the distinguished owner vertex. The hardness reduction is parsimonious from counting edge covers of bipartite graphs, and remains valid for every fixed number of agents at least three.

Specifically, for two agents write the chromatic facets as edges of a simple bipartite graph \(G=(A\sqcup B,E_G)\), with \(v\in A\), and let \(d(b)\) be the degree of \(b\in B\). Then
\[
\boxed{E(v)=2^{\lvert E_G\rvert-\sum_{b\in N_G(v)}d(b)}\prod_{b\in N_G(v)}\bigl(2^{d(b)-1}-1\bigr).}
\]
An isolated local state is disallowed by purity. The expression is zero precisely when some neighbor of \(v\) has degree one.

For three agents, every finite bipartite graph \(H=(B\sqcup C,E_H)\) with both colour classes nonempty and at least one edge has an associated pure three-colour complex with exactly two owner-colour vertices \(v,w\), having facets
\[
\{(v,b,c): b\in B,c\in C\}\ \cup\ \{(w,b,c):(b,c)\in E_H\}.
\]
Its effective capacity at \(v\) equals the exact number of edge covers of \(H\), including zero when \(H\) has isolated vertices. The \(v\)-star is the full \(B\times C\) rectangle.

More generally, define the family of **external-witness sets**
\[
\mathcal H_v=\{\operatorname{St}(v_b(X))\setminus\operatorname{St}(v):X\in\operatorname{St}(v),\ b\ne a\},
\]
where \(v_b(X)\) is the unique vertex of colour \(b\) in facet \(X\). Then \(E(v)\) is exactly the number of subsets of \(F\setminus\operatorname{St}(v)\) meeting every member of \(\mathcal H_v\). This equivalence includes the case of empty witness sets (then \(E(v)=0\)).

## Assumptions and scope

The complex is finite, nonempty, downward-closed and pure over a fixed finite set of agents: every maximal face (facet) contains exactly one vertex of each agent colour, and every vertex occurs in a facet. Facets are distinct sets (there are no duplicated global states). Secrecy designations are arbitrary collections of facet events subject to Wang's (SN) external-uncertainty axiom. An event is **effective** at \(v\) if it includes the entire owner star; this reflects the knowledge conjunct in the secrecy truth clause. We count potential events over all truth sets, not only formulas definable under a single fixed valuation.

The input encoding lists the agent colours and all facets explicitly; complexity claims use this encoding. The theorem's \(\#\mathrm P\) classification concerns the function of the complex and designated vertex, not modal model checking or the validity problem. The two-agent formula applies to every such pure two-agent complex, not only a complete grid. The three-agent reduction works for every bipartite edge-cover instance with at least one edge; zero-edge instances can be decided directly and mapped to a fixed zero-capacity complex.

## Proof

**1. Outside-event witnesses.** Fix \(v\) and put \(S=\operatorname{St}(v)\). Any effective event \(U\) contains \(S\), and is determined uniquely by its outside complement \(W=F\setminus U\subseteq F\setminus S\). By Definition 3.8 of Wang, (SN) says that, for each \(X\in S\) and each other agent \(b\ne a\), some facet \(Y\notin U\) has the same \(b\)-coloured vertex as \(X\). This is equivalent to
\[
W\cap\bigl(\operatorname{St}(v_b(X))\setminus S\bigr)\ne\varnothing.
\]
Consequently the map \(U\mapsto F\setminus U\) is a bijection from effective secrecy events to hitting subsets for \(\mathcal H_v\). It also proves that every counted event satisfies (SN). Conversely, designate just that event at \(v\), with all other secrecy neighbourhoods empty; take a fresh atom \(p\) true precisely on \(U\). Since \(S\subseteq U\), the owner knows \(p\) on every facet in \(S\), so the truth clause makes \(S_a p\) hold throughout \(S\). Thus the capacity counts semantically usable events, not merely formal subsets.

**2. Two-agent product.** A pure two-colour complex is the downward closure of its bipartite edge set. For a vertex \(v\in A\), the sets in \(\mathcal H_v\) are precisely
\[
D_b=\{(u,b)\in E_G:u\ne v\},\qquad b\in N_G(v).
\]
They are pairwise disjoint because edges have exactly one \(B\)-endpoint. Their cardinalities are \(d(b)-1\). The remaining \(\lvert E_G\rvert-\sum_{b\in N_G(v)}d(b)\) edges are unconstrained. On \(D_b\) there are \(2^{d(b)-1}-1\) nonempty choices for \(W\); independently select any subset of the unconstrained edges. Multiplication gives the asserted formula, even with degree-one neighbours or disconnected components. All exponents are nonnegative because the full \(B\)-stars are disjoint. Degrees, sums and a binary integer of at most \(O(\lvert E_G\rvert)\) bits are computable in polynomial time.

**3. Three-agent parsimonious realization.** Take a finite simple bipartite graph \(H=(B\sqcup C,E_H)\) with nonempty sides and at least one edge. Form two agent-\(a\) vertices \(v,w\), agent-\(b\) vertices \(B\), agent-\(c\) vertices \(C\), and exactly the maximal three-vertex faces specified in the theorem. Their downward closure gives a pure complex, with every vertex in some facet. The owner star \(S\) is all \((v,b,c)\), while \(F\setminus S\) consists of the \(w\)-facets indexed by \(E_H\). For each \(b\in B\), the external-witness requirement at owner facets using \(b\) says that \(W\) includes at least one \((w,b,c)\) incident with \(b\). Analogously, for each \(c\in C\), it includes a facet incident with \(c\). Hence \(W\) meets all witness sets if and only if its indexed edges constitute an edge cover of \(H\). Distinct edge covers give distinct effective events, and conversely: this is a parsimonious polynomial-time translation. It still works when an isolated vertex forces both counts to zero.

**4. Complexity and additional agents.** Given an explicit list of facets, nondeterministically choose the indicator bits of \(U\) and verify \(S\subseteq U\) and all quantified (SN) clauses in deterministic polynomial time. The number of accepting branches is \(E(v)\), giving membership in \(\#\mathrm P\). Counting edge covers of bipartite graphs is \(\#\mathrm P\)-complete even in restricted planar biregular instances (Amarilli--Monet--Senellart, Theorem D.1). Step 3 therefore establishes \(\#\mathrm P\)-hardness for three agents. For every fixed larger agent set add one new, globally shared vertex of each additional colour to all facets. The added-agent external witness condition requires merely \(W\ne\varnothing\), already forced by the nonempty \(B\)- and \(C\)-witness families; the event count is unchanged. The reduction is still parsimonious.

## Verification

The standalone `checker.py` compares a direct enumeration of all candidate events against the degree product on 116 two-agent graphs and against the edge-cover count on 145 three-agent constructed graphs, for a total of 261 distinct small inputs. The checker was run with Python 3 and returned `ALL_CHECKS_OK two_agent_graphs=116 three_agent_graphs=145`. The direct verifier independently checks the quantified external-witness clause for every owner facet and other colour. These exhaustive finite tests are not a proof of the unbounded theorem; the bijections and the cited hardness theorem supply it. Run with `python checker.py`.

As a sample, with two owner-colour vertices and three opposite-colour vertices forming a complete \(2\)-by-\(3\) bipartite graph, the formula gives \(E(v)=1\) (one outside edge must be selected at each of three columns). In the three-agent construction from \(K_{2,2}\), there are seven edge covers and therefore exactly seven effective events.

## Relationship to prior work

Wang, *A Logic of Secrecy on Simplicial Models* (arXiv:2604.02673, first posted April 3, 2026), introduces the (SN) semantic condition, the secrecy truth clause and owner-local normalization (Definition 3.8, Definition 3.10, Lemma 3.12). This result assumes those definitions; it does not claim to invent the semantics or owner-local normalization. The inspected complete manuscript establishes soundness and completeness and gives finite illustrative instances, but does not present the general two-agent enumeration formula, the unrestricted witness-hypergraph correspondence as a capacity theorem, or a sharp two-versus-three-agent counting-complexity classification.

Amarilli, Monet and Senellart, *Conjunctive Queries on Probabilistic Graphs: Combined Complexity*, PODS 2017, Appendix D, Theorem D.1, proves the \(\#\mathrm P\)-completeness of counting bipartite edge covers. This is an explicitly used previous theorem: the new statement is a parsimonious realization of its instances as effective secrecy-event counts, together with the polynomial-time two-agent boundary. Generic hitting-set formulations and their counting complexity are also older mathematics; the semantic classification does not claim their novelty.

## Limitations

The tractable boundary depends on purity, explicit facets, a distinguished owner local state and Wang's (SN) axiom. Fixing a propositional valuation can leave fewer syntactically expressible truth sets than the capacity counts. The complexity bound addresses exact counting, not approximate counting or the minimization of secrecy neighbourhoods. Some older specialized neighborhood-logic or epistemic hypergraph literature could contain an equivalent classification; that historical priority has not been ruled out by finite searches. No independent validation has been performed.

## References

1. Shanxia Wang. *A Logic of Secrecy on Simplicial Models*. arXiv:2604.02673v1, April 3, 2026. https://arxiv.org/pdf/2604.02673. Definition 3.8, Definition 3.10, Lemma 3.12, Example 3.13.
2. Antoine Amarilli, Mikaël Monet and Pierre Senellart. *Conjunctive Queries on Probabilistic Graphs: Combined Complexity*. PODS 2017, pp. 217--232, DOI: 10.1145/3034786.3056121. Appendix D, Theorem D.1. https://pierre.senellart.com/publications/amarilli2017conjunctive.pdf.
