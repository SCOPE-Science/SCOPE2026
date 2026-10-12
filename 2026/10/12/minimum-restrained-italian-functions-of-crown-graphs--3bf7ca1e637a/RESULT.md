# Minimum restrained Italian functions of crown graphs
## Finding
Let
\[
\operatorname{Cr}_n=K_{n,n}-M
\]
be the crown graph for \(n\ge4\), with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad
B=\{b_1,\ldots,b_n\},
\]
where
\[
M=\{a_i b_i:1\le i\le n\}
\]
is the deleted perfect matching.

Then
\[
\gamma_{rI}(\operatorname{Cr}_n)=4.
\]

More strongly, every minimum restrained Italian dominating function is obtained from a vector
\[
z=(z_1,\ldots,z_n)\in\{0,1,2\}^n
\]
satisfying
\[
\sum_{i=1}^n z_i=2
\]
by setting
\[
f(a_i)=f(b_i)=z_i
\qquad
(1\le i\le n).
\]

Therefore the minimum functions are exactly of two types:

\[
f(a_i)=f(b_i)=2
\]
for one index \(i\), with every other label \(0\); or

\[
f(a_i)=f(b_i)=f(a_j)=f(b_j)=1
\]
for two distinct indices \(i,j\), with every other label \(0\).

Hence the exact number of minimum functions is
\[
n+\binom n2
=
\frac{n(n+1)}2.
\]

## Assumptions and scope
A restrained Italian dominating function on a graph \(G\) is a map
\[
f:V(G)\to\{0,1,2\}
\]
such that every vertex \(v\) with \(f(v)=0\) satisfies
\[
\sum_{u\in N(v)}f(u)\ge2,
\]
and the subgraph induced by the zero-labeled vertices has no isolated vertex.

The restrained Italian domination number
\[
\gamma_{rI}(G)
\]
is the minimum total weight
\[
\sum_{v\in V(G)}f(v)
\]
of such a function.

The theorem is stated for \(n\ge4\). The boundary graph \(\operatorname{Cr}_3\cong C_6\) also has restrained Italian domination number \(4\), but only the one-index label-\(2\) functions survive the restrained zero-subgraph condition.

## Proof
A known exact value for complete bipartite graphs is
\[
\gamma_{rI}(K_{m,n})=4
\qquad
(m,n\ge2).
\tag{1}
\]

Every restrained Italian dominating function on \(\operatorname{Cr}_n\) is also a restrained Italian dominating function on \(K_{n,n}\): adding the deleted matching edges can only increase the defending neighborhood sums of zero vertices, and can only add edges inside the zero-induced subgraph. Thus
\[
\gamma_{rI}(\operatorname{Cr}_n)\ge4.
\tag{2}
\]

Conversely, fix an index \(i\) and put
\[
f(a_i)=f(b_i)=2
\]
and assign \(0\) elsewhere. Every zero vertex is adjacent to the opposite-side label-\(2\) vertex because its index differs from \(i\). The zero-induced subgraph is
\[
\operatorname{Cr}_{n-1},
\]
which has no isolated vertex for \(n\ge4\). Hence
\[
\gamma_{rI}(\operatorname{Cr}_n)\le4.
\tag{3}
\]
Equations (2)--(3) prove the value.

It remains to classify all weight-\(4\) functions. Write
\[
x_i=f(a_i),\qquad y_i=f(b_i),
\]
and
\[
X=\sum_i x_i,\qquad Y=\sum_i y_i.
\]

There must be at least one zero in each bipartition class. Indeed, if every vertex of \(A\) were positive, then
\[
X\ge n\ge4,
\]
so weight \(4\) would force \(Y=0\). Then all vertices of \(B\) would be zero, and the zero-induced subgraph would contain the independent set \(B\) as isolated vertices, contradicting restrained feasibility. The same argument applies with \(A,B\) reversed.

Choose a zero vertex \(a_i\). Its neighborhood consists of all \(b_j\) except \(b_i\), so
\[
Y-y_i\ge2.
\]
In particular,
\[
Y\ge2.
\]
Similarly, a zero vertex in \(B\) gives
\[
X\ge2.
\]
Since the total weight is \(X+Y=4\), necessarily
\[
X=Y=2.
\tag{4}
\]

Now if \(x_i=0\), the defending condition for \(a_i\) gives
\[
2-y_i=Y-y_i\ge2,
\]
hence
\[
y_i=0.
\]
By symmetry,
\[
y_i=0\Longrightarrow x_i=0.
\]
Thus
\[
x_i=0\quad\Longleftrightarrow\quad y_i=0
\]
for every index \(i\).

The two sides therefore have the same positive support. Because each side has total weight \(2\), that common support has either one index labeled \(2\) on both sides, or two indices labeled \(1\) on both sides. Equivalently,
\[
x_i=y_i=z_i
\]
for a vector \(z\in\{0,1,2\}^n\) with total sum \(2\).

Conversely, every such vector gives a restrained Italian dominating function when \(n\ge4\). If the support has size one, the zero-induced graph is \(\operatorname{Cr}_{n-1}\); if it has size two, the zero-induced graph is \(\operatorname{Cr}_{n-2}\). Both have no isolated vertices in the stated range. Every zero vertex sees opposite-side total label weight \(2\), because the unmatched coordinate is also zero.

There are \(n\) one-index vectors and \(\binom n2\) two-index vectors, giving the claimed count.

## Verification
The included checker constructs \(\operatorname{Cr}_n\) directly for
\[
3\le n\le6.
\]
It exhausts every ternary labeling
\[
f:V(\operatorname{Cr}_n)\to\{0,1,2\},
\]
tests the Italian defending inequalities and the absence of isolated zero vertices, and computes all minimum functions.

For \(n=4,5,6\), the complete minimum family is compared with the theorem's identical-side vectors of side weight \(2\).

## Relationship to prior work
Restrained Italian domination was introduced in 2020, with a first public preprint dated 25 September 2020. The introducing paper proves complexity results, bounds, and structural characterizations for small and large values. Its full searchable text contains no crown-graph treatment.

A later primary note proves
\[
\gamma_{rI}(K_{m,n})=4
\]
for all \(m,n\ge2\), together with exact values for several complete multipartite families. Its full text likewise contains no crown or matching-deletion treatment.

Thus the scalar value for crowns is not obtained by substitution into a complete-multipartite theorem, because a crown graph is not complete bipartite. The proof instead uses the complete-bipartite value only as a lower bound under edge addition, then classifies every equality function directly. The classification also distinguishes the crown from \(K_{n,n}\): deletion of a perfect matching preserves the optimum value but rigidly aligns the two side label vectors.

## Limitations
The theorem treats balanced crown graphs and minimum functions only; it does not give the full restrained Italian domination polynomial.

The finite checker through \(n=6\) is corroborative only. The arbitrary-order classification follows from the weight-\(4\) proof.

A differently phrased or non-indexed crown-graph treatment may exist despite the targeted searches.

## References
1. B. Samadi, M. Alishahi, I. Masoumi, D. A. Mojdeh, “Restrained Italian domination in graphs,” arXiv:2009.12209v1, 25 September 2020; RAIRO Operations Research 55 (2021), 319–332, DOI 10.1051/ro/2021022.
2. L. Volkmann, “Remarks on the restrained Italian domination number in graphs,” Communications in Combinatorics and Optimization 8 (2023), 183–191, DOI 10.22049/CCO.2021.27471.1269; published online 13 December 2021.
