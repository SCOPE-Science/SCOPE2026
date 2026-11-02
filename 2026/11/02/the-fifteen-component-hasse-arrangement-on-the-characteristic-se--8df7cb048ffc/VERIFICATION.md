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

The `verify_humbert7.py` program uses only Python's standard library. Execute `python3 verify_humbert7.py` from the directory containing the program. It checks the Legendre Deuring polynomial and its three roots over characteristic seven, all twenty marked rational parameters, the vanishing-indicator set for each of the five elliptic quotients, all ten pairwise intersection sizes, one complete branch-label orbit, fifteen irreducible components' finite incidences, and the three pairwise transverse local normals at one orbit representative.

The infinite-field completeness is not claimed from the program's finite sample: it is proved by the algebraic reduction of any two elliptic Hasse conditions to six solutions and the full branch-permutation symmetry. The quotient-to-Jacobian prime-to-seven isogeny is proved via finite two-group projectors and the cited Humbert–Edge decomposition. The external independent audit remains unperformed.
