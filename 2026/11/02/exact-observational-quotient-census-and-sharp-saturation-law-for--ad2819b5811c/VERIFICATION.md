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

Reproducibility file: `checker.py` (Python 3 standard library only). Execute `python3 checker.py` from the directory containing this document. All programmatic checks have executed and reported `ALL_CHECKS_OK`.

The program compares exact direct and EGF enumeration for \(m=2, n\le5\) and \(m=3, n\le5\); validates the general model total \(m^nB_n\) for \(m=2,n\le6\) and \(m=3,n\le5\); and independently enumerates the generated value functions of finite Heyting chains under pointwise lattice operations, implication, exact tests and \(\Box\) to verify logical indistinguishability against the support-pair criterion for \(q=2,n\le4\) and \(q=3,n\le3\). A recurrence computes the exact number of size-\(n\) models omitting a specified singleton support through \(n=350\).

The all-size formulas have separate combinatorial proofs. The asymptotic proof uses a conventional saddle-point expansion with an explicit quadratic displacement correction. No finite computation certifies the infinite asymptotic. The historical coverage check is limited to the specifically inspected papers and searches; an independent scientific audit has not been performed.
