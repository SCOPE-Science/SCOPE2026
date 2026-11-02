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
# Finite verification

Run `python3 verify_wagner.py` with Python 3 and no third-party dependencies. On a successful run the checker prints `WAGNER_TWO_POINT_INTEGRAL_DIHEDRAL_LATTICE_OK`. It reconstructs 28 zero-cells, 72 one-cells and 42 two-cells; checks integral cubical boundary composition; calculates rational ranks 27 and 40; and checks two explicit primitive two-cycles with coordinate projection equal to the identity. It checks cellular boundary equivariance under all sixteen graph automorphisms and the exact generator actions. Using rational Gaussian elimination, it computes quotient rational Betti triples (1,0,0), (1,1,1), (1,2,1) for full dihedral, rotation, and chosen reflection subgroups. The finite arithmetic is exact; no finite sample is used to infer an infinite-graph classification. The equivalence between the cubical and continuous configuration spaces uses the cited stable-equivalence theorem under the checked graph subdivision hypotheses.
