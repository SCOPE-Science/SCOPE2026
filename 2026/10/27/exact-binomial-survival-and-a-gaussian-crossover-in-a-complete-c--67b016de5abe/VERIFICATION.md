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

# Finite-state verification and proof dependencies

Execute `python3 verify.py` using the standard library; no packages, input files or network are required. The program implements the full ecological update with exact `fractions.Fraction` arithmetic, independently derives actual iterates, and checks the predicted terminal occupied count and finite binomial full-survival census for every initial \(\{1,2\}\)-state at community sizes \(3\) through \(11\) and the listed rational couplings, excluding resonant instances. It also tests that every checked orbit is fixed or two-periodic from its second iterate. Recorded result: `PASS: 25560 exact rational initial states; finite binomial census and two-step entry into a fixed point or period-two orbit`.

Proof of the general finite-\(n\) assertion is the two-group case analysis in `RESULT.md`. The finite calculation is not a certificate for infinitely many sizes. The limiting mixture and mean invoke the ordinary De Moivre–Laplace central limit theorem for \(\operatorname{Bin}(n,1/2)\), the vanishing maximum binomial atom, and boundedness of occupied fractions. For resonant thresholds at most two initial counts depart from the exact generic case split; their combined mass is \(O(n^{-1/2})\). No claim is made for the exact finite-size law at resonant parameters.
