# Edge-open packings in generalized Petersen graphs \(GP(n,2)\): an exact nine-periodic law

## Finding

For every integer \(n\ge5\), the edge-open-packing number of the generalized Petersen graph satisfies
\[
\boxed{\rho_e^o(GP(n,2))=\left\lfloor\frac{7n}{9}\right\rfloor.}
\]
The construction and upper-bound argument are exact for the entire infinite family, rather than extrapolations from numerical optimization.

## Assumptions and scope

All graphs are finite, simple, and undirected. Write \(\mathbb Z/n\mathbb Z\) for indices modulo \(n\). The graph \(GP(n,2)\) has vertices \(u_i,v_i\) for \(i\in\mathbb Z/n\mathbb Z\) and the three kinds of edges
\[
O_i=u_i u_{i+1},\qquad S_i=u_i v_i,\qquad I_i=v_i v_{i+2}.
\]
For \(n\ge5\), these comprise \(3n\) distinct edges. An **edge-open packing** is a subset \(F\subseteq E(G)\) such that for distinct \(e,f\in F\) there is no third graph edge \(g\notin\{e,f\}\) having one endpoint in \(e\) and one in \(f\). Equivalently, the subgraph formed by selected edges is a vertex-disjoint union of induced stars (isolated selected edges included). Its maximum cardinality is \(\rho_e^o(G)\). The result concerns this invariant, not vertex open packing, maximum induced matching, or the minimum number of colors in an injective edge coloring.

## Proof

**Step 1: a local conflict model.** Represent a selected edge set by a cyclic word \(a_0\ldots a_{n-1}\), with each symbol a three-bit mask: bit \(1\) selects \(O_i\), bit \(2\) selects \(S_i\), and bit \(4\) selects \(I_i\). Label these three edge types \(0,1,2\), respectively. Direct inspection of third edges joining endpoints shows that for \(n\ge9\) every forbidden pair is captured by the following ordered type pairs: the row \(d\) forbids type \(p\) at column \(i\) simultaneously with type \(q\) at column \(i+d\), with indices interpreted cyclically:

| Offset \(d\) | Forbidden ordered pairs \((p,q)\) |
|---|---|
| \(0\) | \((0,2),(2,0)\) |
| \(1\) | \((0,2),(1,0),(1,1),(2,0)\) |
| \(2\) | \((0,0),(0,1),(1,1),(1,2),(2,0)\) |
| \(3\) | none |
| \(4\) | \((2,1),(2,2)\) |

No larger cyclic offset is possible because any connecting third edge has endpoint-index span at most two in each of its two participating selected edges; a direct check among \(O_i,S_i,I_i\) gives the table. The permissible individual masks are exactly \(\{0,1,2,3,4,6\}\). For \(n\ge9\), applying this table to all cyclic columns is equivalent to the original edge-open-packing condition. Define \(\operatorname{ok}(a,b,d)\) to mean that no table pair in row \(d\) has both its designated bits set in masks \(a,b\).

**Step 2: an exact upper-bound certificate.** Let \(\mathcal S\) consist of the four-symbol words \((a,b,c,d)\) from permissible masks for which \(\operatorname{ok}\) holds between every two of the four positions at their separation. These are exactly \(120\) states. An arc from \((a,b,c,d)\) to \((b,c,d,e)\) exists when the appended mask \(e\) is compatible at offsets \(1,2,3,4\) with the preceding four masks. There are exactly \(291\) such arcs; assign arc weight \(w=\operatorname{popcount}(e)\).

The included `verify_gp.py` independently reconstructs all \(120\) states and \(291\) arcs using only the conflict table. It includes a complete **integer potential** \(h:\mathcal S\to\{0,1,\ldots,17\}\), listed in lexicographic state order, and verifies **every** inequality
\[
h(s)\ \ge\ h(t)+9w-7
\quad\text{for each arc }s\xrightarrow{w}t.
\]
This finite set of exact integer inequalities is the entire upper-bound certificate; no floating-point tolerance is involved. A cyclic admissible word of length \(n\ge9\) gives a closed walk of length \(n\) in this automaton. Summing its inequalities cancels the potentials and gives \(9|F|\le7n\). Thus
\[\rho_e^o(GP(n,2))\le\left\lfloor\frac{7n}{9}\right\rfloor\qquad(n\ge9).\]

**Step 3: exact boundary cases.** For each \(n=5,6,7,8\), the provided verifier constructs the \(3n\)-edge conflict graph directly from the original generalized Petersen adjacency lists, without relying on the local offset table. Its exact maximum independent set is computed by the exhaustive recurrence
\[
\alpha(X)=\max\bigl\{\alpha(X\setminus\{v\}),\ 1+\alpha(X\setminus N[v])\bigr\},\qquad\alpha(\varnothing)=0.
\]
The computed optima are respectively \(3,4,5,6\). The explicit cyclic words below attain these values. They agree with the proposed formula.

**Step 4: constructions at every order.** The following words, included verbatim in the executable certificate, are edge-open packings of the indicated lengths. Symbols are the three-bit masks described in Step 1. The total number of set bits in each word equals \(\lfloor7n/9\rfloor\).

| \(n\) | Cyclic mask word |
|---|---|
| \(5\) | `0 1 3 0 0` |
| \(6\) | `0 2 4 0 2 4` |
| \(7\) | `4 2 0 1 0 4 4` |
| \(8\) | `0 0 1 0 4 4 6 4` |
| \(9\) | `2 4 0 6 4 0 2 0 1` |
| \(10\) | `2 4 0 6 0 0 3 0 0 1` |
| \(11\) | `2 4 0 6 4 0 6 0 0 0 1` |
| \(12\) | `2 4 0 6 4 0 2 0 1 2 0 1` |
| \(13\) | `2 4 0 6 4 0 6 0 0 3 0 0 1` |
| \(14\) | `2 4 0 6 4 0 6 0 0 4 0 2 0 1` |
| \(15\) | `2 4 0 6 4 0 6 0 0 6 0 0 2 0 1` |
| \(16\) | `2 4 0 6 4 0 6 0 0 3 0 0 1 2 0 1` |
| \(17\) | `2 4 0 6 4 0 6 0 0 3 0 0 1 3 0 0 1` |

For \(9\le n\le17\), each word begins with the same four-mask state \((2,4,0,6)\). Cyclically rotate its word so that its first symbol comes after these four positions, namely replace \((a_0,\ldots,a_{n-1})\) by \((a_4,\ldots,a_{n-1},a_0,\ldots,a_3)\). This is the edge-label sequence of an automaton closed walk **based at the common state** \((2,4,0,6)\). Concatenating such based closed walks is again a closed walk and thus an admissible cyclic packing word. The length-nine word adds exactly seven selected edges. Write any \(n\ge9\) uniquely as \(n=(9+r)+9q\) where \(0\le r\le8\) and \(q\ge0\). Concatenate the rotated base word of length \(9+r\) with \(q\) copies of the rotated nine-word. The total number of selected edges is
\[
\left\lfloor\frac{7(9+r)}9\right\rfloor+7q
=\left\lfloor\frac{7n}9\right\rfloor.
\]
This proves the lower bound at every \(n\ge9\), completing the proof together with Steps 2–3. \(\square\)

## Verification

Run `python3 verify_gp.py` with a standard Python 3 installation. It checks the complete integer potential against all \(291\) arcs, compares the local conflict table with directly constructed graphs at eight distinct orders, computes the exact small-order maxima by the independent-set recurrence, and checks every thirteen base words. It additionally tests pumped packings for \(n=18,\ldots,180,271,360,721\). The full captured run is in `verification_output.txt`.

The **general proof** consists of the finite inequality certificate plus the automaton and concatenation arguments; tests on finitely many larger graphs are corroboration only. The exact certificate and the general argument are reproducible and are distinct from sampled tests.

## Relationship to prior work

Chelladurai, Kalimuthu, and Soundararajan (2022) introduce and investigate edge-open packing, including its exact value \(3\) for the Petersen graph \(GP(5,2)\) (their Proposition 2.5). This is included here only as a previously known boundary instance. Brešar and Samadi (2024) develop complexity methods and universal bounds for edge-open packing. Brešar, Dravec, Hedžet, and Samadi (2024) study induced matching versus edge-open packing for trees and graph products. Pandey and Santra (2025) give necessary-and-sufficient conditions for a graph to have bounded edge-open-packing number in terms of tests over induced matchings and other packings; they do not evaluate those conditions for \(GP(n,2)\) or imply the explicit periodic formula without a new family-specific argument. The inspected statements and full texts do not supply the exact \(GP(n,2)\) formula for arbitrary \(n\). A universal cubic upper bound of order \(n\) does not imply the sharper \(\lfloor7n/9\rfloor\) bound or its attainability.

## Limitations

This theorem concerns only \(GP(n,2)\) with \(n\ge5\); it makes no assertion about \(GP(n,k)\) for general \(k\). The main certificate is finite and reproducible, but its interpretation as a bound for every graph order uses the proved local-conflict representation. The work does not classify **all** optimal packings, nor determine the injective edge-chromatic number. Undiscovered equivalent older work under the language of induced star forests or edge-color classes is a residual literature risk.

## References

1. G. Chelladurai, K. Kalimuthu, S. Soundararajan, *Edge open packing sets in graphs*, RAIRO Operations Research **56** (2022), 3765–3776. DOI `10.1051/ro/2022171`. Full text: https://www.numdam.org/item/10.1051/ro/2022171.pdf.
2. B. Brešar and B. Samadi, *Edge open packing: complexity, algorithmic aspects, and bounds*, arXiv:2403.00750 (first public March 1, 2024). Full text: https://arxiv.org/pdf/2403.00750.
3. B. Brešar, T. Dravec, T. Hedžet, and B. Samadi, *Induced matching vs edge open packing: trees and product graphs*, arXiv:2406.04020 (first public June 6, 2024). Full text: https://arxiv.org/pdf/2406.04020.
4. A. Pandey and K. Santra, *Edge open packing: further characterizations*, arXiv:2508.01935 (first public August 3, 2025). Full text: https://arxiv.org/pdf/2508.01935.
