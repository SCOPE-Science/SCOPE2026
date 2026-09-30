# Independent Audit — Coefficient transport removes the characteristic-two restriction in Promislow unit localization

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `28846f77ef87c6d9dabb1130e76e7676c1392f56`  
**Audited current source tree:** `28846f77ef87c6d9dabb1130e76e7676c1392f56`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree is unchanged from the dispatcher-audited source tree. GitHub was used read-only as evidence; this staged change set is not claimed to be already published.

## Correctness — PASS

PASS. The coefficient-sum coarsening lemma is correct: if each exact old product fiber remains monochromatic after moving supports, every new product fiber is a union of whole old fibers, so the old coefficient sums 1 at the anchored identity fiber and 0 elsewhere survive arbitrary mergers over any field. Applying this to the Promislow normal-form equality system transports the original nonzero coefficient lists unchanged while the prior small-integer compression moves only support coordinates. Pairwise support distinctness preserves total support. The resulting relation alpha beta=1 is two-sided because the Promislow group is virtually abelian, hence sofic, and group algebras of sofic groups over fields are directly finite. The finite-field decidability and least-support computability consequence follows because the bounded ball and coefficient set are finite and nontrivial units are known in every positive characteristic.

## Originality — PASS

PASS, with a source-access qualification. Tabei's 2026 abstract explicitly presents the effective localization theorem only over F_2 and identifies parity coarsening as its new ingredient. The submitted weighted-fiber transport removes precisely that characteristic-two dependence without changing the geometric support-compression input. Searches for an arbitrary-field coefficient-preserving Promislow localization theorem with radius depending only on total support did not locate a prior equivalent statement. Murray's arbitrary-positive-characteristic units and older virtually-abelian property-(U) work are materially different inputs/results.

## Scientific value — PASS

PASS. Extending effective localization from F_2 to every field converts a characteristic-specific finite-localization result into a coefficient-independent structural theorem and yields a finite decision procedure for every finite field. The new argument is short, but it removes the only algebraic obstruction in a recent computability theorem and preserves its support bound and support size.

## Independent checks

- Independently proved the coefficient-sum coarsening lemma for arbitrary mergers of exact old product fibers.
- Checked that exact old-fiber equalities and the identity anchor are field-independent integer equations in the moved support variables; retaining the old coefficients then reconstructs the unit equation.
- Checked the direct-finiteness step via virtual abelianness/soficity and the finite-field enumeration argument.
- Compared the result with Tabei's public F2 localization statement, Murray's positive-characteristic existence theorem, and older virtually-abelian group-ring work.
- Verified no assigned-path file changed between the dispatcher source-check commit and current audited main.

## Limitations

- The web retrieval layer exposed Tabei's abstract but not the full arXiv body during this run; no claim is made to have line-by-line read the inaccessible body. The audit independently checked the weighted transport step and the field-independence of the equality constraints used by the submitted proof.
- The exact geometric compression radius D_u(n) itself is inherited from Tabei and is not newly derived here.
- Over infinite fields, bounded support does not make coefficient search finite; the computability corollary is only for finite fields.

## Evidence and references

- https://arxiv.org/abs/2609.17559
- https://arxiv.org/abs/math/0305440
- https://arxiv.org/abs/2106.02147
- https://doi.org/10.1016/j.jalgebra.2013.07.014
- https://arxiv.org/abs/2303.02823
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/promislow-unit-localization-over-arbitrary-fields--7ba3ec8aec00

This change set updates only the independent-audit channel. Lean verification and expert attestation are preserved exactly as previously recorded.
