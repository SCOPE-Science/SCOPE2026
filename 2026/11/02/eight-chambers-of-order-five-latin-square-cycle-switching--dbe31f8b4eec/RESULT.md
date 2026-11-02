# Eight chambers of order-five Latin-square cycle switching

## Finding
Let \(\mathcal L_5\) be the set of fully labelled order-five Latin squares on rows, columns and symbols \(\{0,1,2,3,4\}\). A *single-cycle switch* takes two distinct rows and exchanges their entries in exactly the columns of one minimal nonempty row cycle, or applies the transposed operation to two columns. In order five, these cycles have length \(2\), \(3\), or \(5\). Write \(\mathcal R_T\) for the undirected graph of all \(\mathcal L_5\) under switches of lengths in \(T\).

**Theorem (complete proper-Latin cycle-switch census).** Exactly \(161{,}280\) labelled squares exist. The graph \(\mathcal R_{\{2,3\}}\) has exactly \(17{,}280\) isolated vertices and two connected components of \(72{,}000\) vertices each. When length-five single cycles are also allowed, \(\mathcal R_{\{2,3,5\}}\) has exactly eight components: six components of \(2{,}880\) vertices each and two components of \(72{,}000\) vertices each. No move in these graphs changes between the two ordinary isotopy classes of order-five Latin squares.

The three single-cycle lengths contribute exactly \(288{,}000\), \(576{,}000\), and \(1{,}036{,}800\) distinct undirected edges, respectively. Among the labelled squares, \(17{,}280\) have no intercalate and \(144{,}000\) have exactly four; these are the cyclic-table and noncyclic isotopy classes. In the full switch graph, the cyclic class forms the six small components and the noncyclic class forms the two large components.

The intercalate-only baseline (\(17{,}280\) isolates and eight connected \(18{,}000\)-vertex components) is prior knowledge and is **not** an originality claim here. The contribution concerns the connectivity changes caused by adding length-three and length-five single-cycle moves.

## Assumptions and scope
A Latin square \(L=(L_{r,c})_{0\le r,c<5}\) uses each of the five symbols exactly once in each row and column. The labels are fixed; no relabelling is identified with equality. For two rows \(a<b\), let \(\sigma\) be the permutation on the column indices that maps each column \(c\) to the position in row \(a\) occupied by symbol \(L_{b,c}\). Since the rows have different symbols in every column, \(\sigma\) has no fixed points; its cycle type is either \((5)\) or \((2,3)\). A row-cycle switch exchanges the two entries in each column in one cycle of \(\sigma\). Column-cycle switches are defined by transposition of the square. A length-five move is legal only for a full five-cycle; swapping two entire rows whose relative permutation decomposes as \((2,3)\) is **not** counted as one single-cycle switch. No improper arrays or intermediate states outside \(\mathcal L_5\) are permitted.

## Proof
**Exhaustive finite domain.** Normalize the first row to \((0,1,2,3,4)\). For each of the remaining four rows, try every permutation of five symbols and reject immediately when a symbol repeats in an earlier row of a column. The complete backtracking has exactly \(1{,}344\) terminal squares. Applying each of the \(120\) symbol permutations produces each fully labelled Latin square once and yields \(1{,}344\cdot120=161{,}280\) distinct squares. Both supplied programs independently implement and verify this count, including uniqueness in a key-indexed table.

**All legal moves.** For each square and each of its ten row pairs and ten column pairs, the first verifier constructs the relative derangement and visits *every* disjoint cycle. There are no other legal single-cycle swaps by definition. After swapping the corresponding entries, it locates the resulting square in the complete table and records each unordered pair only once. The second verifier instead examines all \(31\) nonempty subsets of the five positions between every pair of parallel rows or columns, directly tests the Latin condition, and retains precisely the inclusion-minimal Latin-preserving swaps. It separately rejects a full-line swap whenever a proper two-position swap exists, preventing a decomposable \((2,3)\) change from masquerading as a length-five cycle. No one- or four-position minimal swaps exist. Both implementations sort and deduplicate undirected edges independently.

**Components and class separation.** For each permitted length set, both implementations apply disjoint-set union to the complete labelled vertex set, joining the endpoints of every listed legal edge. The exhaustive component histograms are

| Allowed cycle lengths | Complete component-size multiset |
| --- | --- |
| \(\{2\}\) | \(17{,}280\) singletons; eight of size \(18{,}000\) (prior baseline) |
| \(\{2,3\}\) | \(17{,}280\) singletons; two of size \(72{,}000\) |
| \(\{2,3,5\}\) | six of size \(2{,}880\); two of size \(72{,}000\) |

To identify the ordinary isotopy classes, count intercalates in each of the \(161{,}280\) squares. Exactly \(17{,}280\) have zero and the other \(144{,}000\) have four. The classical two-class order-five Latin-square classification identifies the first group with isotopes of the addition table of \(\mathbb Z/5\mathbb Z\). A direct count for every connected component confirms that the six smaller full-switch components comprise exactly the zero-intercalate class; the two larger components comprise exactly the four-intercalate class. Alternatively, this last assignment follows from the fact that a single-cycle switch cannot move between those two isotopy classes, together with the verified component sizes and class totals.

The finite enumeration covers every square and every possible move, so the union-find component sizes are an exact exhaustive certificate rather than a statistical estimate.

## Verification
The attached `verify.cpp` and `verify_alt.cpp` are independent C++17 source files. Compile and run each from the directory containing the source:

```sh
g++ -O3 -std=c++17 verify.cpp -o verify
./verify
g++ -O3 -std=c++17 verify_alt.cpp -o verify_alt
./verify_alt
```

`verify.cpp` tests all candidate subsets for each pair of rows or columns; `verify_alt.cpp` constructs derangement cycles and also counts the four traditional row/column/symbol parities. Each checks the complete domain and edges before reporting component histograms. Both implementations obtain \((288{,}000,576{,}000,1{,}036{,}800)\) unique edges by cycle length, \(17{,}280\) zero-intercalate and \(144{,}000\) four-intercalate squares, and the claimed component decompositions. The assertions raise an error if the core counts disagree.

## Relationship to prior work
Wanless's 2004 *Cycle Switches in Latin Squares* studies graphs on **isotopy or main classes**, including order five, and records the disconnection of the two order-five class vertices. That class-level statement does not specify the number or sizes of connected components on the \(161{,}280\) distinct **labelled squares**. The existing labelled *intercalate-only* census gives eight \(18{,}000\)-vertex components and the \(17{,}280\) cyclic-class isolates, but has no legal three- or five-cycle edges and cannot imply how those components merge or how isolated squares become mobile. Aryapoor and Mahmoodian prove connectivity for a larger reconfiguration space allowing *improper* Latin squares; this is a different move model and does not imply connectedness for proper-only cycles. Cavenagh and Wanless study parity changes under odd row cycles and asymptotic parity counts; their arguments do not give this labelled small-order component census. The exact multiset stated above was not identified as a previously published result in the inspected material; an equivalent classification elsewhere is not ruled out.

## Limitations
This theorem concerns only fully labelled order-five Latin squares with single-cycle exchanges and exact move definitions. It does not establish a classification for higher orders, flip-graph diameters, mixing times, or connectivity of every possible Latin-bitrade chain. A relevant 2004 class-level paper could only be inspected through its public abstract and indexed excerpts, not its complete text; its inaccessible sections remain a literature-priority risk. The computations have been checked in two independent implementations, but no independent scholarly audit has been performed.

## References
1. I. M. Wanless, *Cycle Switches in Latin Squares*, Graphs and Combinatorics 20 (2004), 545–570, doi:10.1007/s00373-004-0567-7.
2. M. Aryapoor and E. S. Mahmoodian, *On Uniformly Generating Latin Squares*, arXiv:1005.0121v1, publicly posted 2010-05-02; full text inspected in the subsequent v2 rendering.
3. N. J. Cavenagh and I. M. Wanless, *There Are Asymptotically the Same Number of Latin Squares of Each Parity*, arXiv:1610.06262v1, publicly posted 2016-10-20.
4. B. D. McKay's small Latin-square enumeration catalogue, `https://users.cecs.anu.edu.au/~bdm/data/latin.html`, recording 56 reduced order-five Latin squares.
