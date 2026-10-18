---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Reconstructed all four rational-canonical GL_2 conjugacy cases: scalar (one identity d=8, other scalars d=0), Jordan unipotent (d=4 exactly in characteristic 2, else d=3), split semisimple (tensor eigenvalue multiplicities 3,3,1,1; directed squaring and cubic-root exception), and irreducible quadratic semisimple (exactly one d=2 class when q is 2 mod 3). Similarity-class cardinalities are 1, q^2−1, q(q+1), q(q−1). Their weighted sum produces the posted six N_k(q) formula for every prime power. Independent direct rank computation over GF(2),GF(3),GF(4),GF(5),GF(7) exhaustively enumerated GL_2 and matched N_k and group orders; these finite cases corroborate rather than establish the all-q theorem.

## originality

PASS

Verhulst 2020 Lemma 3.3 and Theorem 3.4 express the orbit count as a Burnside sum over the tensor-fixed dimensions and work out q=2; the Outlook asks for the all-q distribution. Petersson–Scherer 2004 supplies the summed count of 2-dimensional algebras, which is not equivalent to the six separate N_k(q). Querying published mathematical records returned the assigned finding as top self-hit, with other finite-field spectral results on different invariants; no independently earlier equivalent distribution was identified.

## value

PASS

The full q-uniform fiber distribution of a natural GL_2 tensor representation is an explicitly posed gap; it resolves which stabilizer dimensions occur and their frequencies, strictly more informative than a Burnside weighted orbit total. The proof isolates representation resonances relevant to general higher-dimensional cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
