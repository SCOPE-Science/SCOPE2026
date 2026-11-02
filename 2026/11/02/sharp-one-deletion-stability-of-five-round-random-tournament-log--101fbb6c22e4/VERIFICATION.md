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

# Verification and reproducibility

The exact calculations use the standard library of Python 3 only. Invoke `python3 verify.py > verification_output.json` and `python3 crosscheck.py > crosscheck_output.json` from the directory containing the four named files. The output files are included with this package. Both programs independently enumerate all \((p-2)(p-3)/2\) normalized four-sets, evaluate all 16 orientation prescriptions, and report the exact smallest number of witnesses for every prime \(p\equiv3\pmod4\) between 7 and 211 inclusive (24 primes). The first implementation intersects bit masks, whereas the second constructs scalar orientation codes vertex by vertex.

The two programs agreed on all 24 minima, with minimum 0 or 1 below 107, minimum 2 at 107, and minimum at least 2 for every eligible prime 107–211. An explicit attaining normalized quadruple at 107 is \(\{0,1,3,32\}\), with the witness pattern and two witnesses recorded in the outputs. Source code checks the finite-field square table for prime fields.

Completeness of the finite census rests on the **mathematical** affine-square normalization proven in `RESULT.md`. The nonprime field \(\mathbb F_{27}\) is ruled out by \(27-4<2\cdot16\), not by either program. All fields of order at least 223 are handled by the stated Weil-bound proof. The executable programs are finite verifiers and do not certify that external character-sum theorem, nor do they amount to an independent mathematical review.

Independent mathematical audit has not been performed.
