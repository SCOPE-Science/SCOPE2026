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

# Verification evidence and boundaries

Run `python verify_fibonacci_geodesics.py fibonacci_geodesic_certificate.json` using Python 3.8 or newer. The checker generates all valid binary words without adjacent ones, enumerates each graph edge from one-bit flips, checks each provided path word-by-word, confirms endpoint Hamming distance equals the number of steps, and confirms that all edges are covered. It checks exactly \(8,13,21\) geodesics at \(n=6,7,8\), the expected graph sizes, and \(2F_n\) outer-class edges. The supplied `verification_output.txt` records a clean execution of the checker; a separate independent breadth-first-search test reproduced every endpoint geodesic distance. The certificate, not the recorded output, is the finite proof witness. No extrapolation to higher dimensions is verified; independent scientific audit has not been performed.
