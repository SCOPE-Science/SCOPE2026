# A missing norm square invalidates an integral \(K\)-operator-frame perturbation theorem

## Finding
Theorem 3.1 of Labrigui--Rossafi--Touri--Kabbaj states that an integral \(K\)-operator frame
\[
\{\Lambda_\omega\}_{\omega\in\Omega}
\]
with lower bound \(A\) remains an integral \(K\)-operator frame after the perturbation
\[
\Lambda_\omega\longmapsto \Lambda_\omega+a_\omega LK^*
\]
whenever
\[
\int_\Omega |a_\omega|^2\,d\mu(\omega)
<
\frac{A}{\|L\|}.
\]
This condition is false as printed. The proof defines
\[
R=
\|L\|^2
\int_\Omega |a_\omega|^2\,d\mu(\omega)
\]
and derives a lower estimate containing \(\sqrt A-\sqrt R\). The argument therefore requires
\[
R<A,
\]
which is equivalent to
\[
\int_\Omega |a_\omega|^2\,d\mu(\omega)
<
\frac{A}{\|L\|^2}.
\]

The missing square is not cosmetic. Fix any \(A>0\) and \(t>1\). Let
\[
H=\mathbb C,\qquad
\Omega=\{\ast\},\qquad
\mu(\{\ast\})=1,
\]
and choose
\[
K=I,\qquad
\Lambda_\ast=\sqrt A\,I,\qquad
L=tI,\qquad
a_\ast=-\frac{\sqrt A}{t}.
\]
Then
\[
\int_\Omega\|\Lambda_\omega x\|^2\,d\mu(\omega)
=
A\|x\|^2
=
A\|K^*x\|^2,
\]
so the original family is \(A\)-tight. Moreover,
\[
\int_\Omega |a_\omega|^2\,d\mu(\omega)
=
\frac{A}{t^2}
<
\frac{A}{t}
=
\frac{A}{\|L\|},
\]
and hence every printed hypothesis is satisfied. But
\[
\Lambda_\ast+a_\ast LK^*
=
\sqrt A\,I-\frac{\sqrt A}{t}\,tI
=
0.
\]
The perturbed family therefore has no positive lower \(K\)-frame bound.

The same missing norm square occurs in the later Hilbert-\(C^*\)-module generalization of integral operator frames. There the perturbing operator is denoted here by \(Q\): the theorem prints
\[
\int_\Omega |c_\omega|^2\,d\mu(\omega)
<
\frac{A}{\|Q\|},
\]
although the proof defines
\[
R=
\|Q\|^2
\int_\Omega |c_\omega|^2\,d\mu(\omega)
\]
and again needs \(R<A\). The scalar Hilbert-\(\mathbb C\)-module specialization gives the same exact counterexample.

## Assumptions and scope
For the first theorem, \(H\) is a separable Hilbert space, \(K,L\in\mathcal B(H)\), and \(\{\Lambda_\omega\}\) is an integral \(K\)-operator frame with lower and upper bounds \(A,B>0\). The perturbation coefficient \(a\) is square integrable.

The counterexample uses the smallest possible coefficient and ambient spaces. Thus it does not rely on nonclosed ranges, weak measurability subtleties, infinite-dimensional effects, or failure of an integral to exist.

The corrected condition below is a universal sufficient condition depending only on the original lower bound, the \(L^2\)-size of the scalar perturbation, and the operator norm. Its strict boundary is sharp in this norm-only form. This does not assert that every individual perturbation with larger norm must fail.

For the later Hilbert-\(C^*\)-module theorem, the scalar module over \(\mathbb C\) is already a special case, so it suffices to refute the printed statement. The general repaired module statement follows from the bounded-below analysis-operator argument described below, assuming the analysis operator and its adjoint are defined as in the source.

## Proof
Set
\[
\rho
=
\|L\|
\left(
\int_\Omega |a_\omega|^2\,d\mu(\omega)
\right)^{1/2}.
\]
For every \(x\in H\), the perturbation coefficient vector satisfies
\[
\left(
\int_\Omega
\|a_\omega LK^*x\|^2\,d\mu(\omega)
\right)^{1/2}
\le
\rho\|K^*x\|.
\]
The original lower frame inequality gives
\[
\left(
\int_\Omega
\|\Lambda_\omega x\|^2\,d\mu(\omega)
\right)^{1/2}
\ge
\sqrt A\,\|K^*x\|.
\]
The reverse triangle inequality in \(L^2(\Omega,H)\) therefore yields
\[
\left(
\int_\Omega
\|(\Lambda_\omega+a_\omega LK^*)x\|^2\,d\mu(\omega)
\right)^{1/2}
\ge
(\sqrt A-\rho)\|K^*x\|.
\]
If
\[
\rho<\sqrt A,
\]
squaring gives the positive lower \(K\)-frame bound
\[
(\sqrt A-\rho)^2.
\]

For the upper bound,
\[
\left(
\int_\Omega
\|(\Lambda_\omega+a_\omega LK^*)x\|^2\,d\mu(\omega)
\right)^{1/2}
\le
\sqrt B\,\|x\|
+
\rho\|K^*x\|.
\]
Since
\[
\|K^*x\|\le\|K\|\|x\|,
\]
one valid upper bound is
\[
\left(\sqrt B+\rho\|K\|\right)^2.
\]
Thus
\[
\int_\Omega |a_\omega|^2\,d\mu(\omega)
<
\frac{A}{\|L\|^2}
\]
is sufficient.

It is sharp as a universal strict norm threshold. In the scalar family above,
\[
\rho
=
t\frac{\sqrt A}{t}
=
\sqrt A,
\]
and the perturbation cancels the frame exactly.

For the Hilbert-\(C^*\)-module version, let \(R_T\) be the analysis operator of the original integral operator frame and let \(D\) be the perturbation analysis operator. The same norm estimate gives
\[
\|D\|
\le
\|Q\|
\left(
\int_\Omega |c_\omega|^2\,d\mu(\omega)
\right)^{1/2}.
\]
If this is strictly less than \(\sqrt A\), then \(R_T+D\) is bounded below. An adjointable bounded-below operator has positive invertible \((R_T+D)^*(R_T+D)\), hence a positive module-order lower frame bound. The usual norm estimate supplies an upper bound. Therefore the squared-denominator condition is also the correct norm-scale sufficient hypothesis for that generalization.

## Verification
The first public full text was inspected at Definition 2.1 and at the complete statement and proof of Theorem 3.1. The theorem prints the denominator \(\|L\|\), while its own proof defines
\[
R=
\|L\|^2\int_\Omega|a_\omega|^2\,d\mu
\]
and concludes from \(R<A\). These two lines are algebraically incompatible unless the final denominator is \(\|L\|^2\).

The 2021 published version was checked at the same perturbation theorem and retains the printed condition.

The later first public Hilbert-\(C^*\)-module version was inspected at its primary classification, integral operator-frame definition, and complete Theorem 3.1 proof. It repeats the same pattern with a perturbing operator \(Q\): \(R\) contains \(\|Q\|^2\), but the final displayed sufficient condition contains only \(\|Q\|\). The 2024 published text likewise retains that theorem.

The scalar cancellation is exact for every \(A>0\) and every \(t>1\). No finite experiment, numerical approximation, or asymptotic inference is used.

## Relationship to prior work
The ordinary perturbation principle behind the proof is the standard reverse-triangle estimate for analysis operators: an analysis operator bounded below by \(\sqrt A\) remains bounded below after a perturbation of operator norm strictly smaller than \(\sqrt A\).

The closest indexed frame-theoretic comparison found in the searches concerns a different result: a compact rank-one perturbation can destroy a controlled \(K\)-frame, with quantitative smallness restoring stability. That result supports the general role of a \(\sqrt A\)-scale perturbation threshold but neither states nor implies the missing-square correction for integral \(K\)-operator frames.

Other close indexed results concern closed-range reconstruction, diagonal scaling, frame excess, and dual-\(g\)-frame obstructions. Their hypotheses and conclusions do not cover the scalar cancellation above.

The notable literature relation is propagation: the same norm-square mismatch appears first in the 2020 integral \(K\)-operator-frame theorem and later in the 2023 Hilbert-\(C^*\)-module integral-operator-frame generalization. No inspected indexed source supplied a correction of this perturbation threshold.

## Limitations
The corrected threshold is a sharp universal sufficient condition in terms of \(A\), the scalar \(L^2\)-norm, and the perturbing operator norm. It is not claimed to be necessary for every particular perturbation direction.

The finding does not assess the other perturbation or stability theorems in either paper.

A nonindexed erratum, thesis remark, or informal correction may contain the same observation.

## References
1. H. Labrigui, M. Rossafi, A. Touri and S. Kabbaj, *Integral \(K\)-Operator Frames for \(\mathcal B(H)\)*, arXiv:2008.05037v1, first posted 11 August 2020; later published in *Annals of the University of Craiova, Mathematics and Computer Science Series* 48(2) (2021), 244--257.
2. N. Assila, H. Labrigui, A. Touri and M. Rossafi, *Integral Operator Frames on Hilbert \(C^*\)-modules*, arXiv:2301.07217v1, first posted 17 January 2023; later published in *Annali dell'Università di Ferrara* 70 (2024), 1271--1284, DOI 10.1007/s11565-024-00501-z.
