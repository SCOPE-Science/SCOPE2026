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

# Reproducibility and limits

Run `python verify.py` with Python 3 and SymPy. The checker uses exact symbolic expansion and finite-field row ranks. It verifies the affine derivative numerator from a generic quadratic pair, produces explicit rank-three and rank-two examples in characteristic zero and primes three, five, and seven, checks the characteristic-two nonempty example including an inseparable component, and enumerates all degree-two maps over \(\mathbb F_2\) and every ordered triple thereof.

Observed output ends in `VERIFY_OK exact_checks_complete`. The characteristic-two finite enumeration finds \(24\) maps and \(9072\) unramified triples among \(13824\) ordered triples. The rank tests determine normal splitting only after the proven cohomology exact-sequence equivalence. Finite enumerations are not proofs for arbitrary algebraically closed fields, all positive characteristics, or infinite families.

The universal proof in `RESULT.md` separately checks differential sections and rank, degree and splitting alternatives, Serre-dual cohomology, basepoint-freeness, and the smooth irreducible determinant divisor via the quadratic-pencil \(\operatorname{PGL}_2\)-torsor. Public literature searches give best-knowledge originality only. No independent audit or external certification has been performed.
