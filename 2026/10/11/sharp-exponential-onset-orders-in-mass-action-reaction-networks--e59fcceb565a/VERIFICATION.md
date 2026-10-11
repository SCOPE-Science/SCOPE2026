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

## Analytic checks

The exact decomposition \(\dot c_i=P_i(c)+c_iQ_i(c)\) is obtained by separating reactions with zero input stoichiometry for species \(i\). On every compact solution interval, \(Q_i(c(t))\) is bounded. Its integrating factor is positive and equals \(1+O(t)\) near zero, so it cannot alter the first positive exponent from \(P_i\). Polynomial ODE analyticity, nonnegative products and strictly positive constants establish the leading term and prevent cancellation. The min-plus recurrence is finite because productive dependencies strictly decrease the integer exponent. A closure-level induction gives \(H_\ell\le 1+mH_{\ell-1}\) and the sharp chain attains equality for every length.

## Exact finite calculation

Run `python activation_checker.py` using the Python standard library. The checker constructs Taylor series through degree ten using `fractions.Fraction` for 140 deterministic random reaction systems (including missing initial species, inflows, nonlinear production, and consumption). It verifies zero coefficients preceding each predicted onset degree and verifies the predicted positive leading coefficient. It separately evaluates 12 exact serial networks with reactant molecularity \(m=1,2,3\), each for chain lengths \(s=1,2,3,4\). The observed output was `PASS: 152 exact rational checks; sharp chains for m=1,2,3 and s<=4`.

## Limits

The finite checker is not an exhaustive proof of all network sizes and is not a certificate of independent scientific audit. The universal theorem is mathematical, proved in `RESULT.md`. No claim is made that numerical threshold crossing occurs at a universal time independent of rate constants. Source overlap comparisons distinguish the new formula from qualitative closure, perturbation-pulse propagation, and tropical equilibrium balancing; an unindexed equivalent prior result cannot be absolutely excluded.
