---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The standalone `verify.py` artifact was read from its packaged path before replay.

For a tuple of local nilpotency lengths \((\ell_1,\ldots,\ell_r)\), the checker enumerates all exponent vectors
\[
(a_1,\ldots,a_r),
\qquad
0\le a_i\le\ell_i,
\]
removing the vectors for \(R\) and \(0\). It joins two vertices exactly when some coordinate is nonzero in both corresponding product ideals.

The checker then:

1. builds the support-incidence Gram matrix and verifies its complete off-diagonal zero-nonzero pattern against the graph;
2. computes the Gram rank exactly over rational arithmetic;
3. constructs the theorem's explicit set with exactly \(r\) white ideals and replays the full zero forcing sequence;
4. for every nonboundary test graph of order at most \(16\), exhaustively verifies that no set of size \(N-r-1\) is zero forcing;
5. separately verifies the \(K_1\) boundary.

Exact replay output:

```text
lengths=(2,): N=1, boundary K1, Z=1, mr=0
lengths=(3,): N=2, r=1, constructed_Z=1, forces=1, Gram_rank=1
lengths=(4,): N=3, r=1, constructed_Z=2, forces=1, Gram_rank=1
lengths=(2, 1): N=4, r=2, constructed_Z=2, forces=2, Gram_rank=2
lengths=(3, 1): N=6, r=2, constructed_Z=4, forces=2, Gram_rank=2
lengths=(2, 2): N=7, r=2, constructed_Z=5, forces=2, Gram_rank=2
lengths=(3, 2): N=10, r=2, constructed_Z=8, forces=2, Gram_rank=2
lengths=(2, 1, 1): N=10, r=3, constructed_Z=7, forces=3, Gram_rank=3
lengths=(2, 2, 1): N=16, r=3, constructed_Z=13, forces=3, Gram_rank=3
lengths=(2, 1, 1, 1): N=22, r=4, constructed_Z=18, forces=4, Gram_rank=4
VERIFY_OK
```

The finite checks corroborate the symbolic proof but do not replace it. The general lower bound is supplied by the exact rank-\(r\) Gram witness and the inequality \(M(G)\le Z(G)\).
