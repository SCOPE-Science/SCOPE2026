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

The standalone standard-library verifier is `verify.py`, which must be run in a directory containing `flag_flip_certificate.json`. It checks graph6 decoding, manifold links, absence of four-cliques, and every one of the 30 candidate edges of both complexes using the proved flag-flip neighborhood criterion. It reconstructs every flipped graph, tests all nine explicit isomorphism witnesses, independently enumerates every graph automorphism using backtracking, and confirms each family of legal flips is one orbit. Executed check: `python3 verify.py` produced `VERIFY_OK {'G1': (5, 10), 'G2': (4, 8)} single_flip_orbit_sizes {'G1': 5, 'G2': 4}`.

The finite certificate is an exhaustive computation on the explicitly specified eleven-vertex complexes. The theorem's completeness across isomorphism types additionally uses the cited eleven-vertex graph census and the elementary connected-complement argument; the verifier does not repeat that billion-graph census. Publication date, scholarly novelty, and external mathematical review are not certified by the checker. Independent audit has not been performed.
