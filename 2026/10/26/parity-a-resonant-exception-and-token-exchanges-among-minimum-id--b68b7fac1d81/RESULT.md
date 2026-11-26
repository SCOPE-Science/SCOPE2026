# Parity, a resonant exception, and token exchanges among minimum identifying codes of cycles

## Finding

Let \(\mathcal I_n\) have the minimum radius-one identifying codes of the labeled cycle \(C_n\) as its vertices, with edges for one selected vertex exchanged for one unselected vertex. For even \(n\ge8\), the minimum size is \(n/2\) and \(\mathcal I_n\cong 2K_1\), with the two alternating codes as vertices. For odd \(n\ge13\), the minimum size is \((n+3)/2\). The rotations \(H_i,L_i\) (shifting by \(+i\) modulo \(n\)) of
\[
H=1111(01)^{(n-5)/2}0,\qquad L=111(01)^{(n-7)/2}1100
\]
form a connected graph on \(2n\) vertices and \(3n\) edges. Its entire edge set is given by
\[
H_i\sim H_{i\pm2},\qquad H_i\sim L_{i+1},L_{i+5}.
\]
The \(H\) orbit induces a cycle and each \(L\) subdivides a distance-two chord of that cycle. These rotations exhaust the minimum codes except at \(n=15\), when there are also the five distinct rotations of \((00111)^3\), all isolated. Thus \(\mathcal I_{15}\) has 35 vertices and 45 edges.

## Assumptions and scope

A code \(C\subseteq\mathbb Z/n\mathbb Z\) is identifying if all the intersections \(N[v]\cap C\) of closed neighborhoods with the code are nonempty and pairwise distinct. A 1 in a cyclic word denotes membership, and indexing starts at zero. Counts are for labeled cycles; exchanges are unrestricted one-out/one-in moves on minimum codes, not token slides.

## Proof

**Local conditions.** For \(n\ge7\), a code word \(c\) is valid exactly when it has no three consecutive zeros and no two zeros at cyclic offset three. The first condition gives domination. For adjacent vertices, their closed-neighborhood symmetric difference is the pair of vertices at offset three, so separation requires the second condition. For distance-two vertices \(i,i+2\), the symmetric difference contains \(i-1,i+2\), again at offset three, which ensures separation. At cyclic distance at least three the neighborhoods are disjoint and nonempty.

**Minimum counts.** Use the transfer matrix \(T(t)\) with states \(001,010,011,100,101,110,111\), transitioning \(abc\to bcd\) with weight \(t^d\) when both states are allowed and \(a+d\ge1\). The trace of \(T^n\) counts all labeled cyclic words with these local conditions, with \(t\) marking code size, since the index zero fixes the start of the closed walk and every word determines its states. To check the determinant, the simple directed cycles in the state graph are the loop at 111, the cycle \(010,101\), the cycle \(011,111,110,101\), and the cycle \(001,011,111,110,100\), with weights \(t,t,t^3,t^3\). The only pairs of disjoint cycles are the length-two cycle with the loop and with the length-five cycle. Expanding by disjoint cycles gives
\[
D(z,t)=\det(I-zT(t))=1-tz-tz^2+t^2z^3-t^3z^4-t^3z^5+t^4z^7,
\qquad \sum_{n\ge1}\operatorname{tr}(T(t)^n)z^n=-z\partial_z\log D.
\]
Under \(t=u^2,z=w/u\), the exponent of \(u\) is the excess \(2|C|-n\). The determinant factors as \((1-w^2)(1-uA-u^2B)\), where \(A=w(1+w^4)\) and \(B=w^4/(1-w^2)\). Consequently no negative excess occurs. The coefficients of \(u^0,u^1,u^3\) in the logarithmic derivative are, respectively,
\[
\frac{2w^2}{1-w^2},\qquad w+5w^5,\qquad
w\partial_w\left(\frac{w^5+w^9}{1-w^2}+\frac{w^3+3w^7+3w^{11}+w^{15}}{3}\right).
\]
Even lengths have exactly the two exhibited alternating codes at excess zero. At odd \(n\ge13\), excess one is absent and excess three gives \(2n\) codes plus an extra five at \(n=15\).

The exhibited words are valid: the zeros of \(H\) are \(4,6,\ldots,n-1\), with no adjacent pair or offset-three pair. In \(L\) they are \(3,5,\ldots,n-6\) and \(n-2,n-1\). The odd zeros have even ordinary differences at most \(n-5\), so none is at offset three from another; the even zero \(n-1\) has odd differences 1 or at least 5 from the odd zeros, which are not 3 or \(n-3\). There is just one adjacent-zero pair, and no triple. The unique length-four run of ones of \(H\) and the unique adjacent-zero pair of \(L\) ensure full rotation orbits; those orbits are distinct. The five periodic words have zeros in two consecutive residues modulo five, yielding neither a triple nor offset-three zeros. Their three disjoint adjacent-zero pairs distinguish them from the regular words. This list attains the minimum counts from the trace.

**All exchanges between regular words.** Use zero sets, so two distinct regular codes are adjacent exactly when their zero sets intersect in all but one position. Even alternating codes cannot be adjacent because their zero sets are disjoint and have size at least four. In the odd case write \(n=2m+3\), \(m\ge5\). Change coordinates from an ordinary vertex \(v\) to \(j\) with \(v=2j\pmod n\). The \(H_0\) zero set is now the circular interval \([2,m+1]\) and the \(L_0\) zero set is \(m+1+A_0\), where
\[
A_0=\{0\}\cup[2,m-1]\cup\{m+1\}.
\]
Here integer intervals are inclusive, read modulo \(n\). A shift by \(i\) ordinary vertices translates zero sets by \(i/2\) in these coordinates. Two length-\(m\) circular intervals have intersection \(m-1\) exactly when their translations differ by \(\pm1\): by swapping the intervals the shift can be taken in \([1,m+1]\), where \([0,m-1]\) and its translate do not wrap and intersect in \(\max(0,m-s)\) for shift \(s\). This gives the two \(H\)-to-\(H\) neighbors.

A length-\(m\) interval meeting \(A_0\) in \(m-1\) points must include exactly one endpoint of \([0,m+1]\): the interior has only \(m-2\) points of \(A_0\), and neither circular arc between the endpoints fits in the interval. It must also include all interior points. Including 0 then forces the entire interval \([0,m-1]\); including \(m+1\) forces \([2,m+1]\), since the other arcs between the respective extreme required points are too long. Each candidate works. Therefore \(H_0\) is adjacent to \(L_i\) when the start 2 of its interval equals \(m+1+i/2\) or \(m+3+i/2\); equivalently \(i=5\) or \(i=1\). Rotation gives all cross edges.

For two \(L\) sets, by symmetry it suffices to check \(|A_0\cap(A_0+s)|\) for \(1\le s\le m+1\), where the translated set does not wrap. At \(s=1\) the intersection is \([3,m-1]\), of size \(m-3\). At \(s=2\) it is \(\{2\}\cup[4,m-1]\cup\{m+1\}\), of size \(m-2\). For \(s\ge3\) it is contained in \([s,m+1]\setminus\{m\}\), of size \(m+1-s\le m-2\). Thus there are no \(L\)-to-\(L\) edges; this does not require any assumption about whether the two adjacent-zero pairs intersect. Since \(n\) is odd, the \(\pm2\) shifts produce one \(n\)-cycle. Each \(L_i\) connects \(H_{i-1}\) and \(H_{i-5}\), at distance two along that cycle. There are \(n\) cycle edges and \(2n\) cross edges.

**Exceptional exchanges.** At \(n=15\), one zero exchanged can destroy at most one of the three disjoint adjacent-zero pairs in an exceptional word, so at least two survive. This rules out adjacency to any \(H\) or \(L\). Two different exceptional rotations have zero residues in distinct two-element subsets modulo five; at most one residue agrees, accounting for at most three shared zeros out of six. Hence they are mutually nonadjacent.

## Reproducibility and prior work

The determinant expansion and set-intersection proof are exact. The frozen checker can be used as a finite diagnostic of the unchanged statement; it is not needed for the infinite classification. Bertrand–Charon–Hudry–Lobstein (2004), Section 4.1, give the even-order minimum cardinality and alternating construction for radius one. The closely related odd-order papers of Gravier–Moncel–Semri (2006), Xu–Thulasiraman–Hu (2008) and Junnila–Laihonen (2012) concern optimum sizes; the extent of their orbit classifications could not be determined from the available full texts. This statement does not claim new minimum-size formulas. Its focus is the exhaustive token-jump structure of the minimum codes, including the order-fifteen isolated configurations. The separate indexed result on the minimum-code reconfiguration graphs of \(C_{11}\) (34a87656b6f7) concerns an odd length excluded here.
