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

The proof checks the residue map modulo \(7\), the unique Hensel roots modulo \(49\), the exact multiplier orders and the first nonzero return displacement for all shells. The odd-prime Taylor lifting lemma supplies the infinite step. All basin masses follow by disjoint isometric inverse branches and the critical image \(f^3(7\mathbb Z_7)\subseteq5+49\mathbb Z_7\).

Run `python3 verify.py` in the directory containing the script. The test enumerates finite dynamics modulo \(7^k\) for \(k=2,3,4,5\), checks periods and multiplicities of all declared shell components and their finite preimages, and prints `Z7_QUADRATIC_MINIMAL_BASINS_VERIFY_OK` upon completion. Its recorded output appears in `verify_output.txt`. These finite tests are supplementary and do not constitute a proof for arbitrary \(k\). Independent audit has not been performed.
