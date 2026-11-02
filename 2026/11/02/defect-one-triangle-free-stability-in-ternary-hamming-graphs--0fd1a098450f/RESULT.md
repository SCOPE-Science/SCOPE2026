# Defect-one triangle-free stability in ternary Hamming graphs

## Finding

Let \(H_n=K_3^{\square n}\), with vertex set \(\mathbb F_3^n\) and edges joining words that differ in exactly one coordinate. For each integer \(n\ge 2\), let \(\mathcal T_n\) comprise the **labelled** subsets \(A\subseteq\mathbb F_3^n\) of size \(2\cdot3^{n-1}-1\) that induce no triangle in \(H_n\). Then

\[
|\mathcal T_n|=\begin{cases}
45,&n=2,\\
270,&n=3,\\
6^n,&n\ge4.
\end{cases}
\]

For \(n\ge4\), every \(A\in\mathcal T_n\) extends to a **unique** maximum triangle-free vertex set by adjoining exactly one vertex. The maximum sets are exactly the complements of hyperplanes

\[
B_{a,c}=\{x\in\mathbb F_3^n:\sum_{i=1}^n a_i x_i=c\},\qquad a_i\in\mathbb F_3^\times,\ c\in\mathbb F_3.
\]

There are \(3\cdot2^{n-1}\) distinct such hyperplanes. For \(n=2\), exactly \(9\) members of \(\mathcal T_n\) have no maximum extension; for \(n=3\), exactly \(54\) have no maximum extension. The remaining \(6^n\) sets in these two small dimensions each have a unique extension.

## Assumptions and scope

All coordinates, colors, vertices and subsets are labelled. A *coordinate line* is obtained by fixing all but one coordinate of a word in \(\mathbb F_3^n\); it has three vertices. A *coordinate \(k\)-face* is obtained by fixing all but \(k\) coordinates. In this graph, every triangle lies on one coordinate line. Let \(B=\mathbb F_3^n\setminus A\). Then \(A\) is triangle-free precisely when \(B\) meets every coordinate line. For \(A\in\mathcal T_n\), the complement has \(|B|=3^{n-1}+1\).

The result counts all near-maximum sets, not merely those obtained by deleting one point from a maximum set. Neither a classification of general alphabet sizes nor a statement about Hamming distance greater than one is claimed.

## Proof

**1. Exceptional lines and their common anchor.** Fix a coordinate direction \(i\). Its \(3^{n-1}\) parallel lines partition \(\mathbb F_3^n\), each meets \(B\), and their intersection counts add to \(3^{n-1}+1\). Consequently exactly one line, denoted \(L_i\), meets \(B\) in two vertices; all other lines in direction \(i\) meet \(B\) in exactly one vertex. No coordinate line has three points of \(B\).

Fix distinct directions \(i,j\). The \(3^{n-2}\) coordinate two-faces in these directions partition the cube. Every such \(3\times3\) face contains at least three vertices of \(B\), since it must meet each of its three coordinate rows. Their total is \(3^{n-1}+1\), so exactly one face has four vertices of \(B\) and all others have three. The face containing \(L_i\) has at least four points: two on \(L_i\) and one on each of the other two parallel lines within the face. Hence it is the unique four-point face and also contains \(L_j\). Thus \(L_i\) and \(L_j\) lie in a common coordinate two-face for every distinct pair \(i,j\).

When \(n=2\) the two exceptional lines plainly intersect at a single vertex \(v\). When \(n\ge3\), for each coordinate \(k\), the fixed \(k\)-th entries of all \(L_i\) with \(i\ne k\) coincide: given two such directions \(i,j\), the common \((i,j)\)-face has fixed \(k\)-th coordinate. Call this entry \(v_k\). It follows that \(L_i\) is exactly the \(i\)-coordinate line through the unique word \(v=(v_1,\ldots,v_n)\). We call \(v\) the *anchor*.

**2. Completion.** If \(v\in B\), then \(B\setminus\{v\}\) meets every coordinate line exactly once: the only doubled lines are the \(n\) lines through \(v\). Thus \(A\cup\{v\}\) is triangle-free of maximum size \(2\cdot3^{n-1}\). Conversely, if \(B\setminus\{w\}\) meets all coordinate lines, \(w\) must lie on all doubled lines, hence \(w=v\). Any completion is therefore unique. We next show that \(v\notin B\) is possible only for \(n=2,3\).

**3. The local hole pattern.** Assume \(v\notin B\). Because each \(L_i\) contains two points of \(B\), both noncentral vertices on \(L_i\) belong to \(B\). Consequently \(B\) contains all \(2n\) vertices of Hamming distance one from \(v\). A two-coordinate face through \(v\) has exactly four points of \(B\), already supplied by those four distance-one vertices. Thus no vertex at distance two from \(v\) lies in \(B\).

Take a coordinate three-face through \(v\). It contains exactly \(3^2+1=10\) vertices of \(B\) by counting lines in any of its coordinate directions. The center contributes none; its six weight-one points contribute six; the weight-two points contribute none. Thus precisely four of its eight weight-three corners belong to \(B\). For every choice of signs at two of the three nonzero coordinates, the line varying the third coordinate has exactly one point of \(B\): its weight-two point is absent and it is not a doubled line through \(v\). Hence the four allowed sign triples are exactly one of the two parity classes

\[
\sigma_i\sigma_j\sigma_k=\varepsilon_{ijk},\qquad \varepsilon_{ijk}\in\{+1,-1\},
\]

where \(\mathbb F_3^\times\) is identified with \(\{+1,-1\}\). To see the parity assertion, choose the sign of the third entry when the first two signs are both positive. The requirement of one choice per line in all three directions then forces the other three sign triples, leaving only the two parity possibilities.

**4. The four-coordinate obstruction.** Suppose \(n\ge4\), and select any four coordinate positions, fixing every other coordinate to the anchor. This four-face has \(3^3+1=28\) points of \(B\). Its weight-zero layer contains no point, its weight-one layer all eight points, its weight-two layer none, and its four different three-coordinate subfaces contain four weight-three points each. Thus it contains exactly \(16\) weight-three points and would require **four** weight-four points.

Write \(\varepsilon_j\) for the parity sign on the weight-three subface with coordinate \(j\) at the anchor, and let \(\sigma=(\sigma_1,\ldots,\sigma_4)\in\{\pm1\}^4\) be a possible weight-four point of \(B\). For each \(j\), the coordinate line through this point and the corresponding weight-three neighbor is not doubled. The neighbor must therefore be outside \(B\), requiring

\[
\prod_{\ell\ne j}\sigma_\ell=-\varepsilon_j\qquad(j=1,2,3,4).
\]

Put \(S=\prod_{\ell=1}^4\sigma_\ell\). The four equations give \(\sigma_j=-S\varepsilon_j\). Multiplying these equations yields \(S=\prod_{j=1}^4\varepsilon_j\), so the entire sign vector \(\sigma\) is uniquely determined. There is **at most one** permitted weight-four point, contradicting the four required. Therefore the anchor belongs to \(B\) for every \(n\ge4\).

**5. Maximum sets are affine.** Suppose \(B_0\) meets every coordinate line exactly once. Projection onto the first \(n-1\) coordinates is a bijection, so \(B_0\) is the graph of a function \(f:\mathbb F_3^{n-1}\to\mathbb F_3\). For each input coordinate, the corresponding unary section of \(f\) is a permutation of \(\mathbb F_3\). Every permutation of \(\mathbb F_3\) is affine. When two input coordinates vary, their \(3\times3\) section is a Latin square. Every order-three Latin square is affine: its first row is an affine permutation; to avoid all first-row entries columnwise, its second row is one of the two constant nonzero cyclic shifts, and its third row is forced to be the opposite shift. Thus the increment in a given input coordinate is independent of that coordinate and of any other coordinate, and hence is a fixed nonzero element of \(\mathbb F_3\). Therefore \(f(x)=c+\sum_i b_i x_i\) with all \(b_i\ne0\). In the one-input case this follows from the unary permutation statement. Equivalently, the maximum complements are the displayed affine hyperplanes with all coefficients nonzero. A scalar normalization of one coefficient gives exactly \(3\cdot2^{n-1}\) distinct hyperplanes.

**6. Enumeration and small exceptions.** Every maximum complement \(B_0\) has \(3^n-3^{n-1}=2\cdot3^{n-1}\) possible extra points \(v\notin B_0\). The set \(B=B_0\cup\{v\}\) hits every coordinate line, has size \(3^{n-1}+1\), and has unique completion \(B_0\) by Step 2. Hence the number of completable near-maximum triangle-free vertex sets, in any dimension \(n\ge2\), is

\[
(3\cdot2^{n-1})(2\cdot3^{n-1})=6^n.
\]

For \(n=2\), an uncompletable set \(B\) with anchor \(v\notin B\) consists exactly of the four distance-one vertices; there is one such set per \(v\), hence nine. For \(n=3\), the local-hole analysis is global: \(B\) contains the six distance-one vertices and exactly one of the two parity classes on the eight distance-three vertices, and no others. These two choices give valid line-hitting sets (check the line families fixing zero, one or two nonzero coordinates), and the anchor is unique. There are therefore \(2\cdot3^3=54\) uncompletable cases. Adding the completable cases gives \(36+9=45\) and \(216+54=270\). In dimension at least four, Step 4 rules out the exceptional cases and yields exactly \(6^n\). This completes the proof.

## Verification

The included standalone `verify.py` uses only the Python standard library and independently tests the **original line-hitting condition**. It exhaustively enumerates all size-four line-hitting sets in dimension two, and all size-ten candidates in dimension three using their independently forced three- or four-point two-dimensional layers. It finds, respectively, \(45\) and \(270\) solutions, with \(9\) and \(54\) uncompletable. It also independently enumerates maximum line-hitting sets in dimensions three and four and finds exactly \(12\) and \(24\), agreeing with the affine classification. Finally, it checks all \(16\) four-dimensional triple-parity profiles and verifies that each admits exactly one compatible weight-four sign vector. Execute with `python3 verify.py`; the final output is `VERIFY_OK`. These are finite checks and are not presented as a substitute for the all-dimensional proof.

## Relationship to prior work

Csajbók, Mukkamala, and Nagy prove the sharp vertex extremum \(T_q(n,1)=2q^{n-1}\) for triangle-free induced sets in unit-distance Hamming graphs (Theorem 1.3, Section 3.1 of arXiv:2610.32789). Their coordinate-line argument supplies the starting size bound; it does not give the defect-one completion theorem or the counts proved here. The characterization of maximum ternary complements as distance-two MDS codes / ternary quasigroups connects to classical coding theory; only the next-to-extremal stability and enumeration are proposed as new. Krotov's discussion of quasigroups and MDS codes (arXiv:math/0607284) concerns exact one-per-line objects, not the one-extra-point line-hitting classification. Work on Latin-cuboid completion in alphabet size five is related in terminology but has different constraints. No historical-priority or independent-audit certification is claimed.

## Limitations

The exact count and the unique-completion transition concern the alphabet \(\mathbb F_3\), Hamming distance exactly one, and near-maximum sets with deficiency exactly one. They do not classify arbitrary deficiencies, larger alphabets, different Hamming distances or the broader literature of noncompletable Latin arrays. The verification program covers low dimensions only; the infinite classification is established by the written proof. Historical coverage remains qualified by possible differently named results on coordinate-line blocking sets.

## References

1. B. Csajbók, P. Mukkamala and Z. L. Nagy, *Triangle-Free Sets in Exact-Distance Hamming Graphs*, arXiv:2610.32789, first public 2026-10-23, especially Theorem 1.3 and Section 3.1. https://arxiv.org/abs/2610.32789
2. D. S. Krotov, *On reducibility of n-ary quasigroups*, arXiv:math/0607284, 2006. https://arxiv.org/abs/math/0607284
3. A. L. Perezhogin, V. N. Potapov and S. Yu. Vladimirov, *Every latin hypercube of order 5 has transversals*, *Journal of Combinatorial Designs*, 2024, https://doi.org/10.1002/jcd.21954 (related completion vocabulary; not equivalent objects).
