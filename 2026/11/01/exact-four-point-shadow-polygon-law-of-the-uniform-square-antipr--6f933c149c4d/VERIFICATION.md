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

# Reproduction

Run `python3 verify.py` with Python 3.9 or later. It uses only the standard library and takes a few seconds on an ordinary machine. It independently builds the facet list from all vertex triples, computes 20,000 direct planar convex hulls, checks the analytic sign regime on all directions, compares the exact probabilities with separate angular quadrature, and compares the mean with the edge-by-edge exterior dihedral-angle identity.

The successful run produced probability values \(0.356758138764323\), \(0.600915394900956\), \(0.011795388796147\), and \(0.030531077538575\) for five through eight vertices. The absolute difference between exact formulas and numerical angular quadrature was below \(8\times 10^{-11}\), and the independent mean and four-outcome mean matched to displayed precision.

# Proof boundary

The universal result is established by the exact facet normal table, exhaustive sign regime division and elementary spherical integration in `RESULT.md`. The program is finite diagnostic verification, not a substitute for these steps or a certification of historical novelty. Independent audit: not performed.
