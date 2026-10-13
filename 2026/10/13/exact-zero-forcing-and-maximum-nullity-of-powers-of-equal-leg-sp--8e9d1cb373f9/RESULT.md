# Exact zero forcing and maximum nullity of powers of equal-leg spiders
## Finding
Let \(m\ge 2\), \(k\ge 1\), and \(\ell\ge k+1\). Let \(S_m(\ell)\) be the spider obtained from \(m\) disjoint paths of length \(\ell\) by joining one endpoint of each path to a new center. Then
\[
M(S_m(\ell)^k)=Z(S_m(\ell)^k)=(m-1)k.
\]
Thus Conjecture 10 of Abiad--Flagg--Ghasemi Nezhad--Zeijlemaker is true, and the same formula also gives the maximum nullity.

## Assumptions and scope
All graphs are finite, simple, and undirected. For a graph \(G\), its \(k\)-th power \(G^k\) joins distinct vertices whose distance in \(G\) is at most \(k\). The standard zero forcing number is \(Z(G)\). The maximum nullity \(M(G)\) is the largest nullity among real symmetric matrices whose nonzero off-diagonal pattern is exactly \(G\). The general inequality \(M(G)\le Z(G)\) is used.

Write the vertices on leg \(i\) as \(v_{i,1},\ldots,v_{i,\ell}\), where the second index is distance from the center. In \(S_m(\ell)^k\), two vertices on one leg are adjacent exactly when their depth difference is at most \(k\); vertices on different legs are adjacent exactly when the sum of their depths is at most \(k\); and the center is adjacent exactly to depths at most \(k\).

## Proof
Abiad--Flagg--Ghasemi Nezhad--Zeijlemaker give the upper bound
\[
Z(S_m(\ell)^k)\le (m-1)k
\]
for the stated range. It remains to prove a matching lower bound. We do this by constructing a symmetric matrix described by the graph with nullity at least \((m-1)k\).

Let \(W\) be the \(\ell\times(\ell-k)\) matrix whose column \(s\), for \(1\le s\le \ell-k\), is the indicator of the consecutive interval \(\{s,s+1,\ldots,s+k\}\). Its columns are linearly independent: reading rows from the top gives a triangular elimination in the column coefficients. Hence
\[
\operatorname{rank}W=\ell-k.
\]
Put \(D=WW^{\mathsf T}\). Then \(D_{ab}>0\) exactly when \(|a-b|\le k\), including the diagonal, so its off-diagonal support is exactly the path power \(P_\ell^k\). Moreover
\[
\operatorname{rank}D=\ell-k,
\qquad
\dim\ker D=k.
\]

Let \(C\) be the symmetric \(\ell\times\ell\) matrix defined by
\[
C_{ab}=\begin{cases}1,&a+b\le k,\\0,&a+b>k.\end{cases}
\]
and put \(B=D+C\). Since \(a+b\le k\) implies \(|a-b|\le k\), adding \(C\) cannot create a forbidden within-leg off-diagonal entry, and all required within-leg entries of \(B\) remain positive. Let \(d\in\mathbb R^\ell\) have \(d_a=1\) for \(a\le k\) and \(d_a=0\) for \(a>k\).

Order the vertices by the center followed by the \(m\) legs, and form
\[
X=
\begin{pmatrix}
0&d^{\mathsf T}&d^{\mathsf T}&\cdots&d^{\mathsf T}\\
d&B&C&\cdots&C\\
d&C&B&\cdots&C\\
\vdots&\vdots&\vdots&\ddots&\vdots\\
d&C&C&\cdots&B
\end{pmatrix}.
\]
The distance description above shows directly that \(X\) has nonzero off-diagonal entries exactly on the edges of \(S_m(\ell)^k\), so \(X\in\mathcal S(S_m(\ell)^k)\).

Let \(K=\ker D\). Consider vectors of the form
\[
(0,x_1,\ldots,x_m),
\qquad x_i\in K,
\qquad \sum_{i=1}^m x_i=0.
\]
For such a vector, the center coordinate of its image under \(X\) is \(d^{\mathsf T}\sum_i x_i=0\). On leg \(i\), the image is
\[
Bx_i+\sum_{j\ne i}Cx_j=(B-C)x_i+C\sum_jx_j=Dx_i=0.
\]
Hence this entire subspace lies in \(\ker X\). It has dimension \((m-1)\dim K=(m-1)k\), so
\[
M(S_m(\ell)^k)\ge (m-1)k.
\]
Together with \(M(G)\le Z(G)\) and the published upper bound for \(Z(S_m(\ell)^k)\), this gives
\[
(m-1)k\le M(S_m(\ell)^k)\le Z(S_m(\ell)^k)\le(m-1)k,
\]
which proves all equalities.

## Verification
The proof is symbolic and covers every integer triple \(m\ge2\), \(k\ge1\), \(\ell\ge k+1\). The included checker independently constructs the graph power from distances and the block matrix above. For a small exhaustive range it computes the zero forcing number directly from the color-change rule; for a larger range it verifies the matrix support and exact nullity by exact arithmetic.

Recorded output is:

```text
ALL CHECKS PASSED
bruteforce_profiles=18
matrix_profiles_small=18
constructive_profiles=100
small_order_limit=13
```

The finite computation is corroborative only; the arbitrary-parameter conclusion follows from the proof.

## Relationship to prior work
Abiad, Flagg, Ghasemi Nezhad, and Zeijlemaker introduced the first systematic study of zero forcing on graph powers. Their Proposition 9 proves \(Z(S_m(\ell)^k)\le(m-1)k\) for \(m\ge2\), \(k\ge1\), and \(\ell\ge k+1\). They report exhaustive equality checks for a bounded parameter range and state the equality as Conjecture 10. The theorem above supplies the missing lower bound and simultaneously identifies maximum nullity.

DeAlba, Grout, Kim, Kirkland, McDonald, and Yielding determine minimum rank for ordinary powers of paths, including \(\operatorname{mr}(P_\ell^k)=\ell-k\) in the noncomplete regime, and study strict powers of general trees. Their paper does not state the equal-leg-spider power formula proved here. The matrix \(D=WW^{\mathsf T}\) used above is a self-contained path-power certificate and the block coupling across legs is the new step.

## Limitations
The theorem is restricted to equal-leg spiders and to \(\ell\ge k+1\), exactly the range of the motivating conjecture. It does not determine unequal-leg spiders, the shorter-leg regime \(\ell\le k\), positive-semidefinite zero forcing, or zero forcing for general tree powers. The literature anchor is extremely recent, so a later revision or independently posted result may change the originality landscape. No independent audit has yet been performed.

## References
1. A. Abiad, M. Flagg, S. Ghasemi Nezhad, and S. Zeijlemaker, “The Zero Forcing Number of Graph Powers,” arXiv:2610.03892v1, first submitted 2 October 2026. Proposition 9 and Conjecture 10.
2. L. M. DeAlba, J. Grout, I.-J. Kim, S. Kirkland, J. J. McDonald, and A. Yielding, “Minimum rank of powers of trees,” Electronic Journal of Linear Algebra 23 (2012), 151–163, DOI:10.13001/1081-3810.1511.
