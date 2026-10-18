# Exact three-colour census and sharp deletion budget for a two-atom dependence disjunction

## Finding

Let \(C=\{0,1,2\}\), let \(n\geq0\), and let the underlying \((x,y)\)-support be the full labelled bipartite graph \(K_{2,n}\). For every assignment of one value \(c_{ij}\in C\) to each edge, form the team
\[
T_c=\{(i,j,c_{ij}): i\in\{0,1\},\ j\in\{1,\ldots,n\}\}.
\]
Under ordinary lax team-splitting semantics, write
\[\Phi=\operatorname{dep}(x,z)\vee\operatorname{dep}(y,z).\]
For all \(n\ge0\), the exact number of the \(9^n\) colourings for which \(T_c\models\Phi\) is
\[
\boxed{N_n=3\cdot7^n+6\cdot6^n-21\cdot5^n+18\cdot4^n-5\cdot3^n.}
\]
Define the deletion distance \(\delta(c)\) to be the minimum number of assignments removed from \(T_c\) to make \(\Phi\) true. Then every three-colouring has the exact repair formula
\[
\boxed{\delta(c)=\min_{r,s\in C}\#\{j:c_{0j}\ne c_{1j},\ c_{0j}\ne r,\ c_{1j}\ne s\}.}
\]
Moreover the sharp worst-case deletion budget is
\[
\boxed{\max_{c}\delta(c)=\lfloor n/3\rfloor.}
\]
Thus the uniform random satisfaction probability is \(N_n/9^n=3(7/9)^n+O((2/3)^n)\), which tends to zero, although every input admits repair by deleting at most \(\lfloor n/3\rfloor\) of its \(2n\) assignments.

## Assumptions and scope

Each \((i,j)\) occurs exactly once in the team; its consequent value belongs to exactly three named values. The two vertices on the \(x\) side and the \(n\) vertices on the \(y\) side are labelled. Colourings are counted individually, not modulo permutation of colours or vertices. A deletion may remove any entire assignment, and no changes or insertions are allowed. The empty team for \(n=0\) satisfies \(\Phi\); the formulas give \(N_0=1\) and deletion budget zero. The disjunction is lax, permitting overlapping covering subteams, and its downward-closed dependence atoms permit replacement by a disjoint split.

## Proof

**Step 1: exact splitting and repair reduction.** Suppose \(T_c=U\cup V\), with \(U\models\operatorname{dep}(x,z)\) and \(V\models\operatorname{dep}(y,z)\). Each of the two \(x\)-vertices has a single \(z\)-value throughout its incident assignments in \(U\), when any exist; extend this partial map arbitrarily to values \(r,s\in C\). Likewise each \(y\)-vertex has a unique \(z\)-value in \(V\), when any exist. Consequently each edge's colour agrees with the chosen colour of at least one endpoint. Conversely, from such endpoint colours put an edge in \(U\) when its colour agrees with the \(x\)-endpoint, and otherwise in \(V\); both dependencies hold. This equivalence also applies to any retained subteam.

Write the two edge colours at column \(j\) as \((a_j,b_j)\). Fix the two \(x\)-endpoint colours \((r,s)\). If \(a_j=b_j\), the right endpoint can cover both edges. If the colours differ, both edges can be retained precisely when \(a_j=r\) or \(b_j=s\): whichever edge is not covered by its left endpoint determines the right endpoint's colour. Otherwise at least one edge must be deleted, and one deletion suffices. Columns are independent once \(r,s\) are fixed. Minimizing over all nine pairs \((r,s)\) gives the displayed exact distance formula. In particular, zero distance is equivalent to the existence of one such pair covering every column.

**Step 2: exact all-size count.** Let \(Q=C\times C\) be the nine possible column types, and for each \((r,s)\in Q\), let
\[
A_{r,s}=\{(a,b)\in Q:a=b\text{ or }a=r\text{ or }b=s\}.
\]
By Step 1, a length-\(n\) word of column types satisfies \(\Phi\) exactly when all letters lie in at least one of the nine \(A_{r,s}\). There are three sets of cardinality seven (\(r=s\)) and six of cardinality six (\(r\ne s\)). Ordinary inclusion–exclusion gives the *exact identity for every integer* \(n\ge0\)
\[
N_n=\sum_{\varnothing\ne I\subseteq C\times C}(-1)^{|I|+1}\left|\bigcap_{(r,s)\in I}A_{r,s}\right|^n.
\]
The remaining finite arithmetic is entirely independent of \(n\). Enumerate each of the \(2^9-1=511\) nonempty index subsets; the following table reports the numbers of odd- and even-cardinality index subsets yielding an intersection of each size:

| Intersection size | Odd index subsets | Even index subsets | Difference |
| ---: | ---: | ---: | ---: |
| 3 | 187 | 192 | -5 |
| 4 | 54 | 36 | 18 |
| 5 | 6 | 27 | -21 |
| 6 | 6 | 0 | 6 |
| 7 | 3 | 0 | 3 |

To verify each entry without any search, form the nine explicitly specified sets \(A_{r,s}\), run through the binary masks \(1,\ldots,511\), intersect exactly those sets corresponding to one-bits, and increment the indicated parity bin. This is a finite exhaustive proof of the table, reproduced from scratch by the included standard-library checker. Multiplying each difference by the corresponding \(k^n\) gives the claimed formula, including \(n=0\).

**Step 3: sharp repair budget.** For each \(t\in C\), consider the admissible left-colour pair \((r,s)=(t,t)\). Every unequal column type \((a,b)\) avoids exactly one of the three values of \(t\), namely the third colour distinct from both \(a,b\), while an equal column avoids none. Therefore, summing the numbers of columns requiring one deletion under these three choices gives at most \(n\). At least one choice requires no more than \(\lfloor n/3\rfloor\) deletions, establishing the upper bound.

For sharpness, distribute the \(n\) columns as evenly as possible among the three ordered types \((0,1),(1,2),(2,0)\), so each occurs at least \(\lfloor n/3\rfloor\) times. Every fixed pair \((r,s)\) can cover at most two of these three types, because the three first entries and the three second entries are respectively all distinct and no row-column pair covers the entire directed cycle. Thus at least one type, appearing at least \(\lfloor n/3\rfloor\) times, remains uncovered and must lose an assignment in every such column. The exact distance formula gives the opposite inequality and proves sharpness.

**Step 4: probability consequence.** Under independent uniform colours, all \(9^n\) column sequences are equiprobable. Division by \(9^n\) proves the probability identity; the leading exponential base seven yields the stated asymptotic. This probability conclusion does not assert independence among the nine possible splitting strategies.

## Verification

Run `python3 verify.py` with Python 3.10 or newer. It independently reconstructs all nine template sets and all 511 nonempty inclusion–exclusion masks, checks the finite parity table, and explicitly enumerates genuine split partitions using the defining dependencies for every three-colouring of \(K_{2,n}\) with \(0\le n\le4\). For nontrivial cases in this range it independently enumerates deletion subsets before applying the split evaluator; the exact distance formula is checked for every colouring. The checker also enumerates all \(9^5=59{,}049\) colourings at \(n=5\) for the zero-repair count, and checks balanced directed-cycle witnesses through \(n=19\). All tests passed. The infinite family of identities follows from the proof, not from finitely many team enumerations.

Sample counts are \(N_0=1\), \(N_1=9\), \(N_2=81\), \(N_3=717\), \(N_4=6057\), and \(N_5=48669\). The first non-satisfying full-support three-colour teams occur for \(n=3\), with exactly twelve labelled colourings.

## Relationship to prior work

Fröhlich, Kolaitis, and Meier (first preprint in 2025) study complexity and coherence of disjunctions of dependence atoms, including the precise formula \(\operatorname{dep}(x,z)\vee\operatorname{dep}(y,z)\). Their published results do not state an exact labelled-colouring census or optimal assignment-deletion distances for the fixed full support \(K_{2,n}\). Fröhlich, Häggblom, Hirvonen, and Hirvonen (2026) study approximate functional dependencies and disjunction model checking, providing a concrete motivation for the deletion formulation; their stated general complexity and implication results do not directly give these specialised formulas.

A previously established pseudoforest criterion characterizes supports whose *every* three-colouring satisfies this same disjunction. That zero-versus-nonzero robustness criterion implies only that all colourings are accepted at \(n\le2\), and that some are rejected at \(n\ge3\), not their exact numbers or worst-case repair costs. The present result is the all-\(n\) quantitative enumeration and sharp repair bound for a fixed two-row support. These are specialized new deductions, not claims to discover the semantics, the initial robustness threshold, or a general polynomial-time repair theorem for arbitrary supports.

## Limitations

The theorem assumes a complete, simple, labelled two-by-\(n\) support and exactly three available consequent values. It does not classify arbitrary bipartite supports or larger alphabets. It measures deletions of entire assignments only. A numerical coincidence with an existing combinatorial sequence, or derivability from an as-yet-unlocated general covering theorem, remains a possible historical-priority risk. The verification program is a finite exhaustive corroboration plus an exhaustive calculation of the constant template identity; independent audit of the general mathematical proof has not been performed.

## References

1. Nicolas Fröhlich, Phokion G. Kolaitis, Arne Meier, *Disjunctions of Two Dependence Atoms*, arXiv:2508.16146 (first public 2025-08-22); *Leibniz International Proceedings in Informatics* 363 (CSL 2026), article 10, DOI:10.4230/LIPIcs.CSL.2026.10. Public HTML: https://drops.dagstuhl.de/storage/00lipics/lipics-vol363-csl2026/html/LIPIcs.CSL.2026.10/LIPIcs.CSL.2026.10.html.
2. Nicolas Fröhlich, Matilda Häggblom, Åsa Hirvonen, Minna Hirvonen, *Approximate Functional Dependencies—Implication Problem Revisited*, arXiv:2608.16570 (first public 2026-08-17).
