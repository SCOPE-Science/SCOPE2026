# Exact general-position polynomials and strict log-concavity after degree-two edge deletion

## Finding

**Theorem.** Let \(H\) be any finite simple graph on \(n\ge5\) vertices with maximum degree at most two, and let \(G=\overline H\). Let \(I(H;z)\) denote its independence polynomial. Write \(e(H)\) for its edge count, \(p(H)\) for the number of induced three-vertex paths, \(t(H)\) for its triangle count, and \(q(H)\) for its induced four-cycle count. Then the entire general-position polynomial is

\[
\psi(G;z)=I(H;z)+e(H)z^2+\bigl(p(H)+t(H)\bigr)z^3+q(H)z^4.
\]

Moreover, if \(\psi(G;z)=\sum_{j=0}^{d}a_jz^j\), then all \(a_j\) are positive and

\[
a_j^2>a_{j-1}a_{j+1}\qquad(1\le j<d).
\]

Thus these polynomials are **strictly log-concave**, hence unimodal, for all path/cycle component multisets, with no connectedness restriction on \(H\). The new polynomial is not generally real-rooted: for \(H=C_5\), its complement is again \(C_5\) and \(\psi(G;z)=1+5z+10z^2+5z^3\), which has a nonreal conjugate pair of roots. Consequently ordinary real-rootedness cannot by itself explain the claimed strict log-concavity.

## Assumptions and scope

All graphs are finite, simple, undirected. A vertex set \(S\subseteq V(G)\) is in *general position* if no member lies on any shortest path joining two other members; the empty set counts. The coefficient \(a_j\) counts general-position sets of size \(j\). The independent-set coefficient \(b_j=[z^j]I(H;z)\) counts independent \(j\)-subsets of \(H\); coefficients outside the natural degree are zero. An *induced three-vertex path* has precisely two edges. For \(\Delta(H)\le2\), an induced four-cycle is necessarily a four-cycle component. The proof applies to arbitrary disconnected \(H\), including isolated vertices and a disjoint union of triangles and paths. The lower cutoff \(n=5\) guarantees that \(\overline H\) has diameter at most two.

For explicit coefficients, decompose \(H\) as a disjoint union of paths and cycles. For a path on \(m\ge1\) vertices and a cycle on \(m\ge3\) vertices,

\[
I(P_m;z)=\sum_{j=0}^{\lfloor(m+1)/2\rfloor}\binom{m-j+1}{j}z^j,
\quad
I(C_m;z)=1+\sum_{j=1}^{\lfloor m/2\rfloor}\frac{m}{m-j}\binom{m-j}{j}z^j.
\]

Multiplying the component polynomials and applying the displayed correction therefore yields every coefficient exactly.

## Proof

**1. Diameter and structural classification.** Suppose \(uv\) is a nonedge of \(G\), hence an edge of \(H\). Each of \(u,v\) has at most two neighbors in \(H\), including each other; their closed \(H\)-neighborhoods have union of size at most four. Since \(n\ge5\), some third vertex \(w\) is adjacent in \(G\) to both \(u,v\). Hence every pair is at distance one or two in \(G\).

For a graph of diameter at most two, a subset \(S\) is in general position exactly when \(G[S]\) contains no induced three-vertex path. Indeed, such a path makes the middle member lie on a length-two geodesic in \(G\); conversely any selected vertex on a geodesic between other selected vertices is necessarily the middle vertex of an induced length-two path. The absence of an induced three-vertex path is equivalent to \(G[S]\) being a disjoint union of complete graphs, equivalently \(H[S]\) being complete multipartite.

A nonempty complete multipartite graph of maximum degree at most two is one of: an independent set (any size), an edge \(K_2\), an induced path \(P_3=K_{1,2}\), a triangle \(K_3\), or a cycle \(C_4=K_{2,2}\). To see completeness, every nontrivial partite class in a complete multipartite graph has all other vertices as neighbors; the degree bound permits at most two neighbors, giving precisely those cases. Independent sets of size zero, one, or two have no overlap with the four extra nonempty types. Counting these induced subgraphs proves the polynomial identity.

**2. Real roots of the base polynomial.** For any path or cycle, the independence polynomial is real-rooted with negative roots. One elementary derivation sets \(\lambda_{\pm}=(1\pm\sqrt{1+4z})/2\). The path and cycle recurrences yield

\[
I(P_m;z)=\frac{\lambda_+^{m+2}-\lambda_-^{m+2}}{\lambda_+-\lambda_-},
\qquad I(C_m;z)=\lambda_+^m+\lambda_-^m.
\]

The path roots are \(-1/(4\cos^2(j\pi/(m+2)))\), with \(1\le j\le\lfloor(m+1)/2\rfloor\); cycle roots are \(-1/(4\cos^2((2j-1)\pi/(2m)))\), with \(1\le j\le\lfloor m/2\rfloor\). Multiplication over the components preserves negative real-rootedness. Since the coefficients \(b_j\) are strictly positive up to the independence number, the elementary Newton inequalities give

\[
 b_j^2\ge\frac{j+1}{j}\,b_{j-1}b_{j+1}
\]

whenever the three indices occur (the usual Newton factor depending on total degree is even stronger).

**3. Uniform bounds for \(n\ge14\).** Put \(m=e(H)\), \(\delta=p(H)+t(H)\), and \(q=q(H)\). Clearly \(m\le n\), \(\delta\le n\), and \(q\le n/4\): each nontriangle vertex contributes at most one induced centered three-path, each triangle contributes only one triangle, and four-cycles are disjoint components. Elementary union bounds on independent subsets give

\[
\begin{aligned}
b_2&=\binom n2-m\ge n(n-3)/2,\\
b_3&\ge\binom n3-m(n-2)\ge n(n-2)(n-7)/6,\\
b_4&\ge\binom n4-m\binom{n-2}{2}\ge n(n-2)(n-3)(n-13)/24.
\end{aligned}
\]

The correction changes only indices two, three and four: \(a_2=b_2+m=\binom n2\), \(a_3=b_3+\delta\), \(a_4=b_4+q\), and \(a_j=b_j\) elsewhere. At index one, \(a_1^2=n^2>\binom n2=a_0a_2\). At index two, \(a_2^2>na_3=a_1a_3\), since \(a_3\le\binom n3\) and \(\binom n2^2>n\binom n3\).

At index three, Newton's inequality yields

\[
\begin{aligned}
a_3^2-a_2a_4
&\ge b_3^2-(b_2+m)(b_4+q)\\
&\ge (b_2/3-m)b_4-\binom n2q\\
&\ge\frac{n^2}{144}\bigl((n-9)(n-2)(n-3)(n-13)-18(n-1)\bigr)>0.
\end{aligned}
\]

The last strict inequality holds for every \(n\ge14\): at \(n=14\), the product is \(660>234=18(n-1)\), and the product's positive factors grow faster than the linear right side.

At index four, using \(b_4^2\ge(5/4)b_3b_5\),

\[
a_4^2-a_3a_5\ge\bigl(b_3/4-\delta\bigr)b_5>0
\]

whenever \(b_5>0\), since \(b_3\ge n(n-2)(n-7)/6>4n\ge4\delta\). If \(b_5=0\), index four is an endpoint and does not require an internal inequality. At index five, when \(b_6>0\),

\[
a_5^2-a_4a_6\ge\bigl(b_4/5-q\bigr)b_6>0,
\]

since \(b_4\ge n(n-2)(n-3)(n-13)/24>5n/4\ge5q\). If \(b_6=0\), there is no index-five internal inequality. From index six onward the neighboring coefficients are all unaltered \(b_j\), and Newton gives the strict inequalities. Positivity without gaps follows because \(I(H;z)\) has positive coefficients in every degree through its independence number and the corrections are nonnegative. For \(n\ge14\), an independent set of size at least \(\lceil n/3\rceil\) exists by proper three-coloring of the path-and-cycle components, so index five lies in the support.

**4. Finite boundary \(5\le n\le13\).** Every graph with maximum degree at most two is a disjoint union of path components \(P_j\) (including isolated \(P_1\)) and cycle components \(C_j\) for \(j\ge3\). Enumerating unordered multisets of these components gives, for \(n=5,6,7,8,9,10,11,12,13\), respectively, \(11,19,29,46,70,106,156,232,334\) distinct types. The supplied standalone verifier computes the complete exact polynomial for every type and verifies every strict log-concavity inequality using integer arithmetic. The minimum integer slack \(a_j^2-a_{j-1}a_{j+1}\), over every checked type and internal index, is respectively \(15,21,28,36,45,55,66,78,91\), all strictly positive. The executable enumeration is complete because the component-multiset recursion includes every possible path or cycle component and every partition of \(n\). This finite exhaustive result completes the proof for the nine remaining orders.

## Verification

Run \(`python3 verify.py`\) with Python 3.10 or newer; no external dependencies are required. Its final line must be \(`VERIFY_OK`\). The verifier also reconstructs the complement graph and independently tests the shortest-path definition by direct geodesic enumeration for **all 175 graph types of orders five through nine**, comparing complete cardinality distributions rather than just maxima. The 1003 finite graph types of orders five through thirteen are exhaustively checked for strict log-concavity. Selected paths, cycles and packed short-cycle combinations through order one hundred are further tested as nonexhaustive stress cases. The finite computation proves only the explicitly bounded cases; the argument in Step 3 handles all larger orders.

## Relationship to prior work

Iršič, Klavžar, Rus and Tuite introduced general-position polynomials (arXiv:2401.05696, first public 2024-01-11), determined families with unimodal coefficients, and showed that unimodality does not hold universally. Anand, Chandran, Changat, Klavžar and Thomas (arXiv:1812.08460, first public 2018-12-20) proved the relevant general-position structural characterization in diameter-two graphs and evaluated **maximum size** for complements of trees; those facts are credited as context, not claimed as new. Rather (arXiv:2603.06930, 2026) extends general-position polynomial calculations for different families. Chandran, Klavžar and Tuite's 2025–2026 survey (arXiv:2501.19385) outlines known polynomial results, including combs and some complete multipartite graphs. The assessed advance here is the **exact entire polynomial and global strict-log-concavity theorem** simultaneously for all complements of maximum-degree-two graphs, a different family from the compared graph classes.

## Limitations

The conclusion is asserted for \(n\ge5\); smaller complements can be disconnected or have different geodesic behavior. No assertion is made for the complement of a graph of degree three or larger. The strong coefficient inequalities do not imply that \(\psi\) is real-rooted, as the five-cycle illustrates. Computational verification is finite; the uniform proof uses the real-rootedness of the base independence polynomial and exact coefficient bounds. Discovery of an equivalent unindexed theorem cannot be excluded; independent mathematical and priority auditing have not been performed.

## References

1. V. Iršič, S. Klavžar, G. Rus and J. Tuite, *General Position Polynomials*, arXiv:2401.05696 (first posted 2024-01-11), https://arxiv.org/abs/2401.05696; open-access Results in Mathematics, DOI 10.1007/s00025-024-02133-3.
2. B. S. Anand, U. Chandran S. V., M. Changat, S. Klavžar and E. J. Thomas, *Characterization of general position sets and its applications to cographs and bipartite graphs*, arXiv:1812.08460 (first posted 2018-12-20), https://arxiv.org/abs/1812.08460.
3. B. A. Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930 (posted 2026-03-06), https://arxiv.org/abs/2603.06930.
4. U. Chandran S. V., S. Klavžar and J. Tuite, *The General Position Problem: A Survey*, arXiv:2501.19385, https://arxiv.org/abs/2501.19385.
