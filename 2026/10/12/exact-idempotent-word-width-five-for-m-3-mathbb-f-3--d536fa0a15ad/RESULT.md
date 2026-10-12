# Exact idempotent-word width five for \(M_3(\mathbb F_3)^+\)
## Finding
Let \(J=M_3(\mathbb F_3)^+\) with Jordan product \(X\circ Y=(XY+YX)/2\), and let \(\ell_J(A)\) be the minimum length of a left-nested idempotent word representing \(A\). Then \(w(J)=5\). Exactly \(117\) matrices have \(\ell_J(A)=5\), and they are precisely the matrices similar over \(\mathbb F_3\) to \(\operatorname{diag}(1,-1,-1)\), equivalently the nonscalar involutions satisfying \(A^2=I_3\) and \(\operatorname{tr}A=2\). The complete minimum-length census is \(236,3068,12953,3308,117\) for lengths \(1,2,3,4,5\), respectively; the sole nonrepresentable matrix is \(-I_3\).

## Assumptions and scope
All matrices are over \(\mathbb F_3\). The Jordan algebra is \(J=M_3(\mathbb F_3)^+\) with normalized symmetrized product
\[
X\circ Y=\frac{1}{2}(XY+YX).
\]
Since \(2^{-1}=2\) in \(\mathbb F_3\), the verifier computes this product exactly modulo \(3\). An idempotent word means a finite left-nested product of idempotents, and \(\ell_J(A)\) is its minimum length. The claim is a complete finite statement about this specific Jordan algebra; it makes no assertion about \(M_3(\mathbb F_q)^+\) for other fields or about larger matrix sizes.

## Proof
Form a directed graph with vertex set \(M_3(\mathbb F_3)\). For every idempotent \(E\), place an edge \(X\to X\circ E\). A left-nested word of length \(m+1\) is obtained from a word of length \(m\) by exactly one such edge, so the minimum idempotent-word length of a representable matrix is exactly its breadth-first-search distance from the set of idempotents, with all idempotents assigned distance one.

There are exactly \(3^9=19\,683\) matrices. Exhaustive enumeration finds exactly \(236\) idempotents. Breadth-first closure under all \(236\) possible final idempotent factors gives successive new-distance strata of sizes
\[
236,\quad 3068,\quad 12953,\quad 3308,\quad 117.
\]
After the fifth stratum no new vertex appears. Thus \(19\,682\) matrices are representable and their maximum minimum length is \(5\). The single remaining vertex is \(-I_3\), which is consistent with the general scalar obstruction for idempotent words.

The same exhaustive computation tests every matrix in the length-five stratum and proves set equality with the nonscalar matrices satisfying
\[
A^2=I_3,\qquad \operatorname{tr}A=2.
\]
There are exactly \(117\) such matrices. For the structural identification, \(A^2=I_3\) implies that the minimal polynomial divides \((t-1)(t+1)\), which is square-free over \(\mathbb F_3\); hence \(A\) is diagonalizable. If the multiplicity of eigenvalue \(1\) is \(r\), then the trace condition forces \(r=1\). Therefore every length-five matrix is similar to \(\operatorname{diag}(1,-1,-1)\). Conversely, every matrix in that similarity class is a nonscalar trace-two involution, so the verified set equality gives length exactly \(5\). As an independent size check, the similarity class has cardinality
\[
\frac{|\operatorname{GL}_3(\mathbb F_3)|}{|\operatorname{GL}_1(\mathbb F_3)|\,|\operatorname{GL}_2(\mathbb F_3)|}
=\frac{11232}{2\cdot48}=117.
\]

## Verification
Run `python3 verify_f3_m3_jordan_words.py` with Python 3 and NumPy. The script enumerates all \(19\,683\) matrices, recomputes all idempotents, performs the complete breadth-first closure, and independently compares the length-five set with the trace-two nonscalar involution set. The archived output is in `VERIFY.txt` and ends with `width=5 length5=117 trace2_nonscalar_involutions=117` after `VERIFY_OK`.

This is exhaustive finite verification, not sampling: every matrix and every possible final idempotent factor is checked. The symbolic diagonalizability and conjugacy-class argument above explains the extremal stratum after the finite set equality has been established.

## Relationship to prior work
Gogić and Tomašević define left-nested idempotent words and their minimum length, and prove for every field of characteristic different from \(2\) that
\[
\mathscr{P}(M_n(\mathbb F)^+)=(M_n(\mathbb F)\setminus \mathbb F I_n)\cup\{0,I_n\},
\]
together with logarithmic upper and lower bounds for the width. Their Theorem 1.2 does not determine the exact width for \(n=3\). Their Proposition 4.1 gives an exact length classification only for \(2\times2\) matrices, while the later full-matrix argument supplies bounds rather than an exact \(3\times3\) finite-field census. The present result closes the first matrix size beyond that exact \(2\times2\) case over the smallest field of characteristic different from \(2\), and identifies the unique extremal similarity type.

Targeted searches for the exact field-size pair, the width-five statement, the extremal diagonal form, and trace-two involution aliases found no statement implying this census. Nearby results concerning nilpotent-free matrix spaces, binary decomposition problems, and other involution factorizations concern different operations and do not imply idempotent-word lengths in the Jordan product.

## Limitations
The result is specific to \(M_3(\mathbb F_3)^+\). It does not give a formula for \(M_3(\mathbb F_q)^+\) as \(q\) varies, nor does it improve the asymptotic bounds for general \(n\). The exact width and census rely on exhaustive finite computation, although the computation is complete and reproducible and the extremal similarity classification is proved algebraically. An equivalent small-field census may exist in unindexed or differently phrased literature; the searches performed did not reveal one.

## References
1. I. Gogić and M. Tomašević, *Idempotent words in finite-dimensional simple Jordan algebras*, arXiv:2609.23581v1, 20 September 2026. See Definition (1.1), Theorem 1.2, Lemmas 2.2--2.4, Proposition 4.1, and the full-matrix argument in Section 4.
