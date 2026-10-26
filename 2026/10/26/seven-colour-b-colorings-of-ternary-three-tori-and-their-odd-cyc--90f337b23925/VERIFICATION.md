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

# Reproducibility and exact finite checks

The working package contains `certificate.json`, `verify.py`, and `verification_output.txt`. Invoke `python verify.py` with a standard Python 3 interpreter. No network access or third-party modules are required. The 81 prescribed colours use the row/column/axis orientation stated in `RESULT.md`.

The verifier constructs graph edges once, checks that exactly six incident edge colours are distinct at every vertex, enumerates **all simple four-cycles via adjacency** rather than relying on an assumed product-square list, and checks four different colours on every cycle. It reports 27 vertices, 81 edges, 81 four-cycles, and seven colours for the seed. Direct tests are also executed for five larger lifted instances, up to 1215 vertices and 3645 four-cycles. The recorded output is from the exact bundled verifier and certificate.

The infinite family is established by the graph-covering and parity-count proof in `RESULT.md`; the finite tests alone do not prove it. The certificate does not establish uniqueness of the optimum or any claim outside odd triple factors divisible by three. The scientific result has not undergone independent mathematical validation.
