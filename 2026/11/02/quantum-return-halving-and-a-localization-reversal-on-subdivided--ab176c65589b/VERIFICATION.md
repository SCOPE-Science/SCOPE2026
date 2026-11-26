---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Independently, the original-vertex block of exp(-it A_S) is cos(t sqrt(B B^T)) by the power series, with B the unsigned incidence matrix. The constant zero-mode contribution has time-averaged square F_0(u,u)^2; distinct positive frequencies have vanishing cross terms and each cosine has mean square 1/2. The equation B^T f=0 forces opposite values on endpoints, so in a connected bipartite graph F_0(u,u)=1/n and otherwise it is zero. This also covers n=2 and nonregular graphs. On S(K_n), the positive squared frequencies 2(n-1) and n-2 have multiplicities 1 and n-1. Each signed eigenspace projects half its trace onto each bipartition, by the singular-vector pairing, and symmetry is transitive on each part. With part size k the weights per sign are 1/(2k) and (n-1)/(2k), and the remaining weight is 1-n/k. Taking k=n or k=n(n-1)/2 and summing squared weights recovers both fractions and their difference. The zero weight vanishes at n=3. The cubic factor is negative at 4 and 5, positive at 6, and increasing thereafter, giving the full cutoff and limits.

## originality

PASS

Credit the known average-mixing projector formula and standard incidence blocks. The inspected same-invariant and vertex/edge-walk literature does not establish the evaluated pointwise subdivision identity and the all-order two-orbit return comparison. The closest inspected indexed record concerns spectral inertia of a line graph of a subdivision, not the return invariant. This is a bounded scientific comparison, not a historical priority certification.

## value

PASS

The adjacency return invariant tests whether a once-subdivision transfers long-time return from hubs to newly inserted low-degree vertices. The exact clique cutoff answers this for all orders, and the edge-kernel term identifies the mechanism behind a limiting gap of 1/2 rather than just exhibiting a few examples. The pointwise identity also isolates exactly when bipartiteness prevents exact halving.

The dated certificate retains the supplied scientific assessment, sources and limitations.
