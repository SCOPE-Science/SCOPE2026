# Sharp \(2^q\) atom-visibility threshold for finite Boolean algebras
## Finding
Let \(B_n\) be the powerset Boolean algebra on an \(n\)-element atom set, with \(n\ge1\), in the usual language \(\{0,1,\wedge,\vee,\neg}\). For every \(q\ge0\),
\[
B_n\equiv_q B_m \quad\Longleftrightarrow\quad \min(n,2^q)=\min(m,2^q),
\]
where \(\equiv_q\) means agreement on all first-order sentences of quantifier rank at most \(q\). Thus, if \(1\le n<m\), the least quantifier rank of a sentence separating \(B_n\) from \(B_m\) is
\[
\left\lceil\log_2(n+1)\right\rceil.
\]

## Assumptions and scope
Only nontrivial finite Boolean algebras are considered. Every such algebra is isomorphic to a unique \(B_n\), where \(n\) is its number of atoms. Quantifier rank is nesting depth of first-order quantifiers. The language contains the Boolean constants and operations shown above and no extra predicates such as cardinality predicates.

## Proof
For the upper-equivalence direction, consider the \(q\)-round Ehrenfeucht--Fraisse game. After \(j\) elements have been selected in each algebra, those elements cut the atom set into at most \(2^j\) Venn cells. Maintain the following invariant for every corresponding pair of cells: either their atom counts are equal, or both counts are at least \(2^{q-j}\).

If both initial atom counts are at least \(2^q\), the invariant holds at \(j=0\). Suppose it holds before a move and put \(T=2^{q-j-1}\). A Spoiler move splits each old cell into two parts. If an old pair has equal size, Duplicator copies the split sizes exactly. Otherwise both old sizes are at least \(2T\). If one side of Spoiler's split has size below \(T\), Duplicator matches that small size exactly; the complementary part in each structure then has size at least \(T\). If both parts have size at least \(T\), Duplicator chooses any split of the corresponding old cell with both parts at least \(T\). Hence the invariant survives.

After \(q\) rounds the threshold is \(1\), so corresponding Venn cells are simultaneously empty or nonempty. Every Boolean term in the selected elements is a union of Venn cells. Therefore every atomic equality between Boolean terms has the same truth value in the two structures, so the selected correspondence is a partial isomorphism. Duplicator wins. If \(n=m<2^q\), the algebras are isomorphic. This proves the forward implication whenever the truncated atom counts agree.

For the separating direction, define formulas \(A_k(x)\) meaning that at least \(k\) atoms lie below \(x\). Let \(A_1(x)\) be \(x\ne0\). For \(k\ge2\), set \(a=\lfloor k/2\rfloor\), \(b=\lceil k/2\rceil\), and recursively use
\[
A_k(x)\;:=\;\exists y\,\bigl((y\wedge x=y)\wedge A_a(y)\wedge A_b(x\wedge\neg y)\bigr).
\]
The two pieces are disjoint and their join lies below \(x\), so induction on \(k\) proves that this formula has exactly the stated meaning. Its quantifier rank satisfies
\[
\operatorname{qr}(A_k)=\left\lceil\log_2 k\right\rceil.
\]
If \(n<m\), the sentence \(A_{n+1}(1)\) is false in \(B_n\) and true in \(B_m\), giving a separator of rank \(\lceil\log_2(n+1)\rceil\). Conversely, for every smaller \(q\) one has \(n\ge2^q\), so the game argument shows \(B_n\equiv_q B_m\). The rank is therefore minimal.

## Verification
The proof is symbolic and covers all \(n,m\ge1\) and \(q\ge0\). As a finite sanity check, `verify.py` directly solves the full Ehrenfeucht--Fraisse game on powerset algebras for every \(1\le n,m\le4\) and \(0\le q\le3\). It returns `VERIFY_OK cases=64 states=186264` and agrees with the theorem in every tested case. This finite computation is corroborative only; it is not used as an infinite proof.

## Relationship to prior work
Kuncak and Rinard's 2004 technical report develops quantifier elimination for Boolean algebras of finite sets and, in its pure-Boolean-algebra analysis, uses Venn-cell cardinalities truncated at powers of two. In particular, its Section 6.2 contains a truncation lemma with cutoff \(2^{r-1}\) inside the elimination recurrence. The result above isolates the exact invariant at first-order quantifier rank \(q\), proves the converse, and gives the matching least distinguishing rank. Targeted searches of the inspected source found no use of “quantifier rank” or “Ehrenfeucht” and no statement of the displayed iff criterion.

Kozen's 1980 paper studies complexity for finite, atomic, and other classes of Boolean algebras. Its accessible abstract does not state an exact pairwise quantifier-rank threshold. Full text was not available in the checked open sources, so possible overlap there remains a literature risk rather than being treated as ruled out.

## Limitations
No priority or first-discovery claim is made. The exact threshold may be folklore or may appear in an older, unindexed, or inaccessible treatment. The theorem is only for finite nontrivial Boolean algebras in the standard Boolean-algebra language; adding cardinality predicates, named atoms, or other relations changes the game. The finite verifier covers only the stated small range and cannot establish the general theorem by itself.

## References
1. Viktor Kuncak and Martin Rinard, *The First-Order Theory of Sets with Cardinality Constraints is Decidable*, MIT CSAIL Technical Report 958, July 2004; arXiv:cs/0407045, first posted 2004-07-17.
2. Dexter Kozen, *Complexity of Boolean algebras*, Theoretical Computer Science 10 (1980), 221--247, DOI: 10.1016/0304-3975(80)90048-1.
