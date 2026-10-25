# Ballot-polynomial distance profiles and exact geodesic eccentricity in Hamming products

## Finding
Let \(G=\square_{i=1}^{d}K_{q_i}\), where \(d\ge1\) and every \(q_i\ge2\). For a graph geodesic \(P\), let \(S\subseteq\{1,\ldots,d\}\) be the set of coordinates changed by its edges, and write \(L=|S|\). Put \(b=|\{i:q_i=2\}|\), and \(s=|\{i\in S:q_i=2\}|\). Define the polynomial
\[
B_\ell(z)=\sum_{j=0}^{\lfloor\ell/2\rfloor}(\ell-2j+1)\left(\binom{\ell}{j}-\binom{\ell}{j-1}\right)z^j,\qquad \binom{\ell}{-1}=0.
\]
The **complete distance-to-path enumerator**, including every distance layer, is
\[
\boxed{\Phi_{G,P}(z):=\sum_{x\in V(G)}z^{\operatorname{dist}_G(x,V(P))}=\left(\prod_{i\notin S}\bigl[1+(q_i-1)z\bigr]\right)\sum_{T\subseteq S}z^{|T|}\left(\prod_{i\in T}(q_i-2)\right)B_{L-|T|}(z).}
\]
The result depends on the set of changed coordinates, but **not** on their changing order or on the endpoint symbols. The exact path eccentricity is
\[
\boxed{\operatorname{ecc}_G(P)=d-\left\lceil\frac{s}{2}\right\rceil.}
\]
Consequently, the minimum eccentricity of a geodesic is
\[
\boxed{\min_{P\text{ a geodesic}}\operatorname{ecc}_G(P)=d-\left\lceil\frac b2\right\rceil.}
\]
All minimizers are classified by their changed binary coordinates: when \(b\) is odd, all \(b\) must change; when \(b\ge2\) is even, either \(b-1\) or \(b\) must change; when \(b=0\), every geodesic minimizes. In every case, changes in nonbinary coordinates are arbitrary, and the order of all changes is arbitrary.

The number of **unoriented** optimal geodesics can also be evaluated. Let \(h=d-b\), and let \(e_t\) be the degree-\(t\) elementary symmetric polynomial in the \(h\) numbers \(q_i-1\) with \(q_i>2\), with \(e_0=1\). Put \(N=\prod_iq_i\). For \(b\ge1\), write \(\mathcal S_b=\{b\}\) if \(b\) is odd, and \(\mathcal S_b=\{b-1,b\}\) if \(b\ge2\) is even. Then
\[
\boxed{\#\{\text{unoriented optimal geodesics}\}=\frac N2\sum_{s\in\mathcal S_b}\binom bs\sum_{t=0}^{h}e_t(s+t)!.}
\]
For \(b=0\) the answer is \(N+\frac N2\sum_{t=1}^{d}e_tt!\), counting the \(N\) singleton paths separately. An unoriented geodesic is identified with its reversal, but paths having different edge sequences are distinct.

## Assumptions and scope
The graph is a finite simple undirected Cartesian product of complete graphs, with vertices represented by tuples \(x_i\in\{0,\ldots,q_i-1\}\) and adjacency defined by changing exactly one coordinate. Graph distance equals the number of differing coordinates. A geodesic is a nonempty shortest path between its endpoints; a one-vertex path is permitted. Every coordinate changed by a geodesic changes exactly once, so \(S\) and \(L\) are unambiguous. The distance from a vertex to a path is the minimum graph distance to any path vertex. All formulas apply for every admissible tuple of integers and every geodesic, without assumptions of equal alphabet sizes.

## Proof
**1. Coordinates and a universal binary-chain enumerator.** Since each edge changes precisely one coordinate and endpoint distance equals Hamming distance, a shortest path changes each differing coordinate once and no other coordinate. Fix a changing order, relabel each changed coordinate's initial symbol \(0\) and its final symbol \(1\), and relabel coordinates to put the changed ones first. If all \(L\) changed coordinates of a candidate vertex use only symbols \(0,1\), represent them as a binary word \(a=(a_1,\ldots,a_L)\). At the path vertex after \(t\) steps the initial \(t\) coordinates are \(1\) and the remainder are \(0\). With \(O\) the number of ones of \(a\), and \(W_t=\sum_{i=1}^t(2a_i-1)\) (with \(W_0=0\)), the Hamming distance is \(O-W_t\). Thus
\[
\operatorname{dist}(a,P)=O-\max_{0\le t\le L}W_t.
\]
To enumerate words at distance \(j\), put \(M=\max_tW_t\). Then \(O=M+j\). The inequalities \(M\ge0\) and \(W_L=2(M+j)-L\le M\) force \(0\le M\le L-2j\); conversely all such values are feasible. For fixed \(M=m\) and \(O=m+j\), the reflection principle counts binary walks of length \(L\) with maximum at most \(m\) as \(\binom L{m+j}-\binom L{j-1}\), and with maximum at most \(m-1\) as \(\binom L{m+j}-\binom L j\). The difference, counting exact maximum \(m\), is \(\binom L j-\binom L{j-1}\), independently of \(m\). As there are \(L-2j+1\) admissible values of \(m\), the distance polynomial for binary words is exactly \(B_L(z)\). This includes \(L=0\), where \(B_0(z)=1\).

**2. Every distance layer of the mixed product.** Fix a vertex \(x\). In each coordinate \(i\notin S\), the path has a fixed symbol. If \(x_i\) differs from that symbol, the coordinate contributes one to every distance to \(P\); otherwise it contributes zero. Summation over those symbols gives \(\prod_{i\notin S}[1+(q_i-1)z]\). For \(i\in S\), either \(x_i\) is one of the path's two endpoint symbols or it is one of exactly \(q_i-2\) other symbols. Every other symbol differs from **every** vertex of the path, and hence contributes one regardless of path position. Let \(T\) be precisely those coordinates taking other symbols. They contribute \(z^{|T|}\prod_{i\in T}(q_i-2)\). Removing their fixed contributions leaves the binary-chain problem on the remaining \(L-|T|\) positions, in their induced order, with distance enumerator \(B_{L-|T|}(z)\). Multiplication and disjoint summation over all \(T\subseteq S\) prove the polynomial identity. This proof also establishes invariance under any permutation of the changing order. It directly gives \(\Phi(1)=N\) and constant coefficient \(L+1\), as a consistency check.

**3. Exact eccentricity and optimality.** Let \(s\) changed coordinates have binary alphabets. Every coordinate outside \(S\) contributes at most one to the distance, and every changed coordinate with alphabet at least three contributes at most one. On the \(s\) binary changed coordinates, the distance to their monotone path has maximum \(\lfloor s/2\rfloor\), since \(B_s\) has positive leading coefficient in that degree. Conversely, choose in every unchanged coordinate a symbol different from the path's symbol, and in every changed nonbinary coordinate a symbol different from **both** endpoint symbols. Independently choose a binary word reaching distance \(\lfloor s/2\rfloor\) from the induced binary chain. The chosen vertex has distance \((d-L)+(L-s)+\lfloor s/2\rfloor=d-\lceil s/2\rceil\), because the first two groups contribute independent constants to **every** path-vertex distance. This constructs a farthest vertex and proves the eccentricity formula. Since any \(0\le s\le b\) may be obtained by a geodesic, minimizing \(d-\lceil s/2\rceil\) requires \(s=b\) when \(b\) is odd, \(s\in\{b-1,b\}\) when \(b\ge2\) is even, and imposes no restriction when \(b=0\). Nonbinary coordinate choices never affect eccentricity.

**4. Exact optimizer count.** For each set \(S\) of \(L\ge1\) changed coordinates, there are \(N\) ways to choose the initial vertex, \(\prod_{i\in S}(q_i-1)\) choices for its different final coordinate symbols, and \(L!\) possible coordinate-change orders. Reversing the path pairs these oriented geodesics without fixed points, so divide by two. To select exactly \(s\) binary coordinates and \(t\) nonbinary coordinates, the sum of endpoint-symbol weights is \(\binom bs e_t\), and the number of orderings is \((s+t)!\). Summing only the optimal \(s\) values yields the claimed formulas. If \(b=0\), all geodesics are optimal, and the \(N\) singleton paths, which cannot be divided by two, are counted separately. This exhausts all possibilities.

## Verification
The accompanying standalone standard-library Python program `verify.py` enumerates vertices and computes **direct** minimum Hamming distances to geodesic vertices. It compares their complete distance distributions with the closed polynomial and checks the eccentricity formula. It tested 65 binary profiles in dimensions up to ten, 1474 mixed-product coordinate-subset profiles (alphabet sizes two, three, and four), and exhaustively counted optimal unoriented geodesics for twelve small product graphs. The replay result was `VERIFY_OK binary_profiles=65 mixed_profiles=1474 exhaustive_optimal_geodesic_cases=12`. These finite comparisons detect computational errors but are not a substitute for the general reflection and coordinate-decomposition proof.

## Relationship to prior work
Babu, Jacob, Kumar, and Sandeep (2026) investigate structural parameterized complexity of the Eccentricity Shortest Path problem, which motivates this exact structured-family question. Dragan and Leitert (2016), Kučera and Suchý (2020/2021), and related general MESP studies provide algorithms and complexity bounds. The new claim concerns the exact **all-distances polynomial** for each Hamming-product geodesic, a precise eccentricity formula, and all optimizer geodesics, rather than general decision complexity. The ballot-walk reflection principle used in the proof is classical and is not itself claimed as new. Targeted comparisons identified no equivalent mixed-product theorem; this is not a proof of historical priority, and similar formulas might occur under Boolean-chain or Hamming-covering terminology.

## Limitations
The theorem concerns Cartesian products of complete graphs, not general Cartesian products. The distance polynomial counts vertices of each distance, not the finer set of closest path vertices. The path count treats different ordered intermediate-vertex sequences as different, and counts reversals once. Possible earlier literature under monotone Boolean-chain neighborhood enumerators or coding theory remains a priority risk. No independently performed audit is claimed.

## References
- Anand Babu, Ashwin Jacob, Hitendra Kumar, R. B. Sandeep (2026), *Eccentricity Shortest Path: the structural parameter landscape*, arXiv:2610.20769, https://arxiv.org/abs/2610.20769 (public 2026-10-14).
- Feodor Dragan, Arne Leitert (2016), *Minimum Eccentricity Shortest Paths in some Structured Graph Classes*, Journal of Graph Algorithms and Applications 20(2), 299–322, DOI:10.7155/jgaa.00394.
- Martin Kučera, Ondřej Suchý (2020/2021), *Minimum Eccentricity Shortest Path Problem with Respect to Structural Parameters*, arXiv:2008.07898, https://arxiv.org/abs/2008.07898.
- Feodor F. Dragan and Arne Leitert (2017), *On the minimum eccentricity shortest path problem*, Theoretical Computer Science, DOI:10.1016/j.tcs.2017.07.004.
