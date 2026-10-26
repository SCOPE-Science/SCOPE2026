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

# Reproducibility and evidence limits

Run `python3 verify.py` from the directory containing that file using Python 3. The program is self-contained and uses only the standard library.

For \(S_n\), \(2\le n\le6\), the verifier constructs all permutations and the alternating-subgroup conjugacy orbits, compares their count to ordinary partitions plus partitions into distinct odd parts, and checks the resulting quandle operation for all representatives and all four-variable medial identities. For \(3\le n\le5\) it enumerates every bijection on the quotient set and compares the true automorphism count against the stated wreath-product factorial formula.

For \(D_{2m}\), \(3\le m\le16\), the program uses an explicit multiplication and inverse law on pairs representing rotations/reflections. It constructs derived-subgroup conjugacy orbits, checks representative-independence, checks the entire four-variable medial law, and checks each of the four closed operation formulas and the cardinality.

Expected terminal line: `VERIFY_OK`.

These are finite reproducibility checks. They are neither proofs of the claims for unbounded dimensions nor independent certification. The mathematical proof is given in `RESULT.md`. The exact literature-comparison limits are recorded in `REVIEW.md` and `AUDIT.json`. No external audit has been performed.
