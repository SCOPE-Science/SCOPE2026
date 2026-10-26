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

# Verification

Run `python3 check_incidence.py` and `python3 check.py` using Python 3 standard library only. The first script tests seven finite incidence-algebra configurations over \(\mathbb F_2\) or \(\mathbb F_3\), solving the witness equations \(axa=a\) by modular row reduction independently of the Schur-complement criterion, totaling 22,156 algebra elements. The second script checks nine square-zero configurations over \(\mathbb F_2,\mathbb F_3,\mathbb F_4\), 97,829 elements in total, 99 complete witness-enumeration cases, and twelve numerical phase-theta comparisons. Expected outputs are in `incidence_output.txt` and `check_output.txt`.

The scripts test finite instances; they cannot establish the theorem for all finite posets or the infinite limit. The proof of the latter uses strict ratio monotonicity, a phase-uniform local product estimate, and summable discrete Gaussian tails. No independent audit has occurred.
