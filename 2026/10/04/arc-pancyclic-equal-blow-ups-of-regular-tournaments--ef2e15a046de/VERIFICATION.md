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

The universal theorem is proved analytically in `RESULT.md`. The finite verifier is a stress test of the construction, not a substitute for the proof.

`verify.py` builds cyclic regular tournaments of orders \(5,7,9,11,13\) and Paley regular tournaments of orders \(7,11\). For every base arc it independently searches for a containing directed cycle of each base length, then for every \(1\le\alpha\le4\) and every target \(3\le\ell\le c\alpha\) it:

1. finds \(k\le\alpha\) with \(3k\le\ell\le ck\);
2. decomposes \(\ell\) into \(k\) integers in \([3,c]\);
3. lifts the corresponding base cycles into distinct clone layers;
4. verifies that the resulting vertex sequence has exactly \(\ell\) distinct vertices, every successive pair is an arc, the last vertex points back to the first, and the first arc is the prescribed lifted arc.

The verifier also checks regularity of each base tournament and of the equal blow-up degree formula. It does not enumerate all regular tournaments of arbitrary order and does not prove Alspach's theorem; those are outside the role of this finite check.
