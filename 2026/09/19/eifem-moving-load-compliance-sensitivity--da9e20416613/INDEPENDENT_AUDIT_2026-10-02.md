# Independent mathematical audit

## correctness

PASS

The complete frozen derivation was independently checked. Differentiating Fc^T Kc^-1 Fc gives 2 Fc_prime^T q minus q^T Kc_prime q. Expanding the exact Galerkin matrices yields the residual moving-space term; a coordinate change TR adds opposite gauge terms to load and stiffness. The full-space rotational cancellation and rank-one wrong-sign examples check exactly. Primary Eq.10, parameterized T in Section3, and all of Section4.2/Eqs37-41 have now been read: fixed physical F is used to motivate fixed coarse Fc, and Eq39 omits its derivative. The frozen record correctly distinguishes this surrogate from the physical pullback. Direct DEIM stiffness interpolation need not equal T^TKT; the general load derivative identity still holds for any differentiable SPD coarse stiffness, while the residual form is explicitly an exact-Galerkin result. No claim is made that benchmarks or implementation are wrong.

## originality

PASS

Novelty is the specific EIFEM load-convention mismatch and exact-space gauge/sign diagnostics, not the chain rule, Pulay forces, moving bases, or general ROM sensitivity. The actual source does explicitly choose a fixed-coarse-load surrogate: the record allows that surrogate and criticizes only its identification with fixed physical loading. Existing four originality checks are retained as historical evidence, supplemented by exact paper-id/sensitivity/correction searches and an actual five-hit semantic search. No earlier matching correction was found; unindexed equivalent diagnostics remain a stated best-of-knowledge risk.

## value

PASS

The missing pulled-back-load term can reverse a gradient or create a spurious coordinate-dependent sensitivity even with an exact reduced space. The inexpensive term restores consistency without an extra state solve. The fixed-coarse-load surrogate remains allowed, and numerical benchmark failure is not asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
