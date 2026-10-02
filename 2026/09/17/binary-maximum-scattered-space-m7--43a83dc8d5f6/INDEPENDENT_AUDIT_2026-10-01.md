# Independent scientific audit — SCOPE-20260917-43a83dc8d5f6

Audited at: 2026-10-01T05:14:16.390825Z

Disposition: **passed**

## Correctness — PASS

The field arithmetic convention was independently reconstructed. The ten displayed vectors have binary rank ten. For every one of the 126 scalars outside the base field, the combined binary rank of U and its scalar multiple is exactly twenty, so their intersection is zero. This excludes two independent U-vectors on one ambient field line. The standard Desarguesian-spread bound is floor(21/2)=10, hence the construction is maximum scattered. Independent exact recomputation reproduced the rank-ten basis and all 126 rank-twenty tests; the coding consequence then follows from the cited extremal-code/scattered-subspace characterization.

## Originality — PASS

The 2026 rank-metric-intersecting-code paper reduces extremal length to scattered subspaces of dimension m+3 and says known constructions yield the needed extremal codes when m is even; it does not supply the binary m=7 instance. Earlier odd-m dimension-three constructions inspected have rank m+2, while general scattered-space literature explicitly notes that maximum existence is not known in general when the ambient product is odd. Searches for F_128, q=2, m=7 and dimension ten found no earlier explicit construction.

### Equivalent formulations

No equivalent explicit witness was found.

### Broader coverage

These broader results motivate and bound the construction but do not imply a dimension-ten scattered binary subspace for m=7.

### Exact database or table

The exact finite construction appears absent from the searched databases.

### Claim versus prior implication

The explicit rank-ten witness supplies a genuinely missing existence statement rather than a parameter substitution into a general construction.

## Value — PASS

This is a natural smallest unresolved odd-parameter extremal existence instance after the cited m=5 obstruction, and it immediately yields an extremal rank-metric intersecting code. The exact finite witness is therefore a motivated object, not an arbitrary isolated computation.

## Sources inspected

- On the existence of linear rank-metric intersecting codes — https://arxiv.org/abs/2604.02004. NOT_COVERING: Does not provide the q=2,m=7 construction.
- Generalised Evasive Subspaces — https://arxiv.org/abs/2207.01027. NOT_COVERING: Provides the bound and open landscape, not this witness.
- Short Rank-Metric Codes and Scattered Subspaces — https://doi.org/10.1137/23M1574749. NOT_COVERING: The construction has rank/length m+2 rather than the m+3 scattered dimension needed here.

## Checked sources

- https://arxiv.org/abs/2604.02004
- https://arxiv.org/abs/2207.01027
- https://doi.org/10.1137/23M1574749
- https://arxiv.org/abs/2402.15223
- Resultary exact parameter search

## Residual risks

- Older finite-geometry computations may contain an equivalent q=2,m=7 witness without modern rank-metric terminology.
- The coding-theoretic consequence relies on the cited 2026 characterization; the scatteredness certificate itself is independently exact.

## Limitations

- Only q=2,m=7 is constructed; no classification or general odd-m theorem is claimed.
- Originality is best-of-knowledge and remains exposed to older computational finite-geometry literature under different terminology.
