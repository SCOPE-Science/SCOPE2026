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

# Reproducible verification

The theorem concerns the unweighted combinatorial Laplacian and the physical Crank–Nicolson step \(h=2s\). The all-graph proof rests on: the exact resolvent identity \(C=2R-I\), the coefficientwise closed-walk domination by the \(\Delta\)-regular covering tree, the Schur-complement cavity equation, and dominated convergence on finite tree balls. No finite computation substitutes for those arguments.

Run `python3 verify.py` with the Python 3 standard library. The script verifies:

- Exact-rational cavity equations and the identity \(g_\Delta(\sigma_\Delta)=1/2\) for nine integer degrees from two through ten.
- Exact-rational positivity at the universal bound for every connected labelled simple graph on two to five vertices (\(771\) graphs).
- Exact-rational positivity at the bound and negativity at \(s=11\sigma_\Delta/10\) for center vertices of degree-two, degree-three and degree-four radius-two regular-tree balls.

Observed output ends with `VERIFY_OK`; the exact negative center diagonals for degree two, three and four are \(-347/13645\), \(-64/1817\) and \(-12855/324713\), respectively. The all-degree sharpness statement uses a limit of increasing finite trees, not these three specific finite witnesses. Supplementary numerical tests examined \(994\) connected atlas graphs of order at most seven; rounding-dependent numerical checks are not certificates of an infinite claim.

The manuscript's originality comparison has only bounded source coverage and does not establish independent publication priority. The 2005 Horváth paper could be checked at full text by an independent specialist.
