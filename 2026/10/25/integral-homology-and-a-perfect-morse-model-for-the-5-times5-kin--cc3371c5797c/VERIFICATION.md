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

Run `python3 verify_kings5.py` from a directory containing the unpacked files. The verifier uses only the Python standard library and requires no internet or precomputed matrices. Successful exact output is embedded in `verifier_output.txt`.

Its tests independently enumerate all 6,426 nonempty independent sets, count faces by dimension, construct every oriented simplicial incidence, check each maximal/free-facet Morse step, and topologically sort the entire matched-and-unmatched Hasse digraph. It then carries out 3,173 signed integer unit-pivot cancellations and checks that all remaining integral Morse boundary entries are zero. A separate mod-two Gaussian-elimination routine checks every simplicial boundary rank.

The exact critical dimensions are one 0-cell, 45 3-cells, 32 4-cells, and two 5-cells. Thus the integral groups have those three positive Betti ranks and no torsion. No external validation, proof assistant, or peer audit was performed. In particular, zero cellular boundary does not establish nullhomotopic five-cell attaching maps; no complete wedge decomposition is certified.
