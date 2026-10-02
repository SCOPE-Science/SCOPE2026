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

The proof was reconstructed from the frozen RESULT.md rather than inherited from the prior review. Writing d=m+1 and applying the disk automorphism at a=f(0) gives h(z)=z^d phi(z); because 2d>d+k for 0<=k<=m, the degree-(d+k) section is exactly a+(1-|a|^2)z^d S_k phi. Maximizing over a reduces contractivity sharply to 2 r^d M_k(r)<=1. For the classical Schur functional, the Szász extremal polynomial P_{k,r}=r^{k/2} sum_{j=0}^k b_j(z/r)^j has P_{k,r}^2 matching the required first k coefficients and gives M_k(r)=sum b_j^2 r^{k-2j} whenever P_{k,r} is zero-free. Enestroem-Kakeya gives the stated q_k interval; the k=3 cubic roots have moduli about 1.526 and 1.448, exceeding 4/3. Substitution reproduces all four displayed algebraic radius equations, and the fixed-k logarithmic asymptotic follows by taking logarithms of the exact root equation. No finite experiment is used as an infinite proof.

## originality

PASS

The closest recent primary result of Das--Sarkar treats the ordinary Neil algebra and states the single cubic radius 4r^3+r-2=0. Kovalev supplies the classical sharp segment/zero-free machinery used as an ingredient, not the higher-Neil reduction or the family of early-section radii. Resultary returned the audited record itself but no earlier higher-Neil theorem with the same implication. Older section literature was searched by aliases; no source inspected or retrieved stated a theorem covering all N_m early sections or the fixed-offset asymptotic.

## value

PASS

The result gives a natural exact extension of a newly studied Neil-algebra radius problem to the higher gap algebras, identifies the Schur functional controlling all pre-quadratic sections, and yields explicit sharp first radii plus a fixed-offset asymptotic. These are structural gap-dependent laws rather than an arbitrary finite slice or numerical recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
