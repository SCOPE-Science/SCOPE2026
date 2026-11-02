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

Place `certificate.json` and `verify.py` in the same directory, then run `python3 verify.py` (Python standard library, no solver and no other downloads). The script checks both independent deletion-shadow implementations for every binary word at lengths \(2\) through \(8\); every listed codeword has a disjoint shadow from every other; every rational primal and dual feasibility inequality is evaluated exactly; all \(77\) upper-bound cliques are tested pairwise; every length-eight word meets weighted coverage at least one; the exact rational clique-cover weight is \(482/23\). It then prints `VERIFY_OK`.

Certified integer values: \((1,2,4,4,8,13,20)\). Certified fractional values: \((1,2,4,4,8,13,21)\). In particular, the first strict fractional matching gap is at \(n=8\).

This certificate validates the stated finite case by elementary arithmetic and exhaustive checking. It is not a published independent assessment, a proof for all lengths, or a substitute for historical source comparison. Independent audit has not been performed.
