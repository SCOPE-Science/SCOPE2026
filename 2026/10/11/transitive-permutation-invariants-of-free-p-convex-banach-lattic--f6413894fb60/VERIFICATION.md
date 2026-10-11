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

# Verification and reproducibility
The proof's identity \(\max_j\sum_r|v_{rj}|^p\le1\) is the exact weak-\(p\) admissibility condition for the free lattice over \(\ell_1^n\); it is not a heuristic relaxation. Transitivity makes each orbit-coordinate \(p\)-energy equal, proving the lower bound simultaneously for every unit dual vector. The order-statistic bound is the elementary exact inequality \(k s_k(u)^p\le\|u\|_p^p\), with an explicit equality witness. The disjoint ambient-AM counterexample uses the two admissible dual rows \(e_1,e_2\).

The companion `verify_orbit.py` requires only Python's standard library; run `python verify_orbit.py`. It enumerates short integer vectors, cyclic transitive orbits, and invariant examples, checking 14,109 exact rational/integer identities. It does not enumerate all dual tuples, all group actions, all exponents or continuous functions, and therefore does not prove the infinite families by computation. The analytic argument is self-contained once the standard free-lattice functional representation cited in RESULT.md is accepted. No independent audit has been performed.
