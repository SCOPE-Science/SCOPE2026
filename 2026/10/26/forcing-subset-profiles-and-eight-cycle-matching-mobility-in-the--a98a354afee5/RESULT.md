# Forcing-subset profiles and eight-cycle matching mobility in the dodecahedral graph

## Finding
Let \(D\) denote the dodecahedral graph, equivalently the generalized Petersen graph \(GP(10,2)\). For a perfect matching \(M\), define its *forcing-subset polynomial* by
\[P_M(z)=\sum_{S\subseteq M:\,S\not\subseteq M'\text{ for all other perfect matchings }M'}z^{|S|}.\]
There are exactly \(36\) perfect matchings. Their forcing-subset polynomials comprise exactly two types:
\[
\begin{aligned}
P_{\rm A}(z)&=20z^3+110z^4+202z^5+200z^6+120z^7+45z^8+10z^9+z^{10},&&\text{in six matchings},\\
P_{\rm B}(z)&=24z^3+122z^4+216z^5+204z^6+120z^7+45z^8+10z^9+z^{10},&&\text{in thirty matchings}.
\end{aligned}
\]
Consequently every matching has forcing number \(3\), but six of the matching configurations have exactly \(20\) forcing triples while the other thirty have exactly \(24\).

Let \(\mathcal F_8(D)\) have the \(36\) perfect matchings as vertices and join two matchings precisely when they are related by flipping the matched and unmatched edges of a single alternating eight-cycle. Then \(\mathcal F_8(D)\) is connected, has \(120\) edges, and has radius and diameter \(3\). Its degree profile is \(6\) vertices of degree \(10\) and \(30\) vertices of degree \(6\). The degree-ten class is exactly the \(P_{\rm A}\) class: each of its vertices is adjacent to ten degree-six vertices, while each degree-six vertex has exactly two degree-ten neighbors.

## Assumptions and scope
All graphs are finite, undirected, simple, and labelled for enumeration. The graph \(D\) has vertices \(u_i,v_i\) for \(i\in\mathbb Z/10\mathbb Z\), with edges \(u_i u_{i+1}\), \(u_i v_i\), \(v_i v_{i+2}\). Every index is reduced modulo \(10\). This graph has exactly twenty vertices and thirty edges; it is the classical dodecahedral graph. All perfect matchings consist of ten pairwise disjoint edges covering every vertex. A subset \(S\subseteq M\) is forcing when no other perfect matching contains \(S\). The coefficient of \(z^k\) counts every forcing subset of cardinality \(k\), not just inclusion-minimal forcing sets. A flip along an alternating eight-cycle exchanges its four matching edges with the four complementary cycle edges.

## Proof
The proof is a finite exhaustive certificate with two different standalone implementations. Here are the completeness arguments and the executable checks.

**1. Enumeration of every perfect matching.** In `check_gp.py`, the procedure `walk(free,m)` always chooses the least unused vertex \(u\) and branches over every as-yet unused neighbor \(v\), adding the edge \(uv\). Every perfect matching must contain exactly one of these edges. Induction on the size of `free` shows that every matching is generated and no matching can be omitted. Each path covers every vertex once, and the final canonical-set operation removes duplication. Direct execution yields exactly \(36\) distinct matchings. The independent `check_lcf.py` realizes the same dodecahedral graph via its length-twenty LCF chord sequence \((10,7,4,-4,-7,10,-4,7,-7,4)\) repeated twice. Its matching recursion branches on a free vertex of minimum available degree rather than the least vertex and again yields \(36\) solutions.

**2. Exact forcing counts.** Fix a generated matching \(M\). Every subset of its ten edges appears once among the \(2^{10}\) masks (or, equivalently, the combinations by size). The predicate
\[S\text{ is forcing}\iff\#\{M':\,S\subseteq M'\}=1\]
is exactly the definition because \(M\) itself contains \(S\). The first checker evaluates this predicate for all \(36\cdot2^{10}\) pairs \((M,S)\) and obtains the two coefficient lists in the statement, with respective frequencies six and thirty. The second checker instead forms the difference families \(M\setminus M'\) for all \(M'\ne M\) and uses the mathematically equivalent criterion that \(S\) intersects each difference. It reproduces every coefficient and both multiplicities. In particular, coefficients in degrees zero, one and two vanish and every matching has a nonzero coefficient in degree three.

**3. Exact eight-cycle flip graph.** Two distinct perfect matchings have symmetric difference a disjoint union of alternating even cycles. A difference containing eight edges must be one alternating eight-cycle: there are no four-cycles in \(D\), so two disjoint alternating cycles would need at least twelve edges. Conversely, flipping an alternating eight-cycle changes exactly eight edges of the symmetric difference. Thus the first checker builds the entire flip graph by the test \(|M\triangle M'|=8\) over all \(\binom{36}{2}\) unordered matching pairs. It finds \(120\) edges, a connected \(36\)-vertex graph, six vertices of degree ten, thirty vertices of degree six, and eccentricity three at every vertex.

The independent checker obtains flips without inspecting pairwise matching differences: for each matching it selects every four-edge subset, identifies its eight incident vertices, enumerates all alternative coverings of those eight vertices using nonmatching edges, and retains targets that are perfect matchings. An admissible replacement is necessarily one alternating eight-cycle by the preceding absence-of-four-cycles argument. This obtains the same \(120\) edges, connectivity, radius, diameter, and degree profile. Both complete checks show that precisely the six matchings with \(20\) forcing triples have degree ten; the others have degree six. Counting the cross-type incidence gives sixty cross edges, with ten incident to each degree-ten matching and two to each degree-six matching, as explicitly verified by the first checker.

Each recursion, test, and breadth-first search operates on a finite, completely specified search space. Neither a sampling assumption nor extrapolation from a bounded parameter range is used.

## Verification
Requires Python 3 standard library only. From the folder containing this document and the accompanying scripts, run `python3 check_gp.py` and `python3 check_lcf.py`. The expected exact records are in `check_gp_output.json` and `check_lcf_output.json`. The two programs use inequivalent labelled realizations (generalized Petersen and LCF) and different forcing predicates and flip construction mechanisms. They were run directly from the accompanying paths before inclusion, and both completed all asserted checks. Their finite audit domain is the complete set of perfect matchings and all \(2^{10}\) candidate subsets of each.

## Relationship to prior work
The dodecahedron's \(36\) perfect matchings, and their prior-known \(30+6\) decomposition from the Petersen quotient, are described in the January 2015 MathOverflow proof [2]; those counts and the split alone are not proposed as new. The general fullerene forcing-number lower-bound research of Zhang–Ye–Shiu [1] and the later correction/classification by Shi–Zhang–Lin [3] do not determine the complete forcing-subset polynomials or the eight-cycle-flip graph. Han–Zhou–Wang [4] explicitly report \(\{3\}\) as the ordinary forcing-number spectrum for the twenty-vertex fullerene; the present result refines this constant spectrum by counting *all* forcing subsets by size, and relates those two distinct profiles to a natural local transformation graph. Unlike a face-resonance move (involving hexagonal faces), the present move is any abstract alternating eight-cycle of the pentagonal dodecahedron.

## Limitations
This is a finite exact classification for the dodecahedral graph, not a theorem for arbitrary fullerenes. It does not claim the known number \(36\) of perfect matchings, the forcing number \(3\), or the existence of the \(30+6\) split as new. Novelty of the refined coefficient lists and complete eight-cycle transformation graph is based on the inspected accessible literature and searches, not an independent priority guarantee. The 2010 paper [1] was available in accessible bibliographic and abstract form but not in full text; this leaves some residual publication-priority risk. Full independent scientific audit has not been performed.

## References
[1] H. Zhang, D. Ye and W. C. Shiu, “Forcing matching numbers of fullerene graphs,” *Discrete Applied Mathematics* 158 (2010), 573–582, DOI 10.1016/j.dam.2009.10.013. Accessible institutional abstract: https://scholars.hkbu.edu.hk/en/publications/forcing-matching-numbers-of-fullerene-graphs/ .

[2] A. P. Goucher, “Number of perfect matchings of the dodecahedron,” mathematical derivation posted January 25, 2015: https://mathoverflow.net/questions/192159/number-of-perfect-matchings-of-the-dodecahedron .

[3] L. Shi, H. Zhang and R. Lin, “Characterizing the fullerene graphs with the minimum forcing number 3,” arXiv:1812.03750 (first posted 2018-12-10), https://arxiv.org/pdf/1812.03750 .

[4] H. Han, Y. Zhou and Y. Wang, “Continuity of matching forcing spectra and anti-forcing spectra for lower-order fullerenes,” *Advances in Applied Mathematics* 12 (2023), 1173–1187, DOI 10.12677/aam.2023.123119; freely accessible full text: https://pdf.hanspub.org/aam20230300000_67842798.pdf .
