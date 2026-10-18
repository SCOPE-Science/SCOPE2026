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

# Verification of the stated theorem

The proof is analytic for each integer \(n\ge3\). The incidence identity and column calculation yield the upper bound exactly. Signed symmetric-group averaging sends an arbitrary projection to an equivariant one without increasing the norm, and the stabilizer argument shows the latter must be the displayed candidate. It therefore certifies the all-parameter lower bound, not merely its finite sampled values.

Run `python3 VERIFY.py` (Python 3.9 or later, standard library only). The executed checker constructed exact rational matrices for all \(3\le n\le12\), verified \(BQ=0\), \(Q^2=Q\), triangle-cycle fixation, every \(\ell_1\) column sum, and generator commutation for \(3\le n\le8\). Its observed final line was `VERIFY_OK exact comparisons= 59831`. Finite comparison is not a proof for unbounded \(n\); the proof in `RESULT.md` supplies that step.

No independent review or audit has been carried out. The computation is scoped only to matrix identities and supplies no literature novelty certificate.
