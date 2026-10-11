# Exact covering radius and Wigner defect of translated positive trace-class cones
## Finding
Let \(H\) be a nonzero complex Hilbert space and let \(\mathcal C=S_1(H)_+\) be the positive trace-class cone with trace distance \(d_1(A,B)=\|A-B\|_1\). For a unitary or antiunitary \(U\) and \(P\in\mathcal C\), set
\[
T_{U,P}(A)=UAU^*+P.
\]
Then \(T_{U,P}\) is an exact isometric embedding. More precisely, for every \(B\in\mathcal C\),
\[
\operatorname{{dist}}_1(B,T_{U,P}(\mathcal C))=\operatorname{{Tr}}(B-P)_-.
\]
Hence, with
\[
\delta(T)=\sup_{{B\in\mathcal C}}\inf_{{A\in\mathcal C}}\|B-T(A)\|_1
\]
and
\[
D_W(T)=\inf_W\sup_{{A\in\mathcal C}}\|T(A)-WAW^*\|_1,
\]
where \(W\) ranges over unitary and antiunitary Wigner symmetries,
\[
\delta(T_{{U,P}})=D_W(T_{{U,P}})=\operatorname{{Tr}}P.
\]
Thus \(T_{{U,P}}\) is \(\delta_0\)-surjective exactly when \(\delta_0\ge\operatorname{{Tr}}P\). If \(P\ne0\), it is an exact, finitely almost-surjective, nonstandard isometry whose optimal surjectivity defect equals its optimal uniform Wigner defect.

## Assumptions and scope
The statement concerns the full positive trace-class cone, not the trace-one state space. The Hilbert space may be finite- or infinite-dimensional. The map \(U\) may be unitary or antiunitary. No compactness, finite-rank, commutativity, or spectral assumptions are imposed on \(P\) beyond positivity and trace class.

The quantity \((B-P)_-\) is the negative part of the self-adjoint trace-class operator \(B-P\). The covering radius is measured in the trace norm. The Wigner comparison class consists exactly of maps \(A\mapsto WAW^*\) with \(W\) unitary or antiunitary.

## Proof
Conjugation by a unitary or antiunitary preserves positivity and the trace norm. Therefore, for \(A_1,A_2\in\mathcal C\),
\[
\|T_{{U,P}}(A_1)-T_{{U,P}}(A_2)\|_1
=\|U(A_1-A_2)U^*\|_1
=\|A_1-A_2\|_1.
\]
Thus \(T_{{U,P}}\) is an exact isometric embedding. Since conjugation by \(U\) maps \(\mathcal C\) bijectively onto itself, its range is \(P+\mathcal C\).

Fix \(B\in\mathcal C\) and put \(X=B-P\). For any \(C\in\mathcal C\), let \(Q\) be the support projection of \(X_-\). Then
\[
\|X-C\|_1\ge |\operatorname{{Tr}}(Q(X-C))|
=\operatorname{{Tr}}X_-+\operatorname{{Tr}}(QC)
\ge\operatorname{{Tr}}X_-.
\]
Taking \(C=X_+\) gives equality because \(X-X_+=-X_-\). Hence
\[
\operatorname{{dist}}_1(B,P+\mathcal C)=\operatorname{{Tr}}(B-P)_-.
\]
This is the asserted pointwise distance formula.

At \(B=0\), the formula gives distance \(\operatorname{{Tr}}P\), so \(\delta(T_{{U,P}})\ge\operatorname{{Tr}}P\). Conversely, for every positive contraction \(0\le Q\le I\),
\[
-\operatorname{{Tr}}(Q(B-P))
=\operatorname{{Tr}}(QP)-\operatorname{{Tr}}(QB)
\le\operatorname{{Tr}}P.
\]
Using the variational identity
\[
\operatorname{{Tr}}(B-P)_-
=\sup_{{0\le Q\le I}}-\operatorname{{Tr}}(Q(B-P))
\]
gives \(\operatorname{{dist}}_1(B,P+\mathcal C)\le\operatorname{{Tr}}P\) for all \(B\). Therefore \(\delta(T_{{U,P}})=\operatorname{{Tr}}P\).

For the Wigner defect, choosing \(W=U\) gives
\[
\sup_{{A\in\mathcal C}}\|T_{{U,P}}(A)-UAU^*\|_1=\|P\|_1=\operatorname{{Tr}}P.
\]
For every unitary or antiunitary \(W\), evaluating at \(A=0\) yields
\[
\|T_{{U,P}}(0)-W0W^*\|_1=\|P\|_1=\operatorname{{Tr}}P.
\]
Hence no Wigner symmetry can do better, and \(D_W(T_{{U,P}})=\operatorname{{Tr}}P\).

## Verification
The proof uses only standard trace-class facts: unitary or antiunitary invariance of the trace norm, the positive/negative decomposition of a self-adjoint trace-class operator, the dual characterization of the trace norm against contractions, and the variational formula for the trace of the negative part. Each equality is exact; no numerical experiment or finite-dimensional approximation is used.

The boundary cases are consistent. If \(P=0\), the map is a Wigner symmetry and both defects vanish. If \(P\ne0\), the map does not fix zero, its range is proper, but its covering radius remains finite and equals \(\operatorname{{Tr}}P\).

## Relationship to prior work
Looi's 2026 paper proves dimension-independent Hyers--Ulam stability for surjective approximate isometries of the positive trace-class cone and, for maps fixing zero, a trace-metric bound independent of the almost-surjectivity parameter. It also gives nonsurjective exact embeddings in infinite dimension to show why a range hypothesis is needed. The present statement isolates a different boundary phenomenon: a canonical translated cone with a finite covering radius, and it computes both that radius and the nearest-Wigner uniform defect exactly.

Dong, Leung, and Li study stability of almost-surjective approximate isometries between positive cones of ordered Banach spaces under the standard normalization \(T(0)=0\), including several Schatten and operator-algebra settings. Their stated framework reinforces that the origin normalization is structural; it does not supply the exact trace-class translation formulas above.

## Limitations
The theorem concerns the trace metric only; no analogous exact formula is claimed for the Bures metric. It classifies the translated Wigner family \(A\mapsto UAU^*+P\), not all nonstandard approximate isometries. The originality search cannot exclude an older equivalent cone-translation observation under different terminology, although no covering statement was located in the checked sources.

## References
1. Sam Looi, *Stability of isometries of quantum states*, arXiv:2609.37133v1, first public 2026-09-29.
2. Yunbai Dong, Denny H. Leung, and Lei Li, *Stability of isometries between the positive cones of ordered Banach spaces*, Mathematische Annalen 389 (2024), 253--280, DOI 10.1007/s00208-023-02649-z.
