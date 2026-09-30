# Independent Audit — 2026-09-30

**Record:** `2026/09/20/positive-characteristic-two-call-register-programs--e2229eff652e`  
**Title:** Positive characteristic collapses the two-call passive register frontier  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `1986f363e3e7c196583622496498f77ef6b0df87`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS:** The two-register classification is correct in the stated passive-output model. Sufficiency is the clean finite-difference identity A(tau+x)-A(tau)=A(x). For necessity, because the output is passive and there is only one work register, call-free updates of that work register add constants only. If the two nonzero accesses both hit the work register, restoration forces coefficients a and -a and all output updates during the active interval sum to a single polynomial H(tau+ax); cleanliness then gives H(tau+ax)-H(tau)=f(x)-f(0), which forces an additive polynomial after rescaling. In characteristic p, additive polynomials are exactly p-polynomials sum a_j X^(p^j), so X^(p^e) is cleanly computable with two calls for every e.
- **Originality — PASS:** The potentially decisive conflict with Vinciguerra’s abstract was resolved by reading the complete 31-page arXiv v1 through authorized institutional retrieval after direct arXiv PDF access failed. Section 3 explicitly begins “Throughout this section, K is a field of characteristic 0”; Theorem 3.2’s two-call degree-one lower bound is therefore characteristic-zero only. The filed Frobenius counter-regime does not contradict the paper and pinpoints exactly why its exponential/Vandermonde lower bound cannot extend to small positive characteristic. The 2025 MFCS work covers positive-characteristic constructions but no matching exact two-call additive-polynomial classification was located.
- **Scientific value — PASS:** The result exposes a sharp characteristic dependence in a current lower-bound program: a frontier that is finite in characteristic zero becomes formally unbounded in positive characteristic with the same two calls. The exact iff classification by additive polynomials explains the mechanism rather than presenting only a counterexample.

## Independent findings
- The complete Vinciguerra v1 explicitly restricts Section 3 lower bounds to characteristic zero, resolving the apparent field-independent wording of the abstract.
- The five-instruction sufficiency program restores the work register and adds c+A(x) to the passive output for every additive A.
- In the two-call necessity argument, grouping active output updates into H is valid because every active work-register value is tau+ax plus a constant shift.
- Over finite fields the theorem is a formal-polynomial statement; polynomial-function degree remains representation-dependent, exactly as the record warns.

## Independent checks
- Reconstructed the sufficiency and necessity proof from the model definition.
- Checked the Frobenius identity (tau+x)^(p^e)-tau^(p^e)=x^(p^e) in characteristic p.
- Obtained and read the complete arXiv:2609.18692v1 text after open PDF retrieval failed; verified the characteristic-zero scope of Section 3 and Theorem 3.2.
- Compared with the 2025 MFCS register-program paper for positive-characteristic context.

## Literature evidence
- https://arxiv.org/abs/2609.18692 — Vinciguerra (2026). Complete v1 inspected through authorized retrieval; Section 3 explicitly assumes characteristic zero before proving the one/two/three-call lower bounds.
- https://doi.org/10.4230/LIPIcs.MFCS.2025.6 — Alekseev, Filmus, Mertz, Smal and Vinciguerra (MFCS 2025), earlier register-program framework and positive-characteristic constructions; no exact two-call additive classification located.
- https://doi.org/10.1017/S0305004196001168 — Odoni (1997), background on additive polynomials; additive-polynomial classification itself is not claimed as new.

## Limitations
- The exact iff theorem is only for one work register plus one passive output and at most two input accesses.
- The unbounded formal-degree corollary extends to more registers only by reusing this two-register construction, not by classifying all multi-register two-call programs.
- Over finite fields, formal polynomial degree and polynomial-function degree must be distinguished.
- The construction is simple once Frobenius is noticed, so independent folklore or near-simultaneous priority remains possible.

The assigned source tree remained unchanged from the source-tree-check interval through current main commit `eff2c6312cec5b0dee5115e5f42211a853092dfb`; the exact tree audited is `1986f363e3e7c196583622496498f77ef6b0df87` and matches the assignment guard. GitHub was used only as read-only evidence; no repository writes were made. Audit timestamps and this audit-file date use UTC under the task-specific audit contract.
