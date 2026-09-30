# Independent Audit — 2026/09/11/006

**Audit date:** 2026-09-28 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `1fe196a4e063dc46866fb438061ea5a20095d15b`  
**Audited current source tree:** `1fe196a4e063dc46866fb438061ea5a20095d15b`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` directory tree SHA exactly matches the assignment tree SHA, so no intervening record change required a stale-source re-audit.

## Correctness

PASS. The exact threshold algebra and the claimed positivity on mu∈[1,2] check out. Independently simplifying the stated formulas gives p^2-b^2-q^2 = 2(4nu+1)((25+38sqrt(2))nu-84+36sqrt(2))/nu exactly. The unique zero corresponds to mu*=(13+11sqrt(2))/12≈2.3796957655, outside [1,2]. Direct evaluation of the smaller odd eigenvalue is positive at mu=1,1.5,2 (about 3.2441, 1.6613, 0.5941 respectively), while the even eigenvalues are manifestly positive. Thus the transverse Hessian is nondegenerate and positive definite throughout the audited interval, supporting index 0 and local isolation modulo the stated symmetries.

## Originality

SUPPORTED, BUT STRICTLY DELIMITED. Meyer--Schmidt already studied this square-plus-center family and located the same degeneracy/bifurcation parameter, so nondegeneracy on [1,2] is not new by itself. The defensible incremental content is the explicit transverse Hessian inertia/index-0 certificate, closed-form positive-definiteness reduction, and local Morse-degree contribution on the stated interval. I did not identify a prior source tabulating those exact endpoint indices, but absence from search is not evidence of novelty beyond this narrow increment.

## Scientific value

MODEST BUT REUSABLE VALUE. The exact inertia/positive-definiteness certificate supplies a concrete endpoint degree anchor and a reproducible local bifurcation check on a canonical five-body family. Its value is local and technical: it does not advance the known location of the Meyer--Schmidt bifurcation or provide a global five-body central-configuration census.

## Independent checks

- current main record tree SHA equals the assigned source-tree SHA
- symbolic factorization of p^2-b^2-q^2 independently reproduced exactly
- mu*=(13+11sqrt(2))/12 independently evaluated as about 2.3796957655
- smallest odd eigenvalue independently evaluated positive at mu=1,1.5,2

## Limitations

- The same square-family degeneracy threshold and bifurcating branches were already present in Meyer--Schmidt; originality is limited to the explicit inertia/PD certificate.
- Isolation is local to this square-with-center branch and does not exclude disconnected asymmetric or other symmetric configurations.
- The audit verifies the position-form transverse Hessian argument, not a separate elimination in the mutual-distance Albouy--Chenciner ideal.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/11/006
- https://doi.org/10.1017/S0143385700009433
- https://arxiv.org/abs/1903.10270
- https://arxiv.org/abs/1207.1305

This audit changes only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
