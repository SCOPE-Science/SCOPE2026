# A redundancy counterexample to a woven \(g\)-frame perturbation theorem

## Finding
Theorem 2.4 of Rajput--Sahu--Mishra gives a sufficient perturbation condition for two \(g\)-frames in a Hilbert \(C^*\)-module to be woven. The statement is false as printed.

The hypothesis controls
\[
\left(\sum_i\|(\Lambda_i^*-\Gamma_i^*)c_i\|^2\right)^{1/2},
\]
but the proof identifies this with
\[
\left\|\sum_i(\Lambda_i^*-\Gamma_i^*)c_i\right\|.
\]
The first quantity is the direct-sum norm of the individual component outputs; the second is the norm of their synthesis sum. Redundancy can make the second arbitrarily larger than the first.

Take the scalar Hilbert \(C^*\)-module
\[
H=\mathbb C^2
\]
with coefficient spaces \(V_i=\mathbb C\). Let
\[
s=\frac12.
\]
For \(1\le i\le64\), set
\[
\Lambda_i f=s\langle f,e_1\rangle,\qquad
\Gamma_i f=s\langle f,e_2\rangle,
\]
and for \(65\le i\le128\), set
\[
\Lambda_i f=s\langle f,e_2\rangle,\qquad
\Gamma_i f=s\langle f,e_1\rangle.
\]
For all later indices, set both operators equal to zero.

Each family is tight:
\[
\sum_i\|\Lambda_i f\|^2
=
\sum_i\|\Gamma_i f\|^2
=
16\|f\|^2.
\]
Thus the exact frame bounds are
\[
A_1=B_1=A_2=B_2=16.
\]

Choose
\[
\lambda_1=\lambda_2=\frac1{100},
\qquad
\mu=\frac34.
\]
The scalar condition of Theorem 2.4 is satisfied:
\[
\lambda_1\sqrt{B_1}
+\lambda_2\sqrt{B_2}
+\mu
=
\frac{83}{100}
<
1
=
\frac{A_1}{2(\sqrt{B_1}+\sqrt{B_2})}.
\]

For every coefficient family \(c=(c_i)\in\ell^2\),
\[
\left(
\sum_i\|(\Lambda_i^*-\Gamma_i^*)c_i\|^2
\right)^{1/2}
=
\frac1{\sqrt2}\|c_{\rm act}\|
\le
\frac1{\sqrt2}\|c\|.
\]
Since
\[
\frac1{\sqrt2}<\frac34,
\]
the displayed perturbation inequality holds even if the two positive relative-error terms are discarded.

Now choose the weave that takes \(\Lambda_i\) for \(1\le i\le64\) and \(\Gamma_i\) for \(65\le i\le128\). Every active member of this weave is the \(e_1\)-coordinate functional multiplied by \(1/2\). Hence, at
\[
f=e_2,
\]
its energy is zero. The weave is not a \(g\)-frame, so the claimed universal lower bound
\[
\frac{A_1}{2}=8
\]
is impossible.

## Assumptions and scope
A Hilbert space is a Hilbert \(C^*\)-module over the scalar algebra \(\mathbb C\), so the example lies inside the source's stated category.

Only finitely many analysis operators are nonzero, so every sum converges unconditionally and every synthesis operator is bounded. Both original families are tight \(g\)-frames.

The finding refutes Theorem 2.4 as printed. It does not assert that every perturbation result in the paper fails.

## Proof
For \(1\le i\le64\),
\[
\|\Lambda_i f\|^2=\frac14|\langle f,e_1\rangle|^2,
\]
and for \(65\le i\le128\),
\[
\|\Lambda_i f\|^2=\frac14|\langle f,e_2\rangle|^2.
\]
Therefore
\[
\sum_i\|\Lambda_i f\|^2
=
64\cdot\frac14|\langle f,e_1\rangle|^2
+
64\cdot\frac14|\langle f,e_2\rangle|^2
=
16\|f\|^2.
\]
The same calculation applies to \(\Gamma\).

For each active index, the vector
\[
(\Lambda_i^*-\Gamma_i^*)c_i
\]
is either
\[
\frac12c_i(e_1-e_2)
\]
or its negative. Hence
\[
\|(\Lambda_i^*-\Gamma_i^*)c_i\|^2
=
\frac12|c_i|^2,
\]
and summation gives
\[
\left(
\sum_i\|(\Lambda_i^*-\Gamma_i^*)c_i\|^2
\right)^{1/2}
=
\frac1{\sqrt2}\|c_{\rm act}\|.
\]
The source's right-hand side contains the term
\[
\mu\|c\|=\frac34\|c\|,
\]
which alone dominates the left-hand side.

For the synthesis difference, write \(A=\{1,\ldots,64\}\) and \(B=\{65,\ldots,128\}\). Then
\[
(T_\Lambda-T_\Gamma)c
=
\frac12
\left(
\sum_{i\in A}c_i-\sum_{i\in B}c_i
\right)(e_1-e_2).
\]
The coefficient vector of the scalar functional in parentheses has Euclidean norm
\[
\sqrt{128},
\]
so
\[
\|T_\Lambda-T_\Gamma\|
=
\frac12\sqrt2\sqrt{128}
=
8.
\]
By contrast, the direct-sum component-difference operator has norm \(1/\sqrt2\). The ratio is
\[
8\sqrt2=\sqrt{128}.
\]
Thus the equality used in the published proof is false by exactly the redundancy factor in this example.

## Verification
The publisher PDF was inspected at Theorem 2.4 and its proof. The theorem states the componentwise adjoint-difference condition and the universal lower bound \(A_1/2\).

The next page defines the synthesis operators and explicitly replaces the componentwise direct-sum norm by \(\|(T_\Lambda-T_\Gamma)c\|\). These are different quantities; the counterexample computes both exactly.

All calculations above are symbolic. No finite search, approximation, or numerical tolerance is used.

The source was published online on 30 March 2021 and lists primary MSC \(42C15\).

## Relationship to prior work
Perturbation results for woven frames naturally control a global analysis or synthesis operator difference. For example, Zhao's 2021 perturbation theorem for woven frames in Hilbert \(C^*\)-modules is formulated using a global analysis-operator difference rather than an \(\ell^2\)-sum of separate adjoint outputs.

That distinction is essential here: the printed condition in Theorem 2.4 controls an operator into a direct sum, while the proof needs control of an operator obtained after summing those components. There is no dimension-free bound from the former to the latter.

Targeted searches using the exact title, DOI, theorem number, componentwise perturbation formula, synthesis-difference formulation, and correction terminology did not locate an indexed erratum or a source containing this redundancy counterexample.

Nearby results on dual-frame weaving, \(K\)-frame reconstruction, compact perturbations, and local fusion-frame weaving address different hypotheses and do not imply this theorem-specific failure.

## Limitations
The counterexample establishes failure of the published sufficient condition. It does not give a complete sharp replacement theorem.

Replacing the componentwise quantity by the genuine synthesis difference removes the exact false equality in the proof, but any claimed quantitative lower bound should be checked from that corrected hypothesis rather than inherited automatically from the printed theorem.

An unindexed erratum, thesis remark, or informal correction may contain the same observation.

## References
1. E. Rajput, N. K. Sahu and V. N. Mishra, *Woven \(g\)-frames in Hilbert \(C^*\)-modules*, Korean Journal of Mathematics 29(1) (2021), 41--55, DOI 10.11568/kjm.2021.29.1.41.
2. X. Zhao, *Weaving Frames in Hilbert \(C^*\)-Modules*, Journal of Mathematics 2021, Article 2228397, DOI 10.1155/2021/2228397.
