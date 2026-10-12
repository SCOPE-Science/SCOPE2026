# Weight enumerator of total Roman \(\{2\}\)-dominating functions on cocktail party graphs
## Finding
For every integer
\[
n\ge2,
\]
let
\[
CP_n=K_{2,2,\ldots,2}=K_{2n}-nK_2
\]
be the cocktail party graph, with its \(n\) nonedges regarded as partner pairs.

Define the weight enumerator
\[
\mathcal T_n(x)=\sum_f x^{\omega(f)},
\]
where the sum runs over all total Roman \(\{2\}\)-dominating functions
\[
f:V(CP_n)\to\{0,1,2\}.
\]
Then
\[
\mathcal T_n(x)
=
(1+x+x^2)^{2n}
-1
-n\bigl((1+x+x^2)^2-1\bigr)
-2n(n-1)x^2
-4n(n-1)x^3.
\]

Consequently, the total number of feasible functions is
\[
\mathcal T_n(1)=3^{2n}-6n^2-2n-1.
\]

Also,
\[
\gamma_{t\{R2\}}(CP_n)=3,
\]
and the minimum functions are exactly the
\[
\binom{2n}{3}
\]
functions that assign label \(1\) to three vertices and label \(0\) to every other vertex.

The scalar domination number for complete multipartite graphs appears in prior work. The complete weight enumerator and the minimum-function classification are the content established here.

## Assumptions and scope
A total Roman \(\{2\}\)-dominating function is a labeling
\[
f:V(G)\to\{0,1,2\}
\]
satisfying two conditions.

First, every vertex \(v\) with
\[
f(v)=0
\]
has open-neighborhood weight at least \(2\):
\[
\sum_{u\in N(v)} f(u)\ge2.
\]

Second, the subgraph induced by the positive support
\[
S_f=\{v:f(v)>0\}
\]
has no isolated vertex.

The same invariant is also called total Italian domination. The theorem is stated for \(n\ge2\); the graph \(CP_1\) consists of two isolated vertices and is outside the usual isolated-free setting.

For each vertex \(v\), write \(v^\ast\) for its unique nonneighbor other than itself, namely its partner in the deleted perfect matching. Let
\[
W=\omega(f)=\sum_{v}f(v).
\]

## Proof
The proof has two independent structural reductions.

First, the positive-support condition is equivalent to saying that \(S_f\) meets at least two partner pairs. Indeed, if all positive vertices lie in one partner pair, then those two possible positive vertices are nonadjacent and every positive vertex is isolated in the induced support. Conversely, if the support meets two different partner pairs, every positive vertex is adjacent to every positive vertex lying in a different pair, so the induced support has no isolated vertex.

Second, if \(f(v)=0\), then \(v\) is adjacent to every vertex except itself and \(v^\ast\). Hence
\[
\sum_{u\in N(v)}f(u)=W-f(v^\ast).
\tag{1}
\]

If
\[
W\ge4,
\]
then \(f(v^\ast)\le2\), so (1) is at least \(2\). Thus, at every weight at least \(4\), the only condition is that the positive support meet at least two partner pairs.

Start from all
\[
3^{2n}
\]
labelings, recorded by
\[
(1+x+x^2)^{2n}.
\]
The labelings whose positive support is contained in at most one partner pair have enumerator
\[
1+n\bigl((1+x+x^2)^2-1\bigr).
\tag{2}
\]
The all-zero labeling contributes the initial \(1\), while every nonzero labeling supported on at most one partner pair belongs to a unique pair.

After subtracting (2), every remaining labeling already satisfies the total-support condition. By the preceding observation, all such labelings of weight at least \(4\) are valid. It remains only to identify the low-weight exceptions.

At weight \(2\), the only remaining possibility is two vertices of different partner pairs, each labeled \(1\). There are
\[
\binom{2n}{2}-n=2n(n-1)
\]
such labelings. If \(u\) is one selected vertex, then its partner \(u^\ast\) is zero and is nonadjacent to \(u\); it sees only the other selected label \(1\). Therefore its neighborhood weight is \(1\), so every such labeling is invalid. This accounts for
\[
2n(n-1)x^2.
\tag{3}
\]

At weight \(3\), the remaining label patterns are of two types.

If three vertices receive label \(1\), the labeling is always valid. Any three vertices meet at least two partner pairs, and a zero partner of one selected vertex still sees the other two selected vertices, so its neighborhood weight is \(2\).

If instead one vertex receives label \(2\) and one vertex from a different partner pair receives label \(1\), the labeling is invalid. The zero partner of the label-\(2\) vertex is nonadjacent to that label \(2\) and sees only the label \(1\). There are
\[
(2n)(2n-2)=4n(n-1)
\]
such labelings. This accounts for
\[
4n(n-1)x^3.
\tag{4}
\]

There are no further exceptions. Subtracting (2), (3), and (4) from the unrestricted labeling polynomial gives
\[
\mathcal T_n(x)
=
(1+x+x^2)^{2n}
-1
-n\bigl((1+x+x^2)^2-1\bigr)
-2n(n-1)x^2
-4n(n-1)x^3.
\]

The first nonzero coefficient occurs at weight \(3\), and the feasible weight-\(3\) labelings are exactly the all-\(1\) labelings on three vertices. Hence
\[
\gamma_{t\{R2\}}(CP_n)=3
\]
and the number of minimum functions is
\[
\binom{2n}{3}.
\]

Finally, setting \(x=1\) gives
\[
\mathcal T_n(1)
=
3^{2n}-1-8n-6n(n-1)
=
3^{2n}-6n^2-2n-1.
\]

## Verification
The included checker constructs \(CP_n\) directly from its deleted perfect matching and tests the two defining conditions for every labeling
\[
f:V(CP_n)\to\{0,1,2\}
\]
for
\[
2\le n\le5.
\]

For each tested order it compares every coefficient of the exhaustive weight distribution with the stated closed polynomial, and it separately checks the minimum weight and the complete minimum-function family.

## Relationship to prior work
Total Roman \(\{2\}\)-domination was introduced in 2019. The foundational source gives the defining conditions, general inequalities, complexity results, and exact results for several standard graph families. Its accessible full text contains no occurrence of “cocktail” or “multipartite.”

The same parameter is also called total Italian domination in the later \(w\)-domination framework, where it is identified with the \((2,1,1)\)-domination parameter.

A 2021 reinforcement paper records the total Roman \(\{2\}\)-domination number of complete multipartite graphs as a prior proposition before studying reinforcement. Thus the scalar value for \(CP_n\) is not treated here as new. That paper studies reinforcement numbers and does not provide the all-function weight enumerator above.

The closest enumerative results for complete multipartite graphs concern neighboring but different invariants, including ordinary Roman \(\{2\}\)-domination and total Roman domination. Neither one implies the total Roman \(\{2\}\) support-and-defense classification used here.

## Limitations
The theorem specializes to the balanced complete multipartite family in which every part has size \(2\). It does not give the corresponding all-function enumerator for arbitrary complete multipartite part sizes.

The finite exhaustive computation through \(n=5\) is corroborative only. The arbitrary-order polynomial follows from the structural support classification and the identity
\[
\sum_{u\in N(v)}f(u)=W-f(v^\ast).
\]

The scalar minimum is not an originality claim because complete-multipartite total Roman \(\{2\}\)-domination numbers appear in prior literature.

A differently phrased or non-indexed full enumerator may exist despite the targeted searches.

## References
1. S. Cabrera García, A. Cabrera Martínez, F. A. Hernández Mira, I. G. Yero, “Total Roman \(\{2\}\)-domination in graphs,” Quaestiones Mathematicae 44(10) (2021), 1353–1371, DOI 10.2989/16073606.2019.1695230; published online 28 November 2019.
2. H. Abdollahzadeh Ahangar, V. Samodivkin, S. M. Sheikholeslami, “Total Roman \(\{2\}\)-Reinforcement of Graphs,” Journal of Mathematics (2021), article 5515250, DOI 10.1155/2021/5515250.
3. A. Cabrera Martínez, A. Estrada-Moreno, J. A. Rodríguez-Velázquez, “From Italian domination in lexicographic product graphs to \(w\)-domination in graphs,” Discussiones Mathematicae Graph Theory 42 (2022), 407–425, arXiv:2011.05371.
