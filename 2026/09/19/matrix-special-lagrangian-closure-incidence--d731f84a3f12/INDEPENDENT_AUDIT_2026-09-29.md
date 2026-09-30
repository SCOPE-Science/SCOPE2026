# Independent audit — Rank-stratified incidence of matrix special-Lagrangian cone closures

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/19/matrix-special-lagrangian-closure-incidence--d731f84a3f12`  
**Audited tree:** `7294aadef22543840e8e86c2c9aabe680592efe6`

## Disposition

**PASSED.** Correctness, originality on the stated narrow boundary, and scientific value all pass. The record may remain in the validated set.

## Correctness

**PASS.** The incidence classification follows from the source factorization without an extra hidden assumption. Proposition 4.1 gives W_k=V_k P V_{k-1}^* with V_0=I and V_N=Q, while P=(W_1^*W_1)^{1/2} is unique. Telescoping gives W_N...W_1=Q P^N. Hence two labels Q,Q0 through the same point differ by S=Q0^*Q fixing im P pointwise, and unitarity makes S=I_E direct-sum S0 on E^perp. Conversely such an S satisfies SP=P and can replace only the terminal factor, proving the full U(d-r) label fiber. Pairwise and multiple intersections follow by im P subset ker(Q-R), with the converse realized by (P,...,P,QP). The fixed-rank dimension is the sum of 2r(f-r)+r^2 for the supported positive factor and N-1 copies of d^2-(d-r)^2 for intermediate unitary restrictions, giving 2r(f+(N-1)d)-Nr^2.

## Originality

**PASS, with the limitations below.** The source arXiv:2609.20159 proves that rank-deficient points of a closure can belong to another closure, whereas the audited record gives the complete label fiber, relative-unitary spectral criterion for all finite intersections, and fixed-rank stratum dimensions. Those formulas are not merely the standard nonuniqueness of singular polar decomposition: they classify the incidence geometry of the source's closure cover. Kotwal's 2026 Brown dissertation is a relevant same-author background source and was not available in full during this audit, so it remains a residual priority risk; however the source preprint itself cites the dissertation for deep-linear-network geometry while presenting the closure-overlap result only qualitatively, which is positive evidence for the narrower extension claimed here.

## Scientific value

**PASS.** The result upgrades a qualitative singular-overlap statement to a full rank-stratified incidence geometry. The U(d-r) multiplicity, spectral fixed-space criterion, generic vertex-only intersection, and stratum dimensions together give a reusable description of how the special-Lagrangian foliation degenerates on the balanced variety. This is a genuine structural extension of the motivating paper.

## Independent checks

- Derived the label fiber from the telescoping product QP^N and the uniqueness of P.
- Constructed common-intersection witnesses for every admissible rank.
- Recomputed the Grassmannian/positive-form/stabilizer dimension count and the N=2 consistency check.
- Separated the standard singular polar-factor nonuniqueness from the new closure-incidence classification.

## Literature and repository prior-art boundary

- https://arxiv.org/abs/2609.20159 — Kotwal–Menon source defining the closure cover and proving qualitative overlap at rank-deficient points.
- https://doi.org/10.26300/bd6x-0503 — Kotwal 2026 Brown dissertation; relevant background but not inspected in full during this run.

## Limitations

- The result is set-theoretic/differential-topological on fixed-rank strata; it does not prove calibrated-current extension, local analytic normal forms, intersection multiplicities, or angles.
- Kotwal's 2026 Brown dissertation was not inspected in full and remains a same-author originality risk.
- The motivating preprint is very recent, so later revisions or parallel observations may overlap.

## Repository identity

The assigned source-tree SHA `7294aadef22543840e8e86c2c9aabe680592efe6` matched the current tree at the audited path after comparing the assignment inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6` with the source-tree checked commit `253a0fe5d0217455660a277f9adb940030e567ad`; none of the intervening changed files touched this record. GitHub was read only during the audit.
