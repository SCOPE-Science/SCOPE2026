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

The derivation uses Mostovoy's complete rational homology classification in arXiv:2603.01439v1 and independently computes the reflection action. For each fixed finite subset, separate equatorial singleton orbits from off-equator two-orbits. Apply generalized-binomial compact-support Euler counts to the corresponding unordered configuration spaces. The two exact generating functions reduce to \(1+z^2\) in even dimensions and \((1+z)^2/(1+z^2)\) in odd dimensions. Comparing their coefficient sums with the Lefschetz traces determines the odd-dimensional character; the even-dimensional top orientation fixes one sign and Lefschetz fixes the other. Exactness of rational invariants determines the quotient ranks.

## Executable checks

Run `python verify.py` with Python 3 standard library only. Observed output: `VERIFY_OK cases= 2193`. The checker independently constructs generalized binomial coefficients, sums all exact-cardinality fixed-subset Euler counts and verifies predicted traces and quotient Euler characteristics for every integer \(2\le d\le18\) and \(2\le n\le130\), including every parity and residue boundary. It is finite corroboration, not a substitute for the all-parameter identities.

## Independent mathematical cross-checks

When \(d=2\) and \(n=2\), the complex is \(\mathbb{CP}^{2}\), and a degree-minus-one involution of the underlying \(S^2\) acts by \(-1\) on the second homology and by \(+1\) on the fourth, in accord with the formula. The total Euler characteristic from Mostovoy is three for even \(d\) and zero for odd \(d\), matching the ordinary finite-subset configuration series \((1+z)^{\chi(S^d)}\). Reflection quotient Euler characteristics satisfy Burnside's identity.

## Limits

No integral torsion, homotopy-group, or homotopy-equivalence claim has been verified. Independent audit has not been performed. The closest relevant published full texts were inspected to the extent listed in the associated scientific review; one related Euler-characteristic source was available only by abstract.
