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

The proof is analytic. Its critical checks are:

1. Use the published exact square dispersion relation to write each high-energy gap edge as a scalar root near \(k=m\pi/\ell\).
2. Expand both roots through order \(m^{-3}\). After conversion from momentum to energy, the \(m^{-1}\) energy-width contribution vanishes and the first correction is \(-8\ell/(3\pi^2m^2)\).
3. For the hexagonal relation, impose the two extremal Bloch values \(d=-1\) and \(d=3\), expand all four nearby roots, convert to energy, and add the two band widths. Again there is no \(m^{-1}\) term; the first correction is \(8\ell(4-3\sqrt3)/(3\pi^2m^2)\).
4. Since \(\sum m^{-2}\) converges and the number of Neumann centers below energy \(K\) is \(\ell\sqrt K/\pi+O(1)\), the cumulative remainder is bounded. A terminal partially cut cell has bounded width and changes only the \(O(1)\) term.

The included `verify.py` uses only the Python standard library. It solves the exact boundary equations by bisection for several values of \(\ell\) and large \(m\), then verifies the displayed second-order asymptotics and the expected \(m^{-4}\) residual scale. It prints `VERIFY_OK` on success.

Limits: finite numerical checks do not prove the asymptotic theorem; the Taylor expansion and summability argument above do. No independent audit has been performed.
