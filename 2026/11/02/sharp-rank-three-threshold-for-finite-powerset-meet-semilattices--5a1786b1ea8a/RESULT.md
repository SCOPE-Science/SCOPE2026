# Sharp rank-three threshold for finite powerset meet semilattices

## Finding
Let \(F_n=(\mathcal P([n]),M)\), where \(n\ge1\) and \(M(X,Y,Z)\) means \(X\cap Y=Z\). The signature consists only of equality and ternary \(M\), without constants or a complement symbol. Then
\[
F_m\equiv_3F_n\quad\Longleftrightarrow\quad\min(m,6)=\min(n,6).
\]
Hence exactly six quantifier-rank-three theories occur; every such finite powerset meet semilattice has a rank-three equivalent representative of at most \(64\) elements, and the bound is sharp within the family.

## Assumptions and scope
The quantifier rank counts nested first-order quantifiers; repeated choices of elements are allowed. The structures are the full powersets under intersection, presented relationally by the graph of intersection, not by a function symbol. We make no claim about arbitrary semilattices, infinite semilattices, greater quantifier rank, or signatures containing complement.

## Proof
For an ordered tuple of \(k\) selected subsets, record its \(2^k\) Venn-cell cardinalities as a vector \(c\). Any quantifier-free equality or \(M\)-atom on the tuple is equivalent to a conjunction of emptiness requirements for specific Venn cells; its truth therefore depends only on which components of \(c\) vanish. Every next move chooses, for each Venn cell of size \(c_i\), precisely \(x_i\) atoms to include in the new subset, where \(0\le x_i\le c_i\), producing the new vector \((c_0-x_0,\ldots,c_{2^k-1}-x_{2^k-1},x_0,\ldots,x_{2^k-1})\). These are all and only possible move types.

Write \(T(c,0)\) for the complete atomic diagram and \(T(c,r+1)=\{T(c[x],r):0\le x_i\le c_i\}\), taking sets rather than multisets. This exact recursion describes the \(r\)-round extension type of the selected tuple. In particular, for two selected subsets and one remaining move, \(T(c,1)\) depends on each of the four Venn-region sizes only through its truncation at \(2\): a region can contribute either side of a split, or both, exactly when its size is at least \(2\).

For one selected subset \(X\), write \(a=|X|\), \(b=n-a\). Computing the possible splits of each of these two regions, with the preceding \(2\)-truncation, shows that \(T((a,b),2)\) depends only on \((\min(a,4),\min(b,4))\). The exhaustive finite reduction certificate `verify.py` performs these finite splits, proving the additional identities \(T((3,b),2)=T((4,b),2)\) and \(T((b,3),2)=T((b,4),2)\) for every \(0\le b\le4\). Since all higher counts already truncate at \(4\), this establishes that the pointed two-round type depends only on \((\min(a,3),\min(b,3))\).

The same certificate computes these sixteen possible truncated pairs by exact recursion and verifies that their pointed two-round types are pairwise distinct. Thus the rank-three type of \(F_n\) is encoded by the set
\[
S_n=\{(\min(a,3),\min(n-a,3)):0\le a\le n\}.
\]
For \(1\le n\le5\), this set contains exactly \(n+1\) members, making all five types distinct. For all \(n\ge6\), the set is the fixed seven-element collection \(\{(0,3),(1,3),(2,3),(3,3),(3,2),(3,1),(3,0)\}\). Therefore exactly six equivalence classes occur, as claimed. This uses finite exhaustive identities plus a proof that the finite truncation applies to every integer \(n\), not finite-case extrapolation.

## Verification
Run `python3 verify.py` using Python 3 and no nonstandard dependencies. It recomputes all atomic diagrams, all possible Venn-cell splits, all ten reduction identities, and distinctness of the sixteen pointed types, then checks the six root types and stabilization for parameters \(6\le n\le10\). The proof of the infinite tail is the preceding symbolic truncation argument; finite checks alone do not certify the tail.

## Relationship to prior work
Powerset meet semilattices are classical examples of idempotent semigroups; Araújo and Konieczny analyze related embedding and maximal-size questions for semilattices of finite transformations, rather than logical equivalence (arXiv:1007.4845, first public July 27, 2010). The standard full Boolean-algebra signature sees an eight-atom threshold at quantifier rank three, a stronger language with complement. In the inclusion-only relational signature, a threshold of six is known; that result does not directly imply the claim for the additional atomic meet relation, which is quantifier-free in the present language but not in the inclusion language. Searches found no statement whose implication yields the precise meet-signature threshold; this is not a proof of historical uniqueness.

## Limitations
Self-review is not independent mathematical audit. Priority may be affected by unindexed literature; the closest original semilattice paper is about extremal structural semigroup questions, not Ehrenfeucht–Fraïssé equivalence. The complete atomic-type recursion applies to the stated relational signature only. No broader depth hierarchy is claimed.

## References
Araújo, J., and Konieczny, J., *The Largest Subsemilattices of the Semigroup of Transformations on a Finite Set*, arXiv:1007.4845 (2010), https://arxiv.org/abs/1007.4845.

Libkin, L., *Elements of Finite Model Theory*, Springer, 2004, for Ehrenfeucht–Fraïssé games and powerset inclusion structures.
