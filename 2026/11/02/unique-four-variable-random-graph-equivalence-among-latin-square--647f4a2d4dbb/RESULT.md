# Unique four-variable random-graph equivalence among Latin-square graphs

## Finding

Let \(L\) be any Latin square of order \(n\ge 2\). Its *Latin-square graph* \(G(L)\) has one vertex for every cell \((r,c,L(r,c))\); two **distinct** cells are adjacent precisely when they share a row, column, or symbol. Work in pure graph adjacency with equality, without counting quantifiers. Let \(\mathcal R\) be the countable random graph.

**Theorem.** The following are equivalent:

1. \(G(L)\) and \(\mathcal R\) satisfy exactly the same first-order sentences using at most four reusable variables, at unrestricted quantifier depth.
2. \(G(L)\) is **3-existentially closed**: for every three distinct vertices and every selection of which of the three must be adjacent to a fourth, there is a distinct fourth vertex realizing that pattern.
3. \(n=8\) and \(L\) is isotopic (by independent bijections on rows, columns, and symbols) to the addition table of \((\mathbb Z/2\mathbb Z)^3\).

In particular exactly **one isomorphism type of Latin-square graph**, on \(64\) vertices, has the same unrestricted four-variable theory as \(\mathcal R\). This graph is also *3-extension vertex-critical*: deleting **any** vertex destroys its 3-existential closure.

## Assumptions and scope

No associativity, coordinatization, commutativity, or extra predicates are assumed for the original Latin square. The order condition \(n\ge2\) avoids the vacuity of three-anchor extension requirements on one-vertex graphs. The three coordinates of a cell are not named in the **graph language**; they are used only to analyze its adjacency. All statements concern ordinary first-order logic with only four reusable variables and *unrestricted* quantifier rank, not counting logic.

## Proof

**(1) and (2) are equivalent.** The Rado graph satisfies the full three-anchor adjacency-extension axiom, a first-order sentence using exactly four variable symbols: three universally quantified, pairwise distinct anchors and one existentially quantified fresh witness, for each of eight patterns. Thus (1) implies (2). Conversely, in the four-pebble partial-isomorphism game between a 3-e.c. finite graph and the random graph, after a move at most three distinct anchors remain. The extension property of the structure into which the moved pebble is placed supplies a point with exactly the required adjacency pattern and distinct from all anchors. For fewer than three distinct anchors, extend them to a three-set first (there are at least four vertices). This is a permanent strategy, hence gives equivalence at every finite quantifier rank and at unrestricted depth.

**An algebraic obstruction forces a Boolean-group table.** Suppose \(G(L)\) is 3-e.c. Choose distinct rows \(r,s\) and distinct columns \(c,d\) with \(L(r,d)=L(s,c)=a\), and put \(b=L(r,c)\). The three cells \(x=(r,c,b)\), \(y=(r,d,a)\), and \(z=(s,c,a)\) form a triangle, by sharing, respectively, a row, column, and symbol. A common neighbor distinct from all three cannot be in row \(r\): there it could be adjacent to \(z\) only at \(x\) or \(y\). Nor can it be in column \(c\), or have symbol \(a\), by the corresponding symmetric argument. Therefore it must match \(x\) by symbol \(b\), \(y\) by column \(d\), and \(z\) by row \(s\). The sole possible fourth vertex is \((s,d,b)\). Thus 3-e.c. implies the **rectangle law**

\[
L(r,d)=L(s,c)\quad\Longrightarrow\quad L(r,c)=L(s,d)
\]

for all distinct rows and columns.

Fix a reference row \(r_0\), and relabel the symbols by its entries so that \(L(r_0,c)=c\) for every column \(c\). Write \(f_r(c)=L(r,c)\), identifying symbols with columns; thus \(f_{r_0}=\mathrm{id}\). Each \(f_r\) is a permutation. Relative to any two distinct rows \(r,s\), the permutation \(f_r^{-1}f_s\) is fixed-point-free by the Latin condition. The rectangle law says that whenever it sends \(c\) to \(d\), it also sends \(d\) to \(c\). Hence \(f_r^{-1}f_s\) is an involution. Taking \(r=r_0\) shows every \(f_s\) is an involution. Since \(f_r^{-1}f_s=f_rf_s\) is also an involution, the permutations \(f_r\) commute pairwise.

Consequently \(H=\langle f_r:r\in R\rangle\) is an elementary abelian 2-group acting on the columns. For each fixed column \(c\), its \(n\) entries \(f_r(c)\) run through all \(n\) columns, so \(H\) is transitive. Any faithful transitive abelian permutation group is regular: an element fixing one point fixes every point and hence is the identity. Therefore \(|H|=n\). The \(n\) distinct elements \(f_r\) exhaust \(H\), and after relabeling rows and columns the original Latin square is the group table of \(H\cong(\mathbb Z/2\mathbb Z)^d\), where \(n=2^d\).

**Excluding the other powers of two.** For \(n=2\), the Latin-square graph is \(K_4\), and every three-set lacks a vertex nonadjacent to all its members. For \(n=4\), choose three cells in one row. A common nonneighbor would have to lie outside that row, use the fourth column, and use the fourth symbol. But the intersection of the fourth column and fourth symbol is the cell in the chosen row, so no witness exists. The same argument applies at order \(3\), although order \(3\) is already excluded by the group reduction.

For \(n=2^d\ge16\), write the Boolean-group table additively as \(L(r,c)=r+c\) on \(V=\mathbb F_2^d\). Choose four linearly independent vectors \(a,b,c,d\in V\), and three vertices \((0,0,0)\), \((a,b,a+b)\), and \((c,d,c+d)\). These vertices share no coordinate pairwise. A common neighbor must match each of them in one of the three coordinate types: row, column, symbol. The same coordinate type cannot be used for two anchors, since all three values in each coordinate type are different. Thus the three types must be assigned bijectively to the anchors. Each of the six assignments equates either one of \(a,b,c,d\) to another or to a sum of two of the others, contradicting linear independence. Consequently this triple has **no** common neighbor and the graph is not 3-e.c.

**The order-eight case.** The sole remaining possibility is \(V=\mathbb F_2^3\), with vertices \((r,c)\in V^2\) and adjacency

\[
(r,c)\sim(s,d)\iff (r,c)\ne(s,d)\ \wedge\ \bigl(r=s\ \vee\ c=d\ \vee\ r+c=s+d\bigr).
\]

The finite exhaustive proof below checks all \(\binom{64}{3}=41664\) unordered triples and all eight patterns (\(333312\) tests). Every pattern has a witness; the smallest witness count is one. The executable, self-contained, independent checkers `check_full.py` and `check_translation.py` are integral to this proof. The first uses adjacency bitsets; the second uses direct coordinate comparisons and translation symmetry. The complete search is over a **fixed finite structure**, so exhaustive enumeration is logically sufficient for this last finite case; no infinite claim is inferred from a bounded experiment. Any Latin square isotopic to this table induces the same graph up to isomorphism.

**Vertex-criticality.** The three mutually nonadjacent anchors \((0,0,0)\), \((1,2,3)\), and \((2,4,6)\) have the **unique** common neighbor \((2,2,0)\). The graph is vertex-transitive under translations \((r,c)\mapsto(r+a,c+b)\). Every vertex is the translate of this unique witness, so deletion of any vertex destroys a required three-anchor extension. This completes the proof.

## Verification

Run `python3 check_full.py` and `python3 check_translation.py` with ordinary Python 3 (no dependencies). Expected exact console outputs are in `output_full.txt` and `output_translation.txt`. The full checker reports minima, over all triples with respectively zero, one, two, or three induced edges, for the eight ordered adjacency masks. Its four rows are

```
0: 13 10 10 3 10 3 3 1
1: 16 8 8 2 8 2 2 2
2: 21 5 5 3 5 3 3 2
3: 20 6 6 2 6 2 2 1
```

Every entry is positive. The second checker independently verifies \(3906\) ordered pairs of nonzero relative anchors after translation sends the first anchor to zero. The two programs use independent adjacency and enumeration implementations.

## Relationship to prior work

Baker, Bonato, and Brown (2003) establish 3-e.c. graphs from approximately half the parallel classes of **odd-order** affine planes, not from exactly three classes in arbitrary Latin squares. Baker, Bonato, Brown, and Szőnyi (2008, Theorem 4) prove 3-e.c. for graphs built from \(q/2\) classes in even-order Desarguesian affine planes \(q\ge8\). At \(q=8\), those graphs have four parallel classes and degree \(28\), whereas the unique graph here uses **three** classes and has degree \(21\). Neither construction states the all-Latin-square uniqueness classification or its Boolean-group obstruction. Besharati et al. (2015) discuss chromatic numbers of Latin-square graphs but not this three-extension classification. Grohe and Otto (2012) provide general finite-variable pebble-game machinery, but not the present exact family-specific outcome. A 2026 paper on VC-dimension of strongly regular graphs is relevant to extension-pattern richness; its full text was not verified for this comparison and remains a priority risk.

## Limitations

The graph must be the **ordinary three-coordinate Latin-square graph**. The conclusion does not cover graphs formed from four or more parallel classes, generic orthogonal arrays, arbitrary strongly regular graphs, signatures naming coordinate classes, counting logic, or five-variable first-order theory. The necessary-structure proof is general, but sufficiency for order eight uses a transparent exhaustive finite computation and therefore depends on verifying the supplied code. Literature search does not prove historical uniqueness, and there has been no independent mathematical audit.

## References

1. C. A. Baker, A. Bonato, and J. M. N. Brown, “Graphs with the 3-e.c. adjacency property constructed from affine planes,” *J. Combin. Math. Combin. Comput.* 46 (2003), 65–83, published 2003-08-31. https://combinatorialpress.com/jcmcc-articles/volume-046/graphs-with-the-3-b-c-adjacency-property-constructed-from-affine-planes/
2. C. A. Baker, A. Bonato, J. M. N. Brown, and T. Szőnyi, “Graphs with the n-e.c. adjacency property constructed from affine planes,” *Discrete Mathematics* 308 (2008), 901–912, online 2007-08-22. https://doi.org/10.1016/j.disc.2007.07.029
3. N. Besharati, L. Goddyn, E. S. Mahmoodian, and M. Mortezaeefar, “On the chromatic number of Latin square graphs,” arXiv:1510.02521, posted 2015-10-08. https://arxiv.org/abs/1510.02521
4. M. Grohe and M. Otto, “Pebble Games and Linear Equations,” arXiv:1204.1990, posted 2012-04-09. https://arxiv.org/abs/1204.1990
5. I. Byrne, J. Byrne, and S. M. Cioabă, “The VC-dimension of strongly regular graphs,” arXiv:2609.10330, posted 2026-09-09 (comparison risk only). https://arxiv.org/abs/2609.10330
