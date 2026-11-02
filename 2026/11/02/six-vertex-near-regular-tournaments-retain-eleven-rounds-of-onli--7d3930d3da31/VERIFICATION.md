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

The included `verify_nearregular.py` and `nearregular_depth11_certificate.json` are sufficient for complete finite replay with Python 3.8 or newer and no nonstandard dependencies. Run them in the same directory using `python verify_nearregular.py`.

The checker reconstructs all \(2640\) score-feasible tournament encodings among the \(2^{15}\) orientations of the six-vertex complete graph; tests the trace cardinality on **every** of the \(2^{15}\) support masks; independently checks the cut-bound characterization on the same complete domain; classifies all maximum supports under the full \(720\)-permutation group; verifies every branch of the explicit \(2048\)-leaf depth-eleven tree; and recomputes the two- and four-vertex boundary cases.

A valid run prints `DIRECT_TRACE_PROFILE_PASS`, `CUT_CHARACTERIZATION_PASS`, `FIVE_MAX_SUPPORT_ISOMORPHISM_TYPES_PASS`, `ONLINE_CERTIFICATE_PASS`, `SMALL_EVEN_BOUNDARIES_PASS`, and finally `ALL_NEARREGULAR_TOURNAMENT_CHECKS_PASS`.

The polynomial and online lower bound are finite exhaustive findings, not inferences from incomplete experiments. The online upper bound follows from \(|\mathcal N_6|=2640<4096\). The general all-even cut characterization is proved separately via integral degree-constrained orientation feasibility. This package does not establish exact polynomial or online dimension at even order eight or larger. Independent mathematical validation is not included.
