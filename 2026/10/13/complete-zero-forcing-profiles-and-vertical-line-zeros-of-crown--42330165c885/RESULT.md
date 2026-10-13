# Complete zero-forcing profiles and vertical-line zeros of crown graphs

## Finding

Let \(H_n=K_{n,n}-M\) be the crown graph with bipartition \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), where \(n\ge3\), and \(a_ib_j\) is an edge exactly when \(i\ne j\). In standard zero forcing, a blue vertex with exactly one white neighbor may make that neighbor blue. Define \(Z(H_n;x)=\sum_{S\subseteq V(H_n):\,S\text{ zero-forcing}}x^{|S|}\), in which a set is counted once irrespective of its forcing sequences.

**Complete classification.** Write \(I=\{i:a_i\text{ is initially white}\}\) and \(J=\{j:b_j\text{ is initially white}\}\). The initial blue set is zero forcing exactly when
\[
|I|\le2,\qquad |J|\le2,\qquad (|I|=|J|=2\Longrightarrow I\ne J).
\]
The complete generating polynomial is
\[
Z(H_n;x)=x^{2n-4}\left[\binom n2\left(\binom n2-1\right)+n^2(n-1)x+\binom{2n}2x^2+2nx^3+x^4\right].\tag{1}
\]
In particular, the minimum size is \(2n-4\), with exactly \(\binom n2(\binom n2-1)\) minimum sets. Every zero-forcing set contains one of these minimum sets, so all inclusion-minimal zero-forcing sets have the same cardinality.

**Complex zeros.** The four nonzero zeros are all simple. For every \(n\ge5\), their real parts equal \(-n/2\); for \(n=3,4\), exactly two of them are negative real numbers and the other two form a complex-conjugate pair on \(\operatorname{Re}x=-n/2\). The additional root at \(x=0\) has multiplicity \(2n-4\).

## Assumptions and scope

Graphs are finite, simple, undirected, and labeled by the displayed partite indices. A zero-forcing set means an initial blue set from which a sequence of standard one-white-neighbor color changes colors every vertex blue. The counting polynomial uses one indeterminate and ordinary (not skew, positive-semidefinite, or \(k\)-) zero forcing. The claim covers exactly \(n\ge3\), including the six-cycle \(H_3\).

## Proof

**Necessity.** If \(|I|\ge3\), every blue vertex of \(B\) is adjacent to at least two still-white vertices of \(A\). Thus no first change can turn a white \(A\)-vertex blue. Even if changes occur on the \(B\)-side, the number of white \(A\)-vertices remains at least three, so this obstruction persists. Similarly \(|J|\le2\) is necessary. If \(|I|=|J|=2\) with \(I=J\), each blue \(A\)-vertex sees both white \(B\)-vertices and each blue \(B\)-vertex sees both white \(A\)-vertices. No first force exists, making the set infeasible.

**Sufficiency.** Consider a pair \((I,J)\) satisfying the three conditions. If both are empty, there is nothing to force. If one side has exactly one white vertex and the other side none, a blue vertex on the opposite side with a different index forces it; such a vertex exists because \(n\ge3\). If \(|I|=|J|=1\), select a blue \(a_k\) with \(k\notin I\cup J\), possible for \(n\ge3\). It forces the sole white \(B\)-vertex, and a suitable blue \(B\)-vertex then forces the remaining white \(A\)-vertex. When \(J\) has size two and \(I\) at most one, choose \(j\in J\setminus I\); the blue vertex \(a_j\) sees exactly the other white \(B\)-vertex and forces it, reducing to an already treated case. The symmetric construction handles \(|I|=2\) and \(|J|\le1\): a blue \(b_i\) with \(i\in I\setminus J\) forces the other white \(A\)-vertex. Finally, when \(|I|=|J|=2\) with \(I\ne J\), choose \(j\in J\setminus I\); the blue \(a_j\) forces one white \(B\)-vertex, reducing to \((|I|,|J|)=(2,1)\). This proves the exact classification.

**Counting.** Enumerate choices by the total number of omitted vertices. For omitted total \(0,1,2,3,4\), the respective counts are \(1\), \(2n\), \(\binom{2n}2\), \(2n\binom n2=n^2(n-1)\), and \(\binom n2^2-\binom n2\). Every omitted total at most two is feasible, while an omitted total of three must have side occupancies \((2,1)\) or \((1,2)\). The classification proves these are all cases and gives (1).

**Inclusion-minimal sets.** Given feasible \(I,J\), choose two-subsets \(I^\ast\supseteq I\), \(J^\ast\supseteq J\) with \(I^\ast\ne J^\ast\). This is always possible for \(n\ge3\): if one original set already has size two, avoid that two-set in extending the other, while if both have size at most one there are at least three two-subsets of \([n]\) and one can choose two distinct extensions. Their complement is a zero-forcing subset of the initial blue set, of size \(2n-4\). Conversely no initial set of smaller size is feasible by the classification. This proves the inclusion-minimal and exact-count statements.

**Zero locations.** Write \(Q_n(x)=Z(H_n;x)/x^{2n-4}\) and center the variable at \(x=y-n/2\). Direct integer-coefficient expansion yields
\[
Q_n(y-n/2)=y^4+\frac{n(n-2)}2y^2+\frac{n(n^3-4n^2-4n+8)}{16}.\tag{2}
\]
The two solutions for \(y^2\) are
\[
-\frac{n(n-2)}4\pm\sqrt{\frac{n(n-1)}2}.\tag{3}
\]
For \(n\ge5\), both values in (3) are strictly negative: squaring the required inequality reduces it to \(n(n-2)^2>8(n-1)\), true at \(n=5\) and strictly increasing thereafter. These values are distinct and nonzero, so all four corresponding \(y\)-roots are simple and imaginary, establishing the common real part. For \(n=3,4\), (3) has one positive and one negative value, yielding two real roots and a nonreal pair. The same nonzero/distinct observation establishes simplicity in all cases.

## Verification

The independent implementations in `verify.py` compare standard sequential zero forcing with the displayed side-index classification on every labeled initial vertex subset for \(n=3,\ldots,10\): 1,398,080 subset checks. A separately coded simultaneous-round forcing implementation agrees for \(n=3,\ldots,7\), totaling 21,824 additional checks. All 1,696 zero-forcing sets for \(n=3,\ldots,7\) were independently checked to contain some permitted minimum set. Exact polynomial algebra checked (2) and (3) for eight small orders. All finite checks passed; see `verification_output.txt`. The proof above, not the finite enumeration, establishes the universal assertions.

## Relationship to prior work

Boyer et al. introduce the zero-forcing polynomial and give complete-polynomial examples including complete bipartite graphs; deleting a perfect matching destroys their complete-bipartite hypotheses and changes the degree and coefficients. Jacob examines the zero-forcing span of several graph classes, including graphs obtained by deleting a matching from a complete graph (a different family). Grood et al. introduce well-forcedness and prove it for complete multipartite graphs; a crown graph \(H_n\) for \(n\ge3\) is not complete multipartite. The theorem here contributes the full standard zero-forcing enumerator of crown graphs together with its inclusion-minimality and exact root geometry; it does not claim that standard zero forcing, minimum zero-forcing cardinality, or the general well-forced notion is new.

## Limitations

These formulas apply to matching-deleted **balanced** complete bipartite graphs, not arbitrary bipartite graphs or larger matching-deletion patterns. The proof does not classify every possible forcing sequence. Originality assessments cannot rule out inaccessible, unindexed, or differently phrased earlier equivalent formulas. No independent external audit has been completed.

## References

1. B. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, C. Reinhart, *The zero forcing polynomial of a graph*, arXiv:1801.08910v1 (public 26 January 2018), especially definitions and complete-bipartite formula.
2. B. Jacob, *The zero forcing span of a graph*, arXiv:2309.06234v1 (public 12 September 2023), especially the comparison with complete graphs minus matchings.
3. H. Grood et al., *Well-forced graphs*, arXiv:2312.14298v1 (public 21 December 2023), especially complete multipartite and tree results.
