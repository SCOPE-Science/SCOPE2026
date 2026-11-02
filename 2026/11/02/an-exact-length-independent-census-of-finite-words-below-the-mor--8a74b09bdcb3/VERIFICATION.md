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

# Reproducible checks

Run `python3 verify.py` with a standard Python 3 interpreter; no packages or network access are needed. The exact expected final line is `VERIFY_OK`. The included `verify_output.txt` records the output of a successful execution.

The program evaluates primitive-word counts using Möbius inversion, verifies the boundary-fringe convolution and its rational generating-function coefficients, and directly enumerates all short words for 35 parameter triples. It independently generates normalized primitive-core tuples for 47 further triples and checks that these tuples are unique, satisfy the factor-complexity condition, and have the predicted cardinality. The direct checker uses literal factor sets, rather than the claimed normal-form classification.

The unrestricted result depends on the published finite Morse–Hedlund theorem and the periodic-center uniqueness proof. Finite tests do not establish the infinite quantifiers. Publication priority and independent audit remain unverified.
