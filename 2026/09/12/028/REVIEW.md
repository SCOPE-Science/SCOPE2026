# Review status

Independent mathematical audit date: 2026-10-01 UTC.

Disposition: **passed**.

Correctness: PASS. The exact certificate was rechecked entry by entry from the actual repository JSON files. The 35 by 35 rational matrix is symmetric, has trace exactly 1, is zero on all 248 graph edges, and its supplied LDL decomposition reconstructs every matrix entry exactly with all 35 pivots positive. Its all-ones objective is exactly 754549/100000, which is greater than 6. Therefore it is primal feasible for the stated Lovasz-theta SDP and proves theta(G35) at least 7.54549 by weak duality. The graph6 strings in the graph and certificate files agree.

Originality: PASS. Exoo and McKay supply the Ramsey graph itself, and Lovasz supplies the general theta theory, but targeted searches found no prior theta value or exact SDP certificate for this hash-pinned 35-vertex witness. The certificate is not a specialization of a known closed formula for this irregular graph. The related audited single-vertex maximality result concerns a different invariant and does not imply the theta bound.

Scientific value: PASS. The threshold 6 is intrinsic to the Ramsey(4,6) application: a theta upper bound below 6 would certify the needed independence obstruction, while this exact primal witness proves that this standard relaxation is far too weak on a canonical extremal witness. An exact rational lower certificate on a natural benchmark graph is a useful negative diagnostic for SDP-based Ramsey approaches.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
