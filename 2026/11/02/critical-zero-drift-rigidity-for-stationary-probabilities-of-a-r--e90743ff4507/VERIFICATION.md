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

# Verification of the mathematical claim

The proposition uses a bounded test function and requires no limiting interchange with a nonintegrable \(\log x\): all stationarity identities apply first at finite \(M\). The limit of the lower-branch bound is justified by continuity from above of a finite measure on sets excluding \(0\). The upper-branch test is uniformly negative on each compact interval away from endpoints. For \(0<x<1/2\), strict finite itineraries to \(1/2,1\) exist by excluding countably many slope choices; the endpoint \(x=1/2\) enters directly using the stipulated left branch. Each itinerary persists on an open positive-measure parameter cylinder. Stationarity of each \(P^n\) gives the countable-union argument.

Run `python verify.py` with standard-library Python 3.11 or newer to reproduce: high-precision root bracketing and the defining zero-mean identity, endpoint fixed-point tests, and exact-rational sample reachability using nonexceptional slopes. A finite sample does **not** prove the theorem, and exact symbolic inequalities above are the proof for arbitrary points and invariant probabilities.

No independent audit or externally validated proof certificate has been performed.
