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

# Reproducibility and scope
The complete signed-degree argument in `RESULT.md` proves the infinite-class statement. The supplementary `verify.py` script constructs 19 finite connected cubic graphs, computes each efficient dominating set directly from its closed-neighbourhood definition, computes each valid binary edge-colouring by checking the four adjacent edges for every edge, and asserts equality between the *sets* of observed and predicted edge-colourings. The number of observed named colourings equals twice the number of efficient dominating sets in every tested instance. All 19 checks passed, as documented in `verify_output.txt`, ending in `VERIFY_OK 19 graph instances`.

Execute `python verify.py` with Python 3 and `networkx` installed. The script enumerates finite examples only and does not claim exhaustive coverage of cubic graphs of all orders. The full theorem relies on the exact degree-pair proof, not any finite extrapolation. The sources were compared to the precise claim, but neither exhaustive indexing of all publications nor an independent mathematical audit has been performed.
