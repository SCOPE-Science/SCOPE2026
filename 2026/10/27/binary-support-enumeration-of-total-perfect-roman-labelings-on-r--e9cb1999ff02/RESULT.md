# Binary-support enumeration of total perfect Roman labelings on rook graphs

## Finding

Let \(2\le p\le q\) and let \(R_{p,q}=K_p\square K_q\), whose vertices are the cells of a \(p\)-row, \(q\)-column board, with adjacency when exactly one coordinate agrees. A *total perfect Roman dominating function* (TPRDF) is a labeling \(f:V(R_{p,q})\to\{0,1,2\}\) such that each zero-labeled vertex has exactly one neighbor labeled \(2\) and the vertices labeled \(1\) or \(2\) induce a graph without isolated vertices. Its weight is the sum of its labels. Define

\[\mathcal T_{p,q}(z)=\sum_{f\text{ TPRDF}}z^{\sum_v f(v)}.\]

For each nonempty subset \(H\subseteq[p]\times[q]\), interpret \(H\) as the cells labeled \(2\), with size \(t=|H|\). Let \(a_i\) and \(b_j\) denote the numbers of cells of \(H\) in row \(i\) and column \(j\), and write \(r_s=|\{i:a_i=s\}|\) and \(c_s=|\{j:b_j=s\}|\) for \(s=0,1\). Put

\[u(H)=r_1c_0+r_0c_1,\qquad b(H)=pq-t-u(H).\]

Let \(\epsilon(H)=1\) when either \(t=1\), or \(H\) is a matching in the row-column incidence graph \(K_{p,q}\) that leaves exactly one row and one column uncovered; in all other cases set \(\epsilon(H)=0\). The latter matching case requires \(p=q=t+1\). Then the **complete total perfect Roman weight polynomial** is

\[\boxed{\mathcal T_{p,q}(z)=z^{pq}+\sum_{\varnothing\ne H\subseteq[p]\times[q]}z^{2t+b(H)}\big((1+z)^{u(H)}-\epsilon(H)\big).}\]

This is an exact finite sum over *binary* defender supports, not an enumeration over all ternary labelings. Every coefficient can be evaluated directly from the row/column degree-zero and degree-one counts of those supports. A necessary and sufficient feasibility classification for every complete labeling is given in the proof.

The minimum weight, included for completeness rather than claimed as a new minimum-parameter determination, is

\[\gamma^p_{tR}(R_{p,q})=2p.\]

If \((p,q)\ne(2,2)\), every minimum labeling consists of \(2\)'s on one entire column and \(0\)'s elsewhere, or (only if \(p=q\)) \(2\)'s on one entire row and \(0\)'s elsewhere. The number of minimum labelings is therefore \(q+p\mathbf1_{\{p=q\}}\). For \((p,q)=(2,2)\), there are exactly \(13\) minimum labelings: four entire-row/column \(2\)-placements, eight functions with one \(2\), one adjacent optional \(1\), one forced opposite \(1\), and one remaining \(0\), and the all-\(1\) function.

For instance, \(\mathcal T_{2,2}(z)=13z^4+12z^5+6z^6+4z^7+z^8\); the coefficients at weights \(4,5,6,7,8\) count all \(36\) valid functions.

## Assumptions and scope

All graphs are finite, undirected, and simple. The parameters are integers \(2\le p\le q\); rows and columns are labeled. No asymptotic assumptions are made. In the support formula, a matching means that no two selected cells share a row or column. All weight exponents are nonnegative integers. The polynomial counts labeled functions, with no quotient by graph automorphisms.

## Proof

Fix the set \(H\) of cells receiving label \(2\). A cell outside \(H\) in row \(i\) and column \(j\) has exactly \(a_i+b_j\) neighbors labeled \(2\). The cells eligible to receive label \(0\) are consequently exactly

\[U(H)=\{(i,j):a_i+b_j=1\},\qquad |U(H)|=r_1c_0+r_0c_1=u(H).\]

No cell of \(H\) lies in \(U(H)\). Every cell outside \(H\cup U(H)\) is forced to carry label \(1\), giving \(b(H)=pq-t-u(H)\) mandatory ones. Every cell in \(U(H)\) can independently be labeled \(0\) or \(1\), *subject only to totality*, as classified next. Call the set of optional cells assigned \(1\) by \(J\subseteq U(H)\).

If \(H=\varnothing\), no cell can be labeled \(0\). The all-\(1\) function is valid because the rook graph has no isolated vertices, contributing \(z^{pq}\). If \(t=1\), the unique \(2\)-cell has no positive neighbor among mandatory ones: they lie in the opposite subrectangle. Hence \(J\) must be nonempty, and this condition is sufficient. Indeed, every optional one is adjacent to the lone \(2\); the opposite rectangle of mandatory ones has at least two adjacent cells unless \(p=q=2\), in which case its sole vertex is adjacent to any chosen optional one. This gives the factor \((1+z)^u-1\).

Suppose \(t\ge2\). Every cell labeled \(2\) has a positive neighbor. If another selected \(2\) shares its row or column, this is immediate. Otherwise, take a different selected cell in another row and column: the cross-cell sharing the first row and second column is either itself a \(2\) or a mandatory \(1\), hence is a positive neighbor. Every optional \(1\) has exactly one \(2\)-neighbor. Every mandatory \(1\) in a row or column containing a \(2\) is adjacent to one of those \(2\)'s.

The only remaining mandatory ones lie in the subrectangle of rows and columns containing no \(2\)'s. If that rectangle contains at least two cells, its induced rook graph has no isolated vertex. If it is empty, there is no issue. Its only potentially isolated case is a single cell, so \(r_0=c_0=1\). This corner cell already has a mandatory positive neighbor if some occupied row or occupied column has at least two \(2\)'s (the cell at the corresponding row or column, respectively, is a mandatory \(1\)). Otherwise every occupied row and column has degree one, so \(H\) is a matching; because exactly one row and one column are uncovered, necessarily \(p=q=t+1\). In that case, the mandatory corner has a positive neighbor exactly when \(J\ne\varnothing\). These exhaust all support failures and prove the stated polynomial, since a chosen \(J\) contributes weight \(2t+b(H)+|J|\).

For the minimum, write \(d=p-t\) when \(1\le t<p\). At least \(d\) rows contain no \(2\). In each such row, at least \(q-c_1\) cells are mandatory ones. As \(c_1\le t\),

\[b(H)\ge r_0(q-c_1)\ge d(q-t)\ge d^2.\]

Since every function has weight \(2t+b(H)+|J|\), it suffices to show \(b(H)+|J|>2d\) unless \((p,q,t)=(2,2,1)\). For \(d\ge3\), the displayed bound gives strict inequality. For \(d=2\), equality in \(b\ge4\) requires \(q=p\), \(r_0=d\), and \(c_1=t\). Then the \(t\) defenders occupy distinct rows and columns. If \(t\ge2\), their off-diagonal crossing cells provide \(t(t-1)\) additional mandatory ones; if \(t=1\), at least one optional \(1\) is required for totality. Either way the inequality is strict.

For \(d=1\), the bound is strict if \(q\ge p+2\). If \(q=p+1\), equality in \(b\ge2\) requires one defender in each of \(t\) distinct rows and columns, again creating \(t(t-1)\) additional mandatory ones when \(t\ge2\); the \(t=1\) case requires an optional one. If \(q=p\) and \(c_1<t\), at least one occupied column has two defenders, so \(c_1\le t-2\) and \(b\ge3\). Otherwise \(c_1=t\): the defenders lie in distinct columns and there is one completely uncovered column. If exactly one row is uncovered, the defenders lie in distinct rows and, for \(t\ge2\), the uncovered corner plus off-diagonal crossings give \(b\ge1+t(t-1)\ge3\). If at least two rows are uncovered, some occupied row has at least two defenders; its mandatory one in the unoccupied column is additional to the at least two mandatory ones in the uncovered rows, so \(b\ge3\). The remaining case \(t=1\), \(p=q=2\) satisfies \(b=1\) and requires \(|J|\ge1\), giving equality with weight \(4\).

For \(t\ge p\), weight is at least \(2t\ge2p\). Equality requires \(t=p\) and no ones. Totality then forces two defenders to be adjacent in the rook graph, so they share a row or column. If they share a row, every other cell in that row must also be a defender (otherwise it would be zero with at least two \(2\)-neighbors), hence \(q\le t=p\), which forces \(p=q\) and exactly a full row of defenders. If they share a column, that entire column must likewise contain defenders, yielding exactly one full column. Both types are valid. For \(t=0\), the all-one function has weight \(pq\), equal to \(2p\) only at \((p,q)=(2,2)\). The minimum count follows. In the remaining exceptional \(2\)-by-\(2\) case, with exactly one defender, one of its two neighbors must be labeled \(1\); choosing the defender and this neighbor gives eight assignments. This completes the proof.

## Verification

The standalone `verify.py` independently generates all ternary labelings, tests the literal total perfect Roman definition using graph adjacency, and compares every coefficient against a separate binary-support implementation. Exhaustive comparisons cover six rectangles: \((2,2),(2,3),(2,4),(2,5),(3,3),(3,4)\), totaling \(617544\) ternary assignments examined. Independent support-side checks extend to \((4,4)\) and \((4,5)\), involving \(65536\) and \(1048576\) defender supports. The certificate is `verification_output.txt`; it is generated by running `python verify.py`. Both scripts are self-contained and require only Python's standard library. Finite checks corroborate, but do not prove, the infinitely quantified theorem.

## Relationship to prior work

A. Almulhim introduced total perfect Roman domination and studied its complexity, multipartite values, and general bounds in *Total Perfect Roman Domination* (2023). A. Almulhim, A. D. Akwu, and B. Al Subaiei studied perfect Roman domination for Cartesian products of paths and cycles (2022), not products of complete graphs nor total perfect functions. M. A. Henning and W. F. Klostermeyer gave general regular-graph perfect Roman bounds (2018), without the enumerator derived here. Earlier work computing *perfect* Roman minima for rook graphs already provides the scalar \(2p\) lower bound, because every total perfect function is perfect Roman. Thus the minimum weight is not advanced as a novel result. The distinctive statement here is the exact **complete total-perfect weight enumerator**, its degree-profile support reduction and the exceptional totality criterion. The complete enumerator does not follow from knowledge of a single minimum, a general bound, or an enumerator for a different product family.

## Limitations

The formula is a finite, potentially exponential sum over subsets of an incidence board; it does not claim a polynomial-time method when both dimensions vary. The proof applies only when both complete-graph factors have order at least two. It does not enumerate perfect Roman labelings lacking the totality condition, nor variants of the Roman rule. The priority assessment is limited by search coverage; equivalent unindexed literature could exist. The mathematical proof has not undergone independent review.

## References

1. A. Almulhim, *Total Perfect Roman Domination*, Symmetry **15** (2023), article 1676, DOI: 10.3390/sym15091676; first public page dated 31 August 2023.
2. A. Almulhim, A. D. Akwu, B. Al Subaiei, *The Perfect Roman Domination Number of the Cartesian Product of Some Graphs*, Journal of Mathematics **2022**, 1957027, DOI: 10.1155/2022/1957027; first published 18 October 2022.
3. M. A. Henning, W. F. Klostermeyer, *Perfect Roman domination in regular graphs*, Applicable Analysis and Discrete Mathematics **12** (2018), 143–152, DOI: 10.2298/AADM1801143H.
