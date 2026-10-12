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

Run `python3 verify.py` beside `certificate.json`.

The verifier treats a factor of length \(L\) and period \(p\) as forbidden exactly when
\[
3L>7p.
\]
This is strict, so factors of exponent exactly \(7/3\) are allowed.

Route A generates all Dyck prefixes while pruning exactly when the newly appended symbol creates a forbidden suffix factor. Route B independently enumerates every Dyck word of nesting level at most \(4\) without repetition pruning and then tests every factor against every possible period. The routes agree on the complete level-\(4\) survivor slice from length \(8\) through \(24\).

The certificate records the survivor counts by length and nesting level. In particular, level \(4\) has count zero below \(24\) and count one at \(24\). The verifier also confirms that the unique word is fixed by reverse-complementation and contains the exact boundary factor \(\mathtt{1001001}\) of period \(3\).

The check proves only the stated finite minimum and uniqueness claim. It does not address minimum lengths at nesting level \(5\) or above. Independent audit has not been performed.
