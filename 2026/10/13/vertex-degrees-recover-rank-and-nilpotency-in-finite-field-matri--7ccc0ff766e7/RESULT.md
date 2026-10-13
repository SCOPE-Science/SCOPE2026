# Vertex degrees recover rank and nilpotency in finite-field matrix nilpotent graphs

## Finding

Let \(q\) be a prime power and \(n\ge 2\). For the full matrix algebra \(M_n(\mathbb F_q)\), use the undirected nilpotent graph \(\Gamma_N\) whose vertices are all nonzero matrices and whose distinct vertices \(A,B\) are adjacent exactly when \(AB\) is nilpotent. (Equivalently \(BA\) is nilpotent.)

For a vertex \(A\), put \(r=\operatorname{rank}(A)\), and define \(\varepsilon(A)=1\) if \(A\) is nilpotent and \(\varepsilon(A)=0\) otherwise. Then
\[
\boxed{\deg_{\Gamma_N}(A)=q^{n^2-r}-1-\varepsilon(A).}
\]
In particular, graph degree alone recovers both \(\operatorname{rank}(A)\) and whether \(A\) is nilpotent. The degree values of the two types never collide.

Two extremal consequences are
\[
\Delta(\Gamma_N)=q^{n^2-1}-1,
\]
attained exactly by rank-one nonnilpotent matrices, and
\[
\delta(\Gamma_N)=q^{n^2-n}-1,
\]
attained exactly by invertible matrices.

## Assumptions and scope

The field \(\mathbb F_q\) is arbitrary finite, including non-prime finite fields, and \(n\ge 2\). The graph is simple, so a vertex is never adjacent to itself. For a full matrix algebra over a field, every nonzero matrix is a vertex: a singular matrix annihilates a nonzero matrix on the right, while an invertible matrix can be multiplied by the inverse times a fixed nonzero nilpotent matrix.

No assertion is made here for matrix rings over nonfields, for alternative definitions of nilpotent graphs, or for directed variants.

## Proof

Fix a nonzero \(A\in M_n(\mathbb F_q)\), write \(V=\mathbb F_q^n\), and put \(U=\operatorname{im}(A)\), so \(\dim U=r\). For every \(B\in\operatorname{End}(V)\), the image of \(AB\) lies in \(U\), and \(U\) is invariant under \(AB\). Relative to a decomposition \(V=U\oplus W\), the operator \(AB\) has block form
\[
AB=\begin{pmatrix}T&S\\0&0\end{pmatrix},
\qquad T=(AB)|_U.
\]
Therefore \(AB\) is nilpotent if and only if \(T\) is nilpotent.

Consider the linear map
\[
\Phi_A:\operatorname{End}(V)\longrightarrow\operatorname{End}(U),
\qquad B\longmapsto (AB)|_U.
\]
It is surjective. Indeed, choose a linear section \(s:U\to V\) of the surjection \(A:V\to U\), so \(A\circ s=\operatorname{id}_U\). Given \(T\in\operatorname{End}(U)\), define \(B|_U=s\circ T\) and extend \(B\) arbitrarily to a complement of \(U\); then \(\Phi_A(B)=T\).

Hence every fiber of \(\Phi_A\) has size \(q^{n^2-r^2}\). Fine and Herstein's finite-field nilpotent count says that \(M_r(\mathbb F_q)\) contains exactly \(q^{r^2-r}\) nilpotent matrices. Thus the number of all \(B\in M_n(\mathbb F_q)\), including \(B=0\) and possibly \(B=A\), for which \(AB\) is nilpotent equals
\[
q^{n^2-r^2}q^{r^2-r}=q^{n^2-r}.
\]
The zero matrix is always among these and is not a vertex. The matrix \(B=A\) must also be removed exactly when \(A^2\) is nilpotent. But \(A^2\) is nilpotent if and only if \(A\) is nilpotent: one implication is immediate, and the other follows from \((A^2)^m=0\Rightarrow A^{2m}=0\). This proves the displayed degree formula.

For recovery, degree values within either nilpotency type determine \(r\) from the exponent. Across types an equality would require two powers of \(q\) to differ by \(1\), which is impossible because the difference of two positive powers of \(q\) is either zero or divisible by a positive power of \(q\). Thus rank and nilpotency are both graph-theoretically visible.

Finally, a rank-one nonnilpotent matrix exists, for example \(\operatorname{diag}(1,0,\ldots,0)\), and gives the largest possible degree. An invertible matrix has rank \(n\) and cannot be nilpotent, giving degree \(q^{n^2-n}-1\). Every rank at most \(n-1\) vertex has strictly larger degree, proving the minimum statement.

## Verification

The included `verify.py` constructs the graph directly from matrix multiplication for \((n,q)=(2,2),(2,3),(3,2)\). For every nonzero matrix in these three graphs it independently computes rank, nilpotency, and the full neighborhood, then checks
\[
\deg(A)=q^{n^2-\operatorname{rank}(A)}-1-\varepsilon(A).
\]
It also verifies that all realized rank/nilpotency profiles have distinct degree values and checks the two extremal-degree formulas. The replay prints `VERIFY_OK`.

These finite computations are consistency checks only. The universal statement for every finite field is proved by the surjective restriction map and the exact Fine--Herstein count.

## Relationship to prior work

Nikmehr and Khojasteh introduced and studied this nilpotent graph and established diameter and girth results for full matrix algebras. Mahmoodi's matrix-algebra paper, classified primarily under MSC 16S50, develops vertex, connectivity, diameter, girth, independence, planarity, and graph-isomorphism results using matrix rank; the inspected Section 2 does not state a general vertex-degree formula.

Kuzmina and Maltsev's 2015 classification of finite rings with regular nilpotent graphs comes especially close. In its proof it computes the degree of \(e_{11}\) in \(M_n(\mathbb F_q)\) as \(q^{n^2-1}-1\) and compares it with \(e_{11}+e_{22}\), for which only the upper bound \(q^{n^2-2}-1\) is used. Their later Eulerian classification explicitly computes the two rank-one examples \(e_{11}\) and \(e_{12}\), giving respectively \(q^{n^2-1}-1\) and \(q^{n^2-1}-2\). The formula proved here simultaneously explains those examples, makes the rank-two bound exact, covers every rank and every similarity type, and yields the new inverse conclusion that degree recovers rank and nilpotency.

No claim is made that the nilpotent graph newly determines the field or matrix size: Mahmoodi already proved an isomorphism-recognition result for finite-field full matrix algebras.

## Limitations

The proof uses the exact count of nilpotent endomorphisms over a finite field. The formula therefore does not automatically extend to matrices over finite local rings or general Artinian coefficient rings, where the fibers and nilpotent counts have additional structure.

The literature comparison was concentrated on the founding nilpotent-graph papers, the dedicated matrix-algebra paper, the regular/Eulerian classification papers, and semantic searches for degree/rank formulations. A differently phrased older local-degree theorem could exist outside the indexed material; this remains a residual originality risk.

## References

1. M. J. Nikmehr and S. Khojasteh, *On the nilpotent graph of a ring*, Turkish Journal of Mathematics 37 (2013), 553--559, DOI 10.3906/mat-1112-35. Published online 12 June 2013.
2. A. Mahmoodi, *Nilpotent Graphs of Matrix Algebras*, Algebraic Structures and Their Applications 1(2), 123--132. The article identifies MSC(2010) Primary 16S50 and Secondary 05C12, 05C40.
3. A. S. Kuzmina and Yu. N. Maltsev, *Finite rings with regular nilpotent graphs*, Siberian Electronic Mathematical Reports 12 (2015), 810--817, DOI 10.17377/semi.2015.12.067.
4. A. S. Kuzmina and Yu. N. Maltsev, *Finite rings with Eulerian nilpotent graphs*, Siberian Electronic Mathematical Reports 14 (2017), 274--279, DOI 10.17377/SEMI.2017.14.025.
5. N. J. Fine and I. N. Herstein, *The probability that a matrix be nilpotent*, Illinois Journal of Mathematics 2 (1958), 499--504, DOI 10.1215/ijm/1255454112.
