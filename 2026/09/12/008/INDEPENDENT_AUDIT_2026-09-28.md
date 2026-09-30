# Independent Audit — 2026/09/12/008

**Audit date:** 2026-09-28 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `d95fb64e885b48d6aa2ebf814b6fbda054fa5d2e`  
**Audited current source tree:** `d95fb64e885b48d6aa2ebf814b6fbda054fa5d2e`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** repaired

The current `main` record tree matches the assigned tree SHA.

## Correctness

PASS ONLY AFTER MAJOR REPAIR. The original six “classical-BG-admissible” positive-alpha walls are incorrect because only Delta(F) was checked. For Q=G-F=(-3,0,-3-d_F), Delta(Q)=-60(d_F+3); combining Delta(Q)>=0 with alpha^2=(d_F+3)/15>=0 leaves only d_F=-3 at alpha=0. Thus no positive-alpha rank-two equal-Im wall survives the necessary two-factor BG test, and the E^vee quotient has Delta=-240.

## Originality

SUPPORTED AS A CORRECTED NARROW LEMMA. Existing GM conic-moduli and Serre-invariant-stability sources do not state this two-factor beta=0 discriminant exclusion in the submitted coordinates. The repair sharply limits the claim to this numerical sector.

## Scientific value

USEFUL NEGATIVE RESULT. Eliminating the entire rank-two equal-Im sector corrects a misleading candidate-wall picture and materially narrows the remaining beta=0 analysis to tilt-heart placement, Im=0/torsion behavior, and other sectors.

## Independent checks

- direct derivation of alpha^2=(d_F+3)/15
- direct computation Delta(F)=100-40d_F and Delta(Q)=-60(d_F+3)
- E^vee quotient check Delta=-240
- current main tree equals assigned tree

## Limitations

- Full beta=0 wall-freeness is not proved.
- Tilt-heart placement of G is conditional; Im=0/torsion and other numerical sectors remain open.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/12/008
- https://arxiv.org/abs/2012.12193
- https://doi.org/10.1002/mana.202200010

This audit changes only the independent-audit channel in `VERIFICATION.md`; Lean verification and expert attestation remain unchanged.
