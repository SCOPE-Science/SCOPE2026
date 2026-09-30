# Independent Audit — Unit groups exactly detect pro-star-reversibility

**Audit date:** 2026-09-29 (UTC) (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `a0d87dada0b7ddb312be2792d372928e3eba38a1`  
**Audited current source tree:** `a0d87dada0b7ddb312be2792d372928e3eba38a1`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record path is unchanged from the dispatcher's source-check commit, so the audited tree equals the assigned source tree. GitHub was used only as read-only evidence. The UTC-dated independent-audit marker files were absent when this guarded change set was prepared.

## Correctness — PASSED

PASS. The necessity is immediate: if u is a unit, applying pro-*-reversibility to uu^{-1}=1 makes (u*)^{-1}u an invertible projection, hence 1, so u*=u. For the converse, the classical fact that every *-reversible ring is reversible is available in Fakieh's Proposition 6; reversible rings have central idempotents and if ab is idempotent then ba=ab. With p=ab and e=1-p, the elements u=pa+e and v=pb+e are mutual inverse units. Pointwise fixation of units yields pa*=pa and pb*=pb; *-reversibility kills the complementary e-corner and gives b*a=p. This proves the exact iff and the stronger identity. The stated consequences for abelian units, J(R), clean/semiperfect rings and division rings then follow.

## Originality — PASSED

PASS, but only for the headline exact criterion. An earlier SCOPE record from 2026-09-18 (`pro-star-reversible-semiperfect-rigidity--8cd8850c47f1`) already contains unit self-adjointness, abelianity of the unit group, local/semiperfect collapse, the domain criterion and related examples; those are not credited again. The present 2026-09-19 record adds the genuinely stronger global equivalence `pro-*-reversible iff *-reversible plus every unit self-adjoint` and the identity b*a=ab for every projected product. Chen--Wang--Zou's source introduces pro-*-reversibility and studies basic characterizations, but targeted searches did not locate this exact unit-group iff. Fakieh's older paper supplies the prior fact *-reversible=>reversible, not the new pro-* criterion.

## Scientific value — PASSED

PASS, narrowly. The exact iff completely identifies the obstruction to the converse question from *-reversibility to pro-*-reversibility: among *-reversible rings, the only additional requirement is pointwise fixation of units. That is a meaningful strengthening beyond the earlier SCOPE necessity/local/domain results, even though most of the record's corollaries duplicate that earlier archive entry. Scientific credit is therefore confined to the global characterization and stronger projected-product identity.

## Independent checks

- Reproved the unit necessity directly.
- Checked the converse using the established prior theorem that every *-reversible ring is reversible and the standard central-idempotent consequences of reversibility.
- Verified the unit construction u=pa+e, v=pb+e and the final p/e-corner decomposition yielding b*a=p.
- Compared in full with earlier SCOPE record `2026/09/18/pro-star-reversible-semiperfect-rigidity--8cd8850c47f1`, published 2026-09-18T22:24:04Z; its overlapping corollaries are explicitly excluded from novelty credit.
- Compared with Chen--Wang--Zou arXiv:2609.20076 and Fakieh 2013; targeted searches found no earlier exact global unit-group iff.
- Verified via GitHub compare that the assigned record path did not change from the dispatcher source-check commit to current main; the dated audit pair is absent and VERIFICATION.md is unchanged.

## Limitations

- Most structural corollaries in this record are not original relative to the earlier 2026-09-18 SCOPE record and receive no independent scientific credit here.
- The proof uses prior reversible/*-reversible ring structure; those facts are not new.
- Because pro-*-reversibility is a very recent notion, concurrent unindexed observations remain a residual risk.

## Evidence and references

- https://arxiv.org/abs/2609.20076
- https://doi.org/10.1155/2013/650702
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/pro-star-reversible-semiperfect-rigidity--8cd8850c47f1
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/19/unit-group-criterion-pro-star-reversibility--dcd6bac06405

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
