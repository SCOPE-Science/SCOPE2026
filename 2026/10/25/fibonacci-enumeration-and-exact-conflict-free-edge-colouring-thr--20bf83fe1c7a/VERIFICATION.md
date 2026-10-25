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

The proof handles every integer number of arms \(k\ge3\) and every positive integer length vector; it uses no infinite extrapolation from the finite checker. It reduces the central-spoke conditions to four disjoint cases, proves a Fibonacci path-tail lemma including its \(L=2\) base case, and verifies the exact positivity obstruction and three-colour upper bound.

To reproduce the independent finite checks run `python verify.py` in the directory containing the verifier. `verify_output.txt` contains the output of the shipped script. The verifier constructs the actual spider graph and closed edge neighbourhoods from edge incidences; it directly tests each binary edge-colouring and does not reuse the symbolic central-vertex constraints in its enumeration.

The tests cover 300 systematic nondecreasing arm-length profiles with \(3\le k\le6\), positive lengths at most eight and total edge number at most fourteen; and 56 seeded sampled profiles with \(3\le k\le8\) and at most seventeen edges. The positive-index classification is checked for every profile, together with named small obstruction and non-obstruction witnesses.

Expected output: `VERIFY_OK tested_profiles=356 systematic=300 sampled=56`.

These computations are finite corroboration only; they do not constitute exhaustive coverage of unbounded spiders. Independent mathematical audit has not been performed.
