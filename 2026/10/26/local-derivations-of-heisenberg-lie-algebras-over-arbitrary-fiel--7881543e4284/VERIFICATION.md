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

The symbolic verification checks the derivation identity on arbitrary pairs \(v,w\in V\), reduces it to the conformal-symplectic multiplier equation, and proves the local-map characterization by constructing a matching derivation for central and noncentral vectors separately. The dimension count uses \(\dim\mathfrak{sp}_{2n}=n(2n+1)\) and the center-preserving block form.

The standalone finite check `artifacts/check_h3_f2.py` completed successfully: it enumerates all \(512\) linear maps on the three-dimensional Heisenberg algebra over \(\mathbb F_2\), finding \(64\) derivations and \(128\) local derivations, equal to the count of center-preserving maps. This check is corroborative only; the general result is proved symbolically.
