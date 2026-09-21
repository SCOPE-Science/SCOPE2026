# Monophonic position collapses to two in Cartesian products of twice-subdivided trees

Let \(\operatorname{mp}(G)\) denote the monophonic position number: the largest size of a vertex set no three members of which lie on a common induced path. For a tree \(T\) with at least one edge, let \(S_2(T)\) be its **twice-subdivision**, obtained by replacing every edge of \(T\) by a path of length three.

## Theorem

For any two nontrivial finite trees \(T_1,T_2\),
\[
\boxed{\operatorname{mp}\!\left(S_2(T_1)\square S_2(T_2)\right)=2.}
\]

The same local obstruction also gives the useful asymmetric corollary
\[
\boxed{\operatorname{mp}\!\left(P_m\square S_2(T)\right)=2
\qquad(m\ge 4)}
\]
for every nontrivial tree \(T\).

In particular, taking \(T_1=T_2=K_{1,d}\) gives tree factors of maximum degree \(d\) whose Cartesian product still has monophonic position number two. Thus the triangle-free upper bound
\[
\operatorname{mp}(G\square H)
\le \max\{2,\sigma(G)\Delta(H),\sigma(H)\Delta(G)\}
\]
from Chandran--Klavžar--Neethu--Tuite can have arbitrarily large slack even when both factors are trees with leaves: its right-hand side is \(d\) on this family while the exact value is 2.

## Proof

Put \(A=S_2(T_1)\) and \(B=S_2(T_2)\). Both are trees of order at least four. Suppose, for contradiction, that \(A\square B\) has a monophonic position set of size at least three, and take one of maximum size.

The proof of Theorem 3.18 in Chandran--Klavžar--Neethu--Tuite shows that for connected triangle-free factors, every maximum monophonic position set of size at least three must be layered over a leaf of one factor, and the projection onto the other factor consists of vertices that are pairwise at distance two. After exchanging the factors if necessary, write the set as
\[
M\subseteq \{x_0\}\times V(B),
\]
where \(x_0\) is a leaf of \(A\), and every two vertices of
\(Q=\pi_B(M)\) are at distance two in \(B\).

Because \(B\) is a tree and \(|Q|\ge3\), all vertices of \(Q\) have a common neighbour \(z\). Indeed, the unique length-two path between any first pair fixes its midpoint; a third vertex at distance two from both must use the same midpoint, otherwise the union of the three unique paths contains a cycle. Hence \(Q\subseteq N_B(z)\), and \(d_B(z)\ge3\).

Subdivision vertices of \(S_2(T_2)\) have degree two, so \(z\) is an original vertex of \(T_2\). Choose three distinct members \(a_1,b_1,c_1\in Q\). Along the corresponding subdivided original edges there are paths
\[
z-a_1-a_2-a_3,\qquad
z-b_1-b_2-b_3,\qquad
z-c_1-c_2-c_3.
\]
Also, every leaf of \(A=S_2(T_1)\) is an original leaf of \(T_1\), so its incident subdivided edge supplies a path
\[
x_0-x_1-x_2-x_3.
\]

Now consider the following path in \(A\square B\):
\[
\begin{aligned}
 &(x_0,a_1),(x_0,a_2),(x_1,a_2),(x_2,a_2),(x_3,a_2),\\
 &(x_3,a_1),(x_3,z),(x_3,c_1),(x_3,c_2),(x_2,c_2),\\
 &(x_2,c_3),(x_1,c_3),(x_0,c_3),(x_0,c_2),(x_0,c_1),\\
 &(x_1,c_1),(x_1,z),(x_1,b_1),(x_0,b_1).
\end{aligned}
\]
Consecutive displayed vertices are adjacent. The path is induced: within each fixed \(A\)-layer, the displayed \(B\)-coordinates form disjoint path fragments of the tree \(B\), and for each repeated \(B\)-coordinate the occurrences in different \(A\)-layers are either consecutive on the displayed path or their \(A\)-coordinates are at distance at least two. Hence no two nonconsecutive displayed vertices are adjacent.

This induced path contains the three vertices
\[
(x_0,a_1),\quad (x_0,c_1),\quad (x_0,b_1)
\]
of \(M\), contradicting monophonic position. Therefore
\(\operatorname{mp}(A\square B)\le2\). Every graph of order at least two has a monophonic position set of size two, so equality follows.

For \(P_m\square S_2(T)\) with \(m\ge4\), the same argument applies when a putative large set is layered over an endpoint of \(P_m\), using the first four path vertices as \(x_0,x_1,x_2,x_3\). If it is layered over a leaf of \(S_2(T)\), its projection onto \(P_m\) would contain at least three pairwise-distance-two vertices, impossible in a path. This proves the corollary.

## Relation to the current literature

Chandran, Klavžar, Neethu and Tuite (2026) establish the structural trichotomy for monophonic position sets in Cartesian products, the general upper bound of Theorem 3.16, Proposition 3.17 for vertices adjacent to many leaves, and the triangle-free maximum-degree upper bound in Theorem 3.18. Their full accessible article was checked for subdivision and tree specializations; the twice-subdivision family above is not stated there. Their star-by-star example shows that the maximum-degree upper bound can be tight, whereas the present theorem gives a natural tree family on which the same bound is arbitrarily non-sharp.

Targeted searches for monophonic position together with Cartesian products, trees, subdivisions, twice subdivisions, 2-subdivisions, and spiders did not locate this exact statement or an equivalent formulation. Because monophonic position is a recent parameter and the Cartesian-product article itself is very recent, originality is asserted only **to the best of our knowledge**. The main residual risk is an unindexed or differently phrased follow-up using induced-path position terminology.

## Finite verification

A compact verification script checks the explicit 19-vertex induced-path obstruction for every relevant leaf/branch-center/neighbour-triple in both factor orientations for all ordered pairs of nonisomorphic base trees of orders 2 through 6. It covers 13 base trees, 169 ordered pairs, and 1872 oriented local obstructions. This check corroborates the local construction; the theorem itself is proved above and does not depend on enumeration.

Run:

```text
python artifacts/verify_obstruction.py
```

Expected output is stored in `artifacts/expected_output.txt`.

## Limitations

- The theorem gives an exact infinite family, not a classification of all tree pairs with monophonic position number two.
- The use of exact twice-subdivision is sufficient, not claimed necessary.
- The finite verification is corroborative only.
- Originality remains subject to the residual literature risk described above.

## References

1. U. Chandran S. V., S. Klavžar, P. K. Neethu, J. Tuite, *Monophonic position sets of Cartesian and lexicographic products of graphs*, Computational and Applied Mathematics 46, 44 (2027), published online 11 September 2026. DOI: https://doi.org/10.1007/s40314-026-03901-3. Preprint: https://arxiv.org/abs/2412.09837.
2. E. J. Thomas, S. V. Ullas Chandran, J. Tuite, G. Di Stefano, *On monophonic position sets in graphs*, Discrete Applied Mathematics 354 (2024), 72--82.
