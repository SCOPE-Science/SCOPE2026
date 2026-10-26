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

# Verification record

## Mathematical checks
The proof uses strict divisor-sum upper bounds to exclude all but the pairs \((5,7),(5,11),(5,13)\), proves weirdness at \(70\) by the excluded-sum obstruction, and supplies four exact complementary-divisor sets. Every other surviving case contains a certified semiperfect seed. Proper-divisor analysis proves seed primitivity. The inequality and inclusion arguments apply to all positive exponents; no finite exploration is substituted for these arguments.

## Standalone executable
Run `python3 verify.py` with Python 3 and the standard library. It recomputes each seed's divisor sum and excluded subset, directly tests all proper divisors of each seed for semiperfectness, checks \(70\) is weird, and independently compares all \(550\) parameter combinations in the bounded search with the predicted closed criterion. During package preparation the script returned:

`VERIFY_OK: four exact divisor-complement certificates; four primitive seeds; 550 independent finite semiperfect cases; unique weird instance 70 below 20000.`

## Limits
The finite test covers only the explicitly coded range and does not certify any assertion about arbitrarily large primes or exponents; the written proof provides that. Originality is a best-knowledge comparison against the inspected materials and cannot rule out an unlocated stronger historical classification. Independent audit has not been performed.
