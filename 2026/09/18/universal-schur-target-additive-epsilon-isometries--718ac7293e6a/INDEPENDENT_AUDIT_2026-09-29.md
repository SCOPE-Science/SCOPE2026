# Independent Audit — A single Schur target universal for additive epsilon-isometries

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `3270a24c00776b8e72258585058357e31723f8ed`  
**Audited current source tree:** `3270a24c00776b8e72258585058357e31723f8ed`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assignment tree SHA. GitHub was used read-only as evidence. The dated independent-audit marker files were absent when this guarded change set was prepared.

## Correctness — PASSED

PASS. Let U=C[0,1] and rho(u,v)=max{||u-v||,sqrt(||u-v||)}. The gauge is continuous, increasing, subadditive, strongly normalized, and nontrivial; Kalton's theorem therefore gives the Schur property for Y=F(U,rho), and separability follows from separability of U. Banach--Mazur gives an isometric linear embedding J_X:X->U for every separable real Banach X. With c=4epsilon, the free-space metric identity gives ||f(x)-f(y)||=max{r,2sqrt(epsilon r)}, so the distance excess is in [0,epsilon], reaches epsilon at r=epsilon for nonzero Banach X, and yields injectivity, a 1-Lipschitz inverse on the range, and uniform continuity. Godefroy--Kalton linearization then excludes every separable non-Schur X from embedding isometrically into the Schur target Y. The pointed metric-space extension through F(M) is also valid.

## Originality — PASSED

PASS, narrowly scoped. Sun--Zhang's full open arXiv text proves the construction only for a fixed pair, explicitly taking X=l2 and Y=F_omega(l2). It already contains the gauge, exact distance formula, Schur argument, and isometric-linearization obstruction. The audited contribution changes the quantifiers by putting the construction over the classical Banach--Mazur universal host C[0,1], producing one target independent of the separable domain and extending the statement to all pointed separable metric spaces. Targeted searches did not locate this single-Schur-target formulation. No novelty is credited to Banach--Mazur, Kalton, Godefroy--Kalton, or Lipschitz-free linearization individually.

## Scientific value — PASSED

PASS. Although the proof is a short synthesis of strong existing ingredients, the quantifier strengthening is substantial: one fixed separable Schur Banach space admits arbitrarily accurate one-sided additive embeddings of every separable Banach space while still excluding exact isometric copies of every non-Schur one. The metric-space extension makes the universality statement structurally clear.

## Independent checks

- Read Sun--Zhang's lawful open arXiv HTML in full around Theorem 1.5 and Section 3; their target is explicitly F_omega(l2) and their domain X is l2.
- Rechecked subadditivity and normalization of omega(t)=max{t,sqrt(t)}.
- Recomputed the exact scaled free-space distance formula and the sharp epsilon excess at r=epsilon.
- Checked Banach--Mazur isometric universality of C[0,1] and the separability of the resulting Lipschitz-free target.
- Checked the Godefroy--Kalton obstruction: an isometric embedding of a separable Banach space into Y produces a linear isometric copy, impossible for a non-Schur domain because Schur passes to closed subspaces.
- Checked the pointed separable metric extension through the canonical isometry M->F(M).
- Verified that the assigned record path did not change between the dispatcher source-check commit and current main and that the dated audit markers are absent.

## Limitations

- The construction is over real scalars as stated; no complex-linear universal analogue is certified here.
- The new step is a quantifier-strengthening synthesis, not a new Lipschitz-free-space or Schur theorem.
- An equivalent universal-target formulation under older epsilon-isometry terminology remains a residual literature-search risk.

## Evidence and references

- https://arxiv.org/abs/2609.13937
- https://doi.org/10.1344/CM.V55I2.4055
- https://doi.org/10.4064/sm159-1-6
- https://doi.org/10.4153/CMB-1971-023-1
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/universal-schur-target-additive-epsilon-isometries--718ac7293e6a

This change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
