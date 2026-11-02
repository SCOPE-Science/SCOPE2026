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

## Verification state

The exact nilpotency claim was checked against the explicit differential \(\omega=x^{p^{t-1}b-1}y^{p^{t-1}}dx\), the monomial Cartier transformation, and the cited maximal-curve upper bound. Its central nonzero identity is \(\mathcal C^{tn-1}(\omega)=-dx\). No independent audit is represented.

## Exact-arithmetic reproducibility

Execute `python3 verify.py` with Python 3 standard library. The included program enumerates all holomorphic monomial differentials for the twelve parameter triples `(p,t,n)` in its `main` function; independently derives the Cartier arrow, checks all nonzero images remain regular, verifies its coefficient never vanishes modulo \(p\), calculates every monomial's terminating chain length, and checks that the proposed witness has terminal output \(-dx\) after exactly \(tn-1\) applications. The packaged run returned `VERIFY_OK`.

## Proof boundaries

The computation is exhaustive only for the twelve explicit finite instances; the proof for all primes and all exponents consists of the symbolic chain and the known maximal-curve bound in `RESULT.md`. No finite computation establishes absolute literature priority or determines all intermediate Cartier ranks. The external source on maximality is used with attribution; no source's complete article is redistributed.
