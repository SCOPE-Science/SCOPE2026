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
# Verification of the sharp orbit-count maximum law

Run `python verify_orbit_lattice.py` with a standard Python interpreter (only standard-library modules are imported). The checker enumerates all ordered set-block compositions for dimensions \(1\) to \(7\), arities \(1\) to \(7\), and integer exponents \(1\), \(2\), and \(3\). For each choice it verifies the exact binary Jensen cost certificate for every binary input and an attaining family of disjoint orbit indicators. The test output contains \(229{,}362\) exact certificate comparisons and \(2{,}667\) exact witness identities.

These checks do not enumerate all invariant lattice functions, all permutation groups or the continuum of exponents. They verify critical algebraic ingredients on finite instances. The universal inequality follows from the independent analytic orbit-averaging proof in `RESULT.md`; its use of the established source norm representation is explicit. The infinite-exponent case uses the supremum norm of the free AM-space. No independent audit has been performed.
