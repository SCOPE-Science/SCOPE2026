# The six extremal minimal dominating sets of an even ladder

## Finding
For an integer \(n\geq1\), let \(L_n=P_2\square P_n\) be the ladder graph. A dominating set \(D\subseteq V(L_n)\) is *minimal* if no proper subset is dominating. For each column \(j\), encode \(D\) by \(s_j\in\{0,1,2,3\}\), with bit 0 indicating selection of its upper vertex and bit 1 indicating selection of its lower vertex. Thus \(0\) means empty and \(3\) means full.

**Theorem (complete extremal classification).** Every inclusion-minimal dominating set of \(L_n\) contains at most \(n\) vertices. Equality holds if and only if \(s_1s_2\cdots s_n\) is a prefix of one of the following six periodic words:
\[
1^\infty,\qquad 2^\infty,\qquad
(12)^\infty,\qquad(21)^\infty,\qquad
(3003)^\infty,\qquad(0330)^\infty.
\]
The final two words are admissible **only when \(n\) is even**. Consequently, writing \(M_n\) for the number of largest inclusion-minimal dominating sets,
\[
\Gamma(L_n)=n,\qquad
M_n=\begin{cases}2,&n=1,\\4,&n\ge3\text{ odd},\\6,&n\ge2\text{ even}.\end{cases}
\]
Here \(\Gamma\) is upper domination. The scalar identity \(\Gamma(L_n)=n\) is known from the bipartite grid upper-domination theorem; the claimed refinement is the classification and enumeration of **all** equality cases.

## Assumptions and scope
Graphs are finite, undirected and simple. The ladder has two ordered rows and \(n\ge1\) ordered columns. The code \(1\) selects the first row only; \(2\) the second. A prefix is taken beginning at the first symbol of the infinite periodic word, without an arbitrary cyclic shift. All six candidate types are listed with their precise parity requirement. Distinct row/column-labelled vertex subsets are counted separately. At \(n=1\), the first four prefixes duplicate in pairs, yielding two sets.

## Proof
A selected vertex \(v\in D\) has a *private witness* when a vertex \(w\in N[v]\) satisfies \(N[w]\cap D=\{v\}\). The standard elementary equivalence is:
\[
D\text{ is inclusion-minimal dominating}\iff
D\text{ dominates and each }v\in D\text{ has a private witness}.
\]
Indeed removal of \(v\) destroys domination exactly when a vertex is dominated by \(v\) alone. On a ladder, domination of a vertex in column \(j\) and existence of its private witness are decided by the five columns \(j-2,\ldots,j+2\), since a witness is at graph distance at most one from \(v\), and its closed neighborhood is another step away. Outside the ladder, we put the special sentinel symbol \(4\); it is not a selectable column.

Here is a finite-state exact proof of the classification, with complete executable details in `verify.py`. A state consists of the four most recently read column symbols, one of three closing phases, and a Boolean indicating whether a genuine column was read. Start from four sentinels. In the body, append any of \(0,1,2,3\); after at least one body column, close with exactly two sentinel symbols. On appending \(e\), test the central column of the resulting five-column window using the private-witness equivalence. Reject the transition if it fails. After both sentinels, accept. Every accepted path is exactly one minimal dominating set, and vice versa: the two sentinels check the rightmost two columns, while initial sentinels handle the left boundary.

For each transition whose central column has genuine symbol \(c\), give weight \(\operatorname{popcount}(c)-1\); sentinel-centered transitions have weight zero. Every column is tested exactly once, hence every complete path has total weight \(|D|-n\). The reachable finite automaton has **229 states, 471 transitions and 10 final states**. The standalone exact-integer algorithm computes a potential \(h\) with \(h(\mathrm{start})=0\), checks \(h(v)\ge h(u)+w(u,v)\) for **all 471 edges**, and checks \(h(t)\le0\) for **every final state** (maximum zero). It also verifies convergence of the finite max-plus relaxation without a positive-weight cycle. Summing the inequalities over any accepting path shows \(|D|-n\le0\).

To identify equality, every edge on a zero-weight complete path must be tight: \(h(v)=h(u)+w(u,v)\). Retain only tight edges that can still reach a zero-potential final state. Intersect that finite-state language with a six-pattern prefix tracker: one bit per candidate periodic word, updated on each genuine symbol, with a four-position residue and unchanged bits on sentinels. The exact reachable product has **91 states**, with **zero terminal states having all six pattern bits cleared**. Thus every equality-case word is a prefix of one of the six listed periodic words.

Conversely, the constant-row patterns and alternating single-vertex patterns dominate and are minimal at every length: in the constant-row cases the unselected mate provides each selected vertex's private witness, and in alternating cases every selected vertex witnesses itself. In the periodic \(3003\) and \(0330\) patterns for even lengths, each empty rung is adjacent to a selected full rung and each full rung has an adjacent empty rung whose vertices are private witnesses for its two selected vertices. Every such word selects exactly \(n\) vertices. For odd lengths, these full/empty-rung patterns either leave the rightmost empty rung undominated or leave the rightmost full rung without a private witness; the executable local predicate tests the boundary generally. There are therefore two distinct maximum sets at \(n=1\), four for odd \(n\ge3\) and six for even \(n\ge2\).

The finite computation is an exhaustive proof on a **fixed** state graph of size 229 valid for every \(n\), not an inference from testing finitely many ladder lengths. Exact integer checks and full source are included in `verify.py`.

## Verification
Run `python3 verify.py` using Python 3.10 or later from the directory containing the artifacts. The recorded stdout is `verification_output.txt`. It generates the entire finite automaton from the five-column predicate; checks the 229-state/471-edge graph, terminal potentials, each longest-path inequality, and language containment; then independently enumerates all \(2^{2n}\) vertex subsets for each \(1\le n\le9\) using a direct closed-neighborhood formulation. The latter checks 349,524 candidate subsets in total, and independently finds equality-case counts \(2,6,4,6,4,6,4,6,4\). The finite-length brute force supports but does not establish the infinite theorem; that depends on the complete finite-state certificate described above.

## Relationship to prior work
Sahbi, *Upper k-Star-Forming Sets, k-Independence, and Upper Domination*, arXiv:2610.03785 (first posted September 30, 2026), Theorem 8.1, records \(\Gamma(P_m\square P_n)=\lceil mn/2\rceil\) for all rectangular grids, using the classical bipartite equality \(\Gamma=\alpha\). This theorem already implies the **scalar** upper-domination number here, so that scalar is not claimed new; the inspected article does not classify its maximizing minimal dominating sets. Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph*, arXiv:2408.08053, counts **all** dominating sets by cardinality, without directly filtering the inclusion-minimal maximizers. OEIS A290379 (Weisstein/Howroyd) enumerates **all minimal dominating sets** of \(L_n\) without separating their cardinalities; its values for \(1\le n\le9\) agree with the independent brute-force check. None of these data gives the complete equality classification by direct statement or numerical implication.

## Limitations
The result concerns width-two ladders only, not wider grids, cylinders, or total domination. The executable certificate supplies a finite-state exhaustive proof, not a hand-derived concise recurrence for the full minimal-domination polynomial. No absolute novelty conclusion is inferred from unsuccessful searches; equivalent historical classifications, possibly in unindexed literature, remain a residual risk.

## References
1. R. Sahbi, *Upper k-Star-Forming Sets, k-Independence, and Upper Domination*, arXiv:2610.03785v2 (2026), especially Theorems 2.4 and 8.1. https://arxiv.org/abs/2610.03785
2. S. Mertens, *Domination Polynomials of the Grid, the Cylinder, the Torus, and the King Graph*, arXiv:2408.08053 (2024). https://arxiv.org/abs/2408.08053
3. E. W. Weisstein and A. Howroyd, *Number of minimal dominating sets in the n-ladder graph*, OEIS A290379 (2017). https://oeis.org/A290379
