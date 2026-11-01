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

Exact, reproducible arithmetic checks use `python3 verify.py` and `c++ -O2 -std=c++17 verify_level7.cpp -o verify_level7 && ./verify_level7` in the same directory. The script enumerates every coefficient triple for moduli \(2^k\) with \(1\leq k\leq6\) (299592 cubics) and each square-root target for \(1\leq k\leq9\), independently of the symbolic recurrence. It checks 24 dyadic cubic distribution levels for normalization, mean-one identities, maximum-root formulas, and the exact number of extremizers. Recorded output of the bundled Python checker:

`VERIFY_OK direct_moduli=6 direct_cubics=299592 quadratic_moduli=9 recurrence_levels=24 exact_integer=yes max_cycle=2,3,5`

All integer equalities are exact. Finite enumerations corroborate, but do not prove, the unrestricted statement. The proof in `RESULT.md` covers every positive exponent and supplies the independent infinite argument.

Recorded output of the C++ checker:

`VERIFY_OK modulus=128 cubics=2097152 max_roots=32 extremizers=512 exact_integer=yes`
