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

The exact finite checks use the included standalone `verify.py` with Python 3 standard library, with no cached matrices or external data. Invoke `python verify.py` from the extracted package directory.

The verifier enumerates every simplex of the open-neighborhood complex via its support criterion at ground-set sizes 7 and 8. These have respectively 421 and 54,475 faces including the empty face. It computes the signed Lefschetz contributions of every invariant simplex for every permutation conjugacy class, using the orientation sign induced on simplex vertices. Both sizes satisfy the claimed formula on all 15 and 22 classes.

Independently, a recursive Murnaghan–Nakayama character computation confirms that the proposed three Specht modules give the claimed trace for every cycle type at ground-set sizes 7 through 11. The horizontal-strip Pieri identity is checked over those sizes. An actual run produced `SPECHT_OK` five times, `DIRECT_LEFSCHETZ_OK` twice and `VERIFY_OK`.

The universal mathematical proof does **not** rely on these finite cases: it rests on a signed fixed-face count, Boolean Möbius inversion on permutation cycles, and the standard Pieri rule. Published homology concentration for ordinary Kneser neighborhood complexes is cited as an input, not independently re-established here. No independent external audit has been performed.
