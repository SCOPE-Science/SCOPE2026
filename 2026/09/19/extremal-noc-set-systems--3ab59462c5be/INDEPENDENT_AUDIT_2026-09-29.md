# Independent Audit — 2026-09-29

**Record:** `2026/09/19/extremal-noc-set-systems--3ab59462c5be`  
**Disposition:** **PASSED**

## Correctness

**PASS** — The equality argument is sound. Equality in the published levelwise bound forces every k-level to be a full sunflower with a (k-1)-element core Y_k. The NOC witness condition between consecutive saturated levels forces Y_k⊂Y_{k+1}, hence a maximal chain of cores and exactly the ordered family in the record. The converse witness x_j works directly. I independently exhaustively enumerated all set systems for n=1,2,3,4 and reproduced maximum sizes 1,3,6,10 and extremizer counts 1,1,3,12, matching n!/2 for n≥2. The adjacent-level Hasse count also gives n(n-1) arcs; the only ambiguity in the recovered order is the last two labels.

## Originality

**PASS** — The current Lindeberg–Hellmuth preprint proves the sharp n(n+1)/2 bound and gives the ordered construction as a sharpness example, but does not state the nested-core equality classification or the n!/2 labeled count. Its concluding discussion treats enumeration of NOC clustering systems as a future direction. Targeted searches under NOC, inclusion-visible, strict-compatible, private-element, and sunflower terminology did not locate an equivalent theorem. This is evidence rather than a guarantee; older set-system literature under different terminology remains a residual risk.

## Scientific value

**PASS** — The record upgrades a sharp numerical bound with one construction to a rigidity theorem, an exact labeled enumeration, and explicit structural counts for the canonical regular normal realizations. That is a meaningful structural strengthening rather than a cosmetic reformulation.

## Evidence checked

- Lindeberg and Hellmuth, NOC NOC, who's there? Clustering systems of tree-child and normal networks: https://arxiv.org/abs/2609.13336 — Current public preprint used to check the sharp bound, sharpness construction, network transfer, and open enumeration direction.
- Alcalà, Llabrés, Rosselló, and Rullan, Tree-Child Cluster Networks: https://doi.org/10.3233/FI-2014-1087 — Background strict-compatibility literature; no exact equality classification located in the accessible material/search evidence.

Repository evidence was read at inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6` / source-check commit `253a0fe5d0217455660a277f9adb940030e567ad`. A later repository-head comparison through `eff2c6312cec5b0dee5115e5f42211a853092dfb` found no changes under this record path, so the assigned source-tree SHA `47c788def3e922430a5aceace96ae1e81c0aae01` is the tree audited. GitHub was used only as read-only evidence.

## Limitations

- No near-extremal stability theorem is audited here.
- Search evidence cannot exclude older equivalent extremal-set-system language that was not indexed under the terms checked.
- Finite enumeration through n=4 is corroboration, not a substitute for the general proof.

## Audit conclusion

This independent audit is scientifically complete on correctness, originality, and value. The record may remain at its source path without substantive research-file edits.
