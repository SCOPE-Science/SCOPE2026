# Exact maximum size of rank-three fooling-set matrices

## Statement

Let \(\mathbb F\) be a field. A square matrix \(M\in\mathbb F^{n\times n}\) is a **fooling-set matrix** if

\[
M_{ii}\ne0\quad(1\le i\le n),\qquad M_{ij}M_{ji}=0\quad(i\ne j).
\]

Write \(f_{\mathbb F}(r)\) for the largest order of a fooling-set matrix over \(\mathbb F\) of rank at most \(r\). Then

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

Thus rank three is the first rank at which the exact extremal size depends on the characteristic. In particular, the classical rank-three, size-six fooling-set construction is optimal over every field of characteristic different from two, while the known characteristic-two size-seven construction is optimal.

A useful general by-product is

\[
\boxed{f_{\mathbb F}(r)\le 2^r-1}
\]

for every field and every \(r\ge1\). Combined with the Dietzfelbinger--Hromkovič--Schnitger inequality, this gives
\[
f_{\mathbb F}(r)\le \min\{r^2,2^r-1\}.
\]

## Tournament lemma

Given a fooling-set matrix \(M\), orient every unordered pair \(\{i,j\}\) as \(i\to j\) whenever \(M_{ij}=0\). If both opposite entries vanish, choose either orientation. This produces a tournament \(T\).

If \(T\) contains a transitive subtournament on \(r+1\) vertices, order those vertices so that all tournament edges point forward. The corresponding \((r+1)\times(r+1)\) principal submatrix of \(M\) is triangular, up to reversing the convention for upper and lower triangularity, with nonzero diagonal. Hence it has rank \(r+1\), impossible when \(\operatorname{rank}M\le r\).

Every tournament on \(2^r\) vertices contains a transitive subtournament on \(r+1\) vertices. This follows by the standard induction: a vertex has at least \(2^{r-1}\) out-neighbors or in-neighbors, and the induction hypothesis applies there. Therefore \(n<2^r\), proving \(f_{\mathbb F}(r)\le2^r-1\).

For \(r=1,2\), this gives the sharp upper bounds \(1,3\). The matrices

\[
[1]
\quad\text{and}\quad
\begin{pmatrix}
1&0&1\\
1&1&0\\
0&-1&1
\end{pmatrix}
\]

show equality; the latter has determinant zero and a unit \(2\times2\) minor over every field.

## Rank three: the seven-vertex equality case

The tournament lemma gives \(f_{\mathbb F}(3)\le7\). Suppose an order-seven rank-at-most-three fooling-set matrix exists, and let \(T\) be a tournament obtained from its zero pattern as above. Then \(T\) has no transitive subtournament of order four.

Every vertex of \(T\) has outdegree at most three: four out-neighbors would contain a transitive triple, which together with the vertex would form a transitive four. The same argument applies to indegree. Since each vertex has total degree six, every vertex has indegree and outdegree exactly three. Moreover, the three out-neighbors of each vertex form a directed 3-cycle, and so do its three in-neighbors.

For each vertex \(j\), put
\[
B_j=N^-(j).
\]
Each \(B_j\) is a triple. If \(u\to v\), write \(N^+(u)=\{v,a,b\}\). This triple is a directed 3-cycle, so exactly one of \(a,b\) is an out-neighbor of \(v\). Hence \(u\) and \(v\) have exactly one common out-neighbor. Equivalently, every unordered pair of vertices occurs in exactly one of the seven triples \(B_j\). Thus the \(B_j\) form the unique Steiner triple system on seven points, the Fano plane.

## Why seven forces characteristic two

Factor \(M=AB\) through \(\mathbb F^3\), with \(A\in\mathbb F^{7\times3}\) and \(B\in\mathbb F^{3\times7}\). Let \(p_i\) be the projective point represented by row \(i\) of \(A\), and let \(L_j=\ker(B_{*j})\) be the projective line represented by column \(j\) of \(B\).

The seven \(p_i\) are pairwise distinct: if two rows were proportional, the two corresponding opposite off-diagonal entries would both be nonzero because the two diagonal entries are nonzero. The same argument shows that the seven lines \(L_j\) are pairwise distinct.

Whenever \(i\to j\), we have \(M_{ij}=0\), hence \(p_i\in L_j\). Consequently, each Fano triple \(B_j\) is collinear on the corresponding distinct line \(L_j\). We have therefore embedded the Fano incidence pattern into the projective plane over \(\mathbb F\).

Relabel the Fano triples as
\[
123,\ 145,\ 167,\ 246,\ 257,\ 347,\ 356.
\]
The points \(p_1,p_2,p_4\) are noncollinear, so after a projective change of coordinates and diagonal rescaling we may take
\[
p_1=(1,0,0),\quad p_2=(0,1,0),\quad p_4=(0,0,1),
\]
\[
p_3=(1,1,0),\qquad p_5=(1,0,1).
\]
Since \(p_6\) lies on line \(246\), write \(p_6=(0,1,\lambda)\) with \(\lambda\ne0\). The incidences \(347\) and \(257\) force \(p_7=(1,1,1)\). The incidence \(167\) then forces \(\lambda=1\). Finally, the last required line \(356\) is collinear exactly when
\[
\det\begin{pmatrix}
1&1&0\\
1&0&1\\
0&1&1
\end{pmatrix}=-2=0.
\]
Hence \(\operatorname{char}\mathbb F=2\). Therefore every field of characteristic different from two satisfies \(f_{\mathbb F}(3)\le6\).

## Matching constructions

A rank-three fooling-set matrix of order six exists over every field. One convenient integer representative is

\[
M_6=\begin{pmatrix}
1&1&0&0&0&1\\
0&1&0&-1&-1&0\\
-1&1&1&0&-1&0\\
-1&0&1&1&0&0\\
1&0&0&1&1&1\\
0&1&1&1&0&1
\end{pmatrix}.
\]

It factors over the integers as
\[
M_6=
\begin{pmatrix}
1&1&0\\
0&1&0\\
-1&1&1\\
-1&0&1\\
1&0&0\\
0&1&1
\end{pmatrix}
\begin{pmatrix}
1&0&0&1&1&1\\
0&1&0&-1&-1&0\\
0&0&1&2&1&1
\end{pmatrix}.
\]
The leading \(3\times3\) minor of \(M_6\) is one, so its rank is exactly three over every field. This is the rank-three construction used in the communication-complexity literature by Klauck and de Wolf.

In characteristic two, the following order-seven matrix works:
\[
M_7=\begin{pmatrix}
1&1&0&1&0&1&0\\
0&1&1&1&0&0&1\\
1&0&1&0&0&1&1\\
0&0&1&1&1&1&0\\
1&1&1&0&1&0&0\\
0&1&0&0&1&1&1\\
1&0&0&1&1&0&1
\end{pmatrix}.
\]
It is a fooling-set matrix and factors as \(UV^T\) over characteristic two with
\[
U=\begin{pmatrix}
0&0&1\\0&1&0\\0&1&1\\1&0&0\\1&0&1\\1&1&0\\1&1&1
\end{pmatrix},\qquad
V=\begin{pmatrix}
0&0&1\\0&1&1\\1&1&0\\1&1&1\\1&0&0\\1&0&1\\0&1&0
\end{pmatrix}.
\]
A \(3\times3\) minor is nonzero, so the rank is exactly three. This is also the \(p=2,t=1\) specialization of the positive-characteristic construction of Friesen, Hamed, Lee and Theis.

Together with the upper bounds, these constructions prove the theorem.

## Relation to prior work and originality

Dietzfelbinger, Hromkovič and Schnitger proved the field-independent inequality \(n\le(\operatorname{rank}M)^2\). Klauck and de Wolf exhibited the order-six rank-three matrix above in their fooling-set separation for one-sided quantum communication. Friesen, Hamed, Lee and Theis later constructed characteristic-zero families of size \(\binom{r+1}{2}\) and asymptotically quadratic families in positive characteristic; their positive-characteristic family includes a rank-three, size-seven example in characteristic two.

The searches performed for exact low-rank fooling-set bounds, cross-free matchings, isolation sets, characteristic-dependent rank-three bounds, tournament formulations, and projective/Fano formulations did not locate the exact rank-three upper bound or the characteristic-two equality criterion above. A recent result of Parnas and Shraibman determines isolation-set sizes for **0/1 matrices whose ordinary real rank is small**; that is a different restriction from weighted fooling-set matrices whose entries may be chosen over an arbitrary field to minimize rank.

Accordingly, the exact formula for \(f_{\mathbb F}(3)\), the equality-to-Fano mechanism, and the general tournament bound are claimed **to the best of our knowledge**. The main residual originality risk is that the short low-rank argument may have appeared under sign-pattern, minimum-rank, cross-free-matching, or projective-incidence terminology not indexed together with fooling-set matrices.

## Reproducibility

`artifacts/verify_rank3.py` checks, using exact integer arithmetic and exact arithmetic modulo two, the rank-two example, the universal order-six factorization and unit minor, the characteristic-two order-seven factorization and rank, the fooling-set conditions, and the final Fano determinant \(-2\). `artifacts/verification_output.txt` contains the resulting verified output. The program supports the explicit constructions and coordinate calculation; the tournament/Fano upper-bound argument is symbolic and is proved above.

## Limitations

The result determines the exact extremal function only through rank three. It does not classify all extremal order-six matrices in characteristic different from two or all order-seven matrices in characteristic two. The general bound \(2^r-1\) is weaker than the classical \(r^2\) bound for sufficiently large \(r\), so its main role here is the sharp low-rank structural reduction. Originality is to the best of our knowledge rather than a claim of exhaustive bibliographic coverage.

## References

1. M. Dietzfelbinger, J. Hromkovič, G. Schnitger, *A comparison of two lower-bound methods for communication complexity*, Theoretical Computer Science 168 (1996), 39--51. https://doi.org/10.1016/S0304-3975(96)00062-X
2. H. Klauck, R. de Wolf, *Fooling One-Sided Quantum Protocols*, STACS 2013, 424--435. https://doi.org/10.4230/LIPIcs.STACS.2013.424
3. M. Friesen, A. Hamed, T. Lee, D. O. Theis, *Fooling sets and rank*, European Journal of Combinatorics 48 (2015), 143--153. https://doi.org/10.1016/j.ejc.2015.02.016
4. M. Pourmoradnasseri, D. O. Theis, *The (minimum) rank of typical fooling-set matrices*, CSR 2017. https://doi.org/10.1007/978-3-319-58747-9_24
5. M. Parnas, A. Shraibman, *A Study of the Binary and Boolean Rank of Matrices with Small Constant Real Rank*, FCT 2025 proceedings. https://doi.org/10.1007/978-3-032-04700-7_27
