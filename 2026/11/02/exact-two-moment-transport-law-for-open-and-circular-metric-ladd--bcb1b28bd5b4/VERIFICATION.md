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

# Mathematical checks and limits

Run `python verify_ladders.py` with Python 3 in the same directory. It imports only the standard-library modules `collections` and `fractions`, builds the two metric graphs for each integer order from 3 through 9, uses breadth-first search to obtain all vertex distances, clips endpoint-route affine envelopes into exact rational polygons, integrates the affine distance and its square exactly, and compares both results with the claimed formulas as exact fractions.

Observed execution: 14 networks, 2,401 distinct unordered metric-edge pairs, and 4,802 exact rational moment comparisons; every comparison passed. There is no floating-point tolerance. The verifier independently builds the geometric distance integrals rather than reusing the conditional-moment proof formulas. The algebraic proof applies to all integer orders at least three; finite checks alone would not prove that universal claim.

The strict inequality is proved by an all-positive coefficient polynomial expansion, and the scaled distributional claims follow from explicit bounded couplings, not empirical sampling. No independent audit or external mathematical certification is claimed. Historical priority remains subject to accessibility of earlier literature, especially the full 1982 account.
