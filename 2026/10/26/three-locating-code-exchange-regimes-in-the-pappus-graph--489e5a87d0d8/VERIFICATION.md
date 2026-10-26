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

# Reproduction and limitations

`verify_lcf.py` starts from the eighteen-cycle with repeated LCF shifts, checks cubic degree, exhaustively generates every minimum candidate by cardinality, and constructs all code exchanges. It computes every OLD eccentricity, both ID majority components, all three exchange counts, and the full degree profiles. Execution ends in `ALL_LCF_CHECKS_PASS`.

`verify_incidence.py` starts independently from nine explicit point-line triples. It verifies an explicit label map to the LCF graph, tests each code with ordinary Python sets, independently enumerates all minimum code families and exchanges, verifies that the two ID majority classes are separately connected and uncrossed, and reconstructs the OLD factor graph from all \(\binom95=126\) five-point choices. It verifies the count of forty-five valid five-point configurations, their geometric incidence profiles, the point-line duality, and each factor's full eccentricity profile. Execution ends in `ALL_INCIDENCE_CHECKS_PASS`.

To replay, place all embedded files in one directory and run:

```
python3 verify_lcf.py
python3 verify_incidence.py
```

Compare standard output to `verify_lcf.out` and `verify_incidence.out`. Both checker programs use only the Python standard library. They do not require a paper download, a precomputed table, an external solver, or any file not embedded with this finding.

The general degree-counting arguments supply independent lower-bound reasoning for LD and OLD; the nontrivial ID lower bound and all finite exchange counts use explicit complete enumeration. A finite exhaustive certificate applies to this fixed finite graph, not to arbitrary cubic graphs. A self-review checked these calculations, their mathematical meaning, their source comparisons, and the scientific limitations. No independent audit was performed.
