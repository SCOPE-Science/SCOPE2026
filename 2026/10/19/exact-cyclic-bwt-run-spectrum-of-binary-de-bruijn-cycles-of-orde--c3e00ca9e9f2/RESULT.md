# Exact cyclic BWT run spectrum of binary de Bruijn cycles of order five

## Finding

Let \(\mathcal D_5\) be the set of binary de Bruijn cycles of order five, with two cycles identified exactly when one is a cyclic rotation of the other. Every cycle contains each binary length-five factor exactly once, and hence has length \(32\). For a binary cycle \(w\), let \(\operatorname{BWT}(w)\) be the last column obtained by lexicographically sorting its 32 cyclic rotations, without any terminal symbol. Let \(r(v)\) count maximal equal-symbol runs in a **linear** word \(v\), without merging its first and last runs.

The exact histogram \(H_j=|\{w\in\mathcal D_5:r(\operatorname{BWT}(w))=j\}|\) is

| \(j\) | \(H_j\) |
| ---: | ---: |
| \(20\) | \(38\) |
| \(22\) | \(426\) |
| \(24\) | \(840\) |
| \(26\) | \(608\) |
| \(28\) | \(130\) |
| \(30\) | \(6\) |

Every other \(H_j\) is zero. In particular, the minimum and maximum are exactly \(20\) and \(30\), respectively, and the complete histogram sums to \(2048\) distinct cycles. A uniformly selected cycle therefore has exact run-count mean \(195/8\) and variance \(211/64\). The BWT run-spectrum polynomial is \(38z^{20}+426z^{22}+840z^{24}+608z^{26}+130z^{28}+6z^{30}\).

Two rotation-normalized witnesses, each beginning with the unique `00000` factor, are `00000100011100101111101010011011` for the minimum \(20\), and `00000100011011001010111010011111` for the maximum \(30\).

## Assumptions and scope

The alphabet is the ordered binary alphabet \(0<1\). The BWT is the classical sentinel-free transform on the **full list** of circular rotations of one primitive word. De Bruijn cycles are taken modulo rotation only: neither bit complementation nor reversal is a quotient operation. All counts refer to order five, not arbitrary orders. The run number counts linear, not circular, runs of the BWT output.

## Proof

This is an exact finite classification with a complete, standalone, exhaustively replayable enumeration proof.

**First exhaustive derivation (Eulerian circuits).** Form the directed binary de Bruijn graph whose vertices are four-bit strings. Each five-bit string \(v b\), with four-bit \(v\) and bit \(b\), is one directed edge from \(v\) to the four-bit suffix of \(v b\). There are exactly \(16\) vertices and \(32\) individually labeled edges. An order-five de Bruijn cycle is equivalent to a closed Eulerian circuit using all \(32\) edges once. Since every cycle contains `00000` exactly once, each cycle has exactly one circuit whose first edge is `00000`. Thus fixing the first vertex as `0000` and the first edge as `00000` removes all rotational duplication, without removing any cycle.

Function `necklace_circuits` in the attached `verify.py` recursively extends a partial circuit by each unused outgoing edge. An edge is represented by the integer \(2v+b\), and its successor vertex is \((2v+b)\bmod16\). The base case accepts only a complete \(32\)-edge traversal ending at vertex `0000`. Every accepted walk is an Eulerian circuit, hence generates a valid cycle; conversely every order-five binary de Bruijn cycle has the unique normalized walk described above, and every walk is visited by this recursion. The implementation independently verifies that each accepted binary word has exactly \(32\) distinct circular five-factors and no duplicate representative. It lexicographically sorts every accepted word's full rotations and counts equal-symbol runs in the last column. This exact traversal returns the six counts in the Finding section, with \(2048\) distinct words and \(2048\) distinct BWT images.

**Independent exhaustive derivation (last-column permutations).** The standard de Bruijn BWT characterization says that the BWT of each binary order-five de Bruijn cycle is a concatenation of \(16\) permutations of \(\{0,1\}\), each equal to `01` or `10`. The transform's last-to-first map is \(\operatorname{LF}(i)=\operatorname{rank}_{L_i}(L[0:i])+16L_i\), for indices \(0\le i<32\), where \(L_i\) is bit \(i\) of the proposed last column and the rank counts earlier occurrences. Such a proposed column represents one primitive length-\(32\) circular word precisely when the LF permutation is one \(32\)-cycle. The de Bruijn block characterization then ensures that this primitive word is an order-five de Bruijn cycle. These standard BWT facts are reviewed by Higgins [1] and Fici–Gabory [3].

The second independent generator `lf_census` therefore examines all \(2^{16}=65536\) possible ordered `01`/`10` block concatenations. It constructs each LF permutation explicitly and retains exactly those containing one \(32\)-cycle. It independently counts the run histogram. It obtains exactly \(2048\) accepted last columns, agrees cell-for-cell with the first enumeration, **and compares the entire sets of \(2048\) BWT images for equality**. This also verifies that the Eulerian walk enumeration did not accidentally miss a BWT image or count a rotation twice.

Both traversals terminate after explicitly bounded finite state spaces, with no timeouts, heuristic pruning, probabilistic sampling, or assumed extrapolation. The complete algorithms and expected exact histogram are included verbatim in `verify.py`; all arithmetic is exact. This is a finite, computer-assisted proof for the stated order-five domain, not an infinite-order theorem.

The permutation-pair structure also gives a simple interpretation: writing the first bit of each `01`/`10` block as \(f_i\), one has \(r(L)=32-|\{i:0\le i<15,\ f_i\ne f_{i+1}\}|\). The complete accepted-transition histogram is thus also certified by the same run-count enumeration.

## Verification

Run `python3 verify.py` with standard Python 3 and no third-party packages. The program independently checks all \(2048\) Eulerian circuits, all \(65536\) candidate block columns, all single-cycle LF permutations, every output's de Bruijn property, exact agreement of the image sets, the six histogram cells, and the extremal values. Its expected final output is:

`VERIFY_OK order5 necklaces=2048 orientations=65536 independent_methods=2 bwt_sets_identical=2048 histogram=20:38,22:426,24:840,26:608,28:130,30:6`

The two explicit extremal witnesses can additionally be checked by directly sorting their \(32\) circular rotations.

## Relationship to prior work

The BWT last-column pair structure and its connection to de Bruijn circuits are **prior results**, particularly Higgins [1]. The new claim is not this characterization, nor the classical total of \(2048\) cycles; it is the **complete run-count histogram and the exact extrema at order five**. Mantaci et al. [2, Theorem 5.2] give general BWT-run inequalities for binary de Bruijn words, which at order five imply the coarser bounds \(18\le r\le30\); they do not determine the complete order-five histogram or establish the sharper lower bound \(20\). Fici–Gabory [3] give further graph-theoretic BWT characterizations and enumeration formulas, but no equivalent run-refined order-five census in the inspected text. Lipták–Parmigiani [4] develop BWT-based random construction; the inspected author presentation concerns generation and highlights BWT-run behavior, but does not give this exact histogram. Ruskey–Sawada–Williams [5] give a classical source on de Bruijn constructions, not this BWT statistic.

## Limitations

This establishes the complete **order-five** histogram only. It does not characterize the run-count distribution at order six or above, prove a uniform all-order formula, or quantify compressed bit size including the BWT indexing overhead. The independent LF enumeration uses known BWT permutation characterization; the novel content is its exact application and complete distribution at the specified natural order. Earlier unindexed or differently presented finite enumerations may exist. A closely related 2024 journal/conference chapter was not inspected in full; its author's accessible presentation was examined instead.

## References

1. P. M. Higgins, “Burrows–Wheeler transformations and de Bruijn words,” *Theoretical Computer Science* 457 (2012), 128–136, DOI: 10.1016/j.tcs.2012.07.019. Author version: https://arxiv.org/pdf/1901.08392 (uploaded subsequently).
2. S. Mantaci, A. Restivo, G. Rosone, M. Sciortino, and L. Versari, “Measuring the clustering effect of BWT via RLE,” *Theoretical Computer Science* 698 (2017), 79–87, DOI: 10.1016/j.tcs.2017.07.015. Author postprint: https://pages.di.unipi.it/rosone/Papers/MRRSV_TCS2017.pdf.
3. G. Fici and J. Gabory, “Generalized De Bruijn Words, Invertible Necklaces, and the Burrows–Wheeler Transform,” *MFCS 2025*, DOI: 10.4230/LIPIcs.MFCS.2025.48. Full text: https://drops.dagstuhl.de/storage/00lipics/lipics-vol345-mfcs2025/html/LIPIcs.MFCS.2025.48/LIPIcs.MFCS.2025.48.html.
4. Z. Lipták and L. Parmigiani, “A BWT-Based Algorithm for Random de Bruijn Sequence Construction,” *LATIN 2024*, pp. 130–145, DOI: 10.1007/978-3-031-55598-5_9. Author presentation: https://profs.scienze.univr.it/~liptak/files/SeqBIM2024.pdf.
5. F. Ruskey, J. Sawada, and A. Williams, “De Bruijn Sequences for Fixed-Weight Binary Strings,” *SIAM Journal on Discrete Mathematics* 26(2) (2012), 605–617, DOI: 10.1137/100808782 (published online 2012-05-08).
