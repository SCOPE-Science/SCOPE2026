---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Let N be projective-point to k-subspace incidence, v=[n]_q, r=[k]_q, B=#Gr_q(n,k). Transitivity on ordered distinct projective points gives Gram N*N=aI+bJ with a=Br(v-r)/(v(v-1))>0, so H_{<=1}=ran N has dimension v and contains constants. On the P0-star, point columns identify with quotient projective points of V/P0 (q lifts each), so RN has rank v'=[n-1]_q; its mean-zero permutation constituent is irreducible over C by double transitivity. Compression S=RPR* acts as scalar on that constituent and as 1 on constants because 1_A is itself an incidence column. Trace of P M_A P is [k]_q, giving theta=([k]_q-1)/([n-1]_q-1)=[k-1]_q/[n-2]_q; zero eigenspace has dimension v-v'=q^(n-1). For k=n-1, theta=1 correctly merges eigenvalue multiplicities. Nonzero singular values and optimal minimum-energy extension norm follow from the singular-value theorem. Independently recomputed finite q=2,3 trace/rank identities; finite q<=4 checker cannot prove all-prime-power theorem, but proof does.

## originality

PASS

Best-of-knowledge comparison of mathematical statements and implications against named primary sources, published findings and exact source-object searches. The current Resultary hit for the very assignment under audit is not independent novelty evidence. A mirror of this assigned 2026-10-11 finding returned as the highest-ranked Resultary hit is not counted as independent prior art.

## value

PASS

A fixed-point Schubert star is a canonical parabolic subgeometry, and point incidences are the first nonconstant Grassmann frequency band. A complete all-size/all-prime-power restriction spectrum with rank, dimension-independent-in-k nullity and exact best minimum-energy interpolation operator norm is independently useful in finite harmonic sampling and incidence combinatorics; not a finite enumeration or incidental spectral example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
