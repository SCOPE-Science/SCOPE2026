---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

The actual constructor and verifier were read completely, along with the filed instance. They independently rebuild GF(16), PG(2,16), the 65-point Hermitian unital, 208 secants and 65 tangents, reconstruct the 65 size-16 cliques and the seeded bipartitions, and require exact equality with the filed adjacency. The verifier exhaustively counts K4s as zero and checks every one of the 595 pairs in the explicit 35-vertex witness is a nonedge. Thus the precise conclusion alpha>=35>26 for this seeded 208-vertex instance is certified; no exact-alpha claim is made.

## originality

PASS

The Mattheus-Verstraete paper defines the Hermitian-unital random block construction for general q and proves asymptotic pseudorandomness for sufficiently large q, but its inspected full text does not give this q=4 seeded instance or the 35-vertex independent witness. Fresh Resultary search found only the audited record as an exact match.

## value

PASS

The q=4 case is the smallest natural parameter of the Hermitian-unital Section-3 construction, and the explicit witness decisively refutes the proposed N/8 upper window for a fully specified realization while retaining K4-freeness. As a finite boundary/counterexample for extrapolating the asymptotic construction to its smallest parameter, this has a clear mathematical use despite not determining exact alpha.

The dated certificate retains the supplied scientific assessment, sources and limitations.
