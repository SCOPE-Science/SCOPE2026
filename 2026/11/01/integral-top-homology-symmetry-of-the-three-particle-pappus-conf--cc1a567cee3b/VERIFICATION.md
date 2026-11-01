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

# Reproducibility checks

Run `python verify.py` (Python 3.10+, standard library). Compare its JSON output to the embedded `verification_output.json`. The verifier regenerates the Pappus graph from the LCF sequence, constructs 6,528 top generators and 16,524 degree-two generators, calculates the complete boundary rank over the prime field of order 101, and lifts seven sparse kernel vectors to exact integral cycles. It checks all integer boundaries and their seven free coordinates, proves the integral kernel-basis property, enumerates 216 automorphisms, and checks every transformed integral cycle against its integer basis coordinates. It also constructs every conjugacy class, group kernel, character scalar product, and the eigenspace dimensions of a central involution class sum.

Additional direct exact elimination checks at primes 103 and 1009 gave the same 6,521 boundary rank, free positions and support sizes; these are secondary consistency tests, not a substitute for integer-cycle equality. The rank certificate and seven integer cycles together give the complete integral top-homology statement. All scientific checks described here were performed before acceptance. No independent mathematical audit has been performed.
