# Independent Audit — 2026/09/16/007

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `93990bd98f2b930233cf097ca9d5e11d8829c285`  
**Audited current source tree:** `93990bd98f2b930233cf097ca9d5e11d8829c285`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** repaired

The current `main` directory tree SHA exactly matches the assignment tree SHA, and the designated failed destination was verified absent.

## Correctness — PASSED

PASS AFTER REPRODUCIBILITY REPAIR. The no-go proof is correct. Product hPEPS force C|v>^m to be nonzero for every v. The explicit D=2 cat tensor on a connected torus produces |v_1>^n+|v_2>^n, and for independent v_1,v_2 the complement tensor powers remain independent. Hence universal cut-purity forces all C|v>^m to be collinear. Pure powers span Sym^m(C^2), so the restriction of C has rank at most one; rank zero kills all products, while rank one is a nonzero homogeneous binary form times a fixed output vector and therefore has a projective root over C, killing some product. The committed script path, however, is artifacts/verify_impossibility.py rather than output/artifacts/verify_impossibility.py, so RESULT.md and METADATA.json required repair.

## Originality — PASSED

PASS WITH SEARCH QUALIFICATION. The argument is elementary once the product and cat subfamilies are isolated, but targeted PEPS/tensor-network searches did not locate a prior theorem with this exact quantification over one A-independent, n-independent fixed patch operator. Standard PEPS references such as Buerschaper concern injectivity/topological phases rather than this universal-filter obstruction. Priority is therefore treated cautiously rather than advertised broadly.

## Scientific value — PASSED

PASS, NARROWLY. The theorem cleanly rules out the first step of a specific universal cut-and-glue program for distinguishing homogeneous bond dimensions. It is useful because the obstruction holds for every patch size and follows from very small D<=2 subfamilies, while the limitations correctly leave tensor-dependent, approximate, and adaptive methods open.

## Independent checks

- independently reconstructed the D=2 all-virtual-0/all-virtual-1 cat PEPS on a connected torus
- proved independence of tensor powers of two independent qubit vectors on any nonempty complement
- rederived the cut-purity/collinearity implication and the span of pure powers in Sym^m(C^2)
- applied the fundamental theorem of algebra to the rank-one binary form to obtain a killed product state
- checked current record tree equals the assigned tree and failed destination is vacant

## Limitations

- The audit establishes no absolute priority from search alone; the originality pass is limited to the exact universal-filter statement.
- The theorem applies to a single exact fixed linear postselection operator and does not address tensor-dependent, size-dependent, approximate, multi-Kraus, or adaptive procedures.
- The numerical artifact is illustrative rather than part of the proof.
- Open-access sources were sufficient; Oxford Download was not needed.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/16/007
- https://arxiv.org/abs/1307.7763

This audit changes only the independent-audit channel in `VERIFICATION.md`; Lean verification and expert attestation remain exactly as previously recorded.
