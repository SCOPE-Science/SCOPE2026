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

# Reproducibility and verification

Run `python verify_star_uncentered.py` with standard-library Python 3. The checker independently enumerates all graph balls on stars of bounded size, evaluates each maximal average directly with rational arithmetic, and compares that definition with the compact analytic formula. The normalized exhaustive grid uses \(488{,}280\) input configurations, and the separate direct-ball calculation covers \(3{,}276\) graph inputs. Exactly \(100\) additional rational single-leaf extremizers supplement the initial eight grid witnesses.

The code checks the exact edgewise bound \(|L_i-H|\le|t_i|/2+[(k-1)/(2(k+1))]\sum_{j\ne i}|t_j|\) and the summed sharp bound. It uses no numerical tolerances. These finite checks do not certify all real inputs or arbitrarily many branches; the general theorem rests on the explicit ball-list argument, complete case split, and equality calculation given in `RESULT.md`. No independent audit has been performed.
