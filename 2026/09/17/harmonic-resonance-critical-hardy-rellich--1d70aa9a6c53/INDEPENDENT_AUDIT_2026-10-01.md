# Independent scientific audit — SCOPE-20260917-1d70aa9a6c53

Date (UTC): 2026-10-01

## Final claim

For the weighted critical Hardy--Rellich functional in the record, the Hessian estimate holds exactly away from weights a=0 and a=N. For the Laplacian estimate, logarithmic cutoffs of homogeneous harmonic modes force failure at every resonant weight a=N(1-beta), including both endpoints of the relevant Muckenhoupt interval; inside that interval the corrected validity set excludes precisely a=0 and a=N.

## Correctness

**PASS** — The logarithmic-cutoff calculation was reconstructed. For a harmonic homogeneous mode of degree beta, choosing weight a=N(1-beta) makes the radial power exactly dr/r. The left functional grows linearly with the logarithmic plateau length while the weighted Laplacian or affine-Hessian transition term is of order L^(1-N), forcing failure. Castro's revised primary paper independently confirms that the unweighted a=0 case is false. Majdoub's direct Hessian estimates cover a outside {0,N}; its original inclusion of a=0 relied on the superseded unweighted claim. These pieces establish the exact Hessian classification and the stated endpoint failures.

## Originality

**PASS** — The record explicitly credits Castro for the a=0 counterexample and Majdoub for the positive weighted estimates. Targeted searches found no prior source stating the full harmonic-resonance family for this specific critical functional or both Muckenhoupt-endpoint consequences. McOwen's classical weighted-Sobolev work is a genuine broader-context risk and was not inspected in full, so originality is best-of-knowledge and limited to this functional and correction.

### Equivalent formulations

The component a=0 obstruction is prior and credited, but the full resonance family and combined corrected range were not found as an equivalent earlier statement.

### Broader coverage

Broader theory is a residual originality risk but did not furnish a decisive implication in the material actually inspected.

### Exact database or table

The result is an analytic obstruction theorem, not a tabulated computation.

### Claim versus prior implication

Known components imply part of the corrected statement but not the full infinite resonance conclusion.

## Scientific value

**PASS** — The result corrects a recent sharp-range claim, supplies the exact Hessian exceptional set, resolves both boundary cases of an explicitly raised Laplacian-range question, and organizes the failures into an infinite harmonic-resonance family. These are motivated structural corrections rather than arbitrary examples.

## Source inspections

- **A critical Hardy--Rellich inequality** — https://arxiv.org/abs/2511.16537. Accessible revised theorem and counterexample discussion, including cutoff approximations of the linear function Assessment: PARTIAL_COVERAGE. The revision explicitly makes the unweighted case false and supplies the a=0 obstruction.
- **An extension of a critical Hardy--Rellich inequality: explicit constants and the sharp weight range** — https://arxiv.org/abs/2606.15668. Accessible theorem/proof material including the separate a=0 and a=N degeneracies and weighted Calderón--Zygmund range Assessment: PARTIAL_COVERAGE_WITH_CORRECTION. Its direct Hessian estimates exclude 0 and N; its treatment of a=0 relies on the older unweighted theorem superseded by Castro v4.
- **The behavior of the Laplacian on weighted Sobolev spaces** — https://doi.org/10.1002/cpa.3160320604. Bibliographic metadata and secondary descriptions only; full text not inspected in this run Assessment: RESIDUAL_RISK. It is plausibly relevant to the general resonance mechanism but was not shown to imply the exact functional audited here.
- **Harmonic-resonance obstructions for weighted critical Hardy--Rellich inequalities** — https://github.com/Resultary/2026/tree/main/2026/9/17/SCOPE-harmonic-resonance-critical-hardy-rellich--1d70aa9a6c53. Title and summary Assessment: SELF_MATCH. Exact same claim.

## Limitations and residual risks

- The record does not characterize all nonresonant Laplacian weights outside the Muckenhoupt interval. Classical weighted elliptic Fredholm theory may contain broader versions of the resonance mechanism.
- McOwen (1979) was not inspected in full; a broader classical formulation could reduce the originality of the resonance mechanism.
- The Laplacian result is intentionally not a complete classification outside the Muckenhoupt interval.

## Disposition

**PASS**
