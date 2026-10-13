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

# Finite verification and mathematical limits

Run `python3 checker.py` using Python 3.11 or newer. The program requires only the standard library and regenerates all endomorphisms from their generator images for \(n=1,2\) over \(\mathbb F_2\). It tests each map for composition idempotency, compares each ordered pair by exact composition for commutativity, computes binary linear ranks, and compares every pair-rank and pair-product-rank multiplicity with the theorem's separately derived orbit-and-shear formula. The observed individual retraction counts are \(2\) at \(n=1\) and \(98\) at \(n=2\); there are \(4\) ordered commuting pairs at \(n=1\), and \(868\) at \(n=2\).

The program additionally computes the formula for \(1\le n\le4\), \(1\le k\le3\), and \(q\in\{2,3,4\}\) to test integer and nonnegative coefficients. These parameter checks do not directly enumerate all \(\mathbb F_3\) or \(\mathbb F_4\) algebra maps. No finite check proves the all-field theorem: that conclusion follows from the short-exact-sequence splitting, the shared-shear normal form, and the exact dimension of the intertwiner space. No independent mathematical audit or external certification has been performed.
