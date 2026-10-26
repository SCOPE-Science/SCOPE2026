# Exactly 357 rank-three theories of finite threshold graphs, with a sharp 17-vertex kernel

## Finding

Let \(\mathcal T\) be the class of all nonempty finite simple undirected threshold graphs, considered in the first-order language consisting of equality and a symmetric, irreflexive adjacency predicate \(E\). Write \(G\equiv_3 H\) if the same first-order sentences of quantifier rank at most three are true in \(G\) and \(H\).

**Theorem.** The quotient \(\mathcal T/{\equiv_3}\) has exactly **357 classes**. Every class has a threshold-graph representative on at most **17 vertices**, and 17 is optimal for this requirement: exactly two classes have no threshold-graph representative on fewer than 17 vertices. The two classes have respective minimal representatives encoded by the creation words `0110011011001100` and `1001001100110011`.

The distribution of the 357 classes by their minimum possible threshold-graph order is

\[
\begin{array}{c|rrrrrrrrr}
\text{minimum order}&1&2&3&4&5&6&7&8&9\\
\text{number of classes}&1&2&4&6&8&10&16&26&38\\
\hline
\text{minimum order}&10&11&12&13&14&15&16&17\\
\text{number of classes}&48&54&54&44&26&12&6&2
\end{array}
\]

The number 357 is an exact statement about all sizes, not a count restricted to graphs with at most 17 vertices.

## Assumptions and scope

A creation word is a binary word \(w\in\{0,1\}^{*}\). Start with a single vertex. Reading its letters from left to right, append a vertex adjacent to no earlier vertex when the letter is `0`, and a vertex adjacent to all earlier vertices when it is `1`. Let \(T(w)\) denote the resulting graph. The standard recursive characterization of threshold graphs says that the isomorphism types in \(\mathcal T\) are exactly the \(T(w)\). A word with \(\ell\) symbols produces \(\ell+1\) vertices. The creation order is only a construction device; it is **not** named in the first-order language.

The theorem concerns ordinary first-order quantifier rank, with arbitrarily many variable symbols and arbitrary Boolean combinations, but without counting quantifiers, extra colors, or named creation positions. The empty graph is excluded.

## Proof

**1. Exact description of a three-round type.** For a graph \(G\) and ordered distinct vertices \(x,y\), put
\[
P_G(x,y)=\{(a,b)\in\{0,1\}^{2}:\exists z\notin\{x,y\},\ E(x,z)=a,\ E(y,z)=b\}.
\]
Here equalities with 0 or 1 abbreviate truth-value conditions, not additional predicates. Write \(e_G(x,y)\in\{0,1\}\) for adjacency. For each vertex \(x\), define
\[
 \varepsilon_G(x)=[\exists z\ne x:E(x,z)],\qquad
 \eta_G(x)=[\exists z\ne x:\neg E(x,z)]
\]
and
\[
 V_G(x)=\bigl(\varepsilon_G(x),\eta_G(x),
          \{(e_G(x,y),P_G(x,y)):y\ne x\}\bigr).
\]
Finally let \(S_3(G)=\{V_G(x):x\in V(G)\}\), where all braces denote **sets**, not multisets.

We claim, for any two nonempty finite simple graphs, that
\[
              G\equiv_3 H\quad\Longleftrightarrow\quad S_3(G)=S_3(H). \tag{1}
\]
To prove this, define the rank-zero type of an ordered tuple to be its entire equality-and-adjacency diagram. Its rank-one type is determined by its rank-zero type and by the **set** of rank-zero types of all one-vertex extensions. The same recursion defines rank-two and rank-three types. This is exact: at each step, existential formulas ask whether a lower-rank extension type occurs, universal formulas are negations of such requests, and Boolean combinations add no information. Conversely, each finite type in this recursion has a characteristic finite formula of that quantifier rank.

For a pair \((x,x)\), its rank-one type is specified by the two flags \(\varepsilon_G(x),\eta_G(x)\), since the third variable may equal \(x\) or be a distinct neighbor or nonneighbor. For \(x\ne y\), its rank-one type is specified by the edge bit \(e_G(x,y)\) and the four possible third-vertex patterns in \(P_G(x,y)\); extensions choosing \(z=x\) or \(z=y\) are already determined by the pair diagram. The rank-two type of \(x\) is therefore precisely \(V_G(x)\), up to a fixed encoding. Its rank-three sentence type is the set of rank-two vertex types, namely \(S_3(G)\). This proves (1), including equality cases and graphs of order one.

**2. The two append operations respect the types.** Let \(I(G)=G\sqcup K_1\), and let \(U(G)\) be obtained from \(G\) by adding a vertex adjacent to all original vertices. If \(G\equiv_3 H\), then
\[
 I(G)\equiv_3 I(H),\qquad U(G)\equiv_3 U(H). \tag{2}
\]
For the first assertion, in the three-round Ehrenfeucht–Fraïssé game on the two disjoint unions, Duplicator pairs the new isolated vertices and uses a winning strategy on the old components. This preserves equalities and all cross-component nonedges. The second assertion follows by complementing the graphs, applying the first assertion, and complementing back: first-order quantifier rank is unchanged by the quantifier-free replacement \(E(u,v)\mapsto(u\ne v\wedge\neg E(u,v))\). Thus the rank-three equivalence classes reachable by appending `0` or `1` form a deterministic two-letter transition system.

**3. Finite closure certificate.** The attached `canonical_classes.json` lists 357 states. Each state contains a creation word, its exact signature \(S_3(T(w))\) in a 32-bit-pattern encoding, and the indices of the states reached by appending `0` and `1`. Starting from the one-vertex word, `verify.py` reconstructs this entire list in breadth-first order, never using any size cutoff. It checks each new signature for equality against all earlier ones and stops only when every discovered state has both successors among the discovered states. Thus the resulting set of states is closed under both append operations. Every creation word is obtainable from the one-vertex graph by these operations; (2) and induction on its length imply that every threshold graph belongs to one of these 357 classes.

Each listed state has a different exact \(S_3\) signature; (1) therefore implies that no two represent the same class. This gives both the upper and the lower bound of **357**.

**4. Sharp vertex bound.** Breadth-first search assigns a state its first (hence shortest) creation word. Because of (2), any shorter word reaching the same rank-three class would produce a shorter path to that state, contradicting breadth-first minimality. The longest recorded words contain exactly 16 symbols, corresponding to 17 vertices. There are exactly two such words, displayed in the theorem. Hence every class has a representative of order at most 17 and these two classes have none of order at most 16 within \(\mathcal T\). This proves sharpness.

## Verification

The verification artifacts are `verify.py`, `canonical_classes.json`, and `verification_output.txt`. From their common directory, run `python3 verify.py` using Python 3 with only the standard library. The program independently re-generates the breadth-first state graph, checks all 357 distinct signatures and all **714** transitions, and compares every representative and transition with a second implementation of the generic nested rank-zero-to-rank-three Hintikka-type recursion. It also enumerates all **8191** creation words having at most 12 symbols and checks their coverage. Its recorded final line is `VERIFY_OK`.

The core finite proof requires the finite certificate and the mathematical congruence lemma: enumerating words only through a fixed length, by itself, would not establish the theorem for arbitrarily large threshold graphs. The reproducible program explicitly verifies transition closure, which supplies the infinite step via (2).

## Relationship to prior work

Threshold graphs and their binary recursive construction originate with Chvátal and Hammer (1977). Fürer's 2015 preprint studies characteristic polynomials via the same binary construction and does not give bounded-quantifier-rank classifications. Pikhurko and Verbitsky (2010) describe the general finite-index and Hintikka-type recursion for bounded-rank graph logic, which is a basis for Step 1 but does not report the 357-class threshold-graph specialization or the sharp 17-vertex bound. Verbitsky (2004) examines logical depth of trees, outerplanar graphs, and graph separators, rather than this exact threshold-graph quotient. The last three cited works were examined in accessible rendered full text or substantive sections.

The main added result is the **exact** finite quotient and its **sharp** least-representative distribution, not the general statement that bounded-rank logic has finitely many types. Searches of relevant research records and threshold-graph/finite-model-theory literature did not identify an equivalent exact census. Absence from these searches does not prove global novelty.

## Limitations

The minimality statement is only among **threshold-graph** representatives; a non-threshold graph with an equivalent rank-three theory is not ruled out. Nothing here classifies rank four, a logic with counting, or threshold graphs with a named creation order. No independent external mathematical audit has been performed. Unindexed or inaccessible publications, including historical books on threshold graphs, remain a potential originality risk. The embedded program is an executable finite certificate; mathematical correctness also depends on the explicit rank-type characterization and closure lemma proved above.

## References

1. M. Fürer, *Efficient Computation of the Characteristic Polynomial of a Threshold Graph*, arXiv:1503.00617, first public preprint 2015-03-02. https://arxiv.org/abs/1503.00617
2. O. Pikhurko and O. Verbitsky, *Logical Complexity of Graphs: A Survey*, arXiv:1003.4865, first public preprint 2010-03-25. https://arxiv.org/abs/1003.4865
3. O. Verbitsky, *The First Order Definability of Graphs with Separators via the Ehrenfeucht Game*, arXiv:math/0401361, first public preprint 2004-01-26. https://arxiv.org/abs/math/0401361
4. V. Chvátal and P. L. Hammer, *Aggregation of Inequalities in Integer Programming*, Annals of Discrete Mathematics 1 (1977), 145–162; historical origin of the class (bibliographic identification, not full-text verification).
