# A quartic Schatten metric on qubit trace slices and a minimal cone obstruction

## Finding

For positive semidefinite complex matrices of any fixed size, let the *quartic Schatten affinity distance* be
\[
D_4(A,B)=\left(\operatorname{Tr}A^4+\operatorname{Tr}B^4-2\|A^{1/2}B^{1/2}\|_4^4\right)^{1/2}.
\]
The fourth-power Schatten cross term equals \(\operatorname{Tr}(ABAB)\). For **every fixed positive trace** \(\tau>0\), the restriction of \(D_4\) to
\[
\mathcal P_{2,\tau}=\{A\in M_2(\mathbb C):A=A^*\ge0,\ \operatorname{Tr}A=\tau\}
\]
is a genuine metric, even though the general metric theorem for this affinity concerns exponents \(1\le p\le2\).

In sharp contrast, \(D_4\) is **not** a metric on the unrestricted positive cone of \(M_2(\mathbb C)\). Indeed the three positive semidefinite matrices
\[
A=\begin{pmatrix}2&2\\2&2\end{pmatrix},\quad
B=\begin{pmatrix}2&0\\0&1\end{pmatrix},\quad
C=\begin{pmatrix}2&0\\0&0\end{pmatrix}
\]
satisfy
\[
D_4(A,C)=\sqrt{240}>\sqrt{201}+1=D_4(A,B)+D_4(B,C).
\]
The dimension is optimal for an unrestricted-cone counterexample: for nonnegative scalars, \(D_4(a,b)=|a^2-b^2|\), a metric on \([0,\infty)\).

More generally, for any real inner-product space \(H\) and every \(c>0\),
\[
d_c(x,y)=\|x-y\|\sqrt{c+\|x+y\|^2}
\]
defines a metric on \(H\). For every triple, it is represented *exactly* by a Euclidean chord metric on \(\mathbb C^2\). The fixed-trace matrix theorem follows from this geometric statement.

## Assumptions and scope

All matrices are complex Hermitian positive semidefinite; no invertibility is assumed. The Schatten-four norm is \(\|X\|_4^4=\operatorname{Tr}(X^*X)^2\). The trace parameter \(\tau\) is the **same** for all matrices in the metric statement and is strictly positive. In the general Hilbert-space lemma, the norm comes from a real inner product and \(c>0\). No metric claim is made here for arbitrary trace, arbitrary matrix dimension, or other exponents above two.

## Proof

**Step 1 (exact quartic formula).** For positive semidefinite \(A,B\), cyclicity of trace gives
\[
\|A^{1/2}B^{1/2}\|_4^4
=\operatorname{Tr}(B^{1/2}AB^{1/2})^2
=\operatorname{Tr}(ABAB).
\]
Thus the squared expression is nonnegative because
\[
D_4(A,B)^2=\|(A-B)(A+B)\|_2^2
=\|A^2-B^2\|_2^2+\|[A,B]\|_2^2.
\]
Indeed \((A-B)(A+B)=(A^2-B^2)+[A,B]\), the first summand is Hermitian, and the second is skew-Hermitian, so their real Hilbert–Schmidt inner product vanishes. Expanding its trace gives the defining fourth-power expression. If it vanishes, the Hermitian term \(A^2-B^2\) vanishes; positive square-root uniqueness then implies \(A=B\). Symmetry is evident.

**Step 2 (Pauli reduction).** Let \(\sigma_1,\sigma_2,\sigma_3\) be the standard Pauli matrices. Every Hermitian \(2\times2\) matrix of trace \(2t\) is uniquely
\[
A=tI+x_1\sigma_1+x_2\sigma_2+x_3\sigma_3,
\qquad x\in\mathbb R^3.
\]
It is positive semidefinite if and only if \(\|x\|\le t\). The identities \(\sigma_i\sigma_j+\sigma_j\sigma_i=2\delta_{ij}I\), \(\operatorname{Tr}\sigma_i=0\), and \(\operatorname{Tr}I=2\), when applied to \(A=tI+x\cdot\sigma\) and \(B=tI+y\cdot\sigma\), yield
\[
\boxed{D_4(A,B)^2=2\|x-y\|^2\bigl(4t^2+\|x+y\|^2\bigr).}
\]
For an independent check, the terms are \(\operatorname{Tr}A^4=2(t^4+6t^2\|x\|^2+\|x\|^4)\) and
\[
\operatorname{Tr}(ABAB)=2\bigl[(t^2+x\cdot y)^2+t^2\|x+y\|^2-\|x\times y\|^2\bigr],
\]
whose subtraction produces the displayed formula.

**Step 3 (three-point Euclidean realization).** Fix any \(x,y,z\) in a real Hilbert space \(H\). Their affine hull \(W\) has dimension at most two. Let \(w\) be the closest point of \(W\) to the origin, so \(W=w+V\) with \(w\perp V\). Identify the one- or two-dimensional Euclidean space \(V\) isometrically with a real subspace of \(\mathbb C\), writing the coordinates of \(x,y,z\) as \(\alpha,\beta,\gamma\). For each pair,
\[
\|x-y\|^2=|\alpha-\beta|^2,
\qquad\|x+y\|^2=4\|w\|^2+|\alpha+\beta|^2.
\]
Therefore, for any \(c>0\),
\[
\begin{aligned}
d_c(x,y)^2
&=(c+4\|w\|^2)|\alpha-\beta|^2+|\alpha^2-\beta^2|^2\\
&=\|\Phi(\alpha)-\Phi(\beta)\|_{\mathbb C^2}^2,
\end{aligned}
\]
where \(\Phi(\zeta)=(\sqrt{c+4\|w\|^2}\,\zeta,\zeta^2)\). The **same** map represents all three pairwise distances of this triple, hence the Euclidean triangle inequality proves the triangle inequality for \(d_c\). Since \(c>0\), \(d_c(x,y)=0\) only if \(x=y\). Apply the lemma to \(H=\mathbb R^3\) with \(c=4t^2>0\), then scale the metric by \(\sqrt2\), proving the fixed-trace assertion.

**Step 4 (exact obstruction and minimal dimension).** For the displayed integer matrices, all principal minors are nonnegative (\(A\) has rank one, \(B\) is positive definite, \(C\) is rank one). Exact matrix multiplication gives
\[
D_4(A,C)^2=240,\quad D_4(A,B)^2=201,\quad D_4(B,C)^2=1.
\]
As \(240-(201+1)=38>2\sqrt{201}\), equivalently \(19^2=361>201\), the triangle inequality fails. In matrix dimension one, \(D_4(a,b)=|a^2-b^2|\) is the Euclidean distance under the injective mapping \(a\mapsto a^2\); dimension two is therefore minimal.

## Verification

The accompanying `check.py` recomputes all three squared counterexample distances by exact integer matrix arithmetic, checks the strict integer inequality, and numerically cross-checks the Pauli identity and metric triangle relations on deterministic finite samples. The equality of all three pairwise distances with a single \(\mathbb C^2\)-chord construction in Step 3 provides the infinite, noncomputational proof of the triangle inequality; the numerical tests are only diagnostics.

## Relationship to prior work

Sra's October 11, 2026 preprint, arXiv:2610.15889v1, proves that the \(p\)-Bures–Wasserstein affinity distance is a metric on arbitrary finite positive matrix cones for \(1\le p\le2\) and develops a three-block Schatten inequality and barycenter theory. It does not assert the fourth-exponent fixed-trace qubit metric or the stated cone obstruction. Its introduction also cites the related October 2026 work of Vuong and Osaka, which addresses the same \(1\le p\le2\) positive-matrix metric range. The present theorem deliberately concerns \(p=4\), with a restrictive positive trace slice and an exact counterexample off that slice. Earlier results about generalized Bures geometry may use related terminology; no complete historical uniqueness claim is made.

## Limitations

The positive theorem is specific to dimension two and a common fixed trace. The counterexample proves failure on the full cone already in dimension two, but does not classify every exponent above two or all higher-dimensional fixed-trace slices. The geometric embedding depends on the affine plane of the triple; it is not a claimed single global Hilbert embedding of all qubit states. Independent verification and comprehensive historical-priority certification remain outstanding.

## References

1. Suvrit Sra, *The \(p\)-Bures–Wasserstein distance via \(3\times3\) block matrices (with application to \(p\)-Bures–Wasserstein barycenters)*, arXiv:2610.15889v1, first posted 2026-10-11. https://arxiv.org/abs/2610.15889
2. Trung-Dung Vuong and Hiroyuki Osaka, related October 2026 finite-tracial result noted in Sra's Introduction (bibliographic details in reference [Vuong--Osaka 2026] of arXiv:2610.15889v1).
