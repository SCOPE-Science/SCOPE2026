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

# Verification

From this folder run `python verify.py` with Python 3 and SymPy (tested with the installed SymPy). The checker independently constructs each friendship graph and its grounded Laplacian, verifies exact rational inverses, and symbolically recomputes the seven polynomial comparison identities from the block-inverse formula.

Observed outcome: `VERIFY_OK symbolic_identities=7 exhaustive_direct_inverse_comparisons=1984 large_graph_sample_checks=36`.

The symbolic checks cover identities for arbitrary positive gain and symbolic integer blade count; positivity of denominators, coefficients, and the size-eight discriminant, together with Descartes' rule for the size-three quartic, establish the infinite-domain classification by hand. The 1,984 direct inverse computations span every four-leader set on networks with two through five triangles at four positive rational gains; the 36 larger-size checks are illustrative rather than exhaustive. No external expert/independent audit, formal proof-assistant certification, or exhaustive historical-priority certification is claimed.
