# Optimal Boolean-atom budget for valuation-faithful co-consistency representations

## Finding
Let \(F=(V,R)\) be any finite nonempty reflexive symmetric Kripke frame, and let \(G_F=(V,E)\) be its underlying simple graph, with \(\{u,v\}\in E\) precisely when \(u\ne v\) and \(uRv\). Write \(m=|V|\) and let \(\theta_e(G_F)\) be the minimum number of vertex-cliques (each of size at least two) needed to cover every edge; put \(\theta_e(G_F)=0\) if \(E=\varnothing\).

A *valuation-faithful co-consistency representation over \(n\) atoms* is an injective map \(s:V\to\mathcal P([n])\setminus\{\varnothing\}\) such that
\[
u Rv\ \Longleftrightarrow\ s(u)\cap s(v)\ne\varnothing,
\]
and, **for every** truth set \(U\subseteq V\), some Boolean value \(a_U\subseteq[n]\) satisfies
\[
 s(v)\subseteq a_U\quad\Longleftrightarrow\quad v\in U\qquad(v\in V).
\]
Thus the **same** represented frame realizes every propositional valuation, one variable at a time, by the containment-based atom clause of translated co-consistency semantics.

**Theorem.** The least possible number \(b(F)\) of Boolean atoms in such a representation is exactly
\[
\boxed{\ b(F)=m+\theta_e(G_F)\ }.
\]
For every specified Boolean valuation \(q\mapsto U_q\subseteq V\), the optimal representation supports simultaneous translation of all variables \(q\) by assigning \(q\mapsto a_{U_q}\). Consequently, satisfaction of every modal formula is preserved under the resulting frame isomorphism. No bound here is asserted for representing *one particular formula* with a formula-dependent representation, or for arbitrary bounded-morphic rather than isomorphic images.

In particular, a reflexive complete frame on \(m\ge2\) worlds requires exactly \(m+1\) atoms, rather than the \(m+\binom m2\) atoms used by the single-edge-token construction; any triangle-free frame with \(m\) worlds requires exactly \(m+|E|\) atoms. An edgeless reflexive frame needs exactly \(m\) atoms.

## Assumptions and scope
All graphs are finite, undirected, and simple after removing the mandatory reflexive loops of \(F\). Cliques of size at least two are allowed to overlap, and their covering cardinality counts cliques, not edges or vertex incidences. The Boolean algebra is the full power-set algebra \(\mathcal P([n])\), with \(n\ge1\). The translated semantics uses an arbitrary nonempty set \(W\subseteq\mathcal P([n])\setminus\{\varnothing\}\), the inherited intersection relation, and atom truth at \(s(v)\) given by inclusion in the chosen Boolean truth value \(a_q\). Set-theoretic parameters are permitted, ensuring that every Boolean truth value can be realized by a sentence (Jockwich--Tarafder--Venturi, Lemma 5.2).

The *universal* valuation quantifier over all \(U\subseteq V\) is essential. Ordinary graph intersection representations need not permit independently choosing every truth set. The result is not a claim about the optimal atom count for an unlabelled graph when valuations are fixed or absent.

## Proof
**Step 1: a private coordinate is forced at each world.** Suppose \(s\) has the stated properties on an \(n\)-atom algebra. Fix \(v\in V\), and apply valuation faithfulness to \(U=V\setminus\{v\}\). The corresponding \(a_U\) contains each \(s(w)\) for \(w\ne v\) but does not contain \(s(v)\). Therefore
\[
 s(v)\not\subseteq \bigcup_{w\ne v}s(w).
\]
Choose \(d_v\in s(v)\setminus\bigcup_{w\ne v}s(w)\). These \(m\) coordinates are pairwise distinct and each appears at only one world.

**Step 2: remaining shared coordinates cover every edge.** For each coordinate \(x\in[n]\setminus\{d_v:v\in V\}\) occurring in at least two represented sets, form \(C_x=\{v\in V:x\in s(v)\}\). If \(u,v\in C_x\) are distinct, then \(s(u)\cap s(v)\ne\varnothing\) and hence \(uRv\); thus \(C_x\) is a clique. Every graph edge \(\{u,v\}\) has a shared coordinate in \(s(u)\cap s(v)\), and no selected private \(d_w\) can be such a coordinate. The sets \(C_x\) therefore form an edge clique cover. It follows that
\[
\theta_e(G_F)\le n-m,
\]
so \(n\ge m+\theta_e(G_F)\).

**Step 3: a matching upper construction.** Fix a minimum clique cover \(C_1,\ldots,C_t\), with \(t=\theta_e(G_F)\). Take pairwise distinct private coordinates \(d_v\) for \(v\in V\) and shared coordinates \(c_1,\ldots,c_t\), all disjoint. Put
\[
 s(v)=\{d_v\}\cup\{c_i:v\in C_i\}.
\]
Each set is nonempty and the map is injective. For distinct worlds \(u,v\), their represented sets intersect iff some covering clique contains both, which holds iff \(\{u,v\}\in E\). Reflexivity holds because each \(s(v)\) is nonempty.

For each \(U\subseteq V\), choose
\[
 a_U=\{c_1,\ldots,c_t\}\cup\{d_v:v\in U\}.
\]
Every shared coordinate of \(s(v)\) is automatically in \(a_U\), and its unique private coordinate is in \(a_U\) iff \(v\in U\). Hence \(s(v)\subseteq a_U\) iff \(v\in U\), establishing universal valuation faithfulness. This matches the lower bound.

**Step 4: modal transfer and extremal graph families.** For any propositional assignment \(V_0\), choose \(a_q=a_{V_0(q)}\), and realize each \(a_q\) through a parameterized Boolean-valued sentence as allowed by Lemma 5.2 of the motivating paper. Truth of propositional variables agrees under \(s\); Boolean and modal induction follows because \(s\) is a frame isomorphism. A complete graph with at least one edge has one clique covering all its edges, giving \(m+1\). A triangle-free graph has no clique larger than an edge, so every edge needs its own clique, giving \(m+|E|\). In the edgeless case the empty cover suffices, giving \(m\). These calculations exhaust the claimed families.

## Verification
Run the standalone Python 3 file `verify.py` with `python3 verify.py`. It (a) exhaustively searches all nonempty set assignments and **directly** checks every possible Boolean valuation on every frame with at most three worlds, comparing the least atom count against \(m+\theta_e(G_F)\); (b) tests an explicit marker/edge-token construction for every one of the \(64\) labelled simple graphs on four vertices; and (c) checks complete-graph and cycle clique-cover families in a separate dynamic program. Recorded output:

```
BRUTE_MINIMUM_BY_ALL_BOOLEAN_VALUATIONS: [(1, (1, 1, 1)), (2, (2, 5, 3)), (3, (8, 34, 5))]
ALL_4_VERTEX_GRAPH_CONSTRUCTIONS: 64
COMPLETE_GRAPH_OPTIMA: m+1 for m=2..6
TRIANGLE_FREE_CYCLE_OPTIMA: 2m for m=4..5
VERIFY_OK
```

These finite experiments are consistency checks of the constructions and definitions. Steps 1--4, not enumeration, prove the theorem for arbitrary finite \(m\).

## Relationship to prior work
Jockwich, Tarafder and Venturi (2026), Theorem 5.3, embed finite reflexive symmetric frames into co-consistency frames using one private marker per world and one additional shared token per edge, and Lemma 5.2 supplies arbitrary translated Boolean truth values. Theorem 5.3 does not optimize the number of Boolean atoms. Its construction uses \(m+|E|\) coordinates, whereas the sharp, **valuation-universal** bound above uses \(m+\theta_e(G_F)\).

The classical Erdős--Goodman--Pósa graph-intersection correspondence, also treated by Wang and Kuo, already identifies the minimum number of *shared intersection coordinates* with an edge clique cover. That graph-theoretic equality is not claimed as new. What is additional here is proving that the modal translation's **unrestricted valuation requirement forces a separate private coordinate for every world**, that these private and shared budgets add with no trade-off, and that the resulting finite Boolean-atom count is simultaneously necessary and sufficient for *all* valuations on the same represented frame. Distinct-set or antichain intersection representations alone do not provide this valuation universality.

## Limitations
The theorem assumes **every** subset of the original frame is obtainable as a propositional truth set; if the valuation vocabulary is restricted, smaller representations may be possible. It does not compute \(\theta_e(G_F)\) on arbitrary graphs in polynomial time. The edge clique cover optimization itself is classical and computationally difficult. The class of all first-order or parameter-free set-theoretic valuations is not addressed. The bibliographic comparisons cannot rule out an earlier equivalent valuation-universal formulation under terminology such as private-label intersection representations.

## References
1. S. Jockwich, S. Tarafder, and G. Venturi, *The Internal Modal Logic of Forcing*, arXiv:2607.25977v1 (first posted 2026-07-28), especially Definition 5.1, Lemma 5.2, Theorem 5.3 and Section 6.
2. P. Erdős, A. W. Goodman, and L. Pósa, *The Representation of a Graph by Set Intersections*, Canadian Journal of Mathematics **18** (1966), 106--112. DOI:10.4153/CJM-1966-014-3.
3. T.-M. Wang and J.-L. Kuo, *On Intersection Representations and Clique Partitions of Graphs*, arXiv:0804.4617v1 (2008).
4. A. Davoodi, D. Gerbner, A. Methuku, and M. Vizer, *On clique coverings of complete multipartite graphs*, Discrete Applied Mathematics **276** (2020), 19--23. DOI:10.1016/j.dam.2019.09.014 (introduction on intersection representations and clique covers).
