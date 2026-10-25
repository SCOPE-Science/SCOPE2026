# Square-board exceptional weights in two-rainbow independent domination of rook graphs

## Finding

For all integers \(2\le p\le q\), the complete two-rainbow independent domination polynomial of the labeled rectangular rook graph \(R_{p,q}=K_p\square K_q\) is given below. Write \(D_m=\sum_{j=0}^m(-1)^j m!/j!\) for the derangement number (in particular \(D_0=1\) and \(D_1=0\)), and \((a)_{\downarrow b}=a!/(a-b)!\) for the falling factorial, with \((a)_{\downarrow0}=1\). For \(p<q\),

\[
\mathcal R_{p,q}(z)
=(q)_{\downarrow p}
\left(\sum_{j=0}^{p}(-1)^j\binom pj(q-j)_{\downarrow(p-j)}\right)z^{2p}.
\]

For square boards \(p=q=n\ge2\),

\[
\boxed{\mathcal R_{n,n}(z)=n\,n!\,(n-1)D_{n-2}z^{2n-2}
+2n\,n!D_{n-1}z^{2n-1}+n!D_nz^{2n}.}
\]

There are *no other nonzero coefficients*. In particular, every admissible labeling on a nonsquare rectangle has exactly \(2p\) positively labeled cells. Square boards permit up to three consecutive weights. The least weight is \(2\) when \(n=2\), \(5\) when \(n=3\), and \(2n-2\) when \(n\ge4\); on nonsquare rectangles it is \(2p\).

## Assumptions and scope

The board has a labeled row set \([p]\) and labeled column set \([q]\). Distinct cells are adjacent if and only if they share a row or column. A two-rainbow independent dominating function (a \(2\)-RiDF) is a map \(f:[p]\times[q]\to\{0,1,2\}\) satisfying (i) each color class \(f^{-1}(1)\) and \(f^{-1}(2)\) is an independent vertex set and (ii) every cell labeled \(0\) has a *distinct neighboring cell* of color \(1\) and a neighboring cell of color \(2\). Color labels are distinguished. Its weight is the number of nonzero cells, and \(\mathcal R_{p,q}(z)=\sum_f z^{w(f)}\) sums over all such functions.

The formulas count **all** admissible functions, not just minimum-weight functions. The result applies only to the two-color convention just defined; it does not identify this invariant with the older, differently defined independent two-rainbow domination invariant allowing subset-valued labels.

## Proof

**Missing-corner lemma.** Fix a color \(a\in\{1,2\}\). Since its colored cells are pairwise nonadjacent, they form a partial nonattacking-rook placement, equivalently a partial matching between board rows and columns. Suppose this placement uses \(k\) cells, misses row set \(U\) of size \(p-k\), and misses column set \(W\) of size \(q-k\). Any cell in \(U\times W\) has no neighbor of color \(a\). It cannot be assigned \(0\), because every zero must have such a neighbor; nor can it be assigned \(a\), since the color-\(a\) placement misses its row and column. It therefore must carry the *opposite* color. That opposite color also forms a nonattacking-rook placement. Consequently

\[
(p-k)(q-k)=|U\times W|\le1.
\]

If \(p<q\), then \(k<p\) gives \(p-k\ge1\) and \(q-k\ge2\), a contradiction. **Both colors must use exactly one cell in every row**, each in a distinct column. Conversely, any two disjoint row-covering nonattacking-rook placements satisfy both requirements: every zero has a neighboring cell of each color in its own row. To count them, choose the first color in \((q)_{\downarrow p}\) ways. For a fixed first placement, choose a second injective row-to-column map avoiding the first color's column *on the same row*. Inclusion-exclusion on the \(p\) forbidden same-row coincidences gives

\[
\sum_{j=0}^p(-1)^j\binom pj(q-j)_{\downarrow(p-j)}
\]

possibilities, proving the nonsquare formula.

If \(p=q=n\), the missing-corner inequality implies that each color placement contains either \(n\) or \(n-1\) cells. A full placement has no missing row or column. A placement with \(n-1\) cells misses exactly one row and column, whose intersection is called its *missing corner*. The missing-corner lemma now says exactly that its missing corner must be occupied by the opposite color. Conversely, any two disjoint nonattacking-rook placements of these sizes satisfying the missing-corner condition form a valid \(2\)-RiDF: for either color, a zero cell not equal to that color's missing corner lies in an occupied row or an occupied column and hence sees that color; each missing corner was required to have the opposite nonzero label and thus cannot be a zero.

We count the three disjoint square-board cases. (1) If both colors have \(n\) cells, the first is a permutation placement in \(n!\) ways, and the second is a permutation avoiding all \(n\) first-color cells, giving \(n!D_n\) functions of weight \(2n\).

(2) If one color has \(n\) cells and the other has \(n-1\), choose which color is full (two possibilities), the full permutation (\(n!\) possibilities), and the missing row of the smaller placement (\(n\) possibilities). Its missing column is then *forced* by the requirement that its missing corner be occupied by the full color. The smaller placement matches the remaining \(n-1\) rows to remaining \(n-1\) columns without coinciding with the full permutation, giving \(D_{n-1}\) possibilities. This yields \(2n\,n!D_{n-1}\) functions of weight \(2n-1\).

(3) If both colors have \(n-1\) cells, first specify color \(1\)'s missed row and column and its bijection on the remaining rows and columns. There are \(n^2(n-1)!=n\,n!\) choices. The missing corner of color \(2\) must be one of the \(n-1\) cells of color \(1\); choose which. The missing corner of color \(1\) is required to be a color-\(2\) cell. The remaining \(n-2\) color-\(2\) cells therefore constitute a derangement of the other \(n-2\) matched row-column positions of color \(1\), giving \(D_{n-2}\) possibilities. The total is \(n\,n!\,(n-1)D_{n-2}\), with weight \(2n-2\).

These cases exhaust all admissible functions. The least positive monomial gives the minimum weight, using \(D_0=1\), \(D_1=0\), and \(D_m>0\) for \(m\ge2\).

## Verification

The standalone `verify.py` tests the graph definition, not the missing-corner characterization. It directly enumerates all ternary labelings on six boards, checking \(617544\) assignments. It separately enumerates nonattacking-rook pairs on eight larger boards, inspecting \(20260210\) ordered pattern pairs, and verifies every accepted pair against the original independent-domination definition. In every case the full coefficient distribution matches the displayed formula. The exact output appears in `verification_output.txt` and is reproducible using `python3 verify.py` with Python's standard library.

Finite enumerations corroborate the proof but do not themselves establish its infinite range.

## Relationship to prior work

Kraner Šumenjak, Rall and Tepeh introduced \(k\)-rainbow independent domination, proved \(\gamma_{\mathrm{ri}k}(G)=i(G\square K_k)\), and studied basic parameters and elementary families [1]. The present formula therefore also counts maximal independent sets by size in the three-factor Hamming graph \(K_p\square K_q\square K_2\), with the two color layers explicitly distinguished. Zhu [2] gives structural and Nordhaus–Gaddum bounds for the same invariant, not this rook-graph census. Gabrovšek, Peperko and Žerovnik [3] investigate cycle-by-path and cycle-by-cycle products using tropical methods; their results concern a different Cartesian-product family and minimum weights. The older independent \(2\)-rainbow domination [4] uses subset-valued labels and independence of the union of all nonempty labels, and is not equivalent to the labeling counted here.

No identical full enumerator or structurally stronger rook-graph classification was located in the checked primary sources; this is a bounded literature comparison, not a proof of global publication priority.

## Limitations

The statement concerns finite rook graphs with two color classes and both dimensions at least two, and counts labeled functions. It does not claim a formula for more colors, arbitrary graph products, or general Hamming graphs with three factors of unrestricted sizes. General maximal-independent-set enumeration algorithms can compute fixed instances but do not by themselves imply the explicit square-boundary trichotomy. An unindexed equivalent formula or broader theorem may exist; independent mathematical and priority review remain outstanding.

## References

[1] T. Kraner Šumenjak, D. F. Rall, A. Tepeh, *On k-rainbow independent domination in graphs*, arXiv:1709.08966 (first posted 2017-09-26), subsequently *Applied Mathematics and Computation* **333** (2018), 353–361, doi:10.1016/j.amc.2018.03.113.

[2] E. Zhu, *An Improved Nordhaus–Gaddum-Type Theorem for 2-Rainbow Independent Domination Number*, *Mathematics* **9** (2021), 402, doi:10.3390/math9040402.

[3] B. Gabrovšek, A. Peperko, J. Žerovnik, *On the 2-rainbow independent domination numbers of some graphs*, *Central European Journal of Operations Research* **31** (2023), 817–831, doi:10.1007/s10100-023-00840-w.

[4] M. Chellali and N. Jafari Rad, *Independent 2-rainbow domination in graphs*, *Journal of Combinatorial Mathematics and Combinatorial Computing* **94** (2015), 133–148; this is a different invariant.
