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

Run `python3 theta_singularity_checker.py` with ordinary Python 3 and no external packages. The code constructs all alternating monomial blocks for the three paths. For every projectively nonempty coordinate-zero pattern containing no more than five zeros it first checks whether the nonzero pattern of the \(2\times3\) monomial matrix is compatible with rank one; it computes the torus-stratum codimension and the exact integer Jacobian of its three defining minors at the all-ones representative of each nonzero coordinate. Exact two-by-two minors decide whether the Jacobian has rank two. The script asserts that there are no singular strata of codimension below three and that the codimension-three singular patterns have the claimed count.

The tested triples are \((1,1,1),(1,1,2),(1,1,3),(1,1,4),(1,2,2),(1,2,3),(1,2,4),(1,3,3),(2,2,2),(2,2,3)\). Their singular codimension-three counts are respectively \(0,5,27,84,20,64,161,144,63,161\). Exactly 6,793 nonempty compatible coordinate patterns are checked. The script emits `VERIFY_OK triples=10 nonempty_strata_checked=6793` upon success.

**Proof boundaries.** The finite checker is not used to extrapolate the infinite theorem; the proof uses a complete support-shape case distinction for all nonnegative integers \(r_i\). The analytic node reduction is proved symbolically at general points; the script does not independently compute completed local rings. The assertion concerns irreducible components of the singular **reduced locus** that have codimension precisely three, not the entire higher-codimension structure.
