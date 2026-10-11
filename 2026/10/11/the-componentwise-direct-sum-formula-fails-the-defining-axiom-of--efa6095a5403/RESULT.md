# The componentwise direct-sum formula fails the defining axiom of a 2-inner product

## Finding
Ghosh--Samanta define the direct sum \(H\oplus K\) of two \(n\)-Hilbert spaces by
\[
\langle f_1\oplus g_1,f_2\oplus g_2\mid f_3\oplus g_3,\ldots,f_n\oplus g_n\rangle
=
\langle f_1,f_2\mid f_3,\ldots,f_n\rangle_H
+
\langle g_1,g_2\mid g_3,\ldots,g_n\rangle_K.
\]
They then state a direct-sum controlled-frame theorem in this purported \(n\)-Hilbert space.

The displayed formula fails the defining nondegeneracy axiom already for \(n=2\). Let \(H\) and \(K\) be any nontrivial \(2\)-inner-product spaces, choose
\[
a\in H\setminus\{0\},\qquad b\in K\setminus\{0\},
\]
and put
\[
u=a\oplus 2b,\qquad v=a\oplus b.
\]
The vectors \(u\) and \(v\) are linearly independent. Indeed, \(u=\lambda v\) would force \(\lambda=1\) from the \(H\)-component and \(\lambda=2\) from the \(K\)-component.

Nevertheless the source's formula gives
\[
\langle u,u\mid v\rangle
=
\langle a,a\mid a\rangle_H
+
\langle 2b,2b\mid b\rangle_K
=
0.
\]
Each summand vanishes because the corresponding two component vectors are linearly dependent. A \(2\)-inner product must instead satisfy
\[
\langle x,x\mid y\rangle=0
\quad\Longleftrightarrow\quad
x,y\text{ are linearly dependent}.
\]
Thus the proposed direct-sum formula is not a \(2\)-inner product.

It follows that the construction does not define an \(n\)-Hilbert direct sum for the full stated range \(n\ge2\). In particular, the source's direct-sum controlled-frame result, Theorem 4.14 in the first public version and Theorem 16 in the published version, is not a valid theorem in the stated \(n\)-Hilbert-space category.

## Assumptions and scope
The counterexample uses only the axioms of a \(2\)-inner-product space. It does not depend on a special choice of norm, completeness, frame vectors, or control operators.

The result refutes the componentwise direct-sum construction for the universal class claimed in the source. It does not assert that no direct-sum construction of \(n\)-inner-product spaces is possible.

The natural repair described below is deliberately limited to the common Hilbert-induced \(2\)-inner-product subclass. No claim is made here that this repair extends verbatim to every abstract \(n\)-inner-product space or that the source's controlled-frame theorem remains true after replacing the ambient geometry.

## Proof
For \(n=2\), the defining nondegeneracy axiom is
\[
\langle x,x\mid z\rangle\ge0,
\qquad
\langle x,x\mid z\rangle=0
\Longleftrightarrow
x,z\text{ are linearly dependent}.
\]

Choose nonzero \(a\in H\) and \(b\in K\). With
\[
u=a\oplus2b,\qquad v=a\oplus b,
\]
suppose for contradiction that \(u=\lambda v\). Comparing first components gives
\[
a=\lambda a,
\]
hence \(\lambda=1\). Comparing second components gives
\[
2b=\lambda b,
\]
hence \(\lambda=2\). This is impossible, so \(u,v\) are linearly independent.

Apply the source's componentwise formula:
\[
\langle u,u\mid v\rangle
=
\langle a,a\mid a\rangle_H
+
\langle2b,2b\mid b\rangle_K.
\]
Because \(a,a\) are linearly dependent,
\[
\langle a,a\mid a\rangle_H=0.
\]
Because \(2b,b\) are linearly dependent,
\[
\langle2b,2b\mid b\rangle_K=0.
\]
Therefore
\[
\langle u,u\mid v\rangle=0
\]
despite linear independence of \(u,v\). This is a direct contradiction of the axiom.

For comparison, suppose \(H\) and \(K\) are ordinary real Hilbert spaces equipped with their standard Hilbert-induced \(2\)-inner products. Give \(H\oplus K\) the orthogonal direct-sum Hilbert inner product and define
\[
\langle x,y\mid z\rangle_{\oplus}
=
\langle x,y\rangle_{\oplus}\|z\|_{\oplus}^{2}
-
\langle x,z\rangle_{\oplus}\langle z,y\rangle_{\oplus}.
\]
Then
\[
\langle x,x\mid z\rangle_{\oplus}
=
\|x\|_{\oplus}^{2}\|z\|_{\oplus}^{2}
-
|\langle x,z\rangle_{\oplus}|^{2},
\]
the \(2\times2\) Gram determinant. It vanishes exactly when \(x,z\) are linearly dependent.

If
\[
x=x_H\oplus x_K,\quad
y=y_H\oplus y_K,\quad
z=z_H\oplus z_K,
\]
expansion of the canonical expression produces the source's two componentwise terms plus the cross terms
\[
\langle x_H,y_H\rangle\|z_K\|^{2}
+
\langle x_K,y_K\rangle\|z_H\|^{2}
-
\langle x_H,z_H\rangle\langle z_K,y_K\rangle
-
\langle x_K,z_K\rangle\langle z_H,y_H\rangle.
\]
Those cross terms are exactly what can detect linear independence across the two summands.

## Verification
The first public version states the defining \(n\)-inner-product axiom before introducing frames: the squared \(n\)-norm must vanish exactly on linearly dependent \(n\)-tuples. The same document later explicitly declares \(H\oplus K\) to be an \(n\)-Hilbert space under the componentwise sum formula and uses that formula in Theorem 4.14.

The 2024 published full text retains the same construction as formula (10) and the same direct-sum controlled-frame result as Theorem 16. The published proof expands the controlled-frame expression componentwise and derives its bounds from the component norms, so the proof depends essentially on the invalid ambient formula.

The witness is symbolic and exact. No finite experiment, numerical approximation, or computational search is used.

## Relationship to prior work
The standard theory of \(2\)-inner products requires the zero set of
\[
\langle x,x\mid z\rangle
\]
to coincide with linear dependence of \(x,z\). The source itself cites the classical \(2\)-inner-product literature and records this axiom in its preliminary definitions.

The ordinary orthogonal direct sum of Hilbert spaces is unproblematic at the Hilbert-inner-product level. If one then forms the canonical Hilbert-induced \(2\)-inner product, the resulting Gram determinant contains cross terms that are absent from the source's componentwise construction. This explains the failure without introducing any new frame-theoretic assumption.

Targeted searches for the exact source, direct sums of \(n\)-inner-product spaces, the componentwise formula, and the theorem's direct-sum conclusion did not locate an indexed correction that supplies these missing cross terms or resolves the displayed counterexample.

## Limitations
The finding establishes failure of the source's claimed direct-sum \(n\)-Hilbert structure because the universal construction already fails at \(n=2\). It does not classify all valid direct sums of abstract \(n\)-inner-product spaces.

The canonical Hilbert-induced \(2\)-inner-product construction repairs the ambient geometry in that subclass, but the source's direct-sum frame theorem would require a new analysis because its proof uses the invalid componentwise decomposition. No repaired frame theorem is asserted here.

An unindexed erratum, thesis remark, or informal correction may contain the same observation.

## References
1. P. Ghosh and T. K. Samanta, *Controlled frames in n-Hilbert spaces and their tensor products*, arXiv:2109.00543v1, 1 September 2021.
2. P. Ghosh and T. K. Samanta, *Controlled frames in n-Hilbert spaces and their tensor products*, Izvestiya Vysshikh Uchebnykh Zavedenii. Matematika 2024(5), 8--29, DOI 10.26907/0021-3446-2024-5-8-29.
3. P. Ghosh and T. K. Samanta, *Controlled Frames in n-Hilbert Spaces and Their Tensor Products*, Russian Mathematics 68(5) (2024), 1--19, DOI 10.3103/S1066369X24700312.
4. C. Diminnie, S. Gähler and A. White, *2-inner product spaces*, Demonstratio Mathematica 6 (1973), 525--536.
