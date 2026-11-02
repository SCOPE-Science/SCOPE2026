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

Run `python verify.py` from this directory with `construct.py` and `quartet_certificate.json` present. To reproduce the certificate itself, run `python construct.py` first. The tools use Python's standard library only; no package installation or external data are needed. The graph edge-subdivision enumeration has exactly \(945\) distinct seven-leaf binary topologies, and the independent root-attachment construction gives the same \(945\) Boolean vectors using quartet four-point distances.

Actual extracted-program output:

```
SUBDIVISION_ENUMERATOR_PASS 945
INDEPENDENT_ROOTED_FOUR_POINT_PASS 945
VC_UPPER_SEVEN_IMPOSSIBLE_PASS nodes 206992
VC_LOWER_SIX_PASS patterns 64
LITTLESTONE_DEPTH_NINE_PASS internal_nodes 511 distinct_leaves 512
SEVEN_LEAF_QUARTET_C_AND_CERTIFICATE_ALL_PASS
```

`verify.py` independently evaluates the quartet incidence matrix for the exhaustive seven-query upper search, checks all six-coordinate witnesses, and replays every depth-nine adaptive root-to-leaf path. The upper bound on adaptive depth follows separately from \(945<1024\). All data are finite, and no inference is made for more than seven leaves or for nonbinary phylogenetic trees. Scientific historical priority remains a limited-literature finding, not an independent certification.
