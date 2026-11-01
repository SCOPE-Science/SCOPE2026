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

# Verification protocol

The companion standalone `verify.py` uses Python standard-library modules only. Run `python3 verify.py` from this directory. The successful execution prints `VERIFY_OK 24-cell width` followed by the 96 closest-pair count and the exactly evaluated upper-regime mass.

It constructs the 24 unit vertices using rational arithmetic, checks their complete pairwise Gram profile (12 antipodal pairs, 96 pairs at inner product minus one-half, 72 orthogonal pairs, 96 pairs at one-half) and all 2,024 vertex triples. It confirms that every vertex has exactly eight neighbors. At six parameters it evaluates the two-cap Euclidean disk area both by the closed formula and by a separately coded deterministic one-dimensional Simpson integral. It checks the leading quadratic coefficient near the pair-tangency threshold. It then samples 180,000 fixed-seed uniformly random directions on the three-sphere, directly maximizes over all 24 vertices and compares observed tail frequencies at nine points against the exact 24-single-minus-96-double formula.

The sampling tolerance is a numerical diagnostic. The analytic geometric proof supplies the continuum result and the smoothness statement. The program does not check inaccessible primary papers or establish historical uniqueness. Independent external scientific audit has not been performed.
