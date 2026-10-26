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

The standalone Python 3 standard-library source `verify_coset.py` is included with this result, together with its exact output in `verification_output.txt`. Its brute-force layer enumerates all binary received words and all codewords independently of the polynomial construction at \((m,L)=(4,2),(4,3),(4,4),(6,2)\), then divides word counts by \(2^{m-1}\) to compute the number of cosets at each distance. All spectra agree coefficientwise with the polynomial formula. The deterministic formula layer additionally checks \(4\) even values of \(m\) and every \(L\) from \(2\) through \(12\) against the total coset count and radius/deepest multiplicity formulas, using exact integer arithmetic. Final output: `VERIFY_OK`.

These checks do not certify the statement for infinitely many parameters. The main mathematical proof is given in `RESULT.md`; no independent external audit has been performed. Full-text comparison with Solé–Zaslavsky (1993) remains an originality limitation; its covering-radius context is acknowledged, not appropriated.
