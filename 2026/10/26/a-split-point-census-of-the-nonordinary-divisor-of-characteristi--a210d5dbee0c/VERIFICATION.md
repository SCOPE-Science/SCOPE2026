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
# Reproducibility and limitations

Run `python3 verify_picard5.py` with any standard Python 3 implementation. The script checks the relevant coefficient identities over the prime field and independently tests the quartic squarefree criterion. It constructs exact extensions of sizes 5, 25, 125 and enumerates the smooth monic centered quartics by coefficients. Expected totals `(smooth,rank0,rank2)` are `(100,16,84)`, `(15000,576,14424)`, and `(1937500,15376,1922124)`; successful replay ends in `VERIFY_OK`.

The universal proof is symbolic and contained in `RESULT.md`: Cartier action, discriminant identity, two inverse morphisms, squarefree polynomial count. Finite computations alone cannot establish generality over all finite extensions. The characteristic is five, and geometric isomorphism counts, Newton polygons, full Ekedahl–Oort strata and the singular boundary are not asserted. Historical equivalence and priority need further inspection of older specialized literature. Independent mathematical audit has not been performed.
