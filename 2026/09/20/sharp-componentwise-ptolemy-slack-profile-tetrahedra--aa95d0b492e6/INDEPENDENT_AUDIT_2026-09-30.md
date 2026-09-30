# Independent Audit — Sharp componentwise Ptolemy-slack profile for tetrahedra

**Audit date:** 2026-09-30 (UTC) (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `005169f5b81cdbee27bff9743d2d6ef33d9d34b4`  
**Audited current source tree:** `005169f5b81cdbee27bff9743d2d6ef33d9d34b4`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record path has no changes from the assignment snapshot, so the audited tree equals the assigned source tree. GitHub was used read-only. The UTC-dated independent-audit files were absent when this guarded change set was prepared.

## Correctness — PASS

PASS. Crelle's triangle and Heron's formula give L σxσyσz=576R^2V^2 and σx+σy+σz=L, hence the normalized slack product and η≤4/27. The submitted disphenoid coordinates realize every positive probability vector: direct distance calculation gives opposite-edge products (1-p_i)/2, whose triangle slacks are exactly p_i. Fixing p_x=t leaves positive p_y,p_z exactly when t(1-t)^2≥η, yielding the complete interval between the two roots α(η),β(η); every interior value is realized by the same disphenoid construction. Finally, the centroid identity 16R^2=sum(edge^2)+16OG^2 and pairing opposite edges give the exact defect decomposition. Independent tests on 1,000 random tetrahedra verified the defect identity to relative error below about 10^-12.

## Originality — PASS

PASS, narrowly scoped. Crelle's theorem, the d3≥72V^2 tetrahedral inequality, Heron's identity, and the centroid/circumradius formula are established prior art. Mazur and Mazur–Petrenko already use the Crelle triangle in closely related volume inequalities. Targeted searches did not locate the submitted normalized-slack simplex surjectivity, the complete componentwise interval at fixed η with every value attained by disphenoids, or the exact E+16OG^2 defect formula in this packaged form. Because the derivations are elementary consequences of classical identities, older solid-geometry folklore remains a material but nondecisive residual risk.

## Scientific value — PASS

PASS. The result turns a scalar Crelle/Heron product inequality into a complete three-component feasible-region description and gives an explicit realization theorem, sharp one-component profile, asymptotically sharp simple lower bound, and transparent equality defect. This is a useful structural refinement even though its ingredients are classical.

## Independent checks

- Re-derived the normalized product identity from Crelle's triangle and factored Heron formula.
- Checked the disphenoid coordinate construction directly and verified that every positive probability vector is realized.
- Solved the fixed-component feasibility condition and recovered the exact interval t(1-t)^2≥η and the two root endpoints.
- Re-derived the simple lower bound σ_i≥2304R^2V^2/L^3 and its degenerating sharpness.
- Reconstructed the centroid/circumradius algebra leading to the exact defect identity.
- Numerically checked the defect identity on 1,000 random tetrahedra; maximum relative discrepancy was about 10^-12.
- Compared with Mazur–Petrenko, Mazur, and later Crelle-triangle inequality literature; no complete normalized-slack profile was located.
- GitHub comparison found no changes under the assigned record path; both dated audit files are absent and VERIFICATION.md retains the verified blob SHA.

## Limitations

- The theorem concerns nondegenerate Euclidean tetrahedra and opposite-edge-product Ptolemy slacks, not all six edge lengths.
- The exact defect identity is close to classical Crelle/centroid identities, so differently phrased older equivalents remain a residual originality risk.
- Degenerate tetrahedra appear only as limits.

## Evidence and references

- https://arxiv.org/abs/1102.4662
- https://doi.org/10.1080/00029890.2018.1411741
- https://doi.org/10.7153/jmi-2022-16-49
- https://doi.org/10.1080/00029890.2023.2285695
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/20/sharp-componentwise-ptolemy-slack-profile-tetrahedra--aa95d0b492e6

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
