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

Run `python3 verify.py` with Python 3. The script computes exact integer utilities for every committee and every nonempty affordable candidate proposal in its tested finite ranges. For a proposed set, it counts all voters who strictly improve, so a blocking coalition exists exactly if that count meets the Hare quota. It compares this independent direct procedure against the vacant-triple characterization and central-trinomial count.

Recorded half-budget cases \(n=2k\) for \(1\le k\le6\) have \(2,6,14,38,102,282\) core committees, respectively. All sub-half-budget instances through \(n=9\) also pass. The attached `verification_output.txt` lists every checked parameter pair.

The general theorem is established by the incidence-bound proof in `RESULT.md`, not by extrapolating finite computations. The limit formula uses the standard lattice local central limit theorem and Stirling's approximation; the verifier does not certify asymptotic convergence. Independent audit or validation has not been performed.
