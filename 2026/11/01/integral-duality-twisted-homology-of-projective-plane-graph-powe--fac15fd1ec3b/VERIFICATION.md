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

The bundled `verify_incidence_equiv.py` is a standalone Python 3 program using only the standard library. Execute it from the containing directory with `python3 verify_incidence_equiv.py` and compare its stdout byte-for-byte with `verification_output.txt`. It checks Fano-plane incidence axioms, shortest-path Rips faces, all 168 class-preserving projective automorphisms, all 168 dualities, all 336 signed Lefschetz characters, an integral eight-cycle basis, the order-two polarity matrix, its trace and its rank modulo two, and character irreducibility by the exact inner product.

The unrestricted theorem is supported by the explicit Mayer–Vietoris proof in `RESULT.md`; the finite program does not attempt to certify all orders. The older nonequivariant homotopy equivalence is prior work, not a fresh claim here. Independent mathematical audit has not been performed.
