# Exact binary rank distribution in the first odd generalized-commutator case
## Finding
Let \(M=M_3(\mathbb F_2)\). For a three-dimensional subspace \(U\le M\), choose an ordered basis \((A,B,C)\) and define
\[
L_U(X)=s_4(A,B,C,X),
\]
where \(s_4\) is the standard polynomial. This is independent of the chosen basis of \(U\): a change of basis multiplies the alternating trilinear dependence on \((A,B,C)\) by its determinant, and every element of \(\operatorname{GL}_3(\mathbb F_2)\) has determinant \(1\).

Among the
\[
\binom{9}{3}_2=788035
\]
three-dimensional subspaces of \(M\), the rank distribution is exactly
\[
\#\{U:\operatorname{rank}L_U=0\}=11635,
\]
\[
\#\{U:\operatorname{rank}L_U=2\}=122320,
\]
\[
\#\{U:\operatorname{rank}L_U=4\}=654080.
\]
No other rank occurs. Equivalently, the nullities \(9,7,5\) occur with those respective multiplicities. Thus exactly
\[
\frac{654080}{788035}=\frac{1792}{2159}
\]
of the three-spaces attain nullity \(5\), the value predicted by the characteristic-zero Dixon--Pressman formula for \((n,k)=(3,3)\).

There are exactly \(10795=\binom{8}{2}_2\) rank-zero spaces containing \(I_3\), and hence exactly \(840\) further rank-zero spaces not containing \(I_3\).

## Assumptions and scope
All matrices, subspaces, ranks and traces are over \(\mathbb F_2\). The result concerns the single boundary pair \((n,k)=(3,3)\); it is not a statement about arbitrary finite fields or larger matrix sizes. The census is over subspaces, not ordered triples: each three-space is represented once by its unique reduced-row-echelon basis in \(\mathbb F_2^9\).

## Proof
The standard polynomial is alternating over \(\mathbb F_2\) in the sense that it vanishes when two arguments coincide. Hence \(U\subseteq\ker L_U\). The identity insertion formula for even standard-polynomial degree gives \(s_4(A,B,C,I_3)=0\), so \(I_3\in\ker L_U\). If \(I_3\in U\), choosing a basis of \(U\) containing \(I_3\) gives \(L_U=0\).

For the remaining spaces, define
\[
w_U(X,Y)=\operatorname{tr}(X L_U(Y)).
\]
The trace pairing on \(M_3(\mathbb F_2)\) is nondegenerate, so \(\operatorname{rank}w_U=\operatorname{rank}L_U\). The standard cyclic-trace expansion for \(k=3\) gives
\[
\operatorname{tr}s_5(A,B,C,X,Y)=-5w_U(X,Y)=w_U(X,Y)
\]
in characteristic \(2\). Since \(s_5\) is alternating, \(w_U(X,X)=0\). An alternating bilinear form has even rank over every field, including characteristic \(2\). Since \(U+\mathbb F_2 I_3\subseteq\ker L_U\), a space not containing \(I_3\) has kernel dimension at least \(4\), while \(\operatorname{rank}L_U\) is even. Therefore only ranks \(0,2,4\) can occur.

It remains to count them. Every three-space of the nine-dimensional vector space \(M\) has a unique \(3\times9\) reduced-row-echelon basis matrix. Exhausting those representatives gives exactly \(788035\) spaces. For each representative \((A,B,C)\), the verifier constructs the nine columns of \(L_U\) on the matrix-unit basis and performs exact Gaussian elimination over \(\mathbb F_2\). The resulting counts are \(11635,122320,654080\) in ranks \(0,2,4\). The identity-containing rank-zero count is independently forced by choosing a two-space in the eight-dimensional quotient \(M/\mathbb F_2 I_3\), namely \(\binom82_2=10795\), leaving \(840\) nontrivial rank-zero spaces.

## Verification
The standalone verifier `verify_census.py` exhausts all \(788035\) reduced-row-echelon representatives twice. One implementation evaluates all \(24\) monomials of \(s_4\) directly. The second uses the independently grouped characteristic-two identity
\[
\begin{aligned}
s_4(A,B,C,X)={}&SX+XS+A X(BC+CB)+B X(AC+CA)+C X(AB+BA)\\
&+(AB+BA)XC+(AC+CA)XB+(BC+CB)XA,
\end{aligned}
\]
where \(S=s_3(A,B,C)\). The two operator matrices agree for every three-space and produce the same rank histogram. The replay also checks the Gaussian-binomial total and the count of rank-zero spaces containing \(I_3\).

## Relationship to prior work
Dixon and Pressman formulated the generalized-commutator nullity problem over real matrices and predicted nullity \(5\) for generic \((n,k)=(3,3)\). Lin, Tang and Zhao proved the odd-\(k\) conjecture over every characteristic-zero field in 2026. Their theorem is a Zariski-generic characteristic-zero statement and does not give a finite-field distribution. The present result instead gives the complete distribution over the finite Grassmannian \(\operatorname{Gr}(3,M_3(\mathbb F_2))\), including the exact proportion attaining the characteristic-zero extremal nullity and the full lower-rank exceptional mass.

## Limitations
This is an exhaustive finite-field census, not a closed formula in \(q\), \(n\), or \(k\). No structural classification of the \(840\) rank-zero spaces avoiding \(I_3\) is claimed. The literature comparison did not find a prior finite-field table with these counts, but older or differently indexed computations of standard-polynomial maps remain a residual originality risk.

## References
1. Chen Lin, Chenhao Tang, Enhan Zhao, *Generic Nullity of Generalized Commutators*, arXiv:2609.06339v1 (2026), especially Theorems 1.2--1.3 and Section 2.1.
2. John D. Dixon, Irwin S. Pressman, *Generalized commutators and a problem related to the Amitsur--Levitzki theorem*, Linear and Multilinear Algebra 66 (2018), 2199--2207, DOI 10.1080/03081087.2017.1389851.
3. Matthew Brassil, Zinovy Reichstein, *A graph-theoretic approach to a conjecture of Dixon and Pressman*, Israel Journal of Mathematics 252 (2022), 291--336, DOI 10.1007/s11856-022-2349-8.
