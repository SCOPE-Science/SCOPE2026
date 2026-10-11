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
The proof is symbolic and covers every finite nonempty simplicial complex. The finite verifier is an independent sanity check of the definitions, not evidence for extending a finite experiment to the general theorem.

`verify.py` enumerates every labeled simplicial complex on one through four declared vertices. It computes total domination directly from its witness definition and tests \(r\)-conicity independently by enumerating supported subcomplexes and closed-star containment. It checks all \(126\) complexes and all relevant \(r\). It separately checks \(144\) ordered join pairs drawn from all complexes on at most three vertices and verifies exact total-domination additivity, including cone cases.

The recorded output is:

`LABELED_COMPLEXES_CHECKED {1: 1, 2: 2, 3: 9, 4: 114}`

`JOIN_PAIRS_CHECKED 144`

`JOIN_1_S0_TOTAL_DOMINATION=2 EXPECTED_CONICITY=1`

`JOIN_2_S0_TOTAL_DOMINATION=4 EXPECTED_CONICITY=3`

`JOIN_3_S0_TOTAL_DOMINATION=6 EXPECTED_CONICITY=5`

`JOIN_4_S0_TOTAL_DOMINATION=8 EXPECTED_CONICITY=7`

`EXHAUSTIVE_EQUIVALENCE_OK`

Limits: the verifier checks only small finite complexes; the unrestricted conclusion rests on the proof in `RESULT.md`. The original Aharoni--Berger article was not available as verified full text through the attempted routes, so its definition was checked via the later thesis source that explicitly attributes and states it.
