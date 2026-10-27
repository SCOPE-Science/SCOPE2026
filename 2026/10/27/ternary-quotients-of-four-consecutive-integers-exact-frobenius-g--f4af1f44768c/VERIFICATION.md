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

Execute `python3 verify.py` in this directory using Python 3. The script has no nonstandard dependencies. It checks both cases \(r\in\{1,2\}\) at every \(3\le x\le800\), testing the proposed Apéry representatives, all generator-edge maximality comparisons, predicted genus, type, and Frobenius number (1596 parameter pairs). For every \(3\le x\le90\), it also constructs direct membership from the independent integer interval test \(\lceil3n/(a+3)\rceil\le\lfloor3n/a\rfloor\), checks minimal residue representatives, and enumerates all gaps and pseudo-Frobenius elements (176 parameter pairs).

Recorded output:

```
APERY/PF/GENUS/FROBENIUS: PASS: 1596 parameter pairs, x=3..800
DIRECT MEMBERSHIP AND GAP TESTS: PASS: 176 parameter pairs, x=3..90
```

The infinite mathematical proof is in `RESULT.md`; the finite verifier cannot certify an infinite assertion or publication priority. No independent mathematical audit has been performed.
