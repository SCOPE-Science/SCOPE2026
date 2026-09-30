# Independent Audit — 2026/09/16/004

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `618beb09197d3a67499f043a0b852051b54932b7`  
**Audited current source tree:** `618beb09197d3a67499f043a0b852051b54932b7`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** repaired

The current `main` directory tree SHA exactly matches the assignment tree SHA, and the designated failed destination was verified absent.

## Correctness — PASSED

PASS AFTER REPAIR. The Li–Miao formulas were checked against arXiv:2506.17420v3: Corollary 2.5 gives V<=phi(T), equations (25),(29),(30) give the implemented phi/Phi, and for v2 the paper has A=2n-d. Independent recomputation of all 28 pairs 4<=n<=10, 3<=d<=n-1 gives phi_2(T)/B in [1.0402228914,1.1338599191]. At (4,3), exact arithmetic gives Psi(4)=-261/10, Psi(41/10)=7389/1000, hence T in (7,7.1) and phi(T)>1971/4=492.75>486. Two package defects required correction: the archived script omitted n=9 despite the “n<=10” claim, and all reproducibility paths incorrectly used output/artifacts. The sentence claiming Question 4.20 is unprovable by v1/v2 “alone” was also too broad; an overlarge Corollary-2.5 ceiling only defeats that specific quantitative use of the published lower estimate, not every sharper or combined use of the same valuations.

## Originality — PASSED

PASS, NARROWLY STATED. Li–Miao explicitly leave Question 4.20 open and provide the v1/v2 machinery, but the audited search did not locate their comparison of the resulting Corollary-2.5 ceiling with vol(P^{d-1}xP^{n-d+1}) across these 28 pairs or the exact (4,3) certificate. The contribution is therefore the explicit method-diagnostic computation, not a new valuation or a resolution of the open question.

## Scientific value — PASSED

PASS WITH LIMITED SCOPE. The exact anchor and complete small-dimensional table are useful negative information about a natural direct proof route to an explicit open question. The repaired record now states this as a ceiling diagnostic rather than a theorem about what all future v1/v2 arguments can or cannot prove.

## Independent checks

- matched the implemented phi and Phi with Li–Miao equations (25), (29), and (30) and A(v2)=2n-d
- independently recomputed all 28 pairs 4<=n<=10 and both v1/v2 controls
- checked the (4,3) certificate in exact rational arithmetic
- identified the omitted n=9 enumeration and repaired the artifact loop to range(4,11)
- checked current record tree equals the assigned tree and failed destination is vacant

## Limitations

- The full 28-pair comparison remains a floating-point bisection table; only the (4,3) anchor is supplied as an exact interval certificate.
- Literature search can support but cannot prove priority; originality is limited to the explicit ceiling comparison/diagnostic.
- The repaired conclusion does not settle Question 4.20 and does not rule out sharper or combined uses of v1/v2.
- Open-access full text was sufficient; Oxford Download was not needed.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/16/004
- https://arxiv.org/abs/2506.17420
- https://arxiv.org/abs/2608.08193

This audit changes only the independent-audit channel in `VERIFICATION.md`; Lean verification and expert attestation remain exactly as previously recorded.
