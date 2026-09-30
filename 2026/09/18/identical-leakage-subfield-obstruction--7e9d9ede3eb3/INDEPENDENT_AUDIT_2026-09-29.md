# Independent Audit — Identical linear leakage cannot exploit computations over its stabilizer field

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned/current source tree:** `fda0006521b607cb95e6ab66c48cad5fa0e8827b`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The inventory-snapshot and current-main directory entries match exactly by child Git blob/tree SHA, so the assigned source-tree SHA remains the current tree audited. GitHub was used read-only as evidence.

## Correctness — PASSED

PASS. For a B-linear leakage map, its kernel is a B-subspace. The multiplier stabilizer S_j is closed under addition and multiplication, and finiteness of the ambient B-space turns aK_j⊂K_j for nonzero a into equality, hence closure under inversion; S_j and their intersection are subfields. Any a in S_j induces a well-defined B-linear endomorphism of the leakage image satisfying T_{j,a}(ell_j(x))=ell_j(ax). Therefore every computed leakage with coefficients in S is a B-linear function of input leakages. Systematicity gives deterministic equivalence in the other direction, and the stated base/product exact-repair equivalence follows by zeroing the other independent input codewords. For one-symbol finite-field trace leakage, preservation of the kernel forces the induced quotient action to be scalar over B; nondegeneracy of the finite-field trace pairing then gives a in B, so the stabilizer is exactly B. The Kronecker rank factorization for a base-field computation matrix is standard and yields the asserted equivalence of the source rank criteria.

## Originality — PASSED

PASS, narrowly scoped. Aoutouf–Augot study leakage under linear computations and already analyze addition and identical-leakage phenomena, so neither the coding framework nor the observation that some computations add no leakage is new. The surviving contribution is the general stabilizer-field theorem: it handles arbitrary finite-dimensional B-linear leakage maps, arbitrary systematic linear computations whose coefficients lie in the common stabilizer, and proves exact deterministic equivalence with input leakage; for trace leakage it identifies the obstruction field exactly as B. The motivating source's public statement does not formulate this kernel-stabilizer boundary or the resulting all-base-field-circuits iff theorem.

## Scientific value — PASSED

PASS. The theorem turns isolated no-improvement examples into an exact structural obstruction and cleanly separates computations that are information-theoretically incapable of helping identical leakage from those that at least escape the obstruction. The trace specialization gives a practically interpretable necessary condition—some coefficient must leave the base field—while correctly avoiding the stronger and false claim that such a coefficient is sufficient.

## Independent checks

- Reproved that each leakage-kernel stabilizer is a subfield and that multipliers descend to the quotient/leakage image.
- Re-derived the deterministic equivalence of full computed-block leakage and input-block leakage for coefficients in the common stabilizer.
- Rechecked the finite-field trace specialization using nondegeneracy of the trace pairing.
- Rechecked the base-field Kronecker rank factorization and its use in the cited rank-gap criterion.
- Compared the theorem against Aoutouf–Augot arXiv:2609.19929 and the earlier exact-repair construction, crediting only the stabilizer-field generalization.
- Verified inventory-snapshot and current-main record entries are byte-identical by child Git blob/tree SHA.

## Limitations

- The obstruction assumes the same leakage map at each share position is reused across computation blocks.
- For vector-valued leakage the stabilizer may strictly contain the base field; the theorem correctly uses the common stabilizer rather than B itself.
- A coefficient outside the stabilizer is only an opportunity for new leakage, not a sufficient condition for a successful repair/leakage attack.
- The motivating preprint is very recent, so near-simultaneous follow-up work remains a residual priority risk.

## Evidence and references

- https://arxiv.org/abs/2609.19929
- https://wcc2026.inria.fr/assets/final_versions/WCC2026_paper_33.pdf
- https://doi.org/10.1145/2897518.2897525
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/identical-leakage-subfield-obstruction--7e9d9ede3eb3

This staged audit changes only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
