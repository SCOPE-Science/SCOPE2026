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

The continuous-domain proof uses only exact algebra:

1. Since \(|\psi_r\rangle\) is normalized, \(\rho_N\) has eigenvalues \((1+3g)/4\) and \((1-g)/4\) with multiplicity three. This makes \(g\le1\) necessary and sufficient for positivity in the published entangled parametrization.
2. Substituting \(g=(1+r^2)/(3-r^2)+\epsilon\) gives \(\epsilon\le2(1-r^2)/(3-r^2)\); solving instead for \(r^2\) gives the fixed-\(\epsilon\) cutoff.
3. Subtracting the two published fidelities yields the exact threshold \(p_*\).
4. Uniform strict dominance over all useful \(p\) is equivalent to \(p_*<0\). Comparing that lower epsilon requirement with the physical upper epsilon requirement gives \(r^2<1/2\), with a tie at the endpoint.

The included `verify.py` replays these identities using exact rational arithmetic, including the two source-figure epsilon values and one hundred comparison cases. Its finite checks are supplementary and do not establish the universal statements.

Scientific limit: the verification starts from the state and fidelity formulas as printed in the primary source; it does not independently reconstruct the full experimental or protocol derivation.
