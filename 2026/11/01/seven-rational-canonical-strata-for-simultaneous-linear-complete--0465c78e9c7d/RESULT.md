# Seven rational-canonical strata for simultaneous linear complete mappings of two-dimensional finite vector spaces

## Finding
Let \(q\) be any prime power and let \(V=\mathbb F_q^2\), regarded as an additive group. For an ordered pair \(A_1,A_2\in\operatorname{GL}_2(\mathbb F_q)\), define the number of **linear simultaneous mates** by
\[
L_q(A_1,A_2)=\#\{B\in\operatorname{GL}_2(\mathbb F_q): A_1+B\text{ and }A_2+B\text{ are invertible}\}.
\]
These matrices define invertible \(\mathbb F_q\)-linear maps \(f\) such that \(f\), \(A_1+f\), and \(A_2+f\) are bijections. Let \(C=A_1^{-1}A_2\). Write \(e(C)\) for the number of \(C\)-invariant one-dimensional \(\mathbb F_q\)-subspaces of \(V\), and \(e_1(C)\) for the number of such lines on which \(C\) acts as the identity. Define
\[
T=q^3+q^2-q,\qquad
P_0=T,\quad P_1=q(2q-1),\quad P_2=q(q+1).
\]
**The universal formula** is
\[
\boxed{L_q(A_1,A_2)=q^4-3T+2q(q+1)+P_r-\bigl(q+1+q e_1(C)-e(C)\bigr),\quad r=\operatorname{rank}(I-C).}
\]
In particular, \(L_q\) depends only on the rational canonical type of \(C\). Its complete seven-family distribution among all \(C\in\operatorname{GL}_2(\mathbb F_q)\) is:

| Rational canonical type of \(C\) | Number of such \(C\) | \(L_q(A_1,A_1C)\) |
|---|---:|---:|
| Identity | \(1\) | \(q^4-2q^3-q^2+3q\) |
| Scalar \(\lambda I\), \(\lambda\ne0,1\) | \(q-2\) | \(q^4-3q^3+6q\) |
| Irreducible quadratic characteristic polynomial | \(q^2(q-1)^2/2\) | \(q^4-3q^3+5q-1\) |
| One nontrivial Jordan block at eigenvalue \(1\) | \(q^2-1\) | \(q^4-3q^3+q^2+2q\) |
| One nontrivial Jordan block at \(\lambda\ne0,1\) | \((q-2)(q^2-1)\) | \(q^4-3q^3+5q\) |
| Two distinct eigenvalues \(1,\lambda\), \(\lambda\ne0,1\) | \((q-2)q(q+1)\) | \(q^4-3q^3+q^2+2q+1\) |
| Two distinct eigenvalues neither equal to \(1\) | \(\binom{q-2}{2}q(q+1)\) | \(q^4-3q^3+5q+1\) |

Zero-multiplicity families are omitted for small fields. For \(q\ge5\), all seven numerical values occur and are distinct. For \(q=2\), the only mate counts are \(0,1,2\), attained by respectively \(3,2,1\) relative automorphisms \(C\). For every \(q\ge3\), **every pair admits a linear simultaneous mate**, and the sharp minimum is
\[
\boxed{\min_{A_1,A_2}L_q(A_1,A_2)=q^4-3q^3+5q-1,}
\]
attained exactly when \(C\) has irreducible quadratic characteristic polynomial.

For fixed \(A_1\), the table gives the full distribution as \(A_2\) varies. Across **all ordered pairs**, multiply every multiplicity in the middle column by \(|\operatorname{GL}_2(\mathbb F_q)|=(q^2-1)(q^2-q)\).

## Assumptions and scope
All fields are finite, with \(q\ge2\); there is no restriction on characteristic. Every matrix is \(2\times2\), invertible unless explicitly stated otherwise. The mates counted are \(\mathbb F_q\)-linear additive automorphisms, **not arbitrary permutations**. When \(q\) is nonprime, they are only a subset of automorphisms of the underlying elementary abelian prime-power group. The \(\mathbb F_q\)-linear restriction is intrinsic to the count. Similarity type refers to conjugation over \(\mathbb F_q\), not over an algebraic closure.

## Proof
**Reduction.** Set \(B=A_1X\) and \(C=A_1^{-1}A_2\). Because \(A_1\) is invertible, \(B,A_1+B,A_2+B\) are simultaneously invertible precisely when \(X,I+X,C+X\) are invertible. Conjugating \(X\) and \(C\) together preserves the condition, so only the similarity class of \(C\) matters.

**One singular translate.** Every set \(\{X:\det(X+D)=0\}\) has size
\[T=q^4-|\operatorname{GL}_2(\mathbb F_q)|=q^3+q^2-q.\]
Inclusion-exclusion for the three forbidden events \(\det X=0\), \(\det(X+I)=0\), \(\det(X+C)=0\) gives \(L=q^4-3T+P(0,I)+P(0,C)+P(I,C)-R(C)\), where \(R(C)\) denotes their triple intersection.

**Two singular translates.** If \(D\) is invertible, the change of variables \(X\mapsto D^{-1}X\) reduces \(\det X=\det(X+D)=0\) to \(\det Y=\det(Y+I)=0\). The zero matrix is excluded by the second condition. Every remaining matrix has rank one, uniquely representable as \(Y=uv^{\mathsf T}\) after choosing one representative \(u\ne0\) for each image line. The rank-one determinant identity gives \(\det(I+uv^{\mathsf T})=1+v^{\mathsf T}u\); for each of the \(q+1\) lines there are \(q\) row vectors satisfying \(v^{\mathsf T}u=-1\). Thus the intersection has size \(P_2=q(q+1)\).

If \(D\) has rank one, independent invertible row and column operations send it to \(\operatorname{diag}(1,0)\), preserving singularity of both translates. Writing \(Y=\begin{pmatrix}a&b\\c&d\end{pmatrix}\), the two determinant equations become \(ad-bc=(a+1)d-bc=0\), hence \(d=0\) and \(bc=0\). There are \(q(2q-1)=P_1\) solutions. If \(D=0\), the intersection is just one singular translate, of size \(P_0=T\).

Applying these counts to \(D=I\), \(D=C\), and \(D=C-I\), the first two differences have rank two, while the third has rank \(r\). This proves \(P(0,I)=P(0,C)=P_2\) and \(P(I,C)=P_r\).

**Triple intersection: eigenlines.** Suppose that all three determinants vanish. Since \(I+X\) is singular, \(X\ne0\), and since \(X\) is singular, \(X\) has rank one. Fix one nonzero vector \(u\) for each projective line and write \(X=uv^{\mathsf T}\). As \(C\) is invertible, the matrix determinant lemma gives the two conditions
\[
v^{\mathsf T}u=-1,\qquad v^{\mathsf T}C^{-1}u=-1.
\]
If \(u,C^{-1}u\) are linearly independent, there is exactly one such row vector \(v^{\mathsf T}\). If they are dependent, write \(C^{-1}u=\lambda u\); the equations are compatible exactly when \(\lambda=1\). In that case there are \(q\) vectors \(v\), whereas for any other eigenvalue there are zero. Therefore
\[
R(C)=(q+1-e(C))+qe_1(C)=q+1+qe_1(C)-e(C).
\]
Substitution into inclusion-exclusion proves the boxed universal formula, in every characteristic.

**Seven rational-canonical strata.** A scalar matrix \(C=I\) has \((r,e,e_1)=(0,q+1,q+1)\); a scalar \(\lambda I\) with \(\lambda\ne1\) has \((2,q+1,0)\). An irreducible quadratic has \((2,0,0)\). A nontrivial Jordan block at \(1\) has \((1,1,1)\), and one at \(\lambda\ne1\) has \((2,1,0)\). A matrix with distinct rational eigenvalues \(1,\lambda\) has \((1,2,1)\), while one with two distinct nonunit eigenvalues has \((2,2,0)\). Inserting each triple gives the right-hand column of the table.

The number of matrices of each type follows from the usual rational canonical classes: the centralizer sizes in \(\operatorname{GL}_2\) are respectively \(|\operatorname{GL}_2|\) for scalars, \(q(q-1)\) for one nontrivial Jordan block, \((q-1)^2\) for split distinct eigenvalues, and \(q^2-1\) for an irreducible quadratic. There are \((q^2-q)/2\) irreducible monic quadratics. Choosing the respective nonzero scalar eigenvalues, unordered distinct eigenvalue pairs, and dividing \(|\operatorname{GL}_2|\) by these centralizers gives the table's multiplicities; their sum is \(|\operatorname{GL}_2|\).

Finally, direct comparison of the seven polynomials shows that for \(q\ge3\) the irreducible type has the least value, which is strictly positive; for \(q=2\), the nontrivial Jordan type at \(1\) has zero mates. Distinctness of the seven expressions for \(q\ge5\) likewise follows by polynomial comparison. This completes the proof.

## Verification
The accompanying standalone `verify.py` directly enumerates every \(C\in\operatorname{GL}_2(\mathbb F_q)\) and every possible mate \(X\) for \(q=2,3,4,5\), including an independently implemented degree-two extension field at \(q=4\). It compares the brute-force counts with the derived eigenline formula and with each predicted stratum multiplicity. On execution, it prints `VERIFY_OK`.

Observed distributions, stated as mate count followed by number of relative matrices, are:

- \(q=2\): \((0,3),(1,2),(2,1)\).
- \(q=3\): \((14,18),(15,16),(16,12),(18,1),(27,1)\).
- \(q=4\): \((83,72),(84,30),(85,20),(88,17),(89,40),(124,1)\).
- \(q=5\): \((274,200),(275,72),(276,90),(280,3),(285,24),(286,90),(365,1)\).

These computations are finite checks only; the proof above establishes the result for all prime powers.

## Relationship to prior work
Loukaki introduced the simultaneous property \(\mathcal P_k\) and proved existence of mates for arbitrary finite groups when \(k<p-1\), together with stronger homocyclic existence statements. The paper's Section 2 reduces the linear homocyclic case to avoiding singular translates of matrices, using inequalities rather than an exact count; its Section 4 relates mates to common transversals and orthogonal Latin squares. It explicitly records the failure for a pair on the Klein four-group. The present result takes **that same singular-translate formulation** and computes its exact three-way intersection and its complete two-dimensional similarity-type distribution. The existence statements, matrix reduction, and Klein-group obstruction are prior work, not new here.

Classical enumeration of finite general linear groups, rank-one matrices, and rational canonical forms is used in the proof. These ingredients alone do not state the simultaneous-mate count, and the exact triple-intersection statistic requires the relative eigenline geometry. No historical exclusivity claim is made.

## Limitations
The theorem counts only **linear** mates and only **two** prescribed automorphisms acting on a two-dimensional vector space over the same finite field. It does not count nonlinear bijections, mixed-field-linear maps, arbitrary numbers of prescribed automorphisms, or higher dimensions. For \(q=2\), a zero linear count is not by itself a proof that no nonlinear mate exists; the stronger failure for the transposition example is separately established in the cited paper. An equivalent formulation in older matrix-completion, Latin-square or finite-geometry literature remains a historical-priority risk. No independent external validation is claimed.

## References
1. M. Loukaki, *A simultaneous variant of the Hall–Paige theorem and applications*, arXiv:2610.21600, version 1 publicly submitted 2026-10-15; version 2 posted 2026-10-22, https://arxiv.org/html/2610.21600v2 . Especially Definition 1, Theorem 2, Proposition 2, and Section 4.
2. M. Hall and L. J. Paige, *Complete mappings of finite groups*, Pacific Journal of Mathematics **5** (1955), 541–549.
3. A. B. Evans, *The existence of strong complete mappings*, Electronic Journal of Combinatorics **19** (2012), P34.
4. K. E. Morrison, *Integer sequences and matrices over finite fields*, Journal of Integer Sequences **9** (2006), Article 06.2.1, https://cs.uwaterloo.ca/journals/JIS/VOL9/Morrison/morrison37.pdf . Background finite-field matrix enumeration.
