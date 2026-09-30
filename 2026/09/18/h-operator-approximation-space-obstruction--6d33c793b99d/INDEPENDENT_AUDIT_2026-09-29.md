# Independent Audit — A two-dimensional obstruction to H-operator approximation schemes

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `2ad7ab95aafb92fb8c3fa6880407d92be78a4c60`  
**Audited current source tree:** `2ad7ab95aafb92fb8c3fa6880407d92be78a4c60`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree is unchanged from the dispatcher-audited source tree. GitHub was used read-only as evidence; this audit file is staged by the ledger change-set and is not claimed to be already published.

## Correctness — PASSED

PASS. The two displayed 2×2 matrices are each similar to a real diagonal matrix diag(1,-1) or diag(-1,1), so their spectra are real and their resolvents obey the H-operator bound with a finite similarity-condition constant. Finite dimensionality makes them compact. Their sum has characteristic polynomial t^2+4 and spectrum {±2i}, so the class of compact H-operators is not additive. That directly conflicts with the 2024 paper's earlier requirement that the ambient X of an approximation scheme be a quasi-Banach linear space when its later Definition 5.1 takes X to be all compact H-operators. The separate 'between X and Y' typing objection is also valid because the defining resolvent T-λI and ordinary spectrum/eigenvalue sequence are canonical only for endomorphisms.

## Originality — PASSED

PASS, narrowly scoped. The 2024 article itself does not flag this nonadditivity/type inconsistency, and targeted correction/erratum searches did not locate the same objection. The September 2026 follow-up was read in full from arXiv: it changes parts of the framework and often writes K_H(X), but it does not state or resolve the submitted explicit nonadditivity counterexample, and it still mixes same-space H-operator language with broader approximation-space language. The linear-algebra example is elementary; originality is limited to identifying and documenting its consequence for the published framework.

## Scientific value — PASSED

PASS. The counterexample exposes a structural defect in a published approximation-space setup, not just a cosmetic notation issue: subtraction and series reconstruction used in the representation theorem require an additive ambient space. The record also identifies a coherent repair boundary by placing approximation theory in a genuine linear compact-operator space and intersecting with the nonlinear H-operator class.

## Independent checks

- Multiplied the submitted similarity factorizations and re-derived the resolvent estimate.
- Computed the spectrum of A+B directly.
- Read the 2024 definitions requiring a quasi-Banach ambient space and the later section taking all compact H-operators as that ambient X.
- Checked the same-source use of operators 'between' arbitrary Banach spaces against the same-space resolvent/spectrum definition.
- Read the 2026 arXiv follow-up and verified that it does not supply the submitted correction.
- Verified no file under this assigned record changed between the dispatcher source-check commit and current audited main.

## Limitations

- The counterexample is elementary and does not invalidate set-theoretic approximation-number/eigenvalue estimates for an individual compact H-operator.
- The audit does not claim that every possible repaired H-operator approximation framework is impossible.
- An older differently phrased correction could in principle have escaped targeted searches.

## Evidence and references

- https://doi.org/10.2140/involve.2024.17.709
- https://arxiv.org/abs/2306.03633
- https://arxiv.org/abs/2609.14381
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/18/h-operator-approximation-space-obstruction--6d33c793b99d

This change set updates only the independent-audit channel. Lean verification and expert attestation are preserved exactly as previously recorded.
