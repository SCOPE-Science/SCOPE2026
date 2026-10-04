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

The proof was checked at the level of the exact domain, assumptions, and finite combinatorics. The central uniformity statement uses only exchangeability and almost-sure absence of ties: a labeled total ordering is uniform, every calibration/future binary interleaving has the same \(n!m!\) labeled refinements, and binary interleavings are in bijection with weak compositions of \(m\) into \(n+1\) calibration gaps.

`verify.py` performs exact finite checks with no floating-point arithmetic. For \(n=4\), \(m=3\), it enumerates all \(7!\) labeled score orders and confirms that each of the \(\binom{7}{4}=35\) fine-gap compositions occurs exactly \(4!3!\) times. It then aggregates at ranks \((1,3)\), verifies the Dirichlet-multinomial mass function with parameters \((1,2,2)\), and verifies the empirical-coverage cross-covariance \(8/225\). A separate case compares the simultaneous-band dynamic program to brute-force weak-composition enumeration.

Reproduction command: `python3 verify.py`. Expected leading output: `VERIFY_OK`.

Limits: these finite checks validate the implemented formulas and representative combinatorics; the general proof is the bijective argument in `RESULT.md`. The verification does not establish literature priority. Nonexchangeable data or score ties outside an exchangeability-preserving tie-breaking scheme are outside the theorem.
