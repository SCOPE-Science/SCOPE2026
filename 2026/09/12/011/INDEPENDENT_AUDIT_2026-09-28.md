# Independent Audit — 2026-09-29

**Record:** `2026/09/12/011`  
**Title:** Refutation of the 8% binomial-versus-Gaussian Fourier envelope at ML-KEM-768  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `ae9c39a2bd1637cd04076023cf875f042a7f1d02`  
**Disposition:** **PASSED**

## Independent checks

- Solved the rounded-Gaussian variance-matching equation independently at high precision.
- Recomputed both characteristic functions at t=768 and the ratio.
- Checked the filed variance endpoints 0.955 and 0.96 independently.
- Verified the deployed ML-KEM-768 eta parameters against current FIPS 203 context.

## Three-axis assessment

- **Correctness — PASS**: The one-dimensional counterexample is correct for the model stated in the record. Independently solving Var(round(sZ))=1 gives s*=0.957427135029..., with phi_B(768)=cos^4(pi*768/3329)=0.314142902254... and phi_G(768)=0.349190501295..., so phi_B/phi_G=0.899631865957... and the deviation is about 10.04%, exceeding 8%. The filed endpoint variance bracket V(0.955)<1<V(0.96) also reproduces.
- **Originality — LIMITED**: The characteristic function of the eta=2 centered binomial law is elementary, and the counterexample is a targeted numerical/certified comparison to a variance-matched rounded Gaussian. It does not constitute a new theorem about ML-KEM security or a general distribution-transfer bound.
- **Scientific value — PASS**: Within the admitted model, the record usefully rules out a specific uniform 8% surrogate bound and quantifies where the mismatch becomes material. The limitation to a scalar Fourier factor is clearly stated and prevents overinterpretation as a full security claim.

## Findings

- The current record tree exactly matches the assigned tree SHA.
- Independent high-precision calculation gives s*=0.9574271350291349, ratio 0.8996318659571999 at t=768, and therefore a 0.100368... relative deviation.
- FIPS 203 standardizes ML-KEM and ML-KEM-768 uses q=3329 with eta1=eta2=2; the record's centered-binomial law is therefore a relevant deployed coefficient law.
- The asserted interval [0,768] is part of the admitted target/model; the audit does not independently derive that interval from a complete dual-attack analysis.
- The repository's `output/artifacts/...` reproducibility path is stale; the packaged script is `artifacts/verify_counterexample.py`, a non-scientific packaging issue.

## Sources compared

- NIST FIPS 203 (final, 2024-08-13): https://csrc.nist.gov/pubs/fips/203/final — Defines ML-KEM and its parameter sets.
- FIPS 203 parameter summary for ML-KEM-768: https://cryptohives.github.io/Foundation/packages/security/cryptography/specs/NIST-FIPS-203.html — Reports q=3329 and eta1=eta2=2 for ML-KEM-768, consistent with the record's centered-binomial law.

## Limitations

- This validates only the stated scalar modular characteristic-function comparison against a variance-matched rounded Gaussian.
- It does not establish a corrected uniform envelope, a lattice-summed dual advantage, or an end-to-end ML-KEM security estimate.

This audit is independent of the repository's pre-existing audit material. GitHub was read only as evidence; no repository changes were made by this audit run.
