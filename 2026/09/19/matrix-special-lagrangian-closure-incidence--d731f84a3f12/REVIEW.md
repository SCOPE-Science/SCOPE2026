# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

Kotwal--Menon Proposition 4.1 gives a semidefinite common factorization
\(W_k=V_kPV_{k-1}^*\) with prescribed terminal label \(V_N=Q\).
The positive factor is nevertheless unique:
\(P=(W_1^*W_1)^{1/2}\). Telescoping gives
\(W_N\cdots W_1=QP^N\). Therefore two labels \(Q,Q_0\) through the same
rank-\(r\) point differ by a unitary fixing
\(E=\operatorname{im}P\) pointwise, hence by exactly
\(I_E\oplus U(E^\perp)\). Conversely every such unitary leaves \(P\), and
therefore the tuple, unchanged. This proves the exact \(U(d-r)\) label fiber.

For pairwise intersections, the same product identity gives
\(\operatorname{im}P\subseteq\ker(Q-R)\). The converse is constructive:
choose any rank-\(r\) positive semidefinite \(P\) supported in
\(\ker(Q-R)\) and use the tuple \((P,\ldots,P,QP)\). This also proves the
multiple-intersection criterion. The dimension formula counts rank-\(r\)
positive factors supported in an \(f\)-plane and quotients each intermediate
unitary by its \(U(d-r)\) stabilizer. The \(N=2\) formula agrees with the
paper's explicit linear description
\(\mathcal C_Q=\{(A,QA^*):A\in M_d(\mathbb C)\}\), giving an independent
algebraic check of the rank threshold and dimension count.

Edge cases were checked explicitly: \(r=d\) gives one label and the known
dimension \(Nd^2\); \(r=0\) gives the common vertex and all \(U_d\) labels;
\(d=1\) recovers the scalar Harvey--Lawson incidence.

## Originality

The closest source is Kotwal--Menon, arXiv:2609.20159v1. Its Section 4 proves
that the closures cover the balanced variety and that every rank-deficient
point of one closure belongs to at least one other closure. The accessible
full text was checked for intersection, overlap, stabilizer, rank-stratum,
and relative-unitary formulations. No exact description of all labels through
a point, no pairwise spectral intersection criterion, and no rank-stratum
dimension formula was located.

Searches using combinations of “balanced variety”, “special Lagrangian”,
“closure incidence”, “rank-deficient polar factor”, “relative unitary”, and
“unitary extension” likewise did not locate the stated package. The
nonuniqueness of the unitary factor in the polar decomposition of a singular
matrix is standard linear algebra and is not claimed as new; the originality
claim is the resulting global incidence classification for the
Kotwal--Menon closure cover.

Kotwal's 2026 Brown dissertation *Symmetries and Gradient Flows in the Deep
Linear Network* (DOI: 10.26300/bd6x-0503) is cited by the source paper for
DLN symmetry and gauge-theoretic background. Its full text was not inspected.
Because it is by the same author and concerns the same balanced geometry, it
is the most plausible inaccessible source that could contain related
singular-factorization observations, although the source paper itself does
not cite it in Section 4. This is a residual originality risk, not evidence
of prior coverage.

The originality claim is therefore **to the best of our knowledge**. The
motivating preprint was submitted on 17 September 2026, so later revisions or
unindexed parallel observations are an additional residual risk.

## Value

The result turns a qualitative overlap statement into an exact incidence
geometry. At rank \(r\), the multiplicity of the closure cover is the compact
group \(U(d-r)\); for two labels, the largest possible overlap rank is exactly
the multiplicity of the eigenvalue \(1\) of \(R^*Q\). Hence generic distinct
closures meet only at the vertex, while every positive-rank overlap is
spectrally classified. The dimension formula further describes the smooth
rank strata of every finite multiple intersection.

This supplies a reusable structural description of how the special
Lagrangian foliation on the invertible balanced manifold degenerates on the
low-rank balanced variety.

## Limitations

The conclusions concern set-theoretic closure incidence and smooth fixed-rank
strata. They do not establish special-Lagrangian current extension across the
singular locus, local analytic normal forms, intersection multiplicities,
intersection angles, or calibrated-current regularity. The cited Brown
dissertation was not inspected in full, and the motivating preprint is very
recent. Cross-model review has not been performed.
