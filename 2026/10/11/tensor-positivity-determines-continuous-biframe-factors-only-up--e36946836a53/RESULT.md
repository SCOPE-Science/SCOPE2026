# Tensor positivity determines continuous-biframe factors only up to reciprocal phase

## Finding
Ghosh--Samanta Theorem 4.2 states that the tensor-product pair
\[
(F_1\otimes F_2,G_1\otimes G_2)
\]
is a continuous biframe if and only if both factor pairs are continuous biframes. The reverse implication from tensor positivity to factor positivity is false.

Take
\[
H_1=H_2=\mathbb C,
\qquad
X_1=X_2=\{\ast\}
\]
with unit counting measure, and define
\[
F_1(\ast)=F_2(\ast)=1,
\qquad
G_1(\ast)=G_2(\ast)=-1.
\]
For every \(z\in\mathbb C\),
\[
\langle z,F_i(\ast)\rangle
\langle G_i(\ast),z\rangle
=
-|z|^2.
\]
Therefore neither \((F_i,G_i)\) is a continuous biframe: no positive lower bound can be dominated by a negative quadratic form.

On the tensor product,
\[
F_1\otimes F_2=1,
\qquad
G_1\otimes G_2=1.
\]
Consequently, for every simple tensor \(z\otimes w\),
\[
\langle z\otimes w,F_1\otimes F_2\rangle
\langle G_1\otimes G_2,z\otimes w\rangle
=
|z|^2|w|^2
=
\|z\otimes w\|^2.
\]
Thus the tensor pair is a Parseval continuous biframe although neither factor is a continuous biframe.

The exact missing information is phase. Under the scalar-integrability and Fubini hypotheses used to factor the tensor quadratic form in the source proof, the correct converse is:

\[
(F_1\otimes F_2,G_1\otimes G_2)
\text{ is a continuous biframe}
\]
if and only if there exists a unimodular scalar \(\zeta\) such that
\[
(F_1,\zeta G_1)
\quad\text{and}\quad
(F_2,\zeta^{-1}G_2)
\]
are continuous biframes.

In the real case, the phase ambiguity reduces to a common sign.

## Assumptions and scope
The counterexample uses one-dimensional Hilbert spaces and one-point measure spaces, so measurability, convergence, and Fubini issues are absent. It directly satisfies the tensor-product setup of Definition 4.1.

The corrected equivalence is stated under the factorization assumptions actually needed by the proof: for each vector, the scalar factor integrals exist and the tensor integral factors as their product. This holds, in particular, in the finite example and under standard absolute-integrability hypotheses.

No claim is made that the source's most general weak-measurability assumptions alone automatically justify every Fubini step.

## Proof
For the counterexample, the source's continuous-biframe quadratic form on each factor is
\[
q_i(z)
=
\langle z,1\rangle\langle-1,z\rangle
=
-|z|^2.
\]
Hence no constants \(A_i,B_i>0\) can satisfy
\[
A_i|z|^2\le q_i(z)\le B_i|z|^2
\]
for all \(z\).

The tensor vectors satisfy
\[
1\otimes1=1,
\qquad
(-1)\otimes(-1)=1
\]
under the canonical identification \(\mathbb C\otimes\mathbb C\cong\mathbb C\). Therefore the tensor quadratic form equals
\[
|z|^2|w|^2
=
\|z\otimes w\|^2,
\]
which proves the Parseval assertion.

For the corrected converse, write
\[
q_i(u)
=
\int_{X_i}
\langle u,F_i(x)\rangle
\langle G_i(x),u\rangle\,d\mu_i(x).
\]
Suppose
\[
A\|f\|^2\|g\|^2
\le
q_1(f)q_2(g)
\le
B\|f\|^2\|g\|^2
\]
for all \(f,g\), with \(A,B>0\). In particular, \(q_i(u)\ne0\) for every nonzero \(u\).

Fix a unit vector \(g_0\) and define
\[
\zeta=\frac{q_2(g_0)}{|q_2(g_0)|}.
\]
Since \(q_1(f)q_2(g_0)\) is positive real,
\[
\zeta q_1(f)
=
\frac{q_1(f)q_2(g_0)}{|q_2(g_0)|}
\]
is positive real. Dividing the tensor inequality by \(|q_2(g_0)|\) gives
\[
\frac{A}{|q_2(g_0)|}\|f\|^2
\le
\zeta q_1(f)
\le
\frac{B}{|q_2(g_0)|}\|f\|^2.
\]
Thus \((F_1,\zeta G_1)\) is a continuous biframe.

Choose a unit \(f_0\). Put
\[
d=\zeta q_1(f_0)>0.
\]
Then
\[
\zeta^{-1}q_2(g)
=
\frac{q_1(f_0)q_2(g)}{d},
\]
so
\[
\frac{A}{d}\|g\|^2
\le
\zeta^{-1}q_2(g)
\le
\frac{B}{d}\|g\|^2.
\]
Hence \((F_2,\zeta^{-1}G_2)\) is a continuous biframe.

Conversely, reciprocal phase rotations cancel in the tensor:
\[
(\zeta G_1)\otimes(\zeta^{-1}G_2)
=
G_1\otimes G_2.
\]
If the two rotated factor pairs have bounds \(A_1,B_1\) and \(A_2,B_2\), multiplication gives tensor bounds
\[
A_1A_2
\quad\text{and}\quad
B_1B_2.
\]
This proves the corrected equivalence under the stated factorization hypotheses.

## Verification
The first public full text was inspected at Definition 3.1, Definition 4.1, Theorem 4.2, and its complete proof. The theorem explicitly claims an unrotated factorwise equivalence.

Its converse proof factors the tensor quadratic form into \(q_1(f)q_2(g)\), notes that both factors are nonzero, and divides by one factor to manufacture proposed positive factor bounds. Nonvanishing is insufficient: the divisor can have a negative sign or, over complex scalars, a nontrivial phase. The displayed singleton example realizes the negative-sign case exactly.

A later paper on continuous biframes in Hilbert \(C^*\)-modules states the analogous tensor-factor equivalence as Theorem 4.1. Its theorem and proof were inspected. Specializing the coefficient algebra to \(\mathbb C\) returns the Hilbert-space situation above, so the later statement does not repair the phase obstruction.

No numerical experiment or finite search is used in the proof.

## Relationship to prior work
Biframes generalize controlled frames and pair frames, but their defining inequality imposes positivity on the mixed quadratic form. Tensor multiplication preserves only the product of the two factor phases. Therefore tensor positivity cannot distinguish a positive-positive pair from a negative-negative pair, or more generally from reciprocal complex phases.

The forward direction of the source theorem remains valid: two genuine factor biframes produce a tensor biframe by multiplying their positive bounds. What fails is only the unqualified converse.

Targeted searches for the exact source, its tensor theorem, sign cancellation, reciprocal phases, and tensor-product biframe factorization did not locate an indexed correction of the theorem. The closest indexed frame-theoretic results concern mixed-series convergence, dual \(g\)-frame criteria, operator-orbit independence, and unrelated tensor norms.

## Limitations
The corrected phase theorem assumes that the scalar factor integrals are defined and that the tensor integral factors as their product. It does not resolve any independent integrability gap that might arise under weaker hypotheses.

The result does not assess unrelated continuous-biframe theorems in the source. A nonindexed correction or informal note may contain the same observation.

## References
1. P. Ghosh and T. K. Samanta, *Introduction to Continuous biframes in Hilbert spaces and their tensor products*, arXiv:2309.07247v1, first public version 28 August 2023.
2. A. Lfounoune, A. Karara and M. Rossafi, *Continuous Biframes in Hilbert \(C^*\)-Modules*, International Journal of Analysis and Applications 23 (2025), 104, DOI 10.28924/2291-8639-23-2025-104.
3. M. F. Parizi, A. Alijani and M. A. Dehghan, *Biframes and Some of Their Properties*, Journal of Inequalities and Applications 2022 (2022), 104, DOI 10.1186/s13660-022-02844-7.
