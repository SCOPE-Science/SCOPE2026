---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Independence gives velocity covariance g²σ² exp(−(a+b)|τ|)/4, so the covariance double integral and the independent Brownian variance give the same MSD. For the three consecutive gaps x,u,z, set M_c=exp(−c(x+z)) and N_c=M_c exp(−2cu). Wick gives M_c+2N_c after variance normalization for an OU variable, while independent flip increments give M_a for the telegraph force. Subtracting the three common covariance products gives the T cumulant kernel proportional to M_a N_b−N_a N_b, and G−T proportional to N_a M_b+2N_a N_b, with common prefactor g⁴σ⁴/8. Both are strictly positive on the interior of the ordered time simplex. The independent Brownian term contributes no fourth cumulant. Integrating the first time and the outer-gap split gives weight w(t−u−w) for w=x+z, and summing 24 orderings gives the prefactor 3g⁴σ⁴. Dividing by t, dominated convergence gives the common factor 3g⁴σ⁴/(2(a+b)²) times 1/b−1/(a+b) for T and 1/a+1/b+1/(a+b) for G. Their quotient is the claimed a²/(a²+3ab+b²). The original dimer's no-repulsion MSD and entropy calibration agrees with arXiv:2304.07738v1, Eqs. (2a), (11), (13), (17), (19), (S32)–(S37), including the factor two between flip and covariance-decay rates. Inspected verify_cumulants.py and its recorded checks as finite corroboration; the proof establishes the quantified claim without them.

## originality

PASS

The earlier identified sources cover the dimer, the MSD and entropy input formulas, four-time factorization rules and the Gaussian product-OU branch, not the two-protocol fourth-cumulant comparison. There is demonstrable equivalent coverage of the mathematical core in another Resultary record dated November 8, later than this frozen November 2 entry. This is a duplicate scientific statement across the records, not evidence that the later entry anticipates the frozen one. The pass is relative to the identified earlier literature and does not resolve provenance or endorse novelty of the result in the later entry.

## value

PASS

In a motivated exactly solvable nonequilibrium model, the entire MSD curve and stationary mean entropy production cannot distinguish the two calibrated protocols. The fourth cumulant separates them at every positive lag and gives a closed asymptotic ratio without nuisance amplitudes or readout diffusion. This is a usable ensemble discriminator, not a finite-sample detection guarantee, and is stronger than exhibiting a numerical or long-time-only difference.

The dated certificate retains the supplied scientific assessment, sources and limitations.
