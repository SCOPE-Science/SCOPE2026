# Wild-edge connectivity of coordinate-coloured cubes through five dimensions

## Finding

Give the binary hypercube \(Q_d\) its standard proper edge-colouring by coordinate: an edge has colour \(i\in\{0,\ldots,d-1\}\) when its endpoints differ in coordinate \(i\). For each colour \(i\), upgrading a set \(W\) of edges means that every edge in \(W\) can also be used as colour \(i\). A set \(W\) is *colour-connecting* when its union with every monochromatic edge class induces a connected spanning graph. Let \(w_d\) be the minimum size of such a set. Then

\[
\boxed{(w_2,w_3,w_4)=(2,5,10),\qquad 19\le w_5\le20.}
\]

In particular, the four-dimensional cube admits a ten-edge set simultaneously connecting all four coordinate colour classes, and no nine-edge set can do so. An explicit twenty-edge set gives a one-edge interval for the first five-dimensional case. These statements concern only the specified coordinate colouring, not arbitrary minimum proper edge-colourings of the cube.

## Assumptions and scope

For \(d\in\{2,3,4,5\}\), identify \(V(Q_d)\) with \(\{0,1,\ldots,2^d-1\}\), interpreted as \(d\)-bit vectors. Its edges are the unordered pairs \(\{u,u\oplus2^i\}\) for \(0\le i<d\), where \(\oplus\) denotes bitwise exclusive OR; the corresponding colour is \(i\). There are \(2^{d-1}\) edges in each colour class, forming a perfect matching. No other graph products or edge colourings are asserted to satisfy the table.

## Proof

**Lower bound.** Fix any colour-connecting set \(W\) of \(w\) edges, and let \(w_i\) be the number of its edges originally coloured \(i\). Contract all \(2^{d-1}\) monochromatic \(i\)-edges, which form a perfect matching. The resulting graph has \(2^{d-1}\) contracted vertices; edges of \(W\) originally coloured \(i\) become loops and do not aid connectivity. Thus the other \(w-w_i\) edges must connect these vertices, requiring \(w-w_i\ge 2^{d-1}-1\). Summing over all \(d\) colours yields

\[
(d-1)w\ge d(2^{d-1}-1),\qquad
w_d\ge\left\lceil\frac{d(2^{d-1}-1)}{d-1}\right\rceil.
\]

The lower bounds for dimensions \(2,3,4,5\) are respectively \(2,5,10,19\). This bound is a specialization of the known general ceiling lower bound for wild numbers; it is **not** claimed as a new independent bound.

**Upper bounds.** `certificate.json` lists actual unordered edge pairs for dimensions two through five, with cardinalities respectively \(2,5,10,20\). The vertices are labelled by the bit-mask convention above. For clarity, the ten-edge certificate in dimension four is

\[
\begin{aligned}
W_4=\{&\{4,5\},\{8,9\},\{5,7\},\{9,11\},\{12,14\},\\
&\{1,5\},\{2,6\},\{9,13\},\{5,13\},\{6,14\}\}.
\end{aligned}
\]

For every coordinate \(i\), contract all colour-\(i\) matching edges. In each dimension the remaining edges from the listed \(W_d\) contain a spanning tree on the \(2^{d-1}\) quotient vertices. For dimension four, a spanning-tree selection for the four respective colours is, in the above displayed edge order and with one-based indices,

\[
\begin{array}{c|l}
 i &\text{selected certificate-edge indices}\\\hline
0&3,4,5,6,7,8,9\\
1&1,2,6,7,8,9,10\\
2&1,2,3,4,5,9,10\\
3&1,2,3,4,5,6,7
\end{array}
\]

Each selected set has seven edges and connects all eight contracted vertices. This is a directly checkable finite certificate; `verify.py` reconstructs and checks these trees without numerical optimization or external packages. The same program checks all other dimensions and requires exactly \(2^{d-1}-1\) successful merging edges after each contraction. Thus \(w_d\le2,5,10,20\) for the stated dimensions. Combining with the lower bounds proves the displayed claim.

## Verification

Run `python3 verify.py` in the same directory as `certificate.json`. It reconstructs the cube from the bit-mask definition, rejects duplicated or invalid certificate edges, contracts each coordinate matching using a disjoint-set structure, and checks that the remaining certificate edges join every quotient component. It checks the certificate lengths, the explicit lower-bound arithmetic, and the size of every computed spanning tree. The recorded output is in `verification_output.txt`, ending in `VERIFY_OK`. The proof of the lower bound is algebraic and does not depend on the program.

## Relationship to prior work

Anders, Foster-Greenwood, Garcia and Krawzik introduced the wild number and proved a ceiling lower bound in Proposition 5.4 of their 2025 preprint. Dawkins, Nappo, Tong and Zimbizi revisited this bound and investigated minimum proper colourings of complete and complete bipartite graphs, obtaining lower bounds on Cartesian products in Section 5 of their October 2026 preprint. Their statements supply the general counting principle, not the explicit colour-connecting edge sets and exact four-cube value here. The objects, colouring, and tested claims were compared against both primary texts and targeted mathematical-record searches, with no equivalent exact four-cube result identified.

## Limitations

The five-cube is bounded between nineteen and twenty; this result **does not** decide which value is correct. No claim is made for dimensions at least six, for different edge-colourings of hypercubes, or for minimum wild sets beyond the exhibited witnesses. Bibliographic priority and mathematical correctness have not been independently audited. The existence checks are finite and exact; they are not an exhaustive enumeration of all candidate wild sets.

## References

- K. Anders, B. Foster-Greenwood, R. Garcia, N. Krawzik, *The wild number of an edge-colored graph*, arXiv:2508.06711v1 (first public 8 August 2025), especially Proposition 5.4. https://arxiv.org/abs/2508.06711
- A. Dawkins, A. Nappo, J. Tong, C. Zimbizi, *Wild number for spanning trees in complete and complete bipartite graphs*, arXiv:2610.22142v1 (first public 15 October 2026), especially Section 5. https://arxiv.org/abs/2610.22142
