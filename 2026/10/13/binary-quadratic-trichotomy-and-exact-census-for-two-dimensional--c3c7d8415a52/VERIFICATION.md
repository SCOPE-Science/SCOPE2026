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
# Reproducible checks and limits

The accompanying `verify.py` uses Python 3 standard-library arithmetic. Running `python verify.py` enumerates all symmetric multiplication structures on the two-dimensional vector spaces over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\) with surjective multiplication. The nonprime field is implemented as \(\mathbb F_2[z]/(z^2+z+1)\). The script computes projective kernel types, explicitly searches all invertible ordered basis pairs for zero mixed products, and checks the coefficient formulas defining a three-dimensional evolution algebra with the desired stabilized square.

Expected by field order: \(q=2\) has \((18,18,6)\); \(q=3\) has \((288,192,144)\); \(q=4\) has \((1800,900,1080)\); \(q=5\) has \((7200,2880,4800)\), in order split, repeated, irreducible. The program raises an exception for any failed comparison and prints `VERIFY_OK` when all pass.

Computations are exhaustive over these four fields, not all fields or all prime powers. The proof in `RESULT.md` establishes the general statements independently. The cited embedding paper was available only in abstract during the literature comparison; unrecognized historical overlap is possible. No independent audit was conducted.
