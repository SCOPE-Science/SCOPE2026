# Independent Audit — Pro-star reversibility collapses on semiperfect rings

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `128cd24cdd8f9c5ab8b497ea689368c99204200c`  
**Audited current source tree:** `128cd24cdd8f9c5ab8b497ea689368c99204200c`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree is unchanged from the dispatcher-audited source tree. GitHub was used read-only as evidence; this staged change set is not claimed to be already published.

## Correctness — PASS

PASS. The unit argument is exact: applying pro-* reversibility to u u^{-1}=1 makes (u*)^{-1}u an invertible projection, hence 1, so every unit is self-adjoint. The idempotent calculation e*(1-e)=(1-e*)e then forces e*=e. Reapplying the defining condition to b*a after ab=0 makes (ba)* a projection; consequently ba is an idempotent with square zero and is zero, so R is reversible and its idempotents are central. For a local ring, x or 1-x is a unit, hence every element is self-adjoint and the anti-involution being the identity forces commutativity. In a semiperfect ring, a complete family of local primitive idempotents becomes central/self-adjoint, decomposing R into *-stable local factors and proving the claimed collapse. The domain criterion, k[x] example, and F4 Frobenius separation all check directly.

## Originality — PASS

PASS, narrowly scoped. Chen--Wang--Zou introduce pro-* reversibility and establish its basic relation to reversibility and *-reversibility, but their public 2026 statement does not contain the unit obstruction, local/semiperfect classification, domain criterion, or minimal F4 separation. Targeted searches for pro-* reversible units/local/semiperfect rings and older self-adjoint-unit formulations found only related clean-type results under extra hypotheses, not this classification. Standard semiperfect decomposition and reversible-ring facts are not credited as new.

## Scientific value — PASS

PASS. The result gives an exact structural classification on a broad standard class (semiperfect rings), identifies a sharp boundary via domains with nontrivial involution, and supplies a smallest finite separation from *-reversibility. For a newly introduced ring property, this materially clarifies what the definition permits rather than adding isolated examples.

## Independent checks

- Re-derived unit rigidity and verified that the resulting unit group is abelian.
- Rechecked the idempotent self-adjointness and reversibility calculations, including the second use of the defining implication.
- Reconstructed the semiperfect decomposition through central local idempotents and checked passage of the property to each factor.
- Checked the domain converse, direct-finiteness step, k[x] involution example, and F4 minimal separation.
- Compared the claim with Chen--Wang--Zou 2026 and targeted older self-adjoint-unit/clean-ring literature.
- Verified no file under the assigned record changed between the dispatcher source-check commit and audited current main.

## Limitations

- The originality claim is limited to the new pro-* property; semiperfect-ring decomposition and standard reversible-ring lemmas are prior art.
- Related literature where self-adjoint units force a trivial involution under clean-type hypotheses exists; no claim is made that the raw unit observation is unprecedented under every older terminology.
- The motivating preprint is very recent, so contemporaneous unindexed work remains a residual priority risk.

## Evidence and references

- https://arxiv.org/abs/2609.20076
- https://doi.org/10.1112/S0024609399006116
- https://www.eiris.it/ojs/index.php/ratiomathematica/article/download/1144/pdf
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/pro-star-reversible-semiperfect-rigidity--8cd8850c47f1

This change set updates only the independent-audit channel. Lean verification and expert attestation are preserved exactly as previously recorded.
