# Minimal-fort hypergraphs and zero-forcing polynomials of \(\overline{P_n}\)

## Finding

Let \(P_n\) be the path on labeled vertices \(1,\ldots,n\), in this order, and put \(H_n=\overline{P_n}\). For every integer \(n\ge4\), **all inclusion-minimal forts** of \(H_n\) have cardinality three or four, and are exactly:

1. Three-element sets \(F=\{a,b,c\}\) for which there is **no** integer \(i\) with \(\{i,i+2\}\subseteq F\) and \(i+1\notin F\).
2. Four-element sets \(F=\{a,a+2,b,b+2\}\) with \(1\le a\), \(b\ge a+3\), and \(b+2\le n\).

These families are disjoint, and the complete minimal-fort generating polynomial is
\[
\mathcal M_n(z)=\left[\binom n3-(n^2-6n+10)\right]z^3+\binom{n-4}{2}z^4.
\]
Here \(\binom{r}{s}=0\) when \(0\le r<s\); in particular the second term vanishes at \(n=4,5\). The ordinary zero-forcing-set polynomial is, in the notation explained below,
\[
\boxed{\mathcal Z(H_n;z)=z^{n-3}\left[(n^2-6n+10)+\binom n2z+nz^2+z^3\right].}
\]
In particular, exactly \(n^2-6n+10\) minimum zero-forcing sets exist, the pre-existing minimum cardinality is \(n-3\), and a genuine second rank of minimal forts first appears at \(n=6\), in the unique four-element fort \(\{1,3,4,6\}\).

## Assumptions and scope

All graphs are finite, simple, and undirected. In \(H_n\), distinct vertices \(u,v\) are adjacent precisely when \(|u-v|\ne1\). A **fort** is a nonempty vertex set \(F\) for which no vertex outside \(F\) has exactly one neighbor in \(F\); it is **minimal** if no proper nonempty subset is a fort. In **ordinary zero forcing**, initially selected vertices are blue; a blue vertex with precisely one white neighbor may color that neighbor blue. A subset is zero forcing if all vertices can eventually become blue. The polynomial \(\mathcal Z(H_n;z)\) has coefficient of \(z^k\) equal to the number of zero-forcing subsets of size \(k\). The statements quantify over every integer \(n\ge4\) and every indicated vertex subset; no probabilistic or generic-position assumptions are used.

## Proof

**Step 1: fort-size limits.** Every vertex of \(P_n\) has at most two neighbors. Consequently, for any \(F\subseteq V(H_n)\) with \(|F|\ge4\), every outside vertex has at least \(|F|-2\ge2\) neighbors in \(H_n\) belonging to \(F\). Thus all four-element sets and all larger sets are forts. No singleton is a fort, because \(H_n\) has no isolated vertices for \(n\ge4\). A two-element fort would require its two vertices to have identical adjacency to every vertex outside the pair, both in \(H_n\) and in \(P_n\). But \(P_n\), for \(n\ge4\), has no such pair: adjacent vertices have an external neighbor of one but not the other; vertices separated by at least three edges have a neighbor of one not the other; and vertices separated by exactly two edges have the common middle neighbor but at least one has an additional external neighbor. Therefore every three-element fort is automatically minimal, and any minimal fort has size three or four.

**Step 2: three-element forts.** Let \(F\) have three elements. An outside vertex \(i+1\) has exactly one neighbor in \(F\) in \(H_n\) precisely when its two path-neighbors \(i,i+2\) both belong to \(F\). Thus \(F\) is a fort if and only if no \(101\) occurs in its length-\(n\) membership word (\(1\) meaning membership in \(F\)). This proves family 1.

**Step 3: four-element minimal forts.** Write \(F=\{a,b,c,d\}\) with \(a<b<c<d\), and put \(x=b-a\), \(y=c-b\), \(w=d-c\). Every three-subset of \(F\) must be *nonfort* if \(F\) is minimal. By Step 2, a sorted triple is a nonfort exactly when at least one of its two successive gaps equals two. In particular, for triples \(\{a,b,d\}\) and \(\{a,c,d\}\) we require respectively
\[
(x=2)\ \text{or}\ (y+w=2),\qquad (x+y=2)\ \text{or}\ (w=2).
\]
If \(x=2\) and \(w\ne2\), the second condition fails, since \(x+y>2\). Symmetrically, \(w=2\) and \(x\ne2\) violates the first. If both \(x\ne2\) and \(w\ne2\), the displayed conditions force \(x=y=w=1\), but then \(\{a,b,c\}\) is a fort, contradicting minimality. Hence \(x=w=2\); \(y\ge1\) is arbitrary. Conversely, if \(x=w=2\), any three-subset of \(F\) contains at least one of the two pairs \(\{a,a+2\}\), \(\{c,c+2\}\), with its midpoint absent from that triple, so no three-subset is a fort. This proves family 2, with \(c=a+2+y\ge a+3\). Its cardinality is \(\sum_{a=1}^{n-5}(n-a-4)=\binom{n-4}{2}\), interpreted as zero for \(n=4,5\).

**Step 4: count three-forts.** A membership word with exactly three ones avoids \(101\) precisely when each gap of zeros between two maximal runs of ones has length at least two. The word can have one, two, or three runs of ones. The corresponding counts are \(n-2\), \(2\binom{n-3}{2}\), and \(\binom{n-4}{3}\), respectively, with the usual zero binomial convention. Therefore the number of three-forts is
\[
(n-2)+2\binom{n-3}{2}+\binom{n-4}{3}
=\binom n3-(n^2-6n+10).
\]
For \(n=4,5,6\), the same formula is valid by direct boundary substitution (and the zero-binomial convention); for \(n\ge7\), it follows by stars-and-bars for the extra zero positions. Combining with Step 3 establishes \(\mathcal M_n(z)\).

**Step 5: zero forcing.** Every initial white set of at least four vertices contains a four-vertex fort (indeed any chosen four whites), so cannot be completely forced. With three whites, an initial force is possible exactly when an outside blue vertex has just one white neighbor; by Step 2, this means the white triple contains \(101\). Once that force occurs, only two whites remain, and Step 1 ensures they cannot form a fort; a further force is available. The last white vertex can then be forced because \(H_n\) has no isolates. Thus exactly \(n^2-6n+10\) initial white triples are forceable. Likewise, every initial set with one or two whites can be forced, by the nonexistence of forts of those sizes. There are \(\binom n2\), \(n\), and \(1\) ways to choose the sets with two, one, and zero whites, respectively. All smaller blue sets fail; this proves the displayed zero-forcing polynomial.

## Verification

Run `python3 verify.py` from this directory. The program constructs adjacency independently from the graph definition, exhaustively evaluates every vertex subset of \(H_n\) for \(4\le n\le14\), derives minimal forts by inclusion tests without using the classification, and independently performs the forcing process for every initial blue set. It compares the resulting exact counts and full families against both formulas. The run checked \(32{,}752\) subsets and terminated with `VERIFY_OK`. These finite checks corroborate the proof but are not the proof for arbitrary \(n\).

## Relationship to prior work

Curl, Fallat, Moruzzi, Reinhart, and Young (arXiv:2206.03932, initially public June 8, 2022) establish the numerical zero-forcing number \(Z(\overline T)=|V(T)|-3\) for nonstar trees, and thus for \(P_n\). That numerical fact is credited here, not asserted as new. Boyer and collaborators (arXiv:1801.08910, 2018) introduce and examine the zero-forcing polynomial, including generic near-top coefficients; those generic coefficients give the three largest terms of the displayed polynomial but do not determine its leading coefficient. Becker and collaborators (arXiv:2404.05963, 2024) study minimal-fort enumeration and the fort-cover formulation for several graph families, notably paths themselves; the complement-path classification above is a different object. The full two-rank minimal-fort hypergraph, its explicit enumeration, and the leading zero-forcing coefficient are the claims assessed here.

## Limitations

This classification concerns ordinary zero forcing and the complement of a single path, not other forcing rules or arbitrary tree complements. It does not establish novelty against inaccessible or unindexed publications, nor does it claim independent mathematical verification. It supplies a complete symbolic proof and reproducible finite checks, but no external certification. The known scalar zero-forcing minimum and general fort-hitting principle are prior results.

## References

- E. Curl, S. Fallat, R. Moruzzi Jr., C. Reinhart, D. Young, *On the zero forcing number of the complement of graphs with forbidden subgraphs*, arXiv:2206.03932 (first posted 2022-06-08), https://arxiv.org/abs/2206.03932 .
- K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, C. Reinhart, *The zero forcing polynomial of a graph*, arXiv:1801.08910 (first posted 2018-01-26), https://arxiv.org/abs/1801.08910 .
- P. Becker, T. R. Cameron, D. Hanely, B. Ong, J. P. Previte, *On the number of minimal forts of a graph*, arXiv:2404.05963 (first posted 2024-04-09), https://arxiv.org/abs/2404.05963 .
