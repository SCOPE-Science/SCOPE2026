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

# Mathematical verification

The derivation uses the published multiplicative Markov–Krein existence/uniqueness and the stated generalized Cauchy transform identity. The novel computations are the all-integer polylogarithm quotient, endpoint residue evaluation, and two-sided asymptotic inversion. The open-interval density follows by local Stieltjes inversion; the nonzero imaginary part of each denominator's cut value excludes interior poles. The endpoint mass identity and no-atom-at-one check exclude singular endpoint terms.

The provided `verify.py` program (run after `python -m pip install -r requirements.txt`) was executed and returned: `PASS: 45 numerical checks; polylog transform, first moments, density positivity and endpoint asymptotics.` It checks three exterior transforms by direct integration against the second-power benchmark, the first three benchmark moments, positive-density evaluations for powers 2–6, and quantitative left/right asymptotic consistency. The k=2 benchmark is prior-covered and appears solely to validate analytic normalization. The program uses finite checks only and is **not** a proof of the all-power theorem. The proof is in `RESULT.md`.

No independent audit or external validation is represented by this document.
