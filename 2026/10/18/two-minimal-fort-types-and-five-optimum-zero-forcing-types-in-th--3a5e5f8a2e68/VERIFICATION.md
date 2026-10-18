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

# Reproducible finite verification

The attached graph-independent input is the Fano incidence definition: nonzero three-bit vectors are points, and the seven XOR-zero triples are lines. `verify_forcing.py` computes ordinary synchronous color propagation over all \(16384\) masks, identifies inclusion-minimal forcing sets, checks forts and all proper-subset fort minimality via a Boolean-submask recurrence, and constructs all \(336\) graph automorphisms through Fano collineations and a polarity. It verifies that the orbit representatives and counts in `heawood_certificate.json` exhaust the computed sets.

`verify_forts.py` builds a separate point–normal orthogonality model, checks all proper subsets of each fort directly, counts seed sets by hitting the \(70\) minimal forts, and independently checks ordinary color propagation on every possible mask. Its vertex-conversion routine checks each certificate representative in the second model. Both verifiers use only the standard Python library and the files accompanying this document.

Run `python3 verify_forcing.py heawood_certificate.json` and `python3 verify_forts.py heawood_certificate.json` from the package directory. Accepted outputs contain `VERIFY_DIRECT_OK`, `VERIFY_GEOMETRY_OK`, `VERIFY_OBSTRUCTION_OK`, `VERIFY_FORTS_OK`, and `VERIFY_HITTING_OK`. The exact target polynomial coefficients are \(700,1904,2401,1862,987,364,91,14,1\) at degrees \(6\) through \(14\). There are \(70\) minimal forts in orbits of sizes \(14\) and \(56\), and \(700\) minimum forcing sets in orbits of sizes \(28,168,168,168,168\).

Limits: finite exhaustion does not establish an all-order statement for other projective planes, and the computations do not constitute an independent external audit or a proof that the result was never published. A fort is defined by the ordinary zero-forcing rule, not its positive-semidefinite or skew variants.
