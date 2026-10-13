# Self- and solid-location-domination of half graphs
## Finding
Let \(H_n\) be the half graph for \(n\ge3\), with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and adjacency
\[
a_i b_j\in E(H_n)\quad\Longleftrightarrow\quad i\le j.
\]

Then
\[
\gamma^{SLD}(H_n)=\gamma^{DLD}(H_n)=2n-2.
\]

The unique minimum self-locating-dominating code is
\[
V(H_n)\setminus\{a_1,b_n\}.
\]

The minimum solid-locating-dominating codes are exactly
\[
V(H_n)\setminus\{a_i,b_j\},
\]
where
\[
1\le i,j\le n
\]
and
\[
(i,j)\notin\{(1,1),(n,n)\}.
\]
Consequently, the number of minimum solid-locating-dominating codes is
\[
n^2-2.
\]

## Assumptions and scope
For a code \(C\subseteq V(G)\), define the identifying set
\[
I(C;u)=N[u]\cap C.
\]
A code is self-locating-dominating when every non-codeword \(u\) has nonempty identifying set and
\[
\bigcap_{c\in I(C;u)}N[c]=\{u\}.
\]
A code is solid-locating-dominating when for every two distinct non-codewords \(u,v\),
\[
I(C;u)\setminus I(C;v)\ne\varnothing.
\]
For connected graphs of order at least two, the latter condition also forces domination.

The theorem begins at \(n=3\). For \(H_2\), the solid parameter is still \(2\), but the self-locating parameter is \(3\), so the common formula has a genuine small-order boundary.

## Proof
We first treat solid location-domination.

Suppose two vertices
\[
a_i,a_j\notin C,
\qquad i<j.
\]
The half-graph neighborhoods are nested:
\[
N[a_j]\cap B\subseteq N[a_i]\cap B.
\]
Because neither \(a_i\) nor \(a_j\) lies in the code, this gives
\[
I(C;a_j)\subseteq I(C;a_i),
\]
which contradicts the defining solid-locating condition. Therefore at most one vertex of \(A\) can lie outside a solid-locating-dominating code. By symmetry, at most one vertex of \(B\) can lie outside it. Hence
\[
|C|\ge2n-2.
\tag{1}
\]

Now omit one vertex from each side:
\[
C=V(H_n)\setminus\{a_i,b_j\}.
\]
The only two non-codewords have identifying sets contained in opposite bipartition classes, so the two sets are automatically incomparable whenever both are nonempty. The identifying set of \(a_i\) is empty exactly in the corner case
\[
(i,j)=(n,n),
\]
because \(a_n\) has the unique neighbor \(b_n\). Symmetrically, the identifying set of \(b_j\) is empty exactly when
\[
(i,j)=(1,1),
\]
because \(b_1\) has the unique neighbor \(a_1\). Thus every other cross-part omitted pair yields a solid-locating-dominating code of size \(2n-2\). By (1), these are precisely all minimum codes, and their number is
\[
n^2-2.
\]

Every self-locating-dominating code is solid-locating-dominating, so
\[
\gamma^{SLD}(H_n)\ge2n-2.
\tag{2}
\]
We next identify forced codewords. A standard characterization says that a vertex \(u\) is forced into every self-locating-dominating code exactly when some distinct vertex \(v\) satisfies
\[
N(u)\subseteq N[v].
\]
For every \(i\ge2\),
\[
N(a_i)\subseteq N[a_{i-1}],
\]
so every \(a_i\) with \(i\ge2\) is forced. Likewise, for every \(j\le n-1\),
\[
N(b_j)\subseteq N[b_{j+1}],
\]
so every \(b_j\) with \(j\le n-1\) is forced. Therefore any self-locating code of size \(2n-2\) must be
\[
C^*=V(H_n)\setminus\{a_1,b_n\}.
\]

It remains to verify that \(C^*\) is self-locating. Its two non-codewords have identifying sets
\[
I(C^*;a_1)=\{b_1,\ldots,b_{n-1}\}
\]
and
\[
I(C^*;b_n)=\{a_2,\ldots,a_n\}.
\]
For \(n\ge3\), the nested half-graph neighborhoods give
\[
\bigcap_{k=1}^{n-1}N[b_k]=\{a_1\}
\]
and
\[
\bigcap_{k=2}^{n}N[a_k]=\{b_n\}.
\]
Hence \(C^*\) is self-locating-dominating. Together with (2), this proves the common optimum value and the uniqueness assertion.

## Verification
The included checker constructs \(H_n\) directly for
\[
2\le n\le8.
\]
It evaluates the original identifying-set definitions rather than the proof reductions. Every vertex subset is tested for both self- and solid-location-domination, and every minimum family is compared with the theorem. The \(n=2\) boundary is checked separately.

## Relationship to prior work
Self-locating-dominating and solid-locating-dominating codes were introduced in 2018 to strengthen ordinary locating-dominating codes so that multiple irregularities can be detected. The introducing paper studies rook graphs and binary Hamming spaces rather than half graphs.

A 2018 follow-up develops structural characterizations, including the forced-codeword criterion used above, as well as results for trees and Cartesian products. Its searchable text contains no half-graph or chain-graph specialization.

Published-result searches for the target code types on half and chain graphs did not reveal an equivalent theorem. The closest indexed results concern the same two code notions on complete multipartite graphs, or different locating-code notions on chain graphs. Neither implies the strict nested-neighborhood classification above.

The half graph is a canonical twin-free chain graph. The theorem shows a sharp structural separation between the two stronger locating notions despite their equal optimum cardinality: solid location-domination has \(n^2-2\) optimum codes, whereas self-location-domination has a unique optimum.

## Limitations
The statement concerns the thin half graph with one vertex per nesting level, not arbitrary chain graphs with twin classes.

The boundary graph \(H_2\) satisfies \(\gamma^{DLD}(H_2)=2\) but \(\gamma^{SLD}(H_2)=3\), so it is intentionally excluded from the common formula.

The finite exhaustive verification through \(n=8\) is corroborative only. The arbitrary-order result follows from the nested-neighborhood proof.

A differently phrased or non-indexed chain-graph treatment may exist.

## References
1. V. Junnila, T. Laihonen, T. Lehtilä, “On regular and new types of codes for location-domination,” Discrete Applied Mathematics 247 (2018), 225–241, DOI 10.1016/j.dam.2018.03.050; available online 13 April 2018.
2. V. Junnila, T. Laihonen, T. Lehtilä, M. L. Puertas, “On Stronger Types of Locating-dominating Codes,” Discrete Mathematics & Theoretical Computer Science 21(1) (2019), DOI 10.23638/DMTCS-21-1-1; arXiv:1808.06891, first submitted 21 August 2018 UTC.
