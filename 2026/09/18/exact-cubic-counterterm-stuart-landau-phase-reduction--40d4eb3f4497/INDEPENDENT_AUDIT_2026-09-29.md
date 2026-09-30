# Independent audit — Exact cubic counterterm cancels the full second-order phase correction in a Stuart–Landau triad

**Audit date:** 2026-09-29 (UTC)
**Source path:** `2026/09/18/exact-cubic-counterterm-stuart-landau-phase-reduction--40d4eb3f4497`
**Audited tree:** `1c259797b609601a45ce0c7621ca32eeb83f9459`

## Disposition

**PASSED.** The record survives independent review on correctness, originality, and scientific value without a substantive research-file change.

## Correctness

The counterterm identity is correct under the source's stated straight-isochrone triad assumptions. On the radius sqrt(a), each cubic monomial C z_p z_q conjugate(z_r) contributes a Im(C exp(i(theta_p+theta_q-theta_r-theta_i))) to the target phase. Term-by-term projection of Q_i exactly reproduces the source Eq. (55), so the physical coefficient -epsilon^2/(4a^2) contributes -f_i^(2). Because the added term starts at epsilon^2, evaluation on the order-epsilon torus deformation first changes order epsilon^3. The omitted pairwise resonant monomial z_j^2 conjugate(z_i) indeed produces the required second harmonic.

### Independent checks

- Matched every harmonic in the source Eq. (55) to a term in Q_i, including constant sin(2 rho), shifted pairwise, asymmetric three-body, and symmetric three-body terms.
- Verified global phase equivariance: each degree-(2,1) cubic monomial transforms by the same e^{i psi} factor as z_i.
- Independently evaluated the source phase correction plus the proposed counterterm on a 5^3 phase grid for all three targets with nonsymmetric signed weights; the maximum residual was 4.440892098500626e-16.
- Checked perturbative bookkeeping: the epsilon^2 physical term cannot alter the epsilon first-order phase coupling, and its off-torus correction starts at epsilon^3.
- Inspected the source cubic enumeration and restricted cancellation discussion; the pairwise second-harmonic monomial is allowed by the general formula but absent from the listed nonlinear-pairwise cases.

## Originality

PASS to the best of current searchable knowledge. The primary source arXiv:2609.20632 was independently inspected in full text: it writes the general resonant cubic monomial, then lists only two nonlinear-pairwise cases and uses a restricted physical-nonpairwise design that it describes as necessarily partial. The source-specific monomial z_j^2 conjugate(z_i) and complete order-epsilon^2 counterterm are not stated there. General synchronization engineering and phase-harmonic synthesis are established background and are excluded from novelty.

### Literature checked

- https://arxiv.org/abs/2609.20632 — Muolo–Nakao–Bick, primary second-order Stuart–Landau calculation and restricted coupling-design discussion.
- https://doi.org/10.1063/1.2927531 — Kori et al. (2008), established synchronization-engineering background; not claimed as new.
- https://doi.org/10.1088/2632-072X/abbed2 — Gengel et al. (2021), established higher-order phase-reduction background.

## Scientific value

The result changes the interpretation of the source's partial-compensation limitation: within the enlarged globally phase-equivariant resonant-cubic basis, the entire explicit second-order phase correction can be canceled, recovering the first-order model through order epsilon^2. The missing second-harmonic control direction is explicit and directly implementable at the model level.

## Limitations

- Cancellation is perturbative through order epsilon^2, not an exact finite-coupling conjugacy.
- The explicit formula is tied to the source's three-oscillator, straight-isochrone c=-1,d=0 setting.
- No order-epsilon^3 bound, robustness analysis, or laboratory realizability of arbitrary complex cubic coefficients is established.

## Publication guard

This audit is scoped to the exact source-tree SHA above. The guarded change-set adds this independent-audit evidence pair and updates only the independent-audit channel in `VERIFICATION.md`; Lean and expert-attestation channels are preserved unchanged.
