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

# Reproducibility and limitations

Run `python3 checker.py` from a directory containing the bundled checker. Its expected last line is `INCIDENCE_SPLIT_TUPLE_POTTS_OK 32 5625`.

The checker enumerates the full incidence-algebra matrix coordinate spaces for the specified small finite fields and posets. It evaluates \(f_S(a)\) as an actual product of matrices and computes commutation for every ordered pair that satisfies the polynomial constraint; this directly checks the claimed tuple count against a separate enumeration of graph labelings.

There are 32 exhaustive configurations covering two and three roots, one and two tuple coordinates, fields of orders \(2,3,5\), and multiple poset shapes. In the largest reported tuple count, 5,625 commuting ordered pairs occur for the three-root polynomial on a fork poset over \(\mathbb F_3\).

The code exhausts only the stated small finite cases; it is not an exhaustive check over all finite fields or posets. The proof in `RESULT.md` supplies the unrestricted argument using simultaneous spectral idempotents and unitriangular orbit–stabilizer counting. No independent audit has been performed.
