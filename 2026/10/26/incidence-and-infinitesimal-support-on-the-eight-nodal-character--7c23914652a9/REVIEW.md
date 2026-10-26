# Mathematical review

## Correctness — PASS
The degree-four restriction test is exhaustive across 7462 unique RREF two-planes over \(\mathbf F_9\), and the direct form is checked against the expanded quartic at every projective point. A separate pair-of-points enumeration recovers the same 48 lines. All 48 are tested against singular-node incidence and intersection. The five-equation Jacobian in affine Grassmannian charts yields exactly seven one-dimensional tangent spaces, specifically seven of eight two-node lines; the unique tangent-zero exception is explicitly identified. The standalone verifier runs without external dependencies and returns `VERIFY_OK`. No extension-field completeness is inferred merely from this finite computation.

## Originality — PASS, with residual risk
Veniani's first version gives the eight-node/48-line geometric example; an existing finite-field computation already gives the Frobenius split and seven nonreduced line support points. These known counts are expressly not claimed new. The new datum is the **exact incidence/tangent-space cross-classification**, including the unique reduced member among eight two-node/degree-18 lines. This is not a restatement of the prior seven-point count or the geometric line total. Searches against prior records and mathematical literature did not locate the full cross-classification. The 2020 revised Veniani example has different local incidence figures, making independent specialist comparison desirable.

## Mathematical value — PASS
The distinction between tangentially obstructed and reduced points of a Fano scheme is a geometric feature, not a relabeling of a finite graph. Its exact relationship to the natural singular-point stratification provides a structural explanation of why seven of eight maximally incident lines behave differently, and identifies the exceptional smooth Fano point. This classification is a natural complete invariant of a highly line-rich singular quartic, relevant to studying its Fano scheme and deformation behavior.

## Sources and risks
Primary: Veniani, arXiv:1608.04209v1 (Example 6.5) and v4 (Example 5.4); Shimada–Shioda arXiv:1604.06265, its reduction discussion. Specialized equivalent computations could remain unidentified. The result applies precisely to the rational lines over \(\mathbf F_9\). Conflicting numbers in a later version of the primary source are recorded as an unresolved comparison, not concealed or used as proof.

Self-review: passed. Independent audit: not yet performed.
