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

# Verification

The standalone `VERIFY.py` script uses only the Python standard library. Run `python3 VERIFY.py` in the directory containing the science files. Expected final output is `VERIFY_OK: exact 14-state transfer, characteristic polynomial, cyclic words,` followed by `independent rational active-basis enumeration, and endpoint comparisons.`

It directly constructs the transfer adjacency from the four symbol rules, obtains the characteristic polynomial by integer Newton identities, and checks \(F_m=\operatorname{tr}(T^m)\) against independent exhaustive word enumeration for \(3\le m\le8\). It then enumerates vertices from arbitrary independent active inequality bases over exact rational numbers at \(r=3/4\), for \(m=3,4,5\), and compares the entire vertex sets with the four-letter construction. Endpoint checks use independent base enumeration and the known unweighted three-label criterion.

The nontrivial infinite statement rests on the complete tight-graph proof in `RESULT.md` and the finite exact symbolic determinant, not on extrapolating finite cases. This is same-model technical verification only; independent mathematical audit is not performed.
