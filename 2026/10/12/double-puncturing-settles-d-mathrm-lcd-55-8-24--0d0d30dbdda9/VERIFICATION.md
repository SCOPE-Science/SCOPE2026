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

Run:

```text
python3 artifacts/verify.py
```

The verifier performs the following exact finite checks:

1. Expand the eight hexadecimal source rows into binary, require the three appended padding columns to be zero, and remove them.
2. Reproduce row rank \(8\), Gram rank \(8\), and minimum distance \(25\) for the source \([57,8,25]_2\) code.
3. Enumerate all \(\binom{57}{2}=1596\) double punctures.
4. For every puncture, compute row rank and Gram rank over \(\mathbb F_2\); for every dimension-eight LCD puncture, enumerate all \(256\) codewords and compute the exact minimum distance.
5. Require exactly \(756\) LCD double punctures and exactly four LCD distance-\(24\) punctures, at coordinate pairs \(\{9,18\}\), \(\{10,30\}\), \(\{34,48\}\), and \(\{41,42\}\).
6. For the \(\{9,18\}\) witness, require the exact weight enumerator
\[
1+49z^{24}+98z^{26}+53z^{28}+9z^{30}+10z^{32}+28z^{34}+7z^{36}+z^{38}.
\]

These checks are finite and exhaustive for the stated parent representative. They do not enumerate inequivalent parent codes or all LCD \([55,8,24]_2\) equivalence classes.
