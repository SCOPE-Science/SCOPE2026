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

# Reproduction

Run `OPENBLAS_NUM_THREADS=1 python blocking_cubic_classify.py` (Python 3, NumPy). It enumerates all \(59048\) nonzero ternary cubics, all thirteen projective points and lines, and all \(9880\) blocking forms, then tests simultaneous vanishing of each polynomial and its three derivatives at every projective point over \(\mathbf F_9\) and \(\mathbf F_{27}\). It returns \(1872\) smooth forms, \(936\) projective equations, one orbit of size \(936\), projective stabilizer order \(6\), and rational line-intersection spectrum \((6,3,4)\). Compare with `enumeration_output.txt`.

Run `OPENBLAS_NUM_THREADS=1 python blocking_cubic_groebner.py` (Python 3, SymPy). This separately enumerates the same coefficient space and checks Jacobian-unit ideals in all projective patches directly. Compare with `groebner_output.txt`; it returns the same \(9880\) and \(1872\) counts, with six rational points in all smooth blocking cases.

Both scripts were executed successfully with their bundled outputs; the second independently verifies smoothness rather than relying on extension-point searches. The extension-field method is exhaustive only together with the separately proved closed-point degree bound for singular cubics. No independent review of the proof or programs is claimed.
