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

# Reproduction and limitations

Run `python3 verify.py` with Python 3.8 or later. It uses only the standard library. It checks twelve prime-field parameter tuples, including all four twist-order strata in characteristic seven for a complement of order six. For groups of algebra dimension at most twenty it checks associativity for every ordered triple of basis monomials. In every case it separately factors the complement polynomial by exact trial division, computes orbit permutations by scaling roots, counts every composition factor in every projective layer, and compares the resulting integer Cartan matrix with the claimed formula.

The checker does not enumerate all finite extensions or every prime and does not, on its own, establish the theorem for arbitrary parameters. The general result is proved in `RESULT.md` using the radical filtration and Frobenius-orbit argument. Literature and database comparisons were also performed; they cannot exclude unidentified older treatments. No independent mathematical audit has been performed.
