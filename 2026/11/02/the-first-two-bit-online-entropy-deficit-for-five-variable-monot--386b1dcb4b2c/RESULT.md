# The first two-bit online entropy deficit for five-variable monotone Boolean functions

## Finding
For \(1\le n\le5\), let \(B_n=(2^{[n]},\subseteq)\) and take the membership concepts of all its downward-closed subsets. The exact dimensions are
\[
(\operatorname{VCdim}(\mathcal J_n))_{n=1}^5=(\operatorname{Ldim}(\mathcal J_n))_{n=1}^5=(1,2,3,6,10).
\]
The concept counts are \((3,6,20,168,7581)\), giving cardinality upper bounds \((1,2,4,7,12)\). Thus the entropy-minus-Littlestone deficits are \((0,0,1,1,2)\). The first deficit of at least two is attained at five variables.

## Assumptions and scope
A concept is a set \(I\subseteq B_n\) satisfying \(x\in I, y\subseteq x\Rightarrow y\in I\), including the empty and full ideals. For a query \(x\in B_n\), its Boolean answer is \(1\) if and only if \(x\in I\). This is dual by output complementation to all increasing Boolean functions; that duality preserves the two dimensions. Littlestone dimension means maximum fully realized complete binary membership-query-tree depth; VC dimension is the size of a fixed shattered set. All assertions are exact for integer \(n\in\{1,2,3,4,5\}\). No higher-dimensional formula is asserted.

## Proof
**Static dimension.** A shattered support \(S\subseteq B_n\) cannot contain comparable distinct elements: if \(x\subsetneq y\), the labeling that includes \(y\) but excludes \(x\) is forbidden by downward closure. Conversely, if \(S\) is an antichain, for every \(T\subseteq S\), its downward closure has trace \(T\) on \(S\). Therefore the shattered supports are exactly the antichains of \(B_n\). Sperner's theorem gives \(\operatorname{VCdim}(\mathcal J_n)=\binom{n}{\lfloor n/2\rfloor}\). A fixed sequence of shattered queries supplies a complete adaptive tree of that depth, so this is also a lower bound on Littlestone dimension.

**Complete ideal generation.** Split \(B_n\) according to the last coordinate. Every ideal corresponds uniquely to an ordered pair of ideals \((A,C)\) of \(B_{n-1}\) with \(C\subseteq A\): \(A\) is the lower slice and \(C\) the upper slice. Conversely each such pair determines an ideal. Starting with the two ideals of \(B_0\), this generates all concepts without omission and gives the counts shown above.

**Exact adaptive obstruction.** For a finite nonempty subfamily \(F\) and integer \(d\ge1\), put \(R(F,0)=\mathrm{true}\) and use the exact recurrence
\[
R(F,d)\iff\exists x\in B_n:\ R(F_{x,0},d-1)\land R(F_{x,1},d-1),
\]
where \(F_{x,b}=\{I\in F:1_{x\in I}=b\}\). A family supporting depth \(d\) necessarily has at least \(2^d\) concepts, so branches with fewer than \(2^{d-1}\) concepts may be skipped. The recurrence is proved by taking the query at the root of a complete decision tree and restricting its two subtrees; the converse joins two successful subtrees under that query. This induction certifies that an exhaustive evaluation returns exact upper and lower answers.

For \(n\le4\), the supplied checker evaluates the recurrence for the full concept class at depth one above the corresponding Sperner width and returns false. At \(n=5\), a hypothetical depth-eleven tree would require at least \(1024\) concepts in each root branch. By coordinate-permutation symmetry, a root query is determined up to automorphism by its Hamming weight. The smaller branch has respectively \((1,168,2008,2008,168,1)\) concepts at query weights \((0,1,2,3,4,5)\). Only weights two and three can possibly occur. For the weight-two representative \(x=\{1,2\}\), its negative branch of \(2008\) concepts fails \(R(F,10)\); for the weight-three representative \(x=\{1,2,3\}\), its positive branch of \(2008\) concepts also fails \(R(F,10)\). The checker exhaustively verifies both negative statements, visiting respectively \(23644\) and \(6666\) memoized subproblems, under the direct recurrence. Hence no depth-eleven tree exists. Together with the rank-two antichain lower bound of ten, this gives \(\operatorname{Ldim}(\mathcal J_5)=10\).

## Verification
Run `python3 check.py` with standard Python (no third-party packages). It constructs the ideals by the two-slice bijection, independently tests their downward-closure property, recomputes all Boolean query masks, checks all dimension claims through four variables, and evaluates the two symmetry-reduced obstructions at five variables. Its expected final line is `BOOLEAN_LATTICE_IDEALS_ALL_CHECKS_PASS`. The accompanying `CHECK_OUTPUT.txt` is a run record rather than a substitute for the algorithm and proof.

## Relationship to prior work
Classical Sperner theory supplies the VC width and the static lower bound, not the exact online upper bound. Ghazi–Golowich–Kumar–Manurangsi provide general bounds for aggregation of Littlestone classes, not a computed rank for this canonical free distributive-lattice family. The published antichain census of the five-dimensional Boolean lattice (published-finding corpus SCOPE022) provides an independent context for the known \(7581\) Dedekind count but does not state the adaptive tree obstruction in its accessible summary. The comparison concerns implications of exact claims, not merely terminology.

## Limitations
This is a finite exact result through five variables; it does not prove Littlestone dimension equals Sperner width for larger Boolean lattices. The computer-exhaustive upper bound depends on executing `check.py` with correct integer bitset semantics, although the recurrence and concept generation have independent mathematical proofs. Priority checking is limited to accessible historical records and literature, and independent scientific review is not claimed.

## References
- B. Ghazi, N. Golowich, R. Kumar, P. Manurangsi, *Near-tight closure bounds for Littlestone and threshold dimensions*, arXiv:2007.03668 (first public July 7, 2020), PMLR 132 (2021), pp. 686–696.
- P. Manurangsi, *Improved Inapproximability of VC Dimension and Littlestone's Dimension via (Unbalanced) Biclique*, ITCS 2023, DOI:10.4230/LIPIcs.ITCS.2023.85 (general computational context, not an exact dimension table).
- Sperner's theorem (classical antichain-width theorem for Boolean lattices).
