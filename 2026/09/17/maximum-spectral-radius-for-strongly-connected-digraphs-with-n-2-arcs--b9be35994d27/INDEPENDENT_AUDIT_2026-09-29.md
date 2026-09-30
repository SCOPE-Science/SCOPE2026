# Independent audit — 2026-09-29

**Record:** `2026/09/17/maximum-spectral-radius-for-strongly-connected-digraphs-with-n-2-arcs--b9be35994d27`  
**Audited source tree:** `0207f1c5324d0e297d8799c098b1c362fcd7ab63`  
**Repository snapshot:** `SCOPE-Science/SCOPE2026@253a0fe5d0217455660a277f9adb940030e567ad`  
**Disposition:** PASSED

## Correctness

PASS. The outdegree-excess identity sum_v(d^+(v)-1)=2 leaves exactly the one-branch (outdegree 3) and two-branch (two outdegree-2 vertices) cases. Suppressing deterministic chains in a positive Perron eigenvector gives the stated monomials r^L with r=1/rho. For one branch, the return-route lengths have total at least n+2; convexity of r^x for 0<r<1 and the loop/simple-arc restrictions make (1,2,n-1) (loops allowed) and (2,2,n-2) (loopless) the unique extremal exponent patterns. I independently reconstructed the three two-branch compressed matrices. In the mixed/cross-only case, rho(M)<1 reduces to r^a+r^(b+c)+r^(b+d)<1 and the exponent sum is at least n+3; in the mixed/mixed case det(I-M)>0 reduces to (1-r^a)(1-r^d)>r^(b+c), with concavity of log(1-r^x) reducing the fixed-sum comparison to the endpoint cases; in the cross-only/cross-only case rho(M)^2=(r^a+r^b)(r^c+r^d), and simple-arc constraints plus convex spreading give a strict candidate-root bound. The candidate root identities verify all endpoints. An independent exhaustive labelled enumeration for n=3,4,5 in both loop conventions reproduced the archived maxima and equality counts, including the exceptional loopless n=3 value (1+sqrt(5))/2.

## Originality

PASS, qualified. Klech's September 16 preprint still presents the n+2-edge problem as a structural extremal problem and the record identifies its maximum statement as Conjecture 5.15. Targeted searches through September 29 found no later source proving the same maximum theorem. Earlier Guo--Liu and related papers concern generalized infinity/theta or bicyclic (n+1-edge) subclasses rather than the full n+2-edge class; the accessible Guo--Liu abstract supports that scope. Institutional retrieval of the Guo--Liu full text reached a human-verification barrier, so I do not claim to have read that paper in full and retain this as a residual priority limitation.

## Scientific value

PASS. The theorem resolves an explicit fresh global extremal question, including uniqueness and both loop conventions. Its useful content is not the already-known within-rose comparison but the reduction and strict elimination of every two-branch topology; that is a nontrivial infinite-family classification rather than a finite computation.

## Evidence and literature

- https://arxiv.org/abs/2609.18367 — R. Klech, Generating Functions and the Minimum Spectral Radius in Strongly Connected Digraphs with m+2 Edges; motivating September 2026 preprint and source of the stated conjectural maximum problem.
- https://doi.org/10.1016/j.laa.2012.05.034 — G. Guo and J. Liu, Some results on the spectral radius of generalized infinity and theta-digraphs. Abstract inspected; full text could not be completed because institutional access required human verification.
- https://arxiv.org/abs/2105.03077 — Shan, Wang and He; nearby extremal work on rose/generalized-theta/tri-ring type classes, not a located proof of the global n+2-arc maximum.

## Limitations

- The Guo--Liu 2012 full text was not read because the authorized institutional retrieval stopped at a human-verification step; the originality verdict therefore remains qualified against that paper and unindexed contemporaneous work.
- The independent finite enumeration checks only n=3,4,5; the all-n conclusion rests on the reconstructed branch-compression inequalities, not on enumeration.

## Audit conclusion

All three audit axes pass. No substantive research-file correction is required. This audit changes only the independent-audit verification channel and does not alter Lean or expert-attestation channels.
