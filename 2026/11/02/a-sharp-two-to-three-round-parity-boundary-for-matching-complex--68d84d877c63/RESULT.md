# A sharp two-to-three-round parity boundary for matching-complex face posets

## Finding
For each integer \(n\ge2\), define \(\mathcal M_n\) to be the inclusion poset of matchings of the complete graph \(K_n\), **including the empty matching**. In the first-order relational language \(\{\le,=\}\), its rank-two theory depends on \(n\) only through the three possibilities \(n=2\), \(n=3\), and \(n\ge4\). Yet the rank-three sentence
\[
\varphi:=\exists x\,\exists y\,\bigl(x<y\land\forall z\,(x<z\Rightarrow z=y)\bigr)
\]
is true exactly when \(n\) is even. Thus for every \(k\ge2\), \(\mathcal M_{2k}\equiv_2\mathcal M_{2k+1}\) but \(\mathcal M_{2k}\not\equiv_3\mathcal M_{2k+1}\). Quantifier rank three is the least rank for defining ground-set parity on this class.

## Assumptions and scope
A matching is a set of pairwise vertex-disjoint edges of a loopless complete graph; empty matching is included. The domain of \(\mathcal M_n\) consists of **all** such edge sets ordered by ordinary inclusion, with no named rank, edges, endpoints, vertices, or maximum matching. Here \(x<y\) abbreviates \(x\le y\land x\ne y\). The quantifier rank of a sentence is the maximal nesting depth of quantifiers, not the number of quantifiers in total.

## Proof
**First, rank two.** For any selected matching \(X\), the quantifier-free diagram of the pair \((X,Y)\) has precisely four possibilities: equality, a strict subset, a strict superset, or incomparability. In a two-round Ehrenfeucht–Fraïssé game, after the first pick, the second player's possible responses depend only on which of these categories has a witness.

The empty matching has equality and strict supersets, but no strict subset or incomparable matching. Every maximal matching has equality and strict subsets. If \(n=2\), its unique maximal matching has no incomparable element. If \(n\ge3\), every maximal matching has an incomparable matching: if it consists of one edge, another edge of the graph is distinct and incomparable; if it consists of at least two edges, one can replace an edge by an edge meeting a different matched vertex, producing an incomparable matching. Finally, a nonempty nonmaximal matching exists iff \(n\ge4\): one edge leaves at least two unmatched vertices. Such an element has strict smaller and larger faces and an incomparable matching (take a different single edge), as well as itself. Every nonempty nonmaximal element exhibits the same full set of four pair-categories. Every maximal element for \(n\ge3\) exhibits equality, below and incomparable, but no above. These are all pointed one-round profiles. Therefore all \(n\ge4\) have the same three pointed profiles and are rank-two equivalent. For \(n=3\), the intermediate profile is absent, and for \(n=2\), the maximal profile additionally lacks incomparability. Their pointed-profile sets are pairwise different, proving the exact three rank-two classes.

**Second, parity at rank three.** For a matching \(X\) having \(t=n-2|X|\) unmatched graph vertices, its strict upper set in the face poset is nonempty exactly when \(t\ge2\). If \(t=2\), the two uncovered vertices form the only available new edge, so \(X\) has precisely one strict upper matching, namely \(X\cup\{e\}\). If \(t\ge3\), there are at least three different choices of a new edge, hence at least three distinct strict upper matchings. Therefore \(X\) has exactly one strict upper matching if and only if \(t=2\). Since \(n-2|X|=2\) is solvable with a matching in a complete graph iff \(n\) is even (and at least two), the displayed rank-three sentence defines parity. The rank-two collapse of all \(n\ge4\) implies that no rank-two sentence can define parity on the full family; the rank-three sentence is optimal.

## Verification
The standalone script `check.py` builds the matching posets directly for each \(2\le n\le9\), computes the pointed one-round extension profile for every face, checks that all \(n\ge4\) share one profile spectrum, and separately searches for a unique strict upper face. Run `python3 check.py`; its expected output is included as `check_output.txt`. These are finite consistency checks; the proof above establishes the infinitely many cases.

## Relationship to prior work
Shareshian and Wachs [1] define the classical matching complex and study its topology, connectivity and torsion homology. This result instead studies how much combinatorial information survives at **small first-order quantifier rank** in its inclusion poset. A two-round collapse is different from full first-order elementary equivalence, which distinguishes the finite structures by cardinality. Generic order-theoretic extension arguments do not establish the particular parity boundary unless the extension multiplicities of matchings are supplied.

## Limitations
The result applies to complete graphs, the full face poset **with its empty face**, and the pure inclusion language. It does not claim the entire rank-three equivalence classification, nor a corresponding statement for arbitrary graphs, posets excluding the empty face, or richer signatures. Prior-art searching cannot establish worldwide uniqueness; independent mathematical validation is not performed.

## References
[1] John Shareshian and Michelle L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054, first submitted 2004-09-03, https://arxiv.org/abs/math/0409054.
