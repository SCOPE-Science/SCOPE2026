# All two-colour strong-majority edge colourings of binary hypercubes

## Finding
For every integer \(d\ge4\), all strong-majority edge colourings of the binary hypercube \(Q_d\) with two named colours are parametrized **bijectively** by sign vectors \(\varepsilon\in\{-1,+1\}^d\). An edge parallel to coordinate \(i\), with one endpoint \(v=(v_1,\ldots,v_d)\), is coloured red precisely when
\[
\varepsilon_i(-1)^{\sum_{j\ne i}v_j}=+1.
\]
The condition is independent of which endpoint is used. It follows that the strong-majority edge index is \(\operatorname{Maj}'(Q_d)=2\), that the number of named minimum-colour assignments is \(2^d\), and that the count after identifying a colouring with its red/blue exchange is \(2^{d-1}\).

## Assumptions and scope
All graphs are finite and simple. Vertices of \(Q_d\) are binary strings \(\{0,1\}^d\); an edge joins two strings differing in one coordinate. Two distinct edges are adjacent when they share a vertex. A strong-majority edge colouring is a map from edges to colours for which, around each edge, no colour appears on more than half of the adjacent edges [1]. Each edge of \(Q_d\) has exactly \(2(d-1)\) adjacent edges. Hence, with exactly two colours, the condition means \(d-1\) adjacent edges of each named colour. We assert the new all-colouring classification for integers \(d\ge4\), not arbitrary regular graphs or all edge-colourings with three or more colours.

## Proof
Write \(u\oplus e_i\) for the vertex obtained by toggling coordinate \(i\) of \(u\). Call a red edge sign \(+1\), and a blue edge sign \(-1\). Suppose first that \(c\) is any admissible red/blue colouring, and let \(R(v)\) be the number of incident red edges at vertex \(v\). Define the real-valued function \(f(v)=R(v)-d/2\).

For an edge \(uv\) of sign \(s(uv)\), the number of adjacent red edges is \(R(u)+R(v)-2\) if the edge is red, and \(R(u)+R(v)\) if it is blue. Because this number must be \(d-1\), in both cases
\[
f(u)+f(v)=s(uv)\in\{-1,+1\}. \tag{1}
\]
Sum (1) over the \(d\) incident edges at a vertex \(v\). The right-hand side is \(2R(v)-d=2f(v)\). The left-hand side is \((Af)(v)+df(v)\), where \(A\) is the ordinary adjacency operator of \(Q_d\). Therefore
\[
Af=-(d-2)f. \tag{2}
\]

For each coordinate subset \(T\subseteq[d]\), the Walsh character \(\chi_T(v)=(-1)^{\sum_{j\in T}v_j}\) is an eigenfunction of \(A\) with eigenvalue \(d-2|T|\): when one toggles coordinate \(i\), its value changes sign precisely if \(i\in T\). The \(2^d\) Walsh characters form an orthogonal basis of real functions on the cube, by pairing terms after toggling a coordinate in the symmetric difference of distinct subsets. Consequently, equation (2) forces \(|T|=d-1\) and hence
\[
f(v)=\sum_{i=1}^d a_i\chi_{[d]\setminus\{i\}}(v) \tag{3}
\]
for real coefficients \(a_i\). If \(u=v\oplus e_i\), every character in (3) except the one indexed by \([d]\setminus\{i\}\) changes sign between \(u\) and \(v\); that one stays constant. Thus
\[
s(uv)=f(u)+f(v)=2a_i(-1)^{\sum_{j\ne i}v_j}. \tag{4}
\]
Since every edge sign belongs to \(\{-1,+1\}\), we have \(2a_i=\varepsilon_i\in\{-1,+1\}\). This proves **necessity**, including uniqueness of the parameter vector.

Conversely, choose arbitrary signs \(\varepsilon_1,\ldots,\varepsilon_d\) and colour each direction-\(i\) edge by the sign \(\varepsilon_i(-1)^{\sum_{j\ne i}v_j}\). It is well-defined because toggling coordinate \(i\) does not affect that exponent. Fix an edge in direction \(i\). For each other direction \(j\ne i\), exactly two edges in direction \(j\) are adjacent to the fixed edge: one at each endpoint. Their signs are opposite, because the endpoints differ in coordinate \(i\), which appears in the exponent for direction \(j\). Each \(j\ne i\) therefore contributes exactly one red and one blue adjacent edge. There are \(d-1\) choices of \(j\), so the strong-majority condition holds at every edge. This proves **sufficiency**.

Different sign vectors differ on the colour of every edge in at least one chosen direction, and yield distinct assignments. There are exactly \(2^d\) vectors. Swapping red and blue replaces all \(\varepsilon_i\) by their negatives, and has no fixed colouring. Thus there are \(2^{d-1}\) exchange-orbits. Finally, a single colour cannot satisfy the half-neighbourhood constraint, because each edge has \(2(d-1)>0\) adjacent edges. The minimum number of colours is exactly two.

## Verification
The accompanying standalone `verify.py` builds cube edges and independently computes adjacent-edge colour counts. It exhaustively enumerates **all** binary edge-colour assignments in dimensions \(d=2\) and \(d=3\), finding respectively \(4\) and \(8\) valid assignments and matching precisely the prescribed sign-vector families. For each integer \(4\le d\le7\), it generates all \(2^d\) predicted assignments, checks they are distinct, and verifies the local strong-majority condition. It does not exhaustively enumerate arbitrary assignments when \(d\ge4\); the proof above supplies completeness in every dimension.

Run `python3 verify.py`. Its output is recorded in `verify_output.txt`.

## Relationship to prior work
Kalinowski, Kamyczura, Pilśniak and Woźniak [1] introduced the strong-majority edge index and proved global bounds and specific low-degree examples, not this exact high-dimensional cube classification. Antoniuk, Prorok and Salia [2] improved the general admissible-graph colour bound. Pękała and Przybyło [3] proved that three colours suffice under a minimum-degree hypothesis and discussed broader generalizations. These results do not state or imply the exact \(2^d\) two-colour enumeration for \(d\ge4\). An earlier exact correspondence between two-colour strong-majority assignments on *cubic* graphs and efficient dominating sets already covers \(Q_3\), which is explicitly excluded from the newly claimed domain. Standard Walsh diagonalization of the hypercube is used as an established tool, not claimed as new.

## Limitations
The classification is restricted to the standard binary cubes and exactly two named colours. It does not enumerate three-colour assignments or apply automatically to Cartesian products of arbitrary graphs. The search of readily accessible literature and research records cannot establish absolute priority; an equivalent unnoticed parity or spectral formulation could exist. Computational comparisons in small dimensions corroborate, but do not independently certify, the unrestricted proof. No independent mathematical audit has been performed.

## References
[1] R. Kalinowski, M. Kamyczura, M. Pilśniak, M. Woźniak, *Strong majority colorings of graphs*, arXiv:2605.23828 (first public version 22 May 2026), https://arxiv.org/abs/2605.23828.

[2] S. Antoniuk, M. Prorok, N. Salia, *Strong Majority Edge-Coloring*, arXiv:2607.00212 (first public version 30 June 2026), https://arxiv.org/abs/2607.00212.

[3] P. Pękała, J. Przybyło, *On Strong Majority Edge Colourings with Few Colours*, arXiv:2608.04122 (first public version 4 August 2026), https://arxiv.org/abs/2608.04122.
