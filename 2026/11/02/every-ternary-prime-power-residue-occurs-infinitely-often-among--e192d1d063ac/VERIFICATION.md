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

Run `python3 verify.py` in the directory containing the accompanying documents. No third-party Python modules or downloaded mathematical data are necessary.

The executed verification printed:

```text
VERIFY_OK prime_power_levels=1..7 separated_block_checks=1008 direct_Catalan_checks=2800 full_residue_levels=1..5 total_residue_targets=363
```

The script directly compares the modular factorial-unit implementation with 2,800 exact Catalan integer values, checks the block-factorization and valuation formulas in 1,008 cases, checks unit generation for the indicated levels, and enumerates the full prescribed residue set modulo \(3^k\) for \(1\le k\le5\). It checks different block separations to guard against hidden dependence on digit positions.

These finite tests are checks, not proofs for all exponents. The proof's critical unrestricted steps are the factorial-unit recurrence, nonoverlapping length-\(k\) windows and carry counts, the congruence \(c_k\equiv2\pmod9\), and multiplicative generation of the unit group modulo all \(3^k\). The paper-based originality comparison is not an independent mathematical audit.
