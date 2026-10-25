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

# Verification details

Run `python verify.py` with Python 3. The program requires only standard-library modules. Its output is saved in `verification_output.txt`.

The verification recomputes the entire cyclic block list and all tetrad incidences (unique coverage of 330 tetrads), all 1023 nonempty faces with size vector \((11,55,165,330,396,66)\), equality of the 66 free hexads with complements of blocks, and the unique free hexad extension of each nonblock pentad.

For discrete Morse acyclicity, it reconstructs 451 unique vertex-toggle matching pairs, explicitly enumerates every one of 4301 face-cover incidences, orients matched incidences upward and all other incidences downward, and topologically sorts all 1023 vertices of that directed graph. This eliminates any possible closed gradient path and gives a finite, exhaustive certificate.

No external solver, software dependency, precomputed certificate, or external mathematical judgement is needed to replay these finite calculations. The application of the standard discrete-Morse homotopy theorem to this finite matching is the sole topological deduction. No assertion is made about other Steiner-system parameters or independent verification.
