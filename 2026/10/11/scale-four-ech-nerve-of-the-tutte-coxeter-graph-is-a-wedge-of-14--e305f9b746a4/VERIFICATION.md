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
# Reproducibility and verification

Run `python3 verify.py` in a standard Python 3 installation. The program constructs the point–line incidence graph of the smallest symplectic generalized quadrangle from the alternating form on \(\mathbb F_2^4\). It checks the 15 points, 15 lines, 45 edges, generalized-quadrangle axiom, diameter four and girth eight, then enumerates every nonempty subface of every closed graph-distance-two neighborhood.

The exact face vector is `(30, 435, 2620, 5625, 7290, 6255, 3600, 1350, 300, 30)`, totaling `27535` nonempty simplices. The deterministic vertex-toggle matching pairs `13695` face incidences, leaves critical cells `{0: 1, 2: 144}`, and is checked for directed acyclicity across all `144210` Hasse incidences. Independently computed mod-two ranks are `{1: 29, 2: 406, 3: 2070}`, and Euler characteristic is `145`.

A successful invocation prints `VERIFY_OK`. The homotopy proof relies on the *complete* acyclic matching, not on extrapolation from a truncated search or on field-dependent Betti numbers. The included certificate proves only the specified finite graph at scale four; no homotopy statement for arbitrary generalized quadrangles or persistence boundary maps is claimed. Independent audit has not been performed.
