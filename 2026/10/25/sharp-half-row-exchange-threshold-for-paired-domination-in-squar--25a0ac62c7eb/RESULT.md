# Sharp half-row exchange threshold for paired domination in square rook graphs

## Finding
For each even integer \(m=2h\ge4\), the square rook graph \(R_m=K_m\square K_m\) has paired-domination number \(\gamma_{\mathrm{pr}}(R_m)=m\). Every minimum paired-dominating set belongs to precisely one of two types: one vertex in each row with all column occupancies even, or one vertex in each column with all row occupancies even. Their total number is
\[
N_m=2m!\,[z^m](\cosh z)^m.
\]
On the minimum sets, define the batch-\(r\) exchange graph \(X_r\) by joining distinct sets \(S,T\) if \(|S\setminus T|=|T\setminus S|\le r\). Then \(X_1\) has no edges, \(X_r\) has exactly two connected components for \(2\le r<h\), and \(X_r\) is connected if and only if \(r\ge h\). Thus the exact least batch size allowing full optimum-preserving reconfiguration is \(m/2\).

## Assumptions and scope
The vertex set is \([m]\times[m]\), with two distinct vertices adjacent exactly when they share a row or share a column. A set dominates if every vertex belongs to it or has a neighbor in it. It is *paired dominating* if it dominates and the induced subgraph has a perfect matching. Only **minimum-cardinality** paired-dominating sets are reconfiguration states. A batch exchange removes and inserts the same number of vertices simultaneously; feasibility of intermediate partial exchanges is **not** required. All quantifiers are for even \(m\ge4\) and integer \(r\ge1\). The symbol \([z^m]\) means coefficient extraction in a formal power series. No regularity or diameter assertion for general \(m\) is made.

## Proof
**Step 1: the sharp cardinality bound.** If a dominating set misses some row \(i\) and some column \(j\), the cell \((i,j)\) has no selected cell in its closed neighborhood, a contradiction. Consequently a dominating set meets every row or meets every column, and hence contains at least \(m\) cells. Conversely, all \(m\) cells in one fixed column induce \(K_m\), which has a perfect matching because \(m\) is even. Therefore \(\gamma_{\mathrm{pr}}(R_m)=m\).

**Step 2: characterization and count.** Any dominating set of size exactly \(m\) must meet every row exactly once or every column exactly once. In the row-once case write \(S_f=\{(i,f(i)):i\in[m]\}\). Distinct selected cells lie in distinct rows, so the induced graph is the disjoint union of cliques of orders \(a_j=|f^{-1}(j)|\), for \(j\in[m]\). Each clique has a perfect matching if and only if its order is even; empty cliques are permitted. Thus precisely the even-fiber functions \(f\) qualify. Interchanging coordinates yields the column-once class. A set meeting both constraints has only isolated selected cells and hence cannot be paired dominating for \(m\ge2\), so the classes are disjoint. Assigning an even number \(2k_j\) of labeled rows to each column gives \(m!/\prod_j(2k_j)!\) possibilities whenever \(\sum_j2k_j=m\). Summing gives \(m![z^m](\cosh z)^m\) per class, twice that in all.

**Step 3: the one-replacement obstruction.** Within a row-once configuration, replacing one cell must retain the same row, because there are still only \(m\) selected cells. Changing its column toggles the parity of two column occupancies, so the result is not paired dominating. The dual argument applies within column-once configurations. The two classes cannot be adjacent by a one-replacement move either, by Step 5, because \(h\ge2\). Hence \(X_1\) is edgeless.

**Step 4: connectedness within each orientation from batch size two.** Given any even-fiber function \(f\) and a fixed target column \(c\), repeatedly choose a column \(a\ne c\) having at least two selected cells and move two of its row-labeled selected cells from \(a\) to \(c\). This replaces exactly two selected vertices and preserves all fiber parities. Repetition ends at the constant function \(f(i)=c\). Hence every row-once configuration reaches the same canonical one through batch-two exchanges. Coordinate transposition proves the analogous statement for the column-once class.

**Step 5: the sharp cross-class threshold.** A row-once configuration meeting the pairing condition occupies at most \(h=m/2\) distinct columns, since every occupied column contains at least two selected cells. A column-once configuration has only one selected cell per column, so its intersection with any row-once configuration contains at most \(h\) vertices. Therefore a cross-class exchange removes at least \(m-h=h\) vertices. Conversely, relabel rows and columns \(0,\dots,m-1\) and define
\[
S=\{(2j,j),(2j+1,j):0\le j<h\},\qquad
T=\{(2j,j),(2j,j+h):0\le j<h\}.
\]
The first set is row-once with each occupied column used twice; the second is column-once with each occupied row used twice. Both are valid minimum paired-dominating sets and \(|S\cap T|=h\); hence there is a cross-class edge at batch size \(h\). Combining with Step 4, for \(2\le r<h\) the two classes are exactly the two components, and for \(r\ge h\) a cross-class edge joins two individually connected classes. Since \(h\ge2\), this also establishes the claimed behavior at \(r=1\).

All steps are uniform for every stated even \(m\); finite tests below are supplementary, not substitutes for this proof.

## Verification
Run the standard-library files `verify_bruteforce.py` and `verify_evenfiber.py` from the same directory. The former independently enumerates all subsets of the sixteen cells in the four-by-four rook graph through cardinality four, tests domination and existence of induced perfect matchings by recursive pairing, and builds batch-one and batch-two exchange graphs. It finds 80 minima in two classes of 40, no batch-one edges, and a connected batch-two graph with 720 edges, degree eighteen and diameter three. The latter enumerates all functions on four and six row labels, filters by even fibers, and verifies that within-orientation double moves reach every one of 40 and 2,256 functions respectively. It checks explicit threshold-crossing configurations and computes the coefficient formula for \(m=4,6,8\), yielding \(80,4512,500992\) minimum configurations. Assertions in the code fail if any recorded finite check disagrees.

## Relationship to prior work
Paired domination, with the induced-perfect-matching condition, was introduced by Haynes and Slater (1998). Brešar, Henning and Rall (2005), as well as Choudhary, Margulies and Hicks (2011 preprint; 2013 journal), studied paired domination of Cartesian products and proved general product bounds. The latter's five theorem statements and proofs concern inequalities, not this full exact classification or batch-reconfiguration threshold. Reconfiguration of ordinary dominating sets is studied by Suzuki, Mouawad and Nishimura (2014) in an add/remove model; it does not imply a statement about these optimum-constrained paired-dominating sets. The present theorem supplies an explicit classification, counting formula and sharp connectivity threshold for a different, specified batch-exchange model. The definition of the exchange relation matters, and this is not a claim about token sliding, token addition/removal or paths through nonoptimal solutions.

## Limitations
No complete published-literature coverage or priority certification is claimed; the full text of every potentially relevant historical article was not accessible, and equivalent results under alternative terminology might exist. Only square rook graphs of even order and the stated optimum-preserving batch model are treated. For odd orders, minimum pairing forces a different parity situation; no corresponding theorem is asserted here. The provided computations check finite instances only. No independent external scientific validation has been performed.

## References
1. T. W. Haynes and P. J. Slater, "Paired-domination in graphs," *Networks* **32** (1998), 199–206, doi:10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F. Online first 7 December 1998.
2. B. Brešar, M. A. Henning and D. F. Rall, "Paired-domination of Cartesian products of graphs," *Electronic Notes in Discrete Mathematics* **22** (2005), 233–237, doi:10.1016/j.endm.2005.06.059.
3. K. Choudhary, S. Margulies and I. V. Hicks, "A Note on Total and Paired Domination of Cartesian Product Graphs," arXiv:1109.2174v1 (9 September 2011); *Electronic Journal of Combinatorics* **20** (2013), #P25.
4. A. Suzuki, A. E. Mouawad and N. Nishimura, "Reconfiguration of Dominating Sets," arXiv:1401.5714 (2014).
5. C. M. Mynhardt and S. Nasserasr, "Reconfiguration of Colourings and Dominating Sets in Graphs: a Survey," arXiv:2003.05956 (2020).
