# Locating-total domination of rooted products with cycles of length \(1 \pmod 4\)

## Definitions

For a graph \(G\) with no isolated vertices, a **locating-total dominating set** (LTD-set) is a set \(S\subseteq V(G)\) such that

1. every vertex has a neighbor in \(S\); and
2. any two distinct vertices outside \(S\) have different neighborhoods in \(S\).

Its minimum cardinality is denoted \(\gamma_t^L(G)\).

A **locating-dominating set** (LD-set) of a graph \(H\) is a set \(D\subseteq V(H)\) such that every vertex outside \(D\) has a nonempty neighborhood in \(D\), and distinct vertices outside \(D\) have distinct neighborhoods in \(D\). Its minimum cardinality is denoted \(\gamma_L(H)\).

For a connected graph \(H\) and a rooted graph \(R\), the rooted product \(H\odot R\) is formed from one copy of \(H\) and one copy of \(R\) at each vertex of \(H\), identifying that vertex with the root of its copy.

## Main theorem

Let \(H\) be a connected finite simple graph of order \(n\ge 2\), let \(k\ge 1\), and root \(C_{4k+1}\) at any cycle vertex. Then

\[
\boxed{\gamma_t^L(H\odot C_{4k+1})=2kn+\gamma_L(H).}
\]

Thus this family of rooted products exactly embeds ordinary locating domination into locating-total domination, up to the additive term \(2k|V(H)|\).

### Proof

For each \(v\in V(H)\), label the vertices of its rooted cycle copy
\[
v_0,v_1,\ldots,v_{4k},
\]
in cyclic order, with \(v_0=v\) the root. Let \(S\) be an arbitrary LTD-set of \(H\odot C_{4k+1}\), and write
\[
S_v=S\cap\{v_0,\ldots,v_{4k}\}.
\]

Every nonroot \(v_i\), \(1\le i\le4k\), has no neighbors outside its own cycle. Total domination therefore requires at least one of \(v_{i-1},v_{i+1}\) to belong to \(S_v\).

On the index set \(\{0,\ldots,4k\}\), introduce an auxiliary graph with the \(4k\) edges
\[
\{i-1,i+1\},\qquad i=1,\ldots,4k,
\]
where indices are taken modulo \(4k+1\). Adding the omitted edge corresponding to \(i=0\) would give the step-two cycle on \(4k+1\) vertices. Since \(4k+1\) is odd, step two traverses the entire cycle, so omitting one edge leaves the path \(P_{4k+1}\). Hence \(S_v\) is a vertex cover of this path and
\[
|S_v|\ge \tau(P_{4k+1})=2k.
\]

The minimum vertex cover of an odd path is unique. In the original cycle indexing it is
\[
L_v=\{v_{4j+2},v_{4j+3}:0\le j\le k-1\}.
\]
In particular, when \(|S_v|=2k\), neither the root \(v_0\) nor either cycle-neighbor \(v_1,v_{4k}\) belongs to \(S\).

Define
\[
A=\{v\in V(H):|S_v|\ge 2k+1\}
\]
and let
\[
R=\{v\in V(H):v_0\in S\}.
\]
The uniqueness just proved implies \(R\subseteq A\).

If \(v\notin A\), then \(S_v=L_v\), so the root \(v_0\notin S\) has no selected cycle-neighbor. Therefore
\[
N_{H\odot C_{4k+1}}(v_0)\cap S
=
\{u_0:u\in N_H(v)\cap R\}.
\]
This set is nonempty by total domination. For distinct \(v,w\notin A\), these sets are distinct by the locating property of \(S\). Since \(R\subseteq A\), it follows that \(A\) itself is an LD-set of \(H\): every vertex outside \(A\) has a neighbor in \(R\subseteq A\), and equality
\(N_H(v)\cap A=N_H(w)\cap A\) would imply equality after intersecting with \(R\), a contradiction. Hence
\[
|A|\ge\gamma_L(H).
\]
Consequently
\[
|S|=\sum_{v\in V(H)}|S_v|
\ge 2kn+|A|
\ge 2kn+\gamma_L(H).
\]

For the reverse inequality, let \(D\) be a minimum LD-set of \(H\). Use the following two patterns.

For \(v\notin D\), select
\[
L_v=\{v_{4j+2},v_{4j+3}:0\le j\le k-1\},
\]
of size \(2k\).

For \(v\in D\), select
\[
U_v=\{v_0\}\cup
\{v_{4j+1},v_{4j+4}:0\le j\le k-1\},
\]
of size \(2k+1\).

Let
\[
S=\bigcup_{v\notin D}L_v\;\cup\!\!\bigcup_{v\in D}U_v.
\]
Inside every copy, the selected nonroot vertices occur in adjacent pairs, while in a \(U_v\)-copy the selected root is adjacent to selected cycle vertices. Thus all selected vertices have selected neighbors, and every unselected nonroot vertex is adjacent to a selected cycle vertex. If \(v\notin D\), its root has no selected cycle-neighbor but has a selected root-neighbor because \(D\) dominates \(H-D\). Hence \(S\) is total dominating.

Each unselected nonroot vertex has, within its own copy, a singleton selected-neighbor signature, and these singletons are distinct within that copy. Signatures from different copies contain different cycle vertices. The only unselected roots are those for \(v\notin D\), and their signatures are exactly
\[
\{u_0:u\in N_H(v)\cap D\},
\]
which are nonempty and pairwise distinct because \(D\) is locating-dominating in \(H\). Root signatures contain selected roots, whereas nonroot signatures contain selected nonroot cycle vertices, so the two types cannot collide. Therefore \(S\) is an LTD-set and
\[
|S|=2kn+|D|=2kn+\gamma_L(H).
\]
This proves the theorem.

## Correction of the path-by-cycle formula

Wei, Ahmad, Hameed and Hanif (2020), Theorem 9, give for \(q_1\equiv1\pmod4\)
\[
\gamma_t^L(P_{q_2}\odot C_{q_1})
=
q_2\,\gamma_t^L(C_{q_1-1})+\frac{q_2}{2}.
\]
Their displayed formula is already nonintegral when \(q_2\) is odd. More substantially, the theorem above shows that the exact correction is controlled by the locating-domination number of the base path.

Using the classical value
\[
\gamma_L(P_q)=\left\lceil\frac{2q}{5}\right\rceil,
\]
for every \(k\ge1\) and \(q\ge2\),
\[
\boxed{
\gamma_t^L(P_q\odot C_{4k+1})
=
2kq+\left\lceil\frac{2q}{5}\right\rceil.
}
\]

For example,
\[
\gamma_t^L(P_{10}\odot C_5)=24,
\]
whereas the 2020 formula gives \(25\). This shows that the issue is not only the missing rounding in the displayed \(q_2/2\) term.

## Verification evidence

A direct exact 0-1 optimization check was performed for every connected graph in the standard Graph Atlas on at most five vertices, using both rooted cycles \(C_5\) and \(C_9\). Across all 62 products, the computed minimum locating-total domination number agreed with
\[
2k|V(H)|+\gamma_L(H).
\]
The specific example \(P_{10}\odot C_5\) was also checked directly and gives \(24\). The accompanying script reproduces these finite checks. These computations corroborate, but are not used in, the general proof.

## Relation to prior literature and originality

The closest primary source is Wei et al. (2020), which defines the same rooted product and states exact formulas for \(P_{q_2}\odot C_{q_1}\); its \(q_1\equiv1\pmod4\) case is the formula corrected above. A later 2021 paper studies locating-total domination in other cycle-related and rotationally symmetric graph families.

The synonymous **comb product** terminology was also checked. Pribadi and Saputro (2020) determine the ordinary locating-domination number of comb products of arbitrary connected graphs; that is a different parameter and does not supply the locating-total formula proved here. Targeted searches under rooted-product, comb-product, locating-total and location-total terminology did not locate a published correction of Wei et al.'s \(1\pmod4\) case or the general identity above.

Originality is therefore claimed only **to the best of our knowledge**. The main residual risk is literature indexed under alternative product or domination terminology, or a correction not surfaced by the searches used here.

## Limitations

- The theorem treats cycle length \(4k+1\); it does not reclassify the other congruence classes in Wei et al.'s rooted-product formulas.
- It does not determine \(\gamma_L(H)\) for arbitrary \(H\); rather, it transfers that parameter exactly into the rooted product.
- The finite verification is supplementary and is not a substitute for the proof.
- No claim is made that every statement in the 2020 paper outside the corrected case is valid or invalid.

## References

1. J. Wei, U. Ahmad, S. Hameed, J. Hanif, “Locating-Total Domination Number of Cacti Graphs,” *Mathematical Problems in Engineering* 2020, Article ID 6197065. https://doi.org/10.1155/2020/6197065
2. P. J. Slater, “Domination and location in acyclic graphs,” *Networks* 17 (1987), 55–64. https://doi.org/10.1002/net.3230170105
3. A. A. Pribadi and S. W. Saputro, “On locating-dominating number of comb product graphs,” *Indonesian Journal of Combinatorics* 4 (2020).
4. H. Raza, N. Iqbal, H. Khan, T. Botmart, “Computing locating-total domination number in some rotationally symmetric graphs,” *Science Progress* 104 (2021). https://doi.org/10.1177/00368504211053417

**Same-model review: passed. Independent audit: not yet performed.**
