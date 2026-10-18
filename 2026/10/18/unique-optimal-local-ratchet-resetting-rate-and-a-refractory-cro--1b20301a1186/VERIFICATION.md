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
# Verification of the optimized local-reset ratchet

Run `python3 verify.py` from this directory. This uses only Python's standard library and prints the number of successful independent checks. A successful replay on the packaged source produced 116 assertions. The tests independently sum positive and negative lattice-jump tails and compare with the hyperbolic mean; check root bracketing, global maximality at selected rates, strict comparative statics, and the two singular scaling regimes.

Analytic ingredients checked separately are the bilateral-exponential exponential-time Brownian endpoint, geometric tail summation, regenerative strong law, and strict concavity of the log derivative through \(\sinh(\delta y)<\delta\sinh y\). Parameter-domain endpoints and nondimensional constants were checked in the proof. The program samples finitely many values; it is not an exhaustive certificate for all real parameter choices. No external independent audit has been performed.
