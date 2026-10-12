# Independent double Roman weight enumerator of half graphs
## Finding
Let \(H_n\) be the half graph with \(n\ge2\), bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad
B=\{b_1,\ldots,b_n\},
\]
and
\[
a_i b_j\in E(H_n)\quad\Longleftrightarrow\quad i\le j.
\]

For
\[
0\le t\le n,
\]
put
\[
S_t=\{b_1,\ldots,b_t\}\cup\{a_{t+1},\ldots,a_n\}.
\]

Every independent double Roman dominating function on \(H_n\) has positive support equal to exactly one \(S_t\). Its labels are then characterized as follows.

For \(t=0\), the vertex \(a_1\) is forced to have label \(3\), every other vertex of \(A\) may independently have label \(2\) or \(3\), and every vertex of \(B\) has label \(0\).

For \(t=n\), the vertex \(b_n\) is forced to have label \(3\), every other vertex of \(B\) may independently have label \(2\) or \(3\), and every vertex of \(A\) has label \(0\).

For
\[
1\le t\le n-1,
\]
the vertices \(b_t\) and \(a_{t+1}\) are forced to have label \(3\), every other vertex of \(S_t\) may independently have label \(2\) or \(3\), and every vertex outside \(S_t\) has label \(0\).

Therefore the complete weight enumerator is
\[
\mathcal I_{dR}(H_n;z)
=
2z^{2n+1}(1+z)^{n-1}
+
(n-1)z^{2n+2}(1+z)^{n-2}.
\tag{1}
\]

In particular, the total number of independent double Roman dominating functions is
\[
\mathcal I_{dR}(H_n;1)=2^{n-2}(n+3),
\]
the independent double Roman domination number is
\[
i_{dR}(H_n)=2n+1,
\]
and there are exactly two minimum functions.

## Assumptions and scope
An independent double Roman dominating function is a map
\[
f:V(G)\to\{0,1,2,3\}
\]
such that every vertex labeled \(0\) has either a neighbor labeled \(3\) or at least two neighbors labeled \(2\), every vertex labeled \(1\) has a neighbor labeled \(2\) or \(3\), and the set of positive-labeled vertices is independent.

The polynomial
\[
\mathcal I_{dR}(G;z)
\]
counts all independent double Roman dominating functions by weight.

## Proof
Let \(f\) be an independent double Roman dominating function, and write
\[
P=\{v:f(v)>0\}.
\]

No vertex can have label \(1\). Indeed, a label-\(1\) vertex must have an adjacent vertex labeled \(2\) or \(3\), but then two adjacent vertices would both lie in the positive support \(P\), contradicting independence. Hence every positive label is \(2\) or \(3\).

Every zero-labeled vertex must have a positive neighbor, so \(P\) is an independent dominating set.

We now classify the independent dominating sets of \(H_n\). Let
\[
t=\max\{j:b_j\in P\},
\]
with \(t=0\) if \(P\cap B=\varnothing\).

If \(1\le t\le n\), independence implies that every positive vertex \(a_i\) satisfies
\[
i>t.
\]
If some \(b_j\) with \(j\le t\) were zero, then all its neighbors
\[
a_1,\ldots,a_j
\]
would be zero, so \(b_j\) would not be dominated. Thus
\[
b_1,\ldots,b_t\in P.
\]

If some \(a_i\) with \(i>t\) were zero, then every neighbor of \(a_i\) has index at least \(i>t\), while all positive \(B\)-vertices have index at most \(t\). Hence \(a_i\) would not be dominated. Therefore
\[
a_{t+1},\ldots,a_n\in P.
\]

This proves
\[
P=S_t.
\]
The endpoint cases are included: if \(P\cap B=\varnothing\), domination forces \(P=A=S_0\); if \(P\cap A=\varnothing\), domination forces \(P=B=S_n\).

Fix this support.

When \(t=0\), the zero vertex \(b_1\) has the unique neighbor \(a_1\). It cannot be defended by two label-\(2\) neighbors, so
\[
f(a_1)=3.
\]
This one defender also dominates every other zero in \(B\). Hence every other positive vertex may be labeled \(2\) or \(3\).

The case \(t=n\) is symmetric: the leaf \(a_n\) forces
\[
f(b_n)=3,
\]
and all other positive labels are freely \(2\) or \(3\).

Now let
\[
1\le t\le n-1.
\]
The zero vertex \(a_t\) has exactly one positive neighbor, namely \(b_t\). Therefore
\[
f(b_t)=3.
\]
Likewise the zero vertex \(b_{t+1}\) has exactly one positive neighbor, namely \(a_{t+1}\), so
\[
f(a_{t+1})=3.
\]
These two vertices dominate all zeros: \(b_t\) is adjacent to every zero \(a_i\) with \(i\le t\), and \(a_{t+1}\) is adjacent to every zero \(b_j\) with \(j\ge t+1\). Thus every other support vertex is free to receive label \(2\) or \(3\).

The two endpoint support families each contribute
\[
z^3(z^2+z^3)^{n-1}
=
z^{2n+1}(1+z)^{n-1},
\]
while each of the \(n-1\) interior support families contributes
\[
z^6(z^2+z^3)^{n-2}
=
z^{2n+2}(1+z)^{n-2}.
\]
Summing gives (1).

The lowest power in (1) is \(2n+1\), and its coefficient is \(2\). Substituting \(z=1\) gives the total count \(2^{n-2}(n+3)\).

## Verification
The included verifier constructs \(H_n\) directly for
\[
2\le n\le5
\]
and enumerates every map
\[
f:V(H_n)\to\{0,1,2,3\}.
\]
It tests the double Roman conditions and the independence of the positive support directly from the definition.

For every feasible function, it then compares the support and forced-label pattern with the theorem. It also compares the full weight histogram with the coefficients of (1), the minimum weight, and the number of minimum functions.

## Relationship to prior work
Independent double Roman domination was introduced in 2019 and subsequently developed through general inequalities, complexity results, and tree bounds. A full-text 2020 primary treatment states the definition, gives broad bounds relating the parameter to independent domination and independent Roman domination, and contains no half-graph, chain-graph, or Ferrers-graph occurrence in targeted searches.

The known complete-multipartite behavior is structurally different. In a complete multipartite graph, an independent positive support is confined to one part. In a half graph, nested neighborhoods instead force one of the \(n+1\) canonical cut independent sets \(S_t\), and the two boundary zeros at an interior cut force two labels \(3\). This yields an all-function formula rather than only a minimum parameter value.

A 2023 survey of double Roman domination summarizes independent double Roman domination through complexity, inequalities, and tree results; no half-graph enumeration is reported in the inspected section.

## Limitations
The theorem is restricted to half graphs with \(n\ge2\).

The exhaustive verification through \(n=5\) is corroborative only. The all-orders classification follows from the proof.

The earliest 2019 preprint establishing the parameter was available through abstract and bibliographic metadata in the accessible sources, while the detailed statement comparison used a later full-text primary paper and the survey. A differently phrased or non-indexed half-graph enumeration may still exist.

## References
1. D. A. Mojdeh, Z. Mansouri, “Independent double Roman domination in graphs,” arXiv:1904.04788v1, 9 April 2019; later published as “On the Independent Double Roman Domination in Graphs,” Bulletin of the Iranian Mathematical Society 46 (2020), DOI 10.1007/s41980-019-00300-9.
2. H. R. Maimani, M. Momeni, F. Rahimi Mahid, S. M. Sheikholeslami, “Independent double Roman domination in graphs,” AKCE International Journal of Graphs and Combinatorics 17 (2020), 905–910, DOI 10.1016/j.akcej.2020.02.001.
3. H. Abdollahzadeh Ahangar et al., “Double Roman Domination: A Survey,” Mathematics 11 (2023), 351, DOI 10.3390/math11020351.
