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

# Computational and mathematical verification

Execute `python3 verify_rectangle.py` with the Python 3 standard library. The checker independently lists all 16 spanning trees, calculates unique cut flows using graph connectivity, verifies exact rational inequalities for all tree flow triples at seven nontrivial aspect ratios, reproduces each exact centered secant, and checks 3,080 varied boundary/random tangent loads; its output was `PASS: 16 exhaustive spanning trees; 3192 total exact/rand comparisons; all sharp witnesses and bounds verified.` The mathematical proof is not a consequence of finite sampling. Its continuum upper bound uses a concavity certificate in the sole potentially dominant sign sector and analytic comparisons in the remaining three sectors. The lower certificate is an exhaustive symbolic 16-tree enumeration displayed in the main result.

Scope: only the real exponent \(p=1/2\), four Manhattan-rectangle vertices, and the canonical bilinear map. A broader equivalent theorem may exist outside inspected material. Independent validation has not been performed.
