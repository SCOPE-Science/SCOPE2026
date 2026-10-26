# Parity, a resonant exception, and token exchanges among minimum identifying codes of cycles

## Finding
For the ordinary cycle \(C_n\) and closed-neighborhood radius-one identifying codes, let \(\mathcal I_n\) be the graph whose vertices are **minimum-cardinality** identifying codes, with two codes adjacent precisely when one vertex of the code can be replaced by one vertex outside it.

**Theorem.** For every even \(n\ge 8\), the minimum cardinality is \(n/2\) and \(\mathcal I_n\cong 2K_1\): its only two vertices are the complementary alternating codes and neither admits an exchange.

For every odd \(n\ge13\), the minimum cardinality is \((n+3)/2\). If \(n\ne15\), there are exactly \(2n\) minimum codes and \(\mathcal I_n\) is a connected graph with \(2n\) vertices and \(3n\) edges, comprising \(n\) degree-four vertices \(H_i\) and \(n\) degree-two vertices \(L_i\), where indices are modulo \(n\) and
\[
H_i\sim H_{i+2},\qquad H_i\sim H_{i-2},\qquad H_i\sim L_{i+1},\qquad H_i\sim L_{i+5}.
\]
There are no further edges. In particular, the subgraph induced by \(H_i\) is an \(n\)-cycle (because \(n\) is odd), and each \(L_i\) subdivides a distance-two chord of that cycle.

At the exceptional odd order \(n=15\), there are exactly \(35\) minimum codes. The exchange graph is the just-described connected \(30\)-vertex graph together with **five isolated vertices**; it has exactly \(45\) edges. Thus minimal identifying-code exchange connectivity exhibits an even/odd dichotomy and a unique resonant disconnection within the odd range \(n\ge13\).

The explicit cyclic bit words for the two regular orbits are
\[
H=1111(01)^{(n-5)/2}0,\qquad L=111(01)^{(n-7)/2}1100.
\]
The code \(H_i\) (respectively \(L_i\)) is the shift of the displayed word by \(i\) vertex positions. At \(n=15\), the additional five minimum codes are the distinct rotations of the periodic word \((00111)^3\).

## Assumptions and scope
Vertices are \(\mathbb Z/n\mathbb Z\) with edges between consecutive residues. A code \(C\subseteq V(C_n)\) is identifying when each set \(I(v)=N[v]\cap C\) is nonempty and \(I(u)\ne I(v)\) whenever \(u\ne v\), where \(N[v]\) includes \(v\). Bit \(1\) in a word means a selected code vertex; coordinates increase cyclically. Edges of \(\mathcal I_n\) are **token-jumping** one-out/one-in exchanges, not arbitrary local token sliding. The result concerns only \(n\ge8\) even and \(n\ge13\) odd; the odd shorter lengths are not part of the classification statement. All counts are for labeled cycles, not dihedral equivalence classes.

## Proof
**1. Exact local characterization.** For \(n\ge7\), a cyclic bit word \(c\) defines an identifying code precisely when
\[
 c_i+c_{i+1}+c_{i+2}\ge1\quad\text{and}\quad c_i+c_{i+3}\ge1
 \qquad\text{for every }i\pmod n.
\]
The first condition is exactly closed-neighborhood domination. The symmetric difference of the closed neighborhoods of adjacent vertices is the pair at distance three; for vertices at distance two, another pair at distance three occurs in the symmetric difference, and these pairs guarantee separation. Neighborhoods at distance at least three are disjoint, or, at cyclic distance three, disjoint, hence are separated once both are nonempty. Conversely, separating adjacent vertices forces the second condition. The hypotheses \(n\ge7\) avoid wraparound collisions between the relevant neighborhoods.

**2. An exact low-excess census.** Consider cyclic words satisfying these conditions, weighted by \(t\) for each selected bit. Use nonzero three-bit states \(abc\in\{0,1\}^3\setminus\{000\}\), allowing \(abc\to bcd\) with weight \(t^d\) exactly when \(a+d\ge1\). Let \(T(t)\) be the resulting seven-by-seven transfer matrix (state order \(001,010,011,100,101,110,111\)). The trace \(\operatorname{tr}(T(t)^n)\) counts every valid labeled circular word of length \(n\), once per word. Direct expansion of this explicit determinant gives
\[
D(z,t)=\det(I-zT(t))
=1-tz-tz^2+t^2z^3-t^3z^4-t^3z^5+t^4z^7.
\]
Consequently the bivariate enumerator is exactly
\[
\sum_{n\ge1}\operatorname{tr}(T(t)^n)z^n
=-z\frac{\partial}{\partial z}\log D(z,t).
\]
Introduce \(t=u^2\), \(z=w/u\) and note
\[
D(w/u,u^2)=(1-w^2)\left[1-u\,w(1+w^4)\right]-u^2w^4.
\]
Writing \(A=w(1+w^4)\) and \(B=w^4/(1-w^2)\), the nonconstant portion of the logarithmic series becomes
\[
w\frac{\partial}{\partial w}\sum_{r\ge1}\frac{(uA+u^2B)^r}{r},
\]
while the \(u^0\) portion is \(2w^2/(1-w^2)\). In this substitution, the power of \(u\) attached to a word is exactly the **excess** \(e=2|C|-n\).

The coefficient of \(u^0\) is \(2w^2/(1-w^2)\); for every even \(n\ge8\), exactly two words have excess zero. No negative excess is possible, as the displayed expansion contains no negative powers of \(u\). The two words are the alternating codes. The coefficient of \(u^1\) is \(w+5w^5\), hence for odd \(n\ge7\) excess one is impossible. The coefficient of \(u^3\) is
\[
 w\frac{\partial}{\partial w}\left(AB+\frac{A^3}{3}\right)
=w\frac{\partial}{\partial w}\left(\frac{w^5+w^9}{1-w^2}+\frac{w^3+3w^7+3w^{11}+w^{15}}3\right).
\]
For every odd \(n\ge13\), this supplies \(2n\) words of excess three, except at \(n=15\), when it supplies \(2n+5=35\). Since odd excess one is absent, these are the minimum codes. Substituting the displayed \(H\) and \(L\) words into the two local conditions produces \(n\) distinct rotations of each, with distinct patterns (\(H\) has no adjacent zeros, \(L\) has exactly one adjacent-zero pair). At \(n=15\), the five rotations of \((00111)^3\) are five additional valid words, distinguished by their three disjoint adjacent-zero pairs. Their total equals the transfer-matrix count, proving there are no other minimum configurations.

**3. Exchanges.** Even-order alternating words differ in all \(n\) coordinates, hence cannot differ by one selected-vertex exchange when \(n\ge8\).

For odd \(n\ge13\), the zero positions of \(H_0\) are exactly \(4,6,8,\ldots,n-1\), an interval of length \((n-3)/2\) when the cyclic group is read in steps of two. Two such translated intervals differ in precisely one zero position apiece if and only if their step-two shifts are adjacent, i.e. ordinary rotation shifts \(\pm2\). Hence two members of the \(H\) orbit have a single-token exchange exactly for those shifts. To change \(H_0\) into a member of the \(L\) orbit, one exchange must both destroy the unique run \(1111\) of \(H_0\) and create the adjacent-zero pair of an \(L\) word. Its only possible outgoing deletions are at the two endpoints of that run. Completion to a valid \(L\)-type word forces respectively the exchanges \(H_0\leftrightarrow L_1\) and \(H_0\leftrightarrow L_5\). This proves the two types of indicated edges after rotating.

Every \(L_i\) has a unique adjacent-zero pair. A single token exchange between two \(L\) words must make those two pairs intersect (at most one zero is lost), hence their rotation difference is \(\pm1\); however the zero sites of \(L_0\) are \(3,5,\ldots,n-6\) together with \(n-2,n-1\), and this set intersects either shift by one in exactly one position. Thus \(L_i\) and \(L_{i\pm1}\) differ at exactly \(n-5\ge8\) bit positions, not two. Hence no \(L\)-to-\(L\) edges exist. Since the shifts by \(2\) generate \(\mathbb Z/n\mathbb Z\) for odd \(n\), all \(H\) vertices and their \(L\) neighbors lie in one component. Its degree sequence and \(3n\) edges follow immediately.

At \(n=15\), the five extra words have three pairwise disjoint adjacent-zero pairs. A single token exchange destroys at most one of those pairs, so none can reach an \(H\) (zero such pairs) or \(L\) (one such pair) word. Distinct rotations of \((00111)^3\) differ by at least three token positions, so they are mutually nonadjacent. Therefore all five are isolated.

## Verification
The accompanying standalone `verify.py` uses only Python's standard library. For every \(7\le n\le18\), it examines all \(2^n\) vertex subsets, compares direct closed-neighborhood separation with the independent local-constraint test, constructs the exact transfer-matrix trace polynomial, and checks it against the directly counted weight polynomial. It enumerates all minimum sets and their one-token exchanges, and tests the stated components, counts, and every predicted edge. For additional odd orders \(19,21,23,25,31,41,51,99\), the program constructs both prescribed orbits and compares their full exchange adjacency with the theorem. A successful run prints `VERIFY_OK`.

These finite checks cross-test definitions, coefficients, and adjacency. The symbolic transfer-matrix and combinatorial exchange proofs establish the infinite-order claims; the computation is not used as an infinite proof.

## Relationship to prior work
Bertrand, Charon, Hudry and Lobstein (2004) establish the graph-identifying-code framework and exact **minimum sizes** on chains and numerous cycle orders. Gravier, Moncel and Semri (2006), Xu, Thulasiraman and Hu (2008), and Junnila and Laihonen (2012) further treat optimal identifying-code cardinalities on cycles, including difficult residues. The previously established minimum cardinalities are not presented as new here. The distinct contribution is the complete number and geometry of optimal codes for the stated infinite ranges, including the five isolated order-fifteen configurations and exact one-token exchange graph. The relevant publicly accessible foundational text was inspected; the complete texts of several closely related later works could not be inspected, leaving possible equivalent earlier classifications as a limitation.

## Limitations
The theorem excludes even orders below eight and odd orders below thirteen. It concerns ordinary closed-neighborhood identifying codes (not locating-dominating codes, identifying-open codes, or tolerance variants). It concerns minimum codes only, and the graph of one-token exchanges, not arbitrary code additions/removals. The all-order proof depends on the explicit seven-state determinant and exhaustive template-exchange comparisons, which can be checked independently; tested finite cases are cross-checks only. Full primary texts of several plausibly relevant earlier papers were unavailable, so novelty is best-knowledge rather than globally certified. Independent scholarly review has not been performed.

## References
- N. Bertrand, I. Charon, O. Hudry and A. Lobstein, *Identifying and locating-dominating codes on chains and cycles*, European Journal of Combinatorics 25 (2004), 969–987. DOI: 10.1016/j.ejc.2003.12.013. Publicly available online March 10, 2004. Open full text: https://lsv.ens-paris-saclay.fr/Publis/PAPERS/PDF/BCHL-ejc04.pdf
- S. Gravier, J. Moncel and A. Semri, *Identifying codes of cycles*, European Journal of Combinatorics (2006). DOI: 10.1016/j.ejc.2004.09.005.
- W. Xu, K. Thulasiraman and X. Hu, *Identifying codes of cycles with odd orders*, European Journal of Combinatorics (2008). DOI: 10.1016/j.ejc.2007.09.006.
- V. Junnila and T. Laihonen, *Optimal Identifying Codes in Cycles and Paths*, Graphs and Combinatorics (2012; first published online 2011). DOI: 10.1007/s00373-011-1058-6.
