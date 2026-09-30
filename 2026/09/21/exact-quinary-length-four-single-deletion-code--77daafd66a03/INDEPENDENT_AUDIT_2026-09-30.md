# Independent audit — 2026-09-30

**Record:** `2026/09/21/exact-quinary-length-four-single-deletion-code--77daafd66a03`  
**Repository:** `SCOPE-Science/SCOPE2026` at `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Audited tree:** `5efa8a89104bb37a86068ad3d9029a65236fa2d9`  
**Disposition:** **REPAIRED**

## Correctness

**PASS WITH PACKAGE REPAIR.** The mathematical claim was independently rechecked as an exact set-packing ILP: 625 binary variables correspond to quinary length-four words and 125 capacity-one constraints to length-three deletion outputs. SciPy/HiGHS returned an optimal objective 42 with zero MIP gap; the displayed 42-word witness has pairwise-disjoint deletion shadows. The same implementation returns the known q=4 optimum 24. The assigned repository tree, however, does not contain the `artifacts/` directory even though RESULT.md and METADATA.json assert `artifacts/verify_q5.py` and `artifacts/verification_output.txt` are present. This is a reproducibility/package defect, not a defect in the theorem. The ready repair adds a freshly audited verifier and output and updates METADATA.json to their actual SHA-256 hashes.

## Originality

**PASS (literature-bounded).** Kim–Lee–Oh prove the exact length-four result for even q and leave the odd-alphabet bound nonsharp. The Li–Houghten 2012 paper was first sought through open routes, then obtained through authorized institutional access; all eight pages were inspected. It focuses on Tenengolts-code properties and ternary experiments and does not state N(4,5,1)=42 or an exact quinary length-four optimum. Searches for the exact notation and quinary/length-four terminology did not locate a prior exact value; the claim remains bounded by the checked literature.

## Scientific value

**PASS.** The result closes a concrete odd-alphabet length-four instance singled out by the classical theory, improving the general bound 45 to the exact optimum 42 with an explicit witness.

## Literature and evidence

- Kim, Lee and Oh, Optimal single deletion correcting code of length four over an alphabet of even size: https://arxiv.org/abs/1003.4057
- Kulkarni and Kiyavash, Nonasymptotic upper bounds for deletion correcting codes: https://arxiv.org/abs/1211.3128
- Li and Houghten, Searching for Optimal Deletion Correcting Codes: https://doi.org/10.1109/CIT.2012.137

## Limitations

- The upper bound is computer-assisted through an exact MILP solve rather than a symbolic odd-q classification.
- The repaired verifier depends on SciPy/HiGHS; it supplies a zero MIP gap but not a separately checkable proof certificate.

## Repair

The assigned tree omits the verifier files named by RESULT.md and METADATA.json. The change set adds a complete exact-MILP verifier and its verified output and updates METADATA.json to their actual SHA-256 values. No theorem text is narrowed because the independent computation confirms the stated optimum.

This audit was performed independently of the same-model review. GitHub was used only as evidence; no repository write was made by the auditor.
