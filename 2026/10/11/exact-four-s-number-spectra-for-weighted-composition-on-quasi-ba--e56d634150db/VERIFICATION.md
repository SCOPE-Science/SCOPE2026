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

# Verification and limits

The analytic proof is given in `RESULT.md`. For \(0<p\le1\), the elementary inequality \(|a+b|^p\le|a|^p+|b|^p\) establishes the decisive column-dominance lemma. If \(j\) disjoint unit columns all admitted approximants in a target subspace of dimension less than \(j\) at distance below one, the approximant matrix would have strictly column-dominant block \(p\)-masses and hence linearly independent columns, a contradiction.

The four minimax formulae are applied directly to selected coordinate blocks; no Hilbert adjoints, metric quotient duality, or inaccessible theorem is assumed. The generalized order statistic is defined by a supremum over finite sets and therefore does not presuppose an attained \(j\)-th largest value.

Run `python3 VERIFY.py` in the same directory; only the standard library is required. Observed output:

`VERIFY_OK exact_dominance_profiles=130 finite_fiber_identities=420 noncomplemented_p_checks=3 proof_is_analytic=True`

The script checks rational finite examples and sampled identity cases; it is neither exhaustive over parameters nor a substitute for the infinite proof. No external or independent audit has been carried out. Inaccessible complete text of the original 2023 sequence-space paper leaves a limited literature-comparison risk.
