# Independent audit — 2026-09-29

Record: `2026/09/15/030`  
Audited source tree: `2df2921d8809617f444a6c480dd793044b43a46f`  
Disposition: **passed**

## Correctness

The Frobenius criterion is correct, and the archived exact trace certificate has a valid zero test because the trace pairing on Q(zeta_39) is nondegenerate. Independently reparsing the raw 74-row irreducible block and recomputing the complex Frobenius sums gives magnitudes about 6.2e-16, 4.4e-14 and 2.7e-14 for classes 12,17,18 respectively, while the next-smallest class is about 0.217, matching the exact-zero list. The e(G)>=4 conclusion is specifically witnessed by the non-real inverse-pair classes 17/18: they miss 1 in C^2 and the exact Frobenius sum shows they also miss 1 in C^3. Class 12 is real, so it is an additional C^3-zero class but not itself an e>=4 witness.

## Originality

Garonzi–Montiijo–Zalesski explicitly left the PSp_6(q) case with 4|(q+1) open, which includes q=3. A focused search through September 2026 found no later public source resolving the PSp_6(3) instance. This supports scientific interest but is not treated as a formal priority proof.

## Scientific value

The q=3 computation gives a concrete counterexample to the universal exponent-3 claim and resolves the smallest open symplectic instance in the cited formulation. The exact character-theoretic certificate makes the negative result especially useful, even though it does not determine the exact exponent or q>3 cases.

## Limitations

- The exact value of e(PSp_6(3)) beyond the lower bound 4 is not determined.
- No q>3 member of the 4|(q+1) family is settled.
- The character table input is inherited from GAP CTblLib/ATLAS, though the audit independently reparsed the raw irreducible block and reproduced the numerical zero/nonzero separation.
- Class 12 is real and therefore not the e>=4 witness; the lower bound comes from the non-real inverse-pair classes 17/18.
- The archived Python scripts refer to pre-publication output/... input paths that are not present verbatim in the record tree; this is a reproducibility packaging defect, not a defect in the independently rechecked character sum.

## Sources checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/15/030
- https://arxiv.org/abs/2506.22268
- https://arxiv.org/abs/1202.2627
- https://brauer.maths.qmul.ac.uk/Atlas/v3/clas/S63/
