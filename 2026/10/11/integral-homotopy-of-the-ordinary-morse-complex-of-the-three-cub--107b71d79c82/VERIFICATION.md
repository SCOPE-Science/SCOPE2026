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
# Verification and reproducibility

Run `python3 verify_homotopy.py` using Python 3.10 or later. The program reconstructs graph edges, 24 primitive incidence choices, all faces, the deterministic matching, directed Hasse graph, the integral 44-by-179 Morse degree matrix, and elementary unimodular reduction. Its independent direct simplicial mod-two ranks are checked in all dimensions. No external libraries or downloaded datasets are required.

Expected successful final line begins with `CUBE_MORSE_HOMOTOPY_VERIFY_OK` and reports 23,625 faces including empty, 11,701 reduced matching pairs, critical cells one in dimension zero plus 44 in dimension five and 179 in dimension six, 124,200 augmented Hasse incidences, forty integral unit pivots, and the sphere decomposition \(\bigvee^4S^5\vee\bigvee^{139}S^6\). The actual replay matched all counts, with mod-two augmented boundary ranks \((1,23,217,1079,3001,4487,2933)\). An independent Smith-normal-form library computation on the generated integer matrix returned precisely forty unit invariants.

Finite exhaustiveness applies solely to the specified cube graph. The review is internal to the mathematical package; no independent audit or external validation has been performed. The full directed-forest thesis identified in the references remained inaccessible at comparison time.
