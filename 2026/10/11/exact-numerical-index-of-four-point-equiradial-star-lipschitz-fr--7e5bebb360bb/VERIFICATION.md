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

# Reproduction and boundaries

The coordinate model and the two finite generating sets are displayed in `RESULT.md`. An exact symbolic verification follows the finite recipe: for each of the twelve signed molecules and fourteen signed dual potentials, retain pairs satisfying \(f(p)=1\) identically as a function of \(q\); evaluate \(f(Sp)\), clear denominators using \(1+3q>0\), and compare against the listed rational values. There are 48 retained pairs counting the redundant endpoint generator descriptions. All values are bounded by \(1\) analytically on \(0\le q\le1\). Independently, substitution in the explicit four-state decomposition confirms the universal operator-norm bound.

The underlying proof works for all real parameters, not just sampled values. Exact rational and numerical diagnostic tests were used to catch transcription errors; neither constitutes an infinite-parameter proof. The equation \(f(S(e_2-e_1))=R\) is the sharp operator-norm witness, whereas supported pairs give the numerical-radius bound. Independent mathematical validation has not been carried out.
