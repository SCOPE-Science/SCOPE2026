# Affine rigidity at the six-bit limit for systematic parity-protecting codes

## Finding
Let \(k\ge1\) and \(f:\mathbb F_2^k\to\mathbb F_2\) be message parity,
\[
f(x)=\sum_{i=1}^k x_i\pmod 2.
\]
Consider every systematic binary encoder \(E_p(x)=(x,p(x))\) with an **arbitrary** map \(p:\mathbb F_2^k\to\mathbb F_2^r\), subject to the two distance conditions in the next section. The least possible redundancy is
\[
r_1=4,\qquad r_k=5\quad(2\le k\le6),\qquad r_k\ge6\quad(k\ge7).
\]

There is a sharp rigidity statement at the last feasible dimension with five check bits. Write \(J=(1,1,1,1,1)\in\mathbb F_2^5\), and let \(e_j\) denote its five standard basis vectors. Put \(v_0=J\) and \(v_j=J+e_j\) for \(1\le j\le5\). When \(k=6\) and \(r=5\), every valid map is precisely
\[
p(x)=b+\sum_{i=1}^{6} x_i v_{\pi(i)},
\]
where \(b\in\mathbb F_2^5\) is arbitrary and \(\pi:\{1,\ldots,6\}\to\{0,1,2,3,4,5\}\) is a bijection. Conversely every displayed map is valid. Therefore the exact number of **labeled** systematic maps is
\[
2^5\,6!=23040.
\]
All are equivalent using a permutation of the message coordinates and translation of the five check bits. In particular no genuinely nonlinear solution survives equality.

## Assumptions and scope
All vector arithmetic below is over \(\mathbb F_2\). For distinct messages \(x,y\), define \(d(x,y)\) as their Hamming distance; the encoded distance is \(d(E_p(x),E_p(y))=d(x,y)+d(p(x),p(y))\). We require
\[
 d(E_p(x),E_p(y))\ge3\quad\text{for all }x\ne y,
\]
and, more strongly,
\[
 d(E_p(x),E_p(y))\ge5\quad\text{whenever }f(x)\ne f(y).
\]
These are respectively single-error correction for the full message and two-error correction for the parity value. No linearity, bijectivity, or other assumption is imposed on \(p\). The classification counts distinct maps with ordered message coordinates and ordered check coordinates; equivalence does not permit arbitrary relabeling of the protected function.

## Proof
**1. At least five check bits once \(k\ge2\).** If \(y=x+e_i\), then the message distance is one and parities differ. Thus \(d(p(x),p(y))\ge4\), forcing \(r\ge4\). If \(r=4\), the only four-bit vector at distance four from \(p(x)\) is its complement. Therefore every edge of the message hypercube forces \(p(x+e_i)=\overline{p(x)}\). Connectivity and bipartiteness imply that \(p\) is constant separately on the even- and odd-parity message classes. For \(k\ge2\), two messages differing in exactly two coordinates have identical check words, giving encoded distance two, contrary to data protection. Hence \(r\ge5\).

**2. Five check bits admit at most six message coordinates.** Fix any \(x\in\mathbb F_2^k\). Its \(k\) neighbors \(x+e_i\) all differ in parity, so their check words lie in the radius-one Hamming ball centered at \(\overline{p(x)}\in\mathbb F_2^5\). This ball has exactly six elements: its center and the five words obtained by flipping one check coordinate. For \(i\ne j\), the messages \(x+e_i\) and \(x+e_j\) are at message distance two; data protection demands different check words. Consequently these \(k\) check words are distinct, so \(k\le6\). This excludes every five-check-bit encoder at \(k\ge7\), regardless of linearity.

**3. The equality case forces a labeled edge coloring.** Assume \(k=6\) and \(r=5\). The six neighbors of each \(x\) use every member of the antipodal radius-one ball exactly once. Put \(e_0=0\) in \(\mathbb F_2^5\). Each edge from \(x\) to \(x+e_i\) therefore has a uniquely determined color \(c_i(x)\in\{0,1,2,3,4,5\}\) satisfying
\[
p(x+e_i)+p(x)=J+e_{c_i(x)}.
\]
The color is independent of the direction in which an undirected edge is traversed. At each vertex, all six incident colors are distinct.

**4. Every square has the same color on opposite edges.** Traverse any square of the message hypercube using distinct coordinate directions \(i,j\). Since each check word occurs twice in the XOR of the four edge increments, this XOR is zero. The four copies of \(J\) cancel, leaving
\[
e_a+e_b+e_c+e_d=0,
\]
where \(a,b,c,d\) are the colors of consecutive edges. The six vectors \(e_0=0,e_1,\ldots,e_5\) have no nontrivial four-term zero sum except repetitions in pairs: every nonzero basis vector must appear an even number of times, and then so must the zero label. Moreover neighboring edges have different colors by the bijection at their common vertex. Hence the two equal-colored pairs necessarily occupy opposite edges. For each \(i\ne j\),
\[
c_i(x)=c_i(x+e_j).
\]
The two orientations of each \(i\)-edge already have the same color, so \(c_i(x)\) also remains unchanged when the \(i\)-th bit of \(x\) is flipped. Thus \(c_i(x)\) is independent of **all** coordinates of \(x\): write it simply \(c_i\). The incident-color bijection forces \(i\mapsto c_i\) to be a permutation of the six colors.

**5. Affinity and enumeration.** Define \(b=p(0)\). Integrating the now constant edge increments along any path from zero to \(x\) yields
\[
p(x)=b+\sum_{i=1}^6x_i(J+e_{c_i}).
\]
This is the asserted affine form, with all six distinct columns. Its parameters are uniquely recoverable as \(b=p(0)\) and \(v_{c_i}=p(e_i)+p(0)\), so there are precisely \(2^5\,6!\) distinct maps.

**6. Every displayed map works.** Let \(S\) be the nonempty set of message positions changed between two messages and write \(m=|S|\). Since the six columns are distinct, if \(m=2\) their XOR is nonzero and the encoded distance is at least three. If \(m\ge4\) is even, its message contribution alone is at least four, meeting the required data distance. If \(m=1\), the single check-column has weight four or five, giving encoded distance at least five. If \(m=3\), XOR of the three distinct check columns equals \(J\) plus at most three distinct standard basis vectors; it therefore has Hamming weight at least two, giving total distance at least five. If \(m\ge5\) is odd, the message distance alone suffices. This proves the two requirements for all pairs. Restricting to any \(2\le k\le5\) input columns gives a valid five-check-bit construction, and the lower bound in Step 1 is tight. For \(k=1\), four complementary check bits give total distance five, and fewer than four cannot.

## Verification
The standalone file `verify.py` uses only the Python standard library. Run `python3 verify.py` in the folder containing the file. It checks all six-column choices, tests all \(720\) zero-offset affine encoders against every message pair, confirms the \(30\) admissible four-edge square patterns have matching opposite colors, checks the constructions for \(2\le k\le6\), and excludes all \(65536\) maps with four check bits for \(k=2\). The run produced `VERIFY_OK`. The general exclusion and classification are consequences of Steps 1–6, **not** inferences from a finite sample.

## Relationship to prior work
Rajput, Rajan, Freij-Hollanti, and Hollanti (2025) introduced function-correcting codes with data protection; their Theorem 4 already supplies the general binary redundancy lower bound \(r\ge2t_f+t_d\), which equals five here, and Example 10 constructs a five-check-bit parity-protecting code for four message bits. The length and redundancy alone are therefore **not new**. Rajput and collaborators' March 2026 follow-up repeats the four-bit example and studies general nonexistence criteria for distance graphs. Van Gils (1982), Appendix A, includes the linear unequal-error-protection separation vector \((5,3,3,3,3,3)\) at length eleven and dimension six; this is a direct warning against claiming linear feasibility as novel. These sources do not establish that arbitrary nonlinear systematic equality-case maps are necessarily affine, enumerate all \(23040\) of them, or give the sharp six-coordinate threshold by the antipodal-neighbor square argument. The new contribution is specifically that **rigidity and classification**.

## Limitations
This is a binary Hamming-metric theorem for the specified parity function and precisely the data/function distance pair \((3,5)\). For dimensions \(k\ge7\) it proves only that five check bits are impossible, **not** the exact larger optimal redundancy. For \(2\le k<6\) it proves the optimal check-bit count but does **not** classify all five-check-bit encoders. The enumeration counts labeled maps at \(k=6\), not equivalence classes for a different metric or a nonsystematic encoder model. No independent scientific audit has been performed; the derivation and checks remain subject to external review. Earlier unindexed nonlinear unequal-protection classifications could overlap the contribution.

## References
- C. Rajput, B. Sundar Rajan, R. Freij-Hollanti, and C. Hollanti, *Function-Correcting Codes With Data Protection*, first public preprint 2025-11-23, https://arxiv.org/abs/2511.18420 (Theorem 4, Example 10).
- C. Rajput, B. Sundar Rajan, R. Freij-Hollanti, and C. Hollanti, *Non-Existence of Some Function-Correcting Codes With Data Protection*, 2026, https://arxiv.org/abs/2603.01049 (Example 1 and distance-graph results).
- C. Rajput, B. Sundar Rajan, R. Freij-Hollanti, and C. Hollanti, *Existence and Constructions of Strict Function-Correcting Codes with Data Protection*, 2026, https://arxiv.org/abs/2604.26397 (linear strict-code constructions).
- W. J. van Gils, *On Linear Unequal Error Protection Codes*, Eindhoven University of Technology report 82-WSK-02, 1982, https://pure.tue.nl/ws/portalfiles/portal/4297991/253159.pdf (Appendix A, linear separation vectors).
