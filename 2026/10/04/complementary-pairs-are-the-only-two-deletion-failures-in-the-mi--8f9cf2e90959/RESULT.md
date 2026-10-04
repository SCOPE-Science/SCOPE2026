# Complementary pairs are the only two-deletion failures in the middle Boolean resolving layer
## Finding
Let \(m\ge 3\), put \(n=2m\), and let
\[
R=(\mathbb F_2)^n.
\]
Identify each nonzero zero divisor with its support, so the vertices of \(\Gamma(R)\) are the nonempty proper subsets of \([n]\), with two distinct vertices adjacent exactly when their supports are disjoint. Let
\[
W_m=\{{S\subset[n]:|S|=m}\}.
\]
For distinct \(X,Y\in W_m\),
\[
W_m\setminus\{{X,Y\}}
\]
is a resolving set if and only if \(Y\ne X^c\).

Equivalently, among all pairs of landmarks in the middle support layer, the complementary pairs are exactly the pairs whose simultaneous deletion destroys resolution. In particular, \(W_m\setminus\{{X\}}\) is resolving but is not minimal: among its landmarks, the unique essential one is \(X^c\).

## Assumptions and scope
The graph is the Anderson--Livingston zero-divisor graph: its vertices are the nonzero zero divisors and distinct vertices are adjacent when their product is zero. For \((\mathbb F_2)^n\), this is the Boolean graph on the nonempty proper subsets of \([n]\), with disjointness adjacency.

The result is stated for even rank \(n=2m\ge6\). It concerns robustness of the canonical middle support layer \(W_m\) as a resolving set. It does not determine the full metric dimension, upper dimension, or fault-tolerant metric dimension of \(\Gamma(R)\).

## Proof
For a vertex \(A\subset[n]\) and a middle-layer landmark \(S\in W_m\), the distance is
\[
d(A,S)=
\begin{{cases}}
0,&A=S,\\
1,&A\cap S=\varnothing,\\
3,&A\cap S\ne\varnothing\text{{ and }}A\cup S=[n],\\
2,&\text{{otherwise}}.
\end{{cases}}
\]
The order of the second and third cases matters: when \(|A|=|S|=m\), a union equal to \([n]\) forces disjointness, so the distance is \(1\).

For distinct graph vertices \(A,B\), define the set of middle-layer distinguishers
\[
D(A,B)=\{{S\in W_m:d(A,S)\ne d(B,S)\}}.
\]
We prove the stronger separator statement
\[
|D(A,B)|=2
\quad\Longleftrightarrow\quad
A,B\in W_m\text{{ and }}B=A^c,
\]
and otherwise \(|D(A,B)|\ge3\).

First suppose \(|A|,|B|<m\). If, after interchanging the two sets if necessary, \(x\in A\setminus B\), then every \(m\)-set \(S\) that contains \(x\) and is disjoint from \(B\) satisfies \(d(A,S)=2\) and \(d(B,S)=1\). There are
\[
\binom{{2m-|B|-1}}{{m-1}}\ge m\ge3
\]
such sets.

Now suppose \(|A|,|B|>m\). Put \(C=A^c\) and \(E=B^c\), so \(|C|,|E|<m\). If \(x\in C\setminus E\), every \(m\)-set \(S\) containing \(E\) but not \(x\) has \(d(B,S)=3\) and \(d(A,S)=2\). Their number is
\[
\binom{{2m-|E|-1}}{{m-|E|}}\ge m\ge3.
\]

If \(|A|<m<|B|\), every middle \(m\)-set disjoint from \(A\) distinguishes the pair, because its distance to \(A\) is \(1\), while a set of size greater than \(m\) cannot be disjoint from an \(m\)-set. There are
\[
\binom{{2m-|A|}}m\ge m+1\ge4
\]
such landmarks.

Suppose next that \(|A|=m>|B|\). There are \(\binom{{2m-|B|}}m\) middle sets disjoint from \(B\). Every one of them distinguishes \(A\) from \(B\), except possibly \(A^c\), where both distances can be \(1\). Hence
\[
|D(A,B)|\ge \binom{{2m-|B|}}m-1\ge m\ge3.
\]
If \(|A|=m<|B|\), every middle set containing \(B^c\) has distance \(3\) from \(B\), whereas a middle vertex has distance only \(0,1\), or \(2\) from another middle vertex. Thus
\[
|D(A,B)|\ge \binom{{2m-|B^c|}}{{m-|B^c|}}\ge m+1\ge4.
\]
The cases with \(A,B\) interchanged are identical.

Finally suppose \(A,B\in W_m\). If \(B=A^c\), then the only middle landmarks that distinguish them are \(A\) and \(B\): at those two coordinates the distances are \(0\) and \(1\) in opposite order, while every other middle landmark has distance \(2\) from both. Hence
\[
D(A,A^c)=\{{A,A^c\}}.
\]
If \(B\ne A^c\), then the four distinct landmarks \(A,B,A^c,B^c\) all distinguish the pair. Thus \(|D(A,B)|\ge4\).

This proves the separator statement. Now delete distinct \(X,Y\in W_m\). If \(Y=X^c\), the two vertices \(X\) and \(X^c\) have equal distance \(2\) to every remaining landmark, so the deletion is not resolving. Conversely, if \(Y\ne X^c\) and two vertices became indistinguishable after deleting \(X,Y\), then all their middle-layer distinguishers would lie in \(\{{X,Y\}}\), contradicting the separator statement. Therefore \(W_m\setminus\{{X,Y\}}\) is resolving exactly for noncomplementary deleted pairs.

For the final assertion, deleting any single \(X\) leaves a resolving set, because every vertex pair has at least two middle-layer distinguishers. Inside \(W_m\setminus\{{X\}}\), deleting a further landmark \(Y\) destroys resolution exactly when \(Y=X^c\). Hence \(X^c\) is its unique essential landmark.

## Verification
A standalone finite replay checks the distance formula and the full two-deletion classification for all landmark pairs at \(n=6\) and \(n=8\). It also verifies directly that the only graph-vertex pairs with exactly two middle-layer distinguishers are complementary middle vertices, and checks the binomial lower bounds used in the infinite proof for \(3\le m\le30\).

Run:
`python3 artifacts/verify.py`

Expected terminal line:
`VERIFY_OK`

The finite replay is a consistency check; the theorem for all \(m\ge3\) is established by the counting argument above.

## Relationship to prior work
Redmond and Szabo proved that every support layer \(W_k\) resolves the Boolean zero-divisor graph. Their Proposition 3.1 then proves minimality of \(W_k\setminus\{{w\}}\) when \(k\ne n/2\), and explicitly excludes the central case \(k=n/2\). The exclusion is structural: in the noncentral proof the complements of two deleted landmarks leave the layer, whereas in the central layer complements remain in the same layer. The present result identifies exactly what happens at that excluded boundary: the central layer survives every two-landmark deletion except a complementary pair.

Later work on fault-tolerant metric dimension of zero-divisor graphs studies several ring families and the product of two finite fields, but does not give this \((\mathbb F_2)^{2m}\) middle-layer two-deletion classification. Work on Boolean graphs has also studied matrix and determinant structure without addressing this resolving-set robustness statement.

## Limitations
The theorem classifies deletions of exactly two landmarks from the full middle layer. It does not classify arbitrary larger deleted subsets of \(W_m\), and it does not claim an exact value for the fault-tolerant metric dimension or upper dimension of the Boolean graph.

The originality comparison is limited by the coverage of the inspected literature and search indexes; an equivalent statement could exist under different terminology or in an unindexed source.

## References
1. S. Redmond and S. Szabo, “When metric and upper dimensions differ in zero divisor graphs of commutative rings,” *Discrete Mathematics Letters* 5 (2021), 34--40. DOI: 10.47443/dml.2021.0005.
2. S. Sharma and V. K. Bhat, “Fault-tolerant metric dimension of zero-divisor graphs of commutative rings,” *AKCE International Journal of Graphs and Combinatorics* 19 (2022), 24--30. DOI: 10.1080/09728600.2021.2009746.
3. G. Sonawane, G. S. Kadu, and Y. M. Borse, “Determinantal properties of Boolean graphs using recursive approach,” *AKCE International Journal of Graphs and Combinatorics* 21 (2024), 16--22. DOI: 10.1080/09728600.2023.2240865.
