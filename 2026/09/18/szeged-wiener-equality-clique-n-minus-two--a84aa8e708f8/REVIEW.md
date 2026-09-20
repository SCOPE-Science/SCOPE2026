# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof is self-contained after the standard definitions of the Wiener and Szeged indices. Fixing an \((n-2)\)-clique \(Q\) reduces the graph to four adjacency types according to the two vertices outside \(Q\). The Szeged contribution of every edge is then determined by its type.

Three exact formulas are obtained, according to whether the two outside vertices are adjacent and, when they are nonadjacent, whether they have a common neighbor in \(Q\). The formulas were algebraically simplified before the equality equation was solved. The remaining Diophantine analysis is elementary and separates all parameter ranges. For \(n\ge10\), the adjacent case yields exactly the Zhang–Li family plus one order-10 graph; the nonadjacent case yields no equality graph.

The two stated equality constructions can also be checked directly from the formulas. In the Zhang–Li family the parameters are
\[
(a,b,c,d)=(1,1,n-4,0),
\]
which gives \(\eta=2n\). For the additional graph \(J_{10}\), the parameters are, up to exchanging \(x,y\),
\[
(a,b,c,d)=(0,1,6,1),
\]
which gives \(\eta=20\).

No computational verification is required for the proof.

## Originality

The closest direct source is Zhang and Li, arXiv:2609.20025v1, submitted 17 September 2026. Their Theorem 6 proves the strengthened BKLPS lower bound \(\eta(G)\ge2n\); their Problem 7 asks for a necessary and sufficient description of equality; and their Lemma 8 supplies one equality graph \(G_n\) for every \(n\ge10\). The paper explicitly remarks that this sufficient construction is not necessary, but it does not classify the high-clique regime or state the order-10 graph \(J_{10}\).

The earlier Bonamy–Knor–Lužar–Pinlou–Škrekovski paper, arXiv:1602.05184 / Applied Mathematics and Computation 312 (2017), characterizes equality for the older lower bound \(2n-6\), not equality at \(2n\).

Searches for exact and synonymous formulations were made around the phrases “Szeged–Wiener gap”, “eta(G)=2n”, “clique number”, “clique of order n-2”, “diameter two”, “graph complement”, and equality characterization. Searches also covered the direct source's reference chain and the older Szeged/Wiener literature surfaced by those queries. No located source stated or implied the classification proved here.

Because the Zhang–Li problem and its proof are extremely recent, unindexed or simultaneous follow-up work is the main residual originality risk. No specific inaccessible paper was located whose title, abstract, or metadata suggested that it contains this exact \(\omega(G)\ge n-2\) classification.

Originality is therefore assessed as PASS to the best of our knowledge, with the residual parallel-work risk retained.

## Value

The result settles a natural dense structural regime of an explicit new equality-classification problem. The regime \(\omega(G)\ge n-2\) is not artificial: it contains the entire equality family constructed in the source paper. The theorem shows that this construction is eventually unique within that regime, and it identifies the precise exceptional order-10 graph explaining why the construction is not necessary there. The accompanying exact formulas describe the whole two-vertex extension of a clique, not only the equality cases.

## Scope limitations

The theorem does not classify equality when \(\omega(G)\le n-3\), so Zhang–Li Problem 7 remains open in general. No claim is made about a full characterization of all \(2n\)-equality graphs. No independent validation, independent audit, formal verification, or journal peer review is asserted.
