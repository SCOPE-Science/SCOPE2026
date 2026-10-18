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

# Verification of the parity classification

The proof in RESULT.md uses the published exact coefficient formula and a local two-adic factorization; the analytic counting argument uses the prime number theorem for the reduced classes \(3,5\pmod8\). The program `verify.py` is a standalone supplementary exact-arithmetic test, not a finite substitute for the infinite proof.

Run `python3 verify.py` with the Python standard library. It independently enumerates signed representations for \(1\le n\le109\), recomputes \(\sigma\) and \(\lambda\), compares the exact coefficient identity and the proposed parity predicate for \(1\le n\le200000\), and prints a finite normalized ratio and the predicted asymptotic constant. The ratio at a finite cutoff is not an error bound or convergence proof.

The OEIS A192717 prime-congruent-to-three subfamily is prior art. No independent audit or independent validation is claimed.
