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

# Verification of rectangular one-type spectrum

`verify_grid.py` requires Python 3 and only its standard library. Run `python3 verify_grid.py`; the expected output is included as `verification_output.txt`.

Three separate finite checks were executed. The first compares the proposed closed binomial expression against its unsimplified double-convolution identity over all \(0\le a,b\le16\) (289 configurations). The second explicitly enumerates all bitmasked down-sets and up-sets and tests the cross-order condition for 29 small grids, including the \(4	imes4\) grid. The third enumerates every ternary relation state of a new point to each named grid vertex and checks all transitivity implications of the full strict order, for 24 configurations. The direct checker does not call the closed formula to generate relation states. All assertions pass; the run concludes with `ALL_TESTS_PASS`.

The checker establishes finite agreement only. The general theorem is justified by the written coordinate-maxima bijection and a marked-lattice-path convolution calculation in the proof. No external independent scientific audit or validation was performed.
