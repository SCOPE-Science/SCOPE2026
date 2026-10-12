# Eight-erasure three-dimensional ambiguity in binary \(\operatorname{SPC}(m)\otimes\operatorname{SPC}(n)\) codes

## Finding

For all integers \(m,n\geq2\) with \((m-1)(n-1)\geq3\), there is a complete classification of eight-coordinate erasure patterns in the binary single parity-check product code whose ambiguity space has dimension at least three. They are exactly the complete \(2\)-by-\(4\) rectangles, the complete \(4\)-by-\(2\) rectangles, and the \(3\)-by-\(3\) rectangles with exactly one missing cell. Each ambiguity space has dimension **exactly** three. Their total number is
\[
N_{m,n}=\binom{m}{2}\binom{n}{4}+\binom{m}{4}\binom{n}{2}+9\binom{m}{3}\binom{n}{3}.
\]
For \(m=n=4\), the three shape counts are \(6,6,144\), respectively: \(156\) of the \(12870\) eight-erasure subsets cause eight possible completions. No erasure pattern with fewer than eight coordinates has eight-way ambiguity.

This is also the complete count and support classification of the three-dimensional subcodes attaining the already-known generalized Hamming weight \(d_3(C_{m,n})=8\). In particular, the minimum support size is not claimed to be new.

## Assumptions and scope

Define \(C_{m,n}\subseteq\mathbb F_2^{m\times n}\) as the space of matrices whose row sums and column sums vanish modulo two. For \(E\subseteq[m]\times[n]\), write
\[
C(E)=\{x\in C_{m,n}:\operatorname{supp}(x)\subseteq E\}.
\]
When an erasure pattern occurs on a known codeword, the set of codeword completions is an affine translate of \(C(E)\) and therefore contains exactly \(2^{\dim C(E)}\) elements. Associate to \(E\) the simple bipartite graph \(G_E\), with row vertices and column vertices and one edge per erased coordinate. Isolated vertices are omitted in \(V_E\); let \(c_E\) denote the number of connected components of the graph on these incident vertices. The count uses \(\binom ab=0\) whenever \(b>a\).

## Proof

**Step 1: ambiguity is the binary cycle space.** A word supported within \(E\) satisfies all parity checks precisely when its selected edges have even incidence degree at each vertex. Therefore \(C(E)\) is the binary cycle space of \(G_E\) and
\[
\dim C(E)=|E|-|V_E|+c_E.
\]
One proof of the formula deletes a spanning forest: the \(|E|-(|V_E|-c_E)\) nonforest edges each create an independent fundamental cycle and span all even-degree subgraphs.

**Step 2: minimal edges needed for cycle rank.** A connected simple bipartite component with positive cycle rank has at least four edges. A component with cycle rank at least two has at least six edges: the cases of at most four vertices have at most four edges, and for at least five vertices the relation \(e-v+1\geq2\) forces \(e\geq v+1\geq6\). Similarly, a component with cycle rank at least three has at least eight edges: when \(v\leq5\), bipartite simplicity gives \(e\leq\lfloor v^2/4\rfloor\leq6\), which is incompatible with \(e-v+1\geq3\); for \(v\geq6\) one has \(e\geq v+2\geq8\). These arguments also apply to a component with pendant trees, because their presence cannot decrease the minimum required edge counts.

**Step 3: exact eight-edge classification.** A graph with at most seven edges cannot have total cycle rank three: a single rank-three component needs eight edges, a rank-two and rank-one pair needs at least ten, and three rank-one components need at least twelve. If \(|E|=8\) and \(\dim C(E)\geq3\), a single connected component must contain all eight edges and have rank exactly three. The equality \(3=8-v+1\) forces \(v=6\). If the two bipartition sizes are \(a\) and \(b\), then \(a+b=6\) and \(ab\geq8\), so \((a,b)\) is \((2,4)\), \((3,3)\), or \((4,2)\). In the first and last cases all eight of the possible edges occur, giving \(K_{2,4}\) and \(K_{4,2}\). In the middle case eight of the nine possible edges occur, giving \(K_{3,3}\) minus one edge. Each graph is connected and has eight edges on six incident vertices, so its cycle space has rank three. This proves necessity and sufficiency, including the exact ambiguity dimension.

**Step 4: exact counting and subcode bijection.** The first two graph types arise by choosing the indicated row and column subsets, yielding \(\binom m2\binom n4\) and \(\binom m4\binom n2\) patterns. The third chooses three rows, three columns, and one of nine omitted cells, yielding \(9\binom m3\binom n3\). The three classes are disjoint because their numbers of incident row and column vertices differ. All eight edges of each type lie on cycles (each edge is part of some even-degree subgraph), so \(\operatorname{supp}(C(E))=E\). If a three-dimensional subcode \(D\) has support of cardinality eight, then \(D\subseteq C(E)\), where \(E=\operatorname{supp}(D)\), and both spaces have dimension three; thus \(D=C(E)\). Conversely each classified \(E\) yields such a subcode. Hence the same formula counts the minimum-support three-spaces exactly once each.

## Verification

The self-contained script `artifacts/verify.py` uses only Python's standard library and checks all seven- and eight-coordinate patterns for five test dimensions. Independently of the graph search, it generates all reduced-row-echelon three-dimensional coefficient spaces, maps them to the parity-check product code by its standard generator, and checks that the eight-support minimizers are in bijection with the graph patterns. For \(m=n=4\), the checker visits \(788035\) three-spaces and confirms \(156\) distinct minimizers. The script prints `VERIFY_OK` if all checks pass. These finite checks corroborate but do not replace the proof for arbitrary \(m,n\).

## Relationship to prior work

Alves and Cardell's 2026 Theorem 7 provides the generalized Hamming weights of \(C_{m,n}\), implying \(d_3=8\), and their Example 2 explicitly lists the hierarchy for the \(4\)-by-\(4\) code. Those results supply the known minimum **size**, but neither the count of minimum three-dimensional subcodes nor the exact classes of eight-erasure patterns with eight-way completion ambiguity. Earlier Cardell–Climent papers analyze failures and count uncorrectable erasure patterns (including cardinality eight), meaning patterns with at least one cycle. A count of all failures does not by itself determine how many have cycle rank three rather than one or two. The 2019 paper develops an exact Kostka-number count for strict uncorrectable graph patterns with specified row and column degrees (Theorem 3); this powerful general enumeration is acknowledged, but it is not a rank-stratified count or a classification of minimum-support three-dimensional subcodes. This finding isolates the highest possible ambiguity rank at eight erasures and evaluates that stratum for rectangular products.

## Limitations

The statement concerns the binary code, exact eight erased coordinates and its ambiguity space under maximum-likelihood erasure completion, not the performance of a particular iterative decoder. It does not improve the known third generalized weight, classify all uncorrectable patterns, or determine probabilities for burst-correlated erasure processes. The 2019 complete open-access preprint was examined through its Theorem 3, the worked examples, the tabulated six-erasure patterns, and the conclusion; it does not state the eight-erasure rank-three classification. Its general margin-enumeration machinery could recover pieces of the count after an additional cycle-rank and connectivity argument. The 2016 full paper could contain an implicit eight-edge graph classification; that precise overlap remains a literature risk. Independent external audit has not been performed.

## References

1. M. M. Ribeiro Alves and S. D. Cardell, *Weight Distributions of Single Parity-Check Product Codes via Character Sums*, arXiv:2608.26457v1 (first public 2026-08-26), Section 3.2, Theorem 7 and Example 2. https://arxiv.org/pdf/2608.26457v1
2. S. D. Cardell and J.-J. Climent, *An approach to the performance of SPC product codes on the erasure channel*, Advances in Mathematics of Communications **10** (2016), 11–28, doi:10.3934/amc.2016.10.11. https://doi.org/10.3934/amc.2016.10.11
3. S. D. Cardell, J.-J. Climent and A. López Martín, *SPC product codes, graphs with cycles and Kostka numbers*, RACSAM **113** (2019), 3751–3765, doi:10.1007/s13398-019-00698-1. https://doi.org/10.1007/s13398-019-00698-1
