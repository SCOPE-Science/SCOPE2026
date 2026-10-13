# Irredundant and maximal irredundant sets of crown graphs

## Finding

For every integer \(n\ge 3\), let \(\operatorname{Cr}_n=K_{n,n}-M_n\) with bipartition \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), and deleted matching \(a_i b_i\). For \(S=X\cup Y\), where \(X\subseteq A\) and \(Y\subseteq B\), put
\[
I=\{i:a_i\in X\},\qquad J=\{j:b_j\in Y\}.
\]
Then \(S\) is irredundant exactly in the following cases:

1. one of \(X,Y\) is empty;
2. \(S=\{a_i,b_i\}\) is one deleted-matching pair; or
3. \(I\cap J=\varnothing\) and \((|I|,|J|)\in\{(1,1),(1,2),(2,1),(2,2)\}\), with the mixed sizes \((1,2)\) and \((2,1)\) possible only when \(n\ge4\).

Therefore, for
\[
\mathcal I_n(x)=\sum_{S\text{ irredundant}}x^{|S|},
\]
one has
\[
\mathcal I_3(x)=2(1+x)^3-1+9x^2,
\]
and, for every \(n\ge4\),
\[
\mathcal I_n(x)=2(1+x)^n-1+n^2x^2+n(n-1)(n-2)x^3+6\binom{n}{4}x^4.
\]

The inclusion-maximal irredundant sets are as follows. For \(n=3\), they are the two full bipartition classes and the nine mixed irredundant two-sets. For \(n\ge4\), they are exactly the two full bipartition classes, the \(n\) deleted-matching pairs, and the disjoint mixed \((2,2)\) sets. Hence the maximal-irredundant-set enumerator is
\[
\mathcal M_3(x)=9x^2+2x^3,
\]
and, for \(n\ge4\),
\[
\mathcal M_n(x)=n x^2+6\binom{n}{4}x^4+2x^n.
\]
Consequently,
\[
\operatorname{ir}(\operatorname{Cr}_n)=2,\qquad \operatorname{IR}(\operatorname{Cr}_n)=n
\]
for every \(n\ge3\). In comparison, \(K_{n,n}\) has all-set enumerator \(2(1+x)^n-1+n^2x^2\). Thus deleting one perfect matching leaves both scalar irredundance numbers unchanged but creates exactly the new mixed cubic and quartic layers described above.

## Assumptions and scope

All graphs are finite, simple, and undirected. For a graph \(G\), a set \(S\subseteq V(G)\) is irredundant when every \(v\in S\) has a private neighbor with respect to \(S\), equivalently a vertex \(z\in N[v]\) such that
\[
N[z]\cap S=\{v\}.
\]
The empty set is included in \(\mathcal I_n(x)\). The polynomial \(\mathcal M_n(x)\) counts inclusion-maximal irredundant sets, not merely maximum-cardinality irredundant sets. The statement is restricted to the connected crown range \(n\ge3\).

## Proof

Write \(I=\{i:a_i\in X\}\) and \(J=\{j:b_j\in Y\}\). First derive an exact local private-neighbor criterion. Fix \(a_i\in X\). The vertex \(a_i\) itself is private precisely when
\[
Y\subseteq\{b_i\},
\]
because \(a_i\) is adjacent to every vertex of \(B\) except \(b_i\). If self-privacy fails, any private neighbor of \(a_i\) must be some \(b_j\) with \(j\ne i\). Since
\[
N[b_j]=\{b_j\}\cup\bigl(A\setminus\{a_j\}\bigr),
\]
the equality \(N[b_j]\cap S=\{a_i\}\) is equivalent to
\[
j\notin J,\qquad I\setminus\{i\}\subseteq\{j\}.
\]
Thus an external private neighbor for \(a_i\) exists exactly when there is an index \(j\ne i\) satisfying those two conditions. The symmetric criterion holds for every selected \(b_j\).

If \(Y=\varnothing\), every vertex of \(X\) is self-private, so every subset of \(A\) is irredundant; symmetrically, every subset of \(B\) is irredundant.

Now suppose both sides are represented. If \(I\cap J\ne\varnothing\), choose \(i\in I\cap J\). The set \(\{a_i,b_i\}\) is irredundant because its two vertices are nonadjacent and hence each is self-private. If a further selected vertex is present, say \(a_k\) with \(k\ne i\), then \(a_k\) is adjacent to \(b_i\), so it is not self-private. Its local criterion would require the only possible witness index to be \(i\), but \(b_i\in Y\), which excludes that witness. The case of an additional vertex of \(B\) is symmetric. Hence index overlap is possible only for one deleted-matching pair.

Assume next that \(I\cap J=\varnothing\). Because \(J\ne\varnothing\), no selected \(a_i\) is self-private. The local criterion then forces \(|I|\le2\); symmetrically \(|J|\le2\). A disjoint \((1,1)\) set is irredundant because \(n\ge3\) leaves an unused index that supplies external private neighbors to both selected vertices. A disjoint \((2,2)\) set is irredundant: for each selected vertex, the index of the other selected vertex on the same side supplies an unselected opposite-side private neighbor. For a disjoint \((1,2)\) set, the singleton-side vertex additionally needs a witness at an index outside the three used indices, so such a set is irredundant exactly when \(n\ge4\); the \((2,1)\) case is symmetric. This proves the classification.

The one-sided sets contribute \(2(1+x)^n-1\), with the empty set counted once. All mixed irredundant two-sets contribute
\[
nx^2+n(n-1)x^2=n^2x^2.
\]
For \(n\ge4\), the disjoint \((1,2)\) and \((2,1)\) sets contribute
\[
2n\binom{n-1}{2}x^3=n(n-1)(n-2)x^3,
\]
and the disjoint \((2,2)\) sets contribute
\[
\binom{n}{2}\binom{n-2}{2}x^4=6\binom{n}{4}x^4.
\]
When \(n=3\), the mixed triples fail exactly because no fourth witness index exists, giving the stated exceptional formula.

For maximality, any proper one-sided set extends by another vertex on the same side, so only the two full bipartition classes are maximal among one-sided sets. A deleted-matching pair has no irredundant extension by the overlap argument. When \(n\ge4\), each disjoint \((1,1)\) set extends to a disjoint mixed triple, and each mixed triple extends to a disjoint \((2,2)\) set. A disjoint \((2,2)\) set is maximal because any added vertex either creates an index overlap or makes one side contain three selected vertices. When \(n=3\), the six disjoint \((1,1)\) sets and the three deleted-matching pairs are already maximal, while the six one-sided two-sets extend to a full side. This proves the maximal enumerators and the formulas for \(\operatorname{ir}\) and \(\operatorname{IR}\).

## Verification

The accompanying `verify_irredundance.py` constructs \(\operatorname{Cr}_n\) directly for every \(3\le n\le8\), enumerates all vertex subsets, tests irredundance from closed neighborhoods and private neighbors, tests inclusion-maximality by all one-vertex extensions, and compares the resulting coefficient tables with the formulas above. This finite replay checks every subset through graph order \(16\); it supplements, but does not replace, the structural proof for arbitrary \(n\).

## Relationship to prior work

Irredundance is a classical domination-related graph parameter. The 1978 paper of Cockayne, Hedetniemi, and Miller provides an early public source connected with the framework, and the 1979 paper of Bollobás and Cockayne develops the associated domination, independence, and irredundance parameters through closed-neighborhood redundancy. A 2011 paper devoted to bipartite irredundance records classification \(05C69\) and studies several bipartite variants of irredundance. Its searchable full text was checked for the terms “crown”, “complete bipartite”, and “perfect matching”; none occurred.

For the natural comparison graph \(K_{n,n}\), the same private-neighbor criterion immediately gives only one-sided irredundant sets and mixed two-sets, hence
\[
\mathcal I(K_{n,n};x)=2(1+x)^n-1+n^2x^2.
\]
The crown classification is not implied by that complete-bipartite case: deleting the perfect matching produces new irredundant sets in degrees \(3\) and \(4\), while simultaneously changing which mixed two-sets are inclusion-maximal.

## Limitations

The theorem concerns ordinary closed-neighborhood irredundance only. It does not assert corresponding formulas for open irredundance, total irredundance, edge-vertex irredundance, or side-restricted bipartite variants. Exhaustive computation covers only \(3\le n\le8\); the infinite statement rests on the private-neighbor proof. Targeted searches under the names “crown graph”, “complete bipartite graph minus a perfect matching”, “complete bipartite graph minus a one-factor”, and “bipartite Kneser \(H(n,1)\)” found no covering all-set or maximal-set classification. Older or poorly indexed equivalent formulations remain a residual bibliographic risk.

## References

1. E. J. Cockayne, S. T. Hedetniemi, and D. J. Miller, *Properties of Hereditary Hypergraphs and Middle Graphs*, Canadian Mathematical Bulletin 21 (1978), 461–468. DOI `10.4153/CMB-1978-079-5`.
2. B. Bollobás and E. J. Cockayne, *Graph-theoretic parameters concerning domination, independence, and irredundance*, Journal of Graph Theory 3 (1979), 241–249. DOI `10.1002/jgt.3190030306`.
3. V. Swaminathan and Y. B. Venkatakrishnan, *Bipartite theory of irredundant set*, Proyecciones Journal of Mathematics 30 (2011), 19–28. Public PDF: `https://www.scielo.cl/pdf/proy/v30n1/art02.pdf`.
