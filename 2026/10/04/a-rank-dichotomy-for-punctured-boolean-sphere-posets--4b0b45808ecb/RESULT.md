# A rank dichotomy for punctured Boolean sphere posets
## Finding
For every integer \(k\ge 4\), let
\[
P_k=\{B\subset [k]:\varnothing\ne B\ne [k]\}
\]
with the inclusion order. For a nonempty proper subset \(A\subset[k]\), put
\[
Q_{k,A}=P_k\setminus\{A\}.
\]
Then \(Q_{k,A}\) is weakly contractible for every \(A\). Moreover,
\[
Q_{k,A}\text{ is contractible}\quad\Longleftrightarrow\quad |A|\in\{1,k-1\}.
\]
If \(2\le |A|\le k-2\), then \(Q_{k,A}\) has no beat points. Thus it is already a Stong core, so it is a noncontractible finite \(T_0\)-space whose order complex is contractible.

## Assumptions and scope
The topology on a finite \(T_0\)-space is identified with its specialization order. A point is an up beat point when its strict upper set has a minimum, and a down beat point when its strict lower set has a maximum. The order complex \(\mathcal K(X)\) has one simplex for every nonempty chain of \(X\).

The claim concerns all integers \(k\ge4\) and every nonempty proper \(A\subset[k]\). No assertion is made that these spaces are minimal among all weakly contractible noncontractible finite spaces; the statement is a complete rank classification inside this canonical punctured-Boolean family.

## Proof
The order complex \(\mathcal K(P_k)\) is the barycentric subdivision of the boundary of the \((k-1)\)-simplex. Hence it is a combinatorial \((k-2)\)-sphere. Passing from \(P_k\) to \(Q_{k,A}\) deletes exactly the vertex of \(\mathcal K(P_k)\) corresponding to the face \(A\), together with all simplices containing that vertex. Therefore \(\mathcal K(Q_{k,A})\) is the antistar of that vertex. The antistar of a vertex in a combinatorial sphere is a combinatorial ball: the open star is an open ball and its complement, with common boundary the vertex link, is a closed ball. Consequently
\[
|\mathcal K(Q_{k,A})|\cong B^{k-2},
\]
so McCord's weak equivalence between a finite \(T_0\)-space and its order complex shows that every \(Q_{k,A}\) is weakly contractible.

Suppose first that \(A=\{a\}\) is an atom. Define
\[
r(B)=\begin{cases}B\setminus\{a\},&a\in B,\\B,&a\notin B.\end{cases}
\]
Because the deleted point is exactly \(\{a\}\), the value \(r(B)\) is never empty. The map is order preserving, satisfies \(r(B)\subseteq B\), and fixes its image pointwise. Its image is the poset of all nonempty subsets of \([k]\setminus\{a\}\), which has the maximum \([k]\setminus\{a\}\). Thus the image is contractible, and the pointwise inequality \(r\le\operatorname{id}\) gives a strong deformation retraction. Hence \(Q_{k,A}\) is contractible.

Dually, if \(A=[k]\setminus\{a\}\) is a coatom, define
\[
r(B)=\begin{cases}B\cup\{a\},&a\notin B,\\B,&a\in B.\end{cases}
\]
Because the unique coatom missing \(a\) has been deleted, the value never equals \([k]\). The image consists of the proper subsets containing \(a\), has minimum \(\{a\}\), and \(\operatorname{id}\le r\). This again gives a strong deformation retraction onto a contractible subspace.

Now assume \(2\le |A|\le k-2\), and let \(B\in Q_{k,A}\). If \(|B|=k-1\), its strict upper set is empty, so \(B\) is not an up beat point. If \(|B|=k-2\), its two immediate proper supersets are distinct coatoms, and neither can equal \(A\); hence the strict upper set has at least two incomparable minimal elements. If \(|B|\le k-3\), then \(B\) has at least three immediate supersets in \(P_k\); deleting the single point \(A\) removes at most one, leaving at least two incomparable minimal strict upper elements. Thus no point is up beat.

The dual argument handles down beat points. If \(|B|=1\), the strict lower set is empty. If \(|B|=2\), both atoms immediately below \(B\) remain because \(|A|\ge2\) and \(B\ne A\). If \(|B|\ge3\), at least three immediate subsets lie below \(B\), and deleting \(A\) removes at most one. Hence at least two incomparable maximal strict lower elements remain. There are therefore no down beat points either.

So for internal ranks \(Q_{k,A}\) has no beat points and has more than one point. Stong's core theorem says that successive beat-point deletions produce the core and that homotopy-equivalent finite \(T_0\)-spaces have homeomorphic cores. A contractible finite \(T_0\)-space has the one-point core. Since \(Q_{k,A}\) is already a non-singleton core, it cannot be contractible. This proves the dichotomy.

## Verification
The accompanying `verify.py` independently constructs \(P_k\) and \(Q_{k,A}\) for \(4\le k\le8\), one representative \(A\) of every possible rank. It checks the point count, the extreme-rank retractions and their order inequalities, and the absence of every up and down beat point in every internal-rank case. It also counts all chains by dynamic programming and verifies Euler characteristic \(1\) and maximal chain length \(k-1\) for each punctured poset.

These finite checks are stress tests only. The universal weak-contractibility assertion uses the antistar argument above, and the universal finite-space contractibility classification uses the explicit retractions and beat-point proof.

## Relationship to prior work
Cianci and Ottina classify the smallest homotopically trivial noncontractible finite spaces and prove that nine points are necessary; their paper also summarizes the beat-point/core criterion used here. Their classification does not discuss punctures of proper Boolean lattices. Barmak and Minian develop the simple-homotopy relation between finite spaces and order complexes and likewise do not state this rank dichotomy. Stong supplies the finite-space core theorem.

The present statement instead fixes the canonical face poset of a simplex boundary, deletes one face, and determines exactly when the resulting finite space remains contractible even though every deletion is weakly contractible. The internal ranks give an infinite family of weakly contractible spaces that are already cores.

## Limitations
The proof uses the standard PL fact that the antistar of a vertex in a combinatorial sphere is a ball. The computation checks only \(4\le k\le8\) and is not used to extrapolate the theorem. The literature search cannot exclude an equivalent statement in unindexed older poset or finite-space literature; no such statement or stronger implication was found in the inspected sources.

## References
1. N. Cianci and M. Ottina, “Smallest homotopically trivial non-contractible spaces,” arXiv:1608.05307, first version 2016-08-18. Primary MSC 55P15 and 06A99.
2. J. A. Barmak and E. G. Minian, “Simple Homotopy Types and Finite Spaces,” arXiv:math/0611158; Advances in Mathematics 218 (2008), 87–104.
3. R. E. Stong, “Finite Topological Spaces,” Transactions of the American Mathematical Society 123 (1966), 325–340.
