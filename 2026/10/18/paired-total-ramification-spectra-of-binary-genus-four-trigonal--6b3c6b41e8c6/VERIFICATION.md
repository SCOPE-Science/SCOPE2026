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

# Verification record

Run `./run_checks.sh` from the extracted package root with C++17, Python 3 and SymPy. Observed replay: 49,515 explicit singularity witnesses were independently verified; 16,020 survivor sections split into 252 orbits; exact Gröbner unit ideals held on all 1,008 representative charts; direct and orbit-weighted paired total-ramification tables agreed; 1,128 four-or-more-total-fibre sections were geometrically singular (1,110 rationally, 18 in one orbit over a quadratic extension); and the two equal-zeta witnesses gave N1..N4=(2,8,17,20). All checks passed. See `data/run_report.txt` for the combined logged output and `data/census.json` for the complete orbit representatives.

The finite-extension witness search excludes curves but does not alone prove the remaining curves smooth. This is why exact Gröbner bases on four charts of all 252 orbit representatives are essential. The isomorphism-class identification additionally uses the canonical uniqueness of the containing split quadric.

No independent external audit or validation has been performed. An unindexed or unpublished equivalent prior enumeration cannot be ruled out by the searches performed.
