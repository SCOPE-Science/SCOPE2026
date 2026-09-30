# Independent Audit — Sharp off-critical powers for discrete Fourier trace defects

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `75f7d104d4a785145611ec909ba932e2d517ce79`  
**Audited current source tree:** `75f7d104d4a785145611ec909ba932e2d517ce79`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assigned source-tree SHA. GitHub was used read-only as evidence, and the dated independent-audit marker files were absent when this guarded change set was prepared.

## Correctness — PASS

PASS. The balanced q-adic branching gives M_l asymptotic to q^{(1-alpha)l}; separated retained cylinders therefore yield boundary-neighborhood measure comparable to r^alpha. Alternating odd/even gap membership gives a matching translation discrepancy at h=q^{-l} along odd l. At scale R=q^{l+1}, gap endpoints become lattice points and each selected gap has at least q lattice-unit length, producing a unit-shift symmetric difference of order R^{1-alpha}. For gamma<eta a single nonzero Fourier coefficient of the smooth spectral box gives R^{d-gamma}; for gamma>eta Parseval and |e^{2 pi i m/N}-1|^2 <=4 pi^2 min(1,|m|/N) give D_N >= N|E△(E-1/N)|/(4 pi^2), hence R^{d-eta}. These match Mayeli's off-critical upper powers along explicit scale sequences.

## Originality — PASS

PASS. Mayeli's indexed full text explicitly says in Remark 9.4 that sharpness of both off-critical powers remained open and labels the Section 10 Cantor computations numerical evidence, not proof. This record was first committed at 02:26 UTC on 2026-09-19, before the later all-fractional SCOPE record that subsumes it. Searches across rough-domain trace-defect and concentration-operator literature did not locate an earlier proof of both discrete off-critical lower powers. Moran-set and Parseval ingredients are standard and are not credited as new.

## Scientific value — PASS

PASS. The theorem resolves the complete off-critical portion of the source's sharpness question and shows that the rougher of the spatial/spectral exponents alone can force the upper power while the other side is smooth. Although a later same-day SCOPE record strengthens it to all scales and the critical line, this record retains independent priority and clear value as the first archive resolution of the off-critical problem.

## Independent checks

- Read Mayeli arXiv:2609.12226v1 from lawful indexed HTML; Remark 9.4 explicitly leaves both off-critical powers open and Section 10 calls the Cantor scaling tests numerical evidence.
- Re-derived the Moran cylinder counts and two-sided boundary-neighborhood exponent.
- Checked the odd-level translation lower bound and the lattice endpoint scaling argument.
- Checked the gamma<eta single-frequency trace lower bound and the gamma>eta Parseval inequality.
- Verified repository chronology showing this result predates the broader all-fractional SCOPE record by about eighteen hours.
- Compared with Hughes--Israel--Mayeli and Marceca--Romero--Speckbacher; their public scopes do not state the submitted discrete off-critical sharpness theorem.
- Verified the current main record tree equals the assigned source-tree SHA and the 2026-09-30 audit markers are absent.

## Limitations

- Lower bounds are along explicit lacunary sequences, not all-scale two-sided asymptotics.
- The record does not address the fractional critical logarithm; a later SCOPE record does.
- The smoother member of each construction has stronger regularity than the prescribed larger exponent, which is sufficient for class-level sharpness.
- The source preprint is recent, so unindexed simultaneous work remains a residual risk.

## Evidence and references

- https://arxiv.org/abs/2609.12226
- https://arxiv.org/html/2609.12226v1
- https://arxiv.org/abs/2607.02996
- https://arxiv.org/abs/2301.11685
- https://doi.org/10.1007/s00205-024-01979-9
- https://github.com/SCOPE-Science/SCOPE2026/commit/3d82b5ae508946c477a9570c4b3d37c716f6b411
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/19/sharp-off-critical-discrete-fourier-trace-defect--dc7870b56a90

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
