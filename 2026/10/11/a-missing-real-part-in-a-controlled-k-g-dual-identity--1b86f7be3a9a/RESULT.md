# A missing real part in a controlled \(K\)-\(g\)-dual identity

## Finding
Theorem 3.2 of Forughi--Osgooei--Rahimi--Javahernia asserts a complex-valued equality for the dual operators of a controlled \(K\)-\(g\)-dual pair. The equality is false over complex Hilbert spaces because its proof replaces a cross inner product by its conjugate without taking a real part.

With \(C=C'=I\), the theorem's dual operators have the form
\[
S_J
=
\sum_{i\in J}
(\Lambda_i^*\Lambda_i)^{1/2}
(\widetilde\Lambda_i^*\widetilde\Lambda_i)^{1/2},
\qquad
S_J+S_{J^c}=K.
\]

Take \(H=\mathbb C^2\), \(I=\{1,2\}\), and
\[
P_1=
\begin{pmatrix}
1&-1\\
-1&2
\end{pmatrix},
\qquad
P_2=
\begin{pmatrix}
1&-1\\
-1&3
\end{pmatrix},
\qquad
R=
\begin{pmatrix}
1&1\\
0&2
\end{pmatrix}.
\]
Set
\[
Q_1=P_1R=
\begin{pmatrix}
1&-1\\
-1&3
\end{pmatrix},
\qquad
Q_2=P_2R=
\begin{pmatrix}
1&-1\\
-1&5
\end{pmatrix},
\]
and define
\[
\Lambda_i=P_i,
\qquad
\widetilde\Lambda_i=Q_i.
\]
All four matrices are positive definite, so they are their own positive square-root factors in the theorem's formulas.

The two representation spaces coincide:
\[
(Q_1x,Q_2x)
=
(P_1Rx,P_2Rx),
\]
and \(R\) is invertible. Therefore the cross synthesis-analysis composition used in the definition of a controlled \(K\)-\(g\)-dual is well-defined. It equals
\[
T_\Lambda T_{\widetilde\Lambda}^*
=
P_1Q_1+P_2Q_2
=
K
=
\begin{pmatrix}
4&-10\\
-7&23
\end{pmatrix}.
\]

For \(J=\{1\}\),
\[
S_J=
\begin{pmatrix}
2&-4\\
-3&7
\end{pmatrix},
\qquad
S_{J^c}=
\begin{pmatrix}
2&-6\\
-4&16
\end{pmatrix}.
\]
At
\[
f=(1,i),
\]
the two sides of the claimed identity reduce to
\[
\langle S_Jf,S_{J^c}f\rangle
\quad\text{and}\quad
\langle S_{J^c}f,S_Jf\rangle.
\]
With the convention conjugate-linear in the first variable they are
\[
152-24i
\quad\text{and}\quad
152+24i,
\]
respectively. The opposite inner-product convention interchanges these values, so the equality fails either way.

The exact universal correction is
\[
\operatorname{Re}\langle S_Jf,Kf\rangle-\|S_Jf\|^2
=
\operatorname{Re}\langle S_{J^c}f,Kf\rangle-\|S_{J^c}f\|^2.
\]

## Assumptions and scope
The example uses the identity controls, which are allowed positive invertible controls. The index set is finite and all coefficient spaces are \(H\), so there are no convergence issues.

The construction also respects the paper's nonstandard representation-space definition of synthesis and analysis operators: the two relevant representation spaces are equal, not merely isomorphic.

The operator
\[
K=
\begin{pmatrix}
4&-10\\
-7&23
\end{pmatrix}
\]
is bounded and invertible. The family \(\Lambda\) is an ordinary finite-dimensional \(g\)-frame because
\[
P_1^2+P_2^2
=
\begin{pmatrix}
4&-7\\
-7&15
\end{pmatrix}
\]
is positive definite. Hence it is automatically a \(K\)-\(g\)-frame after rescaling the lower bound.

## Proof
The positive definiteness is elementary:
\[
\det P_1=1,\qquad
\det P_2=2,\qquad
\det Q_2=4,
\]
and each matrix has positive trace; moreover \(Q_1=P_2\).

The common representation-space statement follows from
\[
Q_i=P_iR
\]
for both \(i=1,2\), with \(R\) invertible. The synthesis operator of \(\Lambda\), applied to an analysis vector of \(\widetilde\Lambda\), therefore gives
\[
T_\Lambda T_{\widetilde\Lambda}^*x
=
\sum_{i=1}^2 P_iQ_i x.
\]
Direct multiplication yields
\[
P_1Q_1=
\begin{pmatrix}
2&-4\\
-3&7
\end{pmatrix},
\qquad
P_2Q_2=
\begin{pmatrix}
2&-6\\
-4&16
\end{pmatrix},
\]
and their sum is \(K\).

For \(A=S_J\) and \(B=S_{J^c}\), the theorem's left side equals
\[
\langle Af,(A+B)f\rangle-\|Af\|^2
=
\langle Af,Bf\rangle,
\]
while its right side equals
\[
\langle Bf,(A+B)f\rangle-\|Bf\|^2
=
\langle Bf,Af\rangle.
\]
These are complex conjugates, not equal in general.

At \(f=(1,i)\), exact multiplication gives
\[
\langle Af,Bf\rangle=152-24i,
\qquad
\langle Bf,Af\rangle=152+24i
\]
under the conjugate-linear-first convention.

Taking real parts repairs the identity because
\[
\operatorname{Re}\langle Af,Bf\rangle
=
\operatorname{Re}\langle Bf,Af\rangle.
\]

## Verification
The complete statement and proof of Theorem 3.2 were inspected in the published full text. The theorem is printed without a real-part operator. In its final proof step the source changes
\[
\langle Kf,S_{J^c}f\rangle
\]
into
\[
\langle S_{J^c}f,Kf\rangle
\]
without conjugating. That is valid over a real Hilbert space but not over a complex Hilbert space.

The earlier representation-space paper by the same authors was inspected for the synthesis and analysis operator definitions. It defines the analysis range from the positive square-root blocks and defines synthesis only on that representation space. The matrices above were chosen so that the two representation spaces coincide exactly, removing any typing ambiguity from the counterexample.

All matrix products and inner products are exact. No numerical approximation, finite search, or extrapolation is used.

## Relationship to prior work
The same authors' earlier controlled \(g\)-frame paper contains an analogous equality with \(S_J+S_{J^c}=I\). The 2020 theorem is a \(K\)-operator extension in which \(S_J+S_{J^c}=K\). The present counterexample uses a nonidentity, nonself-adjoint \(K\) and directly targets the extended statement.

The standard underlying identity over a complex Hilbert space is the equality of real parts of conjugate cross terms. The corrected formula therefore preserves the intended fundamental-identity structure without imposing self-adjointness on each partial dual operator.

Targeted searches using the theorem number, DOI, dual-operator notation, missing-real-part formulation, and conjugate cross-term formulation did not locate an indexed correction of Theorem 3.2.

## Limitations
The finding concerns Theorem 3.2. It does not reassess the later inequalities in the paper.

The repaired real-part identity is universal. The original complex equality can still hold for special dual pairs or vectors for which
\[
\langle S_Jf,S_{J^c}f\rangle
\]
is real.

An unindexed erratum, thesis remark, or informal correction may contain the same observation.

## References
1. M. Forughi, E. Osgooei, A. Rahimi and M. Javahernia, *Operators on controlled \(K\)-\(g\)-frames in Hilbert spaces*, Proceedings of the Institute of Mathematics and Mechanics 46(1) (2020), 102--114, DOI 10.29228/proc.21.
2. M. Forughi, E. Osgooei, A. Rahimi and M. Javahernia, *An appropriate representation space for controlled \(g\)-frames*, arXiv:1905.08962v1; Bulletin of the Iranian Mathematical Society 47 (2021), 855--868.
