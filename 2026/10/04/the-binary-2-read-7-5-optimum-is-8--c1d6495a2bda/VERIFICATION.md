---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

For binary adjacent multisets, the pair is determined by its sum, so the read distance is ordinary Hamming distance between eight-symbol sum vectors. The compatibility graph therefore has exactly the 128 binary words as vertices and codes are cliques. The bundled verifier proves the clique number by two exact searches, and a fresh independent branch-and-bound reconstruction in this audit again returned clique number \(8\). The displayed eight-word set was checked pairwise. The classical comparison follows independently from the radius-one Hamming bound and the length-seven Hamming code.

## originality

PASS

Sun--Ge's full primary text proves that every \(2\)-read \((n,5)_q\) code is a classical \((n,3)_q\) code and derives only the Hamming-bound redundancy lower bound and asymptotic constructions. For \(q=2,n=7\) that prior reduction permits \(16\) codewords, so it does not imply the exact value \(8\). Searches found no indexed exact \((7,5)_2\) optimum or finite table containing it.

## value

PASS

This is a natural first perfect-Hamming-length benchmark for the distance-five \(2\)-read problem. The exact value demonstrates that the read-vector constraint costs a factor of two beyond the known classical-distance reduction, so the finite invariant is mathematically motivated and useful for calibrating general bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
