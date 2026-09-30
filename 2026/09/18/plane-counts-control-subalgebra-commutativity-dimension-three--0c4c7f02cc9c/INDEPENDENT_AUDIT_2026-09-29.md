# Independent audit — Plane counts control subalgebra commutativity in dimension three

**Audit date:** 2026-09-29 (UTC)
**Source path:** `2026/09/18/plane-counts-control-subalgebra-commutativity-dimension-three--0c4c7f02cc9c`
**Audited tree:** `dc70b09b34f0eed16bbccfb50d2e522bc32e7f93`

## Disposition

**PASSED.** The record survives independent review on correctness, originality, and scientific value without a substantive research-file change.

## Correctness

**PASS.** The universal formula is a correct incidence count: in dimension three only two distinct line subalgebras can fail to permute, and they permute exactly when their spanning plane is a Lie subalgebra. The factorization number follows from a separate exhaustive count. In the solvable case, every three-dimensional algebra has a two-dimensional abelian ideal and plane counts reduce to projective eigenlines of a 2x2 adjoint action. In the perfect case the bracket matrix is invertible and symmetric; Lie-subalgebra planes are the q+1 projective zeros of the resulting quadratic form in odd characteristic and of a nonzero squared linear form in characteristic two.

### Independent checks

- Counted all ordered distinct line pairs N(N-1)=Nq(q+1) and subtracted the q(q+1) pairs contributed by each Lie-subalgebra plane.
- Independently enumerated F2 as pairs involving L, ordered distinct planes, and nonincident line--plane pairs, reproducing t^2+(2q^2+1)t+2q^2+2q+5.
- Derived t=1+q e(T) for a solvable decomposition Fx semidirect V and checked e(T) in {0,1,2,q+1}.
- Verified the perfect-case bracket matrix is symmetric from unimodularity and that a^T A a=0 is exactly the plane-closure condition.
- In characteristic two, checked a^T A a is the square of a nonzero linear form; in odd characteristic, a nonsingular projective conic has q+1 points.
- Symbolically substituted t=1,q+1,2q+1,N into the universal formulas and reproduced all displayed D_i and F2 values.

## Originality

**PASS.** PASS to the best of current searchable knowledge. Muhie--Otera--Russo introduce the subalgebra commutativity degree and treat Heisenberg examples, while Towers--Zuleta--Gutierrez already classify three-dimensional comaximal graphs and supply relevant plane counts. Those ingredients are prior art, but no located source states the universal plane-count formula for sd and F2, the equivalence with lattice cardinality, or the complete four-value classification over every finite field.

### Literature and chronology checked

- https://arxiv.org/abs/2609.19086 — Muhie--Otera--Russo, On the number of modular pairs in finite dimensional Lie algebras on finite fields, submitted 2026-09-16; introduces the invariant and specifically studies Heisenberg algebras.
- https://arxiv.org/abs/2605.09583 — Towers--Zuleta--Gutierrez, The comaximal graph of a finite-dimensional Lie algebra; classifies dimension at most three over finite fields and supplies prior structural plane-count information.
- https://arxiv.org/abs/2608.16575 — Towers--Zuleta--Gutierrez, follow-up on triangle counts and structural invariants for finite-field comaximal graphs.

## Scientific value

**PASS.** The record completely determines a newly introduced invariant in dimension three, explains the Heisenberg/perfect coincidence structurally, links it to factorization numbers and the comaximal graph, and gives sharp extremal values in every finite field characteristic.

## Limitations

- The classification is dimension-specific and does not extend automatically to dimension four or higher.
- The plane-count inputs in the solvable case overlap strongly with the earlier comaximal-graph classification; originality is in the new invariant formulas and synthesis, not those prior counts.
- The modular-pairs preprint is very recent and may be revised or independently extended.

## Publication guard

The current source tree on `main` matched the assignment tree `dc70b09b34f0eed16bbccfb50d2e522bc32e7f93` exactly during this audit. The guarded change-set records the independent-audit evidence and updates only the independent-audit channel in `VERIFICATION.md`; Lean and expert-attestation channels are preserved unchanged.
