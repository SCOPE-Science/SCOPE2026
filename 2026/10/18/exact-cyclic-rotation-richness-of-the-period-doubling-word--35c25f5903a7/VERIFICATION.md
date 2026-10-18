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

# Reproduction and limitations

Run `python3 verify.py` with a Python 3 standard library. The script uses the exhaustive two-block substitution factor cover, not an arbitrary prefix cutoff. Its canonical cyclic-rotation routine forms exact classes and checks \(M(n)\) for each integer \(1\le n\le192\), the class-size doubling at applicable even lengths, and a three-rotation witness for every odd length in range. The observed final status is `VERIFY_OK 1..192 complete substitution-cover factor sets and all odd triple witnesses`.

This test is a finite cross-check. The proof in `RESULT.md`, including the odd-gap upper bound and even-distance two-one construction, establishes the all-length statement; no finite computation is used to extrapolate an infinite law. Full-text comparison with Bell–Shallit, arXiv:2102.03821, remains unavailable; the scientific originality claim is expressly bounded by inspected sources. No independent audit has been carried out.
