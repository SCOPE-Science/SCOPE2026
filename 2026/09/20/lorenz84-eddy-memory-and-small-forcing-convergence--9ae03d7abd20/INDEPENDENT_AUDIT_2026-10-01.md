# Independent audit — 2026-10-01

## Record

**Stationary eddy-energy law and a small-forcing convergence criterion for Lorenz-84**

Final claim: Every bounded complete Lorenz-84 trajectory obeys an exact exponentially weighted past-eddy-energy law, every compactly supported invariant measure obeys \(\mathbb E[R\mid X]=a(F-X)\), and for \(F<1\) the stated explicit small-forcing inequality forces the global attractor to be a single equilibrium.

Disposition: **PASSED**

## Correctness — PASS

Fresh derivation verifies \(\dot U=R-aU\), the backward memory formula, the invariant-measure generator identity, covariance and variance consequences, the \(F<1\) eddy bound, and the two-complete-trajectory contraction. Independent algebra reproduced the scalar-filter and total-energy identities.

## Originality — PASS

Lorenz-84 literature located on dissipation/energy transfer, attractor geometry, nonautonomous dynamics and invariant-measure moment matrices does not imply the exact conditional law plus the explicit nonzero-forcing contraction criterion. Gallo–Anselmi–Lazzari use an invariant-measure moment matrix for identifiability, a different statement; Pelino–Pasini discuss geometric dissipation and energy transfer.

Equivalent-formulation, broader-coverage, exact-database/table, and claim-versus-prior implication checks are recorded in the companion JSON audit. Primary-source inspections and residual access risks are also recorded there.

## Scientific value — PASS

The conditional eddy-energy law is an exact invariant-measure diagnostic for a standard atmospheric model, and the contraction inequality excludes all competing compact recurrent dynamics in an explicit nonzero-forcing region.

## Checked scientific sources

- Lorenz, Irregularity: a fundamental property of the atmosphere, Tellus A 36 (1984).
- Pelino–Pasini, Dissipation in Lie-Poisson systems and the Lorenz-84 model, Physics Letters A 291 (2001), DOI:10.1016/S0375-9601(01)00764-2.
- Gallo–Anselmi–Lazzari, Attractor Geometry Determines the Identifiability Limits of System Discovery, arXiv:2607.18490.
- Naser–Abdel Aal–Gumah, DOI:10.1007/s40324-026-00429-8.
- Published-record semantic search for Lorenz-84 invariant-measure and global-convergence statements.

## Residual risks

- The full Pelino–Pasini article was not available through the inspected lawful route; only its institutional abstract was read.
- The full Gallo–Anselmi–Lazzari preprint was not available through the inspected route; its detailed abstract and secondary technical summary were read.
- The sufficient global-convergence inequality is not claimed sharp.

## Verification boundary

The audit reconstructed the argument and performed fresh algebraic or logical checks where needed. Existing package logs were treated as supporting evidence only. No formal proof-assistant or expert attestation is asserted.
