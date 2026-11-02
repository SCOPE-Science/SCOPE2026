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

The self-contained script `verify_affine_coverage.py` reconstructs the relevant evaluation generator columns and their affine-linear dual, so it does not rely on a precomputed matrix or a downloaded code package. Run `python3 verify_affine_coverage.py` from the directory containing the script. The success marker is `AFFINE_COVERAGE_VERIFY_OK`.

The verifier independently enumerates all binary subsets for \(m=3\) and \(m=4\), checks affine independence counts, and compares the exact spanning-set census. At \(m=4\) every one of the \(2^{16}=65{,}536\) subsets is checked against the matroid-duality rank equality. Separate absorbing-state recurrences check \(\mathbb E T_3=115/21\) exactly and \(\mathbb E T_4=172043/9009\) numerically to tight tolerance. The exact rational finite-law identities are checked for each \(3\le m\le12\); convergent series defining the limiting constant agree numerically.

The proof is independent of finite tests: it establishes the binary Reed–Muller dual identity, affine-independent subset formula, sampling CDF and expectation, an explicit geometric tail estimate, and the resulting sharp asymptotic via dominated convergence. Numerical computations do not certify convergence or publication priority by themselves.

Scientific limits: only full-rank recovery under uniform independent noiseless coordinate sampling is considered; no optimality among all linear codes is asserted. Independent mathematical validation has not been performed.
