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

The verifier `artifacts/verify.py` reconstructs the claim from exact integer arithmetic.

It checks the following items:

- the source benchmark at \(n=41\), row \(90\), including saving \(23\cdot31\cdot47\), defect \(3\), and exclusion union \(\{22,29,30,44,45\}\);
- the exact global minima for every \(42\le n\le57\) over the finite row intervals supplied by the binomial lower-bound cutoff;
- at \(n=57\), the row-\(120\) value, saving \(41\cdot61\), and exclusion union \(\{39,40,60\}\);
- the exact global minimum among defect-at-most-\(1\) supports and the exact best prefix value at \(n=57\);
- an independent LCM-state dynamic program on row \(120\), omitting exactly four half-row entries, which returns the same row minimum.

The computation is a finite certificate, not an extrapolation. It does not establish any statement about \(\delta(n)\) for \(n>57\), and it does not enumerate every optimal support at \(n=57\).
