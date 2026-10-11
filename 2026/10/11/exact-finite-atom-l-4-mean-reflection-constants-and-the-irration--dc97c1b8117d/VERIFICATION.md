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

# Mathematical verification and limitations

Run `python CHECK.py` in the package directory. The checker uses only the Python standard library, expands exact integer-polynomial identities for the rational two-value norm functions, checks the general differentiation factorization for dimensions \(3\) through \(39\) as a **diagnostic**, verifies every needed eight-atom branch identity and the four-atom factorization, brackets the unique negative root of the defining quartic with rational endpoints, and prints its high-precision norm approximation. Its final status is `EXACT_IDENTITIES_OK`.

The universal assertion over all \(n\ge2\) follows mathematically from the externally established symmetric quartic half-degree principle and the displayed symbolic binomial identity; a finite computer sweep by itself is not a proof of that universal statement. The sharp universal bound is proved analytically from Pearson's inequality and its equality case, followed by a rational-atom obstruction and an explicit rational approximation argument. The code does not claim exhaustive testing of continuous inputs or independently certify the published reduction theorem.

The scope is real \(\ell_4^n\) and the single mean-reflection involution \(I-2E\), not complex \(\ell_4\), arbitrary atom weights, or the simultaneous unconditional constant for a Haar system. Historical coverage in incompletely inspected projection literature remains an originality risk. Only a same-model mathematical review has been performed; no independent audit or validation is claimed.
