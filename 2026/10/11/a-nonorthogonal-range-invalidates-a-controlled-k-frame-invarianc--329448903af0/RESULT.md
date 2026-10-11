# A nonorthogonal range invalidates a controlled \(K\)-frame invariance theorem

## Finding
Theorem 3.5 of Rajput--Sahu, later published with Mishra, claims that a \(C\)-controlled \(K\)-frame remains a \(C\)-controlled \(K\)-frame after applying a closed-range operator \(T\), provided \(R(TK)\) is orthogonally complemented and \(C,K,T\) commute. The conclusion is stated on \(R(T)\).

This is false. Work in
\[
H=\mathbb C^2
\]
with
\[
C=I,\qquad
T=
\begin{pmatrix}
1&1\\
0&0
\end{pmatrix},
\qquad
K=I-T=
\begin{pmatrix}
0&-1\\
0&1
\end{pmatrix}.
\]
Let
\[
\psi=
\begin{pmatrix}
-1\\
1
\end{pmatrix}.
\]
Then
\[
T^2=T,\qquad
K^2=K,\qquad
TK=KT=0.
\]
Thus \(T\) has closed range,
\[
R(T)=\operatorname{span}\{e_1\},
\]
the operators \(C,K,T\) commute, and
\[
R(TK)=\{0\}
\]
is orthogonally complemented.

Also
\[
K^*=
\begin{pmatrix}
0&0\\
-1&1
\end{pmatrix}.
\]
For every
\[
x=(x_1,x_2)\in\mathbb C^2,
\]
one has
\[
|\langle x,\psi\rangle|^2
=
|-x_1+x_2|^2
=
\|K^*x\|^2.
\]
Hence \(\{\psi\}\) is a Parseval \(K\)-frame and therefore an \(I\)-controlled \(K\)-frame.

However,
\[
T\psi=0.
\]
Taking
\[
f=e_1\in R(T)
\]
gives
\[
K^*f=
\begin{pmatrix}
0\\
-1
\end{pmatrix}
\ne0,
\]
while
\[
|\langle f,T\psi\rangle|^2=0.
\]
No positive lower \(K\)-frame bound can therefore hold for the transformed family on \(R(T)\).

The exact obstruction is failure of \(R(T)\) to be invariant under \(K^*\).

## Assumptions and scope
The counterexample is a scalar Hilbert space, hence a Hilbert \(C^*\)-module over \(\mathbb C\). All operators are bounded and adjointable.

The example satisfies every hypothesis printed in Theorem 3.5: \(C\) is positive and invertible, \(T\) has closed range, \(R(TK)\) is orthogonally complemented, and \(C,K,T\) commute.

The repair asserted here is sufficient:
\[
K^*(R(T))\subseteq R(T).
\]
No claim is made that this is the weakest possible hypothesis in every special configuration.

## Proof
Because
\[
T=
\begin{pmatrix}
1&1\\
0&0
\end{pmatrix},
\]
direct multiplication yields
\[
T^2=T.
\]
Thus \(T\) is an idempotent with
\[
R(T)=\operatorname{span}\{e_1\}.
\]
It is not the orthogonal projection onto its range.

Define
\[
K=I-T.
\]
Then
\[
TK=T(I-T)=T-T^2=0
\]
and similarly
\[
KT=(I-T)T=T-T^2=0.
\]
Consequently \(T\) and \(K\) commute and
\[
R(TK)=\{0\}.
\]

For
\[
\psi=(-1,1),
\]
and arbitrary
\[
x=(x_1,x_2),
\]
the adjoint is
\[
K^*=
\begin{pmatrix}
0&0\\
-1&1
\end{pmatrix},
\]
so
\[
\|K^*x\|^2
=
|-x_1+x_2|^2.
\]
The single frame coefficient satisfies
\[
|\langle x,\psi\rangle|^2
=
|-x_1+x_2|^2.
\]
Thus the lower and upper \(K\)-frame inequalities both hold with constant \(1\).

On the other hand,
\[
T\psi=
\begin{pmatrix}
1&1\\
0&0
\end{pmatrix}
\begin{pmatrix}
-1\\
1
\end{pmatrix}
=0.
\]
At \(f=e_1\),
\[
\|K^*f\|^2=1
\]
but the transformed coefficient energy is \(0\). This contradicts the claimed lower frame inequality.

For the repair, recall that a closed-range adjointable operator has a Moore--Penrose inverse and
\[
TT^\dagger=P_{R(T)},
\]
the orthogonal projection onto \(R(T)\). The disputed proof step becomes legitimate if
\[
K^*C^{1/2}f\in R(T)
\qquad
\text{for every }f\in R(T).
\]
The existing relation \(TC=CT\) implies, by functional calculus for the positive operator \(C\),
\[
TC^{1/2}=C^{1/2}T.
\]
Hence \(C^{1/2}\) preserves \(R(T)\). If additionally
\[
K^*(R(T))\subseteq R(T),
\]
then \(K^*C^{1/2}f\in R(T)\), and therefore
\[
(TT^\dagger)^*K^*C^{1/2}f
=
K^*C^{1/2}f.
\]
This is exactly the missing identity needed for the published lower-bound argument.

## Verification
The first public preprint and the published full text were inspected at the complete statement and proof of Theorem 3.5.

The published proof states that \(TT^\dagger\) acts as the identity on \(R(T)\), then immediately applies it to the vector
\[
K^*C^{1/2}f.
\]
The hypotheses ensure \(f\in R(T)\) when the conclusion is tested, but they do not ensure that \(K^*C^{1/2}f\in R(T)\).

For the explicit matrix \(T\), the Moore--Penrose inverse is
\[
T^\dagger=
\begin{pmatrix}
1/2&0\\
1/2&0
\end{pmatrix},
\]
and therefore
\[
TT^\dagger=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix}
=
P_{R(T)}.
\]
At \(f=e_1\),
\[
K^*f=(0,-1)\in R(T)^\perp,
\]
so
\[
(TT^\dagger)^*K^*f=0
\]
although
\[
K^*f\ne0.
\]
This verifies the precise failure of the proof step.

No numerical approximation, finite search, or asymptotic inference is used.

## Relationship to prior work
The same source contains a separate invariance theorem for an isometry. A distinct counterexample in the literature addresses that later theorem through the difference between an isometry and a co-isometry. That result does not imply the present finding: the current theorem assumes only closed range and fails because an oblique range is not invariant under \(K^*\).

Other close \(K\)-frame results concern compression to \(R(K)\), unbounded diagonal scaling, deletion excess, or quantitative perturbation. They do not imply this closed-range transformation obstruction.

Targeted searches for the exact source, Theorem 3.5, transformed controlled \(K\)-frames, Moore--Penrose range invariance, and \(K^*\)-invariance of \(R(T)\) did not locate an indexed correction of this theorem. The 2022 published version retains the same statement and proof step.

## Limitations
The finding corrects Theorem 3.5 only. It does not reassess the neighboring invariance or perturbation theorems.

The condition
\[
K^*(R(T))\subseteq R(T)
\]
is a direct sufficient repair for the displayed proof. A weaker condition may suffice in special cases.

An unindexed erratum, thesis remark, or informal correction may contain the same observation.

## References
1. E. Rajput and N. K. Sahu, *Controlled \(K\)-frames in Hilbert \(C^*\)-modules*, arXiv:1903.09928v1, first public version 24 March 2019.
2. E. Rajput, N. K. Sahu and V. N. Mishra, *Controlled \(K\)-frames in Hilbert \(C^*\)-modules*, Korean Journal of Mathematics 30(1) (2022), 91--107, DOI 10.11568/kjm.2022.30.1.91.
