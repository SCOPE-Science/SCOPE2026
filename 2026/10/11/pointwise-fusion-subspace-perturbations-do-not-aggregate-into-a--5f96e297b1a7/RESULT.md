# Pointwise fusion-subspace perturbations do not aggregate into a frame bound
## Finding
Theorem 4.9 of Shakoory--Ahmadi--Behzadi--Nami asserts that a controlled fusion frame remains a controlled fusion frame when each indexed subspace perturbation is bounded by the same number \(\varepsilon<\sqrt A\). The assertion is false because the hypothesis is pointwise in the index while a fusion-frame bound is an \(\ell^2\)-sum over all indices.

Let
\[
H=\mathbb R^2,\qquad
I=\{1,2,3,4\},\qquad
C=C'=I_H,\qquad
v_i=\frac12,
\]
and set
\[
W_i=H\qquad(i\in I).
\]
Then
\[
\sum_{i=1}^4v_i^2\|P_{W_i}f\|^2
=
\|f\|^2,
\]
so the family is Parseval with \(A=B=1\).

Now take
\[
Z_i=\operatorname{span}\{e_2\}\qquad(i\in I).
\]
Because
\[
P_{W_i}-P_{Z_i}=P_{\operatorname{span}\{e_1\}},
\]
we have
\[
\left\|v_i(P_{W_i}-P_{Z_i})^{1/2}f\right\|
\le
\frac12\|f\|.
\]
Thus Theorem 4.9 accepts the family with
\[
\varepsilon=\frac12<1=\sqrt A.
\]
Its claimed lower bound is
\[
A-\varepsilon^2=\frac34.
\]
But
\[
\sum_{i=1}^4v_i^2\|P_{Z_i}f\|^2
=
\|P_{\operatorname{span}\{e_2\}}f\|^2,
\]
which is zero at \(f=e_1\). Hence the conclusion fails.

The natural repair is a global square-sum perturbation hypothesis:
\[
\sum_{i\in I}v_i^2
\left\|
\left(C^*P_{W_i}C'-C^*P_{Z_i}C'\right)^{1/2}f
\right\|^2
\le
\varepsilon^2\|f\|^2.
\]
Under the positivity needed for these square roots, this gives the valid bounds
\[
A-\varepsilon^2,\qquad B.
\]

For a finite index set of cardinality \(N\), the printed pointwise hypothesis yields only
\[
A-N\varepsilon^2
\]
as a general lower bound. The factor \(N\) is sharp.

## Assumptions and scope
The counterexample lies in the ordinary controlled-fusion subcase \(C=C'=I_H\), so every operator inside a square root is an orthogonal projection and is positive.

All four original subspaces are \(H\), all four perturbed subspaces are the same line, and all weights equal \(1/2\). There are no convergence, domain, or closure issues.

The result concerns Theorem 4.9. It does not reassess the article's duality results or other perturbation statements.

## Proof
For the original family,
\[
E_W(f)
=
\sum_{i=1}^4\frac14\|f\|^2
=
\|f\|^2.
\]
Hence \(A=B=1\).

For each index,
\[
D_i=P_{W_i}-P_{Z_i}=P_{\operatorname{span}\{e_1\}},
\]
so
\[
D_i^{1/2}=D_i
\]
and
\[
\|v_iD_i^{1/2}f\|
=
\frac12\|P_{\operatorname{span}\{e_1\}}f\|
\le
\frac12\|f\|.
\]
Therefore the source hypothesis holds with \(\varepsilon=1/2\).

For the perturbed family,
\[
E_Z(f)
=
\sum_{i=1}^4\frac14\|P_{\operatorname{span}\{e_2\}}f\|^2
=
\|P_{\operatorname{span}\{e_2\}}f\|^2.
\]
At \(f=e_1\),
\[
E_Z(e_1)=0,
\]
so no positive lower frame bound exists.

For the repair, assume
\[
D_i=C^*P_{W_i}C'-C^*P_{Z_i}C'\ge0
\]
and
\[
\sum_i v_i^2\|D_i^{1/2}f\|^2
\le
\varepsilon^2\|f\|^2.
\]
The controlled energies satisfy the exact identity
\[
E_Z(f)
=
E_W(f)
-
\sum_i v_i^2\|D_i^{1/2}f\|^2.
\]
Thus
\[
E_Z(f)
\ge
(A-\varepsilon^2)\|f\|^2
\]
and, because the subtracted term is nonnegative,
\[
E_Z(f)\le E_W(f)\le B\|f\|^2.
\]

If \(I\) has \(N\) elements and only the source's pointwise estimate is known, summing gives
\[
\sum_i v_i^2\|D_i^{1/2}f\|^2
\le
N\varepsilon^2\|f\|^2.
\]
Hence
\[
E_Z(f)\ge(A-N\varepsilon^2)\|f\|^2.
\]
This is sharp at the positivity threshold. For arbitrary \(N\ge2\), take \(W_i=H\), weights \(v_i=1/\sqrt N\), and \(Z_i=\operatorname{span}\{e_2\}\). Then \(A=1\), the least common pointwise constant is \(\varepsilon=1/\sqrt N\), and \(E_Z(e_1)=0\), so
\[
A-N\varepsilon^2=0.
\]

## Verification
The publisher PDF was inspected at Definition 3.1, the perturbation section, Theorem 4.9, and its complete proof. The theorem's displayed hypothesis contains no sum over \(i\): it bounds each
\[
v_i\left(C^*P_{W_i}C'-C^*P_{Z_i}C'\right)^{1/2}
\]
separately.

The proof then identifies the whole fusion-frame sum with one indexed norm and inserts only one copy of \(\varepsilon^2\). The four-block example shows exactly why this aggregation is invalid: each indexed error contributes \(1/4\) on \(e_1\), so the total perturbation energy is \(1\), not \(1/4\).

A closely related controlled \(K\)-fusion perturbation theorem by Assila--Kabbaj--Moalige uses a genuinely global sum condition over the index set. That theorem is structurally consistent with the repair above.

No numerical experiment is used.

## Relationship to prior work
The target article introduces perturbations for controlled fusion frames and states Theorem 4.9 with a per-index perturbation estimate.

Assila--Kabbaj--Moalige, *Controlled \(K\)-Fusion Frame for Hilbert Spaces*, formulate their perturbation condition through a sum over all subspaces. Their Proposition 4.1 therefore controls the aggregate perturbation energy rather than one indexed term. This does not state the counterexample above, but it shows that the global-sum geometry is standard in closely related controlled-fusion perturbation theory.

Classical frame and fusion-frame stability arguments likewise control a norm of the full analysis perturbation, not merely a uniform bound on each coordinate without accounting for how many coordinates contribute.

No checked indexed erratum or theorem-specific correction was found for Theorem 4.9.

## Limitations
The exact repair stated here uses the positivity of
\[
C^*P_{W_i}C'-C^*P_{Z_i}C'
\]
that is already implicit in the source's square-root notation. If a different perturbation notion does not impose this ordering, a triangle-inequality repair gives different constants.

The sharp \(N\)-factor statement concerns finite index sets under the literal pointwise hypothesis. Infinite index sets require an actual summability condition.

The result does not classify all perturbation metrics for controlled fusion frames.

## References
1. H. Shakoory, R. Ahmadi, N. Behzadi and S. Nami, *Controlled Fusion Frames in Hilbert Spaces and Their Dual*, Journal of Mathematical Extension 16(9) (2022), DOI 10.30495/jme.v0i0.1476.
2. N. Assila, S. Kabbaj and B. Moalige, *Controlled \(K\)-Fusion Frame for Hilbert Spaces*, Moroccan Journal of Pure and Applied Analysis 7(1) (2021), 116--133, DOI 10.2478/mjpaa-2021-0011; arXiv:2007.05110v1.
