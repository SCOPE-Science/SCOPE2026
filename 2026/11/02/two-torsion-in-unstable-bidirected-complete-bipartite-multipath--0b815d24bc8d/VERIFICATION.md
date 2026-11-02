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
# Reproduction and limits

Run `python3 verify_moore.py` with Python 3. The program uses the standard library only, constructs every valid arc subset (all possible simplex dimensions), verifies simplicial down-closure and signed boundary-square zero, generates the matching from increasing arc indices, and validates all directed Hasse incidences in an independent graph-topological-sort check. Exact signed chain elimination yields the integral Morse differential; a separate original-boundary sparse rank computation uses prime fields two and three.

Expected essential outputs: at \(n=4\), face vector \((16,80,144,72)\), 151 matched pairs, critical cell counts \((1,0,8,1)\) and integral Morse differential content two; at \(n=5\), face vector \((20,130,320,240)\), 338 matched pairs, critical cell counts \((1,0,1,32)\) and integer matrix content two; at \(n=6\), critical counts \((1,0,0,169)\). Expected success marker: `BIDIRECTED_K2N_TWO_TORSION_UNSTABLE_MODULE_MOORE_VERIFIED`.

The original-boundary ranks over the two fields are an independent torsion consistency check, **not** an alternative proof of exact integral Smith invariants. The precise invariant factor two comes from the integral Morse matrices; the homotopy statement then uses the simply connected two-skeleton and degree classification of three-cell attachments. The dynamical-module minimality proof is separate mathematics under the definitions from the cited source. The package makes no claim of independent external audit, infinite enumeration or correctness of unexamined literature.
