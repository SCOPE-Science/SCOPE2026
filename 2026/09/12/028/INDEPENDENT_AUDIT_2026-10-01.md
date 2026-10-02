# Independent audit — 2026-10-01

## Final claim

Certified Lovasz theta defect theta(G35) >= 7.54549 for the hash-pinned Exoo Ramsey(4,6;35) core

## Correctness — PASS

PASS. The exact certificate was rechecked entry by entry from the actual repository JSON files. The 35 by 35 rational matrix is symmetric, has trace exactly 1, is zero on all 248 graph edges, and its supplied LDL decomposition reconstructs every matrix entry exactly with all 35 pivots positive. Its all-ones objective is exactly 754549/100000, which is greater than 6. Therefore it is primal feasible for the stated Lovasz-theta SDP and proves theta(G35) at least 7.54549 by weak duality. The graph6 strings in the graph and certificate files agree.

## Originality — PASS

PASS. Exoo and McKay supply the Ramsey graph itself, and Lovasz supplies the general theta theory, but targeted searches found no prior theta value or exact SDP certificate for this hash-pinned 35-vertex witness. The certificate is not a specialization of a known closed formula for this irregular graph. The related audited single-vertex maximality result concerns a different invariant and does not imply the theta bound.

## Scientific value — PASS

PASS. The threshold 6 is intrinsic to the Ramsey(4,6) application: a theta upper bound below 6 would certify the needed independence obstruction, while this exact primal witness proves that this standard relaxation is far too weak on a canonical extremal witness. An exact rational lower certificate on a natural benchmark graph is a useful negative diagnostic for SDP-based Ramsey approaches.

## Sources inspected

- Geoffrey Exoo, On the Ramsey Number R(4,6) — https://doi.org/10.37236/2102: OBJECT_SOURCE_NOT_THETA_COVERAGE. The paper supplies the extremal graph family, not Lovasz-theta computations.
- L. Lovasz, On the Shannon Capacity of a Graph — https://doi.org/10.1109/TIT.1979.1055985: GENERAL_FRAMEWORK_NOT_EXACT_COVERAGE. Defines the invariant and sandwich theorem; it does not compute this graph.

## Residual risks

- The certificate proves only a lower bound, not the exact theta value.
- The RESULT's reproducibility prose uses the historical prefix output/artifacts, while the actual files are under artifacts; the replacement METADATA records the actual paths.

## Disposition

**passed**
