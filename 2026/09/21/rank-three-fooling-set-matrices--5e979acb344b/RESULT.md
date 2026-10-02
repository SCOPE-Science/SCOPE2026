# Exact maximum size of rank-three fooling-set matrices

## Statement

Let \(\mathbb F\) be a field. A square matrix \(M\in\mathbb F^{n\times n}\) is a fooling-set matrix if
\[
M_{ii}\ne0
\]
for every \(i\), and
\[
M_{ij}M_{ji}=0
\]
for every \(i\ne j\).

If \(f_{\mathbb F}(r)\) denotes the largest order of a fooling-set matrix over \(\mathbb F\) of rank at most \(r\), then
\[
f_{\mathbb F}(1)=1,\qquad f_{\mathbb F}(2)=3,
\]
and
\[
\boxed{
f_{\mathbb F}(3)=
\begin{cases}
7,&\operatorname{char}\mathbb F=2,\\
6,&\operatorname{char}\mathbb F\ne2.
\end{cases}}
\]

More generally,
\[
\boxed{f_{\mathbb F}(r)\le 2^r-1}
\]
for every field and every \(r\ge1\).

## Tournament bound

For each unordered pair \(\{i,j\}\), orient one direction \(i\to j\) for which \(M_{ij}=0\). If both opposite entries vanish, choose either direction. If this tournament contained a transitive subtournament on \(r+1\) vertices, ordering those vertices transitively would make the corresponding principal submatrix triangular with nonzero diagonal, hence of rank \(r+1\), a contradiction.

Every tournament on \(2^r\) vertices contains a transitive subtournament on \(r+1\) vertices by the standard induction on \(r\). Therefore
\[
n<2^r.
\]

For \(r=1,2\), this gives the sharp upper bounds \(1\) and \(3\); the usual one-vertex example and a rank-two three-vertex example attain them.

## The seven-vertex equality case

Assume now that \(M\) has order seven and rank at most three. Any compatible tournament \(T\) constructed from its zero entries has no transitive subtournament of order four.

Every vertex of such a tournament has outdegree at most three: four out-neighbors contain a transitive triple, which together with the vertex would form a transitive four. The same argument applies to indegree. Since the total degree is six, every vertex has indegree and outdegree exactly three. Its three out-neighbors, and likewise its three in-neighbors, form directed 3-cycles.

A small point is essential here. No unordered pair can have both off-diagonal entries zero. Indeed, suppose \(M_{uv}=M_{vu}=0\). Reverse only the chosen orientation of \(\{u,v\}\). The reversed tournament is still compatible with the zero pattern, so it also cannot contain a transitive four. Hence it too must be 3-regular. But reversing one edge of a 3-regular tournament changes the endpoint outdegrees from \(3,3\) to \(2,4\), a contradiction.

Thus each unordered pair has exactly one zero direction. Put
\[
B_j=N^-(j).
\]
If \(u\to v\), the out-neighborhood of \(u\) is a directed 3-cycle, so \(u\) and \(v\) have exactly one common out-neighbor. Equivalently every unordered pair of vertices occurs in exactly one of the seven triples \(B_j\). Hence the \(B_j\) form the unique Steiner triple system on seven points, the Fano plane.

## Why seven forces characteristic two

Factor
\[
M=AB
\]
through \(\mathbb F^3\), with \(A\in\mathbb F^{7\times3}\) and \(B\in\mathbb F^{3\times7}\). Let \(p_i\) be the projective point represented by row \(i\) of \(A\), and let \(L_j=\ker(B_{*j})\).

The seven points are pairwise distinct, and the seven lines are pairwise distinct, because proportional rows or columns would force both members of some opposite off-diagonal pair to be nonzero.

By the no-double-zero lemma,
\[
p_i\in L_j
\quad\Longleftrightarrow\quad
M_{ij}=0
\quad\Longleftrightarrow\quad
i\to j
\]
for \(i\ne j\). Thus the incidence pattern of these seven points and seven lines is exactly the Fano plane, with no extra incidences among them.

Relabel the Fano triples as
\[
123,\ 145,\ 167,\ 246,\ 257,\ 347,\ 356.
\]
The non-block triple \(p_1,p_2,p_4\) is noncollinear: the line through any pair is already one of the Fano lines, and exact incidence excludes the third point. After a projective change of coordinates and rescaling,
\[
p_1=(1,0,0),\quad p_2=(0,1,0),\quad p_4=(0,0,1),
\]
\[
p_3=(1,1,0),\qquad p_5=(1,0,1).
\]
Write
\[
p_6=(0,1,\lambda)
\]
from the line \(246\). The incidences \(347\) and \(257\) give \(p_7=(1,1,1)\), and \(167\) forces \(\lambda=1\). The remaining incidence \(356\) requires
\[
\det
\begin{pmatrix}
1&1&0\\
1&0&1\\
0&1&1
\end{pmatrix}
=-2=0.
\]
Therefore \(\operatorname{char}\mathbb F=2\).

## Matching constructions

A rank-three fooling-set matrix of order six exists over every field. One integer example is
\[
M_6=
\begin{pmatrix}
1&1&0&0&0&1\\
0&1&0&-1&-1&0\\
-1&1&1&0&-1&0\\
-1&0&1&1&0&0\\
1&0&0&1&1&1\\
0&1&1&1&0&1
\end{pmatrix}.
\]
It admits an integer rank-three factorization and has a unit \(3\times3\) minor, so its rank is exactly three over every field.

In characteristic two, the standard seven-point construction
\[
M_7=
\begin{pmatrix}
1&1&0&1&0&1&0\\
0&1&1&1&0&0&1\\
1&0&1&0&0&1&1\\
0&0&1&1&1&1&0\\
1&1&1&0&1&0&0\\
0&1&0&0&1&1&1\\
1&0&0&1&1&0&1
\end{pmatrix}
\]
has rank exactly three. The repository verification artifact checks both constructions and the determinant \(-2\) exactly; the upper bound is proved above rather than inferred from the computation.

## Prior coverage and originality boundary

Dietzfelbinger, Hromkovič and Schnitger proved the field-independent quadratic upper bound. Klauck and de Wolf supplied the classical order-six rank-three example. Friesen, Hamed, Lee and Theis proved asymptotically quadratic constructions in positive characteristic and a characteristic-zero family of size \(\binom{r+1}{2}\); their positive-characteristic construction includes the characteristic-two rank-three lower witness.

The inspected primary literature and published-record searches did not locate the exact rank-three maximum or the characteristic-two equality obstruction. The proof above adds the seven-vertex tournament classification and exact Fano-incidence step. The no-double-zero lemma is included explicitly because it is needed to exclude extra projective incidences.

## Limitations

The theorem determines the extremal function only through rank three. It does not classify all extremal order-six or order-seven matrices. The general \(2^r-1\) tournament bound is weaker than the classical quadratic bound for sufficiently large \(r\).

## References

1. M. Dietzfelbinger, J. Hromkovič and G. Schnitger, “A comparison of two lower-bound methods for communication complexity,” *Theoretical Computer Science* 168 (1996), 39–51.
2. H. Klauck and R. de Wolf, “Fooling One-Sided Quantum Protocols,” STACS 2013, 424–435.
3. M. Friesen, A. Hamed, T. Lee and D. O. Theis, “Fooling sets and rank,” *European Journal of Combinatorics* 48 (2015), 143–153, arXiv:1208.2920.
