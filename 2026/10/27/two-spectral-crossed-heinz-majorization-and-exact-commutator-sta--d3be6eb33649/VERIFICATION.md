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

# Reproducibility and scope of verification

Run `python3 verify_heinz.py` from the extracted package. It requires Python 3 and its standard library only. It reconstructs the crossed and ordinary matrices independently from rational projection data at exponents \(t\in\{1/4,1/2,3/4\}\), using two different positive eigenvalue pairs, and confirms **486 exact rational** identities for the squared Frobenius defect in dimensions two, three, and four. It also checks **972** Ky Fan inequalities for one and two principal-angle blocks using floating-point evaluation of singular values of explicit real two-by-two matrices. All exact rational identities use `fractions.Fraction`; the numerical checks have a stated rounding tolerance.

The optional `verify_random.py` uses NumPy to check further randomized complex spectral projection pairs in dimensions two through eight, for 840 cases with different positive levels and exponent parameters. Its floating-point results are diagnostic, not rigorous certificates of weak majorization.

The infinite family is proved in `RESULT.md` using the two-by-two singular-value formula and an explicit finite-dimensional decomposition of a pair of projections into one- and two-dimensional blocks. The commutator coefficient is proved exactly by a trace expansion, independently of the numerical tests. The published dimension-two theorem is credited; the random tests do not certify novelty, priority, or general correctness on their own.

No independent scientific audit has been performed.
