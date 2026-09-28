# Independent audit — SCOPE-20260909-100

## Scope
Independent review of `2026/09/09/100` at tree `77c582ffdbcf25df85f30a920661f321c001a5f7`.

## Correctness
**REPAIR REQUIRED.** The numerical computation is reproducible, but the published phrase “validated principal-eigenvalue enclosure” is not justified by the artifacts. `stageF.py` solves a finite-difference MOTS equation and computes `Q` from sampled numerical derivatives. `verify_certificate.py` checks the same discrete profile. It does not provide a theorem or validated-numerics bound connecting that profile to an exact smooth MOTS with controlled geometric error. Its continuum “Lipschitz” and quadrature corrections are themselves estimated from grid derivatives, and pole values are extrapolated. Consequently the interval cannot certify the exact continuum principal eigenvalue or strict stability.

The underlying numerical signal is robust. An independent implementation at `N=80` and `N=120` reproduced `Q_min≈0.15790164`, area-weighted mean `Q≈0.15999`, and the same surface-radius range. The repaired record therefore retains these as numerical diagnostics and removes the rigorous-certification claim.

## Originality
**PASS ONLY AFTER NARROWING.** The original “no prior work logs a principal-eigenvalue enclosure for any Brill–Lindquist two-puncture cell” statement is false or at least materially misleading: Pook-Kolb et al. (2019) explicitly study the MOTS stability parameter in binary black-hole initial data, including Brill–Lindquist sequences, and later reviews describe the associated stability spectrum. Targeted searches did not locate this exact equal-bare-mass `(1,1)`, separation-2 numerical table, so the repaired record is presented only as a reproducible parameter-point benchmark with no priority claim.

## Scientific value
**PASS AFTER REPAIR.** A reproducible benchmark for an individual horizon candidate, with archived surface/Q arrays and scripts, can be useful for code comparison and stability-operator calibration. Its value is numerical and diagnostic, not a rigorous theorem.

## Independent numerical replay
Using the formulas in `stageF.py`:
- `N=80`: discrete residual `3.99e-13`, `H=[0.3827704,0.4148625]`, `Q_min=0.157901658`, mean `Q=0.159992234`.
- `N=120`: discrete residual `1.24e-12`, `H=[0.3827724,0.4148621]`, `Q_min=0.157901641`, mean `Q=0.159994474`.

These checks support the numerical trend but do not cure the continuum-certification gap.

## Literature checked
- D. Pook-Kolb et al., *Existence and stability of marginally trapped surfaces in black-hole spacetimes*, Phys. Rev. D 99, 064005 (2019), DOI 10.1103/PhysRevD.99.064005; arXiv:1811.10405.
- L. Andersson, M. Mars, W. Simon, *Stability of marginally outer trapped surfaces and existence of marginally outer trapped tubes*, arXiv:0704.2889.
- Quasi-local horizon reviews summarizing Brill–Lindquist MOTS sequences and stability spectra.

## Required publication repair
Replace `RESULT.md`, `METADATA.json`, and `SLOGAN.txt` with the supplied corrected full contents. Preserve the computational artifacts unchanged. The repaired text must call the numbers grid-based numerical diagnostics, not a validated eigenvalue enclosure or proof of strict stability.
